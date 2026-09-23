/**
 * Campus Placement Aptitude & Logical Reasoning Practice Hub View
 */

import { Storage } from '../storage.js';
import { StudyTimer } from '../timer.js';

export function renderAptitudeView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING APTITUDE HUB...</div>
      <h2>Retrieving 30-Day Placement Aptitude Matrix</h2>
    </div>
  `;

  fetch('content/aptitude/all_aptitude.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load Aptitude data');
      return res.json();
    })
    .then(aptList => {
      buildAptitudePage(container, aptList, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Aptitude Data</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildAptitudePage(container, aptList, daysIndex) {
  let activeTopicIdx = 0; // Default to Day 1 topic

  container.innerHTML = `
    <div class="aptitude-header" style="margin-bottom: var(--space-6);">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-4);">
        <div>
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">QUANTITATIVE & LOGICAL REASONING</div>
          <h1 style="margin-bottom: var(--space-1);">Placement Aptitude Practice Hub</h1>
          <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
            Targeted preparation for TCS NQT, Infosys, Cognizant, Wipro, and Accenture. 4-tier problem progression with instant speed shortcuts and step-by-step proofs.
          </p>
        </div>

        <!-- Integrated Speed Stopwatch Card -->
        <div class="card" style="margin-bottom: 0; padding: var(--space-3) var(--space-4); display: flex; align-items: center; gap: var(--space-3); border-color: var(--color-primary);">
          <div>
            <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Aptitude Speed Timer</div>
            <div id="apt-timer-display" style="font-family: var(--font-family-mono); font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-primary);">
              05:00
            </div>
          </div>
          <div style="display: flex; flex-direction: column; gap: 4px;">
            <button id="apt-timer-start" class="btn btn-primary btn-sm" style="padding: 2px 10px;">Start</button>
            <button id="apt-timer-reset" class="btn btn-secondary btn-sm" style="padding: 2px 10px;">Reset</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Topic Directory Selector Grid -->
    <div class="card" style="margin-bottom: var(--space-6); padding: var(--space-4);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
        <h3 class="card-title" style="font-size: var(--font-size-base); margin: 0;">Select Aptitude Day Topic (1 to 30)</h3>
        <span class="badge badge-secondary">${aptList.length} Modules Available</span>
      </div>
      <div style="display: flex; gap: var(--space-2); overflow-x: auto; padding-bottom: var(--space-2);">
        ${aptList.map((item, idx) => `
          <button class="btn ${idx === 0 ? 'btn-primary' : 'btn-secondary'} btn-sm apt-topic-btn" data-idx="${idx}" style="white-space: nowrap;">
            Day ${item.day}: ${item.topic.split('—')[0].trim()}
          </button>
        `).join('')}
      </div>
    </div>

    <!-- Active Topic Workspace -->
    <div id="apt-topic-workspace">
      <!-- Rendered dynamically -->
    </div>
  `;

  // Initialize timer
  const timerDisplay = container.querySelector('#apt-timer-display');
  const timerStartBtn = container.querySelector('#apt-timer-start');
  const timerResetBtn = container.querySelector('#apt-timer-reset');
  let studyTimer = new StudyTimer(timerDisplay, null, () => {
    alert('⏰ Time is up! Review your speed and accuracy.');
  });
  studyTimer.setDuration(5);

  timerStartBtn.addEventListener('click', () => {
    if (studyTimer.isRunning) {
      studyTimer.pause();
      timerStartBtn.textContent = 'Start';
      timerStartBtn.classList.remove('btn-warning');
      timerStartBtn.classList.add('btn-primary');
    } else {
      studyTimer.start();
      timerStartBtn.textContent = 'Pause';
      timerStartBtn.classList.remove('btn-primary');
      timerStartBtn.classList.add('btn-warning');
    }
  });

  timerResetBtn.addEventListener('click', () => {
    studyTimer.stop();
    timerStartBtn.textContent = 'Start';
    timerStartBtn.classList.remove('btn-warning');
    timerStartBtn.classList.add('btn-primary');
  });

  // Render active topic details
  const workspace = container.querySelector('#apt-topic-workspace');
  const topicBtns = container.querySelectorAll('.apt-topic-btn');

  function renderTopic(idx) {
    const item = aptList[idx];
    if (!item) return;

    workspace.innerHTML = `
      <!-- Header Banner -->
      <div class="card" style="border-left: 4px solid var(--color-primary); margin-bottom: var(--space-5);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-2);">
          <div>
            <div class="badge badge-primary" style="margin-bottom: var(--space-1);">DAY ${item.day} APTITUDE MODULE</div>
            <h2 style="margin: 0;">${item.topic}</h2>
          </div>
          <a href="#day/${item.day}" class="btn btn-secondary btn-sm">Full Day ${item.day} Study Page →</a>
        </div>
      </div>

      <!-- Theory Tutorial & Speed Shortcut Grid -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--space-4); margin-bottom: var(--space-5);">
        <!-- Formulas Card -->
        <div class="card" style="margin-bottom: 0;">
          <div class="card-header">
            <h3 class="card-title">📐 Master Formulas & Ratios</h3>
            <span class="badge badge-primary">Formulas</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); font-family: var(--font-family-mono); font-size: var(--font-size-sm); line-height: 1.6; white-space: pre-line;">
            ${item.formulas || 'Formula reference included in problem steps below.'}
          </div>
        </div>

        <!-- Speed Shortcut Card -->
        <div class="card" style="margin-bottom: 0;">
          <div class="card-header">
            <h3 class="card-title">⚡ 30-Second Speed Shortcut</h3>
            <span class="badge badge-warning">Speed Rule</span>
          </div>
          <div style="background: var(--color-warning-subtle); border-left: 3px solid var(--color-warning); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-sm); line-height: 1.6; color: var(--text-primary); white-space: pre-line;">
            ${item.shortcut || 'Instant elimination techniques included in solutions.'}
          </div>
        </div>
      </div>

      ${item.recognition ? `
        <div class="card" style="margin-bottom: var(--space-5); background: var(--bg-surface-2); border-left: 3px solid var(--color-info);">
          <strong style="color: var(--color-info); display: block; margin-bottom: 4px; font-size: var(--font-size-sm);">🎯 Pattern Recognition Trigger Phrases:</strong>
          <span style="font-size: var(--font-size-sm); color: var(--text-secondary);">${item.recognition}</span>
        </div>
      ` : ''}

      <!-- 4-Tier Problem Progression -->
      <h3 style="margin-bottom: var(--space-4);">🎯 4-Tier Graded Problem Progression</h3>
      <div style="display: flex; flex-direction: column; gap: var(--space-4); margin-bottom: var(--space-6);">
        
        <!-- Tier 1 -->
        ${renderProblemCard(1, 'Tier 1: Foundation Concept', item.tier1_problem, item.tier1_solution, 'var(--color-info)', 'badge-info')}

        <!-- Tier 2 -->
        ${renderProblemCard(2, 'Tier 2: Standard Placement Level', item.tier2_problem, item.tier2_solution, 'var(--color-primary)', 'badge-primary')}

        <!-- Tier 3 -->
        ${renderProblemCard(3, `Tier 3: Verified Company Question ${item.tier3_source ? `— ${item.tier3_source}` : ''}`, item.tier3_problem, item.tier3_solution, 'var(--color-success)', 'badge-success')}

        <!-- Tier 4 -->
        ${renderProblemCard(4, 'Tier 4: Hard / Time-Pressure Challenge', item.tier4_problem, item.tier4_solution, 'var(--color-warning)', 'badge-warning')}

      </div>

      <!-- Timed Drill Questions -->
      ${item.timed_set && item.timed_set.length ? `
        <div class="card" style="border-top: 3px solid var(--color-primary);">
          <div class="card-header">
            <h3 class="card-title">⏱️ Rapid-Fire Speed Drills</h3>
            <span class="badge badge-primary">Timed Assessment</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: var(--space-3);">
            ${item.timed_set.map((t, tidx) => `
              <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-sm);">
                <strong>${Array.isArray(t) ? t[0] : `Q${tidx+1}:`}</strong> ${Array.isArray(t) ? t[1] : t}
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}
    `;

    // Attach solution toggle listeners
    workspace.querySelectorAll('.toggle-sol-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.dataset.target;
        const panel = document.getElementById(targetId);
        if (panel) {
          const isHidden = panel.style.display === 'none';
          panel.style.display = isHidden ? 'block' : 'none';
          btn.textContent = isHidden ? '▲ Hide Step-by-Step Solution' : '▼ Reveal Complete Analytical Solution';
          btn.classList.toggle('btn-primary', isHidden);
          btn.classList.toggle('btn-secondary', !isHidden);
        }
      });
    });
  }

  function renderProblemCard(tierNum, title, problem, solution, accentColor, badgeClass) {
    if (!problem) return '';
    const solId = `apt-sol-tier-${tierNum}`;

    return `
      <div class="card" style="margin-bottom: 0; border-left: 4px solid ${accentColor};">
        <div class="card-header" style="padding-bottom: var(--space-2);">
          <span class="badge ${badgeClass}">${title}</span>
        </div>
        <div style="font-size: var(--font-size-base); font-weight: 600; line-height: 1.5; color: var(--text-primary); margin-bottom: var(--space-3);">
          ${problem}
        </div>

        <div>
          <button class="btn btn-secondary btn-sm toggle-sol-btn" data-target="${solId}" style="margin-bottom: var(--space-2);">
            ▼ Reveal Complete Analytical Solution
          </button>
          <div id="${solId}" style="display: none; background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-sm); border-left: 3px solid var(--color-success); font-size: var(--font-size-sm); line-height: 1.7; color: var(--text-secondary); white-space: pre-line; margin-top: var(--space-2);">
            <strong style="color: var(--color-success); display: block; margin-bottom: var(--space-2);">Step-by-Step Analytical Proof:</strong>
            ${solution}
          </div>
        </div>
      </div>
    `;
  }

  // Initial render of first topic
  renderTopic(0);

  // Topic button click handlers
  topicBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      topicBtns.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');
      const idx = parseInt(btn.dataset.idx, 10);
      renderTopic(idx);
    });
  });
}
