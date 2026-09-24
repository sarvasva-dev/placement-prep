/**
 * SVG Diagram Generators for Verified Engineering Projects (SmartGalla, BulkBeat TV, CSMS, DocRoute, Django, BEVM)
 */

export function renderProjectDefenseSvg(projectName = '', topic = '') {
  const p = (projectName + ' ' + topic).toLowerCase();

  if (p.includes('csms') || p.includes('college student')) {
    if (p.includes('auth') || p.includes('bcrypt') || p.includes('role')) {
      return createCsmsAuthSvg();
    }
    if (p.includes('schema') || p.includes('attendance') || p.includes('relational')) {
      return createCsmsAttendanceSvg();
    }
    return createCsmsArchitectureSvg();
  }

  if (p.includes('smartgalla')) {
    if (p.includes('payment') || p.includes('razorpay') || p.includes('webhook')) {
      return createSmartGallaPaymentSvg();
    }
    if (p.includes('geospatial') || p.includes('logistics') || p.includes('delivery')) {
      return createSmartGallaLogisticsSvg();
    }
    return createSmartGallaTenantSvg();
  }

  if (p.includes('bulkbeat') || p.includes('nse2')) {
    if (p.includes('sqlite') || p.includes('wal') || p.includes('lock elimination') || p.includes('queue')) {
      return createBulkBeatWalSvg();
    }
    if (p.includes('telegram') || p.includes('push') || p.includes('notification')) {
      return createBulkBeatNotificationSvg();
    }
    return createBulkBeatConcurrencySvg();
  }

  if (p.includes('docroute') || p.includes('document')) {
    if (p.includes('ocr') || p.includes('tesseract') || p.includes('fallback')) {
      return createDocRouteOcrFallbackSvg();
    }
    return createDocRoutePipelineSvg();
  }

  if (p.includes('django') || p.includes('orm') || p.includes('mvt')) {
    return createDjangoMvtSvg();
  }

  if (p.includes('bevm') || p.includes('voting') || p.includes('fingerprint') || p.includes('cryptographic')) {
    if (p.includes('fernet') || p.includes('encryption') || p.includes('key')) {
      return createBevmEncryptionSvg();
    }
    if (p.includes('biometric') || p.includes('auth') || p.includes('role')) {
      return createBevmBiometricAuthSvg();
    }
    return createBevmCryptographicLedgerSvg();
  }

  // Fallback
  return createProjectFallbackSvg(projectName, topic);
}

function createCsmsAuthSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSMS DEFENSE</span>
      <span class="svg-title">CSMS: Multi-Role JWT RBAC & Bcrypt Password Security</span>
    </div>
    <svg viewBox="0 0 860 230" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <defs>
        <marker id="projArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <!-- Client Request -->
      <g transform="translate(40, 50)">
        <rect width="160" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="80" y="35" text-anchor="middle" fill="#38bdf8" font-weight="800" font-size="13">CLIENT LOGIN</text>
        <text x="80" y="60" text-anchor="middle" fill="#f8fafc" font-size="11">POST /api/auth/login</text>
        <text x="80" y="78" text-anchor="middle" fill="#94a3b8" font-size="10">{ username, pass }</text>
      </g>

      <line x1="200" y1="95" x2="270" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <!-- Bcrypt Verification -->
      <g transform="translate(280, 45)">
        <rect width="190" height="100" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="95" y="32" text-anchor="middle" fill="#c7d2fe" font-weight="800" font-size="13">BCRYPT VERIFY</text>
        <text x="95" y="55" text-anchor="middle" fill="#ffffff" font-size="11">Work Factor: 12 Rounds</text>
        <text x="95" y="75" text-anchor="middle" fill="#a5b4fc" font-size="10">Timing-Attack Resistant</text>
        <text x="95" y="90" text-anchor="middle" fill="#34d399" font-size="10">Hash Match Confirmed</text>
      </g>

      <line x1="470" y1="95" x2="540" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <!-- JWT Claim Token -->
      <g transform="translate(550, 40)">
        <rect width="270" height="110" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="135" y="32" text-anchor="middle" fill="#a7f3d0" font-weight="800" font-size="13">ISSUED JWT CLAIMS</text>
        <text x="135" y="58" text-anchor="middle" fill="#ffffff" font-family="monospace" font-size="11">{ sub: "user_491",</text>
        <text x="135" y="76" text-anchor="middle" fill="#facc15" font-family="monospace" font-size="11">role: "STUDENT"|"FACULTY"|"ADMIN" }</text>
        <text x="135" y="96" text-anchor="middle" fill="#6ee7b7" font-size="10">HMAC-SHA256 Signed • 8h Expiry</text>
      </g>

      <text x="430" y="195" text-anchor="middle" fill="#94a3b8" font-size="12">🛡️ Fast Route Protection via FastAPI Depends(get_current_active_user) Dependency Injection</text>
    </svg>
  </div>
  `;
}

function createCsmsAttendanceSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSMS RELATIONAL ENGINE</span>
      <span class="svg-title">CSMS: Attendance Shortage Engine & Aggregation Pipeline</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="700">Daily Attendance Logs</text>
        <text x="90" y="60" text-anchor="middle" fill="#94a3b8" font-size="11">faculty_id, student_id</text>
        <text x="90" y="78" text-anchor="middle" fill="#94a3b8" font-size="11">date, is_present: Boolean</text>
      </g>

      <line x1="220" y1="95" x2="290" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(300, 45)">
        <rect width="240" height="100" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="120" y="35" text-anchor="middle" fill="#c084fc" font-weight="800">Shortage Engine (SQL)</text>
        <text x="120" y="60" text-anchor="middle" fill="#fff" font-size="11">SUM(present) / COUNT(*) * 100</text>
        <text x="120" y="80" text-anchor="middle" fill="#f87171" font-weight="700" font-size="11">Threshold Check: &lt; 75%</text>
      </g>

      <line x1="540" y1="95" x2="610" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(620, 50)">
        <rect width="200" height="90" rx="8" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <text x="100" y="35" text-anchor="middle" fill="#fecaca" font-weight="800">HOD Alert & Debar List</text>
        <text x="100" y="60" text-anchor="middle" fill="#ffffff" font-size="11">Automated Warning SMS</text>
        <text x="100" y="78" text-anchor="middle" fill="#fca5a5" font-size="10">Admit Card Block Rule</text>
      </g>
    </svg>
  </div>
  `;
}

function createCsmsArchitectureSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSMS ARCHITECTURE</span>
      <span class="svg-title">College Student Management System (Full-Stack ERP Architecture)</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="100" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="800">WEB ERP FRONTEND</text>
        <text x="90" y="60" text-anchor="middle" fill="#f8fafc" font-size="11">HTML5 + CSS3 + JS</text>
        <text x="90" y="80" text-anchor="middle" fill="#94a3b8" font-size="10">Responsive Dashboards</text>
      </g>

      <line x1="220" y1="100" x2="310" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>
      <text x="265" y="90" text-anchor="middle" fill="#38bdf8" font-size="10">REST API</text>

      <g transform="translate(320, 40)">
        <rect width="220" height="120" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="110" y="32" text-anchor="middle" fill="#c7d2fe" font-weight="800">FASTAPI SERVER</text>
        <text x="110" y="55" text-anchor="middle" fill="#fff" font-size="11">Pydantic v2 Serialization</text>
        <text x="110" y="75" text-anchor="middle" fill="#a5b4fc" font-size="11">SQLAlchemy 2.0 ORM</text>
        <text x="110" y="95" text-anchor="middle" fill="#34d399" font-size="10">Alembic Migration Guard</text>
      </g>

      <line x1="540" y1="100" x2="620" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>
      <text x="580" y="90" text-anchor="middle" fill="#38bdf8" font-size="10">TCP Port 5432</text>

      <g transform="translate(630, 50)">
        <rect width="190" height="100" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="95" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800">POSTGRESQL</text>
        <text x="95" y="60" text-anchor="middle" fill="#ffffff" font-size="11">Supabase Managed DB</text>
        <text x="95" y="80" text-anchor="middle" fill="#6ee7b7" font-size="10">ACID Relational Constraints</text>
      </g>
    </svg>
  </div>
  `;
}

function createSmartGallaTenantSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">SMARTGALLA DEFENSE</span>
      <span class="svg-title">SmartGalla: Multi-Tenant Schema Isolation & Subdomain Routing</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="800">PYTHON BACKEND</text>
        <text x="90" y="60" text-anchor="middle" fill="#fff" font-size="11">WSGI / Middleware</text>
        <text x="90" y="78" text-anchor="middle" fill="#94a3b8" font-size="10">store1.smartgalla.com</text>
      </g>

      <line x1="220" y1="95" x2="300" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(310, 45)">
        <rect width="240" height="100" rx="8" fill="#1e1b4b" stroke="#c084fc" stroke-width="2"/>
        <text x="120" y="32" text-anchor="middle" fill="#c084fc" font-weight="800">TENANT CONTEXT INJECTOR</text>
        <text x="120" y="55" text-anchor="middle" fill="#fff" font-size="11">Header: X-Tenant-Id</text>
        <text x="120" y="75" text-anchor="middle" fill="#a855f7" font-size="10">Row-Level Security (RLS)</text>
        <text x="120" y="92" text-anchor="middle" fill="#a7f3d0" font-size="10">tenant_id = auth.uid()</text>
      </g>

      <line x1="550" y1="95" x2="630" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(640, 50)">
        <rect width="180" height="90" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800">SUPABASE POSTGRES</text>
        <text x="90" y="60" text-anchor="middle" fill="#fff" font-size="11">Isolated Row Data</text>
        <text x="90" y="78" text-anchor="middle" fill="#6ee7b7" font-size="10">Zero cross-tenant leak</text>
      </g>
    </svg>
  </div>
  `;
}

function createSmartGallaPaymentSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">SMARTGALLA DEFENSE</span>
      <span class="svg-title">Razorpay Webhook Idempotency & Order Settlement Ledger</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="700">Razorpay Webhook</text>
        <text x="90" y="60" text-anchor="middle" fill="#fff" font-size="11">order.paid event</text>
        <text x="90" y="78" text-anchor="middle" fill="#94a3b8" font-size="10">X-Razorpay-Signature</text>
      </g>

      <line x1="220" y1="95" x2="290" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(300, 45)">
        <rect width="240" height="100" rx="8" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2"/>
        <text x="120" y="32" text-anchor="middle" fill="#fbbf24" font-weight="800">IDEMPOTENCY GUARD</text>
        <text x="120" y="55" text-anchor="middle" fill="#fff" font-size="11">Lookup event_id in SQLite</text>
        <text x="120" y="75" text-anchor="middle" fill="#fde68a" font-size="10">If seen: Return 200 OK early</text>
        <text x="120" y="92" text-anchor="middle" fill="#34d399" font-size="10">Prevents Double-Crediting</text>
      </g>

      <line x1="540" y1="95" x2="620" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(630, 50)">
        <rect width="190" height="90" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="95" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800">SETTLE INVOICE</text>
        <text x="95" y="60" text-anchor="middle" fill="#fff" font-size="11">Update order_status</text>
        <text x="95" y="78" text-anchor="middle" fill="#6ee7b7" font-size="10">Generate thermal slip</text>
      </g>
    </svg>
  </div>
  `;
}

function createSmartGallaLogisticsSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">SMARTGALLA DEFENSE</span>
      <span class="svg-title">Geospatial Routing & Automated Rider Assignment Pipeline</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="700">Order Placed</text>
        <text x="90" y="60" text-anchor="middle" fill="#fff" font-size="11">Lat, Long coordinates</text>
        <text x="90" y="78" text-anchor="middle" fill="#94a3b8" font-size="10">Delivery address</text>
      </g>
      <line x1="220" y1="95" x2="300" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(310, 45)">
        <rect width="230" height="100" rx="8" fill="#1e1b4b" stroke="#34d399" stroke-width="2"/>
        <text x="115" y="32" text-anchor="middle" fill="#34d399" font-weight="800">HAVERSINE DISTANCE</text>
        <text x="115" y="55" text-anchor="middle" fill="#fff" font-size="11">Calculate radius d &lt; 5km</text>
        <text x="115" y="75" text-anchor="middle" fill="#a7f3d0" font-size="10">Filter idle fleet drivers</text>
      </g>
      <line x1="540" y1="95" x2="620" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(630, 50)">
        <rect width="190" height="90" rx="8" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <text x="95" y="35" text-anchor="middle" fill="#fff" font-weight="800">DISPATCH TO RIDER</text>
        <text x="95" y="60" text-anchor="middle" fill="#ecfdf5" font-size="11">Push / SMS Alert</text>
        <text x="95" y="78" text-anchor="middle" fill="#a7f3d0" font-size="10">Accept/Reject 30s timer</text>
      </g>
    </svg>
  </div>
  `;
}

function createBulkBeatConcurrencySvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">BULKBEAT TV / NSE2</span>
      <span class="svg-title">Real-Time Financial Media Ingestion & AsyncIO Architecture</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Media Streams -->
      <g transform="translate(40, 30)">
        <rect width="180" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-size="11">CNBC-TV18 Audio Stream</text>
      </g>
      <g transform="translate(40, 110)">
        <rect width="180" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-size="11">Zee Business Stream</text>
      </g>

      <line x1="220" y1="60" x2="310" y2="90" stroke="#38bdf8" stroke-width="2" marker-end="url(#projArrow)"/>
      <line x1="220" y1="140" x2="310" y2="100" stroke="#38bdf8" stroke-width="2" marker-end="url(#projArrow)"/>

      <!-- Async Ingestion Pipeline -->
      <g transform="translate(320, 45)">
        <rect width="230" height="110" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="115" y="32" text-anchor="middle" fill="#c084fc" font-weight="800">PYTHON ASYNCIO WORKER</text>
        <text x="115" y="55" text-anchor="middle" fill="#fff" font-size="11">FFmpeg Chunk Ingestion</text>
        <text x="115" y="75" text-anchor="middle" fill="#e9d5ff" font-size="11">Whisper Live Audio Transcribe</text>
        <text x="115" y="95" text-anchor="middle" fill="#a7f3d0" font-size="10">Latency: &lt; 850ms</text>
      </g>

      <line x1="550" y1="100" x2="630" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <!-- NLP Keyword Filter -->
      <g transform="translate(640, 45)">
        <rect width="180" height="110" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="32" text-anchor="middle" fill="#a7f3d0" font-weight="800">STOCK MATCHER</text>
        <text x="90" y="55" text-anchor="middle" fill="#fff" font-size="11">Regex 5000+ Tickers</text>
        <text x="90" y="75" text-anchor="middle" fill="#fff" font-size="11">Sentiment Tagging</text>
        <text x="90" y="95" text-anchor="middle" fill="#facc15" font-size="10">Alert Dispatch</text>
      </g>
    </svg>
  </div>
  `;
}

function createBulkBeatWalSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">BULKBEAT TV / NSE2</span>
      <span class="svg-title">SQLite Concurrency: Write-Ahead Logging (WAL) & Single-Writer Queue</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Async Concurrent Readers -->
      <g transform="translate(40, 30)">
        <rect width="180" height="60" rx="6" fill="#0284c7"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="700">Async Reader Coroutines</text>
      </g>

      <!-- Async Writer Queue -->
      <g transform="translate(40, 110)">
        <rect width="180" height="60" rx="6" fill="#7f1d1d" stroke="#ef4444"/>
        <text x="90" y="28" text-anchor="middle" fill="#fff" font-weight="700">Async Writers</text>
        <text x="90" y="48" text-anchor="middle" fill="#fca5a5" font-size="10">asyncio.Queue buffer</text>
      </g>

      <line x1="220" y1="60" x2="330" y2="70" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>
      <line x1="220" y1="140" x2="330" y2="130" stroke="#ef4444" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <!-- SQLite WAL Engine -->
      <g transform="translate(340, 45)">
        <rect width="260" height="110" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="130" y="32" text-anchor="middle" fill="#c7d2fe" font-weight="800">SQLITE (PRAGMA journal_mode=WAL)</text>
        <text x="130" y="55" text-anchor="middle" fill="#fff" font-size="11">Readers DO NOT block Writers</text>
        <text x="130" y="75" text-anchor="middle" fill="#fff" font-size="11">Writers DO NOT block Readers</text>
        <text x="130" y="95" text-anchor="middle" fill="#34d399" font-size="10">Zero "database is locked" crashes</text>
      </g>

      <line x1="600" y1="100" x2="670" y2="100" stroke="#34d399" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <!-- WAL File on Disk -->
      <g transform="translate(680, 50)">
        <rect width="140" height="90" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="70" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800">app.db-wal</text>
        <text x="70" y="60" text-anchor="middle" fill="#fff" font-size="10">Append-Only log</text>
        <text x="70" y="78" text-anchor="middle" fill="#6ee7b7" font-size="9">Auto Checkpoint</text>
      </g>
    </svg>
  </div>
  `;
}

function createBulkBeatNotificationSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">BULKBEAT TV / NSE2</span>
      <span class="svg-title">Telegram Bot Push Notification Delivery Pipeline</span>
    </div>
    <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="80" rx="8" fill="#1e293b" stroke="#38bdf8"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="700">Stock Signal Trigger</text>
        <text x="90" y="58" text-anchor="middle" fill="#fff" font-size="11">Breakout Detection</text>
      </g>
      <line x1="220" y1="90" x2="310" y2="90" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(320, 45)">
        <rect width="220" height="90" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="110" y="32" text-anchor="middle" fill="#c084fc" font-weight="800">RATE-LIMIT THROTTLER</text>
        <text x="110" y="55" text-anchor="middle" fill="#fff" font-size="11">Telegram Cap: 30 msg/sec</text>
        <text x="110" y="75" text-anchor="middle" fill="#a7f3d0" font-size="10">Token Bucket Leaky Flow</text>
      </g>
      <line x1="540" y1="90" x2="630" y2="90" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(640, 50)">
        <rect width="180" height="80" rx="8" fill="#0369a1" stroke="#38bdf8"/>
        <text x="90" y="35" text-anchor="middle" fill="#fff" font-weight="700">Subscribed Channels</text>
        <text x="90" y="58" text-anchor="middle" fill="#bae6fd" font-size="11">Broadcast Message</text>
      </g>
    </svg>
  </div>
  `;
}

function createBevmCryptographicLedgerSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">BEVM ARCHITECTURE</span>
      <span class="svg-title">BEVM: Tamper-Evident Chained SHA-256 Ballot Ledger</span>
    </div>
    <svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <!-- Genesis Block -->
      <g transform="translate(30, 40)">
        <rect width="210" height="130" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="105" y="30" text-anchor="middle" fill="#38bdf8" font-weight="800">GENESIS BLOCK #0</text>
        <rect x="15" y="45" width="180" height="30" rx="4" fill="#0f172a"/>
        <text x="105" y="65" text-anchor="middle" fill="#94a3b8" font-family="monospace" font-size="11">Prev: 000000000000</text>
        <text x="105" y="105" text-anchor="middle" fill="#ffffff" font-size="11">Election Initialized</text>
        <text x="105" y="125" text-anchor="middle" fill="#a7f3d0" font-family="monospace" font-size="10">H0 = SHA256(Genesis)</text>
      </g>

      <line x1="240" y1="105" x2="310" y2="105" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>
      <text x="275" y="95" text-anchor="middle" fill="#38bdf8" font-family="monospace" font-size="10">H0</text>

      <!-- Ballot Block 1 -->
      <g transform="translate(320, 40)">
        <rect width="230" height="130" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="115" y="30" text-anchor="middle" fill="#c7d2fe" font-weight="800">BALLOT BLOCK #1</text>
        <rect x="15" y="45" width="200" height="30" rx="4" fill="#0f172a"/>
        <text x="115" y="65" text-anchor="middle" fill="#818cf8" font-family="monospace" font-size="10">Prev: H0 (Genesis)</text>
        <text x="115" y="100" text-anchor="middle" fill="#ffffff" font-size="11">Fernet(Choice) + Timestamp</text>
        <text x="115" y="125" text-anchor="middle" fill="#a7f3d0" font-family="monospace" font-size="10">H1 = SHA256(H0 + Data1)</text>
      </g>

      <line x1="550" y1="105" x2="620" y2="105" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>
      <text x="585" y="95" text-anchor="middle" fill="#38bdf8" font-family="monospace" font-size="10">H1</text>

      <!-- Ballot Block 2 -->
      <g transform="translate(630, 40)">
        <rect width="200" height="130" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="100" y="30" text-anchor="middle" fill="#a7f3d0" font-weight="800">BALLOT BLOCK #2</text>
        <rect x="15" y="45" width="170" height="30" rx="4" fill="#0f172a"/>
        <text x="100" y="65" text-anchor="middle" fill="#34d399" font-family="monospace" font-size="10">Prev: H1 (Block #1)</text>
        <text x="100" y="100" text-anchor="middle" fill="#ffffff" font-size="11">Fernet(Choice) + Timestamp</text>
        <text x="100" y="125" text-anchor="middle" fill="#a7f3d0" font-family="monospace" font-size="10">H2 = SHA256(H1 + Data2)</text>
      </g>
    </svg>
  </div>
  `;
}

function createBevmEncryptionSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">BEVM CRYPTOGRAPHY</span>
      <span class="svg-title">BEVM: Fernet AES-256 Symmetric Payload Encryption & Key Isolation</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 45)">
        <rect width="180" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="35" text-anchor="middle" fill="#38bdf8" font-weight="700">Raw Ballot Selection</text>
        <text x="90" y="65" text-anchor="middle" fill="#ffffff" font-size="12">Candidate ID: 4</text>
        <text x="90" y="85" text-anchor="middle" fill="#94a3b8" font-size="10">Timestamp: UTC ISO</text>
        <text x="90" y="105" text-anchor="middle" fill="#f87171" font-size="10">Unencrypted Plaintext</text>
      </g>
      <line x1="220" y1="100" x2="300" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(310, 35)">
        <rect width="250" height="130" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="125" y="30" text-anchor="middle" fill="#c084fc" font-weight="800">FERNET ENCRYPTION</text>
        <text x="125" y="55" text-anchor="middle" fill="#fff" font-size="11">AES-128-CBC + PKCS7 Padding</text>
        <text x="125" y="75" text-anchor="middle" fill="#fff" font-size="11">HMAC-SHA256 Authentication</text>
        <rect x="25" y="90" width="200" height="25" rx="4" fill="#0f172a"/>
        <text x="125" y="107" text-anchor="middle" fill="#fbbf24" font-family="monospace" font-size="10">Key: Air-Gapped secret.key</text>
      </g>
      <line x1="560" y1="100" x2="640" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(650, 45)">
        <rect width="170" height="110" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="85" y="35" text-anchor="middle" fill="#a7f3d0" font-weight="800">Encrypted Ballot</text>
        <text x="85" y="65" text-anchor="middle" fill="#ffffff" font-family="monospace" font-size="10">gAAAAABl...</text>
        <text x="85" y="85" text-anchor="middle" fill="#e2e8f0" font-size="10">Ciphertext stored</text>
        <text x="85" y="105" text-anchor="middle" fill="#34d399" font-size="10">Zero plain choice at rest</text>
      </g>
    </svg>
  </div>
  `;
}

function createBevmBiometricAuthSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">BEVM AUTHENTICATION</span>
      <span class="svg-title">BEVM: Biometric Verification & Atomic SQLite State Locking</span>
    </div>
    <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 50)">
        <rect width="180" height="100" rx="8" fill="#1e293b" stroke="#64748b"/>
        <text x="90" y="35" text-anchor="middle" fill="#cbd5e1" font-weight="700">1. Citizen Identity</text>
        <text x="90" y="60" text-anchor="middle" fill="#94a3b8" font-size="11">Voter ID / Biometrics</text>
        <text x="90" y="80" text-anchor="middle" fill="#38bdf8" font-size="10">Fingerprint Hash Match</text>
      </g>
      <line x1="220" y1="100" x2="280" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(290, 45)">
        <polygon points="70,0 140,55 70,110 0,55" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2"/>
        <text x="70" y="50" text-anchor="middle" fill="#fbbf24" font-weight="700" font-size="10">has_voted</text>
        <text x="70" y="68" text-anchor="middle" fill="#fbbf24" font-weight="700" font-size="10">== 0 ?</text>
      </g>

      <line x1="430" y1="100" x2="500" y2="100" stroke="#34d399" stroke-width="2.5" marker-end="url(#projArrow)"/>
      <text x="465" y="90" fill="#34d399" font-weight="700" font-size="11">YES</text>

      <g transform="translate(510, 40)">
        <rect width="310" height="120" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="155" y="30" text-anchor="middle" fill="#a7f3d0" font-weight="800">ATOMIC TRANSACTION COMMIT</text>
        <text x="155" y="55" text-anchor="middle" fill="#fff" font-size="11">1. INSERT INTO votes (encrypted_ballot, hash)</text>
        <text x="155" y="75" text-anchor="middle" fill="#fff" font-size="11">2. UPDATE voters SET has_voted = 1</text>
        <text x="155" y="100" text-anchor="middle" fill="#fde68a" font-weight="700" font-size="10">Double-Vote mathematically prevented</text>
      </g>
    </svg>
  </div>
  `;
}

function createDocRoutePipelineSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">DOCROUTE DEFENSE</span>
      <span class="svg-title">DocRoute: Adaptive Document Intelligence Pipeline (PyMuPDF vs Tesseract OCR)</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(30, 45)">
        <rect width="170" height="100" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="85" y="32" text-anchor="middle" fill="#38bdf8" font-weight="800">DOCUMENT INGEST</text>
        <text x="85" y="55" text-anchor="middle" fill="#fff" font-size="11">PDF / Invoices / Forms</text>
        <text x="85" y="75" text-anchor="middle" fill="#94a3b8" font-size="10">Binary Stream / File</text>
      </g>
      <line x1="200" y1="95" x2="260" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(270, 45)">
        <rect width="190" height="100" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="95" y="32" text-anchor="middle" fill="#c7d2fe" font-weight="800">PyMuPDF EXTRACT</text>
        <text x="95" y="55" text-anchor="middle" fill="#fff" font-size="11">Direct Vector Text Parse</text>
        <text x="95" y="75" text-anchor="middle" fill="#a7f3d0" font-size="10">Confidence & Density Check</text>
      </g>

      <line x1="460" y1="95" x2="520" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(530, 40)">
        <polygon points="55,0 110,55 55,110 0,55" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2"/>
        <text x="55" y="50" text-anchor="middle" fill="#fbbf24" font-weight="700" font-size="10">Vector</text>
        <text x="55" y="66" text-anchor="middle" fill="#fbbf24" font-weight="700" font-size="10">Text OK?</text>
      </g>

      <line x1="640" y1="95" x2="690" y2="95" stroke="#34d399" stroke-width="2.5" marker-end="url(#projArrow)"/>
      <text x="665" y="85" fill="#34d399" font-weight="700" font-size="10">YES</text>

      <g transform="translate(700, 45)">
        <rect width="140" height="100" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="70" y="32" text-anchor="middle" fill="#a7f3d0" font-weight="800">STRUCTURED</text>
        <text x="70" y="55" text-anchor="middle" fill="#fff" font-size="11">Clean JSON</text>
        <text x="70" y="75" text-anchor="middle" fill="#6ee7b7" font-size="10">Sub-50ms Output</text>
      </g>
    </svg>
  </div>
  `;
}

function createDocRouteOcrFallbackSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">DOCROUTE OCR DEFENSE</span>
      <span class="svg-title">DocRoute: Image Preprocessing & Tesseract OCR Fallback Route</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(30, 45)">
        <rect width="180" height="100" rx="8" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <text x="90" y="32" text-anchor="middle" fill="#fca5a5" font-weight="800">SCANNED / RASTER PDF</text>
        <text x="90" y="55" text-anchor="middle" fill="#fff" font-size="11">Zero Native Embedded Text</text>
        <text x="90" y="75" text-anchor="middle" fill="#fecaca" font-size="10">Density &lt; Threshold</text>
      </g>
      <line x1="210" y1="95" x2="280" y2="95" stroke="#ef4444" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(290, 45)">
        <rect width="230" height="100" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="115" y="32" text-anchor="middle" fill="#c084fc" font-weight="800">IMAGE PREPROCESSING</text>
        <text x="115" y="55" text-anchor="middle" fill="#fff" font-size="11">Grayscale + Otsu Binarization</text>
        <text x="115" y="75" text-anchor="middle" fill="#a7f3d0" font-size="10">Deskew & Noise Removal (PIL)</text>
      </g>

      <line x1="520" y1="95" x2="590" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(600, 45)">
        <rect width="230" height="100" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="115" y="32" text-anchor="middle" fill="#a7f3d0" font-weight="800">TESSERACT OCR ENGINE</text>
        <text x="115" y="55" text-anchor="middle" fill="#fff" font-size="11">Bounding Box & Text Recognition</text>
        <text x="115" y="75" text-anchor="middle" fill="#6ee7b7" font-size="10">Confidence-Weighted Extraction</text>
      </g>
    </svg>
  </div>
  `;
}

function createDjangoMvtSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">DJANGO DEFENSE</span>
      <span class="svg-title">Django Architecture: MVT Request-Response Cycle & ORM Relational Guard</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(30, 45)">
        <rect width="160" height="100" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="80" y="32" text-anchor="middle" fill="#38bdf8" font-weight="800">HTTP REQUEST</text>
        <text x="80" y="55" text-anchor="middle" fill="#fff" font-size="11">urls.py Regex Route</text>
        <text x="80" y="75" text-anchor="middle" fill="#94a3b8" font-size="10">CSRF & Session Guard</text>
      </g>
      <line x1="190" y1="95" x2="250" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(260, 45)">
        <rect width="200" height="100" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="100" y="32" text-anchor="middle" fill="#c7d2fe" font-weight="800">VIEW (views.py)</text>
        <text x="100" y="55" text-anchor="middle" fill="#fff" font-size="11">Business Logic Layer</text>
        <text x="100" y="75" text-anchor="middle" fill="#a7f3d0" font-size="10">QuerySet Evaluation</text>
      </g>

      <line x1="460" y1="95" x2="520" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(530, 45)">
        <rect width="170" height="100" rx="8" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <text x="85" y="32" text-anchor="middle" fill="#a7f3d0" font-weight="800">MODEL (ORM)</text>
        <text x="85" y="55" text-anchor="middle" fill="#fff" font-size="11">models.py 3NF Tables</text>
        <text x="85" y="75" text-anchor="middle" fill="#ecfdf5" font-size="10">Postgres / SQLite WAL</text>
      </g>

      <line x1="700" y1="95" x2="740" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#projArrow)"/>

      <g transform="translate(750, 45)">
        <rect width="100" height="100" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
        <text x="50" y="35" text-anchor="middle" fill="#fbbf24" font-weight="800">TEMPLATE</text>
        <text x="50" y="55" text-anchor="middle" fill="#fff" font-size="10">HTML5 /</text>
        <text x="50" y="72" text-anchor="middle" fill="#fff" font-size="10">DRF JSON</text>
      </g>
    </svg>
  </div>
  `;
}

function createProjectFallbackSvg(projectName, topic) {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">PROJECT DEFENSE</span>
      <span class="svg-title">${projectName || 'Production Project'} — ${topic || 'System Topology'}</span>
    </div>
    <svg viewBox="0 0 860 160" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <rect x="40" y="30" width="780" height="100" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="430" y="70" text-anchor="middle" fill="#34d399" font-size="16" font-weight="800">${projectName || 'System Architecture'}</text>
      <text x="430" y="100" text-anchor="middle" fill="#94a3b8" font-size="12">Verified Codebase Artifacts • Zero Hallucination • Placement Defensible</text>
    </svg>
  </div>
  `;
}
