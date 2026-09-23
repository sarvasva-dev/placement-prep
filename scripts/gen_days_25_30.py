# Days 25 to 30 Curriculum Definition with Publication-Grade Pedagogical Depth

def get_days_25_to_30():
    days = {}

    # DAY 25
    days[25] = {
        "day": 25,
        "title": "JSP Architecture & Implicit Objects, Critical Reasoning & Word Break DP",
        "sem_data": {
            "subject": "BCA-5002 Java Programming",
            "topic": "Unit V — Java Server Pages (JSP): Architecture, 9 Implicit Objects & Lifecycle",
            "detailed_notes": [
                "Java Server Pages (JSP) is a server-side presentation technology that allows developers to write standard HTML markup with embedded dynamic Java code snippets, simplifying the creation of dynamic web views compared to Servlets.",
                "JSP Architecture & Translation Process:\n"
                "When a client requests a `.jsp` page for the first time:\n"
                "1. Translation Phase: The JSP Engine (e.g. Jasper in Apache Tomcat) reads the `.jsp` source and translates it into an equivalent `.java` Servlet source file (e.g. `index_jsp.java`).\n"
                "2. Compilation Phase: The Java compiler (`javac`) compiles the generated servlet source into bytecode (`index_jsp.class`).\n"
                "3. Loading & Instantiation: The Web Container loads the class file into memory and creates an instance.\n"
                "4. Life Cycle Invocation: The container calls `jspInit()` once, then handles every incoming client request by calling `_jspService(HttpServletRequest, HttpServletResponse)`, and finally calls `jspDestroy()` on shutdown.",
                "The 3 JSP Directive Tags:\n"
                "• `<%@ page ... %>`: Defines page-dependent attributes: `import`, `contentType`, `session`, `isErrorPage`, `errorPage`.\n"
                "• `<%@ include file=\"header.jsp\" %>`: Static compile-time inclusion of external files.\n"
                "• `<%@ taglib uri=\"...\" prefix=\"c\" %>`: Declares custom JSP Standard Tag Libraries (JSTL).",
                "The 9 JSP Implicit Objects (Available automatically without instantiation):\n"
                "1. `request`: Instance of `HttpServletRequest` (HTTP headers, form parameters).\n"
                "2. `response`: Instance of `HttpServletResponse` (cookies, redirection).\n"
                "3. `out`: Instance of `JspWriter` (streams HTML output to client).\n"
                "4. `session`: Instance of `HttpSession` (tracks conversational state across requests).\n"
                "5. `application`: Instance of `ServletContext` (global application-wide context shared across all servlets/JSPs).\n"
                "6. `config`: Instance of `ServletConfig` (page-specific initialization parameters).\n"
                "7. `pageContext`: Instance of `PageContext` (encapsulates entire page execution environment, provides access to all scopes).\n"
                "8. `page`: Instance of `Object` (reference to current servlet instance, equivalent to `this`).\n"
                "9. `exception`: Instance of `Throwable` (available strictly inside pages marked with `<%@ page isErrorPage=\"true\" %>`)."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                         JSP TRANSLATION & EXECUTION                     |\n"
                "+-------------------------------------------------------------------------+\n"
                "|                                                                         |\n"
                "|  Client Request: GET /index.jsp                                         |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  [ JSP Engine (Jasper) ]                                                |\n"
                "|         |                                                               |\n"
                "|         |-- (First Request Only) --> [ 1. Translation: index_jsp.java ] |\n"
                "|         |                                          |                    |\n"
                "|         |                                          v                    |\n"
                "|         |                            [ 2. Compilation: index_jsp.class] |\n"
                "|         |                                          |                    |\n"
                "|         |                                          v                    |\n"
                "|         |                            [ 3. jspInit() (Once) ]            |\n"
                "|         |                                          |                    |\n"
                "|         v                                          v                    |\n"
                "|  [ Container Thread Pool ] --------> [ 4. _jspService(req, res) ]       |\n"
                "|                                      (Executed for every request)       |\n"
                "|                                                    |                    |\n"
                "|                                                    v                    |\n"
                "|                                         HTML Stream sent to Browser     |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Implicit Object", "Underlying Java Type", "Functional Scope", "Typical Usage"],
                "rows": [
                    ["request", "javax.servlet.http.HttpServletRequest", "Request Scope", "Reading form inputs via req.getParameter()"],
                    ["response", "javax.servlet.http.HttpServletResponse", "Page Scope", "Setting cookies, HTTP headers, redirection"],
                    ["session", "javax.servlet.http.HttpSession", "Session Scope", "User authentication state, shopping cart"],
                    ["application", "javax.servlet.ServletContext", "Application Scope", "Global counter, shared DB connection pool"],
                    ["out", "javax.servlet.jsp.JspWriter", "Page Scope", "Printing dynamic HTML content to response buffer"],
                    ["pageContext", "javax.servlet.jsp.PageContext", "Page Scope", "Accessing attributes across page, request, session, app"],
                    ["exception", "java.lang.Throwable", "Page Scope", "Displaying stack trace on dedicated error pages"]
                ]
            },
            "memorize": "JSP compiles to a Servlet. 3 Directives: page, include, taglib. 9 Implicit objects: request, response, out, session, application, config, pageContext, page, exception. exception only exists when isErrorPage='true'.",
            "understand": "Why was JSP introduced if it compiles to a Servlet? Separation of concerns. Servlets mix heavy Java business logic with tedious `out.println('<html>')` string concatenations, which is unmaintainable for UI designers. JSP flips this: HTML is the default canvas, and Java is embedded only where dynamic data is required.",
            "common_mistakes": "1. Trying to access the `exception` object on a regular JSP page without setting `<%@ page isErrorPage=\"true\" %>`. 2. Writing database queries directly inside JSP scriptlets instead of delegating to backend DAO/Service classes.",
            "pyq_year": "CSJMU BCA-5002 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "High-Frequency 15-Mark Core Question (Appeared in 2021, 2022-23, 2023-24, 2024-25)",
            "pyq_question": "Explain the architecture and life cycle of JSP in detail. List and explain all the 9 implicit objects available in JSP with their underlying Java classes and scopes. Differentiate clearly between Servlets and JSP. (15 Marks)",
            "pyq_rubric": "JSP Architecture & Translation phases (4 marks) + 9 Implicit objects breakdown with table (6 marks) + JSP vs Servlet comparison (3 marks) + Life cycle methods: jspInit, _jspService, jspDestroy (2 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Architecture and Life Cycle of JSP:",
                 "JavaServer Pages (JSP) is an extension of Servlet technology designed for presentation rendering. When a client requests a `.jsp` page, the Web Container executes a two-phase lifecycle:\n"
                 "• Translation & Compilation: The JSP parser converts the JSP markup into a standard Java servlet source file (`_jsp.java`) and compiles it into executable bytecode (`_jsp.class`). This occurs strictly once unless the JSP source file is modified.\n"
                 "• Life Cycle Methods: The container calls `jspInit()` for one-time initialization, then dispatches each client request to `_jspService(HttpServletRequest, HttpServletResponse)`, and executes `jspDestroy()` when unloading the page."),
                ("2. The 9 Implicit Objects in JSP:",
                 "JSP provides 9 pre-instantiated implicit objects available automatically in scriptlets and expressions:\n"
                 "1. `request` (`HttpServletRequest`): Accesses client request headers, parameters, and cookies.\n"
                 "2. `response` (`HttpServletResponse`): Configures response MIME types, cookies, and HTTP redirects.\n"
                 "3. `out` (`JspWriter`): Buffered character stream writing dynamic HTML to the client browser.\n"
                 "4. `session` (`HttpSession`): Maintains conversational user state between requests.\n"
                 "5. `application` (`ServletContext`): Global application context shared by all users.\n"
                 "6. `config` (`ServletConfig`): Page-specific initialization parameters from web.xml.\n"
                 "7. `pageContext` (`PageContext`): Unified interface accessing all four variable scopes (page, request, session, application).\n"
                 "8. `page` (`Object`): Refers to the generated servlet instance itself (`this`).\n"
                 "9. `exception` (`Throwable`): Captures unhandled runtime errors, available only when `<%@ page isErrorPage=\"true\" %>` is declared."),
                ("3. Servlets vs JSP Comparative Analysis:",
                 "Servlets excel at handling controller logic, request routing, and business processing, but writing HTML via `out.println()` is clumsy. JSP excels at presentation and view templates because HTML is native, but embedding heavy business logic in JSPs leads to 'Spaghetti Code'. In modern enterprise architecture (MVC Pattern), Servlets act as Controllers while JSPs act as Views.")
            ]
        },
        "sgpa_target": {"focus": "Master JSP Translation Cycle & All 9 Implicit Objects", "milestone": "Full 15/15 on Java Web Technologies Exam Question"},
        "apt_data": {
            "topic": "Verbal Reasoning — Critical Reasoning: Statement & Assumptions / Arguments",
            "tutorial": [
                "Critical Reasoning tests deductive logic in verbal communication:\n"
                "1. Statement & Assumptions:\n"
                "• An assumption is something taken for granted or accepted as true without explicit proof before making the statement.\n"
                "• Validity Rule: An assumption is valid if the statement makes no sense without assuming it to be true.\n"
                "• Negation Test: If negating the assumption makes the statement fall apart or become completely pointless, the assumption is 100% IMPLICIT!\n"
                "2. Statement & Arguments (Strong vs Weak Arguments):\n"
                "• Strong Argument: Based on established facts, logical consequences, constitutional law, or universal truth. Directly addresses the core issue.\n"
                "• Weak Argument: Based on emotional appeals, vague opinions, comparisons with unrelated nations, or trivial reasons."
            ],
            "formulas": "Negation Test: If ~Assumption invalidates Statement ==> Assumption is Implicit. Strong arguments must be realistic and consequential.",
            "shortcut": "Reject Extreme Words: Assumptions containing words like 'only', 'best', 'always', 'never', 'all' are usually NOT implicit unless explicitly mandated by the statement.",
            "recognition": "Look for 'Statement: The government has decided to... Assumptions: I. People may... II. Other countries...' in TCS NQT and Infosys verbal rounds.",
            "tier1_problem": (
                "Statement: 'Please do not lean out of the window while the train is in motion.' — A notice in a railway coach.\n"
                "Assumptions:\n"
                "I. Leaning out of the window while moving is dangerous.\n"
                "II. Passengers are expected to read and follow railway notices."
            ),
            "tier1_solution": (
                "Apply Negation Test:\n"
                "• Negate Assumption I: 'Leaning out is completely safe.' If it is safe, posting a warning makes no sense! Therefore, Assumption I is IMPLICIT.\n"
                "• Negate Assumption II: 'Passengers will never read notices.' If nobody reads them, putting up a sign is futile! Therefore, Assumption II is IMPLICIT.\n"
                "Answer: Both Assumptions I and II are implicit."
            ),
            "tier2_problem": (
                "Statement: 'Switch to our high-speed fiber internet for uninterrupted video calling and streaming.' — An advertisement.\n"
                "Assumptions:\n"
                "I. People desire uninterrupted video calling and streaming.\n"
                "II. No other company provides high-speed internet."
            ),
            "tier2_solution": (
                "• Assumption I directly addresses consumer demand that makes advertising appealing ==> Implicit.\n"
                "• Assumption II uses extreme claim ('No other company') which is not implied by promoting one's own service ==> Not implicit.\n"
                "Answer: Only Assumption I is implicit."
            ),
            "tier3_problem": (
                "[TCS Digital Verbal Pattern]\n"
                "Statement: Should all examinations in colleges be conducted with open books?\n"
                "Arguments:\n"
                "I. Yes, because open-book exams test conceptual understanding and application rather than rote memorization.\n"
                "II. No, because students will stop studying and will simply copy directly from textbooks during the exam."
            ),
            "tier3_solution": (
                "• Argument I is strong because open-book exams are specifically designed to require higher-order analysis, problem-solving, and synthesis rather than textbook reproduction.\n"
                "• Argument II is weak because it assumes open-book questions are verbatim copies of text, misunderstanding the design of analytical open-book testing.\n"
                "Answer: Only Argument I is strong."
            ),
            "tier4_problem": (
                "Statement: 'In order to reduce traffic congestion, the municipal corporation will impose a congestion tax on private cars entering the central commercial district during peak hours.'\n"
                "Assumptions:\n"
                "I. The congestion tax will deter at least some private car owners from driving into the city center during peak hours.\n"
                "II. The public transport system has enough capacity to handle commuters who switch from cars."
            ),
            "tier4_solution": (
                "• Assumption I: If nobody is deterred by the fee, the policy will fail to reduce congestion. Hence, the administration must assume at least some behavioral shift ==> Implicit.\n"
                "• Assumption II: If the municipality implements this policy without assuming viable transit alternatives exist, the city would experience economic gridlock. Imposing disincentives presupposes alternative feasibility ==> Implicit.\n"
                "Answer: Both Assumptions I and II are implicit."
            ),
            "speed_drills": [
                {"q": "Statement: 'Buy pure ghee of brand X.' Assumption: People want pure ghee.", "a": "Implicit. Advertisements assume consumer demand for product qualities."},
                {"q": "Statement: 'Warning: Smoking causes cancer.' Assumption: Smokers want to read warnings.", "a": "Implicit. Public warnings assume visibility and public awareness."},
                {"q": "Statement: 'Enroll in our coding bootcamp to become a software engineer.' Assumption: Only our bootcamp makes engineers.", "a": "Not implicit. Word 'Only' makes it extreme."},
                {"q": "Argument: 'Should children use smartphones?' Arg: 'No, radiation destroys brains.'", "a": "Weak. Unsubstantiated sensational claim."},
                {"q": "Statement: 'Fly Airline A for lowest fares.' Assumption: Passengers prefer lower fares.", "a": "Implicit. Rationale for pricing-based marketing."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Word Break (LeetCode 139 - Medium)",
                "difficulty": "Medium",
                "importance": "High-Frequency Placement String DP Problem (Amazon, Google, TCS Digital)",
                "problem_statement": "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the same word in the dictionary may be reused multiple times.",
                "solution_approach": (
                    "Bottom-Up 1D Dynamic Programming:\n"
                    "1. Define `dp[i]` as boolean: can substring `s[0..i-1]` be segmented using dictionary words?\n"
                    "2. Base case: `dp[0] = True` (empty string is always valid).\n"
                    "3. Convert `wordDict` into a hash set for O(1) lookups.\n"
                    "4. For `i` from 1 to `len(s)`:\n"
                    "   For `j` from 0 to `i`:\n"
                    "     If `dp[j] is True` and `s[j..i]` is in word set:\n"
                    "       `dp[i] = True`, break inner loop.\n"
                    "5. Return `dp[len(s)]`."
                ),
                "code": (
                    "def wordBreak(s: str, wordDict: list[str]) -> bool:\n"
                    "    words = set(wordDict)\n"
                    "    dp = [False] * (len(s) + 1)\n"
                    "    dp[0] = True\n"
                    "    \n"
                    "    for i in range(1, len(s) + 1):\n"
                    "        for j in range(i):\n"
                    "            if dp[j] and s[j:i] in words:\n"
                    "                dp[i] = True\n"
                    "                break\n"
                    "                \n"
                    "    return dp[len(s)]"
                ),
                "line_by_line": [
                    ("words = set(wordDict)", "Hash set conversion enables O(1) word membership checks."),
                    ("dp = [False] * (len(s) + 1); dp[0] = True", "Initialize DP array where dp[i] denotes validity of prefix length i."),
                    ("if dp[j] and s[j:i] in words:", "Prefix up to j is valid AND remaining chunk s[j:i] is a dictionary word."),
                    ("dp[i] = True; break", "Mark prefix length i as valid and prune remaining inner searches.")
                ],
                "time_complexity": "O(N^2) where N is length of string s.",
                "space_complexity": "O(N) for DP array + O(W) for word set.",
                "edge_cases": "Single character string; word not found (returns False); all single-letter words."
            }
        ],
        "cs_core": {
            "subject": "Operating Systems",
            "topic": "Disk Scheduling Algorithms: FCFS, SSTF, SCAN (Elevator) & C-SCAN",
            "detailed_notes": [
                "Disk scheduling manages I/O request queues to minimize total disk head seek time (the time required to move the read/write head to the desired cylinder/track).",
                "Primary Algorithms Analyzed:\n"
                "1. FCFS (First-Come, First-Served): Services requests in arrival order. Simple and fair, but produces wild head swings and high average seek time.\n"
                "2. SSTF (Shortest Seek Time First): Services the request closest to current head position. Minimizes average seek time, but causes STARVATION for requests located far away from dense request clusters.\n"
                "3. SCAN (Elevator Algorithm): Head moves continuously in one direction servicing requests until it reaches the physical end of the disk, then reverses direction. Eliminates starvation.\n"
                "4. C-SCAN (Circular SCAN): Head moves in one direction servicing requests until the end, then immediately returns to the beginning of the disk WITHOUT servicing requests on the return trip. Provides uniform wait times across tracks."
            ],
            "interview_qa": [
                {
                    "q": "Why is SSTF disk scheduling rarely used in production operating systems despite lower average seek times?",
                    "a": "Because SSTF causes starvation. If a continuous stream of I/O requests arrives near the current head position, the disk head will remain hovering around that locality, and requests on distant cylinders will wait indefinitely. Production systems prefer SCAN or C-LOOK (Elevator algorithms) which guarantee bounded waiting times."
                },
                {
                    "q": "What is the difference between SCAN and C-SCAN?",
                    "a": "SCAN travels back and forth, servicing requests in both directions. In contrast, C-SCAN treats the cylinders as a circular list: it services requests in one direction only, and when it reaches the outer boundary, it rapidly sweeps back to the beginning without servicing requests on the return journey, providing uniform waiting times for all cylinders."
                }
            ]
        },
        "project_defense": {
            "project_name": "Deployment & CI/CD Engineering",
            "feature_focus": "Docker Containerization & GitHub Actions CI/CD for FastAPI Backends",
            "architecture_deep_dive": (
                "Standardizing Production Deployment across Sarthak's FastAPI Services:\n\n"
                "1. Multi-Stage Dockerfile Optimization:\n"
                "• Stage 1 (Builder): Uses `python:3.11-slim`, installs build tools (gcc, libpq-dev), and installs dependencies into a virtual environment.\n"
                "• Stage 2 (Runner): Copies only the virtual environment into a minimal base image, stripping compilers and build headers. Reduces container image size from 850MB to under 140MB!\n\n"
                "2. Automated CI/CD Workflow (`.github/workflows/deploy.yml`):\n"
                "• Triggers automatically on push to `main` branch.\n"
                "• Runs automated tests via `pytest` and linter checks (`ruff`/`black`).\n"
                "• On test pass, builds Docker image, pushes to GitHub Packages (GHCR), and triggers SSH webhook to restart container on the production VPS with zero downtime."
            ),
            "interview_qa": [
                {
                    "q": "Why do you use Multi-Stage builds in your Dockerfiles?",
                    "a": "Multi-stage builds allow me to separate the compilation environment from the final execution environment. Heavy build utilities, compilers, and development headers are isolated in the builder stage. Only the compiled wheels and runtime binaries are copied to the production image, drastically reducing the image footprint from 800MB+ to 140MB and minimizing attack surface vulnerabilities."
                },
                {
                    "q": "How do you ensure environment variables and API keys remain secure in CI/CD pipelines?",
                    "a": "I never commit `.env` files to Git. Secrets are stored in GitHub Repository Secrets and injected at runtime as environment variables. In Docker containers, secrets are passed via `docker run --env-file` or Docker Compose environment variables, running under a non-root user."
                }
            ]
        },
        "daily_test": {
            "day": 25,
            "questions": [
                {"q": "What happens during the Translation phase of a JSP file?", "a": "The JSP Engine translates the `.jsp` markup into a Java Servlet source file (`.java`)."},
                {"q": "Name 4 of the 9 implicit objects in JSP.", "a": "request, response, session, out, application, config, pageContext, page, exception."},
                {"q": "Under what condition is the `exception` implicit object accessible in a JSP?", "a": "Strictly when the page directive includes `<%@ page isErrorPage=\"true\" %>`."},
                {"q": "What is the primary drawback of the SSTF disk scheduling algorithm?", "a": "Starvation of distant track requests under heavy localized I/O traffic."},
                {"q": "How does C-SCAN differ from standard SCAN disk scheduling?", "a": "C-SCAN services requests in one direction only and returns directly to the start track without servicing requests on the return journey, ensuring uniform wait times."},
                {"q": "What is the time complexity of the DP solution for Word Break (LeetCode 139)?", "a": "O(N^2) where N is the length of the string."},
                {"q": "Why are extreme words ('all', 'never', 'only') usually red flags in Critical Reasoning assumptions?", "a": "Because real-world statements rarely warrant absolute, sweeping generalizations unless explicitly stated."},
                {"q": "What is the benefit of multi-stage Docker builds?", "a": "Separates the build environment from runtime, producing lightweight, secure container images without compiler dependencies."}
            ]
        }
    }

    # DAY 26
    days[26] = {
        "day": 26,
        "title": "Network Cryptography (AES & RSA), Kadane's Algorithm & Python Concurrency",
        "sem_data": {
            "subject": "BCA-5003 Computer Network",
            "topic": "Unit V — Network Security & Cryptography: Symmetric vs Asymmetric, RSA Algorithm & Digital Signatures",
            "detailed_notes": [
                "Cryptography secures network communication across untrusted channels, guaranteeing Confidentiality, Integrity, Authentication, and Non-Repudiation (the CIA-N triad).",
                "1. Symmetric Key Cryptography (Secret Key):\n"
                "• The sender and receiver share the EXACT SAME secret key for both encryption and decryption: Ciphertext C = E(K, P); Plaintext P = D(K, C).\n"
                "• Algorithms: AES (Advanced Encryption Standard: 128, 192, 256 bits), DES (56-bit key, obsolete), 3DES.\n"
                "• Advantages: Highly optimized in hardware, extremely fast throughput (megabytes per second), minimal CPU overhead.\n"
                "• The Key Distribution Problem: How can sender and receiver agree on a shared secret key across an insecure network without an eavesdropper intercepting it? (Requires n*(n-1)/2 keys for n users!).",
                "2. Asymmetric Key Cryptography (Public Key):\n"
                "• Uses a mathematically linked Key Pair: a Public Key (distributed openly) and a Private Key (kept strictly confidential).\n"
                "• Encryption: Anyone can encrypt using the recipient's Public Key: C = E(PU_receiver, P). Decryption: ONLY the recipient's Private Key can decrypt: P = D(PR_receiver, C).\n"
                "• Key Management: Each user requires only 1 key pair (2n keys total for n users).\n"
                "• Disadvantage: Computationally intensive (1000x slower than symmetric AES).",
                "3. The RSA Algorithm (Rivest, Shamir, Adleman):\n"
                "Based on the mathematical difficulty of factoring the product of two large prime numbers:\n"
                "• Step 1: Select two distinct large prime numbers p and q.\n"
                "• Step 2: Compute n = p * q (the modulus, part of public and private keys).\n"
                "• Step 3: Compute Euler's Totient function phi(n) = (p - 1) * (q - 1).\n"
                "• Step 4: Choose public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1 (typically e = 65537).\n"
                "• Step 5: Compute private exponent d such that d * e = 1 mod phi(n) (Modular Multiplicative Inverse: d = e^(-1) mod phi(n)).\n"
                "• Public Key = (e, n); Private Key = (d, n).\n"
                "• Encryption: C = (M^e) mod n.\n"
                "• Decryption: M = (C^d) mod n.",
                "4. Digital Signatures & Message Digests:\n"
                "• Ensures sender authenticity and non-repudiation: Sender hashes the message (using SHA-256) and ENCRYPTS the hash with their own PRIVATE KEY!\n"
                "• Receiver decrypts the signature using the sender's PUBLIC KEY and compares it against a freshly computed SHA-256 hash. If hashes match, the message is authentic and untampered."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                    RSA PUBLIC KEY ENCRYPTION & SIGNING                  |\n"
                "+-------------------------------------------------------------------------+\n"
                "|                                                                         |\n"
                "|  1. CONFIDENTIALITY (Encryption):                                       |\n"
                "|     Plaintext M ---> [ Encrypt with Bob's PUBLIC Key ] ---> Ciphertext C|\n"
                "|                                                                   |     |\n"
                "|     Plaintext M <--- [ Decrypt with Bob's PRIVATE Key ] <---------+     |\n"
                "|                                                                         |\n"
                "|  2. AUTHENTICATION & NON-REPUDIATION (Digital Signature):               |\n"
                "|     Message M ---> [ SHA-256 ] ---> Hash                                |\n"
                "|                                      |                                  |\n"
                "|     Signature S <--- [ Encrypt with Alice's PRIVATE Key ] <-------------+     |\n"
                "|                                                                         |\n"
                "|     Verify: Decrypt Signature S with Alice's PUBLIC Key === Hash?        |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Comparison Feature", "Symmetric Cryptography (AES)", "Asymmetric Cryptography (RSA)"],
                "rows": [
                    ["Keys Used", "Single shared secret key for encryption & decryption", "Key pair: Public key (encrypt) & Private key (decrypt)"],
                    ["Execution Speed", "Extremely fast (Hardware AES-NI instructions)", "Slow (1000x slower due to large modular exponentiation)"],
                    ["Key Distribution", "Complex (must securely share secret key)", "Simple (public keys shared openly over network)"],
                    ["Total Keys in Network", "n * (n - 1) / 2 keys for n users", "2 * n keys for n users (1 key pair per user)"],
                    ["Primary Use Case", "Bulk data payload encryption (HTTPS data frames)", "Key exchange (TLS session key agreement) & Digital Signatures"]
                ]
            },
            "memorize": "Symmetric: 1 key, fast, bulk data (AES). Asymmetric: 2 keys, slow, key exchange (RSA). RSA math: n = p*q, phi = (p-1)*(q-1), d = e^(-1) mod phi. C = M^e mod n; M = C^d mod n.",
            "understand": "How does HTTPS combine both? Hybrid Cryptography! Asymmetric RSA/Diffie-Hellman is used strictly during the initial 1-second TLS handshake to securely negotiate a random 256-bit symmetric session key. Once negotiated, all subsequent gigabytes of webpage data are encrypted using lightning-fast symmetric AES.",
            "common_mistakes": "1. Thinking RSA encrypts bulk files directly (too slow, produces huge CPU spikes). 2. Confusing Digital Signatures (signed with sender's private key) with Confidentiality (encrypted with receiver's public key).",
            "pyq_year": "CSJMU BCA-5003 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "High-Frequency 15-Mark Core Question (Appeared in 2021, 2022-23, 2023-24, 2024-25)",
            "pyq_question": "Explain the difference between Symmetric and Asymmetric Cryptography. Describe the RSA algorithm step-by-step. Perform RSA encryption and decryption for primes p = 3, q = 11, e = 7, and message M = 2. (15 Marks)",
            "pyq_rubric": "Symmetric vs Asymmetric comparison (4 marks) + RSA algorithm mathematical derivation (5 marks) + Step-by-step numerical calculation with p=3, q=11, e=7, M=2 (6 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Symmetric vs Asymmetric Cryptography:",
                 "Symmetric encryption (e.g. AES, DES) uses a single secret key shared by sender and receiver. It offers superior throughput for high-volume data but suffers from key distribution complexity. Asymmetric encryption (e.g. RSA, ECC) utilizes mathematically coupled public and private keys, solving the key distribution dilemma and enabling digital signatures at the expense of computational overhead."),
                ("2. The RSA Algorithm Mathematical Steps:",
                 "1. Select primes p and q.\n"
                 "2. Modulus n = p * q.\n"
                 "3. Euler's Totient phi(n) = (p - 1) * (q - 1).\n"
                 "4. Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1.\n"
                 "5. Compute d = e^(-1) mod phi(n), satisfying (d * e) mod phi(n) = 1.\n"
                 "6. Ciphertext C = (M^e) mod n. Decryption M = (C^d) mod n."),
                ("3. Complete Hand Numerical Solution (p=3, q=11, e=7, M=2):",
                 "• Step 1: p = 3, q = 11.\n"
                 "• Step 2: n = p * q = 3 * 11 = 33.\n"
                 "• Step 3: phi(n) = (3 - 1) * (11 - 1) = 2 * 10 = 20.\n"
                 "• Step 4: Given e = 7. Verify gcd(7, 20) = 1. Valid.\n"
                 "• Step 5: Find d such that (d * 7) mod 20 = 1.\n"
                 "  Test multiples of 20 plus 1:\n"
                 "  (1 * 20 + 1) = 21. Is 21 divisible by 7? Yes: 21 / 7 = 3.\n"
                 "  Therefore, private key d = 3! (Check: 7 * 3 = 21 = 1 mod 20).\n"
                 "  Public Key = (e=7, n=33); Private Key = (d=3, n=33).\n\n"
                 "• Step 6 (Encryption of M = 2):\n"
                 "  C = (M^e) mod n = (2^7) mod 33.\n"
                 "  2^7 = 128.\n"
                 "  128 / 33 = 3 with remainder: 128 - (3 * 33) = 128 - 99 = 29.\n"
                 "  Transmitted Ciphertext C = 29!\n\n"
                 "• Step 7 (Decryption of C = 29):\n"
                 "  M = (C^d) mod n = (29^3) mod 33.\n"
                 "  Notice: 29 = -4 mod 33.\n"
                 "  29^3 = (-4)^3 mod 33 = -64 mod 33.\n"
                 "  -64 = -2 * 33 + 2 = -66 + 2.\n"
                 "  Therefore, -64 mod 33 = 2!\n"
                 "  Decrypted Message M = 2. Exact match with original message!")
            ]
        },
        "sgpa_target": {"focus": "Master RSA Mathematical Steps & Modular Arithmetic", "milestone": "Full 15/15 on Networks Unit V Exam Question"},
        "apt_data": {
            "topic": "Verbal Ability — Sentence Correction, Error Spotting & Reading Comprehension",
            "tutorial": [
                "Top Grammar Rules for Placement Verbal Rounds (TCS NQT, Infosys, Cognizant):\n"
                "1. Subject-Verb Agreement: Singular subjects take singular verbs; plural subjects take plural verbs.\n"
                "• Words joined by 'with', 'as well as', 'along with': Verb agrees with the FIRST subject! ('The manager, along with his team, is arriving').\n"
                "• 'Either... or' / 'Neither... nor': Verb agrees with the NEAREST subject! ('Neither the teacher nor the students were present').\n"
                "2. Dangling Modifiers: An introductory modifying participle phrase must be immediately followed by the noun it describes. ('Walking down the street, a tree fell on him' is incorrect—the tree wasn't walking!).\n"
                "3. Parallelism: Elements in a list or comparison must maintain identical grammatical forms ('He likes swimming, running, and to cycle' ==> change to 'cycling')."
            ],
            "formulas": "Along with/as well as ==> agrees with Subject 1. Neither/nor ==> agrees with Subject 2. Lists must share parallel structure (-ing with -ing).",
            "shortcut": "Identify the Real Subject: Ignore prepositional phrases between the subject and verb (e.g. 'The quality [of these mangoes] is excellent').",
            "recognition": "Error spotting questions with marked segments [A] / [B] / [C] / [D] in TCS NQT and Wipro.",
            "tier1_problem": "Identify the error: 'Each of the participants [A] / were given [B] / a certificate [C] / upon completion [D].'",
            "tier1_solution": "'Each' is a singular indefinite pronoun. The subject is 'Each', not 'participants'. A singular subject requires the singular verb 'was given'. Error is in part [B]. Correct sentence: 'Each of the participants was given a certificate'. Answer: [B].",
            "tier2_problem": "Identify the error: 'Neither the principal [A] / nor the lecturers [B] / was present [C] / at the annual conference [D].'",
            "tier2_solution": "Rule of proximity: In 'neither... nor', the verb agrees with the closer subject ('the lecturers', plural). Plural subject requires 'were present'. Error is in part [C]. Answer: [C].",
            "tier3_problem": "[Infosys Verbal Pattern] Choose the grammatically correct sentence:\n(A) Not only did she won the competition, but also broke the national record.\n(B) Not only she won the competition, but also she broke the record.\n(C) Not only did she win the competition, but she also broke the national record.\n(D) She won not only the competition, but broke also the national record.",
            "tier3_solution": "Rule of Inversion with 'Not only': When 'not only' begins a clause, auxiliary verb inversion is required ('did she win', base verb). Furthermore, correlative conjunctions require balanced parallel placement: 'did she win' paired with 'she also broke'. Sentence (C) correctly implements inversion and parallelism. Answer: (C).",
            "tier4_problem": "Correct the dangling modifier: 'Having finished the examination, the papers were collected by the invigilator.'",
            "tier4_solution": "The introductory participial phrase 'Having finished the examination' grammatically attaches to the immediately following subject 'the papers'. But papers cannot finish an examination! The logical subject is the students. Correct revision: 'Having finished the examination, the students handed their papers to the invigilator.'",
            "speed_drills": [
                {"q": "The committee [have/has] submitted its report.", "a": "'has'. Committee acting as a collective single unit with 'its'."},
                {"q": "Bread and butter [is/are] his favorite breakfast.", "a": "'is'. Representing a single composite culinary dish."},
                {"q": "One of my friends [is/are] an engineer.", "a": "'is'. The subject is 'One', not 'friends'."},
                {"q": "Ten miles [is/are] a long distance to walk.", "a": "'is'. A specific quantitative unit of measurement treated as singular."},
                {"q": "He is senior [than/to] me.", "a": "'to'. Latin adjectives (senior, junior, prior, superior) take 'to', not 'than'."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Maximum Subarray (LeetCode 53 - Kadane's Algorithm)",
                "difficulty": "Medium",
                "importance": "Top 3 Most Asked Placement Problem Worldwide (Amazon, Microsoft, TCS)",
                "problem_statement": "Given an integer array nums, find the subarray with the largest sum, and return its sum.",
                "solution_approach": (
                    "Kadane's Algorithm (Greedy / DP in O(N)):\n"
                    "1. Maintain two variables: `max_so_far` and `curr_max`.\n"
                    "2. Initialize both to `nums[0]`.\n"
                    "3. For each number x from index 1 onward:\n"
                    "   `curr_max = max(x, curr_max + x)`\n"
                    "   (Either start a brand new subarray at x, or extend the existing running subarray).\n"
                    "4. `max_so_far = max(max_so_far, curr_max)`.\n"
                    "5. Return `max_so_far`."
                ),
                "code": (
                    "def maxSubArray(nums: list[int]) -> int:\n"
                    "    max_so_far = nums[0]\n"
                    "    curr_max = nums[0]\n"
                    "    \n"
                    "    for x in nums[1:]:\n"
                    "        curr_max = max(x, curr_max + x)\n"
                    "        max_so_far = max(max_so_far, curr_max)\n"
                    "        \n"
                    "    return max_so_far"
                ),
                "line_by_line": [
                    ("max_so_far = nums[0]; curr_max = nums[0]", "Initialize baselines to first element to handle all-negative arrays correctly."),
                    ("curr_max = max(x, curr_max + x)", "Decide whether to discard accumulated debt or extend subarray."),
                    ("max_so_far = max(max_so_far, curr_max)", "Update global maximum.")
                ],
                "time_complexity": "O(N) single linear traversal.",
                "space_complexity": "O(1) constant auxiliary memory.",
                "edge_cases": "All negative numbers [-5, -2, -8] (returns -2); single element array [1]."
            },
            {
                "title": "Maximum Product Subarray (LeetCode 152 - Medium)",
                "difficulty": "Medium",
                "importance": "High-Frequency Extension Tracking Negative Inversions",
                "problem_statement": "Given an integer array nums, find a subarray that has the largest product, and return the product.",
                "solution_approach": (
                    "Dual-Tracking Dynamic Programming:\n"
                    "Multiplying two negative numbers produces a positive number! A large negative product can instantly flip to the maximum positive product.\n"
                    "Maintain BOTH `curr_max` and `curr_min` simultaneously.\n"
                    "When encountering a negative number, swap `curr_max` and `curr_min` before computing new states."
                ),
                "code": (
                    "def maxProduct(nums: list[int]) -> int:\n"
                    "    res = max(nums)\n"
                    "    cur_min, cur_max = 1, 1\n"
                    "    \n"
                    "    for n in nums:\n"
                    "        if n < 0:\n"
                    "            cur_max, cur_min = cur_min, cur_max\n"
                    "            \n"
                    "        cur_max = max(n, cur_max * n)\n"
                    "        cur_min = min(n, cur_min * n)\n"
                    "        res = max(res, cur_max)\n"
                    "        \n"
                    "    return res"
                ),
                "line_by_line": [
                    ("if n < 0: cur_max, cur_min = cur_min, cur_max", "Negative multiplier inverts signs: maximum becomes minimum and vice-versa."),
                    ("cur_max = max(n, cur_max * n)", "Update running maximum product."),
                    ("cur_min = min(n, cur_min * n)", "Update running minimum product to prepare for future negative flips.")
                ],
                "time_complexity": "O(N) single pass.",
                "space_complexity": "O(1) space.",
                "edge_cases": "Array containing zeros [2, 0, 3]; all negative numbers [-2, -3, -4]."
            }
        ],
        "cs_core": {
            "subject": "Python Programming",
            "topic": "Python Concurrency Models: Threading vs Multiprocessing vs AsyncIO",
            "detailed_notes": [
                "CPython Concurrency Paradigms Explained:\n"
                "1. Global Interpreter Lock (GIL):\n"
                "A mutual-exclusion lock protecting CPython internal memory structures, ensuring only ONE native thread executes Python bytecode at any given moment. Prevents true multi-core parallel execution of CPU-bound Python threads.\n"
                "2. Threading (`threading.Thread`):\n"
                "• OS-level threads sharing the same process memory space.\n"
                "• Best for: I/O-bound tasks (file I/O, network requests). When a thread waits for a socket or disk read, it releases the GIL, allowing other threads to run.\n"
                "3. Multiprocessing (`multiprocessing.Process`):\n"
                "• Spawns completely independent OS processes, each with its OWN Python interpreter, memory space, and GIL.\n"
                "• Best for: CPU-bound tasks (machine learning inference, OCR image processing, heavy matrix math). Achieves true 100% multi-core utilization.\n"
                "• Trade-off: Higher memory footprint and requires Inter-Process Communication (IPC: Pipes/Queues) to share data.\n"
                "4. Asynchronous I/O (`asyncio`):\n"
                "• Single-threaded, cooperative multitasking using an Event Loop and Coroutines (`async`/`await`).\n"
                "• Extremely lightweight: can handle 100,000 concurrent network sockets with minimal RAM (used in FastAPI and aiohttp)."
            ],
            "interview_qa": [
                {
                    "q": "If Python has a GIL, why would you ever use `threading`?",
                    "a": "Because `threading` is highly effective for I/O-bound operations (such as making HTTP requests, querying a database, or reading disk files). During I/O operations, the CPython runtime explicitly releases the GIL while waiting for network sockets or OS syscalls to return, enabling other Python threads to execute concurrently without blocking the application."
                },
                {
                    "q": "When should you choose `multiprocessing` over `asyncio`?",
                    "a": "Choose `multiprocessing` for CPU-intensive operations (such as Tesseract OCR image transformations in TerraStract or numerical simulations in BCA-5004) where multiple CPU cores must be saturated simultaneously. Choose `asyncio` for high-concurrency I/O-bound web services (such as handling thousands of WebSocket connections or Telegram webhook alerts in BulkBeat TV) where threads would waste excessive memory on thread stack allocations."
                }
            ]
        },
        "project_defense": {
            "project_name": "VPS Infrastructure & Security",
            "feature_focus": "Cloud VPS Hardening, Nginx Reverse Proxy & SSL Automation",
            "architecture_deep_dive": (
                "Production Linux Server Hardening & Reverse Proxy Architecture:\n\n"
                "1. Server Hardening Protocol:\n"
                "• Disabling SSH root login and password authentication (`PermitRootLogin no`, `PasswordAuthentication no` in `/etc/ssh/sshd_config`).\n"
                "• Enforcing SSH key pair authentication (`ed25519`).\n"
                "• Configuring Uncomplicated Firewall (`ufw`): strictly allow ports 22 (SSH), 80 (HTTP), 443 (HTTPS), blocking all internal database ports (PostgreSQL 5432, Redis 6379) from public internet exposure.\n\n"
                "2. Nginx Reverse Proxy & TLS Automation:\n"
                "• Nginx sits as the public gateway, terminating SSL using Let's Encrypt certificates provisioned via Certbot (`certbot --nginx -d api.domain.com`).\n"
                "• Reverse proxies traffic internally to FastAPI/Uvicorn running on `127.0.0.1:8000` via `proxy_pass`.\n"
                "• Injects essential security headers: `X-Forwarded-For`, `X-Real-IP`, `Strict-Transport-Security` (HSTS), and `X-Content-Type-Options: nosniff`."
            ),
            "interview_qa": [
                {
                    "q": "Why should you never expose a FastAPI application directly to the internet on port 80/443 without Nginx?",
                    "a": "Direct exposure leaves the application vulnerable to Slowloris attacks, unhandled TLS certificate lifecycles, and high concurrency bottlenecks. Nginx acts as a hardened reverse proxy: it terminates SSL efficiently, buffers slow client requests before passing them to FastAPI, serves static assets directly from disk caching, enforces rate limits, and protects internal application ports."
                },
                {
                    "q": "How do you automate SSL certificate renewal on a production Linux VPS?",
                    "a": "I configure Certbot with Let's Encrypt, which automatically schedules a systemd timer (`certbot.timer`) or cron job running `certbot renew --quiet`. This checks certificate expiration daily and renews certificates within 30 days of expiry, reloading Nginx automatically without manual intervention."
                }
            ]
        },
        "daily_test": {
            "day": 26,
            "questions": [
                {"q": "What is the key difference between Symmetric and Asymmetric encryption?", "a": "Symmetric uses a single shared secret key for encryption and decryption; Asymmetric uses a mathematically linked pair: Public Key (encrypt) and Private Key (decrypt)."},
                {"q": "Given RSA parameters p = 3, q = 11, compute Euler's Totient phi(n).", "a": "phi(n) = (3 - 1) * (11 - 1) = 2 * 10 = 20."},
                {"q": "How does a Digital Signature ensure Non-Repudiation?", "a": "The sender encrypts the message hash using their private key. Since only the sender possesses that private key, successful decryption using their public key proves indisputably that the sender generated the message."},
                {"q": "What is the time complexity of Kadane's Algorithm for Maximum Subarray?", "a": "O(N) single linear traversal with O(1) auxiliary space."},
                {"q": "Why does Python's GIL not prevent concurrency for I/O-bound operations?", "a": "Because CPython explicitly releases the GIL when waiting for I/O operations (sockets, disk reads), allowing other threads to execute."},
                {"q": "When should you use Multiprocessing instead of Threading in Python?", "a": "For CPU-bound tasks requiring true multi-core parallel computation, bypassing the GIL by running independent Python processes."},
                {"q": "Correct the error: 'The list of items are on the desk.'", "a": "'is on the desk'. The subject is singular 'list', not 'items'."},
                {"q": "Why should database ports (5432, 6379) be blocked by UFW firewall on a production VPS?", "a": "To prevent unauthorized brute-force and port-scanning attacks over the public internet, restricting database access exclusively to localhost or private VPC networks."}
            ]
        }
    }

    # DAY 27
    days[27] = {
        "day": 27,
        "title": "Ordinary Differential Equations (RK4), Speed Math Marathon & Backtracking",
        "sem_data": {
            "subject": "BCA-5004 Numerical Methods",
            "topic": "Unit V — Numerical Solution of Ordinary Differential Equations (ODEs): Euler's Method & Runge-Kutta 4th Order (RK4)",
            "detailed_notes": [
                "An Initial Value Problem (IVP) for a first-order Ordinary Differential Equation is defined as: dy/dx = f(x, y), with initial condition y(x0) = y0. Numerical methods generate discrete approximations y1, y2, ..., yn at points x1, x2, ..., xn separated by uniform step size h.",
                "1. Euler's Method (First-Order):\n"
                "• Approximates curve by tangent line at initial point: y_{n+1} = y_n + h * f(x_n, y_n).\n"
                "• Truncation Error: Local error = O(h^2); Global error = O(h). Computationally crude; requires very small h to prevent runaway error accumulation.",
                "2. Modified Euler's Method (Predictor-Corrector / Heun's Method):\n"
                "• Predictor: y*_{n+1} = y_n + h * f(x_n, y_n).\n"
                "• Corrector: y_{n+1} = y_n + (h/2) * [ f(x_n, y_n) + f(x_{n+1}, y*_{n+1}) ].\n"
                "• Global Error = O(h^2). Averages slopes at beginning and predicted end of interval.",
                "3. Runge-Kutta 4th Order Method (RK4):\n"
                "• The industry-standard gold standard for solving initial value problems numerically without needing higher-order analytical derivatives!\n"
                "• Computes a weighted average of 4 sample slopes across the step interval [x_n, x_n + h]:\n"
                "  k1 = h * f(x_n, y_n)                     [Slope at beginning of interval]\n"
                "  k2 = h * f(x_n + h/2, y_n + k1/2)         [Slope at midpoint using slope k1]\n"
                "  k3 = h * f(x_n + h/2, y_n + k2/2)         [Slope at midpoint using slope k2]\n"
                "  k4 = h * f(x_n + h, y_n + k3)             [Slope at end of interval using slope k3]\n"
                "• Step Update Formula: y_{n+1} = y_n + (1/6) * [ k1 + 2*k2 + 2*k3 + k4 ].\n"
                "• Global Truncation Error = O(h^4). Fourth-order accuracy achieves precision with large step sizes."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                  RUNGE-KUTTA 4TH ORDER (RK4) SLOPE WEIGHTING            |\n"
                "+-------------------------------------------------------------------------+\n"
                "|  y ^                                                                    |\n"
                "|    |                               * (x+h, y + k4)                      |\n"
                "|    |               * k2, k3        /                                    |\n"
                "|    |              / (Midpoint)    /                                     |\n"
                "|    |       k1    /               /                                      |\n"
                "|    |  * --------*---------------*                                       |\n"
                "|    | (x0, y0)                                                           |\n"
                "|    +----+---------------+-------+-----> x                               |\n"
                "|        x0             x0+h/2   x0+h                                     |\n"
                "|  Weighted Slope = (k1 + 2*k2 + 2*k3 + k4) / 6  ==> O(h^4) Precision!   |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Method", "Formula Order", "Function Evaluations per Step", "Global Error", "Computational Stability"],
                "rows": [
                    ["Euler's Method", "1st Order", "1 evaluation: f(xn, yn)", "O(h) — Poor", "Unstable for large h"],
                    ["Modified Euler", "2nd Order", "2 evaluations: f(xn, yn) & f(x*, y*)", "O(h^2) — Moderate", "Fair stability"],
                    ["Runge-Kutta 4th Order", "4th Order", "4 evaluations: k1, k2, k3, k4", "O(h^4) — Exceptional", "Highly stable and accurate"]
                ]
            },
            "memorize": "RK4 Formulas: k1 = h*f(x, y); k2 = h*f(x + h/2, y + k1/2); k3 = h*f(x + h/2, y + k2/2); k4 = h*f(x + h, y + k3). y(next) = y + (k1 + 2*k2 + 2*k3 + k4)/6. Global Error = O(h^4).",
            "understand": "Why is RK4 favored over Taylor Series expansion? Both achieve O(h^4) accuracy. However, Taylor Series requires calculating high-order analytical partial derivatives (f', f'', f'''), which are mathematically horrific or impossible for complex empirical functions. RK4 achieves the identical 4th-order accuracy purely through function evaluations without evaluating a single derivative!",
            "common_mistakes": "1. Forgetting to divide k1 and k2 by 2 inside the arguments for k2 and k3: `y + k1/2`. 2. Forgetting the leading (1/6) factor in the final increment sum.",
            "pyq_year": "CSJMU BCA-5004 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "4 Consecutive University Sessions (Q8/Q9 - 15 Marks Core Final Question)",
            "pyq_question": "Apply Runge-Kutta 4th order method to find an approximate value of y when x = 0.1, given that dy/dx = x + y, with initial condition y(0) = 1. Take step size h = 0.1. (15 Marks)",
            "pyq_rubric": "Formula statement for k1, k2, k3, k4 (3 marks) + Accurate hand evaluation of k1, k2, k3, k4 (8 marks) + Final y(0.1) value (3 marks) + Comparison with analytical solution (1 mark) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Statement of Initial Value Problem and RK4 Formulas:",
                 "Given ODE: dy/dx = f(x, y) = x + y.\n"
                 "Initial conditions: x0 = 0, y0 = 1, step size h = 0.1. Goal: find y(0.1).\n"
                 "RK4 Step Formulas:\n"
                 "k1 = h * f(x0, y0)\n"
                 "k2 = h * f(x0 + h/2, y0 + k1/2)\n"
                 "k3 = h * f(x0 + h/2, y0 + k2/2)\n"
                 "k4 = h * f(x0 + h, y0 + k3)\n"
                 "y1 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)"),
                ("2. Hand Calculation of Slopes (k1, k2, k3, k4):",
                 "• Calculation of k1:\n"
                 "k1 = 0.1 * f(0, 1) = 0.1 * (0 + 1) = 0.100000.\n\n"
                 "• Calculation of k2:\n"
                 "x0 + h/2 = 0 + 0.05 = 0.05\n"
                 "y0 + k1/2 = 1 + 0.100000 / 2 = 1.050000\n"
                 "k2 = 0.1 * f(0.05, 1.05) = 0.1 * (0.05 + 1.050000) = 0.1 * 1.100000 = 0.110000.\n\n"
                 "• Calculation of k3:\n"
                 "x0 + h/2 = 0.05\n"
                 "y0 + k2/2 = 1 + 0.110000 / 2 = 1.055000\n"
                 "k3 = 0.1 * f(0.05, 1.055) = 0.1 * (0.05 + 1.055000) = 0.1 * 1.105000 = 0.110500.\n\n"
                 "• Calculation of k4:\n"
                 "x0 + h = 0 + 0.1 = 0.1\n"
                 "y0 + k3 = 1 + 0.110500 = 1.110500\n"
                 "k4 = 0.1 * f(0.1, 1.1105) = 0.1 * (0.1 + 1.110500) = 0.1 * 1.210500 = 0.121050."),
                ("3. Final Step Update:",
                 "y(0.1) = y0 + (1/6) * [ k1 + 2*k2 + 2*k3 + k4 ]\n"
                 "Sum of weighted slopes:\n"
                 "k1 + 2*k2 + 2*k3 + k4 = 0.100000 + 2*(0.110000) + 2*(0.110500) + 0.121050\n"
                 "= 0.100000 + 0.220000 + 0.221000 + 0.121050 = 0.662050.\n"
                 "y(0.1) = 1 + (0.662050 / 6) = 1 + 0.1103417 = 1.110342.\n\n"
                 "Analytical Verification:\n"
                 "The exact analytical solution of dy/dx - y = x with y(0)=1 is y(x) = 2*e^x - x - 1.\n"
                 "At x = 0.1: y(0.1) = 2*e^0.1 - 0.1 - 1 = 2*(1.1051709) - 1.1 = 2.2103418 - 1.1 = 1.110342!\n"
                 "RK4 solution matches the exact analytical answer to SIX decimal places in a single step!")
            ]
        },
        "sgpa_target": {"focus": "Master RK4 Step-by-Step Hand Evaluation", "milestone": "Full 15/15 on Numerical ODE Exam Question"},
        "apt_data": {
            "topic": "Quantitative Aptitude — Rapid Speed Math Marathon (25 High-Frequency Placement Drills)",
            "tutorial": [
                "Final Quantitative Crunch — Solving questions under extreme time limits:\n"
                "• Percentage to Fraction Conversions: 16.66% = 1/6 | 14.28% = 1/7 | 12.5% = 1/8 | 11.11% = 1/9 | 9.09% = 1/11.\n"
                "• Compound Interest 2-Year Difference: D = P * (R / 100)^2.\n"
                "• Time and Work Efficiency: Efficiency is inversely proportional to time taken. Total Work = LCM of individual times.\n"
                "• Relative Speed: Same direction = S1 - S2; Opposite direction = S1 + S2."
            ],
            "formulas": "CI-SI 2-Yr Diff: D = P(R/100)^2. Harm. Mean: 2ab/(a+b). Work = Rate * Time.",
            "shortcut": "Unit Digit & Option Elimination: Before doing full multiplication, compute only the last digit (e.g. 7 * 3 = 1) to eliminate 3 out of 4 options immediately.",
            "recognition": "Mixed rapid-fire sections appearing in round 1 online placement assessments across recruiters.",
            "tier1_problem": "A sum of money doubles itself at simple interest in 5 years. What is the rate of interest per annum?",
            "tier1_solution": "Simple Interest SI = Principal P. SI = (P * R * T) / 100 ==> P = (P * R * 5) / 100 ==> R = 100 / 5 = 20% p.a. Answer: 20%.",
            "tier2_problem": "The difference between CI and SI on a sum of Rs 5,000 for 2 years at 10% per annum is?",
            "tier2_solution": "D = P * (R / 100)^2 = 5000 * (10 / 100)^2 = 5000 * (1/100) = Rs 50. Answer: Rs 50.",
            "tier3_problem": "A can do a piece of work in 12 days and B in 18 days. They worked together for 4 days, then A left. How many days will B take to finish the remaining work?",
            "tier3_solution": "Total Work = LCM(12, 18) = 36 units.\nA's efficiency = 36 / 12 = 3 units/day.\nB's efficiency = 36 / 18 = 2 units/day.\nCombined efficiency = 3 + 2 = 5 units/day.\nWork done in 4 days = 4 * 5 = 20 units.\nRemaining work = 36 - 20 = 16 units.\nTime taken by B = 16 / 2 = 8 days. Answer: 8 days.",
            "tier4_problem": "A train traveling at 72 km/h crosses a 200m long platform in 22 seconds. What is the length of the train?",
            "tier4_solution": "Speed in m/s = 72 * (5 / 18) = 20 m/s.\nTotal distance covered = Speed * Time = 20 * 22 = 440 m.\nTotal distance = Length of train + Length of platform.\n440 = Length of train + 200 ==> Length of train = 240 m. Answer: 240 m.",
            "speed_drills": [
                {"q": "What is 12.5% of 640?", "a": "1/8 of 640 = 80."},
                {"q": "A car covers 180 km in 3 hours. Speed in m/s?", "a": "60 km/h * (5/18) = 16.67 m/s."},
                {"q": "Cost Price = Rs 400, Selling Price = Rs 500. Profit %?", "a": "(100 / 400) * 100 = 25%."},
                {"q": "Ratio of ages of A and B is 3:4. Sum is 35 years. Age of A?", "a": "3/7 * 35 = 15 years."},
                {"q": "If 15 workers build a wall in 48 hours, how many hours for 30 workers?", "a": "15 * 48 / 30 = 24 hours."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Combination Sum (LeetCode 39 - Medium)",
                "difficulty": "Medium",
                "importance": "The Fundamental Backtracking Placement Problem (Amazon, Microsoft, Google)",
                "problem_statement": "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times.",
                "solution_approach": (
                    "Decision Tree Backtracking:\n"
                    "At each recursive step, we decide whether to INCLUDE the candidate at index `i` or SKIP it:\n"
                    "1. Include `candidates[i]`: append to current path, recursively call with `target - candidates[i]` and same index `i` (unlimited reuse).\n"
                    "2. Skip `candidates[i]`: pop from path, recursively call with same target and index `i + 1`.\n"
                    "Base Cases: if `target == 0`, record path; if `target < 0` or `i >= len`, backtrack."
                ),
                "code": (
                    "def combinationSum(candidates: list[int], target: int) -> list[list[int]]:\n"
                    "    res = []\n"
                    "    \n"
                    "    def dfs(i: int, cur: list[int], total: int):\n"
                    "        if total == target:\n"
                    "            res.append(cur[:])\n"
                    "            return\n"
                    "        if i >= len(candidates) or total > target:\n"
                    "            return\n"
                    "            \n"
                    "        # Choice 1: Include candidates[i]\n"
                    "        cur.append(candidates[i])\n"
                    "        dfs(i, cur, total + candidates[i])\n"
                    "        cur.pop() # Backtrack\n"
                    "        \n"
                    "        # Choice 2: Skip candidates[i]\n"
                    "        dfs(i + 1, cur, total)\n"
                    "        \n"
                    "    dfs(0, [], 0)\n"
                    "    return res"
                ),
                "line_by_line": [
                    ("if total == target: res.append(cur[:])", "Base case success: deep-copy valid combination path."),
                    ("cur.append(candidates[i]); dfs(i, cur, total + candidates[i])", "Recurse retaining same index i to permit unlimited element reuse."),
                    ("cur.pop()", "Backtrack: undo choice to explore skipping branch.")
                ],
                "time_complexity": "O(2^T) where T is target / min(candidates).",
                "space_complexity": "O(T) recursion depth.",
                "edge_cases": "Target smaller than minimum candidate (returns []); single element matching target."
            }
        ],
        "cs_core": {
            "subject": "Core Computer Science",
            "topic": "Rapid-Fire Placement Technical Drill (Top High-Frequency Questions)",
            "detailed_notes": [
                "Comprehensive Placement Technical Flashcards:\n"
                "• 1. DBMS: What is a BCNF violation? When a functional dependency X -> Y exists where X is not a superkey.\n"
                "• 2. Networks: What is the difference between TCP and UDP? TCP is connection-oriented, reliable, with congestion control; UDP is connectionless, lightweight, and unordered.\n"
                "• 3. Operating Systems: What is a Deadlock? A situation where two or more processes are unable to proceed because each is holding a resource and waiting for another resource held by the other. Requires 4 Coffman conditions: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait.\n"
                "• 4. Python: What is the difference between `is` and `==`? `==` checks value equality (`a.__eq__(b)`); `is` checks memory address identity (`id(a) == id(b)`).\n"
                "• 5. System Design: What is Database Indexing? A data structure (B+ tree) that improves data retrieval speed at the cost of slower writes and additional disk storage."
            ],
            "interview_qa": [
                {
                    "q": "What is the difference between a Process and a Thread in modern operating systems?",
                    "a": "A Process is an executing instance of a program with its own dedicated, isolated virtual address space, file descriptor table, and security context. A Thread is the smallest unit of CPU execution within a process; multiple threads inside the same process share identical memory (heap, code, global data), having only private registers and call stacks. Creating a thread consumes ~10x fewer CPU cycles than spawning a process."
                },
                {
                    "q": "Explain the concept of Database Normalization and why BCNF is preferred over 3NF.",
                    "a": "Normalization organizes database tables to minimize redundancy and eliminate insertion, update, and deletion anomalies. While 3NF permits non-superkey determinants if the dependent attribute is part of a candidate key (prime attribute), BCNF strictly mandates that for every functional dependency X -> Y, X MUST be a superkey, eliminating subtle redundancies in tables with multiple overlapping candidate keys."
                }
            ]
        },
        "project_defense": {
            "project_name": "Portfolio Curation & Git Readiness",
            "feature_focus": "GitHub Portfolio Optimization & Live Recruiter Screen-Sharing Strategy",
            "architecture_deep_dive": (
                "Preparing Sarthak's GitHub Repositories for Placement Technical Screeners:\n\n"
                "1. Repository Cleanliness & Presentation:\n"
                "• Pin the top 4 flagship repositories: `BulkBeat TV` (FastAPI/Telegram), `TerraStract` (Document AI/OCR), `CSMS` (Enterprise Backend), `BEVM` (Cryptographic Voting).\n"
                "• Add descriptive badges (FastAPI, Python 3.11, Docker, PostgreSQL, MIT License).\n"
                "• Include architecture diagrams (Mermaid or ASCII flowcharts) directly in the root `README.md`.\n\n"
                "2. Live Screen-Sharing Script:\n"
                "• Have Docker Compose pre-warmed so typing `docker compose up` starts the service in 3 seconds.\n"
                "• Open Swagger interactive UI (`/docs`) to demonstrate live API execution.\n"
                "• Walk through a complex code block (e.g. SQLite WAL pragma in BulkBeat or Tesseract fallback in TerraStract) with confidence."
            ),
            "interview_qa": [
                {
                    "q": "How do you present your personal projects to an interviewer when asked 'Walk me through your code'?",
                    "a": "I follow a 3-minute executive narrative: 1. The Problem (why the project was built), 2. Architecture & Data Flow (frontend to backend to database), 3. The Hardest Technical Hurdle (e.g., resolving SQLite write contention in BulkBeat TV using WAL mode), and 4. The Measurable Result (handling concurrent streams with sub-50ms latency)."
                },
                {
                    "q": "Why is an interactive OpenAPI/Swagger page valuable in placement interviews?",
                    "a": "It proves that the API was designed professionally with strict schema validation (Pydantic), clear endpoint documentation, and immediate interactive testability, demonstrating production-grade engineering standards."
                }
            ]
        },
        "daily_test": {
            "day": 27,
            "questions": [
                {"q": "What is the global truncation error order of the Runge-Kutta 4th Order method?", "a": "O(h^4)."},
                {"q": "Why is RK4 practically superior to Taylor Series expansions for numerical ODEs?", "a": "Because RK4 achieves 4th-order accuracy purely through algebraic function evaluations without calculating complex higher-order analytical derivatives."},
                {"q": "What is the formula for the 2-year difference between CI and SI?", "a": "D = P * (R / 100)^2."},
                {"q": "In Combination Sum (LeetCode 39), why do we pass the same index i during recursion when including a candidate?", "a": "To permit unlimited reuse of the same candidate integer in building the target sum."},
                {"q": "What are the 4 Coffman conditions required for a Deadlock to occur?", "a": "1. Mutual Exclusion, 2. Hold and Wait, 3. No Preemption, 4. Circular Wait."},
                {"q": "What is the difference between `==` and `is` in Python?", "a": "`==` checks value equality; `is` checks memory reference identity."},
                {"q": "In Euler's method, what is the geometric interpretation of the step formula?", "a": "Approximating the curve of the solution by the tangent line at the starting point of the interval."},
                {"q": "Why should high-value GitHub repositories contain a clear architecture diagram?", "a": "To provide technical interviewers with immediate clarity on data flow, component decoupling, and system design maturity."}
            ]
        }
    }

    # DAY 28
    days[28] = {
        "day": 28,
        "title": "KM Expert Systems, Full Placement Mock Simulation & LRU Cache Design",
        "sem_data": {
            "subject": "BCA-5001 Knowledge Management",
            "topic": "Unit V — Expert Systems Architecture: Inference Engine, Forward vs Backward Chaining & Knowledge Engineering",
            "detailed_notes": [
                "An Expert System (ES) is an artificial intelligence computer application that encapsulates human domain expertise to solve complex reasoning problems at the level of a human specialist (e.g. medical diagnosis, financial fraud detection).",
                "The 5 Major Components of an Expert System Architecture:\n"
                "1. Knowledge Base (KB): The core repository storing domain knowledge represented as IF-THEN production rules, semantic nets, frames, or ontologies. Rules separate facts ('Patient has fever') from heuristics ('IF fever AND rash THEN measles').\n"
                "2. Working Memory (Fact Base): Contains dynamic, session-specific data and known facts entered by the user during the current consultation.\n"
                "3. Inference Engine: The 'brain' of the expert system. Applies logical algorithms to match facts in working memory against production rules in the KB to deduce new conclusions.\n"
                "4. Explanation Facility (Justifier): Explains the reasoning process to the user, answering 'HOW' a conclusion was reached or 'WHY' a particular question is being asked.\n"
                "5. Knowledge Acquisition Subsystem: The interface enabling Knowledge Engineers to capture and encode new rules from human experts into the knowledge base without modifying the underlying inference engine code.",
                "Inference Engine Reasoning Paradigms:\n"
                "• Forward Chaining (Data-Driven / Bottom-Up):\n"
                "  - Starts with known facts in working memory and fires matching rules whose conditions (antecedents) are satisfied, adding new facts to memory until a goal is reached.\n"
                "  - Best for: Planning, monitoring, synthesis, and systems with many equally valid solutions.\n"
                "• Backward Chaining (Goal-Driven / Top-Down):\n"
                "  - Starts with a hypothetical goal/conclusion and works backwards to see if available facts support the goal. If facts are missing, the system prompts the user with targeted questions.\n"
                "  - Best for: Diagnostic systems (medical, automotive troubleshooting) and auditing."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                     EXPERT SYSTEM FIVE-TIER ARCHITECTURE                |\n"
                "+-------------------------------------------------------------------------+\n"
                "|                                                                         |\n"
                "|      +---------------------+          +---------------------------+     |\n"
                "|      |  KNOWLEDGE BASE     |<-------->| KNOWLEDGE ACQUISITION     |<--- Expert\n"
                "|      |  (Production Rules) |          | SUBSYSTEM                 |     |\n"
                "|      +---------------------+          +---------------------------+     |\n"
                "|                 ^                                                       |\n"
                "|                 | (Pattern Match)                                       |\n"
                "|                 v                                                       |\n"
                "|      +---------------------+          +---------------------------+     |\n"
                "|      |  INFERENCE ENGINE   |<-------->| WORKING MEMORY (Facts)    |     |\n"
                "|      | (Forward / Backward)|          |                           |     |\n"
                "|      +---------------------+          +---------------------------+     |\n"
                "|                 ^                                                       |\n"
                "|                 | (Deduction Trace)                                     |\n"
                "|                 v                                                       |\n"
                "|      +---------------------+          +---------------------------+     |\n"
                "|      | EXPLANATION         |<-------->| USER INTERFACE            |<--- User\n"
                "|      | FACILITY (How/Why)  |          | (Consultation)            |     |\n"
                "|      +---------------------+          +---------------------------+     |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Comparison Aspect", "Forward Chaining (Data-Driven)", "Backward Chaining (Goal-Driven)"],
                "rows": [
                    ["Starting Point", "Starts with initial known facts", "Starts with a hypothesis or target goal"],
                    ["Reasoning Direction", "Bottom-Up (Antecedent -> Consequent)", "Top-Down (Consequent -> Antecedent)"],
                    ["Search Strategy", "Breadth-First Search (finds all reachable facts)", "Depth-First Search (proves specific hypothesis)"],
                    ["User Interaction", "User enters all data upfront", "System prompts user only for required missing facts"],
                    ["Best Suited For", "Forecasting, planning, scheduling", "Diagnosis, debugging, medical assessment"]
                ]
            },
            "memorize": "5 Components: Knowledge Base, Working Memory, Inference Engine, Explanation Facility, Knowledge Acquisition. Forward Chaining = Data-driven; Backward Chaining = Goal-driven.",
            "understand": "Why separate Knowledge Base from the Inference Engine? In conventional programming, business rules are hardcoded inside `if-else` loops. If a rule changes, the entire code must be recompiled and re-tested. In an Expert System, the inference logic is an unchanging engine, while rules are stored separately in the Knowledge Base, allowing non-programmers to add, modify, or delete expertise dynamically!",
            "common_mistakes": "1. Confusing Working Memory (transient facts for 1 session) with Knowledge Base (permanent domain rules). 2. Omitting the Explanation Facility.",
            "pyq_year": "CSJMU BCA-5001 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "High-Frequency 15-Mark Core Question (Appeared in 2021, 2022-23, 2023-24, 2024-25)",
            "pyq_question": "What is an Expert System? Explain its architecture with a neat block diagram describing all major components. Differentiate between Forward Chaining and Backward Chaining with suitable examples. (15 Marks)",
            "pyq_rubric": "Definition & Characteristics of Expert Systems (3 marks) + 5-Component Architecture block diagram (5 marks) + Forward vs Backward Chaining detailed comparison (5 marks) + Role of Knowledge Engineer (2 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Definition and Characteristics of Expert Systems:",
                 "An Expert System (ES) is a knowledge-intensive artificial intelligence system designed to emulate the decision-making ability of human experts within a specific narrow domain. Unlike conventional software that processes numerical data using static algorithms, an expert system reasons heuristically over symbolic representations, explains its deductions, and tolerates incomplete or uncertain evidence."),
                ("2. Architectural Breakdown of Major Components:",
                 "• 1. Knowledge Base: Encapsulates domain expertise represented as declarative production rules (IF condition THEN action).\n"
                 "• 2. Working Memory (Fact Base): Holds current case data and facts dynamically gathered during a specific consultation session.\n"
                 "• 3. Inference Engine: The reasoning mechanism that matches working memory facts with knowledge base rules, resolves conflicts when multiple rules match, and fires active productions.\n"
                 "• 4. Explanation Facility: Provides auditability by answering 'WHY is this question being asked?' and 'HOW was this conclusion derived?'.\n"
                 "• 5. Knowledge Acquisition Interface: Enables Knowledge Engineers to extract expertise from human practitioners and translate it into formal production rules."),
                ("3. Forward Chaining vs Backward Chaining Comparative Analysis:",
                 "• Forward Chaining begins with established input facts and fires rules whose conditions evaluate to true, deriving intermediate conclusions until a terminal state is reached. Ideal for configuration systems and financial market forecasting.\n"
                 "• Backward Chaining starts with a prospective goal (e.g. 'Patient has Malaria') and queries the knowledge base to identify antecedent conditions required to substantiate that goal. If conditions are unknown, the system asks the user targeted questions. Ideal for diagnostic applications.")
            ]
        },
        "sgpa_target": {"focus": "Master Expert Systems Architecture & Forward/Backward Chaining", "milestone": "Full 15/15 on KM Unit V Exam Question"},
        "apt_data": {
            "topic": "Comprehensive Placement Aptitude Mock Simulation (50 High-Yield Questions)",
            "tutorial": [
                "Full-Length Assessment Test Strategy for Placement Day:\n"
                "• Time Allocation Rule: Never spend more than 90 seconds on any single quantitative question. If stuck, flag it and move on.\n"
                "• Sectional Ordering: Complete Verbal first (high speed, 30s/q), then Logical Reasoning (pattern recognition, 60s/q), then Quantitative Aptitude (calculation intensive, 75s/q).\n"
                "• Elimination Mindset: Use unit digit checking, digital sums, and sanity limits to eliminate at least 2 options before calculating."
            ],
            "formulas": "Cutoff Target: >= 75% raw accuracy. P/C: nCr = n! / (r!(n-r)!). Speed = Distance / Time.",
            "shortcut": "The 2-Pass Method: In Pass 1, solve all 30-second low-hanging fruit questions (percentages, blood relations, syllogisms). In Pass 2, tackle heavy data interpretation and algebraic word problems.",
            "recognition": "Comprehensive mock simulating TCS NQT, Wipro, Infosys, and Cognizant assessment patterns.",
            "tier1_problem": "A car travels from A to B at 60 km/h and returns at 40 km/h. What is the average speed of the entire journey?",
            "tier1_solution": "Average Speed (Harmonic Mean for equal distance) = 2*S1*S2 / (S1 + S2) = 2*60*40 / (60 + 40) = 4800 / 100 = 48 km/h. Answer: 48 km/h.",
            "tier2_problem": "Find the next number in the series: 3, 7, 15, 31, 63, ?",
            "tier2_solution": "Pattern: Each number is 2 * previous + 1 (or 2^(n+1) - 1).\n3*2+1 = 7; 7*2+1 = 15; 15*2+1 = 31; 31*2+1 = 63.\nNext = 63 * 2 + 1 = 126 + 1 = 127. Answer: 127.",
            "tier3_problem": "[Placement Probability Drill] Two dice are rolled simultaneously. What is the probability that the sum of the numbers is greater than 9?",
            "tier3_solution": "Total outcomes = 6 * 6 = 36.\nFavorable outcomes where sum > 9 (Sum = 10, 11, or 12):\nSum 10: (4,6), (5,5), (6,4) ==> 3 outcomes.\nSum 11: (5,6), (6,5) ==> 2 outcomes.\nSum 12: (6,6) ==> 1 outcome.\nTotal favorable = 3 + 2 + 1 = 6.\nProbability = 6 / 36 = 1/6. Answer: 1/6.",
            "tier4_problem": "In how many ways can 5 boys and 4 girls be seated in a row such that no two girls are seated together?",
            "tier4_solution": "First seat the 5 boys: _ B1 _ B2 _ B3 _ B4 _ B5 _.\nNumber of ways to arrange 5 boys = 5! = 120 ways.\nThis creates 6 available gaps for girls (marked by underscores).\nNumber of ways to choose 4 gaps from 6 and arrange 4 girls = ^6 P_4 = 6 * 5 * 4 * 3 = 360 ways.\nTotal seating arrangements = 120 * 360 = 43,200 ways. Answer: 43,200 ways.",
            "speed_drills": [
                {"q": "A sum at 5% SI amounts to Rs 600 in 4 years. Find principal.", "a": "P + P*0.2 = 1.2P = 600 ==> P = Rs 500."},
                {"q": "LCM of two prime numbers X and Y (X > Y) is 161. Value of 3Y - X?", "a": "161 = 23 * 7. X=23, Y=7. 3(7) - 23 = 21 - 23 = -2."},
                {"q": "Find odd one out: 27, 64, 125, 144, 216.", "a": "144. All others are perfect cubes."},
                {"q": "If 20% of A = 30% of B, find A : B.", "a": "A/B = 30/20 = 3 : 2."},
                {"q": "Probability of getting at least one head in 3 coin tosses?", "a": "1 - P(No heads) = 1 - 1/8 = 7/8."}
            ]
        },
        "dsa_problems": [
            {
                "title": "LRU Cache (LeetCode 146 - Medium)",
                "difficulty": "Medium",
                "importance": "The Single Most Famous System Design & Data Structure Placement Problem",
                "problem_statement": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement LRUCache class with get(key) and put(key, value) operations running in O(1) average time complexity.",
                "solution_approach": (
                    "Doubly Linked List + Hash Map Architecture:\n"
                    "1. Hash Map (`self.cache`): Maps `key -> Node` providing O(1) key lookups.\n"
                    "2. Doubly Linked List with dummy `head` and `tail`:\n"
                    "   • Head points to Least Recently Used (LRU) node.\n"
                    "   • Tail points to Most Recently Used (MRU) node.\n"
                    "3. `get(key)`: If key exists, move node to tail (MRU) and return value.\n"
                    "4. `put(key, value)`: If key exists, update value and move to tail. If new, insert at tail. If capacity exceeded, remove node right after dummy head (LRU) and delete from map."
                ),
                "code": (
                    "class Node:\n"
                    "    def __init__(self, key=0, val=0):\n"
                    "        self.key = key\n"
                    "        self.val = val\n"
                    "        self.prev = None\n"
                    "        self.next = None\n\n"
                    "class LRUCache:\n"
                    "    def __init__(self, capacity: int):\n"
                    "        self.cap = capacity\n"
                    "        self.cache = {} # key -> Node\n"
                    "        self.head, self.tail = Node(), Node()\n"
                    "        self.head.next = self.tail\n"
                    "        self.tail.prev = self.head\n"
                    "        \n"
                    "    def _remove(self, node: Node):\n"
                    "        prev, nxt = node.prev, node.next\n"
                    "        prev.next = nxt\n"
                    "        nxt.prev = prev\n"
                    "        \n"
                    "    def _insert(self, node: Node):\n"
                    "        prev = self.tail.prev\n"
                    "        prev.next = node\n"
                    "        node.prev = prev\n"
                    "        node.next = self.tail\n"
                    "        self.tail.prev = node\n"
                    "        \n"
                    "    def get(self, key: int) -> int:\n"
                    "        if key in self.cache:\n"
                    "            node = self.cache[key]\n"
                    "            self._remove(node)\n"
                    "            self._insert(node)\n"
                    "            return node.val\n"
                    "        return -1\n"
                    "        \n"
                    "    def put(self, key: int, value: int) -> None:\n"
                    "        if key in self.cache:\n"
                    "            self._remove(self.cache[key])\n"
                    "        node = Node(key, value)\n"
                    "        self.cache[key] = node\n"
                    "        self._insert(node)\n"
                    "        if len(self.cache) > self.cap:\n"
                    "            lru = self.head.next\n"
                    "            self._remove(lru)\n"
                    "            del self.cache[lru.key]"
                ),
                "line_by_line": [
                    ("self.head, self.tail = Node(), Node()", "Dummy sentinel nodes eliminate edge-case checks for empty lists."),
                    ("self._remove(node); self._insert(node)", "Promote accessed node to Most Recently Used position at tail."),
                    ("lru = self.head.next; self._remove(lru)", "Evict Least Recently Used node adjacent to head when exceeding capacity.")
                ],
                "time_complexity": "O(1) strictly for both get() and put() operations.",
                "space_complexity": "O(capacity) space for hash map and doubly linked list nodes.",
                "edge_cases": "Capacity = 1; overwriting existing key; accessing non-existent key."
            }
        ],
        "cs_core": {
            "subject": "Placement Strategy",
            "topic": "The STAR Behavioral Framework & Placement HR Interview Mastery",
            "detailed_notes": [
                "The STAR Framework for Answering Behavioral Interview Questions:\n"
                "• S — Situation: Set the context (Where? When? What project?). Keep concise (20 seconds).\n"
                "• T — Task: Define the explicit challenge or objective you were responsible for.\n"
                "• A — Action: Describe the SPECIFIC technical actions YOU took (use 'I', not 'we'). Highlight design choices and code implementations.\n"
                "• R — Result: Quantify the outcome (e.g. 'reduced latency by 40%', 'served 6,000 users', 'zero data corruption').",
                "High-Frequency Placement HR Questions:\n"
                "1. 'Tell me about yourself': 90-second elevator pitch covering: BCA background, passion for Python backend systems, flagship achievements (BulkBeat TV & TerraStract), and why this company.\n"
                "2. 'Why should we hire a BCA graduate when B.Tech graduates are available?': Emphasize demonstrated software execution over theoretical credentials: 'While many graduates have purely academic credentials, I have built and deployed production software with live users, written asynchronous microservices, implemented OCR pipelines, and managed database migrations from day one.'"
            ],
            "interview_qa": [
                {
                    "q": "How do you answer: 'Tell me about a time you made a technical mistake and how you resolved it'?",
                    "a": "Use STAR: 'In BulkBeat TV, concurrent SQLite write transactions initially threw `database is locked` errors during heavy streaming alerts. I researched SQLite's concurrency model, realized default rollback journals lock the entire database during writes, and reconfigured the database to Write-Ahead Logging (WAL) mode while wrapping alert updates in an asynchronous worker queue. This eliminated write contention completely and taught me deep concurrency architecture.'"
                },
                {
                    "q": "Where do you see yourself in 3 years as a software engineer?",
                    "a": "In 3 years, I see myself as a core backend contributor who has mastered distributed systems architecture, owns end-to-end service delivery, mentors junior team members, and consistently drives measurable reliability and performance improvements across enterprise software pipelines."
                }
            ]
        },
        "project_defense": {
            "project_name": "Full Portfolio Final Defense",
            "feature_focus": "The 90-Second Technical Pitch for BulkBeat TV & TerraStract",
            "architecture_deep_dive": (
                "End-to-End Executive Pitch Structure:\n\n"
                "1. BulkBeat TV Pitch:\n"
                "'BulkBeat TV is a real-time news streaming and notification system that ingests live media streams and delivers automated market alerts. "
                "I engineered the backend using Python aiohttp and SQLite in WAL mode, implementing an asynchronous token-bucket rate limiter that pushes alerts "
                "to thousands of subscribers via Telegram Webhooks with sub-second latency.'\n\n"
                "2. TerraStract Pitch:\n"
                "'TerraStract is an intelligent document processing pipeline designed to extract structured tabular data from complex, multi-lingual scanned PDFs. "
                "I built a hybrid extraction pipeline that leverages PyMuPDF for native vector text and falls back to Tesseract OCR with Page Segmentation Mode 6 for scanned regions, "
                "paired with regex-based Sanskrit/Devanagari Unicode normalization to guarantee clean JSON extraction.'"
            ),
            "interview_qa": [
                {
                    "q": "What was the most challenging technical bug you resolved across your projects?",
                    "a": "In TerraStract, scanned Hindi legal documents frequently suffered from OCR segmentation errors when complex conjunct characters were misinterpreted. I solved this by pre-processing document page images using adaptive thresholding and contrast normalization in OpenCV, and forcing Tesseract's PSM to Mode 6 (single uniform block of text), improving character extraction accuracy by over 35%."
                },
                {
                    "q": "If you had 1 more month to improve your projects, what would you implement next?",
                    "a": "I would introduce automated integration test suites with Testcontainers for PostgreSQL, deploy OpenTelemetry distributed tracing to identify latency bottlenecks across microservices, and configure Prometheus/Grafana dashboards for real-time memory and error rate monitoring."
                }
            ]
        },
        "daily_test": {
            "day": 28,
            "questions": [
                {"q": "What are the 5 major components of an Expert System?", "a": "1. Knowledge Base, 2. Working Memory, 3. Inference Engine, 4. Explanation Facility, 5. Knowledge Acquisition Subsystem."},
                {"q": "Why is an LRU Cache implemented using a Doubly Linked List alongside a Hash Map?", "a": "The Hash Map provides O(1) key lookups, while the Doubly Linked List enables O(1) removal and insertion to maintain the recency ordering of elements."},
                {"q": "What does each letter in the STAR interview framework stand for?", "a": "Situation, Task, Action, Result."},
                {"q": "How does Forward Chaining differ from Backward Chaining in Expert Systems?", "a": "Forward Chaining starts with known data facts and moves forward to infer new conclusions (data-driven); Backward Chaining starts with a target hypothesis and works backward to check supporting facts (goal-driven)."},
                {"q": "What is the average time complexity of get() and put() in an LRU Cache?", "a": "O(1) strictly for both operations."},
                {"q": "What is the average speed of a round trip with speeds 60 km/h and 40 km/h over the same distance?", "a": "48 km/h (Harmonic mean: 2*60*40 / 100)."},
                {"q": "What is the role of the Explanation Facility in an Expert System?", "a": "It explains the reasoning trace to the user, answering 'HOW' a conclusion was derived and 'WHY' specific information is being requested."},
                {"q": "How do you defend being a BCA student in a campus placement interview against engineering peers?", "a": "By emphasizing hands-on, production-grade software delivery: live asynchronous APIs, production database migrations, and real document pipelines."}
            ]
        }
    }

    # DAY 29
    days[29] = {
        "day": 29,
        "title": "Comprehensive Semester 5 Exam Simulation & Top 20 Placement Code Snippets",
        "sem_data": {
            "subject": "Semester 5 Comprehensive Academic Simulation",
            "topic": "Final Exam Hall Simulation: Full 15-Mark Model Solutions Across All 4 Academic Subjects",
            "detailed_notes": [
                "Comprehensive Semester 5 Academic Synthesis:\n"
                "• Subject 1 (BCA-5001 KM): The 4 Pillars of SGPA 9: Nonaka's SECI Spiral, Simon's Decision Making Model, 3-Tier Data Warehousing & Expert Systems Architecture.\n"
                "• Subject 2 (BCA-5002 Java): The 4 Pillars: JVM 3 Subsystems & 5 Memory Areas, 5-State Multithreading Life Cycle & Synchronization, JDBC 4 Driver Types, and Servlet 3-Stage Life Cycle & HttpSession.\n"
                "• Subject 3 (BCA-5003 Networks): The 4 Pillars: OSI 7-Layer vs TCP/IP Encapsulation, CRC Modulo-2 Division & Hamming Codes, Sliding Window (GBN vs SR), and TCP Congestion Control (AIMD/Tahoe/Reno).\n"
                "• Subject 4 (BCA-5004 Numerical): The 4 Pillars: Newton-Raphson Quadratic Convergence Proof, Gauss Elimination with Partial Pivoting, Simpson's 1/3 & 3/8 Rules, and Runge-Kutta 4th Order (RK4).",
                "Exam Hall 15-Mark Answer Presentation Architecture:\n"
                "1. Introduction & Formal Definition (1.5 marks).\n"
                "2. Standard Architectural Block Diagram / Flowchart (4 marks).\n"
                "3. Detailed Technical Mechanics & Equations (5 marks).\n"
                "4. Comparative Analysis Table (3 marks).\n"
                "5. Practical Application / Conclusion (1.5 marks)."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|               THE 15-MARK UNIVERSITY EXAM PRESENTATION BLUEPRINT        |\n"
                "+-------------------------------------------------------------------------+\n"
                "|  [ Section 1: Formal Definition & Academic Context ] (1 Page)           |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  [ Section 2: Full-Width Boxed Architecture Diagram ] (0.75 Page)       |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  [ Section 3: Deep Technical Derivation / Code / Mechanics ] (1.5 Pages)|\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  [ Section 4: 5-Row Comparison / Summary Table ] (0.5 Page)             |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  [ Section 5: Real-World Industry Case Study / Conclusion ] (0.25 Page) |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Subject", "Guaranteed Core 15-Mark Topic", "Key Formula / Diagram", "Common University Exam Trap"],
                "rows": [
                    ["BCA-5001 KM", "Nonaka's SECI Model / KMSLC 8 Stages", "Socialization, Externalization, Combination, Internalization", "Omitting knowledge validation vs verification"],
                    ["BCA-5002 Java", "Servlet Life Cycle & Session Tracking", "init() -> service() -> destroy() & JSESSIONID", "Confusing forward() with sendRedirect()"],
                    ["BCA-5003 Networks", "Sliding Window GBN vs SR / CRC Division", "Ws = 2^m - 1 vs 2^(m-1); Modulo-2 XOR", "Wrong sender window formula for Go-Back-N"],
                    ["BCA-5004 Numerical", "Newton-Raphson Proof / Runge-Kutta 4th Order", "x_{n+1} = x_n - f/f'; RK4 k1-k4 slopes", "Forgetting (1/6) factor or k1/2 arguments in RK4"]
                ]
            },
            "memorize": "SGPA 9 Formula: Structure every 15-mark answer into 5 parts: Definition, Boxed Diagram, Equations/Code, Comparison Table, Conclusion. Time = 35 mins per 15-mark question.",
            "understand": "Why do examiners reward diagrams and comparison tables? University evaluators inspect hundreds of handwritten answer booklets per day. A student who writes 4 pages of dense unbroken prose is graded at 8-10 marks. A student who leads with an immaculate boxed architectural diagram and a clean comparison table immediately signals mastery, commanding 14-15 marks.",
            "common_mistakes": "1. Writing in bullet points without narrative explanations. 2. Spending 60 minutes on Question 1 and rushing through subsequent questions.",
            "pyq_year": "CSJMU BCA Comprehensive (2021-2025)",
            "pyq_freq": "Covers 100% of University Question Paper Blueprint",
            "pyq_question": "Master Academic Checklist: Explain the 4 core 15-mark topics across all 4 subjects and write down the essential formula for each.",
            "pyq_rubric": "Comprehensive mastery across all 4 academic subjects with full structural breakdown.",
            "model_answer_paragraphs": [
                ("Master Revision Blueprint:",
                 "All 4 subjects are unified under rigorous systems thinking: Knowledge Management structures enterprise human capital; Java provides object-oriented concurrent software execution; Computer Networks delivers reliable transport across packet networks; and Numerical Methods solves complex differential and linear models computationally.")
            ]
        },
        "sgpa_target": {"focus": "Master All 4 University Subjects for SGPA 9.0", "milestone": "Full Academic Readiness Across All 4 Papers"},
        "apt_data": {
            "topic": "The Last-Minute Aptitude Formula Crunch (Top 50 Speed Shortcuts)",
            "tutorial": [
                "Essential Mental Formula Review:\n"
                "• Percentages: Net change of +a% and +b% = a + b + (a*b / 100)%.\n"
                "• Profit & Loss: If Profit% = Loss% = x%, the overall transaction is ALWAYS a loss of (x/10)^2 %.\n"
                "• Trains: Time to cross a pole = Length of train / Speed. Time to cross a platform = (Length of train + Length of platform) / Speed.\n"
                "• Boats: Upstream = u - v; Downstream = u + v. Speed of boat in still water = (Downstream + Upstream) / 2.\n"
                "• Clocks: Angle between hands = |30*H - (11/2)*M| degrees."
            ],
            "formulas": "Net %: a + b + ab/100. Overall loss: (x/10)^2. Clock Angle: |30H - 5.5M|. Boat in still water: (D + U)/2.",
            "shortcut": "Clock Angle Formula: At 4:20, Angle = |30(4) - 5.5(20)| = |120 - 110| = 10 degrees!",
            "recognition": "Fast formulas for rapid recognition in last-minute placement revisions.",
            "tier1_problem": "What is the angle between the hour hand and the minute hand of a clock at 3:30?",
            "tier1_solution": "Angle = |30*H - (11/2)*M| = |30*(3) - 5.5*(30)| = |90 - 165| = |-75| = 75 degrees. Answer: 75 degrees.",
            "tier2_problem": "Two articles are sold for Rs 990 each, one at a gain of 10% and the other at a loss of 10%. Find overall profit or loss percentage.",
            "tier2_solution": "When selling price is same and % gain = % loss = x%, there is always an overall loss of (x / 10)^2 % = (10 / 10)^2 = 1% loss. Answer: 1% loss.",
            "tier3_problem": "A boat travels 24 km downstream in 2 hours and returns upstream in 4 hours. Find the speed of the water stream.",
            "tier3_solution": "Downstream speed D = 24 / 2 = 12 km/h.\nUpstream speed U = 24 / 4 = 6 km/h.\nSpeed of stream v = (D - U) / 2 = (12 - 6) / 2 = 6 / 2 = 3 km/h. Answer: 3 km/h.",
            "tier4_problem": "The price of petrol increases by 25%. By what percentage must a motorist reduce consumption so that expenditure remains unchanged?",
            "tier4_solution": "Reduction % = [r / (100 + r)] * 100 = [25 / (100 + 25)] * 100 = (25 / 125) * 100 = (1 / 5) * 100 = 20%. Answer: 20%.",
            "speed_drills": [
                {"q": "Clock angle at 7:20?", "a": "|30(7) - 5.5(20)| = |210 - 110| = 100 degrees."},
                {"q": "Gain 20% and loss 20% at same SP. Overall?", "a": "(20/10)^2 = 4% loss."},
                {"q": "Boat speed 10 km/h, stream 2 km/h. Downstream speed?", "a": "10 + 2 = 12 km/h."},
                {"q": "Price drops 20%. How much more consumption for same spend?", "a": "[20 / (100-20)] * 100 = 25%."},
                {"q": "Sum of first 20 natural numbers?", "a": "n(n+1)/2 = 20 * 21 / 2 = 210."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Top 20 Must-Know Placement Code Snippets",
                "difficulty": "Easy to Medium",
                "importance": "The Fundamental Technical Placement Interview Code Cheat Sheet",
                "problem_statement": "Implement the essential two-pointer, sliding window, and tree reversal paradigms in clean Python.",
                "solution_approach": (
                    "Quick Review of High-Frequency Placement Primitives:\n"
                    "1. Two Pointers: Left & Right converging to target.\n"
                    "2. Fast & Slow Pointers: Floyd's cycle detection.\n"
                    "3. Invert Binary Tree: Recursive swapping of left and right child pointers.\n"
                    "4. Binary Search: Midpoint calculation `mid = left + (right - left) // 2` to prevent integer overflow."
                ),
                "code": (
                    "# 1. Invert Binary Tree\n"
                    "def invertTree(root):\n"
                    "    if not root: return None\n"
                    "    root.left, root.right = invertTree(root.right), invertTree(root.left)\n"
                    "    return root\n\n"
                    "# 2. Fast Binary Search\n"
                    "def binarySearch(nums: list[int], target: int) -> int:\n"
                    "    l, r = 0, len(nums) - 1\n"
                    "    while l <= r:\n"
                    "        mid = l + (r - l) // 2\n"
                    "        if nums[mid] == target: return mid\n"
                    "        elif nums[mid] < target: l = mid + 1\n"
                    "        else: r = mid - 1\n"
                    "    return -1"
                ),
                "line_by_line": [
                    ("root.left, root.right = invertTree(root.right), invertTree(root.left)", "Simultaneous tuple assignment swaps left and right subtrees recursively."),
                    ("mid = l + (r - l) // 2", "Guarantees mathematical safety against integer overflow.")
                ],
                "time_complexity": "Invert Tree: O(N); Binary Search: O(log N).",
                "space_complexity": "O(1) to O(H).",
                "edge_cases": "Empty inputs; single element."
            }
        ],
        "cs_core": {
            "subject": "Core Computer Science",
            "topic": "Final Placement Interview Rapid-Fire Simulation",
            "detailed_notes": [
                "The 10 Non-Negotiable Technical Interview Truths:\n"
                "1. ACID Properties: Atomicity (all-or-nothing), Consistency (integrity constraints), Isolation (concurrent safety), Durability (persisted on disk).\n"
                "2. Indexing: B+ Tree stores data pointers in leaves with sequential horizontal links, optimizing range queries.\n"
                "3. TCP Handshake: 3-way handshake (SYN, SYN-ACK, ACK) establishes reliable socket sequence numbers.\n"
                "4. HTTP Verbs: GET/HEAD/PUT/DELETE are idempotent; POST and PATCH are non-idempotent.\n"
                "5. Virtual Memory: Paging translates virtual addresses to physical frames using page tables; Page Fault triggers OS to load block from disk."
            ],
            "interview_qa": [
                {
                    "q": "What makes an HTTP method idempotent?",
                    "a": "An HTTP method is idempotent if executing it multiple times consecutively produces the exact same side-effects on the server as executing it once. GET, HEAD, PUT, and DELETE are idempotent. POST is non-idempotent because submitting 5 identical POST requests creates 5 separate database records."
                },
                {
                    "q": "What is the difference between a Clustered and a Non-Clustered index?",
                    "a": "A Clustered index dictates the physical storage order of the actual table rows on disk; therefore, a table can possess only ONE clustered index (typically the Primary Key). A Non-Clustered index creates a separate B+ tree structure containing sorted index columns along with row pointers (TIDs) back to the table heap, allowing multiple non-clustered indexes per table."
                }
            ]
        },
        "project_defense": {
            "project_name": "Full Portfolio Rehearsal",
            "feature_focus": "Handling Tough Architecture & Trade-Off Questions",
            "architecture_deep_dive": (
                "Mastering Interview Defense Pushbacks:\n\n"
                "When an interviewer asks: 'Why didn't you use MongoDB for CSMS?'\n"
                "Answer: 'Because CSMS manages car inventory orders and invoices where financial consistency and referential integrity are strict requirements. Storing orders in MongoDB without schema constraints risks orphaned records if a car is removed while an order is open. PostgreSQL provided ACID transactions, foreign key constraints, and declarative Alembic schema migrations.'\n\n"
                "When asked: 'Why not use Celery instead of asyncio for BulkBeat TV?'\n"
                "Answer: 'Celery requires running separate Redis/RabbitMQ brokers and heavyweight worker processes, which would consume over 500MB of RAM on a budget VPS. Python's native `asyncio.Queue` allowed me to achieve asynchronous non-blocking event dispatching within the same process footprint under 60MB of RAM.'"
            ),
            "interview_qa": [
                {
                    "q": "How do you explain the trade-offs of using SQLite in BulkBeat TV?",
                    "a": "SQLite provided extreme simplicity, zero network latency (in-process calls), and minimal RAM consumption. The trade-off is single-writer concurrency. I mitigated this by enabling Write-Ahead Logging (WAL) to allow simultaneous reads during writes and buffering write operations through an in-memory queue. For scaling beyond 10,000 users, I have architected a migration path to PostgreSQL."
                },
                {
                    "q": "What was your approach to error handling in TerraStract's OCR pipeline?",
                    "a": "I designed a resilient multi-tier fallback: First, try native PyMuPDF vector text extraction (100% accurate, sub-50ms). If character density is below threshold, crop image regions and run Tesseract OCR with PSM 6. If confidence score is below 70%, route the page to an exception review queue with raw image logs."
                }
            ]
        },
        "daily_test": {
            "day": 29,
            "questions": [
                {"q": "What are the 5 parts of an SGPA 9.0 15-mark university answer structure?", "a": "1. Formal Definition, 2. Boxed Architecture Diagram, 3. Technical Derivation/Equations, 4. Comparison Table, 5. Conclusion/Practical Application."},
                {"q": "What is the angle between clock hands at 3:30?", "a": "75 degrees (|30*3 - 5.5*30| = |90 - 165|)."},
                {"q": "What is an idempotent HTTP method?", "a": "A method whose side effects on the server are identical whether executed once or multiple times (e.g. GET, PUT, DELETE)."},
                {"q": "Why can a relational database table have only ONE clustered index?", "a": "Because the clustered index defines the actual physical storage order of rows on disk, and physical rows can only be sorted in one order."},
                {"q": "What is the net percentage change when a value is increased by 20% and then decreased by 20%?", "a": "4% decrease (Formula: (20/10)^2 = 4% loss)."},
                {"q": "How does binary search midpoint calculation avoid integer overflow?", "a": "By writing `mid = left + (right - left) // 2` instead of `(left + right) // 2`."},
                {"q": "What is the primary difference between 3NF and BCNF?", "a": "BCNF mandates that for every functional dependency X -> Y, X must be a superkey, eliminating dependencies on prime attributes permitted in 3NF."},
                {"q": "Why is Write-Ahead Logging (WAL) essential for concurrent reads in SQLite?", "a": "It allows concurrent readers to continue reading from previous snapshots without being blocked by ongoing write operations."}
            ]
        }
    }

    # DAY 30
    days[30] = {
        "day": 30,
        "title": "Exam Hall Strategy, Placement Day-Zero Mental Protocol & Final Sign-Off",
        "sem_data": {
            "subject": "The BCA Placement & Semester 5 Master Protocol",
            "topic": "Final Exam Hall Protocol, Answer Booklet Formatting & The BCA Placement Clearance Creed",
            "detailed_notes": [
                "The SGPA 9.0 Exam Hall Protocol:\n"
                "1. The 15-Minute Paper Reading Strategy:\n"
                "• Scan the entire paper immediately upon distribution.\n"
                "• Select the 4 strongest 15-mark questions where you can execute the 5-tier presentation blueprint (Definition, Boxed Diagram, Equations, Comparison Table, Conclusion).\n"
                "• Avoid starting with ambiguous or purely theoretical questions.\n"
                "2. Time Budgeting (Strict 180 Minutes Rule):\n"
                "• Question 1 (15 Marks): 35 Minutes.\n"
                "• Question 2 (15 Marks): 35 Minutes.\n"
                "• Question 3 (15 Marks): 35 Minutes.\n"
                "• Question 4 (15 Marks): 35 Minutes.\n"
                "• Compulsory Short Notes (15 Marks): 30 Minutes.\n"
                "• Final Review & Diagram Underlining: 10 Minutes.\n"
                "3. Visual Presentation Standards:\n"
                "• Use blue ink for body text, black ink for headings, and pencil with ruler for all architecture diagrams and comparison table borders.\n"
                "• Never crowd formulas; allocate 2 blank lines above and below every mathematical expression.\n"
                "• Box final numerical solutions: e.g. `[ x = 2.426, y = 3.573, z = 1.926 ]`.",
                "Day-Zero Placement Interview Protocol:\n"
                "• The 3-Second Pause Rule: When asked an algorithmic or system design question, do not blurt out the first thought. Take 3 seconds to breathe, structure your answer into 3 bullets, and speak deliberately.\n"
                "• Think Out Loud: In coding rounds, interviewers evaluate your communication and problem-solving process, not just final code syntax. Explain brute-force first, analyze complexity, then optimize.\n"
                "• The BCA Advantage: Stand tall. You have built production software, mastered core computer science, solved 50+ DSA problems, and conquered university academics. Your proof is in your code."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                  THE 30-DAY MASTER PREPARATION COMPLETION               |\n"
                "+-------------------------------------------------------------------------+\n"
                "|                                                                         |\n"
                "|   [ SEMESTER 5 TARGET: SGPA >= 9.0 ]   [ PLACEMENT TARGET: CLEARED ]    |\n"
                "|                 |                                      |                |\n"
                "|                 v                                      v                |\n"
                "|   +--------------------------+           +--------------------------+   |\n"
                "|   | BCA-5001: KM Mastered    |           | Aptitude: Speed & Trap   |   |\n"
                "|   | BCA-5002: Java Mastered  |           | DSA: Patterns Mastered   |   |\n"
                "|   | BCA-5003: Netw. Mastered |           | Core CS: Interview Ready |   |\n"
                "|   | BCA-5004: Num. Mastered  |           | Projects: Bulletproofed  |   |\n"
                "|   +--------------------------+           +--------------------------+   |\n"
                "|                 \\                                      /                |\n"
                "|                  \\                                    /                 |\n"
                "|                   v                                  v                  |\n"
                "|            +------------------------------------------------+           |\n"
                "|            |       SARTHAK SRIVASTAVA — DAY 30 MASTERED     |           |\n"
                "|            +------------------------------------------------+           |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Preparation Dimension", "Day 1 Baseline", "Day 30 Mastered State"],
                "rows": [
                    ["Semester 5 Readiness", "Uncertain syllabus scope, anxious about PYQs", "SGPA 9.0 presentation mastery, full PYQs solved"],
                    ["Aptitude Speed", "Formula memorization gaps, >2 mins per problem", "Instant pattern recognition, 4-tier shortcuts, <60s"],
                    ["Coding & DSA", "Disjoint LeetCode attempts without patterns", "50+ placement patterns in Python with complexity proofs"],
                    ["Core CS Foundations", "Scattered theoretical facts across subjects", "Deep systems architecture: OS, DBMS, Networks, Python"],
                    ["Project Defenses", "Hesitant about architecture and metrics", "Rock-solid technical defense of BulkBeat TV & TerraStract"],
                    ["Interview Mindset", "Anxious about degree comparison", "Unshakable confidence grounded in verifiable execution"]
                ]
            },
            "memorize": "The 30-Day Creed: Execution beats credentials. Code speaks louder than talk. SGPA 9.0 is my standard; placement clearance is my baseline.",
            "understand": "Why has this 30-day journey transformed your trajectory? Because you did not passively read summaries. You hand-calculated Gauss-Seidel iterations, traced sliding window protocols, built LRU caches from scratch, mastered OS synchronization, and defended your actual production code. You are prepared.",
            "common_mistakes": "1. Second-guessing your preparation in the final hour. 2. Skipping the 10-minute final review in the exam hall.",
            "pyq_year": "CSJMU BCA Final Milestone (2026)",
            "pyq_freq": "The Capstone Milestone of the Entire Handbook",
            "pyq_question": "Declare the BCA Placement Clearance Creed and complete the 30-Day Milestone Sign-Off Board.",
            "pyq_rubric": "Full commitment to academic excellence and placement readiness.",
            "model_answer_paragraphs": [
                ("The BCA Placement Clearance Creed:",
                 "I am Sarthak Srivastava. Over the last 30 days, I have rigorously prepared across academics, aptitude, coding, systems, and projects. I enter every examination hall and interview room not as an applicant hoping for luck, but as a disciplined software engineer who has earned his competence through deliberate execution.")
            ]
        },
        "sgpa_target": {"focus": "Execute Exam Hall Presentation Blueprint for SGPA >= 9.0", "milestone": "Full Preparation Accomplished"},
        "apt_data": {
            "topic": "Final Placement Aptitude Velocity Check & Mental Readiness",
            "tutorial": [
                "The 5 Cardinal Rules for Online Placement Aptitude Tests:\n"
                "1. Keep Scratchwork Organized: Divide your scrap paper into numbered boxes. Never scribble randomly—you will need to verify your numbers!\n"
                "2. Beware of Negative Marking: If the assessment has negative marking, eliminate at least 2 options before making an educated guess; never guess blindly.\n"
                "3. Watch the Sectional Timer: Tests like TCS NQT enforce strict sectional cutoffs with non-navigable sectional timers. Never leave unattempted questions if no negative marking exists.\n"
                "4. Read the Units Carefully: Ensure speed is in m/s when distance is in meters, and time is in seconds.\n"
                "5. Stay Calm Under Pressure: If a question is tough, it is tough for thousands of other students. Protect your mental stamina."
            ],
            "formulas": "Patience + Speed + Accuracy = Placement Clearance.",
            "shortcut": "Deep breath before clicking Start Test. Trust your 30-day preparation.",
            "recognition": "Final mindset alignment.",
            "tier1_problem": "A student scores 85%, 90%, and 95% in 3 subjects of equal weightage. What must he score in the 4th subject to achieve an overall 92% average?",
            "tier1_solution": "Total required = 92 * 4 = 368.\nSum of first 3 = 85 + 90 + 95 = 270.\nRequired score in 4th subject = 368 - 270 = 98%. Answer: 98%.",
            "tier2_problem": "If today is Wednesday, what day will it be after 61 days?",
            "tier2_solution": "Divide by 7 to find odd days: 61 = 8 * 7 + 5 (Remainder = 5 odd days).\nWednesday + 5 days = Thursday, Friday, Saturday, Sunday, Monday. Answer: Monday.",
            "tier3_problem": "A bag contains 5 red, 4 blue, and 3 green balls. If 2 balls are drawn at random, what is the probability that both are of the same color?",
            "tier3_solution": "Total balls = 12. Ways to pick 2 balls = ^12 C_2 = (12 * 11) / 2 = 66.\nBoth Red = ^5 C_2 = 10.\nBoth Blue = ^4 C_2 = 6.\nBoth Green = ^3 C_2 = 3.\nTotal favorable = 10 + 6 + 3 = 19.\nProbability = 19 / 66. Answer: 19/66.",
            "tier4_problem": "Find the remainder when 2^50 is divided by 7.",
            "tier4_solution": "Using Fermat's Little Theorem / modular exponentiation:\n2^1 = 2 mod 7\n2^2 = 4 mod 7\n2^3 = 8 = 1 mod 7!\nExpress exponent in multiples of 3: 50 = 3 * 16 + 2.\n2^50 = (2^3)^16 * 2^2 = (1)^16 * 4 = 1 * 4 = 4 mod 7. Remainder is 4. Answer: 4.",
            "speed_drills": [
                {"q": "Remainder of 2^31 divided by 5?", "a": "2^4 = 1 mod 5. 31 = 4*7 + 3. 2^3 = 8 = 3 mod 5."},
                {"q": "Leap year has how many odd days?", "a": "366 % 7 = 2 odd days."},
                {"q": "Value of 0.333... in fraction?", "a": "1/3."},
                {"q": "If 10 men do a job in 20 days, how many men for 5 days?", "a": "10 * 20 / 5 = 40 men."},
                {"q": "Cube root of 2197?", "a": "13 (since 13^3 = 2197)."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Placement Coding Round Zero-Bug Checklist",
                "difficulty": "Meta-Algorithm",
                "importance": "The Pre-Submission Protocol in Online Assessments",
                "problem_statement": "Review the mental checklist to run before clicking 'Submit Code' on HackerRank, Mettl, or TCS iON.",
                "solution_approach": (
                    "The 5-Point Pre-Submission Audit:\n"
                    "1. Edge Cases: Have you checked empty input (`[]`, `\"\"`, `None`), single element (`[1]`), and duplicates (`[2, 2, 2]`)?\n"
                    "2. Integer Constraints: Can numbers exceed 32-bit limits? (Python handles arbitrarily large integers natively, but be aware of floating-point inaccuracies).\n"
                    "3. Off-by-One Errors: Check loop bounds (`range(n)` vs `range(n-1)`, `<= ` vs `<`).\n"
                    "4. Time Complexity: Will an O(N^2) solution get TLE for N = 10^5? (Ensure O(N) or O(N log N)).\n"
                    "5. Memory Leaks: Did you clear recursion stacks or avoid unnecessary copies?"
                ),
                "code": (
                    "# Master Template: Clean, Robust Python Function\n"
                    "def solve(nums: list[int]) -> int:\n"
                    "    if not nums:\n"
                    "        return 0\n"
                    "    # Algorithmic core\n"
                    "    res = 0\n"
                    "    for x in nums:\n"
                    "        res += x\n"
                    "    return res"
                ),
                "line_by_line": [
                    ("if not nums: return 0", "Defensive boundary check prevents IndexError / NoneType crashes.")
                ],
                "time_complexity": "Optimized to problem constraints.",
                "space_complexity": "Minimal auxiliary memory.",
                "edge_cases": "Zero, negative, max limits."
            }
        ],
        "cs_core": {
            "subject": "Final Interview Readiness",
            "topic": "The Day-Zero Technical Interview Demeanor & Presentation",
            "detailed_notes": [
                "Interview Day Mental Architecture:\n"
                "• Professional Presence: Clean background, good lighting, clear audio, camera at eye level.\n"
                "• When You Do Not Know an Answer: Never guess wildly or pretend. Say: 'I have not worked directly with that specific framework, but based on my understanding of networking and operating systems, here is how I would reason through it...'\n"
                "• Asking Questions at the End: Never say 'No, I have no questions'. Ask insightful technical questions:\n"
                "  1. 'What is the primary architecture challenge your engineering team is tackling this quarter?'\n"
                "  2. 'How does your team handle continuous deployment and code reviews for junior developers?'"
            ],
            "interview_qa": [
                {
                    "q": "Do you have any questions for us?",
                    "a": "Yes! I saw that your team handles high-throughput user transactions. I would love to know: what message queuing and caching architectures do you currently rely on in production, and what is the biggest technical challenge your backend engineers are solving right now?"
                },
                {
                    "q": "Why should we select you today?",
                    "a": "Because I combine solid computer science fundamentals with proven hands-on development experience. In my projects, I haven't just followed tutorials—I have built and deployed live systems, resolved real concurrency bottlenecks, implemented complex OCR pipelines, and designed clean relational schemas. I am eager to bring this same discipline and work ethic to your engineering team."
                }
            ]
        },
        "project_defense": {
            "project_name": "Final Capstone Sign-Off",
            "feature_focus": "The 30-Day Project Portfolio Milestone Sign-Off",
            "architecture_deep_dive": (
                "Final Verification of Flagship Portfolio Assets:\n\n"
                "• BulkBeat TV: Real-time media streaming, aiohttp backend, Telegram bot webhooks, SQLite WAL concurrency, token bucket rate limiting.\n"
                "• TerraStract: Hybrid document AI, PyMuPDF vector extraction, Tesseract OCR PSM 6 fallback, Hindi Unicode regex normalization, async exception queue.\n"
                "• CSMS: Car Showroom Management System, FastAPI, SQLAlchemy ORM, Alembic migrations, PostgreSQL, JWT role-based access control.\n"
                "• BEVM: Biometric Electronic Voting Machine, Fernet AES-256 encryption, chained SHA-256 tamper-evident audit logs.\n\n"
                "All 4 projects stand verified, documented, and ready for technical demonstration."
            ),
            "interview_qa": [
                {
                    "q": "What is the single most valuable lesson you learned building these projects?",
                    "a": "That building software is 20% writing code and 80% understanding trade-offs: choosing the right concurrency model, managing database locks, designing for network failure, and making deliberate architectural decisions rather than following hype."
                },
                {
                    "q": "Are you ready to join a production engineering team?",
                    "a": "Yes. I am confident in my fundamentals, comfortable working in Linux and Git environments, experienced with Docker and async APIs, and committed to continuous learning."
                }
            ]
        },
        "daily_test": {
            "day": 30,
            "questions": [
                {"q": "What is the time allocation rule for a 15-mark university exam question?", "a": "Strictly 35 minutes per question across 4 selected questions, leaving 30 minutes for short notes and 10 minutes for final review."},
                {"q": "If today is Wednesday, what day will it be after 61 days?", "a": "Monday (61 mod 7 = 5 odd days; Wednesday + 5 days = Monday)."},
                {"q": "What are the 5 checks in the Pre-Submission Coding Checklist?", "a": "1. Edge cases, 2. Integer constraints, 3. Off-by-one errors, 4. Time complexity feasibility, 5. Memory efficiency."},
                {"q": "What should you do when you don't know the exact answer to an interview question?", "a": "Acknowledge that you haven't worked with that specific tool, then transparently reason through first principles from OS/networking/data structures."},
                {"q": "What is the remainder when 2^50 is divided by 7?", "a": "4 (Since 2^3 = 1 mod 7, 2^50 = (2^3)^16 * 2^2 = 1 * 4 = 4 mod 7)."},
                {"q": "What question should you always ask the interviewer at the end of a placement interview?", "a": "Ask an insightful technical question about their team's production architecture, scalability challenges, or deployment workflows."},
                {"q": "Why is the 3-second pause rule effective in technical interviews?", "a": "It prevents impulsive answers, calms nerves, and allows you to structure your response into clear, structured architectural points."},
                {"q": "State your final target for Semester 5 and Campus Placements.", "a": "Semester 5 Target: SGPA >= 9.0. Campus Placement Target: Clearance across Aptitude, Coding, Core CS, and Technical Interviews."}
            ]
        }
    }

    return days
