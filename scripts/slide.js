/**
 * BizAI Hub - Interactive Slide Deck Controller
 * Provides keyboard navigation, swipe gestures, progress tracking, and hash routing
 */

class SlideDeckController {
  constructor() {
    this.slides = Array.from(document.querySelectorAll('.slide'));
    this.totalSlides = this.slides.length;
    this.currentIndex = 0;

    this.prevBtn = document.getElementById('prevSlideBtn');
    this.nextBtn = document.getElementById('nextSlideBtn');
    this.counterEl = document.getElementById('slideCounter');
    this.progressFillEl = document.getElementById('slideProgressFill');
    this.fullscreenBtn = document.getElementById('fullscreenBtn');

    if (this.totalSlides === 0) return;

    this.init();
  }

  init() {
    // 1. Check URL Hash (e.g. #3 -> slide index 2)
    const hash = window.location.hash;
    if (hash && hash.startsWith('#')) {
      const pageNum = parseInt(hash.replace('#', ''), 10);
      if (!isNaN(pageNum) && pageNum >= 1 && pageNum <= this.totalSlides) {
        this.currentIndex = pageNum - 1;
      }
    }

    // 2. Event Listeners
    if (this.prevBtn) this.prevBtn.addEventListener('click', () => this.prev());
    if (this.nextBtn) this.nextBtn.addEventListener('click', () => this.next());
    if (this.fullscreenBtn) this.fullscreenBtn.addEventListener('click', () => this.toggleFullscreen());

    // Keyboard navigation
    window.addEventListener('keydown', (e) => this.handleKeydown(e));

    // Touch swipe support for mobile/tablets
    this.initTouchSupport();

    // Hash change listener
    window.addEventListener('hashchange', () => {
      const hashNum = parseInt(window.location.hash.replace('#', ''), 10);
      if (!isNaN(hashNum) && hashNum >= 1 && hashNum <= this.totalSlides) {
        this.goTo(hashNum - 1, false);
      }
    });

    // 3. Render initial state
    this.updateUI();
  }

  handleKeydown(e) {
    // Ignore keys if user is typing in an input
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

    switch (e.key) {
      case 'ArrowRight':
      case 'PageDown':
      case ' ':
        e.preventDefault();
        this.next();
        break;
      case 'ArrowLeft':
      case 'PageUp':
        e.preventDefault();
        this.prev();
        break;
      case 'Home':
        e.preventDefault();
        this.goTo(0);
        break;
      case 'End':
        e.preventDefault();
        this.goTo(this.totalSlides - 1);
        break;
      case 'f':
      case 'F':
        this.toggleFullscreen();
        break;
    }
  }

  initTouchSupport() {
    let startX = 0;
    let startY = 0;

    window.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
      startY = e.touches[0].clientY;
    }, { passive: true });

    window.addEventListener('touchend', (e) => {
      const diffX = e.changedTouches[0].clientX - startX;
      const diffY = e.changedTouches[0].clientY - startY;

      // Threshold: horizontal swipe > 50px and more horizontal than vertical
      if (Math.abs(diffX) > 50 && Math.abs(diffX) > Math.abs(diffY)) {
        if (diffX < 0) {
          this.next();
        } else {
          this.prev();
        }
      }
    }, { passive: true });
  }

  next() {
    if (this.currentIndex < this.totalSlides - 1) {
      this.goTo(this.currentIndex + 1);
    }
  }

  prev() {
    if (this.currentIndex > 0) {
      this.goTo(this.currentIndex - 1);
    }
  }

  goTo(index, updateHash = true) {
    if (index < 0 || index >= this.totalSlides) return;
    this.currentIndex = index;
    this.updateUI();

    if (updateHash) {
      history.replaceState(null, '', `#${this.currentIndex + 1}`);
    }
  }

  updateUI() {
    this.slides.forEach((slide, idx) => {
      if (idx === this.currentIndex) {
        slide.classList.add('active');
        slide.setAttribute('aria-hidden', 'false');
      } else {
        slide.classList.remove('active');
        slide.setAttribute('aria-hidden', 'true');
      }
    });

    // Update Counter
    if (this.counterEl) {
      const currentDisplay = String(this.currentIndex + 1).padStart(2, '0');
      const totalDisplay = String(this.totalSlides).padStart(2, '0');
      this.counterEl.textContent = `${currentDisplay} / ${totalDisplay}`;
    }

    // Update Progress bar
    if (this.progressFillEl) {
      const percentage = ((this.currentIndex + 1) / this.totalSlides) * 100;
      this.progressFillEl.style.width = `${percentage}%`;
    }

    // Update Button Disabled States
    if (this.prevBtn) {
      this.prevBtn.disabled = this.currentIndex === 0;
      this.prevBtn.style.opacity = this.currentIndex === 0 ? '0.4' : '1';
      this.prevBtn.style.cursor = this.currentIndex === 0 ? 'not-allowed' : 'pointer';
    }
    if (this.nextBtn) {
      this.nextBtn.disabled = this.currentIndex === this.totalSlides - 1;
      this.nextBtn.style.opacity = this.currentIndex === this.totalSlides - 1 ? '0.4' : '1';
      this.nextBtn.style.cursor = this.currentIndex === this.totalSlides - 1 ? 'not-allowed' : 'pointer';
    }
  }

  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }
}

// Auto-initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.slideController = new SlideDeckController();
});
