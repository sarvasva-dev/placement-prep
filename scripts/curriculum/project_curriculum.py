"""
Curriculum for Project Preparation across all 30 days.
Aligned strictly with Sarthak's real technical stack, projects, and truthful defense:
- BulkBeat TV (Python AsyncIO, Real-Time Ingestion, 20+ Rule Engine, Telegram Bot, SQLite WAL, Linux VPS, ₹1.11L Revenue)
- College Student Management System - CSMS (BCA 5th Sem Capstone, FastAPI, PostgreSQL, 4-tier RBAC, Attendance <75% Alert, Grading, Render)
- SmartGalla (Hyperlocal Kirana Store Portal, Python, PostgreSQL, HTML5/CSS3/JavaScript Frontend, 4-5 Shops Pilot in Kanpur)
- DocRoute (Document Text Extraction, PyMuPDF Vector Text, Tesseract OCR Fallback for Scanned Pages, Structured JSON Output)
- Django Backend & Relational SQL Architecture (Django MVT, ORM & Migrations, Views, REST APIs, PostgreSQL vs SQLite, Normalization & ACID)
"""

def get_project_for_day(day):
    # Rotation cycle of 5 authentic engineering tracks
    proj_type = (day - 1) % 5
    
    if proj_type == 0:
        # BulkBeat TV
        topics = [
            ("Real-Time Financial Media Ingestion in Python (AsyncIO & Requests)",
             "How an asynchronous event loop fetches multiple financial feeds simultaneously without blocking execution.",
             "Python AsyncIO enables cooperative multitasking on a single thread. When awaiting network I/O, control yields to other tasks.",
             [
                 {"q": "Walk me through the architecture and purpose of BulkBeat TV.",
                  "a": "BulkBeat TV is a real-time financial market intelligence and alert platform I built in Python. It scans 5+ live exchange feeds and corporate announcement sources, applies a 20+ keyword rule filtering engine to separate actionable news from market noise, and broadcasts instant alerts to subscribers via a Telegram Bot. It scaled to 6,000+ active users and generated ₹1.11 Lakhs in subscription revenue within months."},
                 {"q": "Why did you use Python AsyncIO instead of traditional multithreading for feed ingestion?",
                  "a": "Feed ingestion is predominantly I/O-bound (waiting on network responses from exchange endpoints). In standard Python (CPython), the Global Interpreter Lock (GIL) limits multithreading CPU execution. AsyncIO uses a single-threaded cooperative event loop where coroutines yield CPU control while waiting for network responses, allowing hundreds of concurrent network calls with negligible memory footprint on a low-cost 1GB RAM Linux VPS."}
             ],
             "I built BulkBeat TV to solve the problem of market noise for active retail stock market traders. Using Python AsyncIO, the platform concurrently polls 5+ financial announcement feeds. Instead of overwhelming traders with hundreds of routine filings, the system processes disclosures in real time and sends filtered alerts via Telegram within seconds."),
            
            ("Deterministic 20+ Keyword Rule Filtering Engine",
             "How rule-based keyword matching identifies high-impact corporate announcements while eliminating 90%+ market noise.",
             "Deterministic keyword scoring provides predictable, zero-latency classification without the cost, latency, or hallucination risks of cloud LLMs.",
             [
                 {"q": "How does the 20+ rule filtering engine in BulkBeat TV work?",
                  "a": "In `rules.txt` and `filter_news.py`, we defined 20+ deterministic pattern rules categorizing disclosures into high-priority buckets: corporate actions (stock splits, bonus issues, dividends), major business contracts/orders (e.g. order value > ₹50 Cr), quarterly financial results (revenue spikes, profit turnarounds), and regulatory actions. Each incoming announcement is tokenized and matched against regex patterns. If a threshold match occurs, the announcement is tagged with urgency and forwarded for broadcasting."},
                 {"q": "Why choose rule-based filtering over a Large Language Model (LLM) for live market alerts?",
                  "a": "For intraday market announcements, speed and cost are critical. LLM API calls introduce 1 to 3 seconds of network latency and token costs that scale linearly with traffic. Our deterministic regex rule engine executes in under 2 milliseconds on a local CPU, costs zero extra API fees, and never hallucinates stock symbols or financial figures."}
             ],
             "In financial markets, speed is an edge. In BulkBeat TV, I built a deterministic 20+ keyword rule engine that inspects incoming corporate filings in under 2ms. It filters out routine administrative filings and flags high-impact corporate catalysts like order wins and stock splits, ensuring traders receive only actionable news."),

            ("Automated Telegram Bot Alerts & Broadcast Architecture",
             "Connecting backend pipelines to end users via Telegram Bot API with instant delivery and rate-limit compliance.",
             "Telegram Bot API offers reliable push notifications with Markdown formatting and inline keyboard buttons, eliminating the need to build a native mobile app.",
             [
                 {"q": "How does BulkBeat TV deliver alerts to subscribers via Telegram?",
                  "a": "We use the Telegram Bot API (`send_message` endpoint). When an announcement passes the rule filter, a message formatter converts the raw disclosure into a clean, formatted Telegram card with company name, NSE symbol, category badge, disclosure excerpt, and source link. The broadcast worker loops through active paid subscriber chat IDs stored in our database, with queue pacing to respect Telegram's rate limit of 30 messages per second."},
                 {"q": "How did you manage subscriber onboarding and chat ID linking?",
                  "a": "Subscribers start the bot with `/start`, which triggers a welcome handshake capturing their unique Telegram `chat_id` and username into SQLite. Once payment is confirmed via Razorpay, their subscription status is marked active with an expiry timestamp, authorizing them to receive automated broadcast alerts."}
             ],
             "To reach traders instantly without requiring them to install a separate custom mobile app, I integrated the Telegram Bot API. BulkBeat TV formats filtered disclosures into readable summary cards and broadcasts them to over 6,000 active subscribers, pacing broadcasts to comply with Telegram's API rate limits."),

            ("SQLite Database Concurrency & Write-Ahead Logging (WAL Mode)",
             "Managing concurrent read and write operations in SQLite for user subscriptions and alert logs on a single server.",
             "`PRAGMA journal_mode=WAL;` allows readers to read from the database without blocking writers, and writers do not block readers.",
             [
                 {"q": "Why use SQLite for BulkBeat TV instead of a larger database like PostgreSQL or MySQL?",
                  "a": "BulkBeat TV was hosted on a cost-effective 1GB RAM Ubuntu VPS. SQLite is an embedded database that runs in-process with zero network overhead, consuming almost no memory. Because the workload consisted of frequent reads (checking user subscription status) and sequential writes (logging processed news items), SQLite was completely sufficient and significantly simpler to maintain with zero separate database daemon to crash."},
                 {"q": "What is WAL mode in SQLite and why did you enable it?",
                  "a": "By default, SQLite uses rollback journal mode where any write locks the entire database file, preventing concurrent reads. By running `PRAGMA journal_mode=WAL;` (Write-Ahead Logging), new writes are appended to a separate `-wal` file while readers continue reading from the original database. This eliminates reader-writer lock contention and prevents 'database is locked' errors during high news volume."}
             ],
             "To maximize server efficiency on our 1GB VPS, I utilized SQLite with Write-Ahead Logging (WAL mode). WAL mode separates read and write operations, allowing subscriber authentication checks to execute without being blocked by background news logging, ensuring zero database lockouts during market peak hours."),

            ("Ubuntu Linux VPS Deployment & Systemd Process Supervision",
             "Deploying Python backend scripts on an Ubuntu server, configuring systemd services, and monitoring logs.",
             "`systemd` manages system services, automatically restarting scripts if they crash and capturing stdout/stderr in `journalctl`.",
             [
                 {"q": "How did you deploy and keep BulkBeat TV running 24/7 on a Linux server?",
                  "a": "I provisioned an Ubuntu Linux VPS, set up a non-root deployment user, and installed Python and virtual environments. To run the background ingestion worker (`sync_worker.py`) and the bot service (`admin_bot_main.py`), I created custom `systemd` unit files (e.g. `/etc/systemd/system/bulkbeat.service`) with `Restart=always` and `RestartSec=5s`. This ensured that if a script encountered an unhandled exception or the server rebooted, systemd automatically restarted the processes."},
                 {"q": "How did you monitor server health and debug issues in production?",
                  "a": "I used `journalctl -u bulkbeat.service -f` to monitor live application logs in real time. In addition, I wrote Python logging handlers that write timestamped logs to rotating log files, preventing disk space exhaustion, and configured an admin alert script that pinged my personal Telegram account if consecutive fetch errors exceeded a safe threshold."}
             ],
             "I managed the complete production lifecycle of BulkBeat TV on an Ubuntu Linux VPS. By authoring custom systemd service units with auto-restart policies and configuring log rotation, I maintained 99.8% uptime with zero orphaned background processes."),

            ("Commercial Traction: Scaling to 6,000+ Users & ₹1.11 Lakhs Revenue",
             "Validating real-world product-market fit, subscription payment integration, and engineering under real user load.",
             "Real traction requires reliable automated billing, quick customer support, and system stability during market trading hours (9:15 AM - 3:30 PM IST).",
             [
                 {"q": "How did BulkBeat TV achieve ₹1.11 Lakhs in revenue and 6,000+ active users?",
                  "a": "We targeted active retail traders who trade corporate action breakouts on NSE. By offering a free 7-day trial through our Telegram bot, we allowed users to experience the speed of the alerts firsthand. Traders found immediate value because our alerts arrived before mainstream financial news portals published articles. We converted trial users into paid subscribers at affordable monthly pricing, collecting payments through Razorpay payment links."},
                 {"q": "What was the biggest technical lesson you learned from running BulkBeat TV in production?",
                  "a": "The biggest lesson was defensive engineering around third-party network failures. During volatile market events (budget day, election results), exchange endpoints frequently rate-limit, timeout, or return 502 Bad Gateway responses. I implemented exponential backoff retries, request timeouts, and error isolation so that a failure in one news feed never crashed the entire alert broadcast pipeline."}
             ],
             "BulkBeat TV was my most commercially successful project to date. I validated market demand by growing the user base to over 6,000 active subscribers and generating ₹1.11 Lakhs in subscription revenue within months. Running a live financial platform taught me the importance of fault tolerance, rate limiting, and reliable payment reconciliation.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "BulkBeat TV",
            "repo_path": "D:\\Projects\\nse2",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }

    elif proj_type == 1:
        # College Student Management System (CSMS)
        topics = [
            ("Cloud-Native Educational ERP Architecture with FastAPI & PostgreSQL",
             "Architecting an academic management portal submitted as Sarthak's BCA 5th Semester project under Asst. Prof. Nitin Mishra at VSICS (CSJMU Kanpur).",
             "FastAPI backend exposes modular REST routers communicating with PostgreSQL, providing automated interactive OpenAPI documentation at `/docs`.",
             [
                 {"q": "Walk me through the architecture and purpose of your College Student Management System (CSMS).",
                  "a": "I developed CSMS as a full-stack educational ERP portal for my BCA 5th Semester Capstone Project under Prof. Nitin Mishra at VSICS Kanpur. Built with Python (FastAPI), PostgreSQL, and a clean HTML5/CSS3/JavaScript frontend, it digitizes academic operations across 4 user roles: HOD, Section Incharge, Faculty, and Students. Key features include daily attendance tracking with automated <75% shortage detection, internal test mark entry with automatic letter grade calculation, semester fee balance tracking, and official HOD notices."},
                 {"q": "Why did you choose FastAPI for CSMS instead of Flask or Django?",
                  "a": "FastAPI provides native asynchronous request handling, automatic request data validation through Pydantic models, and auto-generated interactive Swagger API documentation at `/docs`. It allowed clean separation of domain routers (`auth.py`, `students.py`, `attendance.py`, `grades.py`) with minimal boilerplate code, making API development and testing straightforward."}
             ],
             "I developed the College Student Management System (CSMS) for my BCA 5th Semester project at VSICS Kanpur. Using FastAPI and PostgreSQL, I built an educational ERP featuring multi-role access for HOD, faculty, and students, automated attendance shortage alerts, student grade calculation, and semester fee accounting."),

            ("Multi-Role Authentication & Bcrypt Password Security",
             "Implementing role-based access for HOD, Section Incharges, Faculty, and Students with bcrypt password hashing.",
             "Passwords must never be stored in plaintext. `bcrypt` adds a random salt and applies repeated cryptographic hashing to prevent rainbow table attacks.",
             [
                 {"q": "How is authentication handled in CSMS across different academic roles?",
                  "a": "In `backend/routers/auth.py`, the login system supports dual authentication: faculty and administrators log in using their college email address, while students log in using their University Enrollment Number (e.g. `CSJMA24000004738`). All stored passwords are salted and hashed using the `bcrypt` library. On successful login, the API returns the user's role and profile data to guide the frontend to the appropriate dashboard."},
                 {"q": "How do you ensure students cannot access administrative endpoints?",
                  "a": "Administrative routes (like creating student records, modifying fee balances, or posting HOD circulars) require role verification in FastAPI route dependencies. If a student account attempts to call an admin endpoint, the API immediately rejects the request with HTTP 403 Forbidden."}
             ],
             "Security and role segregation were essential in CSMS. I implemented dual-credential authentication supporting both staff emails and student enrollment numbers. By hashing all passwords with bcrypt and enforcing role checks on protected endpoints, the system prevents unauthorized access to student records and fee data."),

            ("Relational Database Schema Design & Constraints in PostgreSQL",
             "Designing normalized 3NF tables in PostgreSQL with primary keys, foreign keys, and unique constraints to prevent data duplication.",
             "A composite unique constraint `UNIQUE (student_id, record_date)` guarantees that a student cannot have more than one attendance record per calendar day.",
             [
                 {"q": "Explain the relational schema design for attendance and student records in CSMS.",
                  "a": "In `schema.sql`, we designed normalized tables for `admins`, `students`, `courses`, `attendance`, `grades`, and `fees`. The `attendance` table includes `student_id` (foreign key referencing `students`), `record_date`, and `status` ('Present' or 'Absent'). We enforced a composite UNIQUE constraint on `(student_id, record_date)` at the database level, making it physically impossible for duplicate attendance to be logged on the same date."},
                 {"q": "How did you maintain referential integrity between parent and child tables?",
                  "a": "Child tables like `attendance`, `grades`, and `fees` link to the `students` table via foreign keys configured with `ON DELETE CASCADE`. If a student record is removed, all corresponding attendance and fee history are automatically purged, preventing orphaned records and maintaining database consistency."}
             ],
             "I designed the relational PostgreSQL schema in schema.sql following 3NF normalization rules. By enforcing foreign key constraints and composite unique indexes, the database guarantees that daily attendance entries cannot be duplicated and student records remain referentially consistent."),

            ("Attendance Tracking & Automated <75% Shortage Detection",
             "Calculating attendance percentages and identifying students at risk of semester detention.",
             "Attendance Percentage = (Total Present Days / Total Recorded Class Days) * 100. Any student below 75% is flagged for detention risk.",
             [
                 {"q": "How does the attendance shortage detection logic work in CSMS?",
                  "a": "In `backend/routers/attendance.py`, when an administrator or faculty requests the attendance summary, the backend executes an aggregation query counting 'Present' records vs total class sessions for that course and section. The system computes `(present_count / total_classes) * 100`. If the calculated percentage is less than 75%, the API response marks `is_shortage = true`, and the dashboard highlights the student row in red with a warning icon."},
                 {"q": "Can students check their own attendance percentage?",
                  "a": "Yes. When a student logs into `student-dashboard.html`, the frontend queries `/api/attendance/my-summary`. It displays their current subject-wise attendance percentage, total classes held, classes attended, and indicates how many consecutive upcoming classes they must attend to cross the 75% university eligibility requirement."}
             ],
             "College attendance rules require a minimum of 75% attendance to sit for university semester examinations. In CSMS, I implemented an automated aggregation engine that computes each student's current percentage and automatically flags students below 75%, allowing faculty and HODs to generate shortage warning rosters with a single click."),

            ("Academic Grading Engine & Semester Fee Ledger Management",
             "Automating letter grade calculation from continuous test marks and tracking Paid, Pending, and Partial fee states.",
             "Grade mapping: >=90% -> A, 80-89% -> B, 70-79% -> C, 60-69% -> D, <60% -> F. Fee balance = Total Fee - Paid Fee.",
             [
                 {"q": "How does the academic grading engine calculate student performance in CSMS?",
                  "a": "Faculty enter internal test marks and assignment scores in `/api/grades/entry`. The backend aggregates marks into a percentage score and deterministically maps it to letter grades (A, B, C, D, or F). Results are stored in the `grades` table with a unique constraint on `(student_id, course_id, semester)`, preventing duplicate conflicting grade entries."},
                 {"q": "How does the semester fee management module handle partial payments?",
                  "a": "The `fees` table stores `total_amount`, `amount_paid`, and `status`. When an admin logs a fee payment, the system computes `balance = total_amount - amount_paid`. If balance is 0, status is set to 'Paid'; if amount_paid > 0 but balance > 0, status is 'Partial'; if amount_paid is 0, status is 'Pending'. This enables the college accounts desk to filter all fee-defaulter students in seconds."}
             ],
             "In CSMS, I built an automated grading module and semester fee ledger. The grading engine calculates letter grades from continuous internal marks, while the fee ledger maintains dynamic Paid, Partial, and Pending payment balances, giving faculty and administrators instant oversight of student academic and financial status."),

            ("Vanilla HTML/CSS/JavaScript Frontend & Render Cloud Deployment",
             "Building a responsive zero-dependency frontend and deploying the FastAPI service using Render Blueprint.",
             "Vanilla JavaScript using native `fetch()` provides instant page loading with zero build steps, ideal for legacy college lab computers.",
             [
                 {"q": "Why did you build the CSMS frontend with Vanilla HTML, CSS, and JavaScript?",
                  "a": "For a college internal management portal, fast load times and compatibility with older college lab computers were paramount. Vanilla ES6+ JavaScript with native Fetch API requires no build tools (no Webpack, Vite, or npm bundle dependencies), loads in milliseconds, uses minimal memory, and is completely cross-browser compatible."},
                 {"q": "How is CSMS configured for cloud deployment on Render?",
                  "a": "The repository includes a `render.yaml` Blueprint file defining a Python 3 web service running `uvicorn main:app --host 0.0.0.0 --port 10000`. Database connection strings are securely passed via environment variables, and FastAPI's CORS middleware (`CORSMiddleware`) is configured to allow requests from the frontend domain."}
             ],
             "To ensure CSMS could run smoothly on any college desktop without requiring complex build setups, I built a zero-dependency Vanilla HTML/CSS/JavaScript frontend communicating with our FastAPI REST endpoints. I deployed the backend to Render cloud with automated environment configuration and live Swagger API documentation.")
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

    elif proj_type == 2:
        # SmartGalla
        topics = [
            ("Hyperlocal Kirana Store Problem Statement & Architecture",
             "Understanding the challenges of traditional corner grocery stores and how a lightweight digital portal helps them.",
             "Small local Kirana shops need simple, fast order taking without complicated enterprise software or expensive POS hardware.",
             [
                 {"q": "What problem does SmartGalla solve, and what is its architecture?",
                  "a": "SmartGalla was built to help small neighbourhood Kirana grocery stores in Kanpur digitize their product catalogs and receive customer orders online. Built with a Python backend, PostgreSQL database, and a clean HTML5/CSS3/JavaScript web interface, it allowed local shopkeepers to list their daily grocery items, track stock quantities, and view incoming customer orders in real time."},
                 {"q": "How does SmartGalla differ from large quick-commerce platforms like Blinkit or Zepto?",
                  "a": "Quick-commerce platforms rely on expensive dark stores and high commission fees (15-25%) that local corner stores cannot afford. SmartGalla was designed as a direct-to-merchant tool with zero middleman commissions, allowing local customers to place orders directly with their neighbourhood store for home delivery or counter pickup."}
             ],
             "I developed SmartGalla to empower traditional Kirana grocery store owners. Using Python, PostgreSQL, and JavaScript, I built an intuitive store management portal where local shopkeepers could list items, update prices, and receive customer orders directly without paying heavy commissions to aggregator platforms."),

            ("Product Catalog & Inventory Schema Design in PostgreSQL",
             "Structuring relational tables for store categories, product SKUs, prices, and stock counts.",
             "Normalized schema with `stores`, `categories`, `products`, and `inventory` ensures accurate pricing and prevents inconsistent item names.",
             [
                 {"q": "Explain the database schema for product catalog management in SmartGalla.",
                  "a": "The schema in PostgreSQL includes a `stores` table for merchant profiles, `categories` for grouping items (e.g. Atta & Flours, Dairy, Spices, Snacks), and `products` storing item title, brand, description, and base price. An `inventory` table links `store_id` and `product_id` with `stock_quantity` and `is_available` flags, allowing merchants to toggle item availability with a single click when stock runs out."},
                 {"q": "How do you handle unit variations for grocery items (e.g., 500g vs 1kg)?",
                  "a": "We created a `product_variants` table referencing parent `product_id` with `unit` (g, kg, ml, L, piece), `variant_label`, and `variant_price`. When a customer adds an item to cart, the order references the specific variant ID, ensuring exact pricing and inventory deduction."}
             ],
             "In grocery retail, inventory accuracy is critical. In SmartGalla, I designed a normalized PostgreSQL database schema supporting product categories and multi-unit variations (like 500g vs 1kg packs). Merchants can toggle item availability instantly, preventing customers from ordering out-of-stock items."),

            ("Shopping Cart, Order Placement & Cash on Delivery (COD) Workflow",
             "Managing customer carts, order states (Placed, Processing, Delivered, Cancelled), and cash collection.",
             "In Indian tier-2 cities, over 80% of local grocery transactions are settled in Cash on Delivery (COD).",
             [
                 {"q": "How does the ordering and checkout process work in SmartGalla?",
                  "a": "Customers browse the store catalog, add grocery items to their session cart, and provide their delivery address and phone number at checkout. When the order is placed, an `orders` record is created with status 'PENDING_CONFIRMATION' and payment method 'COD'. The shopkeeper's dashboard receives an instant order card showing item breakdown, total amount, and customer address, with buttons to 'Accept Order' and 'Mark Delivered'."},
                 {"q": "How do you ensure data integrity during order checkout?",
                  "a": "Order creation executes inside an atomic database transaction. The system inserts the order record, creates line items in `order_items`, and updates available inventory counts within the same transaction. If any step fails, the entire transaction rolls back, preventing orphaned orders or incorrect stock counts."}
             ],
             "Cash on Delivery remains the dominant payment method for Indian grocery shopping. In SmartGalla, I engineered a streamlined checkout workflow with atomic database transactions. Shopkeepers receive instant order notifications on their dashboard with complete line-item breakdowns and delivery details."),

            ("Real-World Pilot with 4–5 Kanpur Kirana Stores",
             "Deploying the software into live retail environments and gathering firsthand user feedback from shopkeepers.",
             "Software in a lab often behaves differently than in a noisy, fast-paced retail shop with busy shopkeepers.",
             [
                 {"q": "Tell me about your experience piloting SmartGalla with real grocery stores.",
                  "a": "To validate whether local merchants would adopt the tool, I approached 4–5 local Kirana grocery shops in Kanpur and set up their digital catalogs with their most popular 50-100 items. I observed how the shopkeepers interacted with the dashboard during live business hours, monitored order fulfillment workflows, and gathered direct feedback on usability."},
                 {"q": "What did the shopkeepers like most about the platform?",
                  "a": "Shopkeepers appreciated having a clean digital link they could share on WhatsApp with regular customers, which reduced time spent taking orders over manual phone calls or handwritten paper chits. They also liked the clear daily sales summary showing total orders and cash to be collected."}
             ],
             "I did not just build SmartGalla in isolation; I took it into the real world. I piloted the software across 4–5 local Kirana stores in Kanpur, setting up their catalogs and observing how merchants handled orders during busy retail hours. This gave me invaluable insights into real user behavior."),

            ("Merchant Adoption Challenges & Operational Friction",
             "Analyzing the human and operational bottlenecks in local retail digitization.",
             "Small merchants operate under high counter rush; manual data entry during peak rush hours creates operational friction.",
             [
                 {"q": "What were the biggest challenges local Kirana owners faced while using SmartGalla?",
                  "a": "The primary bottleneck was real-time inventory synchronization. Local Kirana stores have constant walk-in counter footfall. If a walk-in customer buys the last packet of biscuits, the shopkeeper often forgets to update the web portal immediately. When an online customer subsequently orders that item, it leads to fulfillment cancellations. Kirana owners simply do not have dedicated staff for manual software entry during rush hours."},
                 {"q": "How could this inventory sync issue be solved in the future?",
                  "a": "Potential solutions include barcode scanner integration at the cash counter that updates online stock simultaneously upon billing, or an automated daily inventory checklist prompt before opening hours."}
             ],
             "Piloting with real merchants taught me that the biggest barrier to software adoption is operational friction, not just technical features. Local grocery store owners are busy handling counter walk-ins and often forget manual inventory updates, leading to fulfillment delays."),

            ("Infrastructure Cost Analysis & Product Sunset Decision",
             "Evaluating the economic viability of cloud hosting versus merchant willingness to pay, leading to a disciplined sunset.",
             "Engineering maturity includes knowing when to sunset a project when server and database hosting costs exceed business revenue.",
             [
                 {"q": "Why was SmartGalla discontinued after the initial pilot?",
                  "a": "After testing with 4–5 shops for several weeks, we analyzed the financial unit economics. Running cloud databases, application hosting, and SSL infrastructure incurred ongoing monthly server costs. However, small corner Kirana shops operating on thin 5-10% retail margins were hesitant to pay a monthly SaaS subscription fee (e.g. ₹500–₹1,000/month). Because the projected revenue could not sustain the hosting infrastructure costs, I made the disciplined engineering and business decision to sunset the live platform."},
                 {"q": "What was your main takeaway from the SmartGalla project?",
                  "a": "It taught me that building good software is only half the battle; economic viability and product-market fit are equally crucial. I gained deep practical experience in database schema design, atomic transaction management, and interacting with non-technical end users, which made me a far more pragmatic and mature engineer."}
             ],
             "SmartGalla was a crucial learning experience in practical engineering and business reality. When our pilot showed that merchant willingness to pay could not offset cloud database and server hosting expenses, I responsibly sunset the project. This experience taught me to always consider cost-to-value ratios when designing software.")
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

    elif proj_type == 3:
        # DocRoute & Document Text Extraction
        topics = [
            ("Document Processing Pipeline & Python Extraction Tools",
             "Overview of document extraction: why organizations need automated text extraction from invoices, resumes, and reports.",
             "Digital PDFs contain direct vector text streams, whereas scanned PDFs are images that require Optical Character Recognition (OCR).",
             [
                 {"q": "What is DocRoute and what problem does it address?",
                  "a": "DocRoute is a modular Python document processing framework I am developing to extract clean, structured text from diverse PDF documents. In real-world enterprise workflows, incoming PDFs vary widely: some are digital native PDFs with selectable text, while others are scanned photo documents. DocRoute establishes a pipeline that extracts digital text directly when available and falls back to OCR only when necessary."},
                 {"q": "Why not use OCR on every single page by default?",
                  "a": "OCR is computationally expensive and slow. Running OCR on a single high-resolution page can take 1.5 to 3 seconds on a CPU, whereas native digital text extraction via PyMuPDF takes less than 20 milliseconds per page (over 100x faster) and produces 100% accurate text without character recognition misreadings."}
             ],
             "I am building DocRoute to solve the challenge of parsing heterogeneous PDF documents efficiently. Instead of treating every PDF as an image, DocRoute inspects document streams to extract digital text instantly, reserving OCR only for scanned pages to optimize speed and resource usage."),

            ("High-Speed Digital Text Extraction with PyMuPDF",
             "Using PyMuPDF (fitz) to extract text, bounding boxes, and document metadata from digital vector PDFs.",
             "PyMuPDF is built on the high-performance MuPDF C rendering engine, making it one of the fastest Python PDF libraries available.",
             [
                 {"q": "How does PyMuPDF extract text from a digital PDF?",
                  "a": "In Python, we import `fitz` (PyMuPDF) and open the document via `doc = fitz.open(file_path)`. We iterate through each `page` and call `page.get_text('text')` or `page.get_text('blocks')`. PyMuPDF parses the PDF's internal font mappings and character stream tables directly from the file structure, returning clean Unicode text without rendering images."},
                 {"q": "How can you distinguish between a digital PDF page and a scanned image page?",
                  "a": "When we call `page.get_text().strip()`, a digital page returns hundreds of readable text characters. If a page contains a full-page image and returns zero or fewer than 20 extracted characters, the system flags the page as a scanned image and triggers the OCR fallback routine."}
             ],
             "In DocRoute, I utilize PyMuPDF for native vector text parsing. By directly reading internal font encoding streams, it extracts text in milliseconds per page, and detects whether a page is digital or a scanned image based on character density."),

            ("Scanned Document OCR Fallback with Tesseract",
             "Integrating Tesseract OCR (`pytesseract`) to recognize printed text from scanned PDF pages and images.",
             "Tesseract is an open-source OCR engine developed by HP and maintained by Google that identifies characters from raster images.",
             [
                 {"q": "How does the OCR fallback pipeline work in DocRoute?",
                  "a": "When a page is identified as scanned, PyMuPDF renders the page to a high-resolution pixmap image (e.g. 300 DPI) using `page.get_pixmap(dpi=300)`. The image bytes are passed to `pytesseract.image_to_string()`, which performs character recognition and returns the recognized text. This ensures that even scanned physical papers are successfully transcribed."},
                 {"q": "What happens if a document contains mixed pages (some digital, some scanned)?",
                  "a": "DocRoute processes documents page-by-page. Digital pages are extracted instantly with PyMuPDF, while only the specific scanned pages invoke the OCR worker. The outputs are reassembled in original page order, minimizing processing time while ensuring complete document coverage."}
             ],
             "For scanned documents and photos where no digital text stream exists, DocRoute automatically converts the page to a high-resolution image and passes it to Tesseract OCR. This hybrid routing ensures that both digital and scanned documents are reliably converted into text."),

            ("Image Preprocessing for Enhanced OCR Accuracy",
             "Improving text recognition accuracy on low-quality scans using image filtering (grayscale, thresholding).",
             "Tesseract performs best on high-contrast black-and-white images with minimal background noise or skew.",
             [
                 {"q": "Why is image preprocessing necessary before running OCR?",
                  "a": "Scanned documents often suffer from uneven lighting, paper shadows, colored backgrounds, or low contrast. Running OCR directly on noisy images causes character substitution errors (like mistaking '8' for 'B' or '1' for 'I'). Preprocessing normalizes the image to clear black text on a pure white background, significantly improving character recognition accuracy."},
                 {"q": "What preprocessing techniques can be applied in Python using OpenCV or PIL?",
                  "a": "Key preprocessing steps include: 1) Grayscale conversion (`cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`) to remove color noise, 2) Otsu's binarization / adaptive thresholding (`cv2.threshold`) to produce crisp black-and-white pixels, and 3) Denoising filters (`cv2.medianBlur`) to eliminate speckles and scanner dust."}
             ],
             "OCR accuracy depends heavily on image clarity. In DocRoute, I implemented preprocessing filters that convert scanned pages to grayscale and apply adaptive thresholding, removing background shadows and noise before character recognition to ensure clean text output."),

            ("Structured JSON Output Schema & Metadata Extraction",
             "Transforming raw extracted text into clean, structured JSON format for downstream application consumption.",
             "Standardized JSON outputs allow downstream systems (like search engines or databases) to easily consume extracted document data.",
             [
                 {"q": "How is the extracted document data structured and returned by DocRoute?",
                  "a": "DocRoute outputs a unified JSON schema containing document-level metadata (filename, page count, processing timestamp) and a `pages` array. Each page object includes `page_number`, `extraction_method` ('NATIVE_VECTOR' or 'OCR_FALLBACK'), `word_count`, and the cleaned `text` content. This provenance metadata lets consuming applications know exactly how each page was parsed."},
                 {"q": "How do you clean and normalize extracted text before outputting JSON?",
                  "a": "Extracted text often contains irregular line breaks, excessive whitespace, and hyphenated line-wraps. We apply regex normalization to reconnect hyphenated words across line breaks, strip redundant whitespace, and normalize Unicode characters to UTF-8."}
             ],
             "Raw text dumps are difficult for backend systems to use. DocRoute structures extracted content into a clean JSON schema with page numbers, word counts, and extraction method tags, enabling easy indexing and integration with backend APIs."),

            ("Testing & Developing Document Pipelines ('Under Development' Status)",
             "How to test, benchmark, and speak about an in-progress engineering project with honesty and technical depth.",
             "Being honest about 'Under Development' status builds strong credibility in interviews while demonstrating proactive learning.",
             [
                 {"q": "Your resume marks DocRoute as 'Under Development'. What is the current progress and what remains to be built?",
                  "a": "Currently, the core Python extraction modules for PyMuPDF digital parsing and Tesseract OCR fallback are functional for single documents. I am currently working on structured table extraction and writing a automated test suite with sample PDFs to benchmark extraction speed across different document sizes. That is why I deliberately marked it as 'Under Development'—to reflect its actual engineering status honestly."},
                 {"q": "How do you test document extraction pipelines for reliability?",
                  "a": "We maintain a test folder with diverse sample documents: clean digital PDFs, scanned receipts, multi-page PDFs, and corrupted files. Using `pytest`, we assert that digital files extract in under 100ms, OCR correctly identifies expected keywords, and invalid files throw graceful exceptions rather than unhandled crashes."}
             ],
             "I believe in complete transparency about my projects. I designated DocRoute as 'Under Development' on my resume because while the core digital extraction and OCR fallback modules work, I am actively refining table parsing and automated test suites before releasing it as a standalone library.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "DocRoute",
            "repo_path": "D:\\Projects\\DocRoute",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }

    else:
        # Django Backend Architecture & SQL Mastery
        topics = [
            ("Django Architecture & MVT (Model-View-Template) Pattern",
             "Understanding Django's design philosophy, batteries-included structure, and how MVT compares to classic MVC.",
             "In Django: Model defines database structure, View handles business logic, and Template renders HTML presentation. `urls.py` routes HTTP requests to views.",
             [
                 {"q": "Explain Django's MVT (Model-View-Template) architecture and the HTTP request lifecycle.",
                  "a": "When an HTTP request hits a Django server, it enters `urls.py`, which matches the requested path and routes it to the corresponding view function or class in `views.py`. The View executes business logic, interacts with the database through Models (`models.py`), and either passes data to an HTML Template (`templates/`) using `render()`, or returns a JSON payload (`JsonResponse`). The resulting HTTP response is returned to the client."},
                 {"q": "How does Django's MVT pattern compare to the classic MVC pattern?",
                  "a": "In traditional MVC, the Controller handles both request routing and view selection. In Django, the framework itself acts as the controller (handling URL routing through `urls.py`), the View in Django corresponds to the Controller's business logic in MVC, and Django Templates correspond to the View in MVC."},
                 {"q": "What are Django apps and why is a project divided into multiple apps?",
                  "a": "A Django project is a complete web application instance, while an app is a self-contained Python package that performs a specific function (e.g., `accounts`, `products`, `orders`). Dividing a project into apps promotes modularity, clean separation of concerns, and reusability across projects."}
             ],
             "My core backend strength is Python with Django. Django follows the Model-View-Template architecture where models handle data schemas, views execute business logic, and templates render presentation. Its modular app structure and built-in tooling make it exceptional for rapid, secure web development."),

            ("Django ORM, Models & Database Migrations",
             "Defining database tables with Python classes, understanding querysets, and managing schema migrations safely.",
             "`makemigrations` inspects `models.py` and creates migration scripts; `migrate` executes the SQL against the active database.",
             [
                 {"q": "What is an ORM and what are the advantages of Django's ORM?",
                  "a": "An Object-Relational Mapper (ORM) maps database tables to Python classes and rows to Python objects. Instead of writing raw SQL queries, developers write Python code like `Student.objects.filter(is_active=True)`. The ORM provides database portability (switching between SQLite, PostgreSQL, and MySQL without changing code), automatically protects against SQL injection via parameterized queries, and simplifies schema migrations."},
                 {"q": "How do database migrations work in Django?",
                  "a": "When you add or modify a model field in `models.py`, running `python manage.py makemigrations` creates a numbered Python file in the `migrations/` folder describing the schema diff. Running `python manage.py migrate` translates those Python migration instructions into native SQL `CREATE TABLE` or `ALTER TABLE` statements and applies them to the database, tracking applied migrations in `django_migrations` table."},
                 {"q": "What is lazy evaluation in Django QuerySets?",
                  "a": "Django QuerySets are lazy: constructing a query like `users = User.objects.filter(is_active=True)` does not touch the database immediately. The database query is executed only when the QuerySet is actually evaluated—such as by iterating over it in a loop, calling `len()`, slicing, or evaluating it in a template. This allows chaining multiple filters efficiently."}
             ],
             "Django's Object-Relational Mapper is one of its strongest features. It allows me to define relational schemas using Python classes, manages database migrations smoothly across development and production, and executes optimized queries with built-in protection against SQL injection."),

            ("Django Views & Django REST Framework (DRF) Basics",
             "Writing Function-Based Views (FBVs) and Class-Based Views (CBVs), building REST API endpoints, and serialization.",
             "Serializers convert complex model instances into native Python datatypes that can easily be rendered into JSON for APIs.",
             [
                 {"q": "What is the difference between Function-Based Views (FBVs) and Class-Based Views (CBVs)?",
                  "a": "Function-Based Views are straightforward Python functions that take an `HttpRequest` object and return an `HttpResponse`. They are explicit, easy to read, and great for custom logic. Class-Based Views utilize Python object-oriented programming (inheritance, mixins) to eliminate repetitive code for standard CRUD operations (like `ListView`, `DetailView`, `CreateView`), making large applications easier to maintain."},
                 {"q": "What is Django REST Framework (DRF) and what role do Serializers play?",
                  "a": "DRF is a toolkit built on top of Django for building robust RESTful APIs. Serializers in DRF perform two vital tasks: 1) Serialization: converting complex Django Model instances into Python dictionaries and JSON strings to send in API responses, and 2) Deserialization: validating incoming JSON request payloads against defined field rules before saving them to the database."},
                 {"q": "How do you handle different HTTP methods in Django?",
                  "a": "In a Function-Based View, we check `if request.method == 'POST': ... elif request.method == 'GET': ...`. In DRF or Class-Based Views, methods are organized into dedicated class methods (`def get(self, request):`, `def post(self, request):`), cleanly separating read and write handling."}
             ],
             "For API development in Django, I use Django REST Framework. By leveraging Serializers for two-way data validation and structured views for handling HTTP verbs, I can build clean, predictable REST APIs that serve frontend clients with validated JSON payloads."),

            ("Django Authentication, Sessions & Security Best Practices",
             "Utilizing Django's built-in user model, password hashing (PBKDF2), CSRF tokens, and security defenses.",
             "Django protects against Top OWASP vulnerabilities out-of-the-box: CSRF via `{% csrf_token %}`, SQL Injection via ORM parameterization, and XSS via automatic template escaping.",
             [
                 {"q": "How does Django handle user authentication and password security?",
                  "a": "Django provides a built-in `User` model with session-based authentication functions (`authenticate()`, `login()`, `logout()`). Passwords are never saved in plaintext; Django automatically uses the PBKDF2 algorithm with a SHA-256 hash and thousands of salt rounds, providing robust cryptographic resistance against brute-force attacks."},
                 {"q": "What is CSRF and how does Django protect against it?",
                  "a": "Cross-Site Request Forgery (CSRF) is an attack where a malicious website tricks a user's browser into executing an unwanted action on a site where the user is authenticated. Django protects against this using the CSRF middleware and `{% csrf_token %}` tag. Every POST form includes a unique, cryptographically generated token that the server validates before processing the request; if the token is missing or invalid, the request is blocked with HTTP 403."},
                 {"q": "How does Django protect against SQL Injection?",
                  "a": "Django's ORM automatically constructs parameterized SQL queries. Instead of directly concatenating user input into SQL strings, query parameters are passed separately to the database engine, ensuring user input is always treated as literal data, never executable SQL commands."}
             ],
             "Security is where Django truly excels. It provides battle-tested defenses against CSRF, XSS, and SQL injection by default. I leverage Django's built-in authentication system with PBKDF2 password hashing to build secure user management workflows."),

            ("Relational SQL Mastery: Joins, Aggregations & Query Optimization",
             "Writing performant SQL queries, understanding INNER vs LEFT JOIN, GROUP BY, and indexing.",
             "An Index creates a B-Tree data structure on specified columns, converting full table scans O(N) into lightning-fast binary lookups O(log N).",
             [
                 {"q": "What is the difference between an INNER JOIN and a LEFT JOIN in SQL?",
                  "a": "An `INNER JOIN` returns only the rows where there is a match in both the left and right tables. A `LEFT JOIN` (or LEFT OUTER JOIN) returns all rows from the left table, along with matching rows from the right table; if there is no match, NULL values are returned for columns from the right table. For example, a LEFT JOIN between Students and Grades ensures students with no grades yet are still listed."},
                 {"q": "Explain GROUP BY and HAVING in SQL with a practical example.",
                  "a": "`GROUP BY` groups rows with identical values in specified columns into summary rows (e.g. `SELECT course_id, COUNT(*) FROM students GROUP BY course_id`). The `HAVING` clause filters those aggregated groups based on a condition, whereas `WHERE` filters individual rows before grouping: `SELECT course_id, COUNT(*) FROM students GROUP BY course_id HAVING COUNT(*) > 50;`."},
                 {"q": "What is the N+1 queries problem and how do you prevent it in Django / SQL?",
                  "a": "The N+1 problem occurs when fetching N records from a table, and then executing an additional separate query for each record to fetch related data (1 initial query + N secondary queries). In Django, this is prevented using `select_related()` for ForeignKey (executes a SQL JOIN) or `prefetch_related()` for ManyToMany relationships, batching the lookup into a single optimized query."}
             ],
             "Strong database fundamentals are the backbone of backend engineering. I am proficient in SQL, writing complex queries involving JOINs, GROUP BY aggregations, and subqueries. I understand how to use database indexes to accelerate lookups and prevent the N+1 query problem using Django's `select_related`."),

            ("Database Transactions & ACID Properties in Practice",
             "Understanding transaction boundaries, Atomicity, Consistency, Isolation, Durability, and preventing race conditions.",
             "ACID guarantees: Atomicity (all-or-nothing), Consistency (valid constraints), Isolation (independent concurrent execution), Durability (persisted on disk).",
             [
                 {"q": "Explain the 4 ACID properties of relational databases with a real-world example.",
                  "a": "Consider transferring money between two bank accounts: 1) **Atomicity**: Debit account A and credit account B must both succeed; if one fails, both roll back (all or nothing). 2) **Consistency**: The database starts in a valid state and ends in a valid state, respecting all constraints (e.g. balance cannot be negative). 3) **Isolation**: Concurrent transactions cannot see intermediate, uncommitted states of other transactions. 4) **Durability**: Once a transaction is committed, changes are written to disk and will not be lost even if the server crashes or loses power."},
                 {"q": "How do you manage atomic database transactions in Django?",
                  "a": "In Django, you wrap operations inside `with transaction.atomic():`. If any exception is raised within the block, all database writes within that block are automatically rolled back, leaving the database in its original clean state. This is essential for operations like order creation and payment ledger updates."},
                 {"q": "What is the difference between SQLite and PostgreSQL, and when should you choose each?",
                  "a": "SQLite is a lightweight, serverless, file-based database requiring zero setup, ideal for development, desktop applications, embedded systems, and moderate read workloads. PostgreSQL is a full client-server relational database supporting high concurrency, multiple concurrent writers, advanced data types (JSONB, spatial geometry), and sophisticated indexing, making it the industry standard for production enterprise backends."}
             ],
             "Data integrity is non-negotiable in backend systems. I design database workflows around ACID guarantees, using atomic transactions in Django and PostgreSQL to ensure that financial and academic operations either complete fully or roll back cleanly without data corruption.")
        ]
        topic_info = topics[(day // 5) % len(topics)]
        return {
            "project_name": "Django Backend & SQL Architecture",
            "repo_path": "D:\\Projects",
            "topic": topic_info[0],
            "what_to_understand": topic_info[1],
            "what_to_memorize": topic_info[2],
            "interview_questions": topic_info[3],
            "interview_pitch_exercise": topic_info[4]
        }
