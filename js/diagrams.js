/**
 * Interactive SVG Diagram Generator for Academic & Placement Visualizations
 * Provides high-contrast, themed, crisp vector diagrams for Herbert Simon's Model,
 * DSS 3-Tier Architecture, JVM, OSI 7-Layer, Bisection Method, Two Pointers, Sliding Window, etc.
 */

import { renderCoreCsSvg } from './diagrams_core.js';
import { renderProjectDefenseSvg } from './diagrams_proj.js';
import { renderAcademicSvg } from './diagrams_acad.js';

export function renderSvgDiagram(diagramType, rawText = '') {
  const typeKey = (diagramType || '').toLowerCase().trim();

  // 1. Check Semester 5 Academic specialized SVG generators (BCA-5001, 5002, 5003, 5004)
  if (typeKey.includes('simon') || rawText.includes('HERBERT SIMON') || rawText.includes('Intelligence Phase') ||
      typeKey.includes('dss') || rawText.includes('3-TIER DSS') || rawText.includes('Data Subsystem') ||
      typeKey.includes('jvm') || rawText.includes('JVM ARCHITECTURE') || rawText.includes('ClassLoader') ||
      typeKey.includes('osi') || rawText.includes('OSI 7-LAYER') || rawText.includes('Transport (Segment)') ||
      typeKey.includes('bisection') || rawText.includes('BISECTION METHOD') || rawText.includes('x_mid') ||
      typeKey.includes('thread') || rawText.includes('THREAD LIFECYCLE') ||
      typeKey.includes('seci') || rawText.includes('SECI SPIRAL') ||
      typeKey.includes('exception') || rawText.includes('EXCEPTION HIERARCHY') ||
      typeKey.includes('newton') || typeKey.includes('regula') || typeKey.includes('gauss') ||
      typeKey.includes('warehouse') || typeKey.includes('ipv4')) {
    return renderAcademicSvg(diagramType, rawText);
  }

  // 2. Detect DSA algorithmic pattern diagrams
  if (typeKey.includes('two_pointer') || rawText.includes('Two Pointers') || rawText.includes('Left -> [2]')) {
    return createTwoPointersSvg(rawText);
  }
  if (typeKey.includes('sliding_window') || rawText.includes('Window 0') || rawText.includes('Sliding Window')) {
    return createSlidingWindowSvg(rawText);
  }
  if (typeKey.includes('fast_slow') || rawText.includes('Cycle Proven') || rawText.includes('Slow =')) {
    return createFastSlowPointerSvg();
  }

  // 3. Check Core CS specialized SVG generators
  if (typeKey.includes('core_cs') || typeKey.includes('os') || typeKey.includes('dbms') || typeKey.includes('process') || typeKey.includes('deadlock') || typeKey.includes('tcp') || typeKey.includes('scheduling') || typeKey.includes('acid') || typeKey.includes('lock') || typeKey.includes('gil') || typeKey.includes('synchronization')) {
    return renderCoreCsSvg(diagramType, rawText);
  }

  // 4. Check Project Defense specialized SVG generators
  if (typeKey.includes('csms') || typeKey.includes('smartgalla') || typeKey.includes('bulkbeat') || typeKey.includes('nse2') || typeKey.includes('bevm') || typeKey.includes('voting') || typeKey.includes('docroute') || typeKey.includes('django')) {
    return renderProjectDefenseSvg(diagramType, rawText);
  }

  // Fallback to stylized vector flowchart if unknown
  return renderAcademicSvg(diagramType, rawText) || createGenericFlowchartSvg(rawText);
}

export { renderCoreCsSvg, renderProjectDefenseSvg, renderAcademicSvg };

/**
 * 1. Herbert Simon's 4-Phase Decision Making Model (Academic Day 1)
 */
function createSimonModelSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">ACADEMIC DIAGRAM</span>
      <span class="svg-title">Herbert Simon's 4-Phase Decision Process (CSJMU BCA-5001)</span>
    </div>
    <svg viewBox="0 0 860 380" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <defs>
        <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0284c7" />
          <stop offset="100%" stop-color="#0369a1" />
        </linearGradient>
        <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#9333ea" />
          <stop offset="100%" stop-color="#7e22ce" />
        </linearGradient>
        <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#059669" />
          <stop offset="100%" stop-color="#047857" />
        </linearGradient>
        <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#d97706" />
          <stop offset="100%" stop-color="#b45309" />
        </linearGradient>
        <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
        </filter>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="arrowPurple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#c084fc" />
        </marker>
      </defs>

      <!-- Phase 1: Intelligence -->
      <g class="svg-node" transform="translate(40, 40)" filter="url(#shadow)">
        <rect width="220" height="70" rx="10" fill="url(#blueGrad)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="110" y="30" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="14">1. INTELLIGENCE</text>
        <text x="110" y="50" text-anchor="middle" fill="#e0f2fe" font-size="11">Problem Identification & Data Scan</text>
      </g>

      <!-- Arrow 1 -> 2 -->
      <line x1="260" y1="75" x2="330" y2="75" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />

      <!-- Phase 2: Design -->
      <g class="svg-node" transform="translate(340, 40)" filter="url(#shadow)">
        <rect width="220" height="70" rx="10" fill="url(#purpleGrad)" stroke="#c084fc" stroke-width="1.5"/>
        <text x="110" y="30" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="14">2. DESIGN PHASE</text>
        <text x="110" y="50" text-anchor="middle" fill="#fae8ff" font-size="11">Formulate & Model Alternatives</text>
      </g>

      <!-- Arrow 2 -> 3 -->
      <line x1="560" y1="75" x2="630" y2="75" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />

      <!-- Phase 3: Choice -->
      <g class="svg-node" transform="translate(640, 40)" filter="url(#shadow)">
        <rect width="180" height="70" rx="10" fill="url(#amberGrad)" stroke="#fcd34d" stroke-width="1.5"/>
        <text x="90" y="30" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="14">3. CHOICE PHASE</text>
        <text x="90" y="50" text-anchor="middle" fill="#fef3c7" font-size="11">Select Best Solution</text>
      </g>

      <!-- Arrow 3 -> 4 (Downwards) -->
      <path d="M 730 110 L 730 190 L 580 190" fill="none" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)" />

      <!-- Phase 4: Implementation -->
      <g class="svg-node" transform="translate(340, 155)" filter="url(#shadow)">
        <rect width="220" height="70" rx="10" fill="url(#emeraldGrad)" stroke="#34d399" stroke-width="1.5"/>
        <text x="110" y="30" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="14">4. IMPLEMENTATION</text>
        <text x="110" y="50" text-anchor="middle" fill="#d1fae5" font-size="11">Deployment & Monitoring</text>
      </g>

      <!-- Feedback Loop to Intelligence -->
      <path d="M 340 190 L 150 190 L 150 120" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrowPurple)" />
      <text x="210" y="215" fill="#c084fc" font-size="12" font-weight="600">Feedback Loop (Evaluation Failure)</text>

      <!-- Feedback Loop from Choice back to Design -->
      <path d="M 730 40 L 730 15 L 450 15 L 450 30" fill="none" stroke="#fcd34d" stroke-width="2" stroke-dasharray="5,4" marker-end="url(#arrow)" />
      <text x="590" y="12" text-anchor="middle" fill="#fcd34d" font-size="11">Refine Design if No Feasible Option</text>

      <!-- Footnote Banner -->
      <rect x="40" y="270" width="780" height="85" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="60" y="295" fill="#38bdf8" font-size="13" font-weight="700">★ EXAM WRITING SCORING KEY (15-Mark University Rubric)</text>
      <text x="60" y="318" fill="#cbd5e1" font-size="12">• Simon originally proposed 3 stages; modern DSS literature added 4th stage: Implementation.</text>
      <text x="60" y="338" fill="#cbd5e1" font-size="12">• Include BOTH feedback loops: Choice -> Design refinement and Implementation -> Intelligence scan.</text>
    </svg>
  </div>
  `;
}

/**
 * 2. 3-Tier DSS Architecture (Academic Day 2)
 */
function createDssArchitectureSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">ARCHITECTURE</span>
      <span class="svg-title">3-Tier Decision Support System (DSS) Framework</span>
    </div>
    <svg viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <defs>
        <marker id="bidir" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 2 L 6 5 L 0 8 z" fill="#38bdf8" />
        </marker>
      </defs>

      <!-- Tier 1: Database Management Subsystem -->
      <g transform="translate(40, 50)">
        <rect width="220" height="150" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="2" />
        <rect x="0" y="0" width="220" height="36" rx="12" fill="#0284c7" />
        <text x="110" y="24" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="13">DATA SUBSYSTEM</text>
        <text x="20" y="65" fill="#93c5fd" font-size="12" font-weight="600">• Internal Transaction Data (TPS)</text>
        <text x="20" y="90" fill="#93c5fd" font-size="12" font-weight="600">• External Industry Feed</text>
        <text x="20" y="115" fill="#93c5fd" font-size="12" font-weight="600">• Data Warehouse & Marts</text>
        <text x="20" y="140" fill="#60a5fa" font-size="11">DBMS Engine & Query Processor</text>
      </g>

      <!-- Connection 1 <-> 2 -->
      <line x1="260" y1="125" x2="330" y2="125" stroke="#38bdf8" stroke-width="3" marker-end="url(#bidir)" marker-start="url(#bidir)" />

      <!-- Tier 2: Model Management Subsystem -->
      <g transform="translate(340, 50)">
        <rect width="230" height="150" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="2" />
        <rect x="0" y="0" width="230" height="36" rx="12" fill="#9333ea" />
        <text x="115" y="24" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="13">MODEL SUBSYSTEM (MBMS)</text>
        <text x="20" y="65" fill="#d8b4fe" font-size="12" font-weight="600">• Quantitative & Forecasting Models</text>
        <text x="20" y="90" fill="#d8b4fe" font-size="12" font-weight="600">• Optimization (Linear/Non-linear)</text>
        <text x="20" y="115" fill="#d8b4fe" font-size="12" font-weight="600">• Sensitivity & 'What-If' Simulators</text>
        <text x="20" y="140" fill="#c084fc" font-size="11">Model Base Management Software</text>
      </g>

      <!-- Connection 2 <-> 3 -->
      <line x1="570" y1="125" x2="640" y2="125" stroke="#38bdf8" stroke-width="3" marker-end="url(#bidir)" marker-start="url(#bidir)" />

      <!-- Tier 3: User Interface & Dialog Subsystem -->
      <g transform="translate(650, 50)">
        <rect width="180" height="150" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2" />
        <rect x="0" y="0" width="180" height="36" rx="12" fill="#059669" />
        <text x="90" y="24" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="13">DIALOG / UI</text>
        <text x="20" y="65" fill="#6ee7b7" font-size="12" font-weight="600">• Executive Dashboards</text>
        <text x="20" y="90" fill="#6ee7b7" font-size="12" font-weight="600">• Natural Query Input</text>
        <text x="20" y="115" fill="#6ee7b7" font-size="12" font-weight="600">• Graphical Drilldown</text>
        <text x="20" y="140" fill="#34d399" font-size="11">Decision Maker Interface</text>
      </g>

      <!-- Footer Note -->
      <rect x="40" y="225" width="790" height="50" rx="6" fill="#1e293b" />
      <text x="435" y="255" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="600">
        Key Architectural Benefit: Decoupling of mathematical decision models from raw corporate transactional storage.
      </text>
    </svg>
  </div>
  `;
}

