/**
 * 50+ Placement Java DSA Problem Directory & Coding View
 */

import { Storage } from '../storage.js';

export function renderCodingView(container, daysIndex, initialQuery = '') {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING DSA DIRECTORY...</div>
      <h2>Retrieving 50+ Placement Java Coding Solutions</h2>
    </div>
  `;

  fetch('content/coding/all_coding.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load coding data');
      return res.json();
    })
    .then(codingList => {
      buildCodingPage(container, codingList, daysIndex, initialQuery);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Coding Directory</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildCodingPage(container, codingList, daysIndex, initialQuery = '') {
  let activePattern = 'all';
  let activeDifficulty = 'all';
  let searchQuery = initialQuery || '';

  // Extract unique patterns
  const allPatterns = Array.from(new Set(codingList.map(p => p.pattern).filter(Boolean)));

  container.innerHTML = `
    <div class="coding-header" style="margin-bottom: var(--space-6);">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-4);">
        <div>
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">JAVA DSA MASTER DIRECTORY</div>
          <h1 style="margin-bottom: var(--space-1);">50+ Placement Coding & Algorithm Vault</h1>
          <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
            Production-grade Java 17+ solutions tested for campus placement coding rounds. Clean algorithmic intuition, edge case handling, and asymptotic complexity analysis.
          </p>
        </div>
      </div>
    </div>

    <!-- Filter & Search Controls -->
    <div class="card" style="margin-bottom: var(--space-6); padding: var(--space-4);">
      <div style="display: flex; flex-direction: column; gap: var(--space-4);">
        <div style="display: flex; gap: var(--space-3); flex-wrap: wrap; align-items: center; justify-content: space-between;">
          <div style="flex: 1; min-width: 250px;">
            <input type="text" id="coding-search-input" class="form-control" value="${searchQuery}" placeholder="🔍 Search by problem name, pattern, or keyword (e.g., Two Pointers, Cycle, Subarray)..." style="width: 100%;">
          </div>
          <div id="coding-results-count" class="badge badge-secondary" style="font-size: var(--font-size-sm); padding: 8px 12px;">
            Showing ${codingList.length} Problems
          </div>
        </div>

        <!-- Pattern Filter Pills -->
        <div>
          <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: var(--space-2);">Filter by Algorithmic Pattern:</div>
          <div style="display: flex; gap: var(--space-2); flex-wrap: wrap;">
            <button class="btn btn-primary btn-sm coding-pattern-btn" data-pattern="all">All Patterns (${codingList.length})</button>
            ${allPatterns.map(p => `
              <button class="btn btn-secondary btn-sm coding-pattern-btn" data-pattern="${p}">${p}</button>
            `).join('')}
          </div>
        </div>

        <!-- Difficulty Filter -->
        <div style="display: flex; gap: var(--space-2); align-items: center;">
          <span style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Difficulty:</span>
          <button class="btn btn-primary btn-sm coding-diff-btn" data-diff="all">All</button>
          <button class="btn btn-secondary btn-sm coding-diff-btn" data-diff="Easy">Easy</button>
          <button class="btn btn-secondary btn-sm coding-diff-btn" data-diff="Medium">Medium</button>
          <button class="btn btn-secondary btn-sm coding-diff-btn" data-diff="Hard">Hard</button>
        </div>
      </div>
    </div>

    <!-- Problems List Container -->
    <div id="coding-cards-list" style="display: flex; flex-direction: column; gap: var(--space-5);">
      <!-- Rendered dynamically -->
    </div>
  `;

  const searchInput = container.querySelector('#coding-search-input');
  const countBadge = container.querySelector('#coding-results-count');
  const cardsList = container.querySelector('#coding-cards-list');
  const patternBtns = container.querySelectorAll('.coding-pattern-btn');
  const diffBtns = container.querySelectorAll('.coding-diff-btn');

  function renderFilteredProblems() {
    const qLower = searchQuery.toLowerCase().trim();
    const filtered = codingList.filter(item => {
      const matchPattern = activePattern === 'all' || (item.pattern && item.pattern.toLowerCase() === activePattern.toLowerCase());
      const matchDiff = activeDifficulty === 'all' || (item.difficulty && item.difficulty.toLowerCase() === activeDifficulty.toLowerCase());
      const matchSearch = !qLower ||
        (item.title && item.title.toLowerCase().includes(qLower)) ||
        (item.problem && item.problem.toLowerCase().includes(qLower)) ||
        (item.pattern && item.pattern.toLowerCase().includes(qLower));
      return matchPattern && matchDiff && matchSearch;
    });

    countBadge.textContent = `Showing ${filtered.length} of ${codingList.length} Problems`;

    if (filtered.length === 0) {
      cardsList.innerHTML = `
        <div class="card" style="text-align: center; padding: var(--space-8); color: var(--text-muted);">
          <h3>No matching coding problems found</h3>
          <p>Try resetting filters or searching with another term.</p>
        </div>
      `;
      return;
    }

    cardsList.innerHTML = filtered.map((item, idx) => {
      const probId = `code_${item.day}_${idx}`;
      const isDone = Storage.isBookmarked(`solved_${probId}`);
      const diffClass = item.difficulty === 'Easy' ? 'badge-success' : item.difficulty === 'Hard' ? 'badge-danger' : 'badge-warning';

      return `
        <div class="card" style="margin-bottom: 0; border-left: 4px solid var(--color-primary);">
          <!-- Problem Header Bar -->
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-3);">
            <div>
              <div style="display: flex; gap: var(--space-2); align-items: center; flex-wrap: wrap; margin-bottom: var(--space-1);">
                <span class="badge ${diffClass}">${item.difficulty || 'Medium'}</span>
                <span class="badge badge-primary">${item.pattern || 'Algorithm'}</span>
                <a href="#day/${item.day}" class="badge badge-secondary" style="text-decoration:none;">Day ${item.day} Sprint</a>
              </div>
              <h3 style="margin: 0; font-size: var(--font-size-xl); color: var(--text-primary);">${item.title}</h3>
            </div>

            <div style="display: flex; gap: var(--space-2); align-items: center;">
              <button class="btn btn-secondary btn-sm toggle-solved-btn" data-id="solved_${probId}" style="padding: 2px 8px;">
                ${isDone ? '✓ Solved' : '○ Mark Solved'}
              </button>
              <button class="btn btn-secondary btn-sm copy-code-btn" data-code="${idx}" style="padding: 2px 8px;">
                📋 Copy Code
              </button>
            </div>
          </div>

          <!-- Problem Description -->
          <div style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6; margin-bottom: var(--space-3); background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            ${item.problem}
          </div>

          <!-- Intuition & Complexity -->
          <div style="margin-bottom: var(--space-4);">
            <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-primary); text-transform: uppercase; margin-bottom: 2px;">
              💡 Algorithmic Intuition & Logic:
            </div>
            <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-bottom: var(--space-2); line-height: 1.5;">
              ${item.intuition || 'Optimal two-pointer / hashing approach with minimal auxiliary space.'}
            </p>
            <div style="display: flex; gap: var(--space-2); flex-wrap: wrap;">
              <span class="badge badge-secondary">Time: ${item.time_complexity || 'O(N)'}</span>
              <span class="badge badge-secondary">Space: ${item.space_complexity || 'O(1)'}</span>
            </div>
          </div>

          <!-- Solution Code Box -->
          <div class="code-container" style="margin-bottom: var(--space-2);">
            <pre><code class="language-java" id="code-content-${idx}">${item.java_code || item.code || item.solution || '// Solution implementation in Day ' + item.day}</code></pre>
          </div>
        </div>
      `;
    }).join('');

    // Attach copy code handlers
    cardsList.querySelectorAll('.copy-code-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const codeIdx = btn.dataset.code;
        const codeEl = document.getElementById(`code-content-${codeIdx}`);
        if (codeEl) {
          navigator.clipboard.writeText(codeEl.textContent).then(() => {
            const originalText = btn.textContent;
            btn.textContent = '✓ Copied!';
            btn.classList.add('btn-success');
            setTimeout(() => {
              btn.textContent = originalText;
              btn.classList.remove('btn-success');
            }, 2000);
          });
        }
      });
    });

    // Attach mark solved handlers
    cardsList.querySelectorAll('.toggle-solved-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.id;
        const added = Storage.toggleBookmark({ id, type: 'solved', title: id });
        btn.textContent = added ? '✓ Solved' : '○ Mark Solved';
        btn.classList.toggle('btn-success', added);
      });
    });
  }

  // Initial render
  renderFilteredProblems();

  // Search input handler
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    renderFilteredProblems();
  });

  // Pattern filter handlers
  patternBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      patternBtns.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');
      activePattern = btn.dataset.pattern;
      renderFilteredProblems();
    });
  });

  // Difficulty filter handlers
  diffBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      diffBtns.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');
      activeDifficulty = btn.dataset.diff;
      renderFilteredProblems();
    });
  });
}
