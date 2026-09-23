/**
 * Professional ATS-Optimized 1-Page Resume Hub View
 */

import { Storage } from '../storage.js';

export function renderResumeView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING RESUMES...</div>
      <h2>Retrieving Sarthak's ATS Resume Package</h2>
    </div>
  `;

  fetch('content/resumes/resumes_all.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load resume data');
      return res.json();
    })
    .then(resumesData => {
      buildResumePage(container, resumesData, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Resume Package</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildResumePage(container, resumesData, daysIndex) {
  let activeProfile = 'python_backend';

  container.innerHTML = `
    <div class="resume-header no-print" style="margin-bottom: var(--space-6);">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-4);">
        <div>
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">ATS-OPTIMIZED RESUME ENGINE</div>
          <h1 style="margin-bottom: var(--space-1);">Professional 1-Page Resume Package</h1>
          <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
            Targeted for campus placements and off-campus backend engineering roles. Formatted with high ATS parseability, XYZ action verbs, and verified metrics.
          </p>
        </div>

        <div style="display: flex; gap: var(--space-2); align-items: center;">
          <button id="resume-print-btn" class="btn btn-primary" style="box-shadow: var(--shadow-glow);">
            🖨️ Print / Save as PDF
          </button>
        </div>
      </div>
    </div>

    <!-- Profile Switcher Tabs -->
    <div class="no-print" style="display: flex; gap: var(--space-2); margin-bottom: var(--space-5);">
      <button class="btn btn-primary resume-tab-btn" data-profile="python_backend">
        🐍 Python Backend Developer Profile
      </button>
      <button class="btn btn-secondary resume-tab-btn" data-profile="software_engineer">
        💻 General Software Engineer Profile
      </button>
    </div>

    <!-- Resume Sheet Workspace -->
    <div id="resume-sheet-container">
      <!-- Rendered dynamically -->
    </div>
  `;

  const containerEl = container.querySelector('#resume-sheet-container');
  const printBtn = container.querySelector('#resume-print-btn');
  const tabBtns = container.querySelectorAll('.resume-tab-btn');

  printBtn.addEventListener('click', () => {
    window.print();
  });

  function renderResume(profileKey) {
    const r = resumesData[profileKey];
    if (!r) return;

    containerEl.innerHTML = `
      <div class="card resume-paper" style="max-width: 850px; margin: 0 auto; background: var(--bg-surface); padding: var(--space-6); border: 1px solid var(--border-color); box-shadow: var(--shadow-lg);">
        
        <!-- Header / Contact -->
        <div style="text-align: center; border-bottom: 2px solid var(--border-color); padding-bottom: var(--space-4); margin-bottom: var(--space-4);">
          <h1 style="font-size: 1.8rem; margin: 0 0 4px 0; letter-spacing: 0.5px; color: var(--text-primary); text-transform: uppercase;">
            ${r.contact.name}
          </h1>
          ${r.contact.tagline ? `<div style="font-size: var(--font-size-xs); font-weight: 700; color: var(--color-primary); margin-bottom: 6px; letter-spacing: 0.5px;">${r.contact.tagline}</div>` : ''}
          <div style="font-size: var(--font-size-sm); color: var(--text-secondary); display: flex; justify-content: center; flex-wrap: wrap; gap: var(--space-3);">
            <span>📍 ${r.contact.location}</span>
            <span>✉️ ${r.contact.email}</span>
            <span>📞 ${r.contact.phone}</span>
            ${r.contact.website ? `<span>🌐 <a href="${r.contact.website}" target="_blank" style="color: var(--color-primary);">${r.contact.website.replace('https://', '')}</a></span>` : ''}
            <span>🔗 <a href="${r.contact.github}" target="_blank" style="color: var(--color-primary);">${r.contact.github.replace('https://', '')}</a></span>
            <span>🔗 <a href="${r.contact.linkedin}" target="_blank" style="color: var(--color-primary);">${r.contact.linkedin.replace('https://', '')}</a></span>
          </div>
        </div>

        <!-- Summary -->
        <div style="margin-bottom: var(--space-4);">
          <div style="font-size: var(--font-size-xs); font-weight: 800; color: var(--color-primary); text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid var(--border-color); padding-bottom: 2px; margin-bottom: 6px;">
            PROFESSIONAL SUMMARY
          </div>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6; margin: 0;">
            ${r.summary}
          </p>
        </div>

        <!-- Technical Skills -->
        <div style="margin-bottom: var(--space-4);">
          <div style="font-size: var(--font-size-xs); font-weight: 800; color: var(--color-primary); text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid var(--border-color); padding-bottom: 2px; margin-bottom: 6px;">
            TECHNICAL SKILLS
          </div>
          <div style="display: flex; flex-direction: column; gap: 4px; font-size: var(--font-size-sm); color: var(--text-secondary);">
            ${Object.entries(r.skills).map(([cat, sk]) => `
              <div><strong style="color: var(--text-primary);">${cat}:</strong> ${sk}</div>
            `).join('')}
          </div>
        </div>

        <!-- Work Experience (if available) -->
        ${r.work_experience ? `
        <div style="margin-bottom: var(--space-4);">
          <div style="font-size: var(--font-size-xs); font-weight: 800; color: var(--color-primary); text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid var(--border-color); padding-bottom: 2px; margin-bottom: 6px;">
            WORK EXPERIENCE
          </div>
          <div style="display: flex; flex-direction: column; gap: var(--space-3);">
            ${r.work_experience.map(exp => `
              <div>
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 4px;">
                  <div>
                    <strong style="font-size: var(--font-size-base); color: var(--text-primary);">${exp.role}</strong>
                    <span style="font-size: var(--font-size-sm); color: var(--color-primary); margin-left: 6px;">@ ${exp.company}</span>
                  </div>
                  <span style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted);">${exp.duration} (${exp.location})</span>
                </div>
                <ul style="margin: 4px 0 0 0; padding-left: var(--space-4); font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.5;">
                  ${exp.bullets.map(b => `<li style="margin-bottom: 4px;">${b}</li>`).join('')}
                </ul>
              </div>
            `).join('')}
          </div>
        </div>
        ` : ''}

        <!-- Key Projects -->
        <div style="margin-bottom: var(--space-4);">
          <div style="font-size: var(--font-size-xs); font-weight: 800; color: var(--color-primary); text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid var(--border-color); padding-bottom: 2px; margin-bottom: 6px;">
            KEY ENGINEERING PROJECTS
          </div>
          <div style="display: flex; flex-direction: column; gap: var(--space-3);">
            ${r.experience_and_projects.map(proj => `
              <div>
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 4px;">
                  <strong style="font-size: var(--font-size-base); color: var(--text-primary);">${proj.name}</strong>
                  <span style="font-size: var(--font-size-xs); font-weight: 700; color: var(--text-muted);">${proj.role}</span>
                </div>
                <ul style="margin: 4px 0 0 0; padding-left: var(--space-4); font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.5;">
                  ${proj.bullets.map(b => `<li style="margin-bottom: 4px;">${b}</li>`).join('')}
                </ul>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Education -->
        <div style="margin-bottom: var(--space-4);">
          <div style="font-size: var(--font-size-xs); font-weight: 800; color: var(--color-primary); text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid var(--border-color); padding-bottom: 2px; margin-bottom: 6px;">
            EDUCATION
          </div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 4px;">
            <div>
              <strong style="color: var(--text-primary); font-size: var(--font-size-sm);">${r.education.degree}</strong><br>
              <span style="font-size: var(--font-size-xs); color: var(--text-muted);">${r.education.institution}</span>
            </div>
            <div style="text-align: right;">
              <span style="font-size: var(--font-size-xs); color: var(--text-muted);">${r.education.duration}</span><br>
              <span class="badge badge-primary" style="font-size: 0.7rem;">${r.education.academic_standing}</span>
            </div>
          </div>
        </div>

        <!-- Certifications & Honors -->
        ${r.certifications ? `
        <div>
          <div style="font-size: var(--font-size-xs); font-weight: 800; color: var(--color-primary); text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid var(--border-color); padding-bottom: 2px; margin-bottom: 6px;">
            CERTIFICATIONS & HONORS
          </div>
          <div style="display: flex; flex-wrap: wrap; gap: var(--space-2); margin-top: 4px;">
            ${r.certifications.map(c => `
              <span class="badge badge-secondary" style="font-size: var(--font-size-xs);">${c}</span>
            `).join('')}
          </div>
        </div>
        ` : ''}

      </div>
    `;
  }

  // Initial render
  renderResume('python_backend');

  // Tab button listeners
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');
      activeProfile = btn.dataset.profile;
      renderResume(activeProfile);
    });
  });
}