/**
 * 3. JVM Runtime Architecture (Academic Day 3)
 */
function createJvmArchitectureSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CORE CS / JAVA</span>
      <span class="svg-title">Java Virtual Machine (JVM) Internal Architecture</span>
    </div>
    <svg viewBox="0 0 860 360" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Outer Box -->
      <rect x="20" y="20" width="820" height="320" rx="16" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <text x="50" y="50" fill="#38bdf8" font-size="16" font-weight="800">JVM RUNTIME SUBSYSTEMS</text>

      <!-- 1. ClassLoader -->
      <g transform="translate(40, 70)">
        <rect width="180" height="240" rx="10" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5"/>
        <rect x="0" y="0" width="180" height="34" rx="10" fill="#0284c7"/>
        <text x="90" y="22" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">1. CLASSLOADER</text>
        <text x="20" y="65" fill="#e2e8f0" font-size="12" font-weight="600">• Loading</text>
        <text x="35" y="85" fill="#94a3b8" font-size="10">Bootstrap / Ext / App</text>
        <text x="20" y="115" fill="#e2e8f0" font-size="12" font-weight="600">• Linking</text>
        <text x="35" y="135" fill="#94a3b8" font-size="10">Verify, Prepare, Resolve</text>
        <text x="20" y="165" fill="#e2e8f0" font-size="12" font-weight="600">• Initialization</text>
        <text x="35" y="185" fill="#94a3b8" font-size="10">Static blocks & vars</text>
      </g>

      <!-- 2. Runtime Data Areas -->
      <g transform="translate(240, 70)">
        <rect width="360" height="240" rx="10" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
        <rect x="0" y="0" width="360" height="34" rx="10" fill="#9333ea"/>
        <text x="180" y="22" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">2. RUNTIME DATA AREAS</text>
        
        <!-- Heap -->
        <rect x="20" y="50" width="150" height="75" rx="6" fill="#3b0764" stroke="#a855f7"/>
        <text x="95" y="75" text-anchor="middle" fill="#f3e8ff" font-size="11" font-weight="700">HEAP AREA</text>
        <text x="95" y="95" text-anchor="middle" fill="#d8b4fe" font-size="10">Objects & Instances (Shared)</text>

        <!-- Method Area -->
        <rect x="190" y="50" width="150" height="75" rx="6" fill="#3b0764" stroke="#a855f7"/>
        <text x="265" y="75" text-anchor="middle" fill="#f3e8ff" font-size="11" font-weight="700">METHOD AREA</text>
        <text x="265" y="95" text-anchor="middle" fill="#d8b4fe" font-size="10">Bytecode & Static Vars</text>

        <!-- JVM Stack -->
        <rect x="20" y="140" width="100" height="80" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
        <text x="70" y="165" text-anchor="middle" fill="#e0e7ff" font-size="11" font-weight="700">JVM STACK</text>
        <text x="70" y="185" text-anchor="middle" fill="#a5b4fc" font-size="9">Frames & Locals</text>

        <!-- Program Counter -->
        <rect x="130" y="140" width="100" height="80" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
        <text x="180" y="165" text-anchor="middle" fill="#e0e7ff" font-size="11" font-weight="700">PC REGISTER</text>
        <text x="180" y="185" text-anchor="middle" fill="#a5b4fc" font-size="9">Current Opcode</text>

        <!-- Native Stack -->
        <rect x="240" y="140" width="100" height="80" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
        <text x="290" y="165" text-anchor="middle" fill="#e0e7ff" font-size="11" font-weight="700">NATIVE STACK</text>
        <text x="290" y="185" text-anchor="middle" fill="#a5b4fc" font-size="9">C/C++ Methods</text>
      </g>

      <!-- 3. Execution Engine -->
      <g transform="translate(620, 70)">
        <rect width="190" height="240" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
        <rect x="0" y="0" width="190" height="34" rx="10" fill="#059669"/>
        <text x="95" y="22" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">3. EXECUTION ENGINE</text>
        
        <rect x="15" y="50" width="160" height="40" rx="4" fill="#064e3b" stroke="#10b981"/>
        <text x="95" y="75" text-anchor="middle" fill="#d1fae5" font-size="11" font-weight="600">Interpreter</text>

        <rect x="15" y="100" width="160" height="50" rx="4" fill="#064e3b" stroke="#10b981"/>
        <text x="95" y="122" text-anchor="middle" fill="#d1fae5" font-size="11" font-weight="600">JIT Compiler</text>
        <text x="95" y="138" text-anchor="middle" fill="#6ee7b7" font-size="9">(HotSpot Native Code)</text>

        <rect x="15" y="160" width="160" height="50" rx="4" fill="#064e3b" stroke="#10b981"/>
        <text x="95" y="182" text-anchor="middle" fill="#d1fae5" font-size="11" font-weight="600">Garbage Collector (GC)</text>
        <text x="95" y="198" text-anchor="middle" fill="#6ee7b7" font-size="9">Generational Sweep</text>
      </g>
    </svg>
  </div>
  `;
}

/**
 * 4. OSI 7-Layer Protocol Model (Academic Day 4)
 */
function createOsiModelSvg() {
  const layers = [
    { num: 7, name: 'Application', pdu: 'User Data', color: '#ec4899', desc: 'HTTP, DNS, SMTP, FTP' },
    { num: 6, name: 'Presentation', pdu: 'Formatted Data', color: '#d946ef', desc: 'Encryption (TLS/SSL), Compression' },
    { num: 5, name: 'Session', pdu: 'Dialog Data', color: '#a855f7', desc: 'Session tokens, Sockets sync' },
    { num: 4, name: 'Transport', pdu: 'Segments / Datagrams', color: '#3b82f6', desc: 'TCP (reliable, flow control) / UDP' },
    { num: 3, name: 'Network', pdu: 'Packets', color: '#0ea5e9', desc: 'IP routing, Routers, ICMP' },
    { num: 2, name: 'Data Link', pdu: 'Frames', color: '#10b981', desc: 'MAC address, Ethernet switch, LLC' },
    { num: 1, name: 'Physical', pdu: 'Bits (0s & 1s)', color: '#f59e0b', desc: 'Cables, RF signals, Hubs, Voltages' }
  ];

  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">NETWORKING MODEL</span>
      <span class="svg-title">OSI 7-Layer Reference Model & Data Units</span>
    </div>
    <svg viewBox="0 0 860 380" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      ${layers.map((l, i) => {
        const y = 30 + i * 46;
        return `
          <g class="svg-row" transform="translate(30, ${y})">
            <rect width="60" height="38" rx="6" fill="${l.color}" />
            <text x="30" y="24" text-anchor="middle" fill="#ffffff" font-weight="800" font-size="14">L${l.num}</text>
            
            <rect x="70" y="0" width="220" height="38" rx="6" fill="#1e293b" stroke="${l.color}" stroke-width="1.5" />
            <text x="85" y="24" fill="#ffffff" font-weight="700" font-size="13">${l.name} Layer</text>

            <rect x="300" y="0" width="240" height="38" rx="6" fill="#0f172a" stroke="#334155" />
            <text x="315" y="24" fill="#38bdf8" font-size="12" font-weight="600">PDU: ${l.pdu}</text>

            <rect x="550" y="0" width="250" height="38" rx="6" fill="#1e293b" />
            <text x="565" y="24" fill="#cbd5e1" font-size="12">${l.desc}</text>
          </g>
        `;
      }).join('')}
    </svg>
  </div>
  `;
}

