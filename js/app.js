/**
 * Sarthak 30-Day Placement & Semester Master Web Application
 * Master Application Orchestrator & Client Hash Router
 */

import { Storage } from './storage.js';
import { GlobalSearch } from './search.js';

// Import View Controllers
import { renderDashboard } from './views/dashboardView.js';
import { renderDayView } from './views/dayView.js';
import { renderSemesterView } from './views/semesterView.js';
import { renderPyqView } from './views/pyqView.js';
import { renderAptitudeView } from './views/aptitudeView.js';
import { renderCodingView } from './views/codingView.js';
import { renderCoreCsView } from './views/coreCsView.js';
import { renderProjectHubView } from './views/projectHubView.js';
import { renderInterviewView } from './views/interviewView.js';
import { renderResumeView } from './views/resumeView.js';
import { renderRevisionView } from './views/revisionView.js';
import { renderFreelanceView } from './views/freelanceView.js';
import { renderDoNotStudyView } from './views/doNotStudyView.js';
import { renderSourceArchiveView } from './views/sourceArchiveView.js';

class StudyApp {
  constructor() {
    this.daysIndex = [];
    this.semesterData = {};
    this.pyqsData = [];
    this.aptitudeData = [];
    this.codingData = [];
    this.projectsData = {};
    this.searchEngine = null;

    this.contentContainer = document.getElementById('content-container');
    this.sidebar = document.getElementById('sidebar');
    this.modalOverlay = document.getElementById('command-palette-modal');
    this.paletteInput = document.getElementById('palette-search-input');
    this.paletteResults = document.getElementById('palette-results-list');
  }

  async init() {
    // 1. Initialize Theme
    const currentTheme = Storage.getTheme();
    Storage.setTheme(currentTheme);
    this.updateThemeButton(currentTheme);

    // 2. Fetch Core Manifests & Index Data
    try {
      const [daysRes, semRes, pyqsRes, aptRes, codeRes, projRes] = await Promise.all([
        fetch('content/days_index.json'),
        fetch('content/semester/semester_all.json'),
        fetch('content/pyqs/all_pyqs.json'),
        fetch('content/aptitude/all_aptitude.json'),
        fetch('content/coding/all_coding.json'),
        fetch('content/projects/projects_all.json')
      ]);

      this.daysIndex = await daysRes.json();
      this.semesterData = await semRes.json();
      this.pyqsData = await pyqsRes.json();
      this.aptitudeData = await aptRes.json();
      this.codingData = await codeRes.json();
      this.projectsData = await projRes.json();

      // Initialize Global Search Engine
      this.searchEngine = new GlobalSearch(
        this.daysIndex,
        this.semesterData,
        this.pyqsData,
        this.aptitudeData,
        this.codingData,
        this.projectsData
      );

      // Setup Listeners
      this.setupEventListeners();

      // Dispatch initial route
      this.handleRoute();

    } catch (err) {
      console.error('Failed to initialize Study App:', err);
      this.contentContainer.innerHTML = `
        <div class="card" style="border-left: 4px solid var(--color-danger); margin: var(--space-6);">
          <h2>Initialization Error</h2>
          <p>Failed to load essential curriculum datasets: ${err.message}</p>
          <button class="btn btn-primary" onclick="location.reload()">Reload Application</button>
        </div>
      `;
    }
  }

