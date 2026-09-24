/**
 * Professional ATS-Optimized 1-Page Resume Hub View
 * Isolated print container: .resume-print-container
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
    <div class="resume-screen-wrapper">
      <div class="resume-toolbar no-print">
        <div>
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">ATS-OPTIMIZED 1-PAGE RESUME ENGINE</div>
          <h1 style="margin-bottom: var(--space-1); font-size: var(--font-size-2xl);">Professional 1-Page Resume Package</h1>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin: 0; max-width: 650px;">
            Single-column, ATS-parseable, verified project portfolio tailored for campus placements and off-campus roles. Strictly calibrated to print on <strong>exactly 1 A4 page</strong>.
          </p>
        </div>

        <div class="resume-actions-group">
          <button id="resume-print-btn" class="btn btn-primary" style="box-shadow: var(--shadow-glow);">
            🖨️ Print / Save as PDF (A4)
          </button>
        </div>
      </div>

      <!-- Profile Switcher Tabs -->
      <div class="no-print" style="margin-bottom: var(--space-5);">
        <div class="resume-tabs-group">
          <button class="btn btn-primary resume-tab-btn" data-profile="python_backend">
            🐍 Python Backend Developer
          </button>
          <button class="btn btn-secondary resume-tab-btn" data-profile="software_engineer">
            💻 Software Engineer (SDE)
          </button>
          <button class="btn btn-secondary resume-tab-btn" data-profile="data_ai">
            🤖 Data & AI Systems Engineer
          </button>
        </div>
      </div>

      <!-- Resume Sheet Workspace (Isolated Print Container) -->
      <div id="resume-sheet-container">
        <!-- Rendered dynamically -->
      </div>
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
      <div class="resume-print-container">
        
        <!-- Header / Contact -->
        <div class="resume-header-block">
          <h1 class="resume-name">${r.contact.name}</h1>
          ${r.contact.tagline ? `<div class="resume-tagline">${r.contact.tagline}</div>` : ''}
          <div class="resume-contact-line">
            <span>${r.contact.location}</span>
            <span class="contact-sep">|</span>
            <span><a href="mailto:${r.contact.email}">${r.contact.email}</a></span>
            <span class="contact-sep">|</span>
            <span>${r.contact.phone}</span>
            ${r.contact.website ? `<span class="contact-sep">|</span><span><a href="${r.contact.website}" target="_blank">${r.contact.website.replace('https://', '')}</a></span>` : ''}
            <span class="contact-sep">|</span>
            <span><a href="${r.contact.github}" target="_blank">${r.contact.github.replace('https://', '')}</a></span>
            <span class="contact-sep">|</span>
            <span><a href="${r.contact.linkedin}" target="_blank">${r.contact.linkedin.replace('https://', '')}</a></span>
          </div>
        </div>

        <!-- Professional Summary -->
        <div class="resume-section">
          <div class="resume-section-heading">PROFESSIONAL SUMMARY</div>
          <p class="resume-summary-text">${r.summary}</p>
        </div>

        <!-- Technical Skills -->
        <div class="resume-section">
          <div class="resume-section-heading">TECHNICAL SKILLS</div>
          <div class="resume-skills-grid">
            ${Object.entries(r.skills).map(([cat, sk]) => `
              <div class="resume-skills-row">
                <span class="resume-skills-label">${cat}:</span>
                <span class="resume-skills-val">${sk}</span>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Work Experience -->
        ${r.work_experience && r.work_experience.length > 0 ? `
        <div class="resume-section">
          <div class="resume-section-heading">WORK EXPERIENCE</div>
          ${r.work_experience.map(exp => `
            <div class="resume-item">
              <div class="resume-item-header">
                <div>
                  <span class="resume-item-title">${exp.role}</span>
                  <span class="resume-item-subtitle">· ${exp.company}</span>
                </div>
                <span class="resume-item-meta">${exp.duration} | ${exp.location}</span>
              </div>
              <ul class="resume-bullet-list">
                ${exp.bullets.map(b => `<li>${b}</li>`).join('')}
              </ul>
            </div>
          `).join('')}
        </div>
        ` : ''}

        <!-- Key Engineering Projects -->
        <div class="resume-section">
          <div class="resume-section-heading">KEY ENGINEERING PROJECTS</div>
          ${r.experience_and_projects.map(proj => `
            <div class="resume-item">
              <div class="resume-item-header">
                <div>
                  <span class="resume-item-title">${proj.name}</span>
                </div>
                <span class="resume-item-meta">${proj.role}</span>
              </div>
              <ul class="resume-bullet-list">
                ${proj.bullets.map(b => `<li>${b}</li>`).join('')}
              </ul>
            </div>
          `).join('')}
        </div>

        <!-- Education -->
        <div class="resume-section">
          <div class="resume-section-heading">EDUCATION</div>
          <div class="resume-edu-row">
            <div>
              <strong style="color: inherit;">${r.education.degree}</strong> — ${r.education.institution}
            </div>
            <div style="font-weight: 600;">
              ${r.education.duration} · ${r.education.academic_standing}
            </div>
          </div>
        </div>

        <!-- Certifications & Honors -->
        ${r.certifications && r.certifications.length > 0 ? `
        <div class="resume-section">
          <div class="resume-section-heading">CERTIFICATIONS & HONORS</div>
          <div class="resume-certs-grid">
            ${r.certifications.map(c => `
              <div class="resume-cert-item">
                <span class="cert-bullet">•</span> <span>${c}</span>
              </div>
            `).join('')}
          </div>
        </div>
        ` : ''}

      </div>
    `;
  }

  // Initial render
  renderResume('python_backend');

  // Tab switcher
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
