/**
 * SVG Diagram Generators for Core Computer Science Topics (OS, DBMS, Networks, Python, System Design)
 */

export function renderCoreCsSvg(topic = '', conceptText = '') {
  const t = (topic + ' ' + conceptText).toLowerCase();

  if (t.includes('process') && (t.includes('pcb') || t.includes('state') || t.includes('context switch'))) {
    return createProcessStateSvg();
  }
  if (t.includes('scheduling') || t.includes('fcfs') || t.includes('sjf') || t.includes('round robin')) {
    return createCpuSchedulingSvg();
  }
  if (t.includes('synchronization') || t.includes('critical section') || t.includes('semaphore') || t.includes('mutex')) {
    return createCriticalSectionSvg();
  }
  if (t.includes('producer') || t.includes('consumer') || t.includes('dining') || t.includes('readers-writers')) {
    return createProducerConsumerSvg();
  }
  if (t.includes('deadlock') || t.includes('coffman') || t.includes('banker') || t.includes('rag')) {
    return createDeadlockConditionsSvg();
  }
  if (t.includes('paging') || t.includes('tlb') || t.includes('segmentation') || t.includes('virtual memory') || t.includes('page fault')) {
    return createVirtualMemoryTlbSvg();
  }
  if (t.includes('3-tier') || t.includes('schema') || t.includes('ansi-sparc') || t.includes('data independence')) {
    return createDbms3TierSvg();
  }
  if (t.includes('normaliz') || t.includes('1nf') || t.includes('2nf') || t.includes('3nf') || t.includes('bcnf')) {
    return createNormalizationSvg();
  }
  if (t.includes('acid') || t.includes('transaction') || t.includes('atomicity')) {
    return createAcidPropertiesSvg();
  }
  if (t.includes('2pl') || t.includes('lock') || t.includes('concurrency') || t.includes('serializ')) {
    return createTwoPhaseLockingSvg();
  }
  if (t.includes('b+ tree') || t.includes('b-tree') || t.includes('index') || t.includes('clustered')) {
    return createBPlusTreeIndexSvg();
  }
  if (t.includes('handshake') || t.includes('tcp vs udp') || t.includes('3-way') || t.includes('transport layer')) {
    return createTcpHandshakeSvg();
  }
  if (t.includes('congestion') || t.includes('slow start') || t.includes('flow control')) {
    return createTcpCongestionControlSvg();
  }
  if (t.includes('crc') || t.includes('framing') || t.includes('error detection')) {
    return createCrcFramingSvg();
  }
  if (t.includes('gil') || t.includes('global interpreter lock') || t.includes('event loop') || t.includes('asyncio')) {
    return createPythonGilSvg();
  }
  if (t.includes('system design') || t.includes('rate limit') || t.includes('load balanc') || t.includes('cache') || t.includes('url short')) {
    return createSystemDesignOverviewSvg();
  }

  // Fallback to stylized high-contrast Core CS architecture card
  return createCoreCsGeneralSvg(topic);
}

function createProcessStateSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">OPERATING SYSTEMS</span>
      <span class="svg-title">OS 5-State Process Lifecycle & PCB Transitions</span>
    </div>
    <svg viewBox="0 0 860 260" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <defs>
        <marker id="csArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="csArrowAmber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#fbbf24" />
        </marker>
      </defs>

      <!-- New State -->
      <g transform="translate(40, 100)">
        <rect width="110" height="60" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
        <text x="55" y="35" text-anchor="middle" fill="#f8fafc" font-weight="700" font-size="14">NEW</text>
      </g>
      <line x1="150" y1="130" x2="210" y2="130" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#csArrow)"/>
      <text x="180" y="120" text-anchor="middle" fill="#94a3b8" font-size="10">Admit</text>

      <!-- Ready State -->
      <g transform="translate(220, 100)">
        <rect width="130" height="60" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <text x="65" y="35" text-anchor="middle" fill="#ffffff" font-weight="800" font-size="14">READY</text>
      </g>
      <line x1="350" y1="120" x2="430" y2="120" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#csArrow)"/>
      <text x="390" y="112" text-anchor="middle" fill="#38bdf8" font-size="10">Dispatch</text>

      <!-- Running State -->
      <g transform="translate(440, 100)">
        <rect width="140" height="60" rx="8" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
        <text x="70" y="35" text-anchor="middle" fill="#ffffff" font-weight="800" font-size="14">RUNNING</text>
      </g>

      <!-- Preempt Arrow back from Running to Ready -->
      <path d="M 480 100 C 480 60, 290 60, 290 100" fill="none" stroke="#fbbf24" stroke-width="2" marker-end="url(#csArrowAmber)"/>
      <text x="385" y="52" text-anchor="middle" fill="#fcd34d" font-size="11" font-weight="600">Interrupt / Time Slice Expired</text>

      <!-- Terminated State -->
      <line x1="580" y1="130" x2="670" y2="130" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#csArrow)"/>
      <text x="625" y="120" text-anchor="middle" fill="#94a3b8" font-size="10">Exit</text>
      <g transform="translate(680, 100)">
        <rect width="130" height="60" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
        <text x="65" y="35" text-anchor="middle" fill="#fca5a5" font-weight="700" font-size="14">TERMINATED</text>
      </g>

      <!-- Waiting / Blocked State -->
      <g transform="translate(330, 190)">
        <rect width="150" height="50" rx="8" fill="#431407" stroke="#ea580c" stroke-width="2"/>
        <text x="75" y="30" text-anchor="middle" fill="#fdba74" font-weight="700" font-size="13">WAITING / I/O</text>
      </g>

      <!-- Running -> Waiting -->
      <path d="M 520 160 L 520 215 L 480 215" fill="none" stroke="#fb923c" stroke-width="2" marker-end="url(#csArrow)"/>
      <text x="535" y="195" fill="#fdba74" font-size="10">I/O Wait</text>

      <!-- Waiting -> Ready -->
      <path d="M 330 215 L 260 215 L 260 160" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#csArrow)"/>
      <text x="235" y="195" fill="#38bdf8" font-size="10">I/O Done</text>
    </svg>
  </div>
  `;
}

function createCpuSchedulingSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">OPERATING SYSTEMS</span>
      <span class="svg-title">CPU Scheduling Gantt Chart & Turnaround Time Analysis</span>
    </div>
    <svg viewBox="0 0 860 230" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <text x="40" y="40" fill="#38bdf8" font-weight="700" font-size="14">Round Robin Execution Timeline (Quantum = 4ms):</text>
      
      <!-- Gantt Bar -->
      <g transform="translate(40, 60)">
        <!-- P1 (0 - 4) -->
        <rect x="0" y="0" width="140" height="50" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="70" y="30" text-anchor="middle" fill="#ffffff" font-weight="800">P1</text>
        <text x="0" y="68" fill="#94a3b8" font-size="11">0ms</text>

        <!-- P2 (4 - 7) -->
        <rect x="140" y="0" width="110" height="50" fill="#16a34a" stroke="#4ade80" stroke-width="1.5"/>
        <text x="195" y="30" text-anchor="middle" fill="#ffffff" font-weight="800">P2</text>
        <text x="140" y="68" fill="#94a3b8" font-size="11">4ms</text>

        <!-- P3 (7 - 11) -->
        <rect x="250" y="0" width="140" height="50" fill="#9333ea" stroke="#c084fc" stroke-width="1.5"/>
        <text x="320" y="30" text-anchor="middle" fill="#ffffff" font-weight="800">P3</text>
        <text x="250" y="68" fill="#94a3b8" font-size="11">7ms</text>

        <!-- P1 Round 2 (11 - 15) -->
        <rect x="390" y="0" width="140" height="50" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="460" y="30" text-anchor="middle" fill="#ffffff" font-weight="800">P1</text>
        <text x="390" y="68" fill="#94a3b8" font-size="11">11ms</text>

        <!-- P3 Round 2 (15 - 17) -->
        <rect x="530" y="0" width="80" height="50" fill="#9333ea" stroke="#c084fc" stroke-width="1.5"/>
        <text x="570" y="30" text-anchor="middle" fill="#ffffff" font-weight="800">P3</text>
        <text x="530" y="68" fill="#94a3b8" font-size="11">15ms</text>
        <text x="610" y="68" fill="#94a3b8" font-size="11">17ms</text>
      </g>

      <!-- Legend & Formulas -->
      <g transform="translate(40, 160)">
        <rect width="770" height="50" rx="8" fill="#0f172a" stroke="#334155"/>
        <text x="20" y="30" fill="#38bdf8" font-weight="700" font-size="12">Key Asymptotic Formulas:</text>
        <text x="200" y="30" fill="#f8fafc" font-size="12">Turnaround Time (TAT) = Completion Time - Arrival Time</text>
        <text x="560" y="30" fill="#a7f3d0" font-size="12">Waiting Time (WT) = TAT - Burst Time</text>
      </g>
    </svg>
  </div>
  `;
}

function createCriticalSectionSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">SYNCHRONIZATION</span>
      <span class="svg-title">Critical Section Problem & Mutex / Semaphore Protocol</span>
    </div>
    <svg viewBox="0 0 860 240" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 4 Sections Flow -->
      <g transform="translate(40, 40)">
        <rect width="160" height="80" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="80" y="35" text-anchor="middle" fill="#38bdf8" font-weight="800" font-size="13">1. ENTRY SECTION</text>
        <text x="80" y="60" text-anchor="middle" fill="#94a3b8" font-size="11">wait(mutex) / Lock</text>
      </g>

      <line x1="200" y1="80" x2="240" y2="80" stroke="#38bdf8" stroke-width="3" marker-end="url(#csArrow)"/>

      <g transform="translate(250, 30)">
        <rect width="210" height="100" rx="10" fill="#7f1d1d" stroke="#ef4444" stroke-width="2.5"/>
        <text x="105" y="38" text-anchor="middle" fill="#fecaca" font-weight="800" font-size="14">2. CRITICAL SECTION</text>
        <text x="105" y="62" text-anchor="middle" fill="#ffffff" font-size="11">Shared Memory Access</text>
        <text x="105" y="82" text-anchor="middle" fill="#fca5a5" font-size="10">MUTUAL EXCLUSION ENFORCED</text>
      </g>

      <line x1="460" y1="80" x2="500" y2="80" stroke="#38bdf8" stroke-width="3" marker-end="url(#csArrow)"/>

      <g transform="translate(510, 40)">
        <rect width="150" height="80" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <text x="75" y="35" text-anchor="middle" fill="#34d399" font-weight="800" font-size="13">3. EXIT SECTION</text>
        <text x="75" y="60" text-anchor="middle" fill="#94a3b8" font-size="11">signal(mutex) / Unlock</text>
      </g>

      <line x1="660" y1="80" x2="700" y2="80" stroke="#38bdf8" stroke-width="3" marker-end="url(#csArrow)"/>

      <g transform="translate(710, 40)">
        <rect width="120" height="80" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
        <text x="60" y="35" text-anchor="middle" fill="#cbd5e1" font-weight="700" font-size="12">REMAINDER</text>
        <text x="60" y="60" text-anchor="middle" fill="#64748b" font-size="10">Local tasks</text>
      </g>

      <!-- 3 Criteria Check Box -->
      <g transform="translate(40, 160)">
        <rect width="790" height="60" rx="8" fill="#0f172a" stroke="#a855f7"/>
        <text x="30" y="25" fill="#c084fc" font-weight="700" font-size="12">3 MANDATORY REQUIREMENTS FOR CORRECTNESS:</text>
        <text x="30" y="48" fill="#f8fafc" font-size="11">1. Mutual Exclusion (At most 1 thread in CS)   |   2. Progress (No infinite wait for entry)   |   3. Bounded Waiting (No starvation)</text>
      </g>
    </svg>
  </div>
  `;
}

function createProducerConsumerSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">SYNCHRONIZATION</span>
      <span class="svg-title">Producer-Consumer Bounded Buffer Architecture (Semaphores)</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Producer -->
      <g transform="translate(40, 50)">
        <rect width="180" height="110" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="45" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">PRODUCER</text>
        <text x="90" y="75" text-anchor="middle" fill="#e0f2fe" font-size="12">wait(empty); wait(mutex)</text>
        <text x="90" y="95" text-anchor="middle" fill="#bae6fd" font-size="11">signal(mutex); signal(full)</text>
      </g>

      <line x1="220" y1="105" x2="300" y2="105" stroke="#38bdf8" stroke-width="3" marker-end="url(#csArrow)"/>
      <text x="260" y="95" text-anchor="middle" fill="#38bdf8" font-size="11">produce()</text>

      <!-- Circular Bounded Buffer -->
      <g transform="translate(310, 35)">
        <rect width="250" height="140" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
        <text x="125" y="30" text-anchor="middle" fill="#d8b4fe" font-weight="800" font-size="13">BOUNDED BUFFER [N=5]</text>
        
        <!-- Slots -->
        <rect x="25" y="45" width="35" height="40" rx="4" fill="#3b0764" stroke="#c084fc"/>
        <text x="42" y="70" text-anchor="middle" fill="#fff" font-size="12">D1</text>
        
        <rect x="65" y="45" width="35" height="40" rx="4" fill="#3b0764" stroke="#c084fc"/>
        <text x="82" y="70" text-anchor="middle" fill="#fff" font-size="12">D2</text>

        <rect x="105" y="45" width="35" height="40" rx="4" fill="#3b0764" stroke="#c084fc"/>
        <text x="122" y="70" text-anchor="middle" fill="#fff" font-size="12">D3</text>

        <rect x="145" y="45" width="35" height="40" rx="4" fill="#1e1b4b" stroke="#6366f1"/>
        <text x="162" y="70" text-anchor="middle" fill="#94a3b8" font-size="11">_</text>

        <rect x="185" y="45" width="35" height="40" rx="4" fill="#1e1b4b" stroke="#6366f1"/>
        <text x="202" y="70" text-anchor="middle" fill="#94a3b8" font-size="11">_</text>

        <text x="125" y="115" text-anchor="middle" fill="#a7f3d0" font-size="11">mutex=1 | empty=2 | full=3</text>
      </g>

      <line x1="560" y1="105" x2="640" y2="105" stroke="#34d399" stroke-width="3" marker-end="url(#csArrow)"/>
      <text x="600" y="95" text-anchor="middle" fill="#34d399" font-size="11">consume()</text>

      <!-- Consumer -->
      <g transform="translate(650, 50)">
        <rect width="170" height="110" rx="10" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <text x="85" y="45" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">CONSUMER</text>
        <text x="85" y="75" text-anchor="middle" fill="#ecfdf5" font-size="12">wait(full); wait(mutex)</text>
        <text x="85" y="95" text-anchor="middle" fill="#a7f3d0" font-size="11">signal(mutex); signal(empty)</text>
      </g>
    </svg>
  </div>
  `;
}

function createDeadlockConditionsSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">OPERATING SYSTEMS</span>
      <span class="svg-title">Deadlock: The 4 Coffman Conditions & Resource Allocation Cycle</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 4 Cards -->
      <g transform="translate(30, 40)">
        <rect width="180" height="140" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#f87171" font-weight="800" font-size="13">1. MUTUAL EXCLUSION</text>
        <text x="90" y="70" text-anchor="middle" fill="#e2e8f0" font-size="11">Resources cannot be</text>
        <text x="90" y="90" text-anchor="middle" fill="#e2e8f0" font-size="11">shared simultaneously.</text>
        <text x="90" y="120" text-anchor="middle" fill="#fca5a5" font-size="10">Non-shareable mode</text>
      </g>

      <g transform="translate(230, 40)">
        <rect width="180" height="140" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#fbbf24" font-weight="800" font-size="13">2. HOLD AND WAIT</text>
        <text x="90" y="70" text-anchor="middle" fill="#e2e8f0" font-size="11">Process holds 1 resource</text>
        <text x="90" y="90" text-anchor="middle" fill="#e2e8f0" font-size="11">while waiting for others.</text>
        <text x="90" y="120" text-anchor="middle" fill="#fde68a" font-size="10">Resource hoarding</text>
      </g>

      <g transform="translate(430, 40)">
        <rect width="180" height="140" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#60a5fa" font-weight="800" font-size="13">3. NO PREEMPTION</text>
        <text x="90" y="70" text-anchor="middle" fill="#e2e8f0" font-size="11">Resource can only be</text>
        <text x="90" y="90" text-anchor="middle" fill="#e2e8f0" font-size="11">released voluntarily.</text>
        <text x="90" y="120" text-anchor="middle" fill="#bfdbfe" font-size="10">No forced eviction</text>
      </g>

      <g transform="translate(630, 40)">
        <rect width="200" height="140" rx="8" fill="#450a0a" stroke="#dc2626" stroke-width="2.5"/>
        <text x="100" y="35" text-anchor="middle" fill="#fecaca" font-weight="800" font-size="13">4. CIRCULAR WAIT</text>
        <text x="100" y="70" text-anchor="middle" fill="#ffffff" font-size="11">P0 waits for P1, P1 waits</text>
        <text x="100" y="90" text-anchor="middle" fill="#ffffff" font-size="11">for P2, Pn waits for P0.</text>
        <text x="100" y="120" text-anchor="middle" fill="#fca5a5" font-weight="700" font-size="10">TRIGGER CONDITION</text>
      </g>
    </svg>
  </div>
  `;
}

function createVirtualMemoryTlbSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">MEMORY ARCHITECTURE</span>
      <span class="svg-title">Virtual Address Translation: TLB Cache Hit & Page Table Resolution</span>
    </div>
    <svg viewBox="0 0 860 260" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- CPU Virtual Address -->
      <g transform="translate(40, 50)">
        <rect width="170" height="70" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
        <text x="85" y="28" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">VIRTUAL ADDRESS</text>
        <text x="45" y="55" text-anchor="middle" fill="#bae6fd" font-weight="700">Page p</text>
        <line x1="85" y1="35" x2="85" y2="70" stroke="#38bdf8"/>
        <text x="125" y="55" text-anchor="middle" fill="#bae6fd">Offset d</text>
      </g>

      <!-- Path to TLB -->
      <line x1="210" y1="85" x2="280" y2="85" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#csArrow)"/>

      <!-- TLB Box -->
      <g transform="translate(290, 40)">
        <rect width="200" height="90" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="100" y="25" text-anchor="middle" fill="#c7d2fe" font-weight="800" font-size="12">TRANSLATION LOOKASIDE BUFFER</text>
        <text x="100" y="50" text-anchor="middle" fill="#a5b4fc" font-size="11">Fast Associative Hardware</text>
        <text x="100" y="75" text-anchor="middle" fill="#34d399" font-weight="700" font-size="11">TLB HIT (~1-2 ns) → Frame f</text>
      </g>

      <!-- TLB Miss Path to Page Table -->
      <path d="M 390 130 L 390 180 L 490 180" fill="none" stroke="#f87171" stroke-width="2" marker-end="url(#csArrow)"/>
      <text x="430" y="170" fill="#fca5a5" font-size="10">TLB MISS</text>

      <!-- Page Table in RAM -->
      <g transform="translate(500, 140)">
        <rect width="160" height="80" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="80" y="30" text-anchor="middle" fill="#fde68a" font-weight="700" font-size="12">PAGE TABLE (RAM)</text>
        <text x="80" y="55" text-anchor="middle" fill="#e2e8f0" font-size="11">Look up Frame f</text>
      </g>

      <!-- Physical Address -->
      <g transform="translate(640, 50)">
        <rect width="180" height="70" rx="8" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="28" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">PHYSICAL ADDRESS</text>
        <text x="50" y="55" text-anchor="middle" fill="#a7f3d0" font-weight="700">Frame f</text>
        <line x1="90" y1="35" x2="90" y2="70" stroke="#34d399"/>
        <text x="135" y="55" text-anchor="middle" fill="#a7f3d0">Offset d</text>
      </g>

      <!-- Connection from TLB Hit directly to Physical RAM -->
      <line x1="490" y1="85" x2="630" y2="85" stroke="#34d399" stroke-width="2.5" marker-end="url(#csArrow)"/>
    </svg>
  </div>
  `;
}

