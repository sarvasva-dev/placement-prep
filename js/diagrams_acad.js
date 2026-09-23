/**
 * Comprehensive SVG Diagram Generator for Semester 5 Academic Curricula
 * Covers CSJMU BCA-5001 (KMS/DSS), BCA-5002 (Java), BCA-5003 (Networks), BCA-5004 (Numerical Methods)
 */

export function renderAcademicSvg(topic = '', diagramRaw = '') {
  const t = (topic + ' ' + diagramRaw).toLowerCase();

  // 1. Herbert Simon's 4-Phase Model (Day 1)
  if (t.includes('simon') || t.includes('intelligence phase') || t.includes('decision making process') || t.includes('bounded rationality')) {
    return createSimonModelSvg();
  }

  // 2. 3-Tier DSS Architecture (Day 2)
  if (t.includes('dss') || t.includes('data subsystem') || t.includes('model subsystem') || t.includes('dialogue') || t.includes('decision support system')) {
    return createDssArchitectureSvg();
  }

  // 3. JVM Architecture & Runtime Data Areas (Day 3)
  if (t.includes('jvm') || t.includes('classloader') || t.includes('execution engine') || t.includes('bytecode') || (t.includes('runtime data') && t.includes('java'))) {
    return createJvmArchitectureSvg();
  }

  // 4. OSI 7-Layer Reference Model (Day 4)
  if (t.includes('osi') || t.includes('7-layer') || t.includes('transport (segment)') || t.includes('pdu') || t.includes('physical (bits)')) {
    return createOsiModelSvg();
  }

  // 5. Numerical Methods: Bisection Method (Day 5)
  if (t.includes('bisection') || t.includes('x_mid') || t.includes('intermediate value') || t.includes('interval halving')) {
    return createBisectionMethodSvg();
  }

  // 6. Java Thread Lifecycle & Concurrency (Day 6)
  if (t.includes('thread lifecycle') || (t.includes('thread') && (t.includes('runnable') || t.includes('waiting') || t.includes('blocked') || t.includes('terminated')))) {
    return createJavaThreadLifecycleSvg();
  }

  // 7. Nonaka's SECI Knowledge Spiral (Day 7)
  if (t.includes('seci') || t.includes('nonaka') || t.includes('tacit') || t.includes('socialization') || t.includes('externalization') || t.includes('knowledge management')) {
    return createSeciSpiralSvg();
  }

  // 8. Java Exception Hierarchy (Day 8)
  if (t.includes('exception hierarchy') || (t.includes('throwable') && t.includes('runtimeexception')) || (t.includes('checked') && t.includes('unchecked') && t.includes('exception'))) {
    return createJavaExceptionHierarchySvg();
  }

  // 9. TCP/IP Architecture vs OSI Model (Day 9)
  if (t.includes('tcp/ip') || t.includes('four layer') || t.includes('internet protocol suite')) {
    return createTcpIpLayersSvg();
  }

  // 10. Newton-Raphson Method Tangent Iteration (Day 10)
  if (t.includes('newton') || t.includes('raphson') || t.includes('tangent') || t.includes('f(x)/f\'(x)')) {
    return createNewtonRaphsonSvg();
  }

  // 11. Java Collections Framework Hierarchy (Day 11)
  if (t.includes('collection') || t.includes('arraylist') || t.includes('hashmap') || t.includes('hashset') || t.includes('iterable')) {
    return createCollectionsHierarchySvg();
  }

  // 12. Regula-Falsi / False Position Method (Day 12)
  if (t.includes('regula') || t.includes('false position') || t.includes('chord')) {
    return createRegulaFalsiSvg();
  }

  // 13. Data Warehouse ETL & Star/Snowflake Schema (Day 13)
  if (t.includes('warehouse') || t.includes('etl') || t.includes('star schema') || t.includes('olap cube')) {
    return createDataWarehouseEtlSvg();
  }

  // 14. IPv4 Subnetting & Header Architecture (Day 14)
  if (t.includes('ipv4') || t.includes('subnet') || t.includes('cidr') || t.includes('ip packet')) {
    return createIpv4HeaderSvg();
  }

  // 15. Gauss Elimination & Matrix Upper Triangular (Day 15)
  if (t.includes('gauss') || t.includes('matrix') || t.includes('triangular') || t.includes('pivoting') || t.includes('forward elimination')) {
    return createGaussEliminationSvg();
  }

  // Default Fallback
  return createAcademicDefaultSvg(topic);
}

function createSimonModelSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5001</span>
      <span class="svg-title">Herbert Simon's 4-Phase Decision Process & Feedback Loops</span>
    </div>
    <svg viewBox="0 0 860 330" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <defs>
        <marker id="acadArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="acadPurpleArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#c084fc" />
        </marker>
        <marker id="acadAmberArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#facc15" />
        </marker>
      </defs>

      <!-- 1. Intelligence Phase -->
      <g transform="translate(40, 40)">
        <rect width="220" height="75" rx="10" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <text x="110" y="32" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">1. INTELLIGENCE</text>
        <text x="110" y="52" text-anchor="middle" fill="#e0f2fe" font-size="11">Problem Scanning & Data Collection</text>
        <text x="110" y="68" text-anchor="middle" fill="#bae6fd" font-size="10">Executive Alerts & OLAP</text>
      </g>

      <line x1="260" y1="77" x2="330" y2="77" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>

      <!-- 2. Design Phase -->
      <g transform="translate(340, 40)">
        <rect width="220" height="75" rx="10" fill="#6d28d9" stroke="#c084fc" stroke-width="2"/>
        <text x="110" y="32" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">2. DESIGN PHASE</text>
        <text x="110" y="52" text-anchor="middle" fill="#f5f3ff" font-size="11">Formulate & Model Alternatives</text>
        <text x="110" y="68" text-anchor="middle" fill="#ddd6fe" font-size="10">Simulations & Mathematical Models</text>
      </g>

      <line x1="560" y1="77" x2="630" y2="77" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>

      <!-- 3. Choice Phase -->
      <g transform="translate(640, 40)">
        <rect width="180" height="75" rx="10" fill="#b45309" stroke="#fcd34d" stroke-width="2"/>
        <text x="90" y="32" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">3. CHOICE PHASE</text>
        <text x="90" y="52" text-anchor="middle" fill="#fef3c7" font-size="11">Evaluate & Satisfice</text>
        <text x="90" y="68" text-anchor="middle" fill="#fde68a" font-size="10">What-if & Sensitivity Trials</text>
      </g>

      <!-- Choice Refinement Loop back to Design -->
      <path d="M 730 40 L 730 15 L 450 15 L 450 30" fill="none" stroke="#facc15" stroke-width="2" stroke-dasharray="5,4" marker-end="url(#acadAmberArrow)" />
      <text x="590" y="11" text-anchor="middle" fill="#fde68a" font-size="10" font-weight="600">Refine Design if No Alternative Satisfies</text>

      <!-- Arrow down to Implementation -->
      <path d="M 730 115 L 730 185 L 570 185" fill="none" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>

      <!-- 4. Implementation Phase -->
      <g transform="translate(340, 150)">
        <rect width="220" height="75" rx="10" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <text x="110" y="32" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">4. IMPLEMENTATION</text>
        <text x="110" y="52" text-anchor="middle" fill="#ecfdf5" font-size="11">Action, Deployment & Scorecards</text>
        <text x="110" y="68" text-anchor="middle" fill="#a7f3d0" font-size="10">Real-Time Operational Monitoring</text>
      </g>

      <!-- Feedback loop from Implementation to Intelligence -->
      <path d="M 340 187 L 150 187 L 150 125" fill="none" stroke="#c084fc" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#acadPurpleArrow)"/>
      <text x="235" y="210" text-anchor="middle" fill="#e9d5ff" font-size="11" font-weight="600">Feedback Loop (Variance from Expected Metrics)</text>

      <!-- Academic Scoring Key Footer -->
      <g transform="translate(40, 250)">
        <rect width="780" height="60" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <text x="20" y="26" fill="#38bdf8" font-size="12" font-weight="700">★ 15-MARK EXAM RUBRIC FOR SIMON'S PROCESS:</text>
        <text x="20" y="47" fill="#94a3b8" font-size="11">• Simon initially proposed 3 stages; modern DSS literature formalized Implementation as the 4th stage.</text>
      </g>
    </svg>
  </div>
  `;
}

function createDssArchitectureSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5001</span>
      <span class="svg-title">3-Tier Decision Support System (DSS) Subsystems</span>
    </div>
    <svg viewBox="0 0 860 250" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 1. Data Management Subsystem -->
      <g transform="translate(40, 50)">
        <rect width="220" height="130" rx="10" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <text x="110" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">DATA SUBSYSTEM</text>
        <text x="110" y="65" text-anchor="middle" fill="#e0f2fe" font-size="11">Internal DBMS (ERP, CRM)</text>
        <text x="110" y="85" text-anchor="middle" fill="#e0f2fe" font-size="11">External Market Feeds</text>
        <text x="110" y="110" text-anchor="middle" fill="#bae6fd" font-size="10">Extraction & Data Directory</text>
      </g>

      <!-- Bidirectional Data <-> Model -->
      <line x1="260" y1="115" x2="330" y2="115" stroke="#38bdf8" stroke-width="3" marker-end="url(#acadArrow)"/>
      <line x1="330" y1="125" x2="260" y2="125" stroke="#38bdf8" stroke-width="3" marker-end="url(#acadArrow)"/>

      <!-- 2. Model Management Subsystem -->
      <g transform="translate(340, 50)">
        <rect width="220" height="130" rx="10" fill="#6d28d9" stroke="#c084fc" stroke-width="2"/>
        <text x="110" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">MODEL SUBSYSTEM</text>
        <text x="110" y="65" text-anchor="middle" fill="#f5f3ff" font-size="11">Financial & Forecasting</text>
        <text x="110" y="85" text-anchor="middle" fill="#f5f3ff" font-size="11">Optimization & Simulation</text>
        <text x="110" y="110" text-anchor="middle" fill="#ddd6fe" font-size="10">Model Base Mgmt (MBMS)</text>
      </g>

      <!-- Bidirectional Model <-> UI -->
      <line x1="560" y1="115" x2="630" y2="115" stroke="#34d399" stroke-width="3" marker-end="url(#acadArrow)"/>
      <line x1="630" y1="125" x2="560" y2="125" stroke="#34d399" stroke-width="3" marker-end="url(#acadArrow)"/>

      <!-- 3. User Interface / Dialogue Subsystem -->
      <g transform="translate(640, 50)">
        <rect width="180" height="130" rx="10" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">USER INTERFACE</text>
        <text x="90" y="65" text-anchor="middle" fill="#ecfdf5" font-size="11">Executive Dashboard</text>
        <text x="90" y="85" text-anchor="middle" fill="#ecfdf5" font-size="11">Interactive "What-If"</text>
        <text x="90" y="110" text-anchor="middle" fill="#a7f3d0" font-size="10">Decision Maker / User</text>
      </g>

      <text x="430" y="220" text-anchor="middle" fill="#facc15" font-size="12" font-weight="600">⚡ Core Architectural Triad: DBMS + MBMS + Dialogue Generation System (DGMS)</text>
    </svg>
  </div>
  `;
}

function createJvmArchitectureSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5002</span>
      <span class="svg-title">JVM Internal Architecture: ClassLoader, Runtime Areas & Execution Engine</span>
    </div>
    <svg viewBox="0 0 860 260" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 1. ClassLoader Subsystem -->
      <g transform="translate(30, 40)">
        <rect width="170" height="180" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="85" y="35" text-anchor="middle" fill="#c7d2fe" font-weight="800" font-size="13">CLASSLOADER</text>
        <text x="85" y="65" text-anchor="middle" fill="#fff" font-size="11">Loading</text>
        <text x="85" y="85" text-anchor="middle" fill="#a5b4fc" font-size="10">(Bootstrap, Ext, App)</text>
        <text x="85" y="115" text-anchor="middle" fill="#fff" font-size="11">Linking</text>
        <text x="85" y="135" text-anchor="middle" fill="#a5b4fc" font-size="10">(Verify, Prepare, Resolve)</text>
        <text x="85" y="165" text-anchor="middle" fill="#fff" font-size="11">Initialization</text>
      </g>

      <line x1="200" y1="130" x2="250" y2="130" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>

      <!-- 2. Runtime Data Areas -->
      <g transform="translate(260, 40)">
        <rect width="330" height="180" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="165" y="28" text-anchor="middle" fill="#38bdf8" font-weight="800" font-size="13">JVM RUNTIME DATA AREAS</text>
        
        <!-- Shared -->
        <rect x="15" y="45" width="140" height="55" rx="6" fill="#0369a1"/>
        <text x="85" y="70" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">HEAP MEMORY</text>
        <text x="85" y="88" text-anchor="middle" fill="#bae6fd" font-size="9">Shared / GC Managed</text>

        <rect x="170" y="45" width="145" height="55" rx="6" fill="#075985"/>
        <text x="242" y="70" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">METHOD AREA</text>
        <text x="242" y="88" text-anchor="middle" fill="#bae6fd" font-size="9">Bytecode / Static Fields</text>

        <!-- Thread-Local -->
        <rect x="15" y="110" width="95" height="55" rx="6" fill="#1e293b" stroke="#64748b"/>
        <text x="62" y="135" text-anchor="middle" fill="#cbd5e1" font-size="10" font-weight="700">JVM STACK</text>
        <text x="62" y="152" text-anchor="middle" fill="#94a3b8" font-size="8">Frames / Locals</text>

        <rect x="118" y="110" width="95" height="55" rx="6" fill="#1e293b" stroke="#64748b"/>
        <text x="165" y="135" text-anchor="middle" fill="#cbd5e1" font-size="10" font-weight="700">PC REGISTER</text>
        <text x="165" y="152" text-anchor="middle" fill="#94a3b8" font-size="8">Next Instruction</text>

        <rect x="220" y="110" width="95" height="55" rx="6" fill="#1e293b" stroke="#64748b"/>
        <text x="267" y="135" text-anchor="middle" fill="#cbd5e1" font-size="10" font-weight="700">NATIVE STACK</text>
        <text x="267" y="152" text-anchor="middle" fill="#94a3b8" font-size="8">C/C++ Methods</text>
      </g>

      <line x1="590" y1="130" x2="640" y2="130" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>

      <!-- 3. Execution Engine -->
      <g transform="translate(650, 40)">
        <rect width="180" height="180" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="32" text-anchor="middle" fill="#a7f3d0" font-weight="800" font-size="13">EXECUTION ENGINE</text>
        <text x="90" y="65" text-anchor="middle" fill="#fff" font-size="11">Interpreter</text>
        <text x="90" y="95" text-anchor="middle" fill="#34d399" font-weight="700" font-size="11">JIT COMPILER</text>
        <text x="90" y="112" text-anchor="middle" fill="#a7f3d0" font-size="9">(HotSpot Native Code)</text>
        <text x="90" y="145" text-anchor="middle" fill="#f87171" font-weight="700" font-size="11">GARBAGE COLLECTOR</text>
        <text x="90" y="162" text-anchor="middle" fill="#fca5a5" font-size="9">(Generational Mark-Sweep)</text>
      </g>
    </svg>
  </div>
  `;
}

function createOsiModelSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5003</span>
      <span class="svg-title">OSI 7-Layer Architecture: Protocols, PDUs & Flow</span>
    </div>
    <svg viewBox="0 0 860 310" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 7 Horizontal Banners -->
      <g transform="translate(40, 25)">
        <rect width="780" height="32" rx="4" fill="#1e1b4b" stroke="#818cf8"/>
        <text x="25" y="21" fill="#c7d2fe" font-weight="800" font-size="12">LAYER 7: APPLICATION</text>
        <text x="320" y="21" fill="#fff" font-size="11">PDU: Data / Message</text>
        <text x="560" y="21" fill="#a5b4fc" font-size="11">HTTP, HTTPS, DNS, SMTP, FTP</text>
      </g>

      <g transform="translate(40, 63)">
        <rect width="780" height="32" rx="4" fill="#311042" stroke="#c084fc"/>
        <text x="25" y="21" fill="#f3e8ff" font-weight="800" font-size="12">LAYER 6: PRESENTATION</text>
        <text x="320" y="21" fill="#fff" font-size="11">PDU: Formatted Data</text>
        <text x="560" y="21" fill="#e9d5ff" font-size="11">SSL/TLS, ASCII, UTF-8, JPEG, gzip</text>
      </g>

      <g transform="translate(40, 101)">
        <rect width="780" height="32" rx="4" fill="#4a044e" stroke="#f472b6"/>
        <text x="25" y="21" fill="#fdf2f8" font-weight="800" font-size="12">LAYER 5: SESSION</text>
        <text x="320" y="21" fill="#fff" font-size="11">PDU: Dialog Token</text>
        <text x="560" y="21" fill="#fbcfe8" font-size="11">RPC, NetBIOS, Sockets Session</text>
      </g>

      <g transform="translate(40, 139)">
        <rect width="780" height="32" rx="4" fill="#0369a1" stroke="#38bdf8"/>
        <text x="25" y="21" fill="#e0f2fe" font-weight="800" font-size="12">LAYER 4: TRANSPORT</text>
        <text x="320" y="21" fill="#fff" font-size="11">PDU: Segment / Datagram</text>
        <text x="560" y="21" fill="#bae6fd" font-size="11">TCP (Reliable), UDP (Fast), Ports</text>
      </g>

      <g transform="translate(40, 177)">
        <rect width="780" height="32" rx="4" fill="#065f46" stroke="#34d399"/>
        <text x="25" y="21" fill="#ecfdf5" font-weight="800" font-size="12">LAYER 3: NETWORK</text>
        <text x="320" y="21" fill="#fff" font-size="11">PDU: Packet</text>
        <text x="560" y="21" fill="#a7f3d0" font-size="11">IPv4, IPv6, ICMP, OSPF, Routers</text>
      </g>

      <g transform="translate(40, 215)">
        <rect width="780" height="32" rx="4" fill="#854d0e" stroke="#facc15"/>
        <text x="25" y="21" fill="#fefce8" font-weight="800" font-size="12">LAYER 2: DATA LINK</text>
        <text x="320" y="21" fill="#fff" font-size="11">PDU: Frame</text>
        <text x="560" y="21" fill="#fef08a" font-size="11">Ethernet, MAC Addresses, Switches</text>
      </g>

      <g transform="translate(40, 253)">
        <rect width="780" height="32" rx="4" fill="#1e293b" stroke="#94a3b8"/>
        <text x="25" y="21" fill="#f1f5f9" font-weight="800" font-size="12">LAYER 1: PHYSICAL</text>
        <text x="320" y="21" fill="#fff" font-size="11">PDU: Bits (0s & 1s)</text>
        <text x="560" y="21" fill="#cbd5e1" font-size="11">Cables (Cat6/Fiber), Hubs, Voltage</text>
      </g>
    </svg>
  </div>
  `;
}

function createBisectionMethodSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Numerical Methods: Bisection Root Search (Bolzano's Theorem)</span>
    </div>
    <svg viewBox="0 0 860 230" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Horizontal X axis -->
      <line x1="60" y1="120" x2="800" y2="120" stroke="#64748b" stroke-width="2"/>
      <text x="810" y="125" fill="#94a3b8" font-size="11">x</text>

      <!-- Curve f(x) crossing zero -->
      <path d="M 100 200 Q 350 160, 480 120 T 750 40" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="760" y="45" fill="#38bdf8" font-weight="700" font-size="12">y = f(x)</text>

      <!-- Point a where f(a) < 0 -->
      <circle cx="200" cy="180" r="5" fill="#ef4444"/>
      <line x1="200" y1="180" x2="200" y2="120" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="200" y="110" text-anchor="middle" fill="#fca5a5" font-weight="700">a [f(a) &lt; 0]</text>

      <!-- Point b where f(b) > 0 -->
      <circle cx="680" cy="60" r="5" fill="#34d399"/>
      <line x1="680" y1="60" x2="680" y2="120" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="680" y="138" text-anchor="middle" fill="#a7f3d0" font-weight="700">b [f(b) &gt; 0]</text>

      <!-- Midpoint x1 -->
      <circle cx="440" cy="130" r="6" fill="#facc15"/>
      <line x1="440" y1="130" x2="440" y2="120" stroke="#facc15" stroke-width="2"/>
      <text x="440" y="105" text-anchor="middle" fill="#fde68a" font-weight="800">x_mid = (a + b) / 2</text>

      <!-- Bracket interval -->
      <line x1="200" y1="160" x2="680" y2="160" stroke="#a855f7" stroke-width="2"/>
      <text x="440" y="175" text-anchor="middle" fill="#c084fc" font-size="11">Search Interval Width: (b - a) halves every iteration (2^-n)</text>
    </svg>
  </div>
  `;
}

function createJavaThreadLifecycleSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5002</span>
      <span class="svg-title">Java Thread Lifecycle (6 JVM States: java.lang.Thread.State)</span>
    </div>
    <svg viewBox="0 0 860 240" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- NEW -->
      <g transform="translate(40, 90)">
        <rect width="110" height="60" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
        <text x="55" y="35" text-anchor="middle" fill="#f8fafc" font-weight="700">NEW</text>
      </g>
      <line x1="150" y1="120" x2="210" y2="120" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>
      <text x="180" y="110" text-anchor="middle" fill="#94a3b8" font-size="10">start()</text>

      <!-- RUNNABLE -->
      <g transform="translate(220, 80)">
        <rect width="180" height="80" rx="10" fill="#0369a1" stroke="#38bdf8" stroke-width="2.5"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="800" font-size="14">RUNNABLE</text>
        <text x="90" y="55" text-anchor="middle" fill="#bae6fd" font-size="10">Ready / Running in OS</text>
      </g>

      <line x1="400" y1="120" x2="480" y2="120" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>

      <!-- BLOCKED / WAITING -->
      <g transform="translate(490, 40)">
        <rect width="170" height="60" rx="8" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <text x="85" y="28" text-anchor="middle" fill="#fecaca" font-weight="800" font-size="12">BLOCKED</text>
        <text x="85" y="46" text-anchor="middle" fill="#ffffff" font-size="10">Waiting for monitor lock</text>
      </g>
      <g transform="translate(490, 140)">
        <rect width="170" height="60" rx="8" fill="#431407" stroke="#f97316" stroke-width="2"/>
        <text x="85" y="28" text-anchor="middle" fill="#ffedd5" font-weight="800" font-size="12">WAITING / TIMED</text>
        <text x="85" y="46" text-anchor="middle" fill="#ffffff" font-size="10">wait() / sleep() / join()</text>
      </g>

      <!-- TERMINATED -->
      <line x1="400" y1="150" x2="710" y2="150" stroke="#34d399" stroke-width="2.5" marker-end="url(#acadArrow)"/>
      <g transform="translate(710, 110)">
        <rect width="120" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <text x="60" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800">TERMINATED</text>
      </g>
    </svg>
  </div>
  `;
}

function createSeciSpiralSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5001</span>
      <span class="svg-title">Nonaka & Takeuchi SECI Knowledge Creation Spiral</span>
    </div>
    <svg viewBox="0 0 860 250" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- 4 Quadrants -->
      <g transform="translate(80, 30)">
        <rect width="320" height="90" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <text x="160" y="35" text-anchor="middle" fill="#fff" font-weight="800">SOCIALIZATION (Tacit → Tacit)</text>
        <text x="160" y="60" text-anchor="middle" fill="#e0f2fe" font-size="11">Shared experience, observation, mentoring</text>
      </g>

      <g transform="translate(460, 30)">
        <rect width="320" height="90" rx="8" fill="#6d28d9" stroke="#c084fc" stroke-width="2"/>
        <text x="160" y="35" text-anchor="middle" fill="#fff" font-weight="800">EXTERNALIZATION (Tacit → Explicit)</text>
        <text x="160" y="60" text-anchor="middle" fill="#f5f3ff" font-size="11">Codifying tacit knowledge into blueprints & SOPs</text>
      </g>

      <g transform="translate(80, 140)">
        <rect width="320" height="90" rx="8" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <text x="160" y="35" text-anchor="middle" fill="#fff" font-weight="800">INTERNALIZATION (Explicit → Tacit)</text>
        <text x="160" y="60" text-anchor="middle" fill="#ecfdf5" font-size="11">Learning by doing, internalizing enterprise docs</text>
      </g>

      <g transform="translate(460, 140)">
        <rect width="320" height="90" rx="8" fill="#b45309" stroke="#fcd34d" stroke-width="2"/>
        <text x="160" y="35" text-anchor="middle" fill="#fff" font-weight="800">COMBINATION (Explicit → Explicit)</text>
        <text x="160" y="60" text-anchor="middle" fill="#fef3c7" font-size="11">Synthesizing multiple reports & databases</text>
      </g>
    </svg>
  </div>
  `;
}

function createJavaExceptionHierarchySvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5002</span>
      <span class="svg-title">Java Throwable Hierarchy: Checked vs Unchecked Exceptions</span>
    </div>
    <svg viewBox="0 0 860 240" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Throwable Root -->
      <g transform="translate(340, 20)">
        <rect width="180" height="40" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="90" y="25" text-anchor="middle" fill="#c7d2fe" font-weight="800">java.lang.Throwable</text>
      </g>

      <line x1="380" y1="60" x2="200" y2="100" stroke="#f87171" stroke-width="2" marker-end="url(#acadArrow)"/>
      <line x1="480" y1="60" x2="640" y2="100" stroke="#38bdf8" stroke-width="2" marker-end="url(#acadArrow)"/>

      <!-- Error -->
      <g transform="translate(100, 100)">
        <rect width="200" height="110" rx="8" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <text x="100" y="30" text-anchor="middle" fill="#fecaca" font-weight="800">Error (Unrecoverable)</text>
        <text x="100" y="55" text-anchor="middle" fill="#fff" font-size="11">OutOfMemoryError</text>
        <text x="100" y="75" text-anchor="middle" fill="#fff" font-size="11">StackOverflowError</text>
        <text x="100" y="95" text-anchor="middle" fill="#fca5a5" font-size="10">JVM Fatal Hardware/RAM</text>
      </g>

      <!-- Exception -->
      <g transform="translate(540, 100)">
        <rect width="280" height="120" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <text x="140" y="28" text-anchor="middle" fill="#fff" font-weight="800">Exception (Program Recoverable)</text>
        <text x="140" y="55" text-anchor="middle" fill="#bae6fd" font-size="11">Checked: IOException, SQLException</text>
        <text x="140" y="75" text-anchor="middle" fill="#facc15" font-weight="700" font-size="11">RuntimeException (Unchecked):</text>
        <text x="140" y="95" text-anchor="middle" fill="#fef08a" font-size="10">NullPointerException, ArrayIndexOutOfBounds</text>
      </g>
    </svg>
  </div>
  `;
}

function createTcpIpLayersSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5003</span>
      <span class="svg-title">TCP/IP 4-Layer Protocol Stack Mapping</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 30)">
        <rect width="780" height="36" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
        <text x="30" y="23" fill="#c7d2fe" font-weight="800">4. APPLICATION LAYER</text>
        <text x="500" y="23" fill="#fff" font-size="11">HTTP, SMTP, DNS, SSH, FTP</text>
      </g>
      <g transform="translate(40, 75)">
        <rect width="780" height="36" rx="6" fill="#0369a1" stroke="#38bdf8"/>
        <text x="30" y="23" fill="#e0f2fe" font-weight="800">3. TRANSPORT LAYER</text>
        <text x="500" y="23" fill="#fff" font-size="11">TCP (Reliable Byte Stream) / UDP</text>
      </g>
      <g transform="translate(40, 120)">
        <rect width="780" height="36" rx="6" fill="#065f46" stroke="#34d399"/>
        <text x="30" y="23" fill="#ecfdf5" font-weight="800">2. INTERNET LAYER</text>
        <text x="500" y="23" fill="#fff" font-size="11">IP (IPv4/IPv6), ICMP, ARP</text>
      </g>
      <g transform="translate(40, 165)">
        <rect width="780" height="36" rx="6" fill="#1e293b" stroke="#64748b"/>
        <text x="30" y="23" fill="#cbd5e1" font-weight="800">1. NETWORK ACCESS LAYER</text>
        <text x="500" y="23" fill="#fff" font-size="11">Ethernet, Wi-Fi (802.11), MAC Drivers</text>
      </g>
    </svg>
  </div>
  `;
}

function createNewtonRaphsonSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Newton-Raphson Method: Quadratic Convergence Tangent Iteration</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <line x1="60" y1="120" x2="800" y2="120" stroke="#64748b" stroke-width="2"/>
      <path d="M 80 190 Q 300 170, 520 80 T 780 20" fill="none" stroke="#38bdf8" stroke-width="3"/>
      
      <!-- Tangent from x0 down to x1 -->
      <line x1="500" y1="88" x2="350" y2="120" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5,4"/>
      <circle cx="500" cy="88" r="5" fill="#ef4444"/>
      <text x="500" y="70" fill="#fca5a5" font-weight="700">(x0, f(x0))</text>
      <text x="350" y="140" fill="#facc15" font-weight="800">x1 = x0 - f(x0)/f'(x0)</text>

      <rect x="60" y="160" width="740" height="36" rx="6" fill="#0f172a" stroke="#38bdf8"/>
      <text x="430" y="183" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="700">Formula: x_(n+1) = x_n - [f(x_n) / f'(x_n)] | Quadratic Convergence: Error_n+1 ≈ C * (Error_n)^2</text>
    </svg>
  </div>
  `;
}

function createCollectionsHierarchySvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5002</span>
      <span class="svg-title">Java Collections Framework (JCF) Interface Hierarchy</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(340, 20)">
        <rect width="180" height="35" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
        <text x="90" y="22" text-anchor="middle" fill="#c7d2fe" font-weight="800">Collection &lt;E&gt;</text>
      </g>
      <g transform="translate(60, 90)">
        <rect width="200" height="100" rx="8" fill="#0369a1" stroke="#38bdf8"/>
        <text x="100" y="30" text-anchor="middle" fill="#fff" font-weight="800">List &lt;E&gt; (Ordered)</text>
        <text x="100" y="55" text-anchor="middle" fill="#bae6fd" font-size="11">• ArrayList (Fast random O(1))</text>
        <text x="100" y="75" text-anchor="middle" fill="#bae6fd" font-size="11">• LinkedList (Fast insert O(1))</text>
      </g>
      <g transform="translate(330, 90)">
        <rect width="200" height="100" rx="8" fill="#6d28d9" stroke="#c084fc"/>
        <text x="100" y="30" text-anchor="middle" fill="#fff" font-weight="800">Set &lt;E&gt; (Unique)</text>
        <text x="100" y="55" text-anchor="middle" fill="#ddd6fe" font-size="11">• HashSet (O(1) Hashing)</text>
        <text x="100" y="75" text-anchor="middle" fill="#ddd6fe" font-size="11">• TreeSet (O(log N) Red-Black)</text>
      </g>
      <g transform="translate(600, 90)">
        <rect width="200" height="100" rx="8" fill="#047857" stroke="#34d399"/>
        <text x="100" y="30" text-anchor="middle" fill="#fff" font-weight="800">Queue &lt;E&gt; / Map</text>
        <text x="100" y="55" text-anchor="middle" fill="#a7f3d0" font-size="11">• PriorityQueue (Binary Heap)</text>
        <text x="100" y="75" text-anchor="middle" fill="#a7f3d0" font-size="11">• HashMap &lt;K,V&gt; (Buckets)</text>
      </g>
    </svg>
  </div>
  `;
}

function createRegulaFalsiSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Regula-Falsi (Method of False Position) Secant Chord Iteration</span>
    </div>
    <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <line x1="60" y1="110" x2="800" y2="110" stroke="#64748b" stroke-width="2"/>
      <path d="M 120 180 Q 400 150, 520 110 T 740 30" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <!-- Secant chord connecting (a, f(a)) and (b, f(b)) -->
      <line x1="180" y1="165" x2="700" y2="40" stroke="#facc15" stroke-width="2" stroke-dasharray="4,3"/>
      <circle cx="180" cy="165" r="5" fill="#ef4444"/>
      <circle cx="700" cy="40" r="5" fill="#34d399"/>
      <text x="180" y="185" fill="#fca5a5" font-weight="700">a, f(a)</text>
      <text x="700" y="30" fill="#a7f3d0" font-weight="700">b, f(b)</text>

      <rect x="60" y="150" width="740" height="36" rx="6" fill="#0f172a" stroke="#facc15"/>
      <text x="430" y="173" text-anchor="middle" fill="#fde68a" font-size="12" font-weight="700">Chord Root Formula: c = [a · f(b) - b · f(a)] / [f(b) - f(a)]</text>
    </svg>
  </div>
  `;
}

function createDataWarehouseEtlSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5001</span>
      <span class="svg-title">Enterprise Data Warehouse (EDW) ETL & Dimensional Modeling Pipeline</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="90" rx="8" fill="#1e293b" stroke="#38bdf8"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="800">OPERATIONAL DATA</text>
        <text x="90" y="60" text-anchor="middle" fill="#fff" font-size="11">OLTP Databases, Logs</text>
        <text x="90" y="78" text-anchor="middle" fill="#94a3b8" font-size="10">Normalized 3NF Tables</text>
      </g>
      <line x1="220" y1="95" x2="300" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>
      <g transform="translate(310, 45)">
        <rect width="240" height="100" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="120" y="32" text-anchor="middle" fill="#c084fc" font-weight="800">ETL PIPELINE</text>
        <text x="120" y="55" text-anchor="middle" fill="#fff" font-size="11">Extract → Transform → Load</text>
        <text x="120" y="75" text-anchor="middle" fill="#e9d5ff" font-size="10">De-duplication & Staging</text>
      </g>
      <line x1="550" y1="95" x2="630" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>
      <g transform="translate(640, 50)">
        <rect width="180" height="90" rx="8" fill="#064e3b" stroke="#34d399"/>
        <text x="90" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800">STAR SCHEMA DW</text>
        <text x="90" y="60" text-anchor="middle" fill="#fff" font-size="11">Central Fact Table</text>
        <text x="90" y="78" text-anchor="middle" fill="#6ee7b7" font-size="10">Dimension Tables</text>
      </g>
    </svg>
  </div>
  `;
}

function createIpv4HeaderSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5003</span>
      <span class="svg-title">IPv4 Datagram Header Format (20 Bytes Minimum)</span>
    </div>
    <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 30)">
        <rect width="100" height="40" fill="#1e293b" stroke="#38bdf8"/>
        <text x="50" y="25" text-anchor="middle" fill="#fff" font-size="11">Version (4b)</text>
        <rect x="100" width="100" height="40" fill="#1e293b" stroke="#38bdf8"/>
        <text x="150" y="25" text-anchor="middle" fill="#fff" font-size="11">IHL (4b)</text>
        <rect x="200" width="180" height="40" fill="#1e293b" stroke="#38bdf8"/>
        <text x="290" y="25" text-anchor="middle" fill="#fff" font-size="11">Type of Service (8b)</text>
        <rect x="380" width="400" height="40" fill="#1e293b" stroke="#38bdf8"/>
        <text x="580" y="25" text-anchor="middle" fill="#fff" font-size="11">Total Length (16 bits)</text>
      </g>
      <g transform="translate(40, 70)">
        <rect width="390" height="40" fill="#0369a1" stroke="#38bdf8"/>
        <text x="195" y="25" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">Source IP Address (32 bits)</text>
        <rect x="390" width="390" height="40" fill="#047857" stroke="#34d399"/>
        <text x="585" y="25" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">Destination IP Address (32 bits)</text>
      </g>
    </svg>
  </div>
  `;
}

function createGaussEliminationSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Gauss Elimination: Forward Elimination to Upper Triangular Form</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(60, 40)">
        <rect width="280" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="140" y="30" text-anchor="middle" fill="#38bdf8" font-weight="700">Augmented Matrix [A | B]</text>
        <text x="140" y="55" text-anchor="middle" fill="#fff" font-family="monospace">[ a11  a12  a13 | b1 ]</text>
        <text x="140" y="75" text-anchor="middle" fill="#fff" font-family="monospace">[ a21  a22  a23 | b2 ]</text>
        <text x="140" y="95" text-anchor="middle" fill="#fff" font-family="monospace">[ a31  a32  a33 | b3 ]</text>
      </g>
      <line x1="360" y1="95" x2="440" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>
      <text x="400" y="85" text-anchor="middle" fill="#38bdf8" font-size="10">R2, R3 Ops</text>

      <g transform="translate(460, 40)">
        <rect width="280" height="110" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="140" y="30" text-anchor="middle" fill="#a7f3d0" font-weight="700">Upper Triangular [U | B']</text>
        <text x="140" y="55" text-anchor="middle" fill="#fff" font-family="monospace">[ a11  a12  a13 | b1 ]</text>
        <text x="140" y="75" text-anchor="middle" fill="#facc15" font-family="monospace">[  0   a22' a23'| b2']</text>
        <text x="140" y="95" text-anchor="middle" fill="#facc15" font-family="monospace">[  0    0   a33''| b3'']</text>
      </g>
      <text x="430" y="180" text-anchor="middle" fill="#cbd5e1" font-size="11">⚡ Solved via Backward Substitution: x3 = b3'' / a33'' → Substitute into Row 2 → Row 1</text>
    </svg>
  </div>
  `;
}

function createAcademicDefaultSvg(topic) {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">ACADEMIC SCHEMATIC</span>
      <span class="svg-title">${topic || 'Theoretical Framework'}</span>
    </div>
    <svg viewBox="0 0 860 160" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <rect x="40" y="30" width="780" height="100" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="430" y="70" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="800">${topic || 'Academic Conceptual Framework'}</text>
      <text x="430" y="100" text-anchor="middle" fill="#94a3b8" font-size="12">15-Mark University Standard • Pedagogical Rigor • CSJMU Syllabi</text>
    </svg>
  </div>
  `;
}
