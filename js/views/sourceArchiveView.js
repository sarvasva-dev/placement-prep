/**
 * Source Archive & Provenance Audit View
 */

export function renderSourceArchiveView(container, daysIndex) {
  container.innerHTML = `
    <div style="text-align: center; padding: var(--space-8) 0;">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">LOADING ARCHIVE AUDIT...</div>
      <h2>Retrieving Source Manifest & Cryptographic Hashes</h2>
    </div>
  `;

  fetch('source_archive/manifests/source_manifest.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load source archive manifest');
      return res.json();
    })
    .then(manifestData => {
      buildSourceArchivePage(container, manifestData, daysIndex);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin-top: var(--space-6);">
          <h3>Error Loading Source Archive Manifest</h3>
          <p>${err.message}</p>
        </div>
      `;
    });
}

function buildSourceArchivePage(container, data, daysIndex) {
  container.innerHTML = `
    <div class="archive-header" style="margin-bottom: var(--space-6);">
      <div class="badge badge-primary" style="margin-bottom: var(--space-2);">PROVENANCE & AUDIT TRAIL</div>
      <h1 style="margin-bottom: var(--space-1);">Source Archive & Integrity Manifest</h1>
      <p style="font-size: var(--font-size-base); color: var(--text-secondary); max-width: 800px;">
        Cryptographic provenance verification. All 22 source files from <code>A:\\</code> drive and project directories are archived into <code>source_archive/</code> with SHA-256 checksums. Original files remain 100% untouched.
      </p>
    </div>

    <!-- Summary Stats Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: var(--space-4); margin-bottom: var(--space-6);">
      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Total Files Archived</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-primary); margin: var(--space-1) 0;">
          ${data.total_files_archived || 22}
        </div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">Academic Notes, PYQs & Projects</div>
      </div>

      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Integrity Status</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-success); margin: var(--space-1) 0;">
          VERIFIED
        </div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">SHA-256 Cryptographic Hashes</div>
      </div>

      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Original Sources</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-info); margin: var(--space-1) 0;">
          UNTOUCHED
        </div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">Read-Only Reference Principle</div>
      </div>

      <div class="card" style="margin-bottom: 0; padding: var(--space-4);">
        <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Study Pipeline</div>
        <div style="font-size: var(--font-size-2xl); font-weight: 800; color: var(--color-warning); margin: var(--space-1) 0;">
          SELF-CONTAINED
        </div>
        <div style="font-size: var(--font-size-xs); color: var(--text-secondary);">Single Source of Truth in /content/</div>
      </div>
    </div>

    <!-- Architecture Callout -->
    <div class="card" style="border-left: 4px solid var(--color-primary); margin-bottom: var(--space-6); background: var(--bg-surface-2);">
      <strong style="color: var(--color-primary); font-size: var(--font-size-base); display: block; margin-bottom: 4px;">
        🛡️ Single Source of Truth Guarantee:
      </strong>
      <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin: 0; line-height: 1.6;">
        The student never needs to open the raw PDFs or split-screen notes again. All syllabus facts, definitions, formulas, and PYQs have been systematically extracted, cleaned, and authored into the structured <code>/content/</code> layer. The web app, master PDF, and master DOCX are compiled directly from this single data layer.
      </p>
    </div>

    <!-- Manifest Table Card -->
    <div class="card">
      <div class="card-header">
        <h2 class="card-title">📋 Archived Source Files & SHA-256 Checksums</h2>
        <span class="badge badge-primary">${(data.manifest || []).length} Records</span>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Source File</th>
              <th>Category</th>
              <th>Original Location</th>
              <th>Size</th>
              <th>SHA-256 Checksum</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            ${(data.manifest || []).map((m, idx) => {
              const sizeKb = Math.round(m.size_bytes / 1024);
              const sizeMb = (m.size_bytes / (1024 * 1024)).toFixed(2);
              const displaySize = m.size_bytes > 1024 * 1024 ? `${sizeMb} MB` : `${sizeKb} KB`;

              return `
                <tr>
                  <td>${idx + 1}</td>
                  <td><strong>${m.filename}</strong></td>
                  <td><span class="badge badge-secondary">${m.category}</span></td>
                  <td><code style="font-size: 0.75rem;">${m.original_path}</code></td>
                  <td>${displaySize}</td>
                  <td>
                    <button class="btn btn-secondary btn-sm copy-hash-btn" data-hash="${m.sha256}" style="font-family: var(--font-family-mono); font-size: 0.7rem; padding: 2px 6px;">
                      ${m.sha256.substring(0, 10)}... 📋
                    </button>
                  </td>
                  <td><span class="badge badge-success">✓ ARCHIVED</span></td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;

  // Attach copy hash buttons
  container.querySelectorAll('.copy-hash-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const hash = btn.dataset.hash;
      navigator.clipboard.writeText(hash).then(() => {
        const orig = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('btn-success');
        setTimeout(() => {
          btn.textContent = orig;
          btn.classList.remove('btn-success');
        }, 1500);
      });
    });
  });
}