function createDbms3TierSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">DATABASE MANAGEMENT</span>
      <span class="svg-title">ANSI-SPARC 3-Tier Database Architecture & Data Independence</span>
    </div>
    <svg viewBox="0 0 860 250" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- External / View Level -->
      <g transform="translate(40, 30)">
        <rect width="210" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="105" y="28" text-anchor="middle" fill="#38bdf8" font-weight="800" font-size="13">EXTERNAL LEVEL</text>
        <text x="105" y="48" text-anchor="middle" fill="#94a3b8" font-size="11">User View 1, View 2, View 3</text>
      </g>

      <line x1="145" y1="90" x2="145" y2="120" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="210" y="110" fill="#facc15" font-size="10" font-weight="600">Logical Data Independence</text>

      <!-- Conceptual / Logical Level -->
      <g transform="translate(40, 120)">
        <rect width="210" height="60" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="105" y="28" text-anchor="middle" fill="#c084fc" font-weight="800" font-size="13">CONCEPTUAL LEVEL</text>
        <text x="105" y="48" text-anchor="middle" fill="#e9d5ff" font-size="11">Entities, Relationships, Rules</text>
      </g>

      <line x1="145" y1="180" x2="145" y2="210" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="210" y="200" fill="#facc15" font-size="10" font-weight="600">Physical Data Independence</text>

      <!-- Internal / Physical Level -->
      <g transform="translate(40, 210)">
        <rect width="210" height="36" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
        <text x="105" y="23" text-anchor="middle" fill="#94a3b8" font-weight="700" font-size="12">INTERNAL / STORAGE LEVEL</text>
      </g>

      <!-- Explanation Panel -->
      <g transform="translate(420, 40)">
        <rect width="390" height="170" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="20" y="35" fill="#38bdf8" font-weight="800" font-size="13">WHY 3-TIER ARCHITECTURE MATTERS:</text>
        <text x="20" y="65" fill="#f8fafc" font-size="12">• Logical Data Independence:</text>
        <text x="35" y="85" fill="#94a3b8" font-size="11">Altering conceptual tables without breaking application views.</text>
        <text x="20" y="115" fill="#f8fafc" font-size="12">• Physical Data Independence:</text>
        <text x="35" y="135" fill="#94a3b8" font-size="11">Changing indexes or SSD storage without altering SQL queries.</text>
      </g>
    </svg>
  </div>
  `;
}

function createNormalizationSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">DATABASE NORMALIZATION</span>
      <span class="svg-title">Progressive Normal Forms (1NF → 2NF → 3NF → BCNF)</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 1NF -->
      <g transform="translate(40, 40)">
        <rect width="170" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="85" y="32" text-anchor="middle" fill="#38bdf8" font-weight="800" font-size="14">1NF</text>
        <text x="85" y="60" text-anchor="middle" fill="#e2e8f0" font-size="12">Atomic Attributes</text>
        <text x="85" y="85" text-anchor="middle" fill="#94a3b8" font-size="10">No repeating groups</text>
        <text x="85" y="105" text-anchor="middle" fill="#fde68a" font-size="10">Unique row identity</text>
      </g>

      <line x1="210" y1="100" x2="250" y2="100" stroke="#38bdf8" stroke-width="3" marker-end="url(#csArrow)"/>

      <!-- 2NF -->
      <g transform="translate(255, 40)">
        <rect width="170" height="120" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <text x="85" y="32" text-anchor="middle" fill="#c084fc" font-weight="800" font-size="14">2NF</text>
        <text x="85" y="60" text-anchor="middle" fill="#e2e8f0" font-size="12">No Partial Dependency</text>
        <text x="85" y="85" text-anchor="middle" fill="#94a3b8" font-size="10">Every non-key attr</text>
        <text x="85" y="105" text-anchor="middle" fill="#fde68a" font-size="10">depends on WHOLE PK</text>
      </g>

      <line x1="425" y1="100" x2="465" y2="100" stroke="#38bdf8" stroke-width="3" marker-end="url(#csArrow)"/>

      <!-- 3NF -->
      <g transform="translate(470, 40)">
        <rect width="170" height="120" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <text x="85" y="32" text-anchor="middle" fill="#34d399" font-weight="800" font-size="14">3NF</text>
        <text x="85" y="60" text-anchor="middle" fill="#e2e8f0" font-size="12">No Transitive Dep.</text>
        <text x="85" y="85" text-anchor="middle" fill="#94a3b8" font-size="10">X → Y: X is superkey</text>
        <text x="85" y="105" text-anchor="middle" fill="#a7f3d0" font-size="10">OR Y is prime attribute</text>
      </g>

      <line x1="640" y1="100" x2="675" y2="100" stroke="#38bdf8" stroke-width="3" marker-end="url(#csArrow)"/>

      <!-- BCNF -->
      <g transform="translate(680, 40)">
        <rect width="145" height="120" rx="8" fill="#312e81" stroke="#818cf8" stroke-width="2.5"/>
        <text x="72" y="32" text-anchor="middle" fill="#c7d2fe" font-weight="800" font-size="14">BCNF</text>
        <text x="72" y="60" text-anchor="middle" fill="#fff" font-size="11">Strict Boyce-Codd</text>
        <text x="72" y="85" text-anchor="middle" fill="#e0e7ff" font-size="10">If X → Y,</text>
        <text x="72" y="105" text-anchor="middle" fill="#fde68a" font-weight="700" font-size="10">X MUST be Superkey</text>
      </g>
    </svg>
  </div>
  `;
}

function createAcidPropertiesSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">TRANSACTIONS</span>
      <span class="svg-title">ACID Properties: Transaction Guarantee Pillars</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 40)">
        <rect width="180" height="130" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">ATOMICITY</text>
        <text x="90" y="65" text-anchor="middle" fill="#e0f2fe" font-size="12">All or Nothing</text>
        <text x="90" y="90" text-anchor="middle" fill="#bae6fd" font-size="10">Write-Ahead Log (WAL)</text>
        <text x="90" y="110" text-anchor="middle" fill="#bae6fd" font-size="10">Rollback on Crash</text>
      </g>

      <g transform="translate(240, 40)">
        <rect width="180" height="130" rx="8" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">CONSISTENCY</text>
        <text x="90" y="65" text-anchor="middle" fill="#ecfdf5" font-size="12">Valid State Transitions</text>
        <text x="90" y="90" text-anchor="middle" fill="#bbf7d0" font-size="10">Foreign Key & Check</text>
        <text x="90" y="110" text-anchor="middle" fill="#bbf7d0" font-size="10">Constraint Enforced</text>
      </g>

      <g transform="translate(440, 40)">
        <rect width="180" height="130" rx="8" fill="#6d28d9" stroke="#c084fc" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">ISOLATION</text>
        <text x="90" y="65" text-anchor="middle" fill="#faf5ff" font-size="12">Concurrent Safety</text>
        <text x="90" y="90" text-anchor="middle" fill="#e9d5ff" font-size="10">2PL & MVCC Snapshots</text>
        <text x="90" y="110" text-anchor="middle" fill="#e9d5ff" font-size="10">Prevents Dirty Reads</text>
      </g>

      <g transform="translate(640, 40)">
        <rect width="180" height="130" rx="8" fill="#b45309" stroke="#fcd34d" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">DURABILITY</text>
        <text x="90" y="65" text-anchor="middle" fill="#fef3c7" font-size="12">Committed = Permanent</text>
        <text x="90" y="90" text-anchor="middle" fill="#fde68a" font-size="10">Non-volatile Disk Flush</text>
        <text x="90" y="110" text-anchor="middle" fill="#fde68a" font-size="10">fsync() / Redo Logs</text>
      </g>
    </svg>
  </div>
  `;
}

function createTwoPhaseLockingSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CONCURRENCY CONTROL</span>
      <span class="svg-title">Two-Phase Locking (2PL) Protocol: Growing vs Shrinking Phase</span>
    </div>
    <svg viewBox="0 0 860 230" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <line x1="80" y1="180" x2="780" y2="180" stroke="#64748b" stroke-width="2"/>
      <text x="795" y="185" fill="#94a3b8" font-size="11">Time →</text>

      <!-- Curve -->
      <path d="M 100 180 L 380 40 L 700 180" fill="none" stroke="#38bdf8" stroke-width="3.5"/>

      <!-- Lock Point -->
      <circle cx="380" cy="40" r="7" fill="#ef4444"/>
      <text x="380" y="25" text-anchor="middle" fill="#f87171" font-weight="800" font-size="13">LOCK POINT (Max Locks Held)</text>

      <!-- Growing Phase -->
      <text x="220" y="120" text-anchor="middle" fill="#38bdf8" font-weight="700" font-size="13">GROWING PHASE</text>
      <text x="220" y="140" text-anchor="middle" fill="#94a3b8" font-size="11">Locks Acquired. No Locks Released.</text>

      <!-- Shrinking Phase -->
      <text x="560" y="120" text-anchor="middle" fill="#a855f7" font-weight="700" font-size="13">SHRINKING PHASE</text>
      <text x="560" y="140" text-anchor="middle" fill="#94a3b8" font-size="11">Locks Released. No Locks Acquired.</text>
    </svg>
  </div>
  `;
}

function createBPlusTreeIndexSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">DATABASE INDEXING</span>
      <span class="svg-title">B+ Tree Index Architecture (Internal Routing & Linked Leaves)</span>
    </div>
    <svg viewBox="0 0 860 240" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Root Node -->
      <g transform="translate(340, 30)">
        <rect width="180" height="40" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="90" y="25" text-anchor="middle" fill="#c7d2fe" font-weight="800" font-size="13">[ Root: 50 | 100 ]</text>
      </g>

      <!-- Pointers down to leaves -->
      <line x1="380" y1="70" x2="200" y2="120" stroke="#38bdf8" stroke-width="2" marker-end="url(#csArrow)"/>
      <line x1="430" y1="70" x2="430" y2="120" stroke="#38bdf8" stroke-width="2" marker-end="url(#csArrow)"/>
      <line x1="480" y1="70" x2="660" y2="120" stroke="#38bdf8" stroke-width="2" marker-end="url(#csArrow)"/>

      <!-- Leaf 1 -->
      <g transform="translate(100, 120)">
        <rect width="180" height="50" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="30" text-anchor="middle" fill="#a7f3d0" font-weight="700" font-size="12">[ 10 | 25 | 40 ] →</text>
      </g>

      <!-- Linked pointer between leaves -->
      <line x1="280" y1="145" x2="340" y2="145" stroke="#facc15" stroke-width="2.5" stroke-dasharray="4,3" marker-end="url(#csArrowAmber)"/>

      <!-- Leaf 2 -->
      <g transform="translate(340, 120)">
        <rect width="180" height="50" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="30" text-anchor="middle" fill="#a7f3d0" font-weight="700" font-size="12">[ 50 | 65 | 80 ] →</text>
      </g>

      <line x1="520" y1="145" x2="580" y2="145" stroke="#facc15" stroke-width="2.5" stroke-dasharray="4,3" marker-end="url(#csArrowAmber)"/>

      <!-- Leaf 3 -->
      <g transform="translate(580, 120)">
        <rect width="180" height="50" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="30" text-anchor="middle" fill="#a7f3d0" font-weight="700" font-size="12">[ 100 | 120 | 150 ]</text>
      </g>

      <text x="430" y="210" text-anchor="middle" fill="#fde68a" font-size="12" font-weight="600">⚡ Leaves contain actual data pointers + doubly linked list for O(log N + K) range queries.</text>
    </svg>
  </div>
  `;
}

function createTcpHandshakeSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">COMPUTER NETWORKS</span>
      <span class="svg-title">TCP 3-Way Handshake Connection Establishment</span>
    </div>
    <svg viewBox="0 0 860 250" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Client -->
      <g transform="translate(100, 20)">
        <rect width="160" height="40" rx="6" fill="#0284c7"/>
        <text x="80" y="25" text-anchor="middle" fill="#fff" font-weight="800">CLIENT (Host A)</text>
      </g>
      <line x1="180" y1="60" x2="180" y2="230" stroke="#0284c7" stroke-width="2" stroke-dasharray="5,5"/>

      <!-- Server -->
      <g transform="translate(600, 20)">
        <rect width="160" height="40" rx="6" fill="#15803d"/>
        <text x="80" y="25" text-anchor="middle" fill="#fff" font-weight="800">SERVER (Host B)</text>
      </g>
      <line x1="680" y1="60" x2="680" y2="230" stroke="#15803d" stroke-width="2" stroke-dasharray="5,5"/>

      <!-- Step 1: SYN -->
      <line x1="180" y1="90" x2="680" y2="120" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#csArrow)"/>
      <rect x="360" y="85" width="160" height="26" rx="4" fill="#0f172a" stroke="#38bdf8"/>
      <text x="440" y="102" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="700">1. SYN (seq = x)</text>

      <!-- Step 2: SYN-ACK -->
      <line x1="680" y1="135" x2="180" y2="165" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#csArrow)"/>
      <rect x="330" y="132" width="220" height="26" rx="4" fill="#0f172a" stroke="#f59e0b"/>
      <text x="440" y="149" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="700">2. SYN-ACK (seq = y, ack = x+1)</text>

      <!-- Step 3: ACK -->
      <line x1="180" y1="180" x2="680" y2="210" stroke="#34d399" stroke-width="2.5" marker-end="url(#csArrow)"/>
      <rect x="350" y="180" width="180" height="26" rx="4" fill="#0f172a" stroke="#34d399"/>
      <text x="440" y="197" text-anchor="middle" fill="#a7f3d0" font-size="11" font-weight="700">3. ACK (ack = y+1, ESTABLISHED)</text>
    </svg>
  </div>
  `;
}

function createTcpCongestionControlSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">TRANSPORT LAYER</span>
      <span class="svg-title">TCP Congestion Window Dynamics (Slow Start, Congestion Avoidance, Fast Recovery)</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <line x1="60" y1="180" x2="800" y2="180" stroke="#64748b" stroke-width="2"/>
      <text x="815" y="185" fill="#94a3b8" font-size="11">RTT →</text>
      <line x1="60" y1="180" x2="60" y2="30" stroke="#64748b" stroke-width="2"/>
      <text x="50" y="20" fill="#94a3b8" font-size="11">cwnd</text>

      <!-- Slow start exponential -->
      <path d="M 60 180 Q 200 170, 280 80" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="160" y="130" fill="#38bdf8" font-weight="700" font-size="11">Slow Start (2^n)</text>

      <!-- ssthresh line -->
      <line x1="60" y1="80" x2="800" y2="80" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6,4"/>
      <text x="730" y="72" fill="#fde68a" font-size="10">ssthresh threshold</text>

      <!-- Linear additive increase -->
      <line x1="280" y1="80" x2="480" y2="40" stroke="#34d399" stroke-width="3"/>
      <text x="360" y="50" fill="#a7f3d0" font-weight="700" font-size="11">Congestion Avoidance (+1 cwnd)</text>

      <!-- Packet Loss & Drop -->
      <line x1="480" y1="40" x2="480" y2="110" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,3"/>
      <circle cx="480" cy="40" r="5" fill="#ef4444"/>
      <text x="495" y="45" fill="#f87171" font-size="10" font-weight="700">Packet Loss</text>

      <!-- Multiplicative decrease & recovery -->
      <line x1="480" y1="110" x2="700" y2="60" stroke="#a855f7" stroke-width="3"/>
      <text x="580" y="100" fill="#c084fc" font-size="11" font-weight="700">Fast Recovery (AIMD)</text>
    </svg>
  </div>
  `;
}

function createCrcFramingSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">DATA LINK LAYER</span>
      <span class="svg-title">Cyclic Redundancy Check (CRC) Polynomial Division & Framing</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Data Frame -->
      <g transform="translate(60, 40)">
        <rect width="320" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="160" y="28" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">RAW DATA BITS (D)</text>
        <text x="160" y="48" text-anchor="middle" fill="#38bdf8" font-family="monospace" font-size="14">1 1 0 1 0 0 1 1</text>
      </g>

      <!-- CRC Checksum appended -->
      <g transform="translate(390, 40)">
        <rect width="180" height="60" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="90" y="28" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">CRC CODE (R)</text>
        <text x="90" y="48" text-anchor="middle" fill="#c084fc" font-family="monospace" font-size="14">1 0 1 1</text>
      </g>

      <line x1="300" y1="115" x2="300" y2="150" stroke="#38bdf8" stroke-width="2" marker-end="url(#csArrow)"/>

      <g transform="translate(60, 150)">
        <rect width="740" height="44" rx="8" fill="#0f172a" stroke="#64748b"/>
        <text x="370" y="27" text-anchor="middle" fill="#a7f3d0" font-size="12">Transmitted Payload: [ Data Bits (D) + CRC Remainder (R) ] mod Generator G(x) == 0</text>
      </g>
    </svg>
  </div>
  `;
}

function createPythonGilSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">PYTHON RUNTIME INTERNALS</span>
      <span class="svg-title">Global Interpreter Lock (GIL) Execution Contention</span>
    </div>
    <svg viewBox="0 0 860 230" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 2 Threads contending for 1 GIL -->
      <g transform="translate(50, 40)">
        <rect width="180" height="50" rx="8" fill="#0284c7"/>
        <text x="90" y="30" text-anchor="middle" fill="#fff" font-weight="700">THREAD 1 (Bytecode)</text>
      </g>

      <g transform="translate(50, 110)">
        <rect width="180" height="50" rx="8" fill="#475569"/>
        <text x="90" y="30" text-anchor="middle" fill="#cbd5e1" font-weight="700">THREAD 2 (Waiting)</text>
      </g>

      <line x1="230" y1="65" x2="350" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#csArrow)"/>
      <line x1="230" y1="135" x2="350" y2="100" stroke="#f87171" stroke-width="2" stroke-dasharray="4,4"/>

      <!-- GIL Mutex Center -->
      <g transform="translate(360, 55)">
        <rect width="170" height="90" rx="10" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <text x="85" y="35" text-anchor="middle" fill="#fecaca" font-weight="800" font-size="14">CPYTHON GIL</text>
        <text x="85" y="60" text-anchor="middle" fill="#ffffff" font-size="11">Mutex Guard</text>
        <text x="85" y="78" text-anchor="middle" fill="#fca5a5" font-size="10">1 Thread at a time</text>
      </g>

      <!-- CPU Core execution -->
      <line x1="530" y1="100" x2="630" y2="100" stroke="#34d399" stroke-width="3" marker-end="url(#csArrow)"/>

      <g transform="translate(640, 55)">
        <rect width="180" height="90" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800" font-size="13">SINGLE CPU CORE</text>
        <text x="90" y="60" text-anchor="middle" fill="#e2e8f0" font-size="11">Executes PyEval_EvalFrame</text>
      </g>

      <text x="430" y="195" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="600">⚡ Remedy for CPU bottlenecks: Use multiprocessing or native C-extensions. AsyncIO for I/O bounds.</text>
    </svg>
  </div>
  `;
}

function createSystemDesignOverviewSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">SYSTEM DESIGN</span>
      <span class="svg-title">High-Availability Scalable Web Tier & Distributed Data Layer</span>
    </div>
    <svg viewBox="0 0 860 240" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Clients -->
      <g transform="translate(30, 80)">
        <rect width="100" height="60" rx="8" fill="#0284c7"/>
        <text x="50" y="35" text-anchor="middle" fill="#fff" font-weight="700" font-size="12">Clients</text>
      </g>

      <line x1="130" y1="110" x2="180" y2="110" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#csArrow)"/>

      <!-- Load Balancer -->
      <g transform="translate(190, 60)">
        <rect width="130" height="100" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="65" y="45" text-anchor="middle" fill="#c7d2fe" font-weight="800" font-size="12">LOAD BALANCER</text>
        <text x="65" y="70" text-anchor="middle" fill="#a5b4fc" font-size="10">NGINX / HAProxy</text>
      </g>

      <!-- Web Nodes -->
      <line x1="320" y1="90" x2="380" y2="60" stroke="#38bdf8" stroke-width="2" marker-end="url(#csArrow)"/>
      <line x1="320" y1="130" x2="380" y2="160" stroke="#38bdf8" stroke-width="2" marker-end="url(#csArrow)"/>

      <g transform="translate(390, 30)">
        <rect width="130" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
        <text x="65" y="30" text-anchor="middle" fill="#fff" font-size="12">API Server 1</text>
      </g>
      <g transform="translate(390, 140)">
        <rect width="130" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
        <text x="65" y="30" text-anchor="middle" fill="#fff" font-size="12">API Server 2</text>
      </g>

      <!-- Redis Cache -->
      <g transform="translate(560, 20)">
        <rect width="130" height="60" rx="8" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <text x="65" y="35" text-anchor="middle" fill="#fecaca" font-weight="800" font-size="12">REDIS CACHE</text>
      </g>

      <!-- Database Cluster -->
      <g transform="translate(560, 130)">
        <rect width="150" height="70" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="75" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800" font-size="12">POSTGRESQL</text>
        <text x="75" y="55" text-anchor="middle" fill="#e2e8f0" font-size="10">Primary + Read Replica</text>
      </g>

      <line x1="520" y1="55" x2="560" y2="55" stroke="#ef4444" stroke-width="2" marker-end="url(#csArrow)"/>
      <line x1="520" y1="165" x2="560" y2="165" stroke="#34d399" stroke-width="2" marker-end="url(#csArrow)"/>
    </svg>
  </div>
  `;
}

function createCoreCsGeneralSvg(topic) {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CORE CS ARCHITECTURE</span>
      <span class="svg-title">${topic || 'Computer Science Architecture Diagram'}</span>
    </div>
    <svg viewBox="0 0 860 160" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <rect x="40" y="30" width="780" height="100" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="430" y="70" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="800">${topic || 'Core CS Foundations'}</text>
      <text x="430" y="100" text-anchor="middle" fill="#94a3b8" font-size="12">Rigorous Asymptotic Rigor • Architectural Determinism • Placement Tested</text>
    </svg>
  </div>
  `;
}
