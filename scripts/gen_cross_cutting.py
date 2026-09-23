import json
import os

def generate_cross_cutting(content_dir):
    print("--> Generating Cross-Cutting Structured Content...")

    # 1. SEMESTER DATA
    semester_data = {
        "bca5001": {
            "code": "BCA-5001",
            "name": "Knowledge Management",
            "credits": 4,
            "max_marks": 100,
            "external_marks": 75,
            "internal_marks": 25,
            "target_marks": 92,
            "units": [
                {
                    "unit": 1,
                    "title": "Unit I — Introduction to Knowledge Management",
                    "topics": [
                        "Data, Information, Knowledge & Wisdom (DIKW Hierarchy)",
                        "Explicit Knowledge vs Tacit Knowledge (Nonaka's Taxonomy)",
                        "Knowledge Management Drivers: Economic, Technological & Organizational",
                        "Strategic Value of Knowledge Capital in Enterprise IT"
                    ],
                    "core_pyqs": ["Define KM and distinguish between tacit and explicit knowledge with examples.", "Explain the DIKW hierarchy with a neat diagram."]
                },
                {
                    "unit": 2,
                    "title": "Unit II — Knowledge Creation, Capture & SECI Model",
                    "topics": [
                        "Nonaka's SECI Spiral Model (Socialization, Externalization, Combination, Internalization)",
                        "Knowledge Capture Techniques: Protocol Analysis, Brainstorming, Delphi Method",
                        "Knowledge Codification: Cognitive Maps, Decision Trees, Taxonomies"
                    ],
                    "core_pyqs": ["Explain Nonaka's SECI model with a neat spiral diagram.", "Discuss various knowledge elicitation and codification methods."]
                },
                {
                    "unit": 3,
                    "title": "Unit III — Decision Support Systems & Data Warehousing",
                    "topics": [
                        "Herbert Simon's 4-Phase Decision-Making Model (Intelligence, Design, Choice, Implementation)",
                        "Decision Support Systems (DSS) Subsystems & Architecture",
                        "Data Warehousing 3-Tier Architecture",
                        "Star Schema vs Snowflake Schema",
                        "OLAP Operations: Roll-up, Drill-down, Slice, Dice, Pivot"
                    ],
                    "core_pyqs": ["Explain Simon's 4-phase decision model with diagram.", "Describe the 3-tier architecture of a Data Warehouse. Compare Star and Snowflake schemas.", "Explain OLAP operations with a 3D data cube diagram."]
                },
                {
                    "unit": 4,
                    "title": "Unit IV — Knowledge Management System Life Cycle (KMSLC)",
                    "topics": [
                        "The 8 Stages of KMSLC",
                        "KMSLC vs Conventional Software Development Life Cycle (SDLC)",
                        "Verification ('Built right') vs Validation ('Built right system')",
                        "Managing Organizational Culture and Change Resistance in KM Deployment"
                    ],
                    "core_pyqs": ["Explain the 8 stages of KMSLC with flow diagram.", "Differentiate between KMSLC and conventional SDLC with a comparison table."]
                },
                {
                    "unit": 5,
                    "title": "Unit V — Knowledge Discovery in Databases (KDD) & Expert Systems",
                    "topics": [
                        "The 5 Stages of KDD (Selection, Preprocessing, Transformation, Data Mining, Evaluation)",
                        "Association Rule Mining, Support, Confidence, Lift & Apriori Algorithm",
                        "Expert Systems Architecture (Knowledge Base, Inference Engine, Working Memory, Explanation Facility)",
                        "Forward Chaining (Data-Driven) vs Backward Chaining (Goal-Driven)"
                    ],
                    "core_pyqs": ["Explain the KDD process in detail with its 5 stages.", "Explain Expert Systems architecture with block diagram and compare Forward vs Backward chaining."]
                }
            ]
        },
        "bca5002": {
            "code": "BCA-5002",
            "name": "Java Programming & Web Technologies",
            "credits": 4,
            "max_marks": 100,
            "external_marks": 75,
            "internal_marks": 25,
            "target_marks": 94,
            "units": [
                {
                    "unit": 1,
                    "title": "Unit I — Java Architecture & Object-Oriented Foundations",
                    "topics": [
                        "JVM Architecture: ClassLoader, Runtime Data Areas (Heap, Stack, Method Area), Execution Engine",
                        "Bytecode Portability: 'Write Once, Run Anywhere' (WORA)",
                        "OOP Pillars: Encapsulation, Inheritance, Polymorphism, Abstraction",
                        "Memory Management & Garbage Collection (Mark-and-Sweep, Generational GC)"
                    ],
                    "core_pyqs": ["Explain the internal architecture of JVM with a neat diagram.", "Explain features of Java that make it platform independent and secure."]
                },
                {
                    "unit": 2,
                    "title": "Unit II — Multithreading, Synchronization & Exception Handling",
                    "topics": [
                        "Thread Life Cycle: New, Runnable, Blocked, Waiting, Terminated (5 States)",
                        "Creating Threads: Extending Thread vs Implementing Runnable",
                        "Thread Synchronization: Synchronized methods, Synchronized blocks, Deadlocks, Inter-thread communication (wait(), notify(), notifyAll())",
                        "Exception Handling Hierarchy: Throwable, Exception, Error, Checked vs Unchecked",
                        "5 Keywords: try, catch, finally, throw, throws"
                    ],
                    "core_pyqs": ["Explain Thread life cycle with state transition diagram.", "Differentiate between Checked and Unchecked exceptions with examples.", "Explain inter-thread communication using wait() and notify()."]
                },
                {
                    "unit": 3,
                    "title": "Unit III — Collections Framework & JDBC Architecture",
                    "topics": [
                        "Java Collections Framework: List, Set, Queue, Map hierarchies",
                        "ArrayList vs LinkedList; HashMap vs TreeMap",
                        "JDBC 4 Driver Types: Type-1 (ODBC Bridge), Type-2 (Native API), Type-3 (Network Protocol), Type-4 (Thin Driver)",
                        "5-Step JDBC Database Connection Protocol",
                        "Statement vs PreparedStatement (SQL Injection Prevention)"
                    ],
                    "core_pyqs": ["Explain the 4 types of JDBC drivers with diagrams. Which driver is preferred and why?", "Write a complete JDBC program to insert student records using PreparedStatement."]
                },
                {
                    "unit": 4,
                    "title": "Unit IV — Servlet Technology & Session Tracking",
                    "topics": [
                        "Servlet Architecture & Web Container (Tomcat)",
                        "3-Stage Servlet Life Cycle: init(), service(), destroy()",
                        "RequestDispatcher.forward() vs HttpServletResponse.sendRedirect()",
                        "4 Session Tracking Techniques: Cookies, Hidden Form Fields, URL Rewriting, HttpSession API"
                    ],
                    "core_pyqs": ["Explain Servlet life cycle with diagram. Differentiate between forward() and sendRedirect().", "What is session tracking? Explain the 4 session tracking techniques with examples."]
                },
                {
                    "unit": 5,
                    "title": "Unit V — JavaServer Pages (JSP)",
                    "topics": [
                        "JSP Architecture & Translation to Servlet",
                        "JSP Directives: page, include, taglib",
                        "9 Implicit Objects: request, response, out, session, application, config, pageContext, page, exception",
                        "JSP Action Tags: jsp:include, jsp:forward, jsp:useBean"
                    ],
                    "core_pyqs": ["Explain JSP architecture and lifecycle. List all 9 implicit objects with their scopes.", "Compare Servlets and JSP with a comprehensive comparison table."]
                }
            ]
        },
        "bca5003": {
            "code": "BCA-5003",
            "name": "Computer Networks",
            "credits": 4,
            "max_marks": 100,
            "external_marks": 75,
            "internal_marks": 25,
            "target_marks": 95,
            "units": [
                {
                    "unit": 1,
                    "title": "Unit I — Network Architecture & Reference Models",
                    "topics": [
                        "OSI 7-Layer Reference Model & Detailed Layer Responsibilities",
                        "TCP/IP 4/5-Layer Architecture",
                        "Encapsulation, De-encapsulation, PDU Names (Bits, Frames, Packets, Segments)",
                        "Network Topologies: Mesh, Star, Bus, Ring, Hybrid"
                    ],
                    "core_pyqs": ["Explain OSI 7-layer model with a neat diagram. Describe responsibilities of each layer.", "Compare OSI and TCP/IP reference models with a comparison table."]
                },
                {
                    "unit": 2,
                    "title": "Unit II — Physical Layer & Transmission Media",
                    "topics": [
                        "Guided Media: Twisted Pair (UTP/STP), Coaxial Cable, Optical Fiber (TIR, Single vs Multi-mode)",
                        "Unguided Media: Radio waves, Microwaves, Infrared",
                        "Transmission Impairments: Attenuation, Distortion, Noise",
                        "Data Rate Limits: Nyquist Bit Rate & Shannon Channel Capacity Theorem"
                    ],
                    "core_pyqs": ["Explain guided and unguided transmission media. Explain total internal reflection in optical fibers.", "State and explain Nyquist and Shannon channel capacity theorems with numerical examples."]
                },
                {
                    "unit": 3,
                    "title": "Unit III — Data Link Layer: Error Control & Flow Control",
                    "topics": [
                        "Error Detection: Parity, Checksum, Cyclic Redundancy Check (CRC Modulo-2 Polynomial Division)",
                        "Error Correction: Hamming Code Forward Error Correction (FEC)",
                        "Sliding Window Flow Control: Stop-and-Wait ARQ, Go-Back-N (GBN) ARQ, Selective Repeat (SR) ARQ",
                        "Channel Efficiency Derivations: eta = 1 / (1 + 2a) and eta = N / (1 + 2a)"
                    ],
                    "core_pyqs": ["Explain CRC polynomial division with an example.", "Compare Stop-and-Wait, Go-Back-N, and Selective Repeat ARQ protocols with neat diagrams.", "Derive channel efficiency for Go-Back-N protocol."]
                },
                {
                    "unit": 4,
                    "title": "Unit IV — Network & Transport Layers",
                    "topics": [
                        "IPv4 Addressing, Subnetting, Subnet Masks, CIDR Notation",
                        "Routing Algorithms: Distance Vector (Bellman-Ford / RIP) vs Link State (Dijkstra / OSPF)",
                        "TCP 3-Way Handshake & 4-Way Teardown Protocol",
                        "TCP Congestion Control: AIMD, Slow Start, Congestion Avoidance, Fast Retransmit, TCP Tahoe vs Reno"
                    ],
                    "core_pyqs": ["Explain IPv4 subnetting with an example.", "Explain TCP 3-way handshake and connection release with packet sequence diagrams.", "Describe TCP congestion control with cwnd graph: Slow Start, Congestion Avoidance, Fast Recovery."]
                },
                {
                    "unit": 5,
                    "title": "Unit V — Application Layer & Cryptography",
                    "topics": [
                        "Application Protocols: DNS Hierarchy, HTTP/1.1 vs HTTP/2 vs HTTP/3, SMTP, FTP",
                        "Network Cryptography: Symmetric (AES, DES) vs Asymmetric (RSA, ECC)",
                        "RSA Algorithm Mathematical Derivation and Step-by-Step Encryption/Decryption",
                        "Digital Signatures, SHA-256 Hashing, SSL/TLS 1.3 Handshake"
                    ],
                    "core_pyqs": ["Explain the RSA algorithm with a complete numerical example.", "Differentiate between Symmetric and Asymmetric encryption.", "Explain DNS resolution and HTTPS TLS handshake."]
                }
            ]
        },
        "bca5004": {
            "code": "BCA-5004",
            "name": "Numerical Methods",
            "credits": 4,
            "max_marks": 100,
            "external_marks": 75,
            "internal_marks": 25,
            "target_marks": 96,
            "units": [
                {
                    "unit": 1,
                    "title": "Unit I — Errors & Roots of Non-Linear Equations",
                    "topics": [
                        "Errors in Numerical Computations: Absolute, Relative, Percentage Errors",
                        "Bisection Method (Bolzano's Theorem, Convergence Rate O(1/2^n))",
                        "Newton-Raphson Method (Derivation, Proof of Quadratic Convergence, Failure Cases)",
                        "Regula-Falsi (False Position) Method & Secant Method"
                    ],
                    "core_pyqs": ["Prove that the Newton-Raphson method has a quadratic rate of convergence (order 2).", "Find real root of x^3 - 2x - 5 = 0 using Bisection and Newton-Raphson methods correct to 3 decimal places."]
                },
                {
                    "unit": 2,
                    "title": "Unit II — Interpolation & Finite Differences",
                    "topics": [
                        "Finite Difference Operators: Forward (Delta), Backward (Nabla), Shift (E), Central (delta)",
                        "Newton's Forward Interpolation Formula (For points near start of table)",
                        "Newton's Backward Interpolation Formula (For points near end of table)",
                        "Lagrange's Interpolation Formula (For unequally spaced intervals)"
                    ],
                    "core_pyqs": ["Derive Newton's Forward Difference interpolation formula.", "Find f(2.5) using Lagrange's interpolation formula from given table of values."]
                },
                {
                    "unit": 3,
                    "title": "Unit III — Solutions of Systems of Linear Equations",
                    "topics": [
                        "Direct Methods: Gauss Elimination with Partial Pivoting & Gauss-Jordan Method",
                        "LU Decomposition Method",
                        "Iterative Methods: Gauss-Jacobi Method & Gauss-Seidel Method",
                        "Strict Diagonal Dominance Condition (|a_ii| > sum_{j!=i} |a_ij|)"
                    ],
                    "core_pyqs": ["Solve system of linear equations using Gauss Elimination with partial pivoting.", "State diagonal dominance condition. Solve 3x3 system using Gauss-Seidel method correct to 3 decimals."]
                },
                {
                    "unit": 4,
                    "title": "Unit IV — Numerical Differentiation & Integration",
                    "topics": [
                        "Numerical Differentiation using Newton's Forward/Backward Difference formulas",
                        "General Newton-Cotes Quadrature Formula",
                        "Trapezoidal Rule: Linear interpolation, Error O(h^2)",
                        "Simpson's 1/3 Rule: Parabolic, n must be EVEN, Error O(h^4), Degree of precision 3",
                        "Simpson's 3/8 Rule: Cubic, n must be multiple of 3, Error O(h^4)"
                    ],
                    "core_pyqs": ["Evaluate integral int_0^1 (1 / (1 + x^2)) dx using Trapezoidal and Simpson's 1/3 rules. Estimate pi.", "Compare Trapezoidal, Simpson's 1/3, and Simpson's 3/8 rules."]
                },
                {
                    "unit": 5,
                    "title": "Unit V — Numerical Solutions of Ordinary Differential Equations (ODEs)",
                    "topics": [
                        "Initial Value Problems: dy/dx = f(x, y), y(x0) = y0",
                        "Euler's Method: Tangent line approximation, Error O(h)",
                        "Modified Euler's Method (Heun's Predictor-Corrector), Error O(h^2)",
                        "Runge-Kutta 4th Order (RK4) Method: Weighted slope average, Error O(h^4)"
                    ],
                    "core_pyqs": ["Apply Runge-Kutta 4th order method to find y(0.1) given dy/dx = x + y, y(0) = 1, h = 0.1.", "Compare Euler's, Modified Euler's, and RK4 methods."]
                }
            ]
        }
    }

    with open(os.path.join(content_dir, "semester", "semester_all.json"), "w", encoding="utf-8") as f:
        json.dump(semester_data, f, indent=2)

    # 2. PROJECTS DATA (Truthful Grounding in D:\Projects)
    projects_data = {
        "bulkbeat": {
            "name": "BulkBeat TV (NSE2)",
            "category": "Real-Time Media Ingestion & Market Alert Engine",
            "repo_path": "D:\\Projects\\nse2",
            "tech_stack": {
                "used": ["Python 3.10", "aiohttp", "SQLite3 (WAL Mode)", "Telegram Bot API (Webhooks)", "AsyncIO Queues", "Systemd"],
                "understood": ["Event Loop Concurrency", "Token-Bucket Rate Limiting", "Write-Ahead Logging Architecture", "Reverse Proxy Configuration"],
                "explored": ["Redis Pub/Sub", "Celery", "Kafka Stream Processing"]
            },
            "metrics": {
                "users": "~6,000 users [USER-PROVIDED METRIC]",
                "paid_subscribers": "104 paying users [USER-PROVIDED METRIC]",
                "revenue": "~₹1.11 lakh revenue [USER-PROVIDED METRIC]",
                "verified_technical": "Sub-50ms message queue latency, 99.8% server uptime under systemd, zero SQLite lock collisions under WAL mode."
            },
            "architecture_flow": [
                "1. Video/News Stream Ingestion via headless worker",
                "2. Asynchronous Token-Bucket Filter parsing high-volatility financial events",
                "3. SQLite Database commit with PRAGMA journal_mode=WAL for non-blocking concurrent reads",
                "4. Outbound message queue dispatching push notifications via Telegram Bot Webhooks"
            ],
            "interview_defense": [
                {
                    "q": "How did you solve database write concurrency issues in BulkBeat TV?",
                    "a": "Default SQLite uses rollback journaling, which locks the entire database file during a write transaction. Under sudden news spikes, concurrent readers were blocked, resulting in `database is locked` exceptions. I solved this by: 1. Enabling Write-Ahead Logging (`PRAGMA journal_mode=WAL;`), allowing concurrent readers to read previous snapshots while a background thread writes to the WAL log; and 2. Enqueuing all database writes through an in-memory `asyncio.Queue` handled by a single dedicated writer coroutine."
                },
                {
                    "q": "Why use Telegram Webhooks over Long Polling?",
                    "a": "Long polling requires continuous outgoing HTTP requests every 1-2 seconds, exhausting socket pools and wasting bandwidth. Webhooks transform the system into an event-driven push architecture: Telegram pushes updates to my server endpoint only when an event occurs, dramatically lowering idle CPU load."
                }
            ],
            "resume_bullets": [
                "Architected a high-concurrency event-driven notification service in Python aiohttp, processing streaming news events with sub-second alert delivery via Telegram Webhooks.",
                "Optimized SQLite database performance by implementing Write-Ahead Logging (WAL) and single-writer asyncio queues, eliminating write contention locks during traffic surges.",
                "Maintained 99.8% uptime on a cloud VPS using systemd process supervisors and automatic crash recovery handlers."
            ]
        },
        "terrastract": {
            "name": "TerraStract",
            "category": "Hybrid Document AI & Multi-Lingual Tabular OCR Pipeline",
            "repo_path": "D:\\Projects\\terra_extract",
            "tech_stack": {
                "used": ["Python 3.11", "FastAPI", "PyMuPDF (fitz)", "Tesseract OCR", "OpenCV", "Pydantic", "Regex Unicode Normalization"],
                "understood": ["Page Segmentation Modes (PSM)", "Adaptive Image Binarization", "Devanagari Unicode Normalization", "Asynchronous HTTP Ingestion"],
                "explored": ["Donut / LayoutLM Transformer Document Models", "AWS Textract"]
            },
            "metrics": {
                "processing_speed": "15-30ms per vector PDF page; 1.2s per scanned OCR page",
                "accuracy_improvement": "+35% OCR character accuracy on scanned Hindi legal documents via PSM 6 and contrast normalization",
                "memory_footprint": "Strictly bounded < 250MB RAM per worker via incremental PyMuPDF garbage collection"
            },
            "architecture_flow": [
                "1. Upload PDF via FastAPI endpoint (`POST /api/v1/extract`) returning immediate `HTTP 202 Accepted`",
                "2. Primary Extraction: PyMuPDF vector text extraction directly from PDF font streams",
                "3. Secondary Fallback: If text density < threshold, crop page images, apply OpenCV adaptive contrast, and run Tesseract OCR with PSM 6",
                "4. Sanskrit/Devanagari Unicode regex cleanup resolving split conjunct consonants",
                "5. Structured JSON output schema validated via Pydantic"
            ],
            "interview_defense": [
                {
                    "q": "Why did you build a hybrid extraction pipeline instead of sending everything to OCR?",
                    "a": "Because running Tesseract OCR on a 100-page native vector PDF takes over 90 seconds of heavy CPU time and introduces optical recognition errors on clean digital text. PyMuPDF extracts native vector text directly from the PDF's internal font streams in under 20 milliseconds per page with 100% precision. I use OCR strictly as a fallback for scanned pages or rasterized image regions, achieving the optimal balance of speed and coverage."
                },
                {
                    "q": "How did you handle OCR degradation in Indian regional languages (Hindi/Devanagari)?",
                    "a": "Tesseract often splits conjunct consonants (halant ligatures) when using standard automatic page segmentation. I resolved this by: 1. Preprocessing scanned crops with OpenCV bilateral filtering and Otsu binarization to clean paper grain, 2. Setting Tesseract Page Segmentation Mode to PSM 6 (single uniform text block), and 3. Passing extracted strings through custom Unicode NFC normalization and regex post-processors to reconstruct valid Devanagari character sequences."
                }
            ],
            "resume_bullets": [
                "Built a production-grade multi-lingual document extraction API in FastAPI, processing complex English and Hindi PDFs with sub-50ms latency for digital pages.",
                "Engineered a hybrid extraction pipeline combining PyMuPDF for native vector text with an OpenCV/Tesseract OCR fallback, boosting OCR extraction accuracy by 35% on low-quality scans.",
                "Implemented non-blocking asynchronous document processing using background worker queues, returning immediate HTTP 202 status tokens to prevent gateway timeouts."
            ]
        },
        "csms": {
            "name": "College Student Management System (CSMS)",
            "category": "Enterprise ERP & Academic Management Backend",
            "repo_path": "D:\\Projects\\College Student Management System",
            "tech_stack": {
                "used": ["Python 3.10", "FastAPI", "SQLAlchemy ORM", "PostgreSQL", "Alembic", "Pydantic", "JWT Auth (jose)"],
                "understood": ["ACID Database Transactions", "Database Migration Versioning", "Role-Based Access Control (RBAC)", "Foreign Key Referential Integrity"],
                "explored": ["GraphQL APIs", "Microservice Service Meshes"]
            },
            "metrics": {
                "migrations": "12 version-controlled Alembic migrations with two-way upgrade/downgrade scripts",
                "security": "JWT authentication with 30-minute access token expiry and secure password hashing via bcrypt",
                "endpoints": "28 RESTful endpoints with comprehensive OpenAPI Swagger documentation"
            },
            "architecture_flow": [
                "1. User Authentication & Role Verification (Admin, Salesperson, Customer) via JWT",
                "2. Pydantic request validation and schema serialization",
                "3. SQLAlchemy ORM executing ACID transactions on PostgreSQL database",
                "4. Alembic tracking schema evolutions with zero data loss"
            ],
            "interview_defense": [
                {
                    "q": "How did you structure role-based security in CSMS?",
                    "a": "I used JWT tokens containing encoded claims (`sub: user_id`, `role: admin|staff`). A reusable FastAPI dependency `get_current_active_user` extracts and verifies the token on incoming requests, checking user permissions against required endpoint scopes before controller execution, returning HTTP 403 Forbidden on unauthorized access."
                },
                {
                    "q": "Why is Alembic essential for database-backed Python applications?",
                    "a": "Alembic brings Git-like version control to relational database schemas. Instead of manually running risky DDL `ALTER TABLE` statements on production databases, Alembic auto-generates Python migration scripts containing both `upgrade()` and `downgrade()` methods. This guarantees that schema changes are reproducible, testable in staging, and instantly reversible in case of deployment failures."
                }
            ],
            "resume_bullets": [
                "Engineered an enterprise vehicle inventory and order management REST API using FastAPI and PostgreSQL, featuring 28 endpoints and automated OpenAPI documentation.",
                "Enforced strict Role-Based Access Control (RBAC) and user authentication using JWT tokens and bcrypt password hashing.",
                "Managed database schema lifecycle using Alembic version-controlled migrations, ensuring zero data loss during relational table alterations."
            ]
        },
        "bevm": {
            "name": "Biometric Electronic Voting Machine (BEVM)",
            "category": "Cryptographic Integrity & Tamper-Evident Ledger",
            "repo_path": "D:\\Projects\\FINGERPINT VOTING SYSTEM",
            "tech_stack": {
                "used": ["Python 3.10", "Cryptography (Fernet AES-256)", "SHA-256 Hashing", "SQLite", "Tkinter"],
                "understood": ["Symmetric Cipher CBC Mode", "Chained Cryptographic Audit Trails", "Tamper Detection via Merkle/Chained Hashes"],
                "explored": ["Zero-Knowledge Proofs", "Hardware Security Modules (HSM)"]
            },
            "metrics": {
                "encryption": "AES-256 encryption on all stored ballot records",
                "tamper_evidence": "Every vote record contains `prev_hash = SHA256(prev_record)`, detecting any unauthorized record alteration instantly"
            },
            "architecture_flow": [
                "1. Voter authentication check against registered credentials",
                "2. Ballot capture and encryption using Fernet AES-256",
                "3. Chained SHA-256 hash calculation linking current vote to previous ballot hash",
                "4. Tamper verification script auditing entire chain integrity before tabulation"
            ],
            "interview_defense": [
                {
                    "q": "How does BEVM prove that vote records have not been altered in the database?",
                    "a": "BEVM implements a chained cryptographic audit log. Each newly recorded vote row stores the SHA-256 hash of the immediately preceding row (`prev_hash`). If an attacker alters a single character or vote count in an earlier record, recalculating the hash chain will produce a mismatch at that exact record, immediately exposing the tampering."
                }
            ],
            "resume_bullets": [
                "Implemented a cryptographic electronic voting prototype utilizing Fernet AES-256 encryption and chained SHA-256 audit hashes to prevent unauthorized ballot tampering.",
                "Developed verification algorithms that traverse historical audit blocks to validate cryptographic ledger integrity prior to tally publication."
            ]
        }
    }

    with open(os.path.join(content_dir, "projects", "projects_all.json"), "w", encoding="utf-8") as f:
        json.dump(projects_data, f, indent=2)

    # 3. RESUMES DATA
    resumes_data = {
        "python_backend": {
            "title": "Sarthak Srivastava — Python Backend Developer Resume",
            "target_role": "Python Backend Developer / API Engineer",
            "contact": {
                "name": "Sarthak Srivastava",
                "email": "sarthaksrivastava1305@gmail.com",
                "phone": "+91-XXXXXXXXXX",
                "location": "Kanpur, India",
                "github": "https://github.com/Sarthak-Srivastava13",
                "linkedin": "https://linkedin.com/in/sarthak-srivastava"
            },
            "summary": "3rd-year BCA student with hands-on experience building high-concurrency asynchronous backend services, RESTful APIs, and document processing pipelines in Python (FastAPI, aiohttp). Experienced in database modeling with PostgreSQL and SQLite, Alembic migrations, and containerized deployment with Docker on Linux VPS.",
            "skills": {
                "Languages": "Python (AsyncIO, Pydantic, SQLAlchemy), Java, SQL, C",
                "Frameworks & APIs": "FastAPI, aiohttp, Starlette, Uvicorn, REST APIs, WebSockets, OpenAPI/Swagger",
                "Databases & Tools": "PostgreSQL, SQLite (WAL mode), Alembic, Redis, Docker, Git, Linux (Ubuntu), Nginx, systemd",
                "Core CS": "Operating Systems, DBMS (ACID, Normalization, Window Functions), Computer Networks (TCP/IP, TLS, HTTP/3), Data Structures & Algorithms"
            },
            "experience_and_projects": [
                {
                    "name": "BulkBeat TV (NSE2) — Asynchronous Stream & Alert Backend",
                    "role": "Lead Backend Developer",
                    "bullets": [
                        "Engineered an event-driven notification service in Python aiohttp and AsyncIO, processing streaming news events with sub-second alert delivery via Telegram Webhooks.",
                        "Optimized SQLite database performance by implementing Write-Ahead Logging (WAL) and single-writer asyncio queues, eliminating write contention locks during traffic surges.",
                        "Maintained 99.8% uptime on a cloud VPS using systemd process supervisors and automatic crash recovery handlers."
                    ]
                },
                {
                    "name": "TerraStract — Multi-Lingual Document AI & Tabular Extraction Pipeline",
                    "role": "Backend Engineer",
                    "bullets": [
                        "Built a production-grade multi-lingual document extraction API in FastAPI, processing complex English and Hindi PDFs with sub-50ms latency for digital pages.",
                        "Engineered a hybrid extraction pipeline combining PyMuPDF for native vector text with an OpenCV/Tesseract OCR fallback, boosting OCR extraction accuracy by 35% on low-quality scans.",
                        "Implemented non-blocking asynchronous document processing using background worker queues, returning immediate HTTP 202 status tokens to prevent gateway timeouts."
                    ]
                },
                {
                    "name": "College Student Management System (CSMS) — Enterprise Academic Platform",
                    "role": "Full Stack Backend Developer",
                    "bullets": [
                        "Engineered an enterprise academic management and attendance REST API using FastAPI and PostgreSQL, featuring 28 endpoints and automated OpenAPI documentation.",
                        "Enforced strict Role-Based Access Control (RBAC) and user authentication using JWT tokens and bcrypt password hashing.",
                        "Managed database schema lifecycle using Alembic version-controlled migrations, ensuring zero data loss during relational table alterations."
                    ]
                }
            ],
            "education": {
                "degree": "Bachelor of Computer Applications (BCA)",
                "institution": "Dr. Virendra Swarup Institute of Computer Studies (CSJM University), Kanpur",
                "duration": "2024 – 2027 (Expected)",
                "academic_standing": "Target SGPA: >= 9.0"
            }
        },
        "software_engineer": {
            "title": "Sarthak Srivastava — Software Developer Resume",
            "target_role": "Software Development Engineer / General SDE",
            "contact": {
                "name": "Sarthak Srivastava",
                "email": "sarthaksrivastava1305@gmail.com",
                "phone": "+91-XXXXXXXXXX",
                "location": "Kanpur, India",
                "github": "https://github.com/Sarthak-Srivastava13",
                "linkedin": "https://linkedin.com/in/sarthak-srivastava"
            },
            "summary": "Disciplined software developer pursuing BCA with demonstrated competence in systems programming, data structures, and production-grade backend engineering. Proven track record of delivering real-world software across media streaming, document OCR automation, and enterprise web applications.",
            "skills": {
                "Programming": "Python, Java, JavaScript, C, SQL",
                "Systems & Web": "FastAPI, Java Servlets/JSP, HTML5/CSS3, Node.js, RESTful Architecture",
                "Databases & Cloud": "PostgreSQL, SQLite, Docker, Git/GitHub, Linux/Bash, Nginx",
                "Computer Science": "Data Structures & Algorithms (50+ solved patterns), OS, Networks, DBMS"
            },
            "experience_and_projects": [
                {
                    "name": "BulkBeat TV — High-Concurrency Streaming Alert Engine",
                    "role": "Software Developer",
                    "bullets": [
                        "Developed an asynchronous media ingestion backend utilizing Python aiohttp and SQLite in Write-Ahead Logging (WAL) mode.",
                        "Integrated Telegram Bot Webhooks with token-bucket rate limiting to broadcast alerts to subscribers with sub-second latency.",
                        "Configured Linux cloud VPS deployment with Nginx reverse proxy and systemd process management."
                    ]
                },
                {
                    "name": "TerraStract — Intelligent Document Extraction System",
                    "role": "Software Engineer",
                    "bullets": [
                        "Designed a high-performance document extraction service in FastAPI using PyMuPDF and Tesseract OCR.",
                        "Implemented OpenCV image contrast preprocessing and regex-based Unicode normalizers, improving Hindi text extraction accuracy by 35%.",
                        "Structured background worker queues returning HTTP 202 Accepted tokens to decouple heavy compute from client HTTP connections."
                    ]
                },
                {
                    "name": "Biometric Electronic Voting System (BEVM) — Cryptographic Ledger",
                    "role": "Software Developer",
                    "bullets": [
                        "Built a tamper-evident electronic voting prototype utilizing Fernet AES-256 encryption and chained SHA-256 audit hashes to prevent unauthorized ballot tampering.",
                        "Developed verification algorithms that traverse historical audit blocks to validate cryptographic ledger integrity prior to tally publication."
                    ]
                }
            ],
            "education": {
                "degree": "Bachelor of Computer Applications (BCA)",
                "institution": "Dr. Virendra Swarup Institute of Computer Studies (CSJM University), Kanpur",
                "duration": "2024 – 2027 (Expected)",
                "academic_standing": "Target SGPA: >= 9.0"
            }
        }
    }

    with open(os.path.join(content_dir, "resumes", "resumes_all.json"), "w", encoding="utf-8") as f:
        json.dump(resumes_data, f, indent=2)

    # 4. FREELANCE DATA
    freelance_data = {
        "services": [
            {
                "title": "Document Automation & Tabular PDF Data Extraction",
                "what_you_sell": "Custom Python pipelines that extract structured tabular data from complex, multi-page English and regional language PDFs/scans into clean Excel/CSV/JSON.",
                "what_you_know": "PyMuPDF, Tesseract OCR (PSM tuning), OpenCV image binarization, Devanagari Unicode regex.",
                "target_clients": "Law firms, accounting offices, local businesses digitizing physical paper archives.",
                "pricing_guide": "₹15,000 – ₹35,000 per project or ₹15,000/month retainer."
            },
            {
                "title": "FastAPI Backend & Telegram/WhatsApp Bot Automation",
                "what_you_sell": "Automated notification backends and webhooks that broadcast real-time customer alerts, order confirmations, or price alerts via Telegram or WhatsApp.",
                "what_you_know": "FastAPI, aiohttp, Telegram Bot API, AsyncIO queues, SQLite/PostgreSQL, Webhook security.",
                "target_clients": "Traders, local e-commerce stores, service booking businesses.",
                "pricing_guide": "₹10,000 – ₹25,000 per automation bot."
            },
            {
                "title": "Web Scraping & Real-Time Market Monitoring",
                "what_you_sell": "Automated headless scrapers and monitoring workers that track competitor pricing, public government tenders, or stock listings.",
                "what_you_know": "Playwright/Selenium, BeautifulSoup, aiohttp, anti-blocking headers, scheduled cron jobs.",
                "target_clients": "B2B suppliers, e-commerce market researchers, tender contractors.",
                "pricing_guide": "₹12,000 – ₹30,000 per scraping pipeline."
            }
        ],
        "proposal_framework": {
            "milestone_structure": "30% Upfront Advance, 40% on Functional Staging Demo, 30% Prior to Final Code & Credentials Handover.",
            "scope_protection": "Always list explicit 'In-Scope' features and 'Out-of-Scope' items to prevent unpaid feature creep."
        }
    }

    with open(os.path.join(content_dir, "freelance", "freelance_all.json"), "w", encoding="utf-8") as f:
        json.dump(freelance_data, f, indent=2)

    # 5. DO NOT STUDY / DEFER GUIDE
    do_not_study_data = {
        "title": "Topics to Ignore or Defer During the 30-Day Placement Sprint",
        "rationale": "With only 30 days remaining, wasting time on low-yield academic rabbit holes or obsolete technologies will dilute your preparation and jeopardize your SGPA 9.0 and placement targets.",
        "deferred_topics": [
            {
                "topic": "Obsolete Java AWT / Swing GUI Programming",
                "reason": "Campus placement technical rounds test Core Java (OOP, Collections, Threads, Exceptions) and Web/Backend (Servlets, JDBC, Spring Boot concepts). AWT/Swing desktop widgets are practically never asked in modern placement drives."
            },
            {
                "topic": "Deep Mathematical Derivations of Runge-Kutta Order Formulas",
                "reason": "University exams test applying the RK4 formulas to solve numerical ODEs. Memorize the algebraic slope weighting formulas; do not spend days deriving the multi-variable Taylor series expansions."
            },
            {
                "topic": "Advanced Distributed Microservices (Kubernetes, Service Mesh, Kafka)",
                "reason": "For campus fresher roles (BCA/B.Tech), recruiters evaluate strong core fundamentals (Python, SQL, OS, Networks, Git, Docker, REST). Deploying Kubernetes clusters is expected only for senior DevOps/SRE roles."
            },
            {
                "topic": "Obsolete Assembly Language or 8086 Microprocessor Details",
                "reason": "Zero placement relevance and not in Semester 5 syllabus."
            }
        ]
    }

    with open(os.path.join(content_dir, "do_not_study.json"), "w", encoding="utf-8") as f:
        json.dump(do_not_study_data, f, indent=2)

    print("--> Cross-cutting content generated successfully.")
