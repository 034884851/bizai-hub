/**
 * BizAI Hub - LLM Wiki Archetype Controller
 * Table of Contents generation, ScrollSpy, and interactive enhancements
 */

document.addEventListener('DOMContentLoaded', () => {
  const tocList = document.getElementById('tocList');
  const headings = Array.from(document.querySelectorAll('.wiki-body h2, .wiki-body h3'));

  if (tocList && headings.length > 0) {
    tocList.innerHTML = '';
    headings.forEach((heading, index) => {
      // Ensure heading has an ID
      if (!heading.id) {
        heading.id = `heading-${index + 1}`;
      }

      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = `#${heading.id}`;
      a.className = 'toc-link';
      a.textContent = heading.textContent.replace(/^[#\s✦🔗]+/, '').trim();

      if (heading.tagName.toLowerCase() === 'h3') {
        a.style.paddingLeft = '18px';
        a.style.fontSize = '13px';
      }

      li.appendChild(a);
      tocList.appendChild(li);
    });

    // ScrollSpy observer
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          document.querySelectorAll('.toc-link').forEach(link => {
            if (link.getAttribute('href') === `#${id}`) {
              link.classList.add('active');
            } else {
              link.classList.remove('active');
            }
          });
        }
      });
    }, { rootMargin: '0px 0px -70% 0px' });

    headings.forEach(heading => observer.observe(heading));
  }

  // Add click to copy functionality to code blocks
  document.querySelectorAll('pre code').forEach((codeBlock) => {
    const pre = codeBlock.parentElement;
    pre.style.position = 'relative';

    const copyBtn = document.createElement('button');
    copyBtn.className = 'copy-code-btn';
    copyBtn.textContent = '複製';
    copyBtn.style.position = 'absolute';
    copyBtn.style.top = '8px';
    copyBtn.style.right = '8px';
    copyBtn.style.padding = '3px 8px';
    copyBtn.style.fontSize = '12px';
    copyBtn.style.fontFamily = 'var(--font-round)';
    copyBtn.style.background = 'var(--cream)';
    copyBtn.style.border = '1px solid var(--border-line)';
    copyBtn.style.borderRadius = '4px';
    copyBtn.style.cursor = 'pointer';

    function fallbackCopyText(text, btn) {
      try {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        btn.textContent = '已複製！';
        setTimeout(() => { btn.textContent = '複製'; }, 2000);
      } catch (err) {
        btn.textContent = '複製失敗';
        setTimeout(() => { btn.textContent = '複製'; }, 2000);
      }
    }

    copyBtn.addEventListener('click', () => {
      const textToCopy = codeBlock.innerText;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(textToCopy).then(() => {
          copyBtn.textContent = '已複製！';
          setTimeout(() => { copyBtn.textContent = '複製'; }, 2000);
        }).catch(() => {
          fallbackCopyText(textToCopy, copyBtn);
        });
      } else {
        fallbackCopyText(textToCopy, copyBtn);
      }
    });

    pre.appendChild(copyBtn);
  });
});
