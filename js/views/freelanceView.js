/**
 * Freelance Monetization Roadmap & Client Services View
 */

import { Storage } from '../storage.js';

export function renderFreelanceView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING FREELANCE BLUEPRINT...</div>
      <h2>Retrieving High-Yield Client Monetization Systems</h2>
    </div>
  `;

  fetch('content/freelance/freelance_all.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load freelance data');
      return res.json();
    })
    .then(freelanceData => {
      buildFreelancePage(container, freelanceData, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Freelance Blueprint</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildFreelancePage(container, data, daysIndex) {
  const proposalTemplate = `Subject: Automated [PDF Data Extraction / Telegram Alert Bot / Scraper] for [Client Company Name]

Hi [Client Name],

I noticed that your team currently processes [mention tedious manual workflow, e.g., legal/invoice PDFs or manual market alerts] manually. 

I am a Python Backend & Automation Engineer with production experience building [mention relevant project, e.g., high-throughput document extraction pipelines / real-time alert engines]. 

I can automate this end-to-end for you within 5 to 7 business days:
1. Automated ingestion of [source documents / web feeds].
2. High-accuracy extraction/filtering into clean structured formats (Excel / CSV / REST API).
3. Automated push notifications directly to your team via Telegram or WhatsApp.

Here is a short screen recording demonstrating a similar pipeline I built: [Portfolio / Demo Link]

Would you be open to a 10-minute discovery call this Thursday at 4 PM IST to discuss how we can automate this for your team?

Best regards,
Sarthak Srivastava
Python Backend & Automation Engineer
Kanpur, India | GitHub: https://github.com/Sarthak-Srivastava13`;

  container.innerHTML = `
    <div class="freelance-header" style="margin-bottom: var(--space-6);">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">SECONDARY CAREER GOAL</div>
      <h1 style="margin-bottom: var(--space-1);">Freelance Monetization & Client Acquisition Engine</h1>
      <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
        Monetize your verified Python and backend skills within 30–45 days. Sell high-value automation tools rather than competing on low-cost generic web pages.
      </p>
    </div>

    <!-- 3 Core Sellable Services Grid -->
    <h3 style="margin-bottom: var(--space-4);">🛠️ 3 Turnkey Services You Can Package & Sell Today</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--space-4); margin-bottom: var(--space-6);">
      ${data.services.map((svc, idx) => `
        <div class="card" style="margin-bottom: 0; border-top: 4px solid var(--color-primary);">
          <div class="badge badge-primary" style="margin-bottom: var(--space-2);">SERVICE PACKAGE 0${idx + 1}</div>
          <h3 style="margin: 0 0 var(--space-2) 0; font-size: var(--font-size-lg);">${svc.title}</h3>
          
          <div style="margin-bottom: var(--space-3); font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.5;">
            <strong style="color: var(--text-primary); display: block;">What You Deliver:</strong>
            ${svc.what_you_sell}
          </div>

          <div style="background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-sm); margin-bottom: var(--space-3); font-size: var(--font-size-xs);">
            <strong style="color: var(--color-primary); display: block; margin-bottom: 2px;">Your Tech Arsenal:</strong>
            ${svc.what_you_know}
          </div>

          <div style="margin-bottom: var(--space-3); font-size: var(--font-size-xs); color: var(--text-secondary);">
            <strong>Target Clients:</strong> ${svc.target_clients}
          </div>

          <div style="background: var(--color-success-subtle); border-left: 3px solid var(--color-success); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-sm); font-weight: 700; color: var(--color-success);">
            💰 Pricing Benchmark: ${svc.pricing_guide}
          </div>
        </div>
      `).join('')}
    </div>

    <!-- Proposal & Milestone Framework -->
    <div class="card" style="margin-bottom: var(--space-6);">
      <div class="card-header">
        <h2 class="card-title">📜 Client Protection & Payment Milestone Framework</h2>
        <span class="badge badge-warning">Zero Financial Risk</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-4); margin-bottom: var(--space-4);">
        <div style="background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-sm);">
          <strong style="color: var(--color-primary); display: block; font-size: var(--font-size-base); margin-bottom: 6px;">
            1. 30% Advance Deposit
          </strong>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin: 0; line-height: 1.5;">
            Never write a single line of client code or configure cloud servers without an upfront deposit. This filters out unserious inquiries immediately.
          </p>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-sm);">
          <strong style="color: var(--color-warning); display: block; font-size: var(--font-size-base); margin-bottom: 6px;">
            2. 40% Functional Staging Milestone
          </strong>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin: 0; line-height: 1.5;">
            Deploy a working staging prototype on your own server/domain or provide a live screen demo demonstrating end-to-end functionality.
          </p>
        </div>

        <div style="background: var(--bg-surface-2); padding: var(--space-4); border-radius: var(--radius-sm);">
          <strong style="color: var(--color-success); display: block; font-size: var(--font-size-base); margin-bottom: 6px;">
            3. 30% Final Handover & Source Code
          </strong>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin: 0; line-height: 1.5;">
            Collect final balance payment before transferring root server credentials, GitHub repository ownership, or API keys.
          </p>
        </div>
      </div>

      <div style="background: var(--color-warning-subtle); border-left: 3px solid var(--color-warning); padding: var(--space-3); border-radius: var(--radius-sm); font-size: var(--font-size-sm); color: var(--text-primary);">
        <strong>Scope Protection Rule:</strong> ${data.proposal_framework.scope_protection}
      </div>
    </div>

    <!-- Ready-to-Use Outreach Template -->
    <div class="card">
      <div class="card-header">
        <h2 class="card-title">✉️ High-Conversion Cold Outreach Proposal Template</h2>
        <button id="copy-proposal-btn" class="btn btn-secondary btn-sm">📋 Copy Outreach Template</button>
      </div>
      <div class="code-container">
        <pre><code class="language-markdown" id="proposal-text-block">${proposalTemplate}</code></pre>
      </div>
    </div>
  `;

  // Attach copy button listener
  container.querySelector('#copy-proposal-btn')?.addEventListener('click', (e) => {
    const btn = e.target;
    navigator.clipboard.writeText(proposalTemplate).then(() => {
      const orig = btn.textContent;
      btn.textContent = '✓ Copied!';
      btn.classList.add('btn-success');
      setTimeout(() => {
        btn.textContent = orig;
        btn.classList.remove('btn-success');
      }, 2000);
    });
  });
}