  setupEventListeners() {
    // Hash change router
    window.addEventListener('hashchange', () => this.handleRoute());

    // Theme toggle button
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const nextTheme = Storage.getTheme() === 'dark' ? 'light' : 'dark';
        Storage.setTheme(nextTheme);
        this.updateThemeButton(nextTheme);
      });
    }

    // Mobile sidebar hamburger toggle
    const menuBtn = document.getElementById('menu-toggle-btn');
    if (menuBtn) {
      menuBtn.addEventListener('click', () => {
        this.sidebar.classList.toggle('open');
      });
    }

    // Command palette triggers (Ctrl+K or Topbar Button)
    const searchTrigger = document.getElementById('search-trigger-btn');
    if (searchTrigger) {
      searchTrigger.addEventListener('click', () => this.openCommandPalette());
    }

    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        this.openCommandPalette();
      }
      if (e.key === 'Escape' && this.modalOverlay.classList.contains('active')) {
        this.closeCommandPalette();
      }
    });

    // Close palette on backdrop click
    if (this.modalOverlay) {
      this.modalOverlay.addEventListener('click', (e) => {
        if (e.target === this.modalOverlay) {
          this.closeCommandPalette();
        }
      });
    }

    // Live search input
    if (this.paletteInput) {
      this.paletteInput.addEventListener('input', (e) => {
        this.renderSearchResults(e.target.value);
      });
    }
  }

  updateThemeButton(theme) {
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
      themeBtn.innerHTML = theme === 'dark' ? '☀️ Light' : '🌙 Dark';
    }
  }

  openCommandPalette() {
    if (!this.modalOverlay) return;
    this.modalOverlay.classList.add('active');
    this.paletteInput.value = '';
    this.renderSearchResults('');
    setTimeout(() => this.paletteInput.focus(), 50);
  }

  closeCommandPalette() {
    if (!this.modalOverlay) return;
    this.modalOverlay.classList.remove('active');
  }

  renderSearchResults(query) {
    if (!this.searchEngine) return;
    const results = this.searchEngine.query(query);

    if (results.length === 0) {
      this.paletteResults.innerHTML = `
        <div style="padding: var(--space-4); text-align: center; color: var(--text-muted); font-size: var(--font-size-sm);">
          No matching lessons, questions, or codes found.
        </div>
      `;
      return;
    }

    this.paletteResults.innerHTML = results.map(r => `
      <div class="palette-item" data-hash="${r.hash}">
        <div>
          <span class="badge badge-secondary" style="font-size: 0.7rem; margin-right: 6px;">${r.type}</span>
          <strong style="color: var(--text-primary); font-size: var(--font-size-sm);">${r.title}</strong>
          ${r.subtitle ? `<div style="font-size: var(--font-size-xs); color: var(--text-muted); margin-top: 2px;">${r.subtitle}</div>` : ''}
        </div>
        <span style="font-size: var(--font-size-xs); color: var(--color-primary);">Jump →</span>
      </div>
    `).join('');

    // Attach click handlers to items
    this.paletteResults.querySelectorAll('.palette-item').forEach(item => {
      item.addEventListener('click', () => {
        const hash = item.dataset.hash;
        this.closeCommandPalette();
        window.location.hash = hash;
      });
    });
  }

  renderNotFound(rawHash, message = null) {
    const safeHash = String(rawHash || '').replace(/[<>&"']/g, '');
    this.contentContainer.innerHTML = `
      <div class="card" style="border-left: 4px solid var(--color-danger); max-width: 680px; margin: var(--space-8) auto; padding: var(--space-6); text-align: center;">
        <div class="badge badge-danger" style="margin-bottom: var(--space-2);">404 ERROR</div>
        <h2 style="margin-bottom: var(--space-2); color: var(--text-primary);">Route Not Found</h2>
        <p style="color: var(--text-secondary); margin-bottom: var(--space-4); line-height: 1.6;">
          ${message ? message : `The requested location <code style="color: var(--color-danger); font-size: var(--font-size-sm);">#${safeHash}</code> does not match any valid curriculum view.`}
        </p>
        <div style="display: flex; gap: var(--space-3); justify-content: center; flex-wrap: wrap;">
          <a href="#dashboard" class="btn btn-primary">Go to Dashboard</a>
          <a href="#day/1" class="btn btn-secondary">Go to Day 1</a>
        </div>
      </div>
    `;
  }

  handleRoute() {
    const rawHash = (window.location.hash.slice(1) || 'dashboard').trim();
    const [pathPart, queryPart] = rawHash.split('?');
    const segments = pathPart.split('/').map(s => s.trim()).filter(Boolean);
    const rootRoute = segments[0] || 'dashboard';
    const subRoute = segments[1];
    const queryParams = new URLSearchParams(queryPart || '');

    // Close mobile drawer on route change
    if (this.sidebar) {
      this.sidebar.classList.remove('open');
    }

    // Update active nav-item in sidebar
    this.updateActiveNavLink(rootRoute, rawHash);

    // Scroll window to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Route dispatch
    switch (rootRoute) {
      case 'dashboard':
      case '':
        renderDashboard(this.contentContainer, this.daysIndex, this.semesterData);
        break;

      case 'days':
        renderDashboard(this.contentContainer, this.daysIndex, this.semesterData);
        break;

      case 'day': {
        const dayNumber = parseInt(subRoute || '1', 10);
        if (isNaN(dayNumber) || dayNumber < 1 || dayNumber > 30) {
          this.renderNotFound(rawHash, `Day <strong>${subRoute || ''}</strong> is out of range. Valid preparation days are <strong>Day 1 to Day 30</strong>.`);
          return;
        }
        renderDayView(this.contentContainer, dayNumber, this.daysIndex);
        break;
      }

      case 'semester':
        renderSemesterView(this.contentContainer, this.daysIndex);
        break;

      case 'pyqs':
        renderPyqView(this.contentContainer, this.daysIndex, queryParams.get('q') || '');
        break;

      case 'aptitude':
        renderAptitudeView(this.contentContainer, this.daysIndex);
        break;

      case 'coding':
        renderCodingView(this.contentContainer, this.daysIndex, queryParams.get('problem') || '');
        break;

      case 'core-cs':
        renderCoreCsView(this.contentContainer, this.daysIndex);
        break;

      case 'projects':
        renderProjectHubView(this.contentContainer, this.daysIndex, subRoute);
        break;

      case 'interviews':
        renderInterviewView(this.contentContainer, this.daysIndex);
        break;

      case 'resumes':
        renderResumeView(this.contentContainer, this.daysIndex);
        break;

      case 'revision':
        renderRevisionView(this.contentContainer, this.daysIndex);
        break;

      case 'freelance':
        renderFreelanceView(this.contentContainer, this.daysIndex);
        break;

      case 'do-not-study':
        renderDoNotStudyView(this.contentContainer, this.daysIndex);
        break;

      case 'source-archive':
        renderSourceArchiveView(this.contentContainer, this.daysIndex);
        break;

      default:
        this.renderNotFound(rawHash);
        break;
    }
  }

  updateActiveNavLink(rootRoute, fullHash) {
    const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
    navItems.forEach(item => {
      item.classList.remove('active');
      const href = item.getAttribute('href');
      if (href) {
        const itemHash = href.slice(1);
        if (itemHash === fullHash || (rootRoute !== 'day' && itemHash === rootRoute)) {
          item.classList.add('active');
        }
      }
    });
  }
}

// Bootstrap Application on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  const app = new StudyApp();
  app.init();
});
