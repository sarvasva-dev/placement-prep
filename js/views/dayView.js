/**
 * Complete Daily Study Operating System Page View (Day 1 to 30)
 * Renders all 14 Multidisciplinary Preparation Streams with Interactive Capabilities
 */

import { Storage } from '../storage.js';

function safeText(value) {
  if (value == null) return '';
  if (typeof value === 'string') return value;
  if (Array.isArray(value)) return value.map(v => safeText(v)).join('\n');
  if (typeof value === 'object') {
    return Object.entries(value).map(([k, v]) => `${k}: ${safeText(v)}`).join('\n');
  }
  return String(value);
}

function formatMultiline(value) {
  return safeText(value).replace(/\n/g, '<br>');
}

function formatParagraphs(value) {
  const text = safeText(value);
  if (!text) return '';
  return text.split(/\n\s*\n/).map(p => `<p style="margin-bottom: var(--space-2);">${p.replace(/\n/g, '<br>')}</p>`).join('');
}

function normalizeOptions(options) {
  if (!options) return [];
  if (Array.isArray(options)) {
    return options.map((opt, idx) => ({
      letter: String.fromCharCode(65 + idx),
      text: safeText(opt)
    }));
  }
  if (typeof options === 'object') {
    return Object.entries(options).map(([k, v]) => ({
      letter: k.toUpperCase(),
      text: safeText(v)
    }));
  }
  return [];
}

