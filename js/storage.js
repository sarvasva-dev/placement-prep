/**
 * LocalStorage State Management Engine for Sarthak 30-Day Master
 */

const STORAGE_KEYS = {
  PROGRESS: 'sarthak_study_progress',
  CHECKLISTS: 'sarthak_day_checklists',
  TEST_RESULTS: 'sarthak_test_results',
  BOOKMARKS: 'sarthak_bookmarks',
  NOTES: 'sarthak_notes',
  THEME: 'sarthak_theme',
  ACTIVE_DAY: 'sarthak_active_day'
};

export const Storage = {
  // Theme Preference
  getTheme() {
    return localStorage.getItem(STORAGE_KEYS.THEME) || 'dark';
  },

  setTheme(theme) {
    localStorage.setItem(STORAGE_KEYS.THEME, theme);
    document.documentElement.setAttribute('data-theme', theme);
  },

  // Active / Current Day
  getActiveDay() {
    const d = parseInt(localStorage.getItem(STORAGE_KEYS.ACTIVE_DAY), 10);
    return isNaN(d) ? 1 : Math.max(1, Math.min(30, d));
  },

  setActiveDay(day) {
    localStorage.setItem(STORAGE_KEYS.ACTIVE_DAY, day);
  },

  // Day Completion Status
  getProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.PROGRESS)) || {};
    } catch {
      return {};
    }
  },

  isDayComplete(day) {
    const progress = this.getProgress();
    return !!progress[day];
  },

  toggleDayComplete(day) {
    const progress = this.getProgress();
    progress[day] = !progress[day];
    localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(progress));
    return progress[day];
  },

  getCompletedDaysCount() {
    const progress = this.getProgress();
    return Object.values(progress).filter(Boolean).length;
  },

  // Daily Workflow Checklist
  getDayChecklist(day) {
    try {
      const all = JSON.parse(localStorage.getItem(STORAGE_KEYS.CHECKLISTS)) || {};
      return all[day] || {
        sem: false,
        pyq: false,
        apt: false,
        code: false,
        cs: false,
        proj: false,
        test: false,
        rev: false
      };
    } catch {
      return { sem: false, pyq: false, apt: false, code: false, cs: false, proj: false, test: false, rev: false };
    }
  },

  saveDayChecklist(day, checklist) {
    try {
      const all = JSON.parse(localStorage.getItem(STORAGE_KEYS.CHECKLISTS)) || {};
      all[day] = checklist;
      localStorage.setItem(STORAGE_KEYS.CHECKLISTS, JSON.stringify(all));
      
      // Auto-mark day complete if all 8 tasks checked
      const allDone = Object.values(checklist).every(Boolean);
      const progress = this.getProgress();
      progress[day] = allDone;
      localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(progress));
    } catch (e) {
      console.error('Failed to save checklist:', e);
    }
  },

  // Test Scores
  saveTestScore(day, score, maxScore, mistakes = []) {
    try {
      const results = JSON.parse(localStorage.getItem(STORAGE_KEYS.TEST_RESULTS)) || {};
      results[day] = {
        score,
        maxScore,
        percentage: Math.round((score / maxScore) * 100),
        date: new Date().toISOString(),
        mistakes
      };
      localStorage.setItem(STORAGE_KEYS.TEST_RESULTS, JSON.stringify(results));
    } catch (e) {
      console.error('Failed to save test score:', e);
    }
  },

  getTestScore(day) {
    try {
      const results = JSON.parse(localStorage.getItem(STORAGE_KEYS.TEST_RESULTS)) || {};
      return results[day] || null;
    } catch {
      return null;
    }
  },

  getAllTestResults() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.TEST_RESULTS)) || {};
    } catch {
      return {};
    }
  },

  // Bookmarks
  getBookmarks() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.BOOKMARKS)) || [];
    } catch {
      return [];
    }
  },

  isBookmarked(id) {
    const list = this.getBookmarks();
    return list.some(b => b.id === id);
  },

  toggleBookmark(item) {
    let list = this.getBookmarks();
    const idx = list.findIndex(b => b.id === item.id);
    if (idx >= 0) {
      list.splice(idx, 1);
    } else {
      list.push({ ...item, timestamp: Date.now() });
    }
    localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(list));
    return idx < 0; // True if newly added
  },

  // Personal Notes
  getNote(id) {
    try {
      const notes = JSON.parse(localStorage.getItem(STORAGE_KEYS.NOTES)) || {};
      return notes[id] || '';
    } catch {
      return '';
    }
  },

  saveNote(id, text) {
    try {
      const notes = JSON.parse(localStorage.getItem(STORAGE_KEYS.NOTES)) || {};
      if (text.trim()) {
        notes[id] = text;
      } else {
        delete notes[id];
      }
      localStorage.setItem(STORAGE_KEYS.NOTES, JSON.stringify(notes));
    } catch (e) {
      console.error('Failed to save note:', e);
    }
  }
};
