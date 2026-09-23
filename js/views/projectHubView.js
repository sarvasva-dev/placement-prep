/**
 * Verified Projects & Interview Defense Hub View
 */

import { Storage } from '../storage.js';

export function renderProjectHubView(container, daysIndex, initialProjectKey = null) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING PROJECTS...</div>
      <h2>Retrieving Sarthak's Verified Technical Projects</h2>
    </div>
  `;

  fetch('content/projects/projects_all.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load projects data');
      return res.json();
    })
    .then(projectsData => {
      buildProjectHubPage(container, projectsData, daysIndex, initialProjectKey);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Projects Hub</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildProjectHubPage(container, projectsData, daysIndex, initialProjectKey = null) {
  const projectKeys = Object.keys(projectsData);
  const activeKey = (initialProjectKey && projectsData[initialProjectKey]) ? initialProjectKey : projectKeys[0];

  container.innerHTML = `
    <div class="project-hub-header" style="margin-bottom: var(--space-6);">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">PORTFOLIO & INTERVIEW DEFENSE</div>
      <h1 style="margin-bottom: var(--space-1);">Verified Engineering Projects Hub</h1>
      <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
        All architectural details, codebase structures, and metrics grounded strictly in verified repository artifacts from local <code>D:\\Projects</code>. Zero hallucinated claims.
      </p>
    </div>

    <!-- Project Selector Tabs -->
    <div style="display: flex; gap: var(--space-2); margin-bottom: var(--space-5); overflow-x: auto; padding-bottom: var(--space-2);">
      ${projectKeys.map((key) => {
        const p = projectsData[key];
        const isActive = key === activeKey;
        return `
          <button class="btn ${isActive ? 'btn-primary' : 'btn-secondary'} proj-tab-btn" data-target="${key}" style="white-space: nowrap;">
            ${p.name}
          </button>
        `;
      }).join('')}
    </div>

    <!-- Project Details Panels -->
    <div id="proj-panels-container">
      ${projectKeys.map((key) => renderProjectCard(key, projectsData[key], key === activeKey)).join('')}
    </div>
  `;

  // Attach tab switching events
  const buttons = container.querySelectorAll('.proj-tab-btn');
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('btn-primary');
        b.classList.add('btn-secondary');
      });
      btn.classList.remove('btn-secondary');
      btn.classList.add('btn-primary');

      const target = btn.dataset.target;
      const panels = container.querySelectorAll('.proj-panel');
      panels.forEach(p => {
        p.style.display = p.id === `proj-${target}` ? 'block' : 'none';
      });
    });
  });

  // Attach copy resume bullets
  container.querySelectorAll('.copy-bullet-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const text = btn.dataset.bullet;
      navigator.clipboard.writeText(text).then(() => {
        const orig = btn.textContent;
        btn.textContent = '✓ Copied!';
        btn.classList.add('btn-success');
        setTimeout(() => {
          btn.textContent = orig;
          btn.classList.remove('btn-success');
        }, 2000);
      });
    });
  });
}

function renderProjectCard(key, p, isVisible) {
  return `
    <div id="proj-${key}" class="proj-panel" style="display: ${isVisible ? 'block' : 'none'}; animation: fadeIn 0.2s ease-in-out;">
      <!-- Main Overview Card -->
      <div class="card" style="border-top: 4px solid var(--color-primary); margin-bottom: var(--space-5);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-3); margin-bottom: var(--space-3);">
          <div>
            <div class="badge badge-primary" style="margin-bottom: var(--space-1);">${p.category}</div>
            <h2 style="margin: 0;">${p.name}</h2>
            <div style="font-size: var(--font-size-xs); color: var(--text-muted); margin-top: 4px; font-family: var(--font-family-mono);">
              Workstation Repo: <code>${p.repo_path}</code>
            </div>
          </div>
        </div>

        <!-- Metrics Grid -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-3); margin-top: var(--space-4); margin-bottom: var(--space-4);">
          ${p.metrics.users ? `
            <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-primary);">
              <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700;">USER TRACTION</div>
              <div style="font-size: var(--font-size-base); font-weight: 800; color: var(--text-primary);">${p.metrics.users}</div>
            </div>
          ` : ''}
          ${p.metrics.revenue ? `
            <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-success);">
              <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700;">REVENUE GENERATED</div>
              <div style="font-size: var(--font-size-base); font-weight: 800; color: var(--color-success);">${p.metrics.revenue}</div>
            </div>
          ` : ''}
          ${p.metrics.verified_technical ? `
            <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); border-left: 3px solid var(--color-info); grid-column: 1 / -1;">
              <div style="font-size: var(--font-size-xs); color: var(--color-info); font-weight: 700;">VERIFIED CODEBASE METRICS</div>
              <div style="font-size: var(--font-size-sm); color: var(--text-primary); margin-top: 2px;">${p.metrics.verified_technical}</div>
            </div>
          ` : ''}
        </div>

        <!-- Tech Stack 3-Tier Categorization -->
        <div style="margin-top: var(--space-4);">
          <h4 style="font-size: var(--font-size-sm); text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--space-2);">Technical Stack Transparency:</h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: var(--space-3);">
            <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
              <strong style="color: var(--color-success); font-size: var(--font-size-xs); display: block; margin-bottom: 6px;">✓ IMPLEMENTED & SHIPPED:</strong>
              <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                ${p.tech_stack.used.map(t => `<span class="badge badge-success" style="font-size: 0.7rem;">${t}</span>`).join('')}
              </div>
            </div>
            <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
              <strong style="color: var(--color-primary); font-size: var(--font-size-xs); display: block; margin-bottom: 6px;">⚙️ ARCHITECTURALLY MASTERED:</strong>
              <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                ${p.tech_stack.understood.map(t => `<span class="badge badge-primary" style="font-size: 0.7rem;">${t}</span>`).join('')}
              </div>
            </div>
            ${p.tech_stack.explored && p.tech_stack.explored.length ? `
              <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
                <strong style="color: var(--color-warning); font-size: var(--font-size-xs); display: block; margin-bottom: 6px;">🔬 EXPLORED / ROADMAP:</strong>
                <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                  ${p.tech_stack.explored.map(t => `<span class="badge badge-warning" style="font-size: 0.7rem;">${t}</span>`).join('')}
                </div>
              </div>
            ` : ''}
          </div>
        </div>
      </div>

      <!-- Architecture Pipeline Card -->
      <div class="card" style="margin-bottom: var(--space-5);">
        <div class="card-header">
          <h3 class="card-title">🏗️ High-Level System Architecture & Ingestion Flow</h3>
          <span class="badge badge-primary">Pipeline Flow</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: var(--space-3);">
          ${p.architecture_flow.map((step, sidx) => `
            <div style="display: flex; align-items: flex-start; gap: var(--space-3); background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
              <div style="background: var(--color-primary); color: white; border-radius: 50%; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 800; flex-shrink: 0;">
                ${sidx + 1}
              </div>
              <div style="font-size: var(--font-size-sm); color: var(--text-primary); line-height: 1.5;">
                ${step}
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- Interview Defense Questions -->
      <div class="card" style="margin-bottom: var(--space-5);">
        <div class="card-header">
          <h3 class="card-title">🛡️ Technical Interview Defense: Questions & Senior Engineer Answers</h3>
          <span class="badge badge-warning">Zero Fluff Defense</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: var(--space-4);">
          ${p.interview_defense.map(qa => `
            <div style="border-left: 3px solid var(--color-primary); padding-left: var(--space-3);">
              <strong style="color: var(--text-primary); font-size: var(--font-size-base); display: block; margin-bottom: var(--space-1);">
                Q: ${qa.q}
              </strong>
              <p style="margin: 0; font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6; background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
                ${qa.a}
              </p>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- ATS-Optimized Resume Bullets -->
      <div class="card" style="margin-bottom: var(--space-5); border-top: 3px solid var(--color-success);">
        <div class="card-header">
          <h3 class="card-title">📄 ATS-Optimized Resume Bullet Points (Copy-Paste Ready)</h3>
          <span class="badge badge-success">XYZ Format Action Verbs</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: var(--space-3);">
          ${p.resume_bullets.map(b => `
            <div style="display: flex; justify-content: space-between; align-items: center; gap: var(--space-3); background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm);">
              <div style="font-size: var(--font-size-sm); color: var(--text-primary); line-height: 1.5;">
                • ${b}
              </div>
              <button class="btn btn-secondary btn-sm copy-bullet-btn" data-bullet="${b}" style="flex-shrink: 0; padding: 2px 8px;">
                📋 Copy
              </button>
            </div>
          `).join('')}
        </div>
      </div>
    </div>
  `;
}
