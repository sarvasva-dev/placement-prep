/**
 * Complete Daily Study Operating System Page View (Day 1 to 30)
 */

import { Storage } from '../storage.js';

export function renderDayView(container, dayNumber, daysIndex) {
  const dayNum = parseInt(dayNumber, 10);
  Storage.setActiveDay(dayNum);

  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING STUDY CHAPTER...</div>
      <h2>Retrieving Day ${dayNum} Structured Content</h2>
    </div>
  `;

  // Fetch structured JSON for this day
  const paddedDay = dayNum.toString().padStart(2, '0');
  fetch(`content/days/day${paddedDay}.json`)
    .then(res => {
      if (!res.ok) throw new Error(`Day ${dayNum} content not found`);
      return res.json();
    })
    .then(data => {
      buildDayPage(container, data, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Day ${dayNum}</h3>
          <p>${err.message}</p>
          <a href="#dashboard" class="btn btn-secondary">Return to Dashboard</a>
        </div>
      `;
    });
}

function buildDayPage(container, d, daysIndex) {
  const dayNum = d.day;
  const isDone = Storage.isDayComplete(dayNum);
  const checklist = Storage.getDayChecklist(dayNum);
  const sem = d.sem_data || {};
  const apt = d.apt_data || {};
  const dsa = d.dsa_problems || [];
  const cs = d.cs_core || {};
  const proj = d.project_defense || {};
  const test = d.daily_test || {};

  container.innerHTML = `
    <!-- Top Action Navigation -->
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: var(--space-3); margin-bottom: var(--space-5);">
      <div style="display: flex; gap: var(--space-2); align-items: center;">
        <a href="#day/${Math.max(1, dayNum - 1)}" class="btn btn-secondary btn-sm" ${dayNum === 1 ? 'disabled style="pointer-events: none; opacity: 0.5;"' : ''}>← Day ${dayNum - 1}</a>
        <span style="font-weight: 700; font-size: var(--font-size-sm); color: var(--text-muted);">Day ${dayNum} of 30</span>
        <a href="#day/${Math.min(30, dayNum + 1)}" class="btn btn-secondary btn-sm" ${dayNum === 30 ? 'disabled style="pointer-events: none; opacity: 0.5;"' : ''}>Day ${dayNum + 1} →</a>
      </div>

      <div style="display: flex; gap: var(--space-2); align-items: center;">
        <button id="toggle-focus-mode" class="btn btn-secondary btn-sm" title="Toggle Distraction-Free Study View">
          <span>🎯 Focus Mode</span>
        </button>
        <button id="print-day-btn" class="btn btn-secondary btn-sm" title="Print this day to PDF">
          <span>🖨️ Print / PDF</span>
        </button>
        <button id="mark-day-complete-top" class="btn ${isDone ? 'btn-success' : 'btn-primary'} btn-sm">
          <span>${isDone ? '✓ Day Completed' : 'Mark Day Complete'}</span>
        </button>
      </div>
    </div>

    <!-- Chapter Header -->
    <div class="card" style="border-top: 4px solid var(--color-primary); margin-bottom: var(--space-6);">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2);">
        <div>
          <div class="badge badge-primary">DAY ${dayNum} OF 30 STUDY CHAPTER</div>
          <h1 style="margin: var(--space-2) 0 var(--space-1);">${d.title}</h1>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary);">
            Academic Focus: <strong>${sem.subject || 'General'}</strong> • Target: <strong>SGPA ≥ 9.0 Standard</strong>
          </p>
        </div>
      </div>
    </div>

    <!-- Table of Contents Quick Anchor Bar -->
    <div class="tabs-header" style="position: sticky; top: var(--header-height); z-index: 80; background: var(--bg-primary); padding: var(--space-2) 0;">
      <a href="#day/${dayNum}#sec-sem" class="tab-btn active">1. Academic Study</a>
      <a href="#day/${dayNum}#sec-pyq" class="tab-btn">2. University PYQ</a>
      <a href="#day/${dayNum}#sec-apt" class="tab-btn">3. Aptitude Drills</a>
      <a href="#day/${dayNum}#sec-code" class="tab-btn">4. Python DSA</a>
      <a href="#day/${dayNum}#sec-cs" class="tab-btn">5. Core CS</a>
      <a href="#day/${dayNum}#sec-proj" class="tab-btn">6. Project Defense</a>
      <a href="#day/${dayNum}#sec-test" class="tab-btn">7. Daily Test</a>
      <a href="#day/${dayNum}#sec-check" class="tab-btn">8. Sign-Off</a>
    </div>

    <!-- ================================================================= -->
    <!-- 1. SEMESTER ACADEMIC STUDY -->
    <!-- ================================================================= -->
    <section id="sec-sem" class="card" style="margin-top: var(--space-4);">
      <div class="card-header">
        <h2 class="card-title">📚 1. Semester 5 Deep Academic Lecture</h2>
        <span class="badge badge-purple">${sem.subject || 'Academic'}</span>
      </div>

      <div style="background: var(--bg-surface); padding: var(--space-3); border-radius: var(--radius-md); margin-bottom: var(--space-4); border: 1px solid var(--border-color);">
        <strong style="color: var(--color-primary); font-size: var(--font-size-sm);">Syllabus Module Focus:</strong>
        <div style="font-size: var(--font-size-base); font-weight: 600; margin-top: 2px;">${sem.topic || ''}</div>
      </div>

      <!-- Detailed Notes -->
      <div class="academic-notes-body" style="font-size: var(--font-size-base); line-height: 1.7;">
        ${(sem.detailed_notes || []).map(p => `<p style="margin-bottom: var(--space-3);">${p.replace(/\n/g, '<br>')}</p>`).join('')}
      </div>

      <!-- ASCII / System Architecture Diagram -->
      ${sem.diagram_ascii ? `
        <div style="margin: var(--space-5) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--color-primary);">Architecture & Flow Diagram</h4>
          <div class="diagram-box">${sem.diagram_ascii}</div>
        </div>
      ` : ''}

      <!-- Comparison Table -->
      ${sem.comparison_table ? `
        <div style="margin: var(--space-5) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--color-primary);">Key Comparative Analysis</h4>
          <div class="table-responsive">
            <table class="study-table">
              <thead>
                <tr>${sem.comparison_table.headers.map(h => `<th>${h}</th>`).join('')}</tr>
              </thead>
              <tbody>
                ${sem.comparison_table.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('')}
              </tbody>
            </table>
          </div>
        </div>
      ` : ''}

      <!-- Pedagogical Callouts -->
      ${sem.memorize ? `
        <div class="callout callout-memorize">
          <div class="callout-header">🚨 WHAT TO MEMORIZE (DAY ${dayNum})</div>
          <div>${sem.memorize}</div>
        </div>
      ` : ''}

      ${sem.understand ? `
        <div class="callout callout-understand">
          <div class="callout-header">💡 WHAT TO UNDERSTAND DEEPLY (DAY ${dayNum})</div>
          <div>${sem.understand}</div>
        </div>
      ` : ''}

      ${sem.common_mistakes ? `
        <div class="callout callout-mistake">
          <div class="callout-header">⚠️ COMMON EXAM MISTAKES TO AVOID</div>
          <div>${sem.common_mistakes}</div>
        </div>
      ` : ''}
    </section>

    <!-- ================================================================= -->
    <!-- 2. UNIVERSITY PYQ & MODEL ANSWER -->
    <!-- ================================================================= -->
    <section id="sec-pyq" class="card">
      <div class="card-header">
        <h2 class="card-title">🏛️ 2. University PYQ Analysis & Model Answer</h2>
        <span class="badge badge-danger">15-Mark Blueprint</span>
      </div>

      <div class="callout callout-exam-tip" style="margin-top: 0;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-3); font-size: var(--font-size-xs);">
          <div><strong>Exam Sessions:</strong> ${sem.pyq_year || 'CSJM University'}</div>
          <div><strong>Recurrence:</strong> ${sem.pyq_freq || 'Verified Paper Theme'}</div>
        </div>
        <div style="margin-top: var(--space-3); font-size: var(--font-size-base); font-weight: 700; color: var(--text-primary);">
          Q: ${sem.pyq_question || 'Explain the core topic in detail with neat diagrams.'}
        </div>
        <div style="margin-top: var(--space-2); font-size: var(--font-size-xs); color: var(--text-muted);">
          <strong>Marking Rubric:</strong> ${sem.pyq_rubric || 'Definition (3m) + Diagram (4m) + Technical Content (5m) + Comparison (3m) = 15 Marks'}
        </div>
      </div>

      <h3 style="margin: var(--space-4) 0 var(--space-3);">Model Answer (Full 15/15 Marks Presentation)</h3>
      <div style="background: var(--bg-surface); padding: var(--space-5); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        ${(sem.model_answer_paragraphs || []).map(([heading, body]) => `
          <div style="margin-bottom: var(--space-4);">
            <h4 style="color: var(--color-primary); margin-bottom: var(--space-2);">${heading}</h4>
            <p style="font-size: var(--font-size-sm); line-height: 1.7;">${body.replace(/\n/g, '<br>')}</p>
          </div>
        `).join('')}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 3. PLACEMENT APTITUDE -->
    <!-- ================================================================= -->
    <section id="sec-apt" class="card">
      <div class="card-header">
        <h2 class="card-title">⚡ 3. Placement Aptitude Mastery</h2>
        <span class="badge badge-warning">${apt.topic || 'Quantitative'}</span>
      </div>

      ${(apt.tutorial || []).map(p => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('')}

      ${apt.formulas ? `
        <div class="callout callout-memorize">
          <div class="callout-header">⚡ KEY FORMULAS & SHORTCUT TRICKS</div>
          <div><strong>Formulas:</strong> ${apt.formulas}</div>
          <div style="margin-top: 4px;"><strong>Speed Shortcut:</strong> ${apt.shortcut || 'Unit digit elimination.'}</div>
        </div>
      ` : ''}

      <h3 style="margin: var(--space-5) 0 var(--space-3);">4-Tier Progressively Challenging Solved Problems</h3>
      
      <!-- Tier 1 -->
      ${apt.tier1_problem ? `
        <div class="quiz-card">
          <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2);">
            <span class="badge badge-primary">Tier 1: Foundation</span>
          </div>
          <div class="quiz-question">${apt.tier1_problem.replace(/\n/g, '<br>')}</div>
          <button class="btn btn-secondary btn-sm toggle-ans-btn">Reveal Solution</button>
          <div class="quiz-answer-block">${apt.tier1_solution.replace(/\n/g, '<br>')}</div>
        </div>
      ` : ''}

      <!-- Tier 2 -->
      ${apt.tier2_problem ? `
        <div class="quiz-card">
          <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2);">
            <span class="badge badge-primary">Tier 2: Standard Placement</span>
          </div>
          <div class="quiz-question">${apt.tier2_problem.replace(/\n/g, '<br>')}</div>
          <button class="btn btn-secondary btn-sm toggle-ans-btn">Reveal Solution</button>
          <div class="quiz-answer-block">${apt.tier2_solution.replace(/\n/g, '<br>')}</div>
        </div>
      ` : ''}

      <!-- Tier 3 -->
      ${apt.tier3_problem ? `
        <div class="quiz-card">
          <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2);">
            <span class="badge badge-warning">Tier 3: TCS NQT / Infosys Pattern</span>
          </div>
          <div class="quiz-question">${apt.tier3_problem.replace(/\n/g, '<br>')}</div>
          <button class="btn btn-secondary btn-sm toggle-ans-btn">Reveal Solution</button>
          <div class="quiz-answer-block">${apt.tier3_solution.replace(/\n/g, '<br>')}</div>
        </div>
      ` : ''}

      <!-- Tier 4 -->
      ${apt.tier4_problem ? `
        <div class="quiz-card">
          <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2);">
            <span class="badge badge-danger">Tier 4: Advanced Hard Traps</span>
          </div>
          <div class="quiz-question">${apt.tier4_problem.replace(/\n/g, '<br>')}</div>
          <button class="btn btn-secondary btn-sm toggle-ans-btn">Reveal Solution</button>
          <div class="quiz-answer-block">${apt.tier4_solution.replace(/\n/g, '<br>')}</div>
        </div>
      ` : ''}

      <!-- 5 Speed Drills -->
      ${(apt.speed_drills || []).length > 0 ? `
        <h4 style="margin: var(--space-4) 0 var(--space-2); color: var(--color-warning);">5-Question Rapid Speed Drills (45s per problem)</h4>
        ${apt.speed_drills.map((drill, idx) => `
          <div class="quiz-card" style="padding: var(--space-3); margin-bottom: var(--space-2);">
            <div style="font-weight: 600; font-size: var(--font-size-sm);">#${idx + 1}: ${drill.q}</div>
            <button class="btn btn-secondary btn-sm toggle-ans-btn" style="margin-top: var(--space-2);">Check Answer</button>
            <div class="quiz-answer-block" style="font-size: var(--font-size-sm);">${drill.a}</div>
          </div>
        `).join('')}
      ` : ''}
    </section>

    <!-- ================================================================= -->
    <!-- 4. PYTHON CODING & DSA -->
    <!-- ================================================================= -->
    <section id="sec-code" class="card">
      <div class="card-header">
        <h2 class="card-title">💻 4. Placement Coding & Data Structures (Python)</h2>
        <span class="badge badge-success">${dsa.length} Problems Solved</span>
      </div>

      ${dsa.map(p => `
        <div style="margin-bottom: var(--space-6); border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-5);">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: var(--space-2);">
            <h3>${p.title}</h3>
            <span class="badge ${p.difficulty === 'Easy' ? 'badge-success' : 'badge-warning'}">${p.difficulty}</span>
          </div>
          <p style="font-size: var(--font-size-xs); color: var(--color-primary); font-weight: 600; margin-top: 2px;">${p.importance || ''}</p>
          
          <div class="callout callout-understand" style="margin: var(--space-3) 0;">
            <div class="callout-header">Problem Statement</div>
            <div>${p.problem_statement}</div>
          </div>

          <div style="font-size: var(--font-size-sm); margin-bottom: var(--space-3);">
            <strong>Algorithmic Strategy:</strong> ${p.solution_approach ? p.solution_approach.replace(/\n/g, '<br>') : ''}
          </div>

          <!-- Code Box -->
          <div class="code-container">
            <div class="code-header">
              <span>Python 3.10 Implementation</span>
              <button class="copy-code-btn" data-code="${encodeURIComponent(p.code || '')}">Copy Code</button>
            </div>
            <pre class="code-pre"><code>${p.code || ''}</code></pre>
          </div>

          <div style="display: flex; gap: var(--space-4); font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: var(--space-2); flex-wrap: wrap;">
            <div><strong>Time Complexity:</strong> ${p.time_complexity || 'O(N)'}</div>
            <div><strong>Space Complexity:</strong> ${p.space_complexity || 'O(1)'}</div>
            ${p.edge_cases ? `<div><strong>Edge Cases:</strong> ${p.edge_cases}</div>` : ''}
          </div>
        </div>
      `).join('')}
    </section>

    <!-- ================================================================= -->
    <!-- 5. CORE COMPUTER SCIENCE -->
    <!-- ================================================================= -->
    <section id="sec-cs" class="card">
      <div class="card-header">
        <h2 class="card-title">🖥️ 5. Core Computer Science Foundations</h2>
        <span class="badge badge-primary">${cs.subject || 'CS Core'}</span>
      </div>

      <div style="font-size: var(--font-size-base); font-weight: 700; color: var(--color-primary); margin-bottom: var(--space-3);">
        ${cs.topic || ''}
      </div>

      ${(cs.detailed_notes || []).map(p => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('')}

      ${(cs.interview_qa || []).map(qa => `
        <div class="callout callout-understand" style="margin-top: var(--space-3);">
          <div class="callout-header">🎯 TECHNICAL INTERVIEW QUESTION</div>
          <div style="font-weight: 700; color: var(--text-primary); margin-bottom: var(--space-2);">${qa.q}</div>
          <div style="font-size: var(--font-size-sm); color: var(--text-secondary);">${qa.a}</div>
        </div>
      `).join('')}
    </section>

    <!-- ================================================================= -->
    <!-- 6. PROJECT DEFENSE -->
    <!-- ================================================================= -->
    <section id="sec-proj" class="card">
      <div class="card-header">
        <h2 class="card-title">🛡️ 6. Project Architecture Defense</h2>
        <span class="badge badge-success">${proj.project_name || 'Project'}</span>
      </div>

      <div style="font-weight: 700; color: var(--color-primary); margin-bottom: var(--space-2);">
        Feature Focus: ${proj.feature_focus || 'Technical Architecture'}
      </div>

      <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-md); font-size: var(--font-size-sm); line-height: 1.7; border: 1px solid var(--border-color); margin-bottom: var(--space-4);">
        ${proj.architecture_deep_dive ? proj.architecture_deep_dive.replace(/\n/g, '<br>') : ''}
      </div>

      ${(proj.interview_qa || []).map(qa => `
        <div class="callout callout-memorize" style="margin-top: var(--space-3);">
          <div class="callout-header">🎯 PROJECT INTERVIEW CHALLENGE</div>
          <div style="font-weight: 700; color: var(--text-primary); margin-bottom: var(--space-2);">${qa.q}</div>
          <div style="font-size: var(--font-size-sm); color: var(--text-secondary);">${qa.a}</div>
        </div>
      `).join('')}
    </section>

    <!-- ================================================================= -->
    <!-- 7. DAILY 8-QUESTION MASTERY TEST -->
    <!-- ================================================================= -->
    <section id="sec-test" class="card" style="border-left: 4px solid var(--color-warning);">
      <div class="card-header">
        <h2 class="card-title">📝 7. Day ${dayNum} Comprehensive 8-Question Test</h2>
        <span class="badge badge-warning">Mastery Check</span>
      </div>
      <p style="font-size: var(--font-size-sm);">
        Test your retention across all 4 streams before signing off for the day. Click each question to reveal and review the full solution.
      </p>

      ${(test.questions || []).map((q, idx) => `
        <div class="quiz-card">
          <div style="display: flex; justify-content: space-between; font-size: var(--font-size-xs); color: var(--text-muted); margin-bottom: var(--space-1);">
            <span>QUESTION ${idx + 1} OF 8</span>
          </div>
          <div class="quiz-question">${q.q}</div>
          <button class="btn btn-secondary btn-sm toggle-ans-btn">Reveal Full Answer</button>
          <div class="quiz-answer-block">${q.a}</div>
        </div>
      `).join('')}
    </section>

    <!-- ================================================================= -->
    <!-- 8. DAY COMPLETION CHECKLIST & SIGN-OFF -->
    <!-- ================================================================= -->
    <section id="sec-check" class="card" style="border-top: 4px solid var(--color-success); background: var(--bg-surface);">
      <div class="card-header">
        <h2 class="card-title">✅ 8. Day ${dayNum} Execution Sign-Off</h2>
        <span class="badge ${isDone ? 'badge-success' : 'badge-warning'}">${isDone ? 'COMPLETED' : 'IN PROGRESS'}</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: var(--space-3); margin-bottom: var(--space-4);">
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-sem" ${checklist.sem ? 'checked' : ''}> Semester Lecture Studied
        </label>
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-pyq" ${checklist.pyq ? 'checked' : ''}> 15-Mark PYQ Solved
        </label>
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-apt" ${checklist.apt ? 'checked' : ''}> Aptitude Drills Solved
        </label>
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-code" ${checklist.code ? 'checked' : ''}> Python DSA Implemented
        </label>
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-cs" ${checklist.cs ? 'checked' : ''}> Core CS Concept Grasped
        </label>
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-proj" ${checklist.proj ? 'checked' : ''}> Project Defense Reviewed
        </label>
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-test" ${checklist.test ? 'checked' : ''}> Daily Test Attempted
        </label>
        <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
          <input type="checkbox" id="page-chk-rev" ${checklist.rev ? 'checked' : ''}> Flashcards Revised
        </label>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: var(--space-3);">
        <button id="final-day-complete-btn" class="btn ${isDone ? 'btn-success' : 'btn-primary'}" style="min-width: 200px;">
          <span>${isDone ? '✓ DAY MASTERED & COMPLETED' : 'COMPLETE DAY ' + dayNum}</span>
        </button>
      </div>
    </section>
  `;

  // Attach interactivity
  attachDayInteractivity(d);
}

