/**
 * University Previous Year Questions (PYQ) Vault View
 */

import { Storage } from '../storage.js';

export function renderPyqView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING QUESTION ARCHIVE...</div>
      <h2>Retrieving CSJMU Verified PYQ Vault (2021–2025)</h2>
    </div>
  `;

  fetch('content/pyqs/all_pyqs.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load PYQ bank');
      return res.json();
    })
    .then(pyqList => {
      buildPyqPage(container, pyqList, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading PYQs</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildPyqPage(container, pyqList, daysIndex) {
  let activeFilter = 'all';
  let searchQuery = '';

  container.innerHTML = `
    <div class="pyq-header" style="margin-bottom: var(--space-6);">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">CSJMU SEMESTER 5 EXAM VAULT</div>
      <h1 style="margin-bottom: var(--space-1);">University Previous Year Questions & Model Answers</h1>
      <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
        Exhaustive collection of 15-mark and 5-mark university exam questions (2021–2025) with exact examiner marking rubrics, full textbook model answers, and study chapter links.
      </p>
    </div>

    <!-- Filter & Search Controls Bar -->
    <div class="card" style="margin-bottom: var(--space-6); padding: var(--space-4);">
      <div style="display: flex; flex-direction: column; gap: var(--space-4);">
        <div style="display: flex; gap: var(--space-3); flex-wrap: wrap; align-items: center; justify-content: space-between;">
          <div style="flex: 1; min-width: 250px;">
            <input type="text" id="pyq-search-input" class="form-control" placeholder="🔍 Search question, topic, algorithm, or year (e.g., Simon, SECI, Gauss, CRC)..." style="width: 100%;">
          </div>
          <div id="pyq-results-count" class="badge badge-secondary" style="font-size: var(--font-size-sm); padding: 8px 12px;">
            Showing ${pyqList.length} Questions
          </div>
        </div>

        <!-- Subject Filter Pills -->
        <div style="display: flex; gap: var(--space-2); flex-wrap: wrap;">
          <button class="btn btn-primary btn-sm pyq-filter-btn" data-subject="all">All Subjects (${pyqList.length})</button>
          <button class="btn btn-secondary btn-sm pyq-filter-btn" data-subject="BCA-5001">BCA-5001 Knowledge Management</button>
          <button class="btn btn-secondary btn-sm pyq-filter-btn" data-subject="BCA-5002">BCA-5002 Java & Web</button>
          <button class="btn btn-secondary btn-sm pyq-filter-btn" data-subject="BCA-5003">BCA-5003 Computer Networks</button>
          <button class="btn btn-secondary btn-sm pyq-filter-btn" data-subject="BCA-5004">BCA-5004 Numerical Methods</button>
        </div>
      </div>
    </div>

    <!-- Questions List Container -->
    <div id="pyq-cards-list" style="display: flex; flex-direction: column; gap: var(--space-5);">
      <!-- Rendered dynamically -->
    </div>
  `;

  const searchInput = container.querySelector('#pyq-search-input');
  const countBadge = container.querySelector('#pyq-results-count');
  const cardsList = container.querySelector('#pyq-cards-list');
  const filterBtns = container.querySelectorAll('.pyq-filter-btn');

  function renderFilteredCards() {
    const qLower = searchQuery.toLowerCase().trim();
    const filtered = pyqList.filter(item => {
      const matchSubj = activeFilter === 'all' || item.subject.toLowerCase().includes(activeFilter.toLowerCase());
      const matchQuery = !qLower || 
        item.question.toLowerCase().includes(qLower) || 
        item.topic.toLowerCase().includes(qLower) || 
        (item.pyq_year && item.pyq_year.toLowerCase().includes(qLower));
      return matchSubj && matchQuery;
    });

    countBadge.textContent = `Showing ${filtered.length} of ${pyqList.length} Questions`;

    if (filtered.length === 0) {
      cardsList.innerHTML = `
        <div class="card" style="text-align: center; padding: var(--space-8); color: var(--text-muted);">
          <h3>No matching questions found</h3>
          <p>Try searching with another keyword or selecting "All Subjects".</p>
        </div>
      `;
      return;
    }

    cardsList.innerHTML = filtered.map((item, idx) => {
      const isBookmarked = Storage.isBookmarked(`pyq_${item.day}`);
      return `
        <div class="card pyq-item-card" id="pyq-card-${idx}" style="margin-bottom: 0; border-left: 4px solid var(--color-primary);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-3);">
            <div style="display: flex; gap: var(--space-2); align-items: center; flex-wrap: wrap;">
              <span class="badge badge-primary">${item.subject}</span>
              <span class="badge badge-secondary">${item.pyq_year || 'CSJMU'}</span>
              <span class="badge badge-warning">15 Marks Rubric</span>
            </div>
            <div style="display: flex; gap: var(--space-2); align-items: center;">
              <button class="btn btn-secondary btn-sm pyq-bookmark-btn" data-id="pyq_${item.day}" data-title="${item.topic}" style="padding: 2px 8px;">
                ${isBookmarked ? '★ Bookmarked' : '☆ Bookmark'}
              </button>
              <a href="#day/${item.day}" class="btn btn-secondary btn-sm" style="padding: 2px 8px;">
                Day ${item.day} Lecture →
              </a>
            </div>
          </div>

          <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase; margin-bottom: var(--space-1);">
            ${item.topic}
          </div>

          <h3 style="font-size: var(--font-size-lg); line-height: 1.4; color: var(--text-primary); margin-bottom: var(--space-3);">
            ${item.question}
          </h3>

          ${item.pyq_freq ? `
            <div style="font-size: var(--font-size-xs); color: var(--color-info); margin-bottom: var(--space-3); background: var(--color-info-subtle); padding: 4px 8px; border-radius: var(--radius-sm); display: inline-block;">
              📌 ${item.pyq_freq}
            </div>
          ` : ''}

          <!-- Marking Rubric -->
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); margin-bottom: var(--space-4); border: 1px dashed var(--border-color);">
            <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-warning); text-transform: uppercase; margin-bottom: 2px;">
              ⚖️ Official 15-Mark Examiner Evaluation Rubric:
            </div>
            <div style="font-size: var(--font-size-sm); color: var(--text-secondary);">
              ${item.rubric}
            </div>
          </div>

          <!-- Model Answer Accordion Trigger -->
          <div>
            <button class="btn btn-secondary btn-sm toggle-model-answer-btn" data-target="ans-${idx}" style="width: 100%; justify-content: center; font-weight: 700;">
              <span>📖 Reveal University-Standard Model Answer</span>
            </button>
            <div id="ans-${idx}" class="pyq-model-answer-panel" style="display: none; margin-top: var(--space-4); padding: var(--space-4); background: var(--bg-surface-2); border-radius: var(--radius-md); border-left: 3px solid var(--color-success);">
              <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-success); text-transform: uppercase; margin-bottom: var(--space-3);">
                ✓ High-Scoring Benchmark Answer (Textbook Pedagogical Depth):
              </div>
              <div style="font-size: var(--font-size-sm); line-height: 1.7; color: var(--text-secondary); display: flex; flex-direction: column; gap: var(--space-3);">
                ${(item.model_answer_paragraphs || []).map(p => {
                  if (Array.isArray(p)) {
                    return `
                      <div style="margin-bottom: var(--space-2);">
                        <strong style="color: var(--text-primary); display: block; margin-bottom: 4px;">${p[0]}</strong>
                        <p style="margin: 0; white-space: pre-line;">${p[1]}</p>
                      </div>
                    `;
                  } else {
                    return `<p style="margin: 0; white-space: pre-line;">${p}</p>`;
                  }
                }).join('')}
              </div>
            </div>
          </div>
        </div>
      `;
    }).join('');

    // Attach answer toggle listeners
    cardsList.querySelectorAll('.toggle-model-answer-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.dataset.target;
        const panel = document.getElementById(targetId);
        if (panel) {
          const isHidden = panel.style.display === 'none';
          panel.style.display = isHidden ? 'block' : 'none';
          btn.innerHTML = isHidden ? '<span>▲ Hide Model Answer</span>' : '<span>📖 Reveal University-Standard Model Answer</span>';
          btn.classList.toggle('btn-primary', isHidden);
          btn.classList.toggle('btn-secondary', !isHidden);
        }
      });
    });

    // Attach bookmark toggle listeners
    cardsList.querySelectorAll('.pyq-bookmark-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.id;
        const title = btn.dataset.title;
        const added = Storage.toggleBookmark({ id, type: 'pyq', title });
        btn.textContent = added ? '★ Bookmarked' : '☆ Bookmark';
      });
    });
  }

  // Initial render
  renderFilteredCards();

  // Search input handler
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    renderFilteredCards();
  });

  // Filter button handlers
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');
      activeFilter = btn.dataset.subject;
      renderFilteredCards();
    });
  });
}
