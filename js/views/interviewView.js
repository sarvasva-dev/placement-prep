/**
 * Mock Interview Simulator & Self-Evaluation View
 */

import { Storage } from '../storage.js';
import { StudyTimer } from '../timer.js';

export function renderInterviewView(container, daysIndex) {
  const interviewRounds = [
    {
      id: 'round1',
      title: 'Round 1: Core Technical Fundamentals',
      subtitle: 'OS, DBMS, Networks & Python Internals (Elimination Round)',
      duration: 3, // minutes per question
      questions: [
        {
          q: 'Tell me about yourself and your technical focus in under 90 seconds.',
          framework: 'Present (BCA 3rd year, Python backend & API systems) → Past (Key projects: BulkBeat TV high-concurrency alert engine, TerraStract OCR pipeline) → Future (Excited to solve distributed system and reliability challenges at your company).',
          key_points: 'Keep under 90 seconds. Focus on what you have built and deployed, not generic childhood interests.'
        },
        {
          q: 'What is the Global Interpreter Lock (GIL) in Python, and how do you achieve true CPU parallelism?',
          framework: 'Definition (Mutex protecting reference counts in CPython) → Impact (Single thread executes Python bytecode at once) → Solution (Use multiprocessing / ProcessPoolExecutor or C-extensions for CPU bound; use asyncio/threading for I/O bound).',
          key_points: 'Clarify that GIL affects only CPython CPU workloads, not I/O-bound network calls.'
        },
        {
          q: 'Explain the difference between clustered and non-clustered indexes in SQL.',
          framework: 'Physical Storage (Clustered physically sorts data rows on disk, only 1 per table; Non-clustered creates a separate B+ tree storing pointers to data rows) → Performance tradeoffs.',
          key_points: 'Mention B+ Tree depth and secondary index pointer overhead.'
        },
        {
          q: 'Walk me through the TCP 3-way handshake and why 2 packets are insufficient.',
          framework: 'SYN (seq=x) → SYN-ACK (seq=y, ack=x+1) → ACK (ack=y+1). Explain why 2 packets fail: server cannot verify client received the server sequence number (half-open connection risk).',
          key_points: 'Mention TIME_WAIT state (2*MSL) during connection termination.'
        }
      ]
    },
    {
      id: 'round2',
      title: 'Round 2: System Architecture & Project Defense',
      subtitle: 'Deep-Dive into BulkBeat TV, TerraStract & CSMS Codebases',
      duration: 5,
      questions: [
        {
          q: 'In BulkBeat TV, how did you handle concurrent database writes without encountering "database is locked" errors?',
          framework: 'Problem Statement (Default SQLite rollback journal locks file) → Architecture Fix 1 (PRAGMA journal_mode=WAL) → Architecture Fix 2 (Single-writer coroutine reading from asyncio.Queue).',
          key_points: 'Demonstrate deep knowledge of write contention and non-blocking asynchronous architectures.'
        },
        {
          q: 'In TerraStract, why combine PyMuPDF with Tesseract OCR rather than running OCR across all pages?',
          framework: 'Performance & Resource Tradeoff (PyMuPDF extracts digital text vector streams in &lt;10ms; Tesseract requires 800ms+ per page and high CPU) → Hybrid Fallback Decision Matrix.',
          key_points: 'Mention fallback triggers: empty text layer, font glyph corruption, or image-only scanned pages.'
        },
        {
          q: 'How did you secure endpoints and manage database schema versions in CSMS?',
          framework: 'Authentication (OAuth2 Password Bearer + JWT with HMAC-SHA256) → Authorization (RBAC dependency guards in FastAPI) → Schema Migrations (Alembic autogen and revision history).',
          key_points: 'Explain why schema migrations should never be done by manually executing DDL on live production tables.'
        }
      ]
    },
    {
      id: 'round3',
      title: 'Round 3: Algorithmic Problem Solving & Live Coding',
      subtitle: 'Thinking Out Loud, Tradeoffs & Edge Cases',
      duration: 10,
      questions: [
        {
          q: 'How do you approach a coding problem in an interview before typing a single line of code?',
          framework: 'UMPIRE Framework: Understand constraints & inputs → Match pattern (Two Pointers, DP, Graph) → Plan algorithm & calculate complexity → Implement cleanly → Review edge cases (empty array, single element, negative numbers).',
          key_points: 'Always state the brute force first, then optimize. Never jump straight to code without communicating.'
        },
        {
          q: 'Explain the difference between Dynamic Programming with Memoization vs Tabulation.',
          framework: 'Top-Down (Recursion + Cache/Memo dictionary) vs Bottom-Up (Iterative Table filling). Tradeoffs: Top-Down is intuitive but risks recursion stack overflow; Bottom-Up has O(1) call stack overhead and allows rolling space optimizations.',
          key_points: 'Give Fibonacci or Climbing Stairs space optimization as an instant example.'
        }
      ]
    },
    {
      id: 'round4',
      title: 'Round 4: HR, Behavioral & Situational Readiness',
      subtitle: 'Cultural Fit, Conflict Resolution & Career Vision',
      duration: 3,
      questions: [
        {
          q: 'Tell me about a time when a bug occurred in production or under deadline pressure. How did you handle it?',
          framework: 'STAR Method: Situation (Sudden alert crash or spike) → Task (Diagnose root cause without panic) → Action (Inspect logs, apply hotfix, write test) → Result (Uptime restored, preventive safeguard added).',
          key_points: 'Take accountability. Focus on debugging telemetry and post-mortem safeguards.'
        },
        {
          q: 'Why should we hire you over candidates from traditional engineering (B.Tech) colleges?',
          framework: 'Demonstrate bias for action: "While academic pedigrees focus heavily on theoretical exams, I have spent the last two years actively building, deploying, and maintaining live backend services with real users, handling production concurrency, writing clean APIs, and achieving academic excellence (Target SGPA 9.0+)."',
          key_points: 'Confidence without arrogance. Emphasize self-driven initiative and verified production projects.'
        }
      ]
    }
  ];

  let activeRoundIdx = 0;

  container.innerHTML = `
    <div class="interview-header" style="margin-bottom: var(--space-6);">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-4);">
        <div>
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">PLACEMENT MOCK SIMULATOR</div>
          <h1 style="margin-bottom: var(--space-1);">Interview Simulator & Defense Rubric</h1>
          <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
            Simulate realistic technical and behavioral interview rounds. Practice verbal clarity under time pressure and self-evaluate across 4 competency dimensions.
          </p>
        </div>

        <!-- Pitch Stopwatch -->
        <div class="card" style="margin-bottom: 0; padding: var(--space-3) var(--space-4); display: flex; align-items: center; gap: var(--space-3); border-color: var(--color-primary);">
          <div>
            <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Speaking Timer</div>
            <div id="interview-timer-display" style="font-family: var(--font-family-mono); font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-primary);">
              03:00
            </div>
          </div>
          <div style="display: flex; flex-direction: column; gap: 4px;">
            <button id="interview-timer-start" class="btn btn-primary btn-sm" style="padding: 2px 10px;">Start</button>
            <button id="interview-timer-reset" class="btn btn-secondary btn-sm" style="padding: 2px 10px;">Reset</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Round Selector Buttons -->
    <div style="display: flex; gap: var(--space-2); margin-bottom: var(--space-5); overflow-x: auto; padding-bottom: var(--space-2);">
      ${interviewRounds.map((r, idx) => `
        <button class="btn ${idx === 0 ? 'btn-primary' : 'btn-secondary'} interview-round-btn" data-idx="${idx}" style="white-space: nowrap;">
          ${r.title}
        </button>
      `).join('')}
    </div>

    <!-- Active Round Container -->
    <div id="interview-round-workspace">
      <!-- Rendered dynamically -->
    </div>
  `;

  // Initialize timer
  const timerDisplay = container.querySelector('#interview-timer-display');
  const timerStartBtn = container.querySelector('#interview-timer-start');
  const timerResetBtn = container.querySelector('#interview-timer-reset');
  let intTimer = new StudyTimer(timerDisplay, null, () => {
    alert('⏰ Interview response time completed! Conclude your answer.');
  });
  intTimer.setDuration(3);

  timerStartBtn.addEventListener('click', () => {
    if (intTimer.isRunning) {
      intTimer.pause();
      timerStartBtn.textContent = 'Start';
      timerStartBtn.classList.remove('btn-warning');
      timerStartBtn.classList.add('btn-primary');
    } else {
      intTimer.start();
      timerStartBtn.textContent = 'Pause';
      timerStartBtn.classList.remove('btn-primary');
      timerStartBtn.classList.add('btn-warning');
    }
  });

  timerResetBtn.addEventListener('click', () => {
    intTimer.stop();
    timerStartBtn.textContent = 'Start';
    timerStartBtn.classList.remove('btn-warning');
    timerStartBtn.classList.add('btn-primary');
  });

  const workspace = container.querySelector('#interview-round-workspace');
  const roundBtns = container.querySelectorAll('.interview-round-btn');

  function renderRound(idx) {
    const round = interviewRounds[idx];
    if (!round) return;

    intTimer.setDuration(round.duration);

    workspace.innerHTML = `
      <div class="card" style="border-left: 4px solid var(--color-primary); margin-bottom: var(--space-5);">
        <div class="badge badge-primary" style="margin-bottom: var(--space-1);">MOCK ROUND ${idx + 1}</div>
        <h2 style="margin: 0 0 4px 0;">${round.title}</h2>
        <div style="font-size: var(--font-size-sm); color: var(--text-secondary);">${round.subtitle} • Target time: ${round.duration} min per question.</div>
      </div>

      <div style="display: flex; flex-direction: column; gap: var(--space-5);">
        ${round.questions.map((q, qidx) => {
          const scoreKey = `interview_score_${round.id}_${qidx}`;
          const savedScore = localStorage.getItem(scoreKey) || '0';

          return `
            <div class="card" style="margin-bottom: 0;">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-3);">
                <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-primary); text-transform: uppercase;">
                  Question ${qidx + 1} of ${round.questions.length}
                </div>
                <div style="display: flex; align-items: center; gap: var(--space-2);">
                  <span style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700;">Self-Rating (0-5):</span>
                  <select class="form-control interview-score-sel" data-key="${scoreKey}" style="width: 70px; padding: 2px 6px; font-size: var(--font-size-xs);">
                    ${[0, 1, 2, 3, 4, 5].map(v => `<option value="${v}" ${parseInt(savedScore, 10) === v ? 'selected' : ''}>${v} / 5</option>`).join('')}
                  </select>
                </div>
              </div>

              <h3 style="font-size: var(--font-size-lg); color: var(--text-primary); margin-bottom: var(--space-3); line-height: 1.4;">
                ${q.q}
              </h3>

              <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); margin-bottom: var(--space-3); border-left: 3px solid var(--color-info);">
                <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-info); text-transform: uppercase; margin-bottom: 2px;">
                  🎙️ Recommended Answering Framework:
                </div>
                <div style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6;">
                  ${q.framework}
                </div>
              </div>

              <div style="background: var(--color-warning-subtle); border-left: 3px solid var(--color-warning); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-sm); color: var(--text-primary);">
                <strong>Key Evaluator Takeaway:</strong> ${q.key_points}
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;

    // Attach score saver handlers
    workspace.querySelectorAll('.interview-score-sel').forEach(sel => {
      sel.addEventListener('change', (e) => {
        const key = sel.dataset.key;
        localStorage.setItem(key, e.target.value);
      });
    });
  }

  // Initial render
  renderRound(0);

  // Round button click handlers
  roundBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      roundBtns.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');
      const idx = parseInt(btn.dataset.idx, 10);
      renderRound(idx);
    });
  });
}
