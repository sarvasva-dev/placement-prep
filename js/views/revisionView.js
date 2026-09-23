/**
 * Spaced Repetition, Revision Hub & Bookmarks View
 */

import { Storage } from '../storage.js';

export function renderRevisionView(container, daysIndex) {
  const activeDay = Storage.getActiveDay();
  const bookmarks = Storage.getBookmarks();
  const testResults = Storage.getAllTestResults();

  const prevDay = Math.max(1, activeDay - 1);
  const spacedDay = Math.max(1, activeDay - 7);

  const prevDayMeta = daysIndex.find(d => d.day === prevDay) || daysIndex[0];
  const spacedDayMeta = daysIndex.find(d => d.day === spacedDay) || daysIndex[0];

  container.innerHTML = `
    <div class="revision-header" style="margin-bottom: var(--space-6);">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">SPACED REPETITION ENGINE</div>
      <h1 style="margin-bottom: var(--space-1);">Revision & Retention Command Center</h1>
      <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
        Combat the Ebbinghaus forgetting curve. Automated spaced repetition triggers (1-day & 7-day intervals), personal bookmarked questions, and final 3-day sprint checklists.
      </p>
    </div>

    <!-- Spaced Repetition Triggers Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--space-4); margin-bottom: var(--space-6);">
      
      <!-- Yesterday's Retain Card -->
      <div class="card" style="margin-bottom: 0; border-left: 4px solid var(--color-warning);">
        <div class="card-header">
          <div>
            <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-warning); text-transform: uppercase;">1-Day Retention Check</div>
            <h3 class="card-title">Day ${prevDay}: Yesterday's Core Knowledge</h3>
          </div>
          <span class="badge badge-warning">24h Interval</span>
        </div>
        <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-bottom: var(--space-3);">
          Subject: <strong>${prevDayMeta.subject}</strong><br>
          Topic: ${prevDayMeta.topic}
        </p>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); margin-bottom: var(--space-3); font-size: var(--font-size-xs);">
          💡 <strong>Rapid Self-Test:</strong> Can you write the definition, primary formula, and algorithm without opening notes?
        </div>
        <a href="#day/${prevDay}" class="btn btn-secondary btn-sm" style="width: 100%; justify-content: center;">
          Review Day ${prevDay} Chapter →
        </a>
      </div>

      <!-- 7-Day Spaced Review Card -->
      <div class="card" style="margin-bottom: 0; border-left: 4px solid var(--color-primary);">
        <div class="card-header">
          <div>
            <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-primary); text-transform: uppercase;">7-Day Long-Term Consolidation</div>
            <h3 class="card-title">Day ${spacedDay}: One Week Ago</h3>
          </div>
          <span class="badge badge-primary">7d Interval</span>
        </div>
        <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-bottom: var(--space-3);">
          Subject: <strong>${spacedDayMeta.subject}</strong><br>
          Topic: ${spacedDayMeta.topic}
        </p>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); margin-bottom: var(--space-3); font-size: var(--font-size-xs);">
          🧠 <strong>Memory Re-consolidation:</strong> Solve 1 problem from this day to permanently anchor the neural pathway.
        </div>
        <a href="#day/${spacedDay}" class="btn btn-secondary btn-sm" style="width: 100%; justify-content: center;">
          Review Day ${spacedDay} Chapter →
        </a>
      </div>

    </div>

    <!-- Bookmarked Questions & Concepts -->
    <div class="card" style="margin-bottom: var(--space-6);">
      <div class="card-header">
        <h2 class="card-title">⭐ Bookmarked Items & Flagged Questions</h2>
        <span class="badge badge-primary">${bookmarks.length} Saved</span>
      </div>

      ${bookmarks.length === 0 ? `
        <div style="text-align: center; padding: var(--space-6); color: var(--text-muted);">
          <p>No items bookmarked yet.</p>
          <span style="font-size: var(--font-size-xs);">Click the "☆ Bookmark" button on any PYQ or problem while studying to save it here for instant revision.</span>
        </div>
      ` : `
        <div style="display: flex; flex-direction: column; gap: var(--space-2);">
          ${bookmarks.map(b => `
            <div style="display: flex; justify-content: space-between; align-items: center; background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); gap: var(--space-3);">
              <div>
                <span class="badge badge-secondary" style="margin-right: var(--space-2); text-transform: uppercase;">${b.type || 'Item'}</span>
                <strong style="font-size: var(--font-size-sm); color: var(--text-primary);">${b.title || b.id}</strong>
              </div>
              <button class="btn btn-secondary btn-sm remove-bookmark-btn" data-id="${b.id}" style="padding: 2px 8px; color: var(--color-danger);">
                Remove ✕
              </button>
            </div>
          `).join('')}
        </div>
      `}
    </div>

    <!-- Daily Test Mistakes Tracker -->
    <div class="card" style="margin-bottom: var(--space-6);">
      <div class="card-header">
        <h2 class="card-title">📝 Daily Test Performance & Weak Spot Tracker</h2>
        <span class="badge badge-warning">Mistake Review</span>
      </div>
      
      ${Object.keys(testResults).length === 0 ? `
        <div style="text-align: center; padding: var(--space-6); color: var(--text-muted);">
          <p>No daily tests completed yet.</p>
          <span style="font-size: var(--font-size-xs);">Complete the 8-question test at the bottom of any day's chapter to record your diagnostic score.</span>
        </div>
      ` : `
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Day</th>
                <th>Score</th>
                <th>Accuracy</th>
                <th>Attempted Date</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${Object.entries(testResults).map(([d, res]) => `
                <tr>
                  <td><strong>Day ${d}</strong></td>
                  <td>${res.score} / ${res.maxScore}</td>
                  <td>
                    <span class="badge ${res.percentage >= 80 ? 'badge-success' : res.percentage >= 60 ? 'badge-warning' : 'badge-danger'}">
                      ${res.percentage}%
                    </span>
                  </td>
                  <td>${new Date(res.date).toLocaleDateString()}</td>
                  <td><a href="#day/${d}" class="btn btn-secondary btn-sm" style="padding: 2px 8px;">Retest →</a></td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `}
    </div>

    <!-- Final 3-Day Sprint Strategy (Days 28, 29, 30) -->
    <div class="card" style="border-top: 4px solid var(--color-success);">
      <div class="card-header">
        <h2 class="card-title">🏁 Days 28–30 Final Exam & Placement Simulation Protocol</h2>
        <span class="badge badge-success">Zero-Failure Protocol</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-4);">
        <div style="background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-md);">
          <div class="badge badge-primary" style="margin-bottom: var(--space-1);">DAY 28</div>
          <h4 style="margin: 0 0 6px 0;">Campus Placement Simulation</h4>
          <p style="font-size: var(--font-size-xs); color: var(--text-secondary); line-height: 1.5; margin-bottom: var(--space-3);">
            Execute complete 3-hour mock placement exam: 60-min Aptitude (TCS/Infosys pattern) + 45-min Coding (2 Python DSA problems) + 45-min Technical Mock Defense.
          </p>
          <a href="#day/28" class="btn btn-secondary btn-sm" style="width: 100%; justify-content: center;">Enter Day 28 Simulation →</a>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-md);">
          <div class="badge badge-warning" style="margin-bottom: var(--space-1);">DAY 29</div>
          <h4 style="margin: 0 0 6px 0;">Semester 5 Exam Simulation</h4>
          <p style="font-size: var(--font-size-xs); color: var(--text-secondary); line-height: 1.5; margin-bottom: var(--space-3);">
            Write out full 15-mark model answers by hand for KM (Simon & SECI), Java (Servlets/JDBC), Networks (OSI/CRC), and Numerical Methods (RK4/Simpson).
          </p>
          <a href="#day/29" class="btn btn-secondary btn-sm" style="width: 100%; justify-content: center;">Enter Day 29 Simulation →</a>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-md);">
          <div class="badge badge-success" style="margin-bottom: var(--space-1);">DAY 30</div>
          <h4 style="margin: 0 0 6px 0;">Exam Hall Strategy & Sign-Off</h4>
          <p style="font-size: var(--font-size-xs); color: var(--text-secondary); line-height: 1.5; margin-bottom: var(--space-3);">
            Final formula cramming, time-management protocol (40 min per 15-mark question), mental composure guidelines, and handbook completion sign-off.
          </p>
          <a href="#day/30" class="btn btn-secondary btn-sm" style="width: 100%; justify-content: center;">Enter Day 30 Protocol →</a>
        </div>
      </div>
    </div>
  `;

  // Attach bookmark remove listeners
  container.querySelectorAll('.remove-bookmark-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.id;
      Storage.toggleBookmark({ id });
      renderRevisionView(container, daysIndex); // re-render
    });
  });
}
