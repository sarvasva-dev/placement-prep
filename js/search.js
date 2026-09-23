/**
 * Global Search Index & Command Palette (Ctrl+K)
 */

export class GlobalSearch {
  constructor(daysIndex, semesterData, pyqsData, aptitudeData, codingData, projectsData) {
    this.daysIndex = daysIndex || [];
    this.semesterData = semesterData || {};
    this.pyqsData = pyqsData || [];
    this.aptitudeData = aptitudeData || [];
    this.codingData = codingData || [];
    this.projectsData = projectsData || {};
    this.searchIndex = [];
    this.buildIndex();
  }

  buildIndex() {
    // 1. Index 30 Days
    this.daysIndex.forEach(d => {
      this.searchIndex.push({
        type: 'Day Chapter',
        title: `Day ${d.day}: ${d.title}`,
        subtitle: `${d.subject} • ${d.topic}`,
        hash: `#day/${d.day}`,
        keywords: `${d.title} ${d.subject} ${d.topic} ${d.aptitude} ${d.core_cs} ${d.project}`.toLowerCase()
      });
    });

    // 2. Index PYQs
    this.pyqsData.forEach(p => {
      this.searchIndex.push({
        type: 'University PYQ',
        title: `[${p.subject}] ${p.question.substring(0, 75)}...`,
        subtitle: `Exam Session: ${p.pyq_year}`,
        hash: `#pyqs?q=${encodeURIComponent(p.topic)}`,
        keywords: `${p.subject} ${p.topic} ${p.question} ${p.pyq_year}`.toLowerCase()
      });
    });

    // 3. Index Coding Problems
    this.codingData.forEach(c => {
      this.searchIndex.push({
        type: 'Coding / DSA',
        title: `${c.title}`,
        subtitle: `Day ${c.day} • ${c.importance}`,
        hash: `#coding?problem=${encodeURIComponent(c.title)}`,
        keywords: `${c.title} ${c.importance} ${c.solution_approach || ''}`.toLowerCase()
      });
    });

    // 4. Index Projects
    Object.entries(this.projectsData).forEach(([key, proj]) => {
      this.searchIndex.push({
        type: 'Project Defense',
        title: `${proj.name} — Architecture & Defense`,
        subtitle: `${proj.category}`,
        hash: `#projects/${key}`,
        keywords: `${proj.name} ${proj.category} ${proj.tech_stack?.used?.join(' ') || ''}`.toLowerCase()
      });
    });

    // 5. Index Core Navigation Routes
    const navShortcuts = [
      { type: 'Navigation', title: 'Dashboard & SGPA 9 Tracker', subtitle: 'Overview & Today Plan', hash: '#dashboard', keywords: 'dashboard home today sgpa' },
      { type: 'Navigation', title: '30-Day Timeline & Chapters', subtitle: 'All 30 Day Study Pages', hash: '#days', keywords: 'days timeline curriculum schedule' },
      { type: 'Navigation', title: 'Semester 5 Textbook & Syllabi', subtitle: '5001, 5002, 5003, 5004', hash: '#semester', keywords: 'semester 5 subjects 5001 5002 5003 5004 syllabus' },
      { type: 'Navigation', title: 'University PYQ Explorer', subtitle: 'CSJM Papers (2021-2025)', hash: '#pyqs', keywords: 'pyq previous year questions exam papers' },
      { type: 'Navigation', title: 'Aptitude Interactive Engine', subtitle: 'Quant, Logical, Verbal & Company Patterns', hash: '#aptitude', keywords: 'aptitude quant math reasoning company' },
      { type: 'Navigation', title: 'Coding Practice Hub', subtitle: '50+ Java DSA Solutions', hash: '#coding', keywords: 'coding dsa leetcode java algorithms' },
      { type: 'Navigation', title: 'Core Computer Science', subtitle: 'OS, DBMS, Networks, Python', hash: '#core-cs', keywords: 'core cs operating systems dbms sql networks' },
      { type: 'Navigation', title: 'Mock Interview Simulator', subtitle: 'Technical, HR & Project Defense', hash: '#interviews', keywords: 'interview mock hr star technical questions' },
      { type: 'Navigation', title: 'ATS Resume Center', subtitle: 'Python Backend & Software Dev Resumes', hash: '#resumes', keywords: 'resume cv ats backend developer' },
      { type: 'Navigation', title: 'Spaced Revision Engine', subtitle: 'Today, Yesterday, 7 Days Ago & Test Mistakes', hash: '#revision', keywords: 'revision spaced review flashcards mistakes' },
      { type: 'Navigation', title: 'Source Archive & Provenance', subtitle: 'Original Academic Files & Hashes', hash: '#source-archive', keywords: 'source archive provenance a drive manifests' },
      { type: 'Navigation', title: 'Freelance Readiness', subtitle: 'Client Services & Proposals', hash: '#freelance', keywords: 'freelance proposal retainer clients' },
      { type: 'Navigation', title: 'Do Not Study / Defer Guide', subtitle: 'Low-Yield Topics to Ignore', hash: '#do-not-study', keywords: 'ignore defer do not study low priority' }
    ];

    this.searchIndex.push(...navShortcuts);
  }

  query(searchTerm) {
    if (!searchTerm || !searchTerm.trim()) {
      return this.searchIndex.slice(0, 10);
    }
    const clean = searchTerm.trim().toLowerCase();
    const parts = clean.split(/\s+/);
    
    return this.searchIndex
      .filter(item => parts.every(p => item.keywords.includes(p) || item.title.toLowerCase().includes(p)))
      .slice(0, 15);
  }
}