function attachDayInteractivity(d) {
  const dayNum = d.day;

  // Toggle Answers in quiz cards
  document.querySelectorAll('.toggle-ans-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const block = btn.nextElementSibling;
      if (block) {
        block.classList.toggle('visible');
        btn.textContent = block.classList.contains('visible') ? 'Hide Answer' : 'Reveal Answer';
      }
    });
  });

  // Copy Code
  document.querySelectorAll('.copy-code-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const rawCode = decodeURIComponent(btn.getAttribute('data-code'));
      navigator.clipboard.writeText(rawCode).then(() => {
        btn.textContent = 'Copied!';
        setTimeout(() => { btn.textContent = 'Copy Code'; }, 2000);
      });
    });
  });

  // Print button
  document.getElementById('print-day-btn')?.addEventListener('click', () => {
    window.print();
  });

  // Focus Mode toggle
  document.getElementById('toggle-focus-mode')?.addEventListener('click', () => {
    document.body.classList.toggle('focus-mode');
  });

  // Checkbox bindings
  const syncChecklist = () => {
    const updated = {
      sem: document.getElementById('page-chk-sem')?.checked || false,
      pyq: document.getElementById('page-chk-pyq')?.checked || false,
      apt: document.getElementById('page-chk-apt')?.checked || false,
      code: document.getElementById('page-chk-code')?.checked || false,
      cs: document.getElementById('page-chk-cs')?.checked || false,
      proj: document.getElementById('page-chk-proj')?.checked || false,
      test: document.getElementById('page-chk-test')?.checked || false,
      rev: document.getElementById('page-chk-rev')?.checked || false
    };
    Storage.saveDayChecklist(dayNum, updated);
  };

  ['page-chk-sem', 'page-chk-pyq', 'page-chk-apt', 'page-chk-code', 'page-chk-cs', 'page-chk-proj', 'page-chk-test', 'page-chk-rev'].forEach(id => {
    document.getElementById(id)?.addEventListener('change', syncChecklist);
  });

  // Complete Day Buttons
  const toggleComplete = () => {
    const newState = Storage.toggleDayComplete(dayNum);
    const topBtn = document.getElementById('mark-day-complete-top');
    const btmBtn = document.getElementById('final-day-complete-btn');
    if (newState) {
      if (topBtn) topBtn.innerHTML = '<span>✓ Day Completed</span>';
      if (btmBtn) btmBtn.innerHTML = `<span>✓ DAY MASTERED & COMPLETED</span>`;
    } else {
      if (topBtn) topBtn.innerHTML = '<span>Mark Day Complete</span>';
      if (btmBtn) btmBtn.innerHTML = `<span>COMPLETE DAY ${dayNum}</span>`;
    }
  };

  document.getElementById('mark-day-complete-top')?.addEventListener('click', toggleComplete);
  document.getElementById('final-day-complete-btn')?.addEventListener('click', toggleComplete);
}
