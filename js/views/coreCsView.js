/**
 * Core Computer Science Subjects (OS, DBMS, Networks, Python) View
 */

import { Storage } from '../storage.js';

export function renderCoreCsView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING CORE CS VAULT...</div>
      <h2>Retrieving Core Computer Science Knowledge Base</h2>
    </div>
  `;

  fetch('content/core_cs/all_core_cs.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load Core CS data');
      return res.json();
    })
    .then(coreList => {
      buildCoreCsPage(container, coreList, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Core CS Data</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildCoreCsPage(container, coreList, daysIndex) {
  let activeCategory = 'all';
  let searchQuery = '';

  container.innerHTML = `
    <div class="core-cs-header" style="margin-bottom: var(--space-6);">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">INTERVIEW TECHNICAL CLEARANCE</div>
      <h1 style="margin-bottom: var(--space-1);">Core Computer Science Knowledge Base</h1>
      <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
        Operating Systems, DBMS, Computer Networks, and Python Runtime Internals. Master the underlying mechanisms and counter interview trap questions with architectural clarity.
      </p>
    </div>

    <!-- Search & Filter Controls -->
    <div class="card" style="margin-bottom: var(--space-6); padding: var(--space-4);">
      <div style="display: flex; flex-direction: column; gap: var(--space-4);">
        <div style="display: flex; gap: var(--space-3); flex-wrap: wrap; align-items: center; justify-content: space-between;">
          <div style="flex: 1; min-width: 250px;">
            <input type="text" id="core-search-input" class="form-control" placeholder="🔍 Search Core CS topic, concept, or interview question (e.g., GIL, Deadlock, ACID, TCP)..." style="width: 100%;">
          </div>
          <div id="core-results-count" class="badge badge-secondary" style="font-size: var(--font-size-sm); padding: 8px 12px;">
            Showing ${coreList.length} Topics
          </div>
        </div>

        <div style="display: flex; gap: var(--space-2); flex-wrap: wrap;">
          <button class="btn btn-primary btn-sm core-filter-btn" data-cat="all">All Topics (${coreList.length})</button>
          <button class="btn btn-secondary btn-sm core-filter-btn" data-cat="OS">Operating Systems</button>
          <button class="btn btn-secondary btn-sm core-filter-btn" data-cat="DBMS">DBMS & SQL</button>
          <button class="btn btn-secondary btn-sm core-filter-btn" data-cat="Network">Networks</button>
          <button class="btn btn-secondary btn-sm core-filter-btn" data-cat="Python">Python Internals</button>
        </div>
      </div>
    </div>

    <!-- Topic Cards List -->
    <div id="core-cards-list" style="display: flex; flex-direction: column; gap: var(--space-5);">
      <!-- Rendered dynamically -->
    </div>
  `;

  const searchInput = container.querySelector('#core-search-input');
  const countBadge = container.querySelector('#core-results-count');
  const cardsList = container.querySelector('#core-cards-list');
  const filterBtns = container.querySelectorAll('.core-filter-btn');

  function renderFilteredTopics() {
    const qLower = searchQuery.toLowerCase().trim();
    const filtered = coreList.filter(item => {
      const matchCat = activeCategory === 'all' || 
        (item.topic && item.topic.toLowerCase().includes(activeCategory.toLowerCase())) ||
        (item.lecture && item.lecture.toLowerCase().includes(activeCategory.toLowerCase()));
      const matchSearch = !qLower ||
        (item.topic && item.topic.toLowerCase().includes(qLower)) ||
        (item.lecture && item.lecture.toLowerCase().includes(qLower)) ||
        (item.interview_qa && item.interview_qa.some(qa => (qa.q && qa.q.toLowerCase().includes(qLower)) || (qa.a && qa.a.toLowerCase().includes(qLower))));
      return matchCat && matchSearch;
    });

    countBadge.textContent = `Showing ${filtered.length} of ${coreList.length} Topics`;

    if (filtered.length === 0) {
      cardsList.innerHTML = `
        <div class="card" style="text-align: center; padding: var(--space-8); color: var(--text-muted);">
          <h3>No matching Core CS topics found</h3>
          <p>Try searching with another keyword or resetting category filters.</p>
        </div>
      `;
      return;
    }

    cardsList.innerHTML = filtered.map((item, idx) => {
      const noteKey = `core_note_${item.day}`;
      const savedNote = Storage.getNote(noteKey);

      return `
        <div class="card" style="margin-bottom: 0; border-left: 4px solid var(--color-primary);">
          <!-- Card Header -->
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-3);">
            <div>
              <div style="display: flex; gap: var(--space-2); align-items: center; margin-bottom: var(--space-1);">
                <span class="badge badge-primary">Day ${item.day} Curriculum</span>
                <span class="badge badge-secondary">Core CS</span>
              </div>
              <h3 style="margin: 0; font-size: var(--font-size-xl); color: var(--text-primary);">${item.topic}</h3>
            </div>
            <a href="#day/${item.day}" class="btn btn-secondary btn-sm">Full Day ${item.day} Lecture →</a>
          </div>

          <!-- Deep-Dive Lecture Notes -->
          <div style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.7; margin-bottom: var(--space-4); background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-sm); white-space: pre-line;">
            ${item.lecture}
          </div>

          <!-- Interview Questions Accordion -->
          ${item.interview_qa && item.interview_qa.length ? `
            <div style="margin-bottom: var(--space-4);">
              <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-warning); text-transform: uppercase; margin-bottom: var(--space-2);">
                🎯 Technical Interview Trap Questions & Architectural Defense:
              </div>
              <div style="display: flex; flex-direction: column; gap: var(--space-3);">
                ${item.interview_qa.map((qa, qidx) => `
                  <div style="border: 1px solid var(--border-color); border-radius: var(--radius-sm); overflow: hidden;">
                    <div style="background: var(--bg-surface-3); padding: var(--space-3); font-weight: 600; font-size: var(--font-size-sm); color: var(--text-primary); display: flex; justify-content: space-between; align-items: center; cursor: pointer;" class="core-qa-header" data-target="qa-${idx}-${qidx}">
                      <span>${qa.q}</span>
                      <span style="color: var(--color-primary); font-size: var(--font-size-xs);">Toggle Answer ▼</span>
                    </div>
                    <div id="qa-${idx}-${qidx}" style="display: none; padding: var(--space-3); background: var(--bg-surface); font-size: var(--font-size-sm); line-height: 1.6; color: var(--text-secondary); border-top: 1px solid var(--border-color);">
                      ${qa.a}
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}

          <!-- Personal Notes Box -->
          <div style="border-top: 1px solid var(--border-color); padding-top: var(--space-3); margin-top: var(--space-3);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <span style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Personal Revision Notes:</span>
              <span id="note-saved-${item.day}" style="font-size: var(--font-size-xs); color: var(--color-success); display: none;">Saved!</span>
            </div>
            <textarea class="form-control core-note-input" data-key="${noteKey}" data-day="${item.day}" placeholder="Jot down personal mnemonic triggers, doubts, or notes..." style="width: 100%; min-height: 60px; font-size: var(--font-size-xs);">${savedNote}</textarea>
          </div>
        </div>
      `;
    }).join('');

    // Attach QA accordion toggle listeners
    cardsList.querySelectorAll('.core-qa-header').forEach(header => {
      header.addEventListener('click', () => {
        const targetId = header.dataset.target;
        const panel = document.getElementById(targetId);
        if (panel) {
          const isHidden = panel.style.display === 'none';
          panel.style.display = isHidden ? 'block' : 'none';
          header.querySelector('span:last-child').textContent = isHidden ? 'Hide ▲' : 'Toggle Answer ▼';
        }
      });
    });

    // Attach personal notes auto-save listeners
    cardsList.querySelectorAll('.core-note-input').forEach(textarea => {
      textarea.addEventListener('input', (e) => {
        const key = textarea.dataset.key;
        const day = textarea.dataset.day;
        Storage.saveNote(key, e.target.value);
        const savedLabel = document.getElementById(`note-saved-${day}`);
        if (savedLabel) {
          savedLabel.style.display = 'inline';
          setTimeout(() => { savedLabel.style.display = 'none'; }, 1500);
        }
      });
    });
  }

  // Initial render
  renderFilteredTopics();

  // Search input handler
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    renderFilteredTopics();
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
      activeCategory = btn.dataset.cat;
      renderFilteredTopics();
    });
  });
}
