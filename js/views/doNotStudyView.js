/**
 * Triage & "Do Not Study" Focus Protection View
 */

export function renderDoNotStudyView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING TRIAGE PROTOCOL...</div>
      <h2>Retrieving High-Yield Scope Protection Rules</h2>
    </div>
  `;

  fetch('content/do_not_study.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load do-not-study data');
      return res.json();
    })
    .then(data => {
      buildDoNotStudyPage(container, data, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Triage Protocol</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildDoNotStudyPage(container, data, daysIndex) {
  const alternatives = {
    'Obsolete Java AWT / Swing GUI Programming': 'Study Core OOP, Collections (HashMap vs TreeMap), Multithreading, and Web Servlets/JDBC instead.',
    'Deep Mathematical Derivations of Runge-Kutta Order Formulas': 'Memorize the RK4 weighted slope formula and solve 3 standard ODE practice problems instead.',
    'Advanced Distributed Microservices (Kubernetes, Service Mesh, Kafka)': 'Focus on single-node Linux VPS deployment, Docker, systemd, SQLite WAL mode, and REST APIs.',
    'Obsolete Assembly Language or 8086 Microprocessor Details': 'Master Python runtime internals (GIL, memory reference counts) and OS Process/Thread concepts.'
  };

  container.innerHTML = `
    <div class="triage-header" style="margin-bottom: var(--space-6);">
      <div class="badge badge-danger" style="margin-bottom: var(--space-2);">FOCUS & BANDWIDTH PROTECTION</div>
      <h1 style="margin-bottom: var(--space-1);">${data.title}</h1>
      <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
        ${data.rationale}
      </p>
    </div>

    <!-- Triage Alert Banner -->
    <div class="card" style="border-left: 4px solid var(--color-danger); margin-bottom: var(--space-6); background: var(--color-danger-subtle);">
      <strong style="color: var(--color-danger); font-size: var(--font-size-base); display: block; margin-bottom: 4px;">
        ⚠️ The 80/20 Pareto Rule for 30-Day Preparation:
      </strong>
      <p style="font-size: var(--font-size-sm); color: var(--text-primary); margin: 0; line-height: 1.6;">
        80% of your exam marks and placement questions will come from 20% of core topics. Spending days memorizing low-yield trivia or obsolete frameworks guarantees burnout without improving your placement or SGPA outcomes.
      </p>
    </div>

    <!-- Deferred Topics Grid -->
    <h3 style="margin-bottom: var(--space-4);">🚫 Explicit Topics to Defer or Ignore</h3>
    <div style="display: flex; flex-direction: column; gap: var(--space-4); margin-bottom: var(--space-6);">
      ${data.deferred_topics.map(item => `
        <div class="card" style="margin-bottom: 0; border-left: 4px solid var(--color-danger);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-2);">
            <h4 style="margin: 0; font-size: var(--font-size-lg); color: var(--color-danger);">
              ✕ DO NOT STUDY: ${item.topic}
            </h4>
            <span class="badge badge-danger">Deferred</span>
          </div>

          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6; margin-bottom: var(--space-3);">
            <strong>Why Ignore:</strong> ${item.reason}
          </p>

          <div style="background: var(--color-success-subtle); border-left: 3px solid var(--color-success); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-sm); color: var(--text-primary);">
            <strong>✓ Study This High-Yield Equivalent Instead:</strong> ${alternatives[item.topic] || 'Focus on Core CS and 15-mark university rubrics.'}
          </div>
        </div>
      `).join('')}
    </div>

    <!-- Daily Study Allocation Recommendation -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title">⏰ Recommended Daily Study Time Allocation (Total: 6 Hours)</h3>
        <span class="badge badge-primary">Balanced Daily Protocol</span>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-3);">
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); text-align: center;">
          <div style="font-size: var(--font-size-xl); font-weight: 800; color: var(--color-primary);">90 Mins</div>
          <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Semester 5 Theory</div>
          <div style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 2px;">Subject Notes & 15m PYQs</div>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); text-align: center;">
          <div style="font-size: var(--font-size-xl); font-weight: 800; color: var(--color-warning);">75 Mins</div>
          <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Placement Aptitude</div>
          <div style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 2px;">4-Tier Drills & Shortcuts</div>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); text-align: center;">
          <div style="font-size: var(--font-size-xl); font-weight: 800; color: var(--color-success);">90 Mins</div>
          <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Python Coding DSA</div>
          <div style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 2px;">2 Problems & Edge Cases</div>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); text-align: center;">
          <div style="font-size: var(--font-size-xl); font-weight: 800; color: var(--color-info);">45 Mins</div>
          <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Core CS & Projects</div>
          <div style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 2px;">OS/DBMS & Project Defense</div>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); text-align: center;">
          <div style="font-size: var(--font-size-xl); font-weight: 800; color: var(--text-primary);">60 Mins</div>
          <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Test & Revision</div>
          <div style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 2px;">8-Q Test & Spaced Review</div>
        </div>
      </div>
    </div>
  `;
}