/**
 * 5. Bisection Numerical Method (Academic Day 5)
 */
function createBisectionMethodSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">NUMERICAL COMPUTING</span>
      <span class="svg-title">Bisection Root Finding Method (Bolzano Intermediate Value Theorem)</span>
    </div>
    <svg viewBox="0 0 860 280" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Axis -->
      <line x1="60" y1="140" x2="800" y2="140" stroke="#64748b" stroke-width="2" />
      <text x="815" y="145" fill="#94a3b8" font-size="12">x-axis</text>

      <!-- Continuous Curve crossing zero -->
      <path d="M 80 230 C 250 210, 380 180, 480 140 C 580 100, 700 50, 780 40" fill="none" stroke="#38bdf8" stroke-width="3" />

      <!-- Point a (f(a) < 0) -->
      <circle cx="160" cy="140" r="6" fill="#ef4444" />
      <circle cx="160" cy="218" r="5" fill="#ef4444" />
      <line x1="160" y1="140" x2="160" y2="218" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="160" y="125" text-anchor="middle" fill="#ef4444" font-weight="700" font-size="13">a</text>
      <text x="160" y="245" text-anchor="middle" fill="#fca5a5" font-size="11">f(a) &lt; 0</text>

      <!-- Point b (f(b) > 0) -->
      <circle cx="700" cy="140" r="6" fill="#10b981" />
      <circle cx="700" cy="55" r="5" fill="#10b981" />
      <line x1="700" y1="140" x2="700" y2="55" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="700" y="165" text-anchor="middle" fill="#10b981" font-weight="700" font-size="13">b</text>
      <text x="700" y="45" text-anchor="middle" fill="#6ee7b7" font-size="11">f(b) &gt; 0</text>

      <!-- Midpoint x_mid = (a+b)/2 -->
      <circle cx="430" cy="140" r="7" fill="#f59e0b" />
      <circle cx="430" cy="155" r="5" fill="#f59e0b" />
      <text x="430" y="125" text-anchor="middle" fill="#f59e0b" font-weight="800" font-size="13">x_mid = (a+b)/2</text>
      <text x="430" y="180" text-anchor="middle" fill="#fde68a" font-size="11">Evaluate f(x_mid)</text>

      <!-- True Root alpha -->
      <circle cx="480" cy="140" r="5" fill="#a855f7" />
      <text x="485" y="165" fill="#d8b4fe" font-weight="700" font-size="12">Root α [f(α)=0]</text>

      <!-- Formula Pill -->
      <rect x="60" y="20" width="340" height="40" rx="8" fill="#1e293b" stroke="#334155" />
      <text x="230" y="45" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="600">Interval Halving: Error ≤ (b - a) / 2ⁿ</text>
    </svg>
  </div>
  `;
}

/**
 * 6. Two Pointers Algorithm Visualization (DSA)
 */
function createTwoPointersSvg(rawText = '') {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">ALGORITHM DRY-RUN</span>
      <span class="svg-title">Two Pointers — Inward Scan Execution State</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Array Elements: [2, 7, 11, 15] -->
      <g transform="translate(140, 50)">
        <!-- Box 0 -->
        <rect x="0" y="0" width="110" height="70" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
        <text x="55" y="42" text-anchor="middle" fill="#38bdf8" font-size="22" font-weight="800">2</text>
        <text x="55" y="-10" text-anchor="middle" fill="#94a3b8" font-size="12">idx [0]</text>
        
        <!-- Left Pointer Indicator -->
        <path d="M 55 110 L 55 80" stroke="#10b981" stroke-width="3" marker-end="url(#arrow)"/>
        <rect x="15" y="115" width="80" height="30" rx="6" fill="#064e3b" stroke="#10b981"/>
        <text x="55" y="135" text-anchor="middle" fill="#a7f3d0" font-weight="700" font-size="12">LEFT (i=0)</text>

        <!-- Box 1 -->
        <rect x="130" y="0" width="110" height="70" rx="8" fill="#1e293b" stroke="#334155" stroke-width="2"/>
        <text x="185" y="42" text-anchor="middle" fill="#f8fafc" font-size="22" font-weight="800">7</text>
        <text x="185" y="-10" text-anchor="middle" fill="#94a3b8" font-size="12">idx [1]</text>

        <!-- Box 2 -->
        <rect x="260" y="0" width="110" height="70" rx="8" fill="#1e293b" stroke="#334155" stroke-width="2"/>
        <text x="315" y="42" text-anchor="middle" fill="#f8fafc" font-size="22" font-weight="800">11</text>
        <text x="315" y="-10" text-anchor="middle" fill="#94a3b8" font-size="12">idx [2]</text>

        <!-- Box 3 -->
        <rect x="390" y="0" width="110" height="70" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
        <text x="445" y="42" text-anchor="middle" fill="#f87171" font-size="22" font-weight="800">15</text>
        <text x="445" y="-10" text-anchor="middle" fill="#94a3b8" font-size="12">idx [3]</text>

        <!-- Right Pointer Indicator -->
        <path d="M 445 110 L 445 80" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow)"/>
        <rect x="400" y="115" width="90" height="30" rx="6" fill="#450a0a" stroke="#ef4444"/>
        <text x="445" y="135" text-anchor="middle" fill="#fecaca" font-weight="700" font-size="12">RIGHT (j=3)</text>
      </g>

      <!-- Target Math Evaluation Card -->
      <g transform="translate(680, 40)">
        <rect width="150" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="75" y="30" text-anchor="middle" fill="#94a3b8" font-size="11">TARGET = 9</text>
        <text x="75" y="60" text-anchor="middle" fill="#f87171" font-weight="700" font-size="14">2 + 15 = 17 &gt; 9</text>
        <text x="75" y="90" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="600">Action: Right--</text>
      </g>
    </svg>
  </div>
  `;
}

