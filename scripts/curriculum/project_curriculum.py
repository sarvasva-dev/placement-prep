"""
Curriculum for Project Preparation across all 30 days.
Focuses strictly on Sarthak's real heavyweight repositories in D:\Projects:
- SmartGalla (Next.js 16, React 19, Supabase RLS, Razorpay, PWA Serwist, Google Maps, Blinkit Scraping, PDF Invoices)
- NSE2 / BulkBeat TV (Real-Time Ingestion, aiohttp, SQLite WAL Concurrency, Telegram Webhooks, Razorpay Reconciliation, Dhan API, Systemd)
- Caloriv (React Native Expo, Android Toolchain, Gradle Build Orchestration, Nutrition Analytics, Offline Sync)
- Biometric Electronic Voting System - BEVM (Python, SQLite, Fernet AES-256, Chained SHA-256 Audit Ledger, Biometric Authentication)
- College Student Management System - CSMS (FastAPI, Supabase PostgreSQL, Vanilla JS, Render)
"""

def get_project_for_day(day):
    # Rotation cycle of 5 real projects
    proj_type = (day - 1) % 5
    
    if proj_type == 0:
        # SmartGalla
        topics = [
            ("Multi-Tenant Architecture & Tech Stack Selection (Next.js 16, React 19, Supabase)", 
             "Understanding the transition from monolithic e-commerce to edge-rendered multi-tenant retail SaaS.",
             "Next.js App Router server components execute on the server, streaming HTML with zero client bundle overhead for catalog views.",
             [
                 {"q": "Why did you choose Next.js 16 with Supabase for SmartGalla instead of a standard MERN stack?",
                  "a": "SmartGalla is a multi-tenant retail and inventory platform where catalog SEO, fast cold starts, and strict tenant isolation are vital. Next.js 16 provides Server Components and streaming SSR, reducing first contentful paint (FCP) to under 800ms. Supabase provides PostgreSQL with Row-Level Security (RLS), allowing us to enforce tenant isolation at the database level rather than relying entirely on application-level filtering."},
                 {"q": "How does Row-Level Security (RLS) protect merchant data in SmartGalla?",
                  "a": "In Postgres, each table has an `auth.uid()` or `store_id` check in its RLS policy: `CREATE POLICY tenant_isolation ON orders USING (store_id = current_setting('app.current_store_id'));`. Even if an API route fails to filter by store_id, the database rejects unauthorized reads or writes."}
             ],
             "I built SmartGalla as a modern retail operating system for local merchants using Next.js 16 and Supabase. The core challenge was keeping client bundles light while maintaining instantaneous inventory lookups. By offloading catalog rendering to Server Components and isolating merchant stores via PostgreSQL Row-Level Security, we achieve sub-second page loads and zero cross-store data leaks."),
            
            ("Payment Gateway Integration & Webhook Idempotency (Razorpay & COD Ledger)",
             "How payment callbacks, signatures, and distributed transactions are verified safely.",
             "HMAC-SHA256 signature verification prevents man-in-the-middle payment spoofing.",
             [
                 {"q": "How do you handle Razorpay webhook idempotency in SmartGalla?",
                  "a": "When a customer pays, Razorpay sends an asynchronous webhook (`payment.captured` or `order.paid`). Because network retries can send the same webhook multiple times, we store every incoming `razorpay_payment_id` in a dedicated `payment_transactions` table with a UNIQUE constraint. If an incoming event already exists, the database ignores it and returns HTTP 200 immediately, preventing duplicate order fulfillments."},
                 {"q": "How does the Cash on Delivery (COD) ledger prevent courier fraud?",
                  "a": "For COD orders, payment status is initialized as 'PENDING_CASH'. When the delivery agent marks an order 'DELIVERED', the transaction triggers an automated debit to the rider's active cash bag in `cod_ledger` and an unverified credit to the merchant. The merchant must reconcile the physical cash handover with a single-click OTP confirmation, closing the ledger loop."}
             ],
             "In SmartGalla, payment reliability is paramount. For digital payments, I implemented Razorpay with cryptographically verified webhooks using HMAC-SHA256 and unique transaction deduplication. For physical cash orders, I built a double-entry COD ledger that reconciles collected cash against delivery agent accounts before crediting merchant balances."),

            ("Geospatial Logistics & Automated Delivery Assignment (Google Maps & Leaflet)",
             "Spatial distance calculation, store geofencing, and rider dispatch algorithms.",
             "The Haversine formula calculates great-circle distance between store coordinates and customer addresses: d = 2R * arcsin(sqrt(sin^2(dlat/2) + cos(lat1)*cos(lat2)*sin^2(dlon/2))).",
             [
                 {"q": "How does SmartGalla assign nearby delivery agents to new orders?",
                  "a": "When an order enters the 'READY_FOR_PICKUP' state, the logistics assignment engine runs a spatial query over active riders within a 5km radius of the merchant's store. We filter riders whose active delivery load is less than 3 orders, rank them by Haversine proximity, and dispatch an automated push notification with a 45-second acceptance timeout. If unanswered, it cascades to the next nearest rider."},
                 {"q": "Why combine Google Maps API with Leaflet in the same project?",
                  "a": "Google Maps Places API provides superior address autocomplete and geocoding accuracy in Indian tier-2 cities. However, for live tracking dashboards where coordinates update every 5 seconds via WebSockets, rendering Google Maps tiles incurs significant API cost. We use Leaflet with OpenStreetMap tiles for client-side map rendering, cutting map API costs by over 70% while keeping high accuracy."}
             ],
             "I designed an automated logistics dispatch engine in SmartGalla. It uses Google Places for customer geocoding and Leaflet with spatial distance formulas to match available delivery partners within a 5km geofenced radius. It balances delivery load across active agents and provides real-time route telemetry."),

            ("Automated Competitive Intelligence: The Blinkit Web Scraping Engine",
             "Headless price intelligence, product matching, and automated catalog pricing.",
             "Price parity alerts help local merchants stay competitive against dark-store quick-commerce giants.",
             [
                 {"q": "How does the Blinkit scraping worker in SmartGalla extract real-time grocery prices?",
                  "a": "We engineered an automated Node.js worker using Playwright that queries Blinkit's public catalog search endpoints using rotating User-Agents and localized pincodes. It extracts SKU names, pack sizes, MRP, and discounted prices into structured JSON (`blinkit_scraped.json`). A string similarity algorithm (Levenshtein distance) matches merchant inventory items to competitor items to highlight price disparities."},
                 {"q": "How do you prevent rate-limiting or IP bans while scraping quick-commerce platforms?",
                  "a": "We use jittered exponential backoffs, polite request intervals (minimum 1.5 seconds between page turns), and headless session cookie reuse. Furthermore, we run extraction in scheduled off-peak batches (2:00 AM IST) and cache scraped pricing snapshots in PostgreSQL for 24 hours."}
             ],
             "To empower traditional merchants against quick-commerce apps, I built a competitive intelligence scraper for SmartGalla. It runs scheduled Playwright workers to capture Blinkit grocery pricing across local pincodes, maps competitor SKUs to local store inventory, and provides merchants with automated margin optimization suggestions."),

            ("Progressive Web App (PWA) & Offline-First POS Engine (Serwist & Service Workers)",
             "Offline POS operations, background sync, and cache storage management.",
             "Cache-first strategy for static assets and Stale-While-Revalidate for product catalogs.",
             [
                 {"q": "How does SmartGalla allow store billing when the store internet disconnects?",
                  "a": "Using `@serwist/next` (modern Workbox successor), we register a service worker that caches the entire merchant POS interface, barcode scanner bundle, and the store's current active product catalog in IndexedDB. When offline, bills can still be created and stored in an IndexedDB outbox queue. Once the browser detects `window.navigator.onLine`, a background sync worker automatically flushes queued orders to the Supabase backend with original timestamps."},
                 {"q": "What happens if two devices sell the last unit of an item while offline?",
                  "a": "We implement an optimistic concurrency model with a timestamped reconciliation log. When the offline queue syncs, if stock falls below zero, the transaction records a 'STOCK_OVERDRAWN' alert in the admin audit log rather than corrupting database integrity, prompting the merchant to adjust stock."}
             ],
             "Internet reliability is unpredictable in Indian grocery stores. In SmartGalla, I implemented an offline-first PWA architecture using Serwist and IndexedDB. Cashiers can continue barcode scanning and printing receipts even during network dropouts, with automatic background synchronization once connectivity is restored."),

            ("Dynamic PDF Invoice & Thermal Receipt Generation (pdf-lib & Serverless)",
             "Programmatic vector PDF composition, GST tax breakdowns, and thermal printer formatting.",
             "`pdf-lib` allows pure JavaScript PDF document creation with zero reliance on heavy headless Chrome / Puppeteer instances.",
             [
                 {"q": "Why generate invoices with pdf-lib instead of rendering HTML to PDF via Puppeteer?",
                  "a": "Spawning a headless Chrome instance via Puppeteer on serverless infrastructure requires 300MB+ RAM, takes 2-4 seconds per document, and causes cold-start timeouts. `pdf-lib` is a pure JavaScript low-overhead library that compiles vector PDF streams directly into memory in under 80 milliseconds with only 15MB RAM, supporting custom 80mm thermal receipt formats and A4 GST invoices."},
                 {"q": "How do you handle Indian GST invoice compliance in the generated document?",
                  "a": "The PDF generator splits total sales into CGST and SGST for intra-state sales (50-50 split of the GST rate) or IGST for inter-state transactions. It automatically formats the merchant's GSTIN, customer details, HSN/SAC codes per item, reverse charge indicators, and converts total numeric amounts to words per Indian banking standards."}
             ],
             "For SmartGalla's billing pipeline, I replaced slow Puppeteer PDF rendering with high-speed programmatic vector generation using `pdf-lib`. It produces compliant GST invoices and 80mm thermal receipts in under 100ms on serverless endpoints with minimal memory overhead.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "SmartGalla",
            "repo_path": "D:\\Projects\\SmartGalla",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }

    elif proj_type == 1:
        # NSE2 / BulkBeat TV
        topics = [
            ("Real-Time Financial Media Ingestion & Concurrency Architecture (Python AsyncIO & aiohttp)",
             "How event loops handle hundreds of concurrent WebSocket connections and polling workers.",
             "AsyncIO runs a single-threaded cooperative event loop where coroutines yield control via `await`, allowing thousands of idle I/O sockets without OS thread overhead.",
             [
                 {"q": "How does the NSE2 ingestion engine achieve sub-50ms announcement processing?",
                  "a": "The engine uses a dedicated `aiohttp.ClientSession` pool with HTTP keep-alive to poll NSE corporate announcement feeds and market disclosure endpoints every 500ms. When a new filing payload arrives, it bypasses synchronous disk operations and pushes raw payloads into an in-memory `asyncio.Queue`. Worker coroutines parse the corporate action (dividends, splits, earnings results) and extract key financial metrics concurrently."},
                 {"q": "How do you handle sudden market open surges (9:15 AM IST) when hundreds of disclosures arrive simultaneously?",
                  "a": "We use a token-bucket rate limiter combined with backpressure handling on the asyncio queue. If the queue size exceeds 500 items, the poller backs off slightly while worker threads drain notifications in priority order (Price Sensitive Announcements first, routine filings second)."}
             ],
             "BulkBeat TV / NSE2 is a real-time market disclosure alert engine built in Python. During earnings season, hundreds of market filings drop simultaneously. Using an async event-driven architecture with aiohttp and priority queues, the system processes and dispatches actionable trade alerts with sub-second latency across 6,000+ active users."),

            ("Database Concurrency & Lock Elimination in SQLite (Write-Ahead Logging & Single-Writer Queue)",
             "Eliminating 'database is locked' errors under heavy write surges.",
             "PRAGMA journal_mode=WAL; allows readers to query previous database snapshots while a writer appends to the -wal file.",
             [
                 {"q": "Why did SQLite throw 'database is locked' errors in NSE2, and how did you permanently fix it?",
                  "a": "Default SQLite uses rollback journaling, where any write operation places an exclusive write lock on the entire database file, preventing concurrent reads. During news spikes, multiple coroutines tried to insert news items while the API server read subscriber lists, causing write collisions. I fixed this by: 1. Enabling Write-Ahead Logging (`PRAGMA journal_mode=WAL;`), allowing concurrent reads and writes, and 2. Funneling all write operations through a single dedicated consumer coroutine reading from an `asyncio.Queue`."},
                 {"q": "What is the difference between PRAGMA synchronous = NORMAL vs FULL?",
                  "a": "Under WAL mode, setting `PRAGMA synchronous = NORMAL;` only syncs the WAL file at critical checkpoints rather than every transaction. This boosts write throughput by over 400% while still maintaining ACID guarantees against application crashes."}
             ],
             "A common critique of SQLite in production is concurrency. In BulkBeat TV, I handled high-traffic alert bursts by enabling Write-Ahead Logging (WAL) and funneling all database inserts through a single-writer asyncio queue. This completely eliminated write contention locks while maintaining blistering microsecond read latencies."),

            ("Telegram Push Notification Infrastructure & Webhook Architecture",
             "Transforming polling bots into event-driven push notification pipelines.",
             "Webhooks allow Telegram's edge servers to push user messages directly to our API server, eliminating idle socket polling.",
             [
                 {"q": "Why migrate from Telegram long polling to Webhook architecture in NSE2?",
                  "a": "Long polling requires continuous outgoing HTTP requests every 1-2 seconds, which exhausts network sockets, consumes idle CPU, and increases latency when thousands of users interact with the bot. Webhooks transform the system into an event-driven push architecture: Telegram pushes updates to our HTTPS domain only when an event occurs, dramatically lowering server resource utilization."},
                 {"q": "How do you broadcast breaking alerts to thousands of subscribers without hitting Telegram rate limits?",
                  "a": "Telegram limits broadcast messages to approximately 30 messages per second across chats. We implement a distributed token-bucket rate-limiter: alerts are enqueued in priority batches and dispatched across an asynchronous worker pool that pauses automatically when Telegram returns an HTTP 429 (`retry_after`) header."}
             ],
             "For instant alert delivery in BulkBeat TV, I architected an event-driven notification service using Telegram Bot Webhooks. It incorporates a token-bucket rate limiter to deliver real-time news cards to thousands of subscribers while strictly honoring Telegram's 30 msg/sec API broadcast limits."),

            ("Subscription Monetization, Webhook Reconciliation & Real Revenue Metrics",
             "Auditing Razorpay subscription webhooks, ledger reconciliation, and verified user metrics.",
             "104 paying subscribers generated approximately ₹1.11 lakh in revenue with automated license key provisioning.",
             [
                 {"q": "How did you automate subscription renewals and access revocation in NSE2?",
                  "a": "We integrated Razorpay Subscriptions. When a user pays, Razorpay triggers a webhook containing the user's telegram ID in the payment notes. The backend verifies the HMAC signature, updates `users.working_days_left` in `trading_bot.db`, and sends a personalized receipt card. A nightly cron job decrements active days and automatically downgrades expired users to the free tier."},
                 {"q": "How did you reconcile payments when webhook deliveries failed during network glitches?",
                  "a": "I authored `audit_all_razorpay_payments.py` and `reconcile_payments.py`, which periodically fetch raw settlement logs directly from Razorpay's REST API and cross-reference them against internal database transactions. Any orphaned payments are backfilled automatically without manual intervention."}
             ],
             "BulkBeat TV wasn't just a toy project—it was a commercial SaaS that generated ~₹1.11 lakh in revenue from 104 paying subscribers. I built the full billing infrastructure with Razorpay webhooks, automated subscription renewals, access gating, and payment reconciliation scripts that ensured zero license loss."),

            ("Dhan REST API Integration, Chartink Screeners & Technical Analysis Pipelines",
             "Connecting market data providers, parsing live quotes, and technical momentum filtering.",
             "Dhan API provides real-time market depth and Level 2 quote data via authenticated HTTP endpoints.",
             [
                 {"q": "How did you integrate Dhan API and Chartink screeners into the news alert flow?",
                  "a": "When a corporate disclosure is published for a stock (e.g., RELIANCE), the pipeline triggers an immediate quote fetch via Dhan REST API (`/v2/quotes`) to capture current market price, volume surge factor, and day's range. It cross-references this with Chartink breakout screeners, allowing the alert card to display whether the stock is breaking its 52-week high at the exact moment of the announcement."},
                 {"q": "How do you filter noise from thousands of daily routine corporate filings?",
                  "a": "We use a multi-stage classification pipeline: 1. Keyword regex filters out standard compliance filings (e.g., loss of share certificates); 2. A sentiment and impact scoring heuristic evaluates financial magnitude; 3. Only announcements scoring above threshold are queued for push delivery."}
             ],
             "To provide actionable context on news alerts, I integrated the Dhan REST API to pull live market quotes and volume multipliers the instant a disclosure hits the wire. The system parses Chartink breakout screeners to append technical momentum indicators to corporate announcement cards in real time."),

            ("Production Linux Deployment, Systemd Supervision & Zero-Downtime Daemon Watchdogs",
             "Process management, crash recovery, and daemon lifecycle on a cloud VPS.",
             "`systemd` manages long-running Python background processes, restarting workers on failure and logging to `journalctl`.",
             [
                 {"q": "How did you achieve 99.8% uptime for NSE2 on a cloud Linux VPS?",
                  "a": "All services (`api_server.py`, `admin_bot_main.py`, `sync_worker.py`) run as supervised systemd service units with `Restart=always` and `RestartSec=5s`. I implemented a dedicated `watchdog_service.py` that sends heartbeat pings to an internal health endpoint every 30 seconds; if the worker hangs or deadlocks, the watchdog kills the PID, triggering systemd to spawn a fresh instance."},
                 {"q": "How do you monitor server logs and memory leaks in production?",
                  "a": "We stream logs through Python's `logging.handlers.RotatingFileHandler` to prevent disk saturation, and use custom bash scripts (`status-logs.ps1`, `view_logs.sh`) and Telegram admin alerts that notify me immediately if unhandled exceptions spike."}
             ],
             "I deployed and maintained BulkBeat TV on a cloud Linux VPS, configuring systemd unit files, process supervisors, and an automated health watchdog. This ensured seamless crash recovery, zero orphaned background processes, and 99.8% server availability.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "NSE2 / BulkBeat TV",
            "repo_path": "D:\\Projects\\nse2",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }

    elif proj_type == 2:
        # Caloriv
        topics = [
            ("Cross-Platform Mobile App Architecture with React Native & Expo",
             "Component lifecycle, native bridge, and Expo managed workflow in mobile health tracking.",
             "React Native renders real native Android and iOS UI components via the native bridge, offering 60 FPS scrolling compared to webview wrappers.",
             [
                 {"q": "Why build Caloriv with React Native Expo instead of native Kotlin/Swift?",
                  "a": "Caloriv required rapid feature iteration across both Android and iOS with a single unified TypeScript codebase. Expo provides pre-built native module bindings for camera capture, local SQLite storage, push notifications, and background task scheduling, allowing 85%+ code reuse between platforms while preserving native rendering performance."},
                 {"q": "How does Caloriv maintain smooth 60 FPS UI performance during complex list scrolling?",
                  "a": "We use React Native's `FlatList` with `getItemLayout` optimization, memoized render items (`React.memo`), and avoid anonymous function allocations in render loops. High-frequency gestures and animation transitions are offloaded to the native thread via `react-native-reanimated`."}
             ],
             "Caloriv is a cross-platform calorie and nutrition tracking mobile app built with React Native and Expo. I structured the application using a modular component hierarchy and typed state management, enabling seamless meal logging and instant macro analytics across both Android and iOS devices."),

            ("Android Build Toolchain, SDK Management & Production Gradle Orchestration",
             "Gradle dependency resolution, Android Studio SDK paths, release keystores, and APK packaging.",
             "`./gradlew assembleRelease` compiles native Java/Kotlin code, packages Hermes bytecode, and signs the release APK.",
             [
                 {"q": "What challenges did you face configuring the Android build toolchain for Caloriv, and how did you resolve them?",
                  "a": "Upgrading to modern React Native versions introduced build failures with Java 17 and Android Gradle Plugin (AGP) incompatibilities. I resolved this by authoring automated PowerShell and batch repair scripts (`fix_gradle.ps1`, `setup-android-env.bat`) that set correct `JAVA_HOME`, patched module-level `build.gradle` files to align `compileSdkVersion 34`, and configured `caloriv-release-key.keystore` for verified production APK signing."},
                 {"q": "What is Hermes and why is it enabled in Caloriv's Android builds?",
                  "a": "Hermes is an open-source JavaScript engine optimized specifically for React Native on Android. By compiling JavaScript into optimized bytecode ahead-of-time (AOT) during the build step, it slashes mobile app startup time (TTI) by over 50% and reduces APK size and memory consumption."}
             ],
             "Beyond writing app features, I mastered the native mobile build pipeline. In Caloriv, I configured Android Studio SDK toolchains, authored Gradle patch scripts to resolve native dependency conflicts, optimized Hermes ahead-of-time compilation, and generated production-signed APKs."),

            ("Nutrition Analytics Engine: Calorie Budgeting & Macronutrient Algorithms",
             "Mathematical formulas for Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE), and macro balancing.",
             "Mifflin-St Jeor Formula: BMR = (10 * weight in kg) + (6.25 * height in cm) - (5 * age) + s (where s = +5 for men, -161 for women).",
             [
                 {"q": "How does Caloriv compute personalized calorie and macronutrient targets for users?",
                  "a": "The app implements the Mifflin-St Jeor formula to determine the user's Basal Metabolic Rate (BMR), multiplies it by an activity multiplier (1.2 to 1.9) to compute Total Daily Energy Expenditure (TDEE), and adjusts by ±500 kcal based on whether the goal is weight loss or gain. It then computes custom macronutrient splits: 30% Protein, 40% Carbohydrates, and 30% Healthy Fats."},
                 {"q": "How does the app prevent rounding discrepancies when users log partial food servings?",
                  "a": "All nutritional data is stored per 100g base units using fixed-precision integers (milligrams for micronutrients, tenths of grams for macros) in SQLite. When a user logs a custom serving (e.g., 140g), the calculation multiplies by `serving_weight / 100` and rounds only at the final display layer to prevent cumulative floating-point errors."}
             ],
             "I engineered Caloriv's core nutrition calculation engine. It utilizes the Mifflin-St Jeor formula to dynamically determine daily caloric budgets and macronutrient ratios based on user biometric goals, maintaining precision by calculating off normalized base-unit weights in local storage."),

            ("Offline-First Mobile Synchronization & SQLite Local Storage",
             "Local data persistence, offline meal logging, and background server sync.",
             "Mobile apps must function reliably in low-connectivity gym or outdoor environments.",
             [
                 {"q": "How does Caloriv allow users to log meals without an internet connection?",
                  "a": "All daily meal logs, food databases, and calorie tallies are written immediately to a local SQLite database using React Native's SQLite library. Each record carries a `sync_status` flag ('SYNCED', 'PENDING_UPLOAD', 'PENDING_DELETE'). When network connectivity is restored, an asynchronous sync manager batches pending records and pushes them to the cloud backend via idempotent REST calls."},
                 {"q": "How do you handle conflict resolution if a user modifies their meal on two devices?",
                  "a": "We use a 'Last-Write-Wins' (LWW) strategy backed by UTC millisecond timestamps (`updated_at`). The record with the later timestamp overwrites the earlier record on the cloud server, and the resolved state syncs back to the client."}
             ],
             "In fitness tracking, offline access is essential. I architected Caloriv with an offline-first SQLite cache. Users can log meals, check daily macros, and view charts without internet access, with automated two-way synchronization occurring seamlessly whenever a network connection is detected."),

            ("Camera Integration, Image Preprocessing & Cloudinary Asset Optimization",
             "Device camera capture, client-side image compression, and cloud asset pipelines.",
             "Compressing images before mobile upload saves cellular data and prevents network timeout failures.",
             [
                 {"q": "How does Caloriv handle meal photo uploads efficiently over slow mobile networks?",
                  "a": "When a user captures a food photo, rather than uploading raw 12MB camera images, we use `expo-image-manipulator` to downsample the image resolution to a maximum 1080px width and compress it to JPEG format with 75% quality. This reduces file size to under 250KB before streaming the binary data to Cloudinary via authenticated upload signatures."},
                 {"q": "Why use Cloudinary CDN instead of saving food photos directly on the backend server?",
                  "a": "Storing images on application servers consumes expensive block storage and burdens the CPU with image resizing. Cloudinary automatically generates dynamic responsive thumbnails (`w_300,h_300,c_fill,f_auto,q_auto`), reducing mobile data usage by over 60% when rendering meal history grids."}
             ],
             "For visual food journaling in Caloriv, I built an image processing pipeline. The mobile client compresses raw camera captures to under 250KB before uploading them to Cloudinary CDN, ensuring lightning-fast meal logging even on restricted 3G/4G connections."),

            ("Mobile State Management & Performance Optimization with Zustand",
             "Lightweight global state, re-render minimization, and selector patterns.",
             "Zustand eliminates Redux boilerplate and prevents unnecessary component re-renders through targeted state selectors.",
             [
                 {"q": "Why choose Zustand over Redux or React Context for Caloriv's state management?",
                  "a": "Redux requires extensive boilerplate (actions, reducers, dispatchers), whereas React Context triggers re-renders across all consuming components whenever any state property updates. Zustand uses a minimalist hook-based store with automatic selector equality checks: components only re-render if their specifically subscribed state property changes."},
                 {"q": "How do you persist selected Zustand stores across mobile app restarts?",
                  "a": "We wrap the Zustand store configuration in `persist` middleware configured with `AsyncStorage` or `react-native-mmkv`. This serializes authentication tokens, user preferences, and today's logged meals to encrypted on-device storage with microsecond read latency on app launch."}
             ],
             "In Caloriv, I implemented global state management using Zustand. By employing atomic state selectors and persistent on-device storage, the app eliminates redundant React component re-renders and provides instant state restoration upon app launch.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "Caloriv",
            "repo_path": "D:\\Projects\\Caloriv",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }

    elif proj_type == 3:
        # Biometric Electronic Voting System (BEVM)
        topics = [
            ("Tamper-Evident Cryptographic Ledger & Chained SHA-256 Audit Hashes",
             "Chaining ballot records using sequential SHA-256 cryptographic hashes (H_i = SHA256(H_{i-1} + ballot_data)) to guarantee that retrospective tampering immediately breaks downstream hash validity.",
             "Sequential cryptographic hash chaining guarantees historical immutability. If any past ballot is modified, all descendant block hashes fail validation.",
             [
                 {"q": "How does the Biometric Electronic Voting System (BEVM) prevent retroactive ballot tampering?",
                  "a": "BEVM implements an append-only cryptographic ledger. Each cast vote record includes the SHA-256 hash of the immediately preceding ballot block alongside timestamp and voter choice data. Prior to tally publication, an audit verification script traverses the block sequence; modifying or inserting a single vote invalidates all subsequent hashes, making undetected tampering mathematically impossible."},
                 {"q": "How do you preserve voter ballot secrecy while maintaining an auditable cryptographic chain?",
                  "a": "Voter authentication (biometric match status) and ballot recording are strictly decoupled. When a citizen authenticates, their record in the `voters` table sets `has_voted = 1`. The ballot record is written to a separate `votes` table containing only encrypted candidate choice and hash links, with no foreign key or linkable identifier connecting voter identity to candidate preference."}
             ],
             "I engineered the Biometric Electronic Voting System (BEVM) as an air-gapped cryptographic voting platform in Python and SQLite. It combines biometric identity verification with a chained SHA-256 append-only audit ledger, guaranteeing that vote records cannot be altered or injected retroactively while strictly preserving voter ballot secrecy."),

            ("Symmetric Ballot Payload Encryption with Fernet AES-256 & Key Management",
             "Securing vote choices stored on disk using Fernet symmetric encryption (AES-128-CBC with PKCS7 padding and HMAC-SHA256 authentication) backed by air-gapped key storage.",
             "Fernet AES-256 provides both confidentiality and message integrity; without the physical `secret.key`, database files cannot be decrypted or inspected.",
             [
                 {"q": "Why use Fernet encryption rather than storing raw vote tallies in SQLite?",
                  "a": "In electronic voting, physical access to the polling terminal could allow malicious actors to inspect intermediate voting trends before polling closes. Storing ballot payloads encrypted with Fernet AES-256 ensures that even with direct file access to `voting_system.db`, candidate choices remain encrypted until the administrative decryption key is provided at election closing."},
                 {"q": "How is the cryptographic key managed during election cycles?",
                  "a": "The Fernet key (`secret.key`) is generated once by the Election Admin during terminal provisioning and stored with restricted filesystem permissions (chmod 600). It is decoupled from voter-facing interfaces and read into memory only during ballot encryption and final official tally publication."}
             ],
             "In BEVM, data confidentiality is enforced at rest. I implemented symmetric ballot payload encryption using Fernet AES-256 and HMAC verification. Even if polling hardware is physically intercepted, candidate choices cannot be viewed or manipulated without the administrative key."),

            ("Biometric Authentication Workflow & Zero-Knowledge Role Separation",
             "Enforcing strict administrative separation between election setup, voter authentication, and tally calculation.",
             "Role separation guarantees that polling booth operators cannot modify candidate rosters once an election commences.",
             [
                 {"q": "How does BEVM enforce role-based privilege separation between election officers and voters?",
                  "a": "BEVM establishes two distinct software modes: Admin Mode and Polling Mode. Admin Mode requires administrative credentials to configure candidates, register voter biometric hashes, and generate keys. Once an election is sealed, the system locks into Polling Mode where only biometric fingerprint verification and ballot casting are enabled."},
                 {"q": "What happens if a biometric sensor fails or misreads a citizen's fingerprint?",
                  "a": "The biometric verification module implements configurable matching threshold tolerances. If consecutive attempts fail, the terminal falls back to biometric administrator override requiring dual-authorization logging in `audit.log` before an alternate verification path is enabled."}
             ],
             "To prevent administrative overreach in electronic voting, I architected BEVM with strict role-based state machines. Terminal provisioning is isolated from voter polling modes, and all administrative overrides require dual-authorized cryptographic audit logging."),

            ("Atomic State Locking & SQLite Double-Vote Prevention",
             "Preventing duplicate voting attempts through atomic database transactions and strict state flag locking.",
             "Atomic SQLite transactions with `has_voted` flags guarantee that once a voter casts a ballot, duplicate attempts are rejected instantly.",
             [
                 {"q": "How does BEVM mathematically prevent a voter from casting multiple ballots?",
                  "a": "When a voter authenticates, the system opens an atomic SQLite transaction. It checks `SELECT has_voted FROM voters WHERE voter_id = ?`. If `has_voted == 0`, it executes the ballot insertion and updates `has_voted = 1` within the exact same transaction before committing. Any subsequent attempt immediately fails the pre-condition check and triggers a security alert."},
                 {"q": "How do you ensure power loss during ballot casting does not leave the database in an inconsistent state?",
                  "a": "SQLite's atomic commit protocols guarantee that if a power outage occurs mid-write, the transaction rolls back cleanly upon terminal reboot. Either both the ballot record and the `has_voted` flag persist together, or neither does, preventing orphaned votes or disenfranchised voters."}
             ],
             "Eliminating double-voting is the fundamental invariant of voting systems. In BEVM, I implemented atomic state locking in SQLite where biometric verification, ballot encryption, and voter status updates commit within a single atomic boundary, guaranteeing zero duplicate ballots."),

            ("Forensic Audit Verification & Ledger Consistency Traversal",
             "Algorithmic validation of the entire vote chain and audit logs prior to publishing election results.",
             "Automated ledger traversal recalculates all SHA-256 block hashes sequentially; a single altered bit halts tallying and flags corruption.",
             [
                 {"q": "How does the forensic verification algorithm validate ledger integrity in BEVM?",
                  "a": "The verification function queries all votes ordered by `block_id`. Starting with the genesis hash, it re-computes `expected_hash = SHA256(previous_hash + encrypted_payload + timestamp)`. If `expected_hash != current_block.hash` at any point, execution immediately halts, reporting the exact block ID of tampering and preventing fraudulent tally publication."},
                 {"q": "What information is captured in BEVM's immutable `audit.log`?",
                  "a": "Every system event (terminal boot, admin authentication, key generation, ballot cast, verification run) is written with ISO UTC timestamps and event classification. The log file is write-append-only and hashed alongside the database backup."}
             ],
             "Trust in voting technology requires verifiable proof. In BEVM, I authored a forensic verification engine that recalculates the cryptographic hash chain across all cast ballots prior to tally publication, providing mathematical proof of zero tampering."),

            ("Offline Polling Booth Architecture & Air-Gapped System Hardening",
             "Operating mission-critical voting platforms in completely air-gapped, zero-network environments.",
             "Air-gapped deployment eliminates remote network vulnerabilities, DDoS vectors, and cloud dependency entirely.",
             [
                 {"q": "Why design BEVM as an offline air-gapped application rather than a cloud-hosted web portal?",
                  "a": "Online internet voting platforms are vulnerable to DDoS attacks, DNS hijacking, credential stuffing, and remote zero-day exploits. Air-gapping the terminal eliminates remote attack vectors entirely. Physical terminal security combined with local cryptographic hashing provides far higher integrity than any cloud database can guarantee."},
                 {"q": "How are results aggregated from multiple air-gapped polling booths?",
                  "a": "Upon election closing, each terminal generates a cryptographically signed, encrypted export package on an authenticated hardware token. The central counting station validates the digital signature of each terminal before ingesting and summing the verified tallies."}
             ],
             "For mission-critical election integrity, I designed BEVM as a hardened, offline air-gapped system. By eliminating internet dependency and securing on-device SQLite databases with cryptographic hash chaining, the system provides rock-solid defense against remote tampering.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "Biometric Electronic Voting System (BEVM)",
            "repo_path": "D:\\Projects\\FINGERPINT VOTING SYSTEM",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }

    else:
        # CSMS (College Student Management System)
        topics = [
            ("Cloud-Native Educational ERP Architecture with FastAPI & Supabase PostgreSQL",
             "Architecting a multi-role educational ERP system submitted as Sarthak's BCA 5th Semester project under Asst. Prof. Nitin Mishra at VSICS (CSJMU Kanpur).",
             "FastAPI backend exposes domain routers (auth, students, attendance, grades, hod) communicating with Supabase Cloud PostgreSQL 15+.",
             [
                 {"q": "Walk me through the architecture and purpose of your College Student Management System (CSMS).",
                  "a": "I developed CSMS as a cloud-native Educational ERP for my BCA 5th Semester project under Prof. Nitin Mishra at VSICS, CSJMU. Built with FastAPI and Supabase Cloud PostgreSQL with a lightweight Vanilla JS frontend, it automates student lifecycle management across four roles: HOD, Section Incharge, Faculty, and Students. It covers attendance tracking with automated <75% shortage alerts, internal test mark entry with auto-grade calculation, semester fee balance monitoring, and official HOD circular distribution."},
                 {"q": "Why did you use FastAPI with Supabase PostgreSQL instead of Django or Flask?",
                  "a": "FastAPI provides native asynchronous route execution with automatic Pydantic request validation and self-generating Swagger documentation at `/docs`. Coupled with Supabase PostgreSQL, it provided enterprise-grade ACID transactions without the heavy ORM overhead of Django, making it ideal for fast, zero-downtime deployment on Render via Blueprint (`render.yaml`)."}
             ],
             "I developed the College Student Management System (CSMS) for my BCA 5th Semester project at VSICS Kanpur. Using FastAPI and Supabase PostgreSQL, I engineered an educational ERP featuring multi-role authentication for HOD, faculty, and students, real-time attendance tracking with shortage alerts, automated grade derivation, and semester fee accounting."),

            ("Multi-Role Authentication & Bcrypt Password Security in CSMS",
             "Implementing role-based access for HOD, Section Incharges, Faculty, and Students with bcrypt hashing.",
             "Passwords are never stored in plaintext; `bcrypt` salt rounds ensure cryptographic resistance against dictionary attacks.",
             [
                 {"q": "How is authentication handled in CSMS across different academic roles?",
                  "a": "In `backend/routers/auth.py`, the login endpoint authenticates both faculty/administrators via email from the `admins` table and students via their University Enrollment Number (e.g. `CSJMA24000004738`) from the `students` table. Stored passwords are salted and hashed using bcrypt. On successful authentication, the response payload returns the authenticated role and session context, steering the client to either `admin-dashboard.html` or `student-dashboard.html`."},
                 {"q": "How do you protect sensitive student academic data against unauthorized tampering?",
                  "a": "Administrative routes (`/api/students`, `/api/hod/*`) enforce strict server-side role validation checking the `role` field ('HOD', 'Section Incharge', 'Faculty'). Grade entry and fee reconciliation endpoints reject requests originating from unverified student sessions."}
             ],
             "In CSMS, security and role segregation were critical. I implemented a dual-lookup authentication system supporting both HOD email and University Enrollment Number credentials. By hashing all credentials with bcrypt and validating roles on every protected endpoint, the system guarantees that students cannot tamper with grade rosters or fee balances."),

            ("Relational Database Schema Design & Attendance Shortage Engine",
             "Designing normalized 3NF tables in PostgreSQL and calculating aggregate attendance percentage thresholds.",
             "Attendance threshold formula: Attendance % = (Total Present Days / Total Recorded Class Days) * 100; triggered alerts when < 75%.",
             [
                 {"q": "Explain the relational schema design for attendance and grade tracking in CSMS.",
                  "a": "In `schema.sql`, the schema utilizes PostgreSQL with UUID primary keys. The `attendance` table maintains a compound unique constraint `(student_id, record_date)` to prevent duplicate daily check-ins. The attendance aggregation query performs a count of 'Present' vs total scheduled sessions per course, flagging any student falling below the mandatory university 75% threshold for detention alerts."},
                 {"q": "How are foreign keys and referential integrity configured in CSMS?",
                  "a": "Child tables (`attendance`, `grades`, `fees`, `test_marks`) reference the parent `students` table with `ON DELETE CASCADE`. This ensures that when a student is archived or deleted from the directory, orphaned records are automatically cleaned up, maintaining zero orphaned rows in PostgreSQL."}
             ],
             "I designed the relational PostgreSQL schema in schema.sql with strict constraints to ensure academic data integrity. The system features a unique constraint preventing duplicate daily attendance and an automated aggregation query that calculates attendance percentages, immediately surfacing students below the university's 75% requirement to the HOD."),

            ("Academic Grading Engine & Semester Fee Ledger Management",
             "Automating grade derivation (A, B, C, D, F) from composite scores and tracking Paid, Pending, and Partial fee states.",
             "Composite scores translate deterministically: >=90% -> A, 80-89% -> B, 70-79% -> C, 60-69% -> D, <60% -> F.",
             [
                 {"q": "How does the academic grading engine calculate student performance in CSMS?",
                  "a": "In `backend/routers/grades.py`, scores across class tests, assignments, and mid-terms from `test_marks` are aggregated into a composite percentage. A deterministic evaluation function maps numerical percentages to academic grades (A through F). Results are stored in the `grades` table with a unique constraint on `(student_id, course_id)`, preventing contradictory grade entries."},
                 {"q": "How does the semester fee management system handle partial payments?",
                  "a": "The `fees` table tracks `total_amount`, `amount_paid`, and `status` ('Paid', 'Pending', 'Partial') constrained across `(student_id, semester)`. When a payment is recorded via `/api/hod/fees`, the system calculates `total_amount - amount_paid`. If the balance is zero, the status transitions to 'Paid'; if positive, it is marked 'Partial', enabling the HOD to generate instant fee-defaulter rosters."}
             ],
             "In CSMS, I built an automated academic grading engine and semester fee ledger. The grading module aggregates continuous test scores into deterministic letter grades, while the fee tracker dynamically maintains pending balances across semesters, giving faculty instantaneous visibility into academic performance and fee compliance."),

            ("HOD Notice Board, Full-Stack Integration & Render Cloud Deployment",
             "Delivering a responsive vanilla frontend connected to FastAPI and deploying via Render Blueprint.",
             "Render Blueprint (`render.yaml`) provides Infrastructure-as-Code for auto-provisioning FastAPI web services.",
             [
                 {"q": "Why did you build the CSMS frontend with Vanilla HTML/CSS/JS instead of React or Vue?",
                  "a": "For an internal college administration portal, zero build overhead and instant browser loading on lab computers with low memory were primary requirements. Vanilla ES6+ JavaScript with native Fetch API consumes less than 20MB of RAM, requires no Webpack/Babel compilation steps, and provides instant cold-start times on any institutional device."},
                 {"q": "How is CSMS configured for cloud deployment on Render and Vercel?",
                  "a": "The repository includes `render.yaml` defining a Python 3.10 web service running Uvicorn with environment injection for `SUPABASE_URL` and `SUPABASE_KEY`. The frontend is served statically with configured CORS middleware on the FastAPI backend, enabling seamless cross-origin communication between the deployed client and API."}
             ],
             "To ensure CSMS could run effortlessly across legacy college lab computers, I built a zero-dependency Vanilla ES6+ frontend backed by native Fetch APIs. I packaged the application with Render Blueprint infrastructure-as-code, enabling one-click cloud deployment with live Swagger API docs.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "College Student Management System (CSMS)",
            "repo_path": "D:\\Projects\\College Student Management System",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }

