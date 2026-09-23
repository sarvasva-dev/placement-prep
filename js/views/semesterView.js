/**
 * Semester 5 Master Hub View (SGPA >= 9.0 Strategy & Syllabus)
 */

import { Storage } from '../storage.js';

export function renderSemesterView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING SYLLABUS...</div>
      <h2>Retrieving Semester 5 Curricula & Blueprints</h2>
    </div>
  `;

  fetch('content/semester/semester_all.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load semester data');
      return res.json();
    })
    .then(data => {
      buildSemesterPage(container, data, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Semester Data</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildSemesterPage(container, semData, daysIndex) {
  // Mapping subject codes to Days
  const subjectDayMap = {
    'bca5001': [1, 2, 7, 11, 16, 20, 24, 28],
    'bca5002': [3, 6, 8, 12, 14, 17, 21, 25],
    'bca5003': [4, 9, 13, 18, 22, 26],
    'bca5004': [5, 10, 15, 19, 23, 27]
  };

  const subjects = [
    { key: 'bca5001', name: 'BCA-5001 Knowledge Management', color: 'var(--color-primary)' },
    { key: 'bca5002', name: 'BCA-5002 Java & Web Design', color: 'var(--color-success)' },
    { key: 'bca5003', name: 'BCA-5003 Computer Networks', color: 'var(--color-info)' },
    { key: 'bca5004', name: 'BCA-5004 Numerical Methods', color: 'var(--color-warning)' }
  ];

  container.innerHTML = `
    <div class="semester-header" style="margin-bottom: var(--space-6);">
      <div style="display: flex; align-items: flex-start; justify-content: space-between; flex-wrap: wrap; gap: var(--space-4);">
        <div>
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">ACADEMIC EXCELLENCE BLUEPRINT</div>
          <h1 style="margin-bottom: var(--space-1);">Semester 5 Master Curriculum & SGPA ≥ 9.0 Strategy</h1>
          <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
            Dr. Virendra Swarup Institute of Computer Studies (CSJM University, Kanpur). 4 Theory Subjects (16 Credits). Target: <strong>370 / 400 Marks (92.5% • Predicted SGPA: 9.35)</strong>.
          </p>
        </div>
      </div>
    </div>

    <!-- SGPA 9.0 Target Blueprint Table -->
    <div class="card" style="margin-bottom: var(--space-6);">
      <div class="card-header">
        <h2 class="card-title">🎯 Targeted Marks & Credit Matrix for SGPA ≥ 9.0</h2>
        <span class="badge badge-success">Target: 370 / 400 (SGPA 9.3+)</span>
      </div>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Paper Code</th>
              <th>Subject Name</th>
              <th>Credits</th>
              <th>Internal (25)</th>
              <th>External (75)</th>
              <th>Target Total (100)</th>
              <th>SGPA Impact</th>
              <th>Assigned Sprint Days</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>BCA-5001</code></td>
              <td><strong>Knowledge Management</strong></td>
              <td>4</td>
              <td>23</td>
              <td>69</td>
              <td><strong style="color: var(--color-primary);">92</strong></td>
              <td><span class="badge badge-primary">High (SECI & Simon Models)</span></td>
              <td>
                <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                  ${subjectDayMap.bca5001.map(d => `<a href="#day/${d}" class="badge badge-secondary" style="text-decoration:none;">Day ${d}</a>`).join('')}
                </div>
              </td>
            </tr>
            <tr>
              <td><code>BCA-5002</code></td>
              <td><strong>Java & Web Development</strong></td>
              <td>4</td>
              <td>23</td>
              <td>67</td>
              <td><strong style="color: var(--color-success);">90</strong></td>
              <td><span class="badge badge-success">High (JDBC, Servlets, JSP)</span></td>
              <td>
                <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                  ${subjectDayMap.bca5002.map(d => `<a href="#day/${d}" class="badge badge-secondary" style="text-decoration:none;">Day ${d}</a>`).join('')}
                </div>
              </td>
            </tr>
            <tr>
              <td><code>BCA-5003</code></td>
              <td><strong>Computer Networks</strong></td>
              <td>4</td>
              <td>24</td>
              <td>68</td>
              <td><strong style="color: var(--color-info);">92</strong></td>
              <td><span class="badge badge-info">High (OSI, TCP/IP, CRC)</span></td>
              <td>
                <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                  ${subjectDayMap.bca5003.map(d => `<a href="#day/${d}" class="badge badge-secondary" style="text-decoration:none;">Day ${d}</a>`).join('')}
                </div>
              </td>
            </tr>
            <tr>
              <td><code>BCA-5004</code></td>
              <td><strong>Numerical Methods</strong></td>
              <td>4</td>
              <td>24</td>
              <td>72</td>
              <td><strong style="color: var(--color-warning);">96</strong></td>
              <td><span class="badge badge-warning">Critical (100% Math Accuracy)</span></td>
              <td>
                <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                  ${subjectDayMap.bca5004.map(d => `<a href="#day/${d}" class="badge badge-secondary" style="text-decoration:none;">Day ${d}</a>`).join('')}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Subject Selector Tabs -->
    <div style="display: flex; gap: var(--space-2); margin-bottom: var(--space-5); overflow-x: auto; padding-bottom: var(--space-2);">
      ${subjects.map((s, idx) => `
        <button class="btn ${idx === 0 ? 'btn-primary' : 'btn-secondary'} sem-tab-btn" data-target="${s.key}" style="white-space: nowrap;">
          ${s.name}
        </button>
      `).join('')}
    </div>

    <!-- Subject Panels -->
    <div id="sem-panels-container">
      ${subjects.map((s, idx) => renderSubjectPanel(s.key, semData[s.key], subjectDayMap[s.key], idx === 0)).join('')}
    </div>
  `;

  // Attach tab switching events
  const buttons = container.querySelectorAll('.sem-tab-btn');
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');

      const target = btn.dataset.target;
      const panels = container.querySelectorAll('.sem-subject-panel');
      panels.forEach(p => {
        p.style.display = p.id === `panel-${target}` ? 'block' : 'none';
      });
    });
  });
}

function renderSubjectPanel(key, data, assignedDays, isVisible) {
  if (!data) return '';

  return `
    <div id="panel-${key}" class="sem-subject-panel" style="display: ${isVisible ? 'block' : 'none'}; animation: fadeIn 0.2s ease-in-out;">
      <div class="card" style="border-top: 4px solid var(--color-primary); margin-bottom: var(--space-6);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-3); margin-bottom: var(--space-4);">
          <div>
            <div class="badge badge-primary" style="margin-bottom: var(--space-1);">${data.code}</div>
            <h2 style="margin: 0;">${data.name}</h2>
          </div>
          <div style="text-align: right;">
            <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700;">TARGET SCORE</div>
            <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-primary);">${data.target_marks} / 100</div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: var(--space-3); margin-bottom: var(--space-4); background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-md);">
          <div><strong>Credits:</strong> ${data.credits}</div>
          <div><strong>External Theory:</strong> 75 Marks</div>
          <div><strong>Internal Assessment:</strong> 25 Marks</div>
          <div><strong>Total Units:</strong> ${data.units ? data.units.length : 5} Units</div>
        </div>

        <div style="margin-top: var(--space-3);">
          <span style="font-size: var(--font-size-sm); font-weight: 700; color: var(--text-secondary);">Sprint Study Schedule:</span>
          <div style="display: inline-flex; gap: var(--space-2); margin-left: var(--space-2); flex-wrap: wrap;">
            ${assignedDays.map(d => `<a href="#day/${d}" class="btn btn-secondary btn-sm" style="padding: 2px 8px;">Day ${d} Lecture →</a>`).join('')}
          </div>
        </div>
      </div>

      <!-- Units Breakdown -->
      <h3 style="margin-bottom: var(--space-4);">📚 Complete Unit-by-Unit Syllabus Breakdown</h3>
      <div style="display: flex; flex-direction: column; gap: var(--space-4); margin-bottom: var(--space-6);">
        ${(data.units || []).map(u => `
          <div class="card" style="margin-bottom: 0;">
            <div class="card-header">
              <h4 class="card-title">${u.title}</h4>
              <span class="badge badge-secondary">Unit ${u.unit}</span>
            </div>
            
            <div style="margin-bottom: var(--space-3);">
              <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: var(--space-1);">Syllabus Topics:</div>
              <ul style="padding-left: var(--space-4); margin: 0; line-height: 1.6;">
                ${u.topics.map(t => `<li>${t}</li>`).join('')}
              </ul>
            </div>

            ${u.core_pyqs && u.core_pyqs.length ? `
              <div style="border-top: 1px solid var(--border-color); padding-top: var(--space-3); margin-top: var(--space-3); background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
                <div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-primary); text-transform: uppercase; margin-bottom: var(--space-1);">⭐ Recurring 15-Mark University Questions:</div>
                <ul style="padding-left: var(--space-4); margin: 0; font-size: var(--font-size-sm); color: var(--text-secondary);">
                  ${u.core_pyqs.map(q => `<li><strong>${q}</strong></li>`).join('')}
                </ul>
              </div>
            ` : ''}
          </div>
        `).join('')}
      </div>

      ${renderSubjectFormulaBank(key)}
    </div>
  `;
}

function renderSubjectFormulaBank(key) {
  if (key === 'bca5004') {
    return `
      <div class="card" style="border-left: 4px solid var(--color-warning);">
        <div class="card-header">
          <h3 class="card-title">🧮 Numerical Methods Golden Formula Bank & Convergence Rules</h3>
          <span class="badge badge-warning">High-Yield Memory Matrix</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: var(--space-3); font-size: var(--font-size-sm);">
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>1. Newton-Raphson Method:</strong><br>
            <code>x_{n+1} = x_n - [f(x_n) / f'(x_n)]</code><br>
            <span style="color: var(--text-muted);">Convergence: Quadratic (Order 2). Error condition: |f(x) * f''(x)| &lt; |f'(x)|^2.</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>2. Bisection Method:</strong><br>
            <code>x_mid = (a + b) / 2</code>, where <code>f(a) * f(b) &lt; 0</code>.<br>
            <span style="color: var(--text-muted);">Convergence: Linear (Order 1, factor 0.5 per iteration). Guaranteed Bolzano convergence.</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>3. Trapezoidal Rule:</strong><br>
            <code>∫ f(x) dx = (h / 2) * [ (y_0 + y_n) + 2 * (y_1 + y_2 + ... + y_{n-1}) ]</code><br>
            <span style="color: var(--text-muted);">Error: O(h²). Valid for any number of sub-intervals n.</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>4. Simpson's 1/3 Rule:</strong><br>
            <code>∫ f(x) dx = (h / 3) * [ (y_0 + y_n) + 4 * (odd y) + 2 * (even y) ]</code><br>
            <span style="color: var(--text-muted);">Condition: Sub-intervals n MUST BE EVEN! Error: O(h⁴). Degree of precision: 3.</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>5. Simpson's 3/8 Rule:</strong><br>
            <code>∫ f(x) dx = (3h / 8) * [ (y_0 + y_n) + 3 * (y_1+y_2+y_4+...) + 2 * (y_3+y_6+...) ]</code><br>
            <span style="color: var(--text-muted);">Condition: Sub-intervals n MUST BE A MULTIPLE OF 3! Error: O(h⁴).</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>6. Runge-Kutta 4th Order (RK4):</strong><br>
            <code>k1 = h*f(x0, y0)</code><br>
            <code>k2 = h*f(x0 + h/2, y0 + k1/2)</code><br>
            <code>k3 = h*f(x0 + h/2, y0 + k2/2)</code><br>
            <code>k4 = h*f(x0 + h, y0 + k3)</code><br>
            <code>y1 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)</code><br>
            <span style="color: var(--text-muted);">Local Truncation Error: O(h⁵), Global Error: O(h⁴).</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>7. Gauss-Seidel Diagonal Dominance Condition:</strong><br>
            <code>|a_{ii}| &gt; ∑_{j ≠ i} |a_{ij}|</code> for every row i. Mandatory for convergence.
          </div>
        </div>
      </div>
    `;
  }
  if (key === 'bca5003') {
    return `
      <div class="card" style="border-left: 4px solid var(--color-info);">
        <div class="card-header">
          <h3 class="card-title">🌐 Computer Networks Key Protocols & Layer Formulas</h3>
          <span class="badge badge-info">Core Architecture Rules</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: var(--space-3); font-size: var(--font-size-sm);">
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>Cyclic Redundancy Check (CRC):</strong><br>
            Divisor has degree <code>k</code>. Append <code>k</code> zeros to frame. Perform Modulo-2 binary XOR division. The remainder is the CRC FCS transmitted with the payload.
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>Sliding Window Efficiency:</strong><br>
            <code>Utilization U = W / (1 + 2*a)</code>, where <code>a = Propagation Delay (Tp) / Transmission Delay (Tt)</code>.<br>
            Go-Back-N Window: <code>Sender Window = 2^m - 1</code>, Receiver Window = 1.<br>
            Selective Repeat: <code>Sender Window = 2^{m-1}</code>, Receiver Window = <code>2^{m-1}</code>.
          </div>
          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
            <strong>TCP 3-Way Handshake & Teardown:</strong><br>
            Connection: <code>SYN (seq=x) → SYN-ACK (seq=y, ack=x+1) → ACK (ack=y+1)</code>.<br>
            Teardown: <code>FIN → ACK → FIN → ACK (TIME_WAIT: 2 * MSL)</code>.
          </div>
        </div>
      </div>
    `;
  }
  return '';
}