/**
 * 7. Sliding Window Algorithm Visualization
 */
function createSlidingWindowSvg(rawText = '') {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">ALGORITHM DRY-RUN</span>
      <span class="svg-title">Fixed Sliding Window (K=3 Max Sum Subarray)</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(80, 50)">
        <!-- Array cells -->
        <rect x="0" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="40" y="37" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">2</text>

        <rect x="90" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="130" y="37" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">1</text>

        <rect x="180" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="220" y="37" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">5</text>

        <rect x="270" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="310" y="37" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">1</text>

        <rect x="360" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="400" y="37" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">3</text>

        <rect x="450" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="490" y="37" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">2</text>

        <!-- Active Window Bracket (Window 2: elements 5, 1, 3 -> Sum = 9) -->
        <rect x="175" y="-8" width="270" height="76" rx="10" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="6,4" />
        <rect x="235" y="80" width="150" height="30" rx="6" fill="#064e3b" stroke="#10b981"/>
        <text x="310" y="100" text-anchor="middle" fill="#a7f3d0" font-weight="700" font-size="12">Active Window (K=3)</text>
      </g>

      <!-- Math Explanation Box -->
      <g transform="translate(640, 45)">
        <rect width="180" height="100" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <text x="90" y="30" text-anchor="middle" fill="#a7f3d0" font-size="12" font-weight="700">O(1) ROLL SLIDE</text>
        <text x="90" y="55" text-anchor="middle" fill="#e2e8f0" font-size="12">Sum = Prev - L + R</text>
        <text x="90" y="80" text-anchor="middle" fill="#38bdf8" font-weight="800" font-size="14">Max Sum = 9</text>
      </g>
    </svg>
  </div>
  `;
}

/**
 * 8. Fast & Slow Pointer / Floyd's Cycle
 */
function createFastSlowPointerSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">ALGORITHM DRY-RUN</span>
      <span class="svg-title">Floyd's Tortoise and Hare Cycle Detection</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Linked list nodes -->
      <g transform="translate(60, 60)">
        <circle cx="50" cy="50" r="24" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="50" y="56" text-anchor="middle" fill="#fff" font-weight="700">1</text>
        <line x1="74" y1="50" x2="126" y2="50" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

        <circle cx="150" cy="50" r="24" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="150" y="56" text-anchor="middle" fill="#fff" font-weight="700">2</text>
        <line x1="174" y1="50" x2="226" y2="50" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

        <!-- Cycle starts at 3 -->
        <circle cx="250" cy="50" r="24" fill="#1e293b" stroke="#a855f7" stroke-width="2.5"/>
        <text x="250" y="56" text-anchor="middle" fill="#e9d5ff" font-weight="700">3</text>
        <line x1="274" y1="50" x2="326" y2="50" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

        <circle cx="350" cy="50" r="24" fill="#1e293b" stroke="#ef4444" stroke-width="2.5"/>
        <text x="350" y="56" text-anchor="middle" fill="#fca5a5" font-weight="700">4</text>
        <line x1="374" y1="50" x2="426" y2="50" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

        <circle cx="450" cy="50" r="24" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="450" y="56" text-anchor="middle" fill="#fff" font-weight="700">5</text>

        <!-- Loop curve from 5 back to 3 -->
        <path d="M 450 74 C 450 140, 250 140, 250 80" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5,4" marker-end="url(#arrow)" />
        <text x="350" y="150" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="600">Back Edge to Node 3</text>
      </g>

      <!-- Collision Badge -->
      <g transform="translate(620, 50)">
        <rect width="200" height="100" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="100" y="35" text-anchor="middle" fill="#c084fc" font-size="12" font-weight="800">COLLISION AT NODE 4</text>
        <text x="100" y="60" text-anchor="middle" fill="#e0e7ff" font-size="11">Slow (1 step) == Fast (2 step)</text>
        <text x="100" y="82" text-anchor="middle" fill="#34d399" font-size="12" font-weight="700">Loop Confirmed in O(N)</text>
      </g>
    </svg>
  </div>
  `;
}

/**
 * Generic Fallback SVG Vector Flowchart
 */
function createGenericFlowchartSvg(rawText = '') {
  const lines = rawText.split('\n').filter(l => l.trim().length > 0 && !l.includes('---') && !l.includes('+=='));
  const safeLines = lines.slice(0, 6);

  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">SCHEMATIC FLOW</span>
      <span class="svg-title">Structured System Topology</span>
    </div>
    <div class="svg-fallback-container">
      <svg viewBox="0 0 860 ${Math.max(160, safeLines.length * 48 + 40)}" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
        ${safeLines.map((line, idx) => {
          const y = 30 + idx * 46;
          const cleanLine = line.replace(/^[|+-]+/, '').replace(/[|+-]+$/, '').trim();
          return `
            <g transform="translate(60, ${y})">
              <rect width="740" height="36" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2" />
              <text x="20" y="23" fill="#38bdf8" font-weight="700" font-size="12">${idx + 1}.</text>
              <text x="50" y="23" fill="#f8fafc" font-size="13" font-family="var(--font-mono)">${cleanLine}</text>
            </g>
          `;
        }).join('')}
      </svg>
    </div>
  </div>
  `;
}