export function renderDayView(container, dayNumber, daysIndex) {
  const dayNum = parseInt(dayNumber, 10);
  Storage.setActiveDay(dayNum);

  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING STUDY CHAPTER...</div>
      <h2>Retrieving Day ${dayNum} 14-Stream Curriculum</h2>
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

  // Extract stream data
  const streams = d.streams || {};
  const acad = streams.academic || d.sem_data || {};
  const pyqs = streams.academic_pyqs || acad.pyqs || [];
  const aptLesson = streams.aptitude_lesson || d.apt_data || {};
  const aptSolved = streams.aptitude_solved || d.apt_data?.solved_examples || [];
  const aptMcqs = streams.aptitude_mcqs || d.apt_data?.mcqs || [];
  const dsaPattern = streams.dsa_pattern || d.dsa_pattern || {};
  const codingProbs = streams.coding_problems || d.dsa_problems || [];
  const coreCs = streams.core_cs || d.cs_core || {};
  const proj = streams.project_preparation || d.project_defense || {};
  const placementInterview = streams.placement_interview || d.placement_interview || [];
  const revision = streams.daily_revision || d.daily_revision || {};
  const mixedTest = streams.mixed_test || d.daily_test?.mcqs || [];
  const codingTask = streams.daily_coding_task || d.daily_coding_task || {};
  const scoreModel = streams.daily_score_model || d.daily_score_model || { total_points: 100, passing_threshold: 80 };

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

    <!-- Chapter Header & 100-Point Live Tracker -->
    <div class="card" style="border-top: 4px solid var(--color-primary); margin-bottom: var(--space-5);">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-3);">
        <div style="flex: 1; min-width: 280px;">
          <div class="badge badge-primary">DAY ${dayNum} OF 30 • 14 PREPARATION STREAMS</div>
          <h1 style="margin: var(--space-2) 0 var(--space-1);">${d.title}</h1>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin: 0;">
            Academic Subject: <strong>${acad.subject_name || acad.subject || 'CSJM University'}</strong> • Daily Standard: <strong>SGPA ≥ 9.0 + Placement Ready</strong>
          </p>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-3) var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-color); text-align: right; min-width: 220px;">
          <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700;">DAILY MASTERY SCORE</div>
          <div style="font-size: 1.8rem; font-weight: 800; color: var(--color-primary); line-height: 1.2;">
            <span id="live-day-score">0</span> / 100
          </div>
          <div style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 2px;">
            Target Threshold: <strong style="color: var(--color-success);">80 Points (80%)</strong>
          </div>
        </div>
      </div>
    </div>

    <!-- Table of Contents Quick Anchor Bar (All 14 Streams) -->
    <div class="tabs-header" style="position: sticky; top: var(--header-height); z-index: 80; background: var(--bg-primary); padding: var(--space-2) 0; overflow-x: auto; white-space: nowrap; display: flex; gap: var(--space-2);">
      <a href="#day/${dayNum}#sec-acad" class="tab-btn active">1. Academic Theory</a>
      <a href="#day/${dayNum}#sec-pyq" class="tab-btn">2. University PYQs</a>
      <a href="#day/${dayNum}#sec-apt-lesson" class="tab-btn">3. Aptitude Lesson</a>
      <a href="#day/${dayNum}#sec-apt-solved" class="tab-btn">4. Aptitude Solved (5)</a>
      <a href="#day/${dayNum}#sec-apt-mcq" class="tab-btn">5. Aptitude MCQs (10)</a>
      <a href="#day/${dayNum}#sec-dsa-pattern" class="tab-btn">6. DSA Pattern</a>
      <a href="#day/${dayNum}#sec-coding-probs" class="tab-btn">7. Coding Problems (2)</a>
      <a href="#day/${dayNum}#sec-core-cs" class="tab-btn">8. Core CS</a>
      <a href="#day/${dayNum}#sec-proj-defense" class="tab-btn">9. Project Defense</a>
      <a href="#day/${dayNum}#sec-interview-prep" class="tab-btn">10. Placement Interview (5)</a>
      <a href="#day/${dayNum}#sec-revision" class="tab-btn">11. Daily Revision</a>
      <a href="#day/${dayNum}#sec-mixed-test" class="tab-btn">12. Mixed Test (20 MCQs)</a>
      <a href="#day/${dayNum}#sec-coding-task" class="tab-btn">13. Practical Task</a>
      <a href="#day/${dayNum}#sec-sign-off" class="tab-btn">14. Sign-Off (100 Pts)</a>
    </div>

    <!-- ================================================================= -->
    <!-- 1. ACADEMIC THEORY LECTURE -->
    <!-- ================================================================= -->
    <section id="sec-acad" class="card" style="margin-top: var(--space-4);">
      <div class="card-header">
        <h2 class="card-title">📚 1. Semester 5 Academic Theory</h2>
        <span class="badge badge-purple">${acad.subject_name || acad.subject || 'Academic'}</span>
      </div>

      <div style="background: var(--bg-surface); padding: var(--space-3); border-radius: var(--radius-md); margin-bottom: var(--space-4); border: 1px solid var(--border-color);">
        <strong style="color: var(--color-primary); font-size: var(--font-size-sm);">Syllabus Focus:</strong>
        <div style="font-size: var(--font-size-base); font-weight: 600; margin-top: 2px;">${acad.topic || ''}</div>
      </div>

      <!-- Objectives -->
      ${acad.objectives && acad.objectives.length ? `
        <div style="margin-bottom: var(--space-4); background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
          <strong style="font-size: var(--font-size-xs); text-transform: uppercase; color: var(--text-muted); display: block; margin-bottom: 4px;">LEARNING OBJECTIVES:</strong>
          <ul style="margin: 0; padding-left: 20px; font-size: var(--font-size-sm); line-height: 1.6;">
            ${acad.objectives.map(obj => `<li>${obj}</li>`).join('')}
          </ul>
        </div>
      ` : ''}

      <!-- Detailed Explanation -->
      <div class="academic-notes-body" style="font-size: var(--font-size-base); line-height: 1.7;">
        ${formatParagraphs(acad.explanation)}
      </div>

      <!-- Subtopics -->
      ${acad.subtopics && acad.subtopics.length ? `
        <div style="margin: var(--space-4) 0;">
          ${acad.subtopics.map(sub => `
            <div style="background: var(--bg-surface); padding: var(--space-3); border-radius: var(--radius-sm); margin-bottom: var(--space-3); border-left: 3px solid var(--color-primary);">
              <h4 style="margin: 0 0 var(--space-1); font-size: var(--font-size-base); color: var(--text-primary);">${sub.title}</h4>
              <p style="margin: 0; font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6;">${sub.content}</p>
            </div>
          `).join('')}
        </div>
      ` : ''}

      <!-- ASCII / Architecture Diagram -->
      ${acad.diagram ? `
        <div style="margin: var(--space-4) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--color-primary);">System Architecture & Conceptual Flow</h4>
          <div class="diagram-box">${acad.diagram}</div>
        </div>
      ` : ''}

      <!-- Comparison Table -->
      ${acad.comparison_table ? `
        <div style="margin: var(--space-4) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--color-primary);">Key Comparative Analysis</h4>
          <div class="table-responsive">
            <table class="study-table">
              <thead>
                <tr>${acad.comparison_table.headers.map(h => `<th>${h}</th>`).join('')}</tr>
              </thead>
              <tbody>
                ${acad.comparison_table.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('')}
              </tbody>
            </table>
          </div>
        </div>
      ` : ''}

      <!-- Callouts: Memorize / Understand / Mistakes -->
      ${acad.memorize ? `
        <div class="callout callout-memorize" style="margin-top: var(--space-3);">
          <div class="callout-header">🚨 WHAT TO MEMORIZE (DAY ${dayNum})</div>
          <div>${acad.memorize}</div>
        </div>
      ` : ''}

      ${acad.understand ? `
        <div class="callout callout-understand" style="margin-top: var(--space-3);">
          <div class="callout-header">💡 WHAT TO UNDERSTAND DEEPLY</div>
          <div>${acad.understand}</div>
        </div>
      ` : ''}

      ${acad.common_mistakes ? `
        <div class="callout callout-mistake" style="margin-top: var(--space-3);">
          <div class="callout-header">⚠️ COMMON EXAM MISTAKES TO AVOID</div>
          <div>${acad.common_mistakes}</div>
        </div>
      ` : ''}

      <!-- Academic Knowledge Check MCQs -->
      ${(acad.mcqs && acad.mcqs.length) ? `
        <h4 style="margin: var(--space-4) 0 var(--space-2); color: var(--color-primary);">Academic Concept Check (5 MCQs)</h4>
        <div style="display: flex; flex-direction: column; gap: var(--space-3); margin-top: var(--space-3);">
          ${acad.mcqs.map((mcq, idx) => {
            const opts = normalizeOptions(mcq.options);
            return `
              <div class="quiz-card mcq-interactive-card" data-correct="${mcq.correct_answer}" data-id="${mcq.id || 'ACAD-' + idx}" style="padding: var(--space-3);">
                <div style="font-weight: 600; font-size: var(--font-size-sm); margin-bottom: var(--space-2);">
                  #${idx + 1}: ${mcq.question}
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-2); margin-bottom: var(--space-2);">
                  ${opts.map(opt => `
                    <button class="btn btn-secondary btn-sm mcq-opt-btn" data-letter="${opt.letter}" style="justify-content: flex-start; text-align: left; padding: 8px 12px;">
                      <strong>${opt.letter})</strong>&nbsp;${opt.text}
                    </button>
                  `).join('')}
                </div>
                <div class="mcq-feedback-block" style="display: none; padding: var(--space-2); border-radius: var(--radius-sm); font-size: var(--font-size-xs);"></div>
              </div>
            `;
          }).join('')}
        </div>
      ` : ''}
    </section>

    <!-- ================================================================= -->
    <!-- 2. UNIVERSITY PYQ & MODEL ANSWER -->
    <!-- ================================================================= -->
    <section id="sec-pyq" class="card">
      <div class="card-header">
        <h2 class="card-title">🏛️ 2. CSJM University PYQs & Model Answers</h2>
        <span class="badge badge-danger">15-Mark University Standard</span>
      </div>

      ${pyqs.map((pyq, idx) => `
        <div style="margin-bottom: var(--space-5); border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-4);">
          <div class="callout callout-exam-tip" style="margin-top: 0;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: var(--space-2); font-size: var(--font-size-xs);">
              <div><strong>Session / Year:</strong> ${pyq.year || 'CSJM University'}</div>
              <div><strong>Paper Marks:</strong> ${pyq.marks || '15 Marks'}</div>
              <div><strong>Question Type:</strong> ${pyq.type || 'Authentic University Question'}</div>
            </div>
            <div style="margin-top: var(--space-3); font-size: var(--font-size-base); font-weight: 700; color: var(--text-primary);">
              Q${idx + 1}: ${pyq.question}
            </div>
            <div style="margin-top: var(--space-2); font-size: var(--font-size-xs); color: var(--text-muted);">
              <strong>Examiner Marking Rubric:</strong> ${pyq.rubric || 'Definition (3m) + Diagram (4m) + Technical Depth (5m) + Summary (3m) = 15 Marks'}
            </div>
          </div>

          <h4 style="margin: var(--space-3) 0 var(--space-2); color: var(--color-primary);">Full Model Answer (15/15 Presentation)</h4>
          <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-color); font-size: var(--font-size-sm); line-height: 1.7;">
            ${formatParagraphs(pyq.model_answer)}
          </div>

          ${pyq.expected_examiner_points ? `
            <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); margin-top: var(--space-3); font-size: var(--font-size-xs); color: var(--text-secondary);">
              <strong>Key Points Evaluator Looks For:</strong> ${pyq.expected_examiner_points}
            </div>
          ` : ''}
        </div>
      `).join('')}
    </section>

    <!-- ================================================================= -->
    <!-- 3. PLACEMENT APTITUDE LESSON -->
    <!-- ================================================================= -->
    <section id="sec-apt-lesson" class="card">
      <div class="card-header">
        <h2 class="card-title">⚡ 3. Placement Aptitude Lesson</h2>
        <span class="badge badge-warning">${aptLesson.category || 'Quantitative'}</span>
      </div>

      <div style="font-weight: 700; font-size: var(--font-size-lg); color: var(--color-primary); margin-bottom: var(--space-2);">
        ${aptLesson.topic || 'Quantitative Aptitude'}
      </div>

      ${(Array.isArray(aptLesson.tutorial) ? aptLesson.tutorial : [aptLesson.tutorial || '']).map(p => `<p style="font-size: var(--font-size-sm); line-height: 1.7;">${formatMultiline(p)}</p>`).join('')}

      <div class="callout callout-memorize" style="margin-top: var(--space-3);">
        <div class="callout-header">⚡ KEY FORMULAS & SPEED SHORTCUTS</div>
        <div><strong>Essential Formulas:</strong><br>${formatMultiline(aptLesson.formulas)}</div>
        ${aptLesson.shortcuts ? `<div style="margin-top: var(--space-2);"><strong>Speed Shortcut:</strong> ${aptLesson.shortcuts}</div>` : ''}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 4. 5-TIER SOLVED APTITUDE PROBLEMS -->
    <!-- ================================================================= -->
    <section id="sec-apt-solved" class="card">
      <div class="card-header">
        <h2 class="card-title">🧮 4. Solved Aptitude Problems (${aptSolved.length} Worked Examples)</h2>
        <span class="badge badge-success">4-Tier Progression</span>
      </div>

      <div style="display: flex; flex-direction: column; gap: var(--space-3);">
        ${aptSolved.map((ex, idx) => `
          <div class="quiz-card" style="padding: var(--space-4);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-2);">
              <span class="badge badge-primary">${ex.difficulty || 'Tier ' + (idx + 1)}: ${ex.source || 'Placement Exam Pattern'}</span>
              <span style="font-size: var(--font-size-xs); color: var(--text-muted);">Target: ${ex.target_time_seconds || 45}s</span>
            </div>
            <div class="quiz-question" style="font-weight: 600; font-size: var(--font-size-sm); color: var(--text-primary); margin-bottom: var(--space-3);">
              #${idx + 1}: ${ex.problem}
            </div>
            <button class="btn btn-secondary btn-sm toggle-ans-btn">Reveal Step-by-Step Solution</button>
            <div class="quiz-answer-block" style="margin-top: var(--space-3); font-size: var(--font-size-sm); line-height: 1.6;">
              <strong style="color: var(--color-success); display: block; margin-bottom: var(--space-1);">Final Answer: ${ex.final_answer}</strong>
              <div>${formatMultiline(ex.step_by_step_solution)}</div>
            </div>
          </div>
        `).join('')}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 5. 10 INTERACTIVE APTITUDE MCQS -->
    <!-- ================================================================= -->
    <section id="sec-apt-mcq" class="card">
      <div class="card-header">
        <h2 class="card-title">🎯 5. Interactive Aptitude MCQs (10 Questions)</h2>
        <span class="badge badge-primary">Instant Evaluation</span>
      </div>
      <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-bottom: var(--space-4);">
        Click your chosen option to check correctness immediately and view step-by-step mathematical reasoning.
      </p>

      <div style="display: flex; flex-direction: column; gap: var(--space-3);">
        ${aptMcqs.map((mcq, idx) => {
          const opts = normalizeOptions(mcq.options);
          return `
            <div class="quiz-card mcq-interactive-card" data-correct="${mcq.correct_answer}" data-id="${mcq.id || 'APT-' + idx}" style="padding: var(--space-4);">
              <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2); font-size: var(--font-size-xs); color: var(--text-muted);">
                <span>QUESTION ${idx + 1} OF 10</span>
                <span class="badge badge-secondary">${mcq.id || ''}</span>
              </div>
              <div style="font-weight: 700; font-size: var(--font-size-sm); color: var(--text-primary); margin-bottom: var(--space-3);">
                ${mcq.question}
              </div>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-2); margin-bottom: var(--space-2);">
                ${opts.map(opt => `
                  <button class="btn btn-secondary btn-sm mcq-opt-btn" data-letter="${opt.letter}" style="justify-content: flex-start; text-align: left; padding: 8px 12px;">
                    <strong>${opt.letter})</strong>&nbsp;${opt.text}
                  </button>
                `).join('')}
              </div>
              <div class="mcq-feedback-block" style="display: none; padding: var(--space-3); border-radius: var(--radius-sm); margin-top: var(--space-2); font-size: var(--font-size-sm);"></div>
            </div>
          `;
        }).join('')}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 6. DSA PATTERN DEEP-DIVE -->
    <!-- ================================================================= -->
    <section id="sec-dsa-pattern" class="card">
      <div class="card-header">
        <h2 class="card-title">🧬 6. Algorithmic DSA Pattern Deep-Dive</h2>
        <span class="badge badge-success">${dsaPattern.pattern_name || 'Pattern'}</span>
      </div>

      <div style="margin-bottom: var(--space-4);">
        <h3 style="margin: 0 0 var(--space-2);">${dsaPattern.pattern_name}</h3>
        <p style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6;">${dsaPattern.concept}</p>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-sm); border-left: 3px solid var(--color-primary); margin-top: var(--space-2);">
          <strong>Why It Works:</strong> ${dsaPattern.why_it_works}
        </div>
      </div>

      <!-- Visual Representation -->
      ${dsaPattern.visual_explanation ? `
        <div style="margin: var(--space-4) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--color-primary);">Visual Execution Trace</h4>
          <div class="diagram-box">${dsaPattern.visual_explanation}</div>
        </div>
      ` : ''}

      <!-- Code Container -->
      <div class="code-container" style="margin: var(--space-4) 0;">
        <div class="code-header">
          <span>Java 17+ Pattern Implementation</span>
          <button class="copy-code-btn" data-code="${encodeURIComponent(dsaPattern.java_code || dsaPattern.code || dsaPattern.python_code || '')}">Copy Code</button>
        </div>
        <pre class="code-pre"><code>${dsaPattern.java_code || dsaPattern.code || dsaPattern.python_code || ''}</code></pre>
      </div>

      <!-- Line-by-Line Walkthrough -->
      ${dsaPattern.line_by_line_walkthrough && dsaPattern.line_by_line_walkthrough.length ? `
        <div style="margin: var(--space-4) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--text-primary);">Line-by-Line Execution Logic</h4>
          <ul style="margin: 0; padding-left: 20px; font-size: var(--font-size-sm); line-height: 1.6; color: var(--text-secondary);">
            ${dsaPattern.line_by_line_walkthrough.map(line => `<li>${line}</li>`).join('')}
          </ul>
        </div>
      ` : ''}

      <div style="display: flex; gap: var(--space-4); font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: var(--space-3); flex-wrap: wrap;">
        <div><strong>Complexity:</strong> ${dsaPattern.complexity || 'O(N) time, O(1) space'}</div>
        ${dsaPattern.edge_cases ? `<div><strong>Edge Cases:</strong> ${dsaPattern.edge_cases}</div>` : ''}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 7. PLACEMENT CODING PROBLEMS (2) -->
    <!-- ================================================================= -->
    <section id="sec-coding-probs" class="card">
      <div class="card-header">
        <h2 class="card-title">💻 7. Placement Coding Problems (2 Solved)</h2>
        <span class="badge badge-primary">Java 17+ Implementation</span>
      </div>

      ${codingProbs.map((prob, idx) => `
        <div style="margin-bottom: var(--space-6); border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-4);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-2);">
            <h3 style="margin: 0;">${prob.title}</h3>
            <span class="badge ${prob.difficulty === 'Easy' ? 'badge-success' : 'badge-warning'}">${prob.difficulty || 'Medium'}</span>
          </div>

          <div class="callout callout-understand" style="margin: var(--space-3) 0;">
            <div class="callout-header">Problem Statement & Constraints</div>
            <div>${prob.problem_statement}</div>
            ${prob.edge_cases ? `<div style="margin-top: var(--space-2); font-size: var(--font-size-xs); color: var(--text-muted);"><strong>Constraints:</strong> ${prob.edge_cases}</div>` : ''}
          </div>

          <div style="font-size: var(--font-size-sm); margin-bottom: var(--space-3); color: var(--text-secondary);">
            <strong>Algorithmic Strategy:</strong> ${formatMultiline(prob.solution_approach)}
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>Java 17+ Solution</span>
              <button class="copy-code-btn" data-code="${encodeURIComponent(prob.java_code || prob.code || prob.solution_python || '')}">Copy Code</button>
            </div>
            <pre class="code-pre"><code>${prob.java_code || prob.code || prob.solution_python || ''}</code></pre>
          </div>

          <div style="display: flex; gap: var(--space-4); font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: var(--space-2);">
            <div><strong>Time Complexity:</strong> ${prob.time_complexity || 'O(N)'}</div>
            <div><strong>Space Complexity:</strong> ${prob.space_complexity || 'O(1)'}</div>
          </div>
        </div>
      `).join('')}
    </section>

    <!-- ================================================================= -->
    <!-- 8. CORE COMPUTER SCIENCE -->
    <!-- ================================================================= -->
    <section id="sec-core-cs" class="card">
      <div class="card-header">
        <h2 class="card-title">🖥️ 8. Core Computer Science Foundations</h2>
        <span class="badge badge-primary">${coreCs.subject || 'Core CS'}</span>
      </div>

      <div style="font-size: var(--font-size-lg); font-weight: 700; color: var(--color-primary); margin-bottom: var(--space-3);">
        ${coreCs.topic || ''}
      </div>

      <div style="font-size: var(--font-size-sm); line-height: 1.7; color: var(--text-secondary); margin-bottom: var(--space-4);">
        ${formatParagraphs(coreCs.concept_lesson || (Array.isArray(coreCs.detailed_notes) ? coreCs.detailed_notes.join('\n\n') : coreCs.detailed_notes))}
      </div>

      <!-- Key Definitions -->
      ${coreCs.key_definitions && coreCs.key_definitions.length ? `
        <div style="margin-bottom: var(--space-4);">
          <h4 style="margin-bottom: var(--space-2); color: var(--text-primary);">Must-Know Technical Definitions</h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: var(--space-2);">
            ${coreCs.key_definitions.map(d => `
              <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-primary);">
                <strong style="color: var(--color-primary); font-size: var(--font-size-sm);">${d.term}</strong>
                <p style="margin: 4px 0 0; font-size: var(--font-size-xs); color: var(--text-secondary);">${d.definition}</p>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}

      <!-- 5 Interview Q&As -->
      <h4 style="margin: var(--space-4) 0 var(--space-2); color: var(--color-primary);">Top 5 Core CS Technical Interview Questions</h4>
      <div style="display: flex; flex-direction: column; gap: var(--space-3);">
        ${(coreCs.interview_questions || coreCs.interview_qa || []).map((qa, idx) => `
          <div class="callout callout-understand" style="margin: 0;">
            <div class="callout-header">Q${idx + 1}: ${qa.q}</div>
            <div style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-top: var(--space-1);">${qa.a}</div>
          </div>
        `).join('')}
      </div>

      <!-- 5 Core CS MCQs -->
      ${coreCs.mcqs && coreCs.mcqs.length ? `
        <h4 style="margin: var(--space-5) 0 var(--space-2); color: var(--color-primary);">Core CS Knowledge Check (5 MCQs)</h4>
        <div style="display: flex; flex-direction: column; gap: var(--space-3);">
          ${coreCs.mcqs.map((mcq, idx) => {
            const opts = normalizeOptions(mcq.options);
            return `
              <div class="quiz-card mcq-interactive-card" data-correct="${mcq.correct_answer}" data-id="${mcq.id || 'CS-' + idx}" style="padding: var(--space-3);">
                <div style="font-weight: 600; font-size: var(--font-size-sm); margin-bottom: var(--space-2);">
                  #${idx + 1}: ${mcq.question}
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-2); margin-bottom: var(--space-2);">
                  ${opts.map(opt => `
                    <button class="btn btn-secondary btn-sm mcq-opt-btn" data-letter="${opt.letter}" style="justify-content: flex-start; text-align: left; padding: 8px 12px;">
                      <strong>${opt.letter})</strong>&nbsp;${opt.text}
                    </button>
                  `).join('')}
                </div>
                <div class="mcq-feedback-block" style="display: none; padding: var(--space-2); border-radius: var(--radius-sm); font-size: var(--font-size-xs);"></div>
              </div>
            `;
          }).join('')}
        </div>
      ` : ''}
    </section>

    <!-- ================================================================= -->
    <!-- 9. REAL PROJECT ARCHITECTURE DEFENSE -->
    <!-- ================================================================= -->
    <section id="sec-proj-defense" class="card">
      <div class="card-header">
        <h2 class="card-title">🛡️ 9. Real Project Architecture Defense</h2>
        <span class="badge badge-success">${proj.project_name || 'Project Defense'}</span>
      </div>

      <div style="font-weight: 700; color: var(--color-primary); margin-bottom: var(--space-2);">
        Feature Focus: ${proj.topic || proj.feature_focus || 'System Architecture'}
      </div>
      <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-family: var(--font-family-mono); margin-bottom: var(--space-3);">
        Verified Workspace: <code>${proj.repo_path || 'D:\\Projects'}</code>
      </div>

      <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-md); font-size: var(--font-size-sm); line-height: 1.7; border: 1px solid var(--border-color); margin-bottom: var(--space-4);">
        ${formatMultiline(proj.what_to_understand || proj.architecture_deep_dive || '')}
      </div>

      ${proj.interview_pitch_exercise ? `
        <div class="callout callout-exam-tip" style="margin-bottom: var(--space-4);">
          <div class="callout-header">🎤 60-SECOND INTERVIEW ELEVATOR PITCH</div>
          <div style="font-size: var(--font-size-sm); line-height: 1.6;">${proj.interview_pitch_exercise}</div>
        </div>
      ` : ''}

      <!-- Project Interview Defense Q&As -->
      <h4 style="margin: var(--space-3) 0 var(--space-2); color: var(--color-primary);">Technical Interview Defense Questions</h4>
      <div style="display: flex; flex-direction: column; gap: var(--space-3);">
        ${(proj.interview_questions || proj.interview_qa || []).map(qa => `
          <div class="callout callout-memorize" style="margin: 0;">
            <div class="callout-header">🎯 ${qa.q}</div>
            <div style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-top: var(--space-1);">${qa.a}</div>
          </div>
        `).join('')}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 10. PLACEMENT & BEHAVIORAL INTERVIEW PREPARATION -->
    <!-- ================================================================= -->
    <section id="sec-interview-prep" class="card">
      <div class="card-header">
        <h2 class="card-title">👔 10. Placement Interview Preparation (5 Questions)</h2>
        <span class="badge badge-primary">Technical + STAR + HR</span>
      </div>

      <div style="display: flex; flex-direction: column; gap: var(--space-4);">
        ${placementInterview.map((item, idx) => `
          <div style="border-left: 3px solid var(--color-primary); padding-left: var(--space-3); background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-1);">
              <span class="badge badge-secondary" style="font-size: 0.7rem;">${item.category}</span>
              <span style="font-size: var(--font-size-xs); color: var(--text-muted);">Question ${idx + 1} of 5</span>
            </div>
            <strong style="font-size: var(--font-size-base); color: var(--text-primary); display: block; margin-bottom: var(--space-2);">
              Q: ${item.question}
            </strong>
            <button class="btn btn-secondary btn-sm toggle-ans-btn" style="margin-bottom: var(--space-2);">Reveal Senior Model Answer</button>
            <div class="quiz-answer-block" style="font-size: var(--font-size-sm); line-height: 1.7; color: var(--text-secondary);">
              <div style="margin-bottom: var(--space-2);">${formatMultiline(item.model_answer)}</div>
              ${item.key_talking_points && item.key_talking_points.length ? `
                <div style="margin-top: var(--space-2); background: var(--bg-surface); padding: var(--space-2); border-radius: var(--radius-xs);">
                  <strong style="color: var(--color-primary); font-size: var(--font-size-xs);">Key Talking Points:</strong>
                  <ul style="margin: 4px 0 0; padding-left: 20px; font-size: var(--font-size-xs);">
                    ${item.key_talking_points.map(pt => `<li>${pt}</li>`).join('')}
                  </ul>
                </div>
              ` : ''}
            </div>
          </div>
        `).join('')}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 11. DAILY ACTIVE REVISION & RAPID-FIRE FLASHCARDS -->
    <!-- ================================================================= -->
    <section id="sec-revision" class="card">
      <div class="card-header">
        <h2 class="card-title">🔄 11. Daily Active Recall & Rapid-Fire Drills</h2>
        <span class="badge badge-warning">Nightly Consolidation</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-3); margin-bottom: var(--space-4);">
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-warning);">
          <strong style="color: var(--color-warning); font-size: var(--font-size-xs); text-transform: uppercase;">1. YESTERDAY RECALL:</strong>
          <p style="margin: 4px 0 0; font-size: var(--font-size-sm); white-space: pre-line;">${revision.yesterday_recall || 'Review prior day principles.'}</p>
        </div>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-primary);">
          <strong style="color: var(--color-primary); font-size: var(--font-size-xs); text-transform: uppercase;">2. TODAY'S RECALL:</strong>
          <p style="margin: 4px 0 0; font-size: var(--font-size-sm); white-space: pre-line;">${revision.today_recall || revision.today_summary || 'Master today\'s core syllabus.'}</p>
        </div>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-purple);">
          <strong style="color: var(--color-purple); font-size: var(--font-size-xs); text-transform: uppercase;">3. FORMULA RECALL:</strong>
          <p style="margin: 4px 0 0; font-size: var(--font-size-sm); white-space: pre-line;">${revision.formula_recall || 'Speed calculation shortcuts and complexity bounds.'}</p>
        </div>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-danger);">
          <strong style="color: var(--color-danger); font-size: var(--font-size-xs); text-transform: uppercase;">4. PYQ RECALL:</strong>
          <p style="margin: 4px 0 0; font-size: var(--font-size-sm); white-space: pre-line;">${revision.pyq_recall || '15-mark university presentation structure.'}</p>
        </div>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-info);">
          <strong style="color: var(--color-info); font-size: var(--font-size-xs); text-transform: uppercase;">5. DSA RECALL:</strong>
          <p style="margin: 4px 0 0; font-size: var(--font-size-sm); white-space: pre-line;">${revision.dsa_recall || 'Algorithmic pattern invariants and pointers.'}</p>
        </div>
        <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-success);">
          <strong style="color: var(--color-success); font-size: var(--font-size-xs); text-transform: uppercase;">6. PROJECT RECALL:</strong>
          <p style="margin: 4px 0 0; font-size: var(--font-size-sm); white-space: pre-line;">${revision.project_recall || 'Production architecture defense & metrics.'}</p>
        </div>
      </div>

      <h4 style="margin: var(--space-4) 0 var(--space-2); color: var(--color-primary);">10-Question Rapid-Fire Active Recall Flashcards</h4>
      <div style="display: flex; flex-direction: column; gap: var(--space-2);">
        ${(revision.rapid_fire_questions || []).map((q, idx) => `
          <div class="quiz-card" style="padding: var(--space-3);">
            <div style="font-weight: 600; font-size: var(--font-size-sm);">#${idx + 1}: ${q.q}</div>
            <button class="btn btn-secondary btn-sm toggle-ans-btn" style="margin-top: var(--space-1);">Reveal Answer</button>
            <div class="quiz-answer-block" style="font-size: var(--font-size-sm); color: var(--color-success); font-weight: 600; margin-top: var(--space-2);">
              ${q.a}
            </div>
          </div>
        `).join('')}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 12. MIXED DAILY MCQ TEST (20 MCQS) -->
    <!-- ================================================================= -->
    <section id="sec-mixed-test" class="card" style="border-left: 4px solid var(--color-warning);">
      <div class="card-header">
        <h2 class="card-title">📝 12. Mixed Daily Mastery Test (20 Questions)</h2>
        <span class="badge badge-warning">All 4 Pillars</span>
      </div>
      <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-bottom: var(--space-4);">
        Balanced 20-question test: 5 Academic + 5 Placement Aptitude + 5 Core Computer Science + 5 Coding & Projects.
      </p>

      <div style="display: flex; flex-direction: column; gap: var(--space-3);">
        ${mixedTest.map((mcq, idx) => {
          const opts = normalizeOptions(mcq.options);
          return `
            <div class="quiz-card mcq-interactive-card" data-correct="${mcq.correct_answer}" data-id="${mcq.id || 'TEST-' + idx}" style="padding: var(--space-4);">
              <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2); font-size: var(--font-size-xs); color: var(--text-muted);">
                <span class="badge badge-secondary">${mcq.category || 'Mixed Test'}</span>
                <span>QUESTION ${idx + 1} OF 20</span>
              </div>
              <div style="font-weight: 700; font-size: var(--font-size-sm); color: var(--text-primary); margin-bottom: var(--space-3);">
                ${mcq.question}
              </div>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-2); margin-bottom: var(--space-2);">
                ${opts.map(opt => `
                  <button class="btn btn-secondary btn-sm mcq-opt-btn" data-letter="${opt.letter}" style="justify-content: flex-start; text-align: left; padding: 8px 12px;">
                    <strong>${opt.letter})</strong>&nbsp;${opt.text}
                  </button>
                `).join('')}
              </div>
              <div class="mcq-feedback-block" style="display: none; padding: var(--space-3); border-radius: var(--radius-sm); margin-top: var(--space-2); font-size: var(--font-size-sm);"></div>
            </div>
          `;
        }).join('')}
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 13. DAILY TIMED PRACTICAL CODING CHALLENGE -->
    <!-- ================================================================= -->
    <section id="sec-coding-task" class="card">
      <div class="card-header">
        <h2 class="card-title">⏱️ 13. Timed Practical Coding Challenge</h2>
        <span class="badge badge-danger">${codingTask.time_limit_minutes || 30} Minutes Limit</span>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-3);">
        <div>
          <h3 style="margin: 0 0 4px;">${codingTask.title || 'Daily Practical Task'}</h3>
          <span class="badge ${codingTask.difficulty === 'Easy' ? 'badge-success' : 'badge-warning'}">${codingTask.difficulty || 'Medium'}</span>
        </div>
      </div>

      <div class="callout callout-understand" style="margin-bottom: var(--space-4);">
        <div class="callout-header">Task Description & Requirements</div>
        <p style="margin: 0; font-size: var(--font-size-sm); line-height: 1.6;">${formatMultiline(codingTask.problem_statement)}</p>
      </div>

      <!-- Starter Code -->
      <h4 style="margin: var(--space-3) 0 var(--space-2); color: var(--color-primary);">Starter Code Stub</h4>
      <div class="code-container" style="margin-bottom: var(--space-4);">
        <div class="code-header">
          <span>Java 17+ Starter Stub</span>
          <button class="copy-code-btn" data-code="${encodeURIComponent(codingTask.java_starter_code || codingTask.starter_code || '')}">Copy Starter Code</button>
        </div>
        <pre class="code-pre"><code>${codingTask.java_starter_code || codingTask.starter_code || ''}</code></pre>
      </div>

      <!-- Sample Test Cases -->
      <h4 style="margin: var(--space-3) 0 var(--space-2); color: var(--color-primary);">Sample Test Cases</h4>
      <div style="display: flex; flex-direction: column; gap: var(--space-2); margin-bottom: var(--space-4);">
        ${(codingTask.test_cases || []).map((tc, idx) => `
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-xs);">
            <div><strong>Test ${idx + 1} Input:</strong> <code>${tc.input}</code></div>
            <div><strong>Expected Output:</strong> <code>${tc.expected_output}</code></div>
            ${tc.explanation ? `<div style="color: var(--text-muted); margin-top: 2px;">${tc.explanation}</div>` : ''}
          </div>
        `).join('')}
      </div>

      <!-- Solution Toggle -->
      <button class="btn btn-secondary btn-sm toggle-ans-btn" style="margin-bottom: var(--space-2);">Reveal Full Production Solution</button>
      <div class="quiz-answer-block">
        <div class="code-container">
          <div class="code-header">
            <span>Official Java 17+ Solution</span>
            <button class="copy-code-btn" data-code="${encodeURIComponent(codingTask.java_solution_code || codingTask.solution_code || '')}">Copy Solution</button>
          </div>
          <pre class="code-pre"><code>${codingTask.java_solution_code || codingTask.solution_code || ''}</code></pre>
        </div>
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- 14. 100-POINT SCORE MODEL & SIGN-OFF CHECKLIST -->
    <!-- ================================================================= -->
    <section id="sec-sign-off" class="card" style="border-top: 4px solid var(--color-success); background: var(--bg-surface);">
      <div class="card-header">
        <h2 class="card-title">🏆 14. Daily 100-Point Model & Completion Sign-Off</h2>
        <span class="badge ${isDone ? 'badge-success' : 'badge-warning'}">${isDone ? 'COMPLETED' : 'IN PROGRESS'}</span>
      </div>

      <div style="margin-bottom: var(--space-4);">
        <h4 style="margin: 0 0 var(--space-2); color: var(--text-primary);">Daily Completion Checklist (Tick when fully studied):</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: var(--space-3);">
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-sem" class="score-contributor-chk" data-points="15" ${checklist.sem ? 'checked' : ''}> 1. Academic Theory & PYQs (15 pts)
          </label>
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-apt" class="score-contributor-chk" data-points="15" ${checklist.apt ? 'checked' : ''}> 2. Aptitude Solved & MCQs (15 pts)
          </label>
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-code" class="score-contributor-chk" data-points="20" ${checklist.code ? 'checked' : ''}> 3. DSA Pattern & Coding (20 pts)
          </label>
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-cs" class="score-contributor-chk" data-points="15" ${checklist.cs ? 'checked' : ''}> 4. Core CS Foundations (15 pts)
          </label>
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-proj" class="score-contributor-chk" data-points="10" ${checklist.proj ? 'checked' : ''}> 5. Project Architecture (10 pts)
          </label>
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-interview" class="score-contributor-chk" data-points="10" ${checklist.interview ? 'checked' : ''}> 6. Placement & STAR (10 pts)
          </label>
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-test" class="score-contributor-chk" data-points="10" ${checklist.test ? 'checked' : ''}> 7. Mixed Daily Test (10 pts)
          </label>
          <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-sm);">
            <input type="checkbox" id="page-chk-task" class="score-contributor-chk" data-points="5" ${checklist.task ? 'checked' : ''}> 8. Practical Coding Task (5 pts)
          </label>
        </div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: var(--space-3); border-top: 1px solid var(--border-color); padding-top: var(--space-4);">
        <div>
          <span style="font-size: var(--font-size-sm); color: var(--text-secondary);">Score Required to Pass: <strong>80 / 100</strong></span>
        </div>
        <button id="final-day-complete-btn" class="btn ${isDone ? 'btn-success' : 'btn-primary'}" style="min-width: 240px;">
          <span>${isDone ? '✓ DAY MASTERED & COMPLETED' : 'COMPLETE DAY ' + dayNum}</span>
        </button>
      </div>
    </section>
  `;

  // Attach full interactivity
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

  // Interactive MCQ selection with instant evaluation
  document.querySelectorAll('.mcq-interactive-card').forEach(card => {
    const correctLetter = card.dataset.correct;
    const optButtons = card.querySelectorAll('.mcq-opt-btn');
    const feedback = card.querySelector('.mcq-feedback-block');

    optButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const selectedLetter = btn.dataset.letter;

        // Disable all buttons in this question
        optButtons.forEach(b => {
          b.disabled = true;
          b.style.pointerEvents = 'none';
          if (b.dataset.letter === correctLetter) {
            b.style.backgroundColor = 'var(--color-success)';
            b.style.color = '#fff';
            b.style.borderColor = 'var(--color-success)';
          }
        });

        if (feedback) {
          feedback.style.display = 'block';
          if (selectedLetter === correctLetter) {
            btn.style.backgroundColor = 'var(--color-success)';
            btn.style.color = '#fff';
            feedback.style.backgroundColor = 'rgba(16, 185, 129, 0.1)';
            feedback.style.color = 'var(--color-success)';
            feedback.innerHTML = `<strong>✓ Correct!</strong> Answer is option ${correctLetter}.`;
          } else {
            btn.style.backgroundColor = 'var(--color-danger)';
            btn.style.color = '#fff';
            feedback.style.backgroundColor = 'rgba(239, 68, 68, 0.1)';
            feedback.style.color = 'var(--color-danger)';
            feedback.innerHTML = `<strong>✗ Incorrect.</strong> Selected ${selectedLetter}, correct answer is <strong>${correctLetter}</strong>.`;
          }
        }

        recalculateLiveScore();
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

  // Score Calculator
  function recalculateLiveScore() {
    let score = 0;
    document.querySelectorAll('.score-contributor-chk').forEach(chk => {
      if (chk.checked) {
        score += parseInt(chk.dataset.points, 10) || 0;
      }
    });

    const scoreDisplay = document.getElementById('live-day-score');
    if (scoreDisplay) {
      scoreDisplay.textContent = score;
      if (score >= 80) {
        scoreDisplay.style.color = 'var(--color-success)';
      } else {
        scoreDisplay.style.color = 'var(--color-primary)';
      }
    }
  }

  // Checkbox bindings & persistence
  const syncChecklist = () => {
    const updated = {
      sem: document.getElementById('page-chk-sem')?.checked || false,
      apt: document.getElementById('page-chk-apt')?.checked || false,
      code: document.getElementById('page-chk-code')?.checked || false,
      cs: document.getElementById('page-chk-cs')?.checked || false,
      proj: document.getElementById('page-chk-proj')?.checked || false,
      interview: document.getElementById('page-chk-interview')?.checked || false,
      test: document.getElementById('page-chk-test')?.checked || false,
      task: document.getElementById('page-chk-task')?.checked || false
    };
    Storage.saveDayChecklist(dayNum, updated);
    recalculateLiveScore();
  };

  document.querySelectorAll('.score-contributor-chk').forEach(chk => {
    chk.addEventListener('change', syncChecklist);
  });

  // Initial score calculation
  recalculateLiveScore();

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
