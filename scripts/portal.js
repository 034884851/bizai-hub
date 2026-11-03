/**
 * BizAI Hub - Portal Index Controller
 * Search, Category Filtering, Content Counters, and AGENTS.md Modal Viewer
 */

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('hubSearchInput');
  const clearSearchBtn = document.getElementById('clearSearchBtn');
  const filterBtns = document.querySelectorAll('.filter-btn');
  const contentCards = document.querySelectorAll('.content-card');
  const counterDisplay = document.getElementById('contentCountDisplay');
  const emptyState = document.getElementById('emptySearchState');

  let activeCategory = 'all';
  let searchQuery = '';

  function filterCards() {
    let visibleCount = 0;
    const query = searchQuery.trim().toLowerCase();

    contentCards.forEach(card => {
      const type = card.dataset.type; // 'lesson' or 'wiki'
      const title = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
      const desc = (card.querySelector('.card-desc')?.textContent || '').toLowerCase();
      const tags = (card.dataset.tags || '').toLowerCase();

      const matchesCategory = (activeCategory === 'all') || (type === activeCategory);
      const matchesSearch = !query || title.includes(query) || desc.includes(query) || tags.includes(query);

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (counterDisplay) {
      counterDisplay.textContent = `顯示中：${visibleCount} 份項目`;
    }

    if (emptyState) {
      emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  // Search input event
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      if (clearSearchBtn) {
        clearSearchBtn.style.display = searchQuery ? 'block' : 'none';
      }
      filterCards();
    });
  }

  // Clear search button
  if (clearSearchBtn) {
    clearSearchBtn.addEventListener('click', () => {
      if (searchInput) {
        searchInput.value = '';
        searchQuery = '';
        clearSearchBtn.style.display = 'none';
        filterCards();
        searchInput.focus();
      }
    });
  }

  // Category filter tabs
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.dataset.category;
      filterCards();
    });
  });

  // Modal for AGENTS.md / CLAUDE.md viewer
  const openModalBtn = document.getElementById('openAgentsModalBtn');
  const modal = document.getElementById('agentsModal');
  const closeModalBtn = document.getElementById('closeAgentsModalBtn');

  if (openModalBtn && modal) {
    openModalBtn.addEventListener('click', () => {
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    });
  }

  if (closeModalBtn && modal) {
    closeModalBtn.addEventListener('click', () => {
      modal.style.display = 'none';
      document.body.style.overflow = 'auto';
    });
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
      }
    });
  }

  // Run initial filter
  filterCards();
});
