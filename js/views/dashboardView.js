/**
 * Personalized Study Operating System Dashboard View
 */

import { Storage } from '../storage.js';

export function renderDashboard(container, daysIndex, semesterData) {
  const now = new Date();
  const hour = now.getHours();
  let greeting = 'Good evening';
  if (hour < 12) greeting = 'Good morning';
  else if (hour < 17) greeting = 'Good afternoon';

  const activeDay = Storage.getActiveDay();
  const completedCount = Storage.getCompletedDaysCount();
  const overallPercent = Math.round((completedCount / 30) * 100);
  const checklist = Storage.getDayChecklist(activeDay);
  
  // Calculate today's /100 score
  let todayScore = 0;
  if (checklist.sem) todayScore += 25;
  if (checklist.pyq) todayScore += 10;
  if (checklist.apt) todayScore += 20;
  if (checklist.code) todayScore += 15;
  if (checklist.cs) todayScore += 10;
  if (checklist.proj) todayScore += 10;
  if (checklist.rev) todayScore += 10;

  const currentDayMeta = daysIndex.find(d => d.day === activeDay) || daysIndex[0];

  container.innerHTML = `
    <div class="dashboard-header" style="margin-bottom: var(--space-6);">
      <div style="display: flex; align-items: flex-start; justify-content: space-between; flex-wrap: wrap; gap: var(--space-4);">
        <div>
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">PERSONAL STUDY OS • DAY ${activeDay} OF 30</div>
          <h1 style="margin-bottom: var(--space-1);">${greeting}, Sarthak</h1>
          <p style="font-size: var(--font-size-base); color: var(--text-secondary);">
            Preparation Target: <strong>Semester 5 SGPA ≥ 9.0</strong> & Campus Placement Clearance.
          </p>
        </div>
        <div style="display: flex; gap: var(--space-3); align-items: center;">
          <a href="#day/${activeDay}" class="btn btn-primary" style="box-shadow: var(--shadow-glow);">
            <span>🚀 Start Day ${activeDay} Study</span>
          </a>
        </div>
      </div>
    </div>

    <!-- Quick Stats Grid -->
    <div class="dashboard-stats-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); margin-bottom: var(--space-6);">
      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Overall 30-Day Velocity</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-primary); margin: var(--space-1) 0;">${overallPercent}%</div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">${completedCount} of 30 Days Mastered</div>
      </div>

      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Today's Study Score</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: ${todayScore >= 80 ? 'var(--color-success)' : 'var(--color-warning)'}; margin: var(--space-1) 0;">
          ${todayScore} / 100
        </div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">7-Category Daily Velocity</div>
      </div>

      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">SGPA 9.0 Target Status</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-purple); margin: var(--space-1) 0;">ON TRACK</div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">Target: ≥ 9.0 (All 4 Subjects)</div>
      </div>

      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Placement DSA Solved</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-success); margin: var(--space-1) 0;">50+ Problems</div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">Blind 75 & High-Frequency</div>
      </div>
    </div>

    <!-- Today's Execution Plan Card -->
    <div class="card" style="border-left: 4px solid var(--color-primary);">
      <div class="card-header">
        <div>
          <div style="font-size: var(--font-size-xs); color: var(--color-primary); font-weight: 700; text-transform: uppercase;">TODAY'S MISSION CONTROL</div>
          <h2 class="card-title" style="margin-top: 4px;">Day ${activeDay}: ${currentDayMeta.title}</h2>
        </div>
        <div style="display: flex; gap: var(--space-2);">
          <select id="day-selector-quick" class="btn btn-secondary btn-sm" style="font-family: var(--font-sans);">
            ${daysIndex.map(d => `<option value="${d.day}" ${d.day === activeDay ? 'selected' : ''}>Switch to Day ${d.day}</option>`).join('')}
          </select>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-4); margin-top: var(--space-3);">
        <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-2);">
            <span style="font-weight: 700; font-size: var(--font-size-sm); color: var(--color-purple);">📚 1. Semester 5 Academic</span>
            <input type="checkbox" id="chk-sem" ${checklist.sem ? 'checked' : ''} style="cursor: pointer; width: 16px; height: 16px;">
          </div>
          <div style="font-size: var(--font-size-sm); font-weight: 600;">${currentDayMeta.subject}</div>
          <p style="font-size: var(--font-size-xs); margin-top: 4px;">${currentDayMeta.topic}</p>
          <a href="#day/${activeDay}" class="btn btn-secondary btn-sm" style="margin-top: var(--space-2);">Open Lecture & PYQs →</a>
        </div>

        <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-2);">
            <span style="font-weight: 700; font-size: var(--font-size-sm); color: var(--color-warning);">⚡ 2. Placement Aptitude</span>
            <input type="checkbox" id="chk-apt" ${checklist.apt ? 'checked' : ''} style="cursor: pointer; width: 16px; height: 16px;">
          </div>
          <div style="font-size: var(--font-size-sm); font-weight: 600;">${currentDayMeta.aptitude}</div>
          <p style="font-size: var(--font-size-xs); margin-top: 4px;">4-Tier Drills, Shortcuts & Company Traps</p>
          <a href="#day/${activeDay}" class="btn btn-secondary btn-sm" style="margin-top: var(--space-2);">Solve Aptitude →</a>
        </div>

        <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-2);">
            <span style="font-weight: 700; font-size: var(--font-size-sm); color: var(--color-primary);">💻 3. Java DSA</span>
            <input type="checkbox" id="chk-code" ${checklist.code ? 'checked' : ''} style="cursor: pointer; width: 16px; height: 16px;">
          </div>
          <div style="font-size: var(--font-size-sm); font-weight: 600;">${Array.isArray(currentDayMeta.dsa) ? currentDayMeta.dsa.join(', ') : (currentDayMeta.dsa_pattern || currentDayMeta.dsa || 'Algorithmic Optimization')}</div>
          <p style="font-size: var(--font-size-xs); margin-top: 4px;">Line-by-line walks & complexities</p>
          <a href="#day/${activeDay}" class="btn btn-secondary btn-sm" style="margin-top: var(--space-2);">Code in Java →</a>
        </div>

        <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-2);">
            <span style="font-weight: 700; font-size: var(--font-size-sm); color: var(--color-success);">🛡️ 4. Project Defense & Core CS</span>
            <input type="checkbox" id="chk-proj" ${checklist.proj ? 'checked' : ''} style="cursor: pointer; width: 16px; height: 16px;">
          </div>
          <div style="font-size: var(--font-size-sm); font-weight: 600;">${currentDayMeta.project || 'System Design'}</div>
          <p style="font-size: var(--font-size-xs); margin-top: 4px;">Grounded in verified D:\\Projects code</p>
          <a href="#day/${activeDay}" class="btn btn-secondary btn-sm" style="margin-top: var(--space-2);">Defend Code →</a>
        </div>
      </div>
    </div>

    <!-- SGPA 9.0 Target Tracker -->
    <div class="card">
      <div class="card-header">
        <h2 class="card-title">🏛️ Academic SGPA 9.0 Target Tracker</h2>
        <span class="badge badge-purple">Target: ≥ 9.0 Standard</span>
      </div>
      <p style="font-size: var(--font-size-sm); margin-bottom: var(--space-4);">
        This tracker is a structured preparation and monitoring model based on the CSJM University Semester 5 marks and credit scheme.
      </p>

      <div class="table-responsive">
        <table class="study-table">
          <thead>
            <tr>
              <th>Paper Code</th>
              <th>Subject Title</th>
              <th>Credits</th>
              <th>Max Marks</th>
              <th>Target Marks</th>
              <th>PYQ Mastery</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>BCA-5001</strong></td>
              <td>Knowledge Management</td>
              <td>4</td>
              <td>100</td>
              <td><strong>92+</strong></td>
              <td><span class="badge badge-success">Units I–V Solved</span></td>
              <td><span class="badge badge-primary">TARGET ON TRACK</span></td>
            </tr>
            <tr>
              <td><strong>BCA-5002</strong></td>
              <td>Java Programming & Web Tech</td>
              <td>4</td>
              <td>100</td>
              <td><strong>94+</strong></td>
              <td><span class="badge badge-success">Servlets/JSP/JDBC Solved</span></td>
              <td><span class="badge badge-primary">TARGET ON TRACK</span></td>
            </tr>
            <tr>
              <td><strong>BCA-5003</strong></td>
              <td>Computer Networks</td>
              <td>4</td>
              <td>100</td>
              <td><strong>95+</strong></td>
              <td><span class="badge badge-success">OSI/TCP/CRC/RSA Solved</span></td>
              <td><span class="badge badge-primary">TARGET ON TRACK</span></td>
            </tr>
            <tr>
              <td><strong>BCA-5004</strong></td>
              <td>Numerical Methods</td>
              <td>4</td>
              <td>100</td>
              <td><strong>96+</strong></td>
              <td><span class="badge badge-success">NR/Gauss/Simpson/RK4 Solved</span></td>
              <td><span class="badge badge-primary">TARGET ON TRACK</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 30-Day Study Roadmap Matrix -->
    <div class="card">
      <div class="card-header">
        <h2 class="card-title">📅 30-Day Master Study Curriculum Timeline</h2>
        <span class="badge badge-primary">Click Any Day to Enter</span>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: var(--space-3);">
        ${daysIndex.map(d => {
          const isDone = Storage.isDayComplete(d.day);
          const isActive = d.day === activeDay;
          return `
            <a href="#day/${d.day}" class="card" style="margin-bottom: 0; padding: var(--space-3); text-align: center; border-color: ${isActive ? 'var(--color-primary)' : isDone ? 'var(--color-success)' : 'var(--border-color)'}; background: ${isActive ? 'var(--color-primary-subtle)' : isDone ? 'var(--color-success-subtle)' : 'var(--bg-surface)'}; text-decoration: none;">
              <div style="font-weight: 800; font-size: var(--font-size-base); color: ${isActive ? 'var(--color-primary)' : isDone ? 'var(--color-success)' : 'var(--text-primary)'};">
                DAY ${d.day}
              </div>
              <div style="font-size: 0.65rem; color: var(--text-muted); margin: 4px 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                ${d.subject.split(' ')[0]} • ${d.topic.substring(0, 15)}...
              </div>
              <div style="font-size: var(--font-size-xs); font-weight: 700;">
                ${isDone ? '<span style=\"color: var(--color-success);\">✓ DONE</span>' : isActive ? '<span style=\"color: var(--color-primary);\">ACTIVE</span>' : '<span style=\"color: var(--text-muted);\">OPEN</span>'}
              </div>
            </a>
          `;
        }).join('')}
      </div>
    </div>
  `;

  // Attach event listener for quick day selector
  const sel = document.getElementById('day-selector-quick');
  if (sel) {
    sel.addEventListener('change', (e) => {
      const targetDay = parseInt(e.target.value, 10);
      Storage.setActiveDay(targetDay);
      window.location.hash = `#day/${targetDay}`;
    });
  }

  // Attach checklist listener
  const updateChecklist = () => {
    const updated = {
      ...checklist,
      sem: document.getElementById('chk-sem')?.checked || false,
      apt: document.getElementById('chk-apt')?.checked || false,
      code: document.getElementById('chk-code')?.checked || false,
      proj: document.getElementById('chk-proj')?.checked || false
    };
    Storage.saveDayChecklist(activeDay, updated);
  };

  ['chk-sem', 'chk-apt', 'chk-code', 'chk-proj'].forEach(id => {
    document.getElementById(id)?.addEventListener('change', updateChecklist);
  });
}
