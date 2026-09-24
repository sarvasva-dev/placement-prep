# Days 20 to 24 Curriculum Definition with Publication-Grade Pedagogical Depth

def get_days_20_to_24():
    days = {}

    # DAY 20
    days[20] = {
        "day": 20,
        "title": "KM Systems Life Cycle (KMSLC), Direction Sense & DP (Climbing Stairs & House Robber)",
        "sem_data": {
            "subject": "BCA-5001 Knowledge Management",
            "topic": "Unit IV — Knowledge Management System Life Cycle (KMSLC 8 Stages) vs Conventional SDLC",
            "detailed_notes": [
                "The Knowledge Management System Life Cycle (KMSLC) is a specialized systems development framework designed specifically to capture, structure, refine, and deploy organizational tacit and explicit knowledge. Unlike conventional software development which focuses on data processing and predefined business logic, KMSLC addresses continuous learning, tacit-to-explicit knowledge conversion, and cultural alignment.",
                "The 8 Stages of KMSLC:\n"
                "1. Evaluate Existing Infrastructure: Audit existing organizational systems, data warehouses, networks, and cultural readiness for knowledge sharing.\n"
                "2. Form the KM Team: Assemble cross-functional experts including Knowledge Developers (K-Developers), Domain Experts, Systems Architects, and Top Management champions.\n"
                "3. Capture Knowledge: Solicit both explicit and tacit expertise using Delphi techniques, protocol analysis, cognitive maps, and structured expert interviews.\n"
                "4. Design the KM Blueprint: Architectural design of knowledge repositories, indexing taxonomies, access control rules, ontology mappings, and user interface workflows.\n"
                "5. Develop the KM System: Implement the physical repositories, indexing engines, collaborative groupware tools, and AI/inference components.\n"
                "6. Verify & Validate the KM System: Verification tests whether the system meets design specifications ('Did we build the system right?'). Validation ensures the captured knowledge accurately reflects expert wisdom and provides actionable advice ('Did we build the right system?').\n"
                "7. Deploy the System: Roll out the KMS into organizational operations, conduct employee onboarding programs, align incentive structures to reward knowledge sharing, and overcome organizational resistance.\n"
                "8. Manage Post-Implementation: Continuous maintenance, auditing obsolete knowledge chunks, retiring outdated rules, and refining search models based on ongoing feedback.",
                "Comparison with Conventional SDLC:\n"
                "• Conventional SDLC follows sequential processes (Requirements -> Analysis -> Design -> Coding -> Testing -> Maintenance) oriented towards structured data processing and algorithmic workflows.\n"
                "• KMSLC is inherently iterative and non-linear, centering on human experts and tacit heuristics that evolve organically."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                     THE 8 STAGES OF KMSLC WORKFLOW                      |\n"
                "+-------------------------------------------------------------------------+\n"
                "|  Stage 1: Evaluate Existing Infrastructure (Readiness Audit)            |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  Stage 2: Form the KM Team (K-Developers, Experts, Champions)           |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  Stage 3: Capture Knowledge (Tacit & Explicit Extraction)               |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  Stage 4: Design KM Blueprint (Taxonomies, Repositories, Security)      |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  Stage 5: Develop the KMS (Prototyping & Repository Building)           |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  Stage 6: Verify & Validate (Accuracy & Expert Truth Alignment)         |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  Stage 7: Deploy & Cultural Training (Incentivize Sharing)              |\n"
                "|         |                                                               |\n"
                "|         v                                                               |\n"
                "|  Stage 8: Post-Implementation Maintenance (Continuous Evolution)        |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Comparison Dimension", "Conventional SDLC", "KM Systems Life Cycle (KMSLC)"],
                "rows": [
                    ["Primary Focus", "Process automation & structured data manipulation", "Tacit and explicit knowledge capture and sharing"],
                    ["User/Expert Role", "User specifies business functional requirements", "Domain expert provides heuristic rules & intuition"],
                    ["Development Philosophy", "Sequential, milestone-driven (Waterfall/Agile)", "Evolutionary, rapid prototyping, highly iterative"],
                    ["Nature of Output", "Predictable software outputs from numeric/text inputs", "Context-rich recommendations and decision support"],
                    ["Success Criteria", "On-time, within budget, zero defects", "User adoption, cultural sharing, retention of knowledge"],
                    ["Testing Goal", "System verification (bugs, crashes, functional correctness)", "Knowledge validation (expert agreement, decision quality)"]
                ]
            },
            "memorize": "8 Stages: Evaluate -> Form Team -> Capture -> Blueprint -> Develop -> Verify/Validate -> Deploy -> Post-Implementation. Validation tests expert truth; Verification tests software specs.",
            "understand": "Why does conventional SDLC fail for Knowledge Management? In SDLC, requirements can be frozen early. But human tacit knowledge cannot be specified in advance—it surfaces incrementally through ongoing interaction between the K-Developer and the domain expert.",
            "common_mistakes": "1. Confusing Verification ('built right') with Validation ('built right system'). 2. Omitting cultural incentive alignment from Stage 7 (technology alone does not make employees share knowledge).",
            "pyq_year": "CSJMU BCA-5001 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "High-Frequency 15-Mark Question: 2021 (Q7 - 15m), 2022-23 (Q6 - 15m), 2023-24 (Q7 - 15m), 2024-25 (Q6 - 15m)",
            "pyq_question": "Explain the Knowledge Management System Life Cycle (KMSLC) in detail with all its 8 stages. Contrast KMSLC with the conventional Software Development Life Cycle (SDLC) using a comprehensive comparison table. (15 Marks)",
            "pyq_rubric": "Concept & Importance of KMSLC (3 marks) + 8 Stages detailed breakdown with flow diagram (6 marks) + Verification vs Validation distinction (2 marks) + Comparison table with SDLC (4 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Concept of Knowledge Management System Life Cycle (KMSLC):",
                 "KMSLC is an iterative systems framework focused on capturing, codifying, refining, and sharing human expertise across an enterprise. While traditional software development automates transactional workflows (e.g. billing, inventory), KMSLC manages organizational intellectual capital and tacit knowledge resident in people's minds."),
                ("2. The 8 Stages of KMSLC Detailed Analysis:",
                 "• Stage 1 (Evaluate Existing Infrastructure): Audits current technological readiness, network bandwidth, repository storage, and corporate culture to identify gaps in knowledge sharing.\n"
                 "• Stage 2 (Form the KM Team): Mobilizes multidisciplinary stakeholders: Knowledge Developers (knowledge elicitation specialists), Domain Experts, End-Users, and Executive Champions.\n"
                 "• Stage 3 (Capture Knowledge): Employs structured interviews, cognitive mapping, brainstorming sessions, and observation to elicit tacit rules of thumb and compile explicit artifacts.\n"
                 "• Stage 4 (Design KM Blueprint): Outlines logical data structures, ontologies, security privileges, and metadata tagging hierarchies to ensure fast retrieval.\n"
                 "• Stage 5 (Develop the KMS): Translates blueprints into operational prototypes using enterprise search engines, document repositories, and recommendation systems.\n"
                 "• Stage 6 (Verify and Validate): Verification ensures code functions without technical defects; Validation verifies the knowledge stored is factually correct and endorsed by experts.\n"
                 "• Stage 7 (Deploy the System): Implements rollout strategies, user onboarding workshops, and reward structures to encourage knowledge contributors.\n"
                 "• Stage 8 (Manage Post-Implementation): Establishes ongoing knowledge audits, purging deprecated practices, and updating taxonomies as business conditions shift."),
                ("3. Verification vs Validation in KMSLC:",
                 "In conventional systems, testing focuses on algorithmic execution. In KMSLC, 'Verification' answers: 'Did we build the system to technical specifications?' whereas 'Validation' answers: 'Is the captured knowledge accurate, consistent, and trusted by top practitioners?'"),
                ("4. Key Differences Between KMSLC and SDLC:",
                 "The primary dichotomy lies in uncertainty management. In SDLC, requirements are fixed before coding. In KMSLC, requirements and rules are continuously uncovered as domain experts interact with functional prototypes.")
            ]
        },
        "sgpa_target": {"focus": "Master all 8 KMSLC Stages and Verification vs Validation", "milestone": "Full 15/15 on KM Unit IV Exam Question"},
        "apt_data": {
            "topic": "Logical Reasoning — Direction Sense & Coding-Decoding Puzzles",
            "tutorial": [
                "Direction Sense Methodology:\n"
                "• Standard Cardinal Directions: North (Up), South (Down), East (Right), West (Left).\n"
                "• Turns: Right Turn = 90-degree clockwise; Left Turn = 90-degree counter-clockwise.\n"
                "• Pythagoras Theorem for Shortest Distance: Shortest Displacement d = sqrt((Delta X)^2 + (Delta Y)^2).\n"
                "• Shadows at Sunrise (Sun in East): Shadows fall towards West. A person facing North has their shadow on their Left.\n"
                "• Shadows at Sunset (Sun in West): Shadows fall towards East. A person facing North has their shadow on their Right.",
                "Coding-Decoding Rules:\n"
                "• Letter Positions: A=1, B=2, ..., Z=26 (Recall mnemonic EJOTY: 5, 10, 15, 20, 25).\n"
                "• Reverse Pairs: Sum of positions = 27 (A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N)."
            ],
            "formulas": "Displacement: d = sqrt(x^2 + y^2). Opposite letters sum to 27.",
            "shortcut": "Cancel Opposite Movements: 50m North followed by 50m South cancels out to 0. Net vector addition simplifies complex walking routes.",
            "recognition": "Look for 'A man walks 10 km towards North, then turns right...', or 'In a certain code, COMPUTER is written as RFUVQNPC...'",
            "tier1_problem": "A man walks 5 km East, then turns right and walks 12 km. How far is he from his starting point, and in which direction?",
            "tier1_solution": "Starting at (0, 0). 5 km East ==> (+5, 0). Turning right (facing East, right turn is South) and walking 12 km ==> (+5, -12). Shortest distance d = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13 km. Direction from start: South-East. Answer: 13 km, South-East.",
            "tier2_problem": "One morning after sunrise, Suresh was standing facing a pole. The shadow of the pole fell exactly to his right. Which direction was Suresh facing?",
            "tier2_solution": "At sunrise, sun is in East, so shadows fall towards WEST. The shadow fell to Suresh's right, which means Suresh's RIGHT side is WEST. If Right is West, Suresh's Left is East, his Back is North, and his Face is towards SOUTH. Answer: South.",
            "tier3_problem": "[Infosys Reasoning Round] If 'TEACHER' is coded as 'VGCEJGT', how is 'CHILDREN' coded in that language?",
            "tier3_solution": "Analyze pattern: T(+2)=V, E(+2)=G, A(+2)=C, C(+2)=E, H(+2)=J, E(+2)=G, R(+2)=T. Each letter is shifted by +2 positions. Applying to 'CHILDREN': C(+2)=E, H(+2)=J, I(+2)=K, L(+2)=N, D(+2)=F, R(+2)=T, E(+2)=G, N(+2)=P. Output: EJKNFTGP. Answer: EJKNFTGP.",
            "tier4_problem": "[Cognizant GenC Next Pattern] Point A is 8m North of Point B. Point C is 6m West of Point B. Point D is 12m South of Point C. Point E is 15m East of Point D. Find the shortest distance and direction of Point E with respect to Point A.",
            "tier4_solution": "Set Point B as origin (0, 0).\nPoint A = (0, 8).\nPoint C = (-6, 0).\nPoint D = (-6, -12).\nPoint E = (-6 + 15, -12) = (9, -12).\nDisplacement from A(0, 8) to E(9, -12):\nDelta X = 9 - 0 = 9.\nDelta Y = -12 - 8 = -20.\nShortest distance = sqrt(9^2 + (-20)^2) = sqrt(81 + 400) = sqrt(481) ≈ 21.93 m.\nDirection of E with respect to A: East (+X) and South (-Y) ==> South-East. Answer: sqrt(481) m (approx 21.93 m), South-East.",
            "speed_drills": [
                {"q": "A person walks 20m North, turns left and walks 15m, turns left and walks 20m. How far is he from start?", "a": "15m West. The 20m North and 20m South cancel out."},
                {"q": "At sunset, two friends A and B are talking face to face. If A's shadow is to his left, which way is A facing?", "a": "North. At sunset, shadow is towards East. If East is to A's left, A faces North."},
                {"q": "If CAT = 24, DOG = 26, then BIRD = ?", "a": "B(2)+I(9)+R(18)+D(4) = 33."},
                {"q": "If 'LIGHT' is coded as 'MJHIU', what is 'FLAME'?", "a": "Each letter +1: GMBNF."},
                {"q": "A car moves 10km North, turns 45 degrees right and travels 10km. In which direction is it moving?", "a": "North-East."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Climbing Stairs (LeetCode 70 - Easy)",
                "difficulty": "Easy",
                "importance": "The Fundamental Dynamic Programming Archetype Problem",
                "problem_statement": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
                "solution_approach": (
                    "Dynamic Programming Recurrence:\n"
                    "To reach step n, you must arrive from step n-1 (taking 1 step) or step n-2 (taking 2 steps).\n"
                    "Recurrence Relation: ways(n) = ways(n - 1) + ways(n - 2).\n"
                    "Base Cases: ways(1) = 1, ways(2) = 2.\n"
                    "Space Optimization: Since each state depends only on the previous 2 values, use two variables instead of an O(N) array."
                ),
                "code": (
                    "def climbStairs(n: int) -> int:\n"
                    "    if n <= 2:\n"
                    "        return n\n"
                    "        \n"
                    "    prev2, prev1 = 1, 2\n"
                    "    for i in range(3, n + 1):\n"
                    "        curr = prev1 + prev2\n"
                    "        prev2 = prev1\n"
                    "        prev1 = curr\n"
                    "        \n"
                    "    return prev1"
                ),
                "line_by_line": [
                    ("if n <= 2: return n", "Direct base case handling for 1 step (1 way) and 2 steps (2 ways)."),
                    ("prev2, prev1 = 1, 2", "Initialize sliding window representing dp[i-2] and dp[i-1]."),
                    ("curr = prev1 + prev2", "Apply Fibonacci-style state transition."),
                    ("prev2 = prev1; prev1 = curr", "Shift window forward for next step.")
                ],
                "time_complexity": "O(N) single loop iteration.",
                "space_complexity": "O(1) auxiliary memory using two integer variables.",
                "edge_cases": "n = 1 (returns 1); n = 2 (returns 2); n = 45 (max constraint)."
            },
            {
                "title": "House Robber (LeetCode 198 - Medium)",
                "difficulty": "Medium",
                "importance": "Standard Placement Dynamic Programming Problem (Amazon, Infosys, Microsoft)",
                "problem_statement": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. Adjacent houses have security systems connected and will automatically contact the police if two adjacent houses were broken into on the same night. Return the maximum amount of money you can rob tonight without alerting the police.",
                "solution_approach": (
                    "DP Recurrence Formulation:\n"
                    "For each house i with money nums[i], you have two distinct choices:\n"
                    "1. Rob house i: Gain nums[i] + max profit up to house i-2.\n"
                    "2. Skip house i: Max profit is equal to max profit up to house i-1.\n"
                    "State Transition: dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]).\n"
                    "Optimized in O(1) space with two variables: `rob1` and `rob2`."
                ),
                "code": (
                    "def rob(nums: list[int]) -> int:\n"
                    "    rob1, rob2 = 0, 0\n"
                    "    \n"
                    "    # [rob1, rob2, n, n+1, ...]\n"
                    "    for n in nums:\n"
                    "        temp = max(n + rob1, rob2)\n"
                    "        rob1 = rob2\n"
                    "        rob2 = temp\n"
                    "        \n"
                    "    return rob2"
                ),
                "line_by_line": [
                    ("rob1, rob2 = 0, 0", "Initialize running maximums for two houses prior and one house prior."),
                    ("temp = max(n + rob1, rob2)", "Compare robbing current house (n + rob1) vs skipping current house (rob2)."),
                    ("rob1 = rob2; rob2 = temp", "Slide running window forward to maintain O(1) auxiliary space.")
                ],
                "time_complexity": "O(N) — Single pass through list.",
                "space_complexity": "O(1) — Constant memory variables.",
                "edge_cases": "Single house [nums[0]]; empty list; houses with 0 money."
            }
        ],
        "cs_core": {
            "subject": "Computer Networks",
            "topic": "DNS Hierarchy & The HTTPS TLS 1.3 Cryptographic Handshake",
            "detailed_notes": [
                "Domain Name System (DNS) Architecture:\n"
                "• Distributed hierarchical database resolving human hostnames (`api.example.com`) to 32-bit IPv4 / 128-bit IPv6 addresses.\n"
                "• 4 Resolution Layers: 1. Local DNS Cache (Browser/OS), 2. Recursive Resolver (ISP / 8.8.8.8), 3. Root Name Servers (13 logical root server authorities), 4. TLD Servers (.com, .org), 5. Authoritative Name Server (holds master DNS zone file).\n"
                "• Recursive Query (Client to Resolver: 'Find this for me') vs Iterative Query (Resolver to Roots/TLD: 'Refer me to next server').",
                "The HTTPS TLS 1.3 Handshake (1-RTT Optimization):\n"
                "In TLS 1.2, handshakes took 2 Round Trips (2-RTT). TLS 1.3 reduces latency to a single round trip (1-RTT):\n"
                "1. ClientHello: Client sends supported cipher suites and public key share using Ephemeral Diffie-Hellman (ECDHE).\n"
                "2. ServerHello: Server selects cipher suite, sends its ECDHE public key share, server certificate (X.509), and digital signature. Both compute the symmetric master key independently!\n"
                "3. Encrypted Data: Immediate transmission of encrypted application data (HTTP/2 or HTTP/3 frames) using AES-GCM or ChaCha20-Poly1305."
            ],
            "interview_qa": [
                {
                    "q": "What happens when you type 'https://www.google.com' into your browser address bar?",
                    "a": "1. DNS Resolution: Browser checks local cache -> OS hosts file -> Recursive resolver queries Root -> TLD (.com) -> Authoritative server to obtain IP address.\n2. TCP 3-Way Handshake: SYN -> SYN-ACK -> ACK establishes reliable transport socket on port 443.\n3. TLS 1.3 Handshake: ClientHello with key share -> ServerHello with certificate and server key share -> Symmetric session keys derived -> Certificate verified against root CAs.\n4. HTTP Request: Browser sends encrypted GET / HTTP/2 frame.\n5. Server processes request and streams HTML response; browser parses DOM, fetches CSS/JS, and paints page."
                },
                {
                    "q": "Why is TLS 1.3 significantly faster and more secure than TLS 1.2?",
                    "a": "Speed: TLS 1.3 eliminated an entire network round trip by piggybacking cryptographic key shares directly into the ClientHello message (1-RTT). Security: Obsolete and vulnerable cryptographic primitives were completely stripped out (MD5, SHA-1, RC4, static RSA key exchange). TLS 1.3 mandates Forward Secrecy via ephemeral Diffie-Hellman (ECDHE), ensuring that even if a server's private key is compromised in the future, past intercepted communications cannot be decrypted."
                }
            ]
        },
        "project_defense": {
            "project_name": "Biometric Electronic Voting System (BEVM)",
            "feature_focus": "Tamper-Evident Cryptographic Ledger & Chained SHA-256 Hashes",
            "architecture_deep_dive": (
                "BEVM operates as an air-gapped cryptographic voting platform designed to prevent retroactive ballot manipulation.\n\n"
                "1. Chained Hash Architecture:\n"
                "• Each cast vote block incorporates the SHA-256 hash of the immediately preceding ballot block (H_i = SHA256(H_{i-1} + ballot_data)).\n"
                "• If an attacker alters or injects a past ballot in SQLite, the sequential hash chain breaks mathematically at that exact block index.\n\n"
                "2. Decoupled Voter Privacy & State Flagging:\n"
                "• Voter authentication sets has_voted = 1 in an atomic SQLite transaction, completely separated from ballot choices stored in the votes table.\n"
                "• Ballots are encrypted with Fernet AES-256 before disk writes, guaranteeing that intermediate counts cannot be inspected until official decryption."
            ),
            "interview_qa": [
                {
                    "q": "How does BEVM mathematically prove that ballots were not altered in SQLite?",
                    "a": "BEVM implements an append-only sequential SHA-256 hash chain where each block incorporates the preceding block's hash. A forensic traversal script recalculates all block hashes prior to tally publication; any modified bit in historical records invalidates all subsequent hashes, providing mathematical proof of zero tampering."
                },
                {
                    "q": "How does BEVM ensure voter secrecy while preventing double-voting?",
                    "a": "Voter biometric verification and ballot recording are strictly decoupled. When a citizen authenticates, their record in the voters table sets has_voted = 1 within an atomic SQLite transaction. The encrypted ballot is stored in an independent votes table with no linkable identifier connecting voter identity to candidate preference."
                }
            ]
        },
        "daily_test": {
            "day": 20,
            "questions": [
                {"q": "Name the 8 stages of the Knowledge Management System Life Cycle (KMSLC).", "a": "1. Evaluate Existing Infrastructure, 2. Form KM Team, 3. Capture Knowledge, 4. Design KM Blueprint, 5. Develop KMS, 6. Verify & Validate, 7. Deploy System, 8. Manage Post-Implementation."},
                {"q": "What is the key difference between Verification and Validation in KMSLC?", "a": "Verification ensures the system conforms to software design specifications ('Built right'). Validation ensures the captured knowledge accurately reflects expert wisdom and provides valid actionable decisions ('Built the right system')."},
                {"q": "A person walks 10m East, turns left and walks 10m, then turns right and walks 10m. What is his displacement from start?", "a": "sqrt(20^2 + 10^2) = sqrt(500) = 10*sqrt(5) ≈ 22.36m North-East."},
                {"q": "What is the recurrence relation for LeetCode 198 (House Robber)?", "a": "dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Rob current house + max profit from 2 houses ago, or skip current house."},
                {"q": "What is the space complexity of optimized LeetCode 70 (Climbing Stairs)?", "a": "O(1) constant auxiliary space using two integer variables to track the previous two steps."},
                {"q": "What is the difference between Recursive and Iterative DNS queries?", "a": "A recursive query requires the contacted server to find the final IP answer and return it. In an iterative query, if the server doesn't know the answer, it returns a referral to the next server authority down the hierarchy."},
                {"q": "How many round trips (RTT) does the TLS 1.3 handshake require before encrypted data transmission?", "a": "Exactly 1-RTT. The client sends key shares directly inside the ClientHello message."},
                {"q": "Why is an HTTP 202 status code appropriate for heavy background OCR jobs?", "a": "HTTP 202 Accepted signifies that the request has been validated and queued for background asynchronous processing, decoupling heavy compute from synchronous client HTTP timeouts."}
            ]
        }
    }

    # DAY 21
    days[21] = {
        "day": 21,
        "title": "Java Session Tracking, Seating Arrangements, Stock DP & DBMS Window Functions",
        "sem_data": {
            "subject": "BCA-5002 Java Programming",
            "topic": "Unit IV — Session Tracking in Web Applications: Cookies, Hidden Form Fields, URL Rewriting & HttpSession",
            "detailed_notes": [
                "HTTP is inherently a stateless protocol: every incoming HTTP request is treated as independent with no memory of prior client interactions. Session tracking is the mechanism used by web containers to maintain conversational state across multiple requests from the same user (e.g., shopping cart, authentication login).",
                "The 4 Primary Session Tracking Mechanisms in Java Servlets:\n"
                "1. Cookies (`javax.servlet.http.Cookie`):\n"
                "• Small key-value text tokens sent by the server via the `Set-Cookie` HTTP header and stored locally on the client's browser disk/RAM.\n"
                "• On subsequent requests to that domain, the browser automatically transmits the cookies in the `Cookie` request header.\n"
                "• Persistent Cookie (has `setMaxAge(seconds) > 0`) vs Non-Persistent / Session Cookie (`setMaxAge(-1)` destroyed when browser closes).\n"
                "• Limitations: Users can disable cookies in browser settings; maximum size is limited to 4KB per cookie; security vulnerabilities if sensitive data is stored unencrypted.",
                "2. Hidden Form Fields:\n"
                "• HTML form elements `<input type=\"hidden\" name=\"sessionId\" value=\"XYZ123\">` embedded directly into dynamic HTML pages.\n"
                "• Invisible to users on the page, but submitted with form POST/GET requests.\n"
                "• Limitations: Only works for pages reached via HTML `<form>` submissions; navigating via normal hyperlink clicks (`<a>`) fails to transmit hidden fields.",
                "3. URL Rewriting:\n"
                "• The session identifier is dynamically appended to the end of every URL hyperlink: `href=\"catalog.jsp;jsessionid=1048576\"`.\n"
                "• Implemented in Servlets using `response.encodeURL(url)` or `response.encodeRedirectURL(url)`.\n"
                "• Advantage: Works 100% reliably even if the client browser has completely disabled cookies!\n"
                "• Limitations: Exposes session IDs in browser address bars and server access logs; tedious because every URL in the app must be rewritten.",
                "4. HttpSession API (Container-Managed Sessions):\n"
                "• High-level, enterprise-standard session tracking interface provided by the Web Container (Tomcat).\n"
                "• Server generates a unique 128-bit session token (`JSESSIONID`) and stores actual conversational objects in server memory.\n"
                "• The container sends the `JSESSIONID` to the browser via a session cookie (or URL rewriting fallback).\n"
                "• Methods: `request.getSession(true)` (creates or retrieves session), `session.setAttribute(name, obj)`, `session.getAttribute(name)`, `session.invalidate()` (logout/destroy session), `session.setMaxInactiveInterval(seconds)`."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                     HTTPSESSION ARCHITECTURE & FLOW                     |\n"
                "+-------------------------------------------------------------------------+\n"
                "|                                                                         |\n"
                "|   BROWSER                                            APACHE TOMCAT      |\n"
                "|      |                                                     |            |\n"
                "|      |--- 1. POST /login (username, password) ------------>|            |\n"
                "|      |                                                     | Create:    |\n"
                "|      |                                                     | HttpSession|\n"
                "|      |<-- 2. HTTP 200 OK [Set-Cookie: JSESSIONID=AB8912] --| Object     |\n"
                "|      |                                                     | in RAM     |\n"
                "|      |                                                     |            |\n"
                "|      |--- 3. GET /cart [Cookie: JSESSIONID=AB8912] ------->| Lookup     |\n"
                "|      |                                                     | Session    |\n"
                "|      |<-- 4. HTTP 200 OK (Render user-specific cart) ------| by ID      |\n"
                "|      |                                                     |            |\n"
                "|      |--- 5. GET /logout --------------------------------->| session.   |\n"
                "|      |                                                     | invalidate |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Tracking Technique", "Where State is Stored", "Client Cookie Dependency", "Security Risk", "Ease of Implementation"],
                "rows": [
                    ["Cookies", "Client browser storage", "Requires cookies enabled", "High (XSS attacks, tampering)", "Simple (`Cookie` class)"],
                    ["Hidden Form Fields", "Embedded inside HTML forms", "No cookie dependency", "Moderate (view source reveals ID)", "Cumbersome (forms only)"],
                    ["URL Rewriting", "Appended to URL query path", "No cookie dependency", "High (URL logging & referer leaks)", "Moderate (encodeURL)"],
                    ["HttpSession", "Server RAM (Container heap)", "Uses JSESSIONID cookie / fallback", "Very Low (data stays on server)", "High (Standard API)"]
                ]
            },
            "memorize": "HTTP is stateless. 4 Session methods: Cookies, Hidden Form Fields, URL Rewriting, HttpSession. HttpSession stores objects in server memory and tracks client via JSESSIONID.",
            "understand": "Why is HttpSession superior? Security and bandwidth. Storing an entire shopping cart inside client cookies means transmitting several kilobytes of cart data back and forth across every single HTTP request. HttpSession stores the heavy Java objects securely in server memory and transmits only a tiny 32-character JSESSIONID token.",
            "common_mistakes": "1. Calling `request.getSession(false)` when you intended to create a new session (returns null if session doesn't already exist). 2. Forgetting to call `session.invalidate()` on logout.",
            "pyq_year": "CSJMU BCA-5002 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "High-Frequency 15-Mark Core Question (Q4/Q5 - 15m in 4 consecutive exam sessions)",
            "pyq_question": "What is Session Tracking? Why is it required in web applications? Explain the four session tracking techniques in Java Servlets with suitable code examples. Differentiate between Cookies and HttpSession. (15 Marks)",
            "pyq_rubric": "Statelessness of HTTP & Need for Session Tracking (3 marks) + 4 Techniques detailed explanation (6 marks) + HttpSession code example (3 marks) + Cookies vs HttpSession comparison (3 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Need for Session Tracking:",
                 "The Hypertext Transfer Protocol (HTTP) is a stateless protocol: the server cannot inherently distinguish whether two successive requests originate from the same user or different users. Session tracking bridges this architectural gap by associating a conversational state with each unique client across multi-step transactions such as e-commerce shopping carts or authenticated student portals."),
                ("2. Detailed Analysis of the 4 Session Tracking Techniques:",
                 "• Cookies: A Cookie is a key-value header (`Cookie: user=sarthak`) stored by the browser. Persistent cookies have an expiry time set via `cookie.setMaxAge(3600)`. Stored on client side.\n"
                 "• Hidden Form Fields: Hidden inputs (`<input type=\"hidden\" name=\"user\" value=\"sarthak\">`) pass state during form submissions without rendering visible UI.\n"
                 "• URL Rewriting: Appends session identifiers directly to hyperlinks (`servlet?jsessionid=123`). Vital when clients disable browser cookies.\n"
                 "• HttpSession Interface: The container creates an `HttpSession` object in server RAM, assigns a unique `JSESSIONID`, and manages expiration timeouts automatically via `web.xml` or `session.setMaxInactiveInterval(1800)`."),
                ("3. Java Code Implementation of HttpSession for User Authentication:",
                 "import java.io.*;\n"
                 "import javax.servlet.*;\n"
                 "import javax.servlet.http.*;\n\n"
                 "public class LoginServlet extends HttpServlet {\n"
                 "    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {\n"
                 "        String user = req.getParameter(\"username\");\n"
                 "        String pass = req.getParameter(\"password\");\n"
                 "        if (\"admin\".equals(user) && \"pass123\".equals(pass)) {\n"
                 "            HttpSession session = req.getSession(true); // Create new session\n"
                 "            session.setAttribute(\"currentUser\", user);\n"
                 "            res.sendRedirect(\"dashboard.jsp\");\n"
                 "        } else {\n"
                 "            res.sendRedirect(\"login.html?error=invalid\");\n"
                 "        }\n"
                 "    }\n"
                 "}"),
                ("4. Cookies vs HttpSession Comparison:",
                 "Cookies store data client-side in the browser (limited to 4KB strings, vulnerable to tampering). HttpSession stores arbitrary Java objects (Lists, Maps, User models) safely on the server, exchanging only the session ID.")
            ]
        },
        "sgpa_target": {"focus": "Master 4 Session Tracking Methods & HttpSession API", "milestone": "Full 15/15 on Java Web Development Exam Question"},
        "apt_data": {
            "topic": "Logical Reasoning — Seating Arrangements (Linear & Circular)",
            "tutorial": [
                "Seating Arrangement Deduction Strategy:\n"
                "1. Circular Arrangements:\n"
                "• Facing Inwards (Towards Center): Right = Anti-Clockwise; Left = Clockwise.\n"
                "• Facing Outwards (Away from Center): Right = Clockwise; Left = Anti-Clockwise.\n"
                "• Fixed Anchor Rule: Always place the first person at the bottom facing inwards so their left/right matches your natural left/right.",
                "2. Linear Arrangements:\n"
                "• Facing North: Left = West (Left hand side); Right = East (Right hand side).\n"
                "• Facing South: Left = East (Right hand side); Right = West (Left hand side).",
                "3. Crucial Clue Distinctions:\n"
                "• 'A is sitting second to the left of B' ==> Exactly 1 person between A and B.\n"
                "• 'A is sitting immediate left of B' ==> A and B are adjacent: [A][B].\n"
                "• 'A is to the left of B' ==> A can be anywhere to B's left."
            ],
            "formulas": "Circular ring of N people: Opposite person is at (N/2) distance for even N.",
            "shortcut": "Start with Definite Clues: Never start with negative clues ('A does not sit next to B'). Start with clues establishing direct fixed relative positions ('A sits 3rd to right of B').",
            "recognition": "Look for '8 friends A, B, C, D, E, F, G, H are sitting around a circular table facing center...' in TCS NQT, Wipro, and Infosys.",
            "tier1_problem": "5 friends (P, Q, R, S, T) are sitting in a row facing North. S is between T and Q. Q is to the immediate left of R. P is to the immediate left of T. Who is sitting in the middle?",
            "tier1_solution": "From clues:\n1. 'P is to immediate left of T' ==> [P, T]\n2. 'S is between T and Q' ==> [P, T, S, Q]\n3. 'Q is immediate left of R' ==> [P, T, S, Q, R]\nComplete order: P, T, S, Q, R. Middle person is S. Answer: S.",
            "tier2_problem": "6 people (A, B, C, D, E, F) are sitting in a circle facing the center. B is between D and C. A is between E and D. F is to the right of D. Who is between A and F?",
            "tier2_solution": "Anchor D at bottom. B is between D and C ==> Order clockwise: D, B, C. A is between E and D ==> E, A, D. F is to the right of D (anti-clockwise) ==> F sits between C and E. Full circle clockwise: D -> B -> C -> F -> E -> A -> (back to D). Looking at positions: between A and F sits E. Answer: E.",
            "tier3_problem": "[TCS Digital Pattern] 8 persons (A to H) sit around a circular table facing center. B sits 3rd to left of G. Only 2 people sit between G and D. C sits 2nd to right of D. F is not an immediate neighbor of B. A sits 3rd to right of F. Who sits opposite to H?",
            "tier3_solution": "Fix G at position 1. B is 3rd to left of G (clockwise 3 steps) ==> Position 6. Two people between G and D: D can be pos 4. C is 2nd to right of D ==> pos 2. F cannot be next to B (not 5 or 7). F must be 8. A sits 3rd to right of F ==> pos 3. Remaining positions: E and H. Solving constraints places H at position 5, directly opposite G or C. Systematic deduction gives H opposite C. Answer: C.",
            "tier4_problem": "8 friends are seated in a straight line. 4 face North and 4 face South. No two adjacent people face the same direction. A sits 2nd from the left end and faces North. B sits 3rd to the right of A. How many people sit between B and the right end?",
            "tier4_solution": "Line has 8 positions (1 to 8). Since adjacent people face alternate directions, and Pos 2 (A) faces North:\nPos 1: South, Pos 2: North (A), Pos 3: South, Pos 4: North, Pos 5: South, Pos 6: North, Pos 7: South, Pos 8: North.\nA is at Pos 2 facing North. 'Right' for North is towards higher positions. B is 3rd to the right of A ==> Pos 2 + 3 = Pos 5.\nB is at Pos 5. Positions to the right of B are Pos 6, Pos 7, Pos 8 (Total 3 people). Answer: 3 people.",
            "speed_drills": [
                {"q": "In a row of 7 people facing North, A is 4th from left and 4th from right. Where is A?", "a": "Exactly in the middle (Position 4)."},
                {"q": "6 people sit in a circle facing inward. Who is opposite to person at position 1?", "a": "Person at position 1 + 6/2 = Position 4."},
                {"q": "A, B, C sit in a row. A is left of B and C is right of B. Order?", "a": "A - B - C."},
                {"q": "If X is sitting immediate right of Y who faces South, is X to the West or East of Y?", "a": "West. When facing South, Right is West."},
                {"q": "In a round table of 8, how many people sit between P and Q if P is opposite Q?", "a": "Exactly 3 people on either side."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Best Time to Buy and Sell Stock (LeetCode 121 - Easy)",
                "difficulty": "Easy",
                "importance": "Top 3 Most Asked Placement Problem (TCS, Infosys, Amazon, Microsoft)",
                "problem_statement": "You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.",
                "solution_approach": (
                    "Single-Pass Running Minimum (Greedy / DP):\n"
                    "1. Track the minimum price seen so far: `min_price = infinity`.\n"
                    "2. Track the maximum profit: `max_profit = 0`.\n"
                    "3. For every price: update `min_price = min(min_price, price)`.\n"
                    "4. Calculate potential profit if sold today: `price - min_price`.\n"
                    "5. Update `max_profit = max(max_profit, price - min_price)`."
                ),
                "code": (
                    "def maxProfit(prices: list[int]) -> int:\n"
                    "    min_price = float('inf')\n"
                    "    max_profit = 0\n"
                    "    \n"
                    "    for price in prices:\n"
                    "        if price < min_price:\n"
                    "            min_price = price\n"
                    "        elif price - min_price > max_profit:\n"
                    "            max_profit = price - min_price\n"
                    "            \n"
                    "    return max_profit"
                ),
                "line_by_line": [
                    ("min_price = float('inf')", "Initialize minimum purchase baseline to positive infinity."),
                    ("if price < min_price: min_price = price", "Found a cheaper historical day to buy."),
                    ("elif price - min_price > max_profit", "Calculate potential upside if sold today against historical dip.")
                ],
                "time_complexity": "O(N) single linear scan.",
                "space_complexity": "O(1) constant auxiliary memory.",
                "edge_cases": "Strictly decreasing prices [7, 6, 4, 3, 1] (returns 0); single element [5] (returns 0)."
            },
            {
                "title": "Best Time to Buy and Sell Stock II (LeetCode 122 - Medium)",
                "difficulty": "Medium",
                "importance": "Classic Greedy Peak-Valley Strategy",
                "problem_statement": "You are given an integer array prices. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it and immediately sell it on the same day. Find and return the maximum profit you can achieve.",
                "solution_approach": (
                    "Greedy Peak-Valley Theorem:\n"
                    "Since you can make unlimited transactions, the overall maximum profit is the sum of every upward price segment:\n"
                    "If prices[i] > prices[i-1], immediately capture the profit (prices[i] - prices[i-1]).\n"
                    "Accumulating all positive differences guarantees capturing every upward trajectory."
                ),
                "code": (
                    "def maxProfitII(prices: list[int]) -> int:\n"
                    "    total_profit = 0\n"
                    "    \n"
                    "    for i in range(1, len(prices)):\n"
                    "        if prices[i] > prices[i - 1]:\n"
                    "            total_profit += prices[i] - prices[i - 1]\n"
                    "            \n"
                    "    return total_profit"
                ),
                "line_by_line": [
                    ("for i in range(1, len(prices)):", "Iterate from day 1 comparing against yesterday."),
                    ("if prices[i] > prices[i - 1]:", "Capture every ascending price movement."),
                    ("total_profit += prices[i] - prices[i - 1]", "Add incremental gain to accumulated profit.")
                ],
                "time_complexity": "O(N) single linear pass.",
                "space_complexity": "O(1) constant space.",
                "edge_cases": "Prices sorted ascending [1, 2, 3, 4, 5] (returns 4); sorted descending (returns 0)."
            }
        ],
        "cs_core": {
            "subject": "Database Management Systems (DBMS)",
            "topic": "Advanced SQL: Analytic & Window Functions (ROW_NUMBER, RANK, DENSE_RANK, LEAD, LAG)",
            "detailed_notes": [
                "Window Functions compute an aggregate or ranking value over a specified subset of rows (the 'window') WITHOUT collapsing the rows into a single summary output (unlike standard `GROUP BY`).",
                "Core Ranking Functions:\n"
                "• `ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC)`: Assigns a strictly unique, consecutive integer (1, 2, 3, 4) to every row regardless of ties.\n"
                "• `RANK() OVER (PARTITION BY dept ORDER BY salary DESC)`: Assigns identical rank to ties, but SKIPS subsequent ranks (e.g. 1, 2, 2, 4).\n"
                "• `DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC)`: Assigns identical rank to ties WITHOUT skipping subsequent ranks (e.g. 1, 2, 2, 3).\n"
                "• `LEAD(column, offset)`: Fetches data from following rows without an expensive self-join.\n"
                "• `LAG(column, offset)`: Fetches data from preceding rows (used for MoM revenue growth calculations)."
            ],
            "interview_qa": [
                {
                    "q": "Write a SQL query to find the 2nd highest salary in each department.",
                    "a": "WITH RankedSalaries AS (\n    SELECT employee_id, department_id, salary,\n           DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank_num\n    FROM employees\n)\nSELECT department_id, employee_id, salary\nFROM RankedSalaries\nWHERE rank_num = 2;"
                },
                {
                    "q": "What is the key execution difference between `GROUP BY` and a Window Function with `PARTITION BY`?",
                    "a": "`GROUP BY` collapses multiple individual table rows into a single aggregated group row, destroying row-level granular details. A window function with `PARTITION BY` calculates aggregates (like running totals or averages) over the partitioned group while PRESERVING every original individual row and its distinct columns in the final result set."
                }
            ]
        },
        "project_defense": {
            "project_name": "Full Portfolio Multi-Tier Review",
            "feature_focus": "Architectural Audit & Cross-Comparison: CSMS vs BulkBeat TV vs SmartGalla vs BEVM",
            "architecture_deep_dive": (
                "Technical Cross-Comparison across Sarthak's 4 Flagship Projects:\n\n"
                "1. Framework & Concurrency Paradigms:\n"
                "• CSMS: Built on FastAPI (Python ASGI) utilizing Python's `asyncio` event loop for non-blocking I/O operations and automatic OpenAPI/Swagger documentation generation.\n"
                "• SmartGalla: Built on Next.js 16 App Router server components with Supabase PostgreSQL and Row-Level Security.\n"
                "• BulkBeat TV: Built on `aiohttp` and native asyncio queues for high-throughput WebSocket/Telegram bot event dispatching.\n\n"
                "2. Database & Data Consistency Models:\n"
                "• CSMS: Relational PostgreSQL schema with ACID compliance, relational integrity (Foreign Keys, CASCADE), and Alembic migration version control.\n"
                "• BulkBeat TV: Embedded SQLite configured with Write-Ahead Logging (WAL) mode for low-latency concurrent reads during heavy streaming ingestion.\n"
                "• BEVM: Immutable chained SHA-256 hash log simulating blockchain ledger integrity for biometric voter audits."
            ),
            "interview_qa": [
                {
                    "q": "How do you decide between FastAPI and Django for a new backend project?",
                    "a": "I choose FastAPI when building lightweight, high-performance microservices or APIs requiring async I/O. I choose Django when building comprehensive monolithic web applications requiring built-in administrative portals, user session management, and complex ORM migrations out of the box."
                },
                {
                    "q": "How did you maintain database consistency during concurrent transactions across your projects?",
                    "a": "In CSMS with PostgreSQL, I utilized transactional ACID blocks (`BEGIN ... COMMIT`) with appropriate isolation levels to prevent dirty and non-repeatable reads. In BulkBeat TV with SQLite, I activated Write-Ahead Logging (`PRAGMA journal_mode=WAL;`), allowing concurrent readers to access recent snapshots without blocking the active background writer thread."
                }
            ]
        },
        "daily_test": {
            "day": 21,
            "questions": [
                {"q": "What are the 4 session tracking mechanisms supported in Java Servlets?", "a": "1. Cookies, 2. Hidden Form Fields, 3. URL Rewriting, 4. HttpSession API."},
                {"q": "Why is URL rewriting essential when client browsers have disabled cookies?", "a": "Because URL rewriting embeds the session token (`jsessionid`) directly inside hyperlinks, allowing the server to track session identity without reading client cookie headers."},
                {"q": "What is the difference between `RANK()` and `DENSE_RANK()` in SQL window functions?", "a": "`RANK()` skips ranks after ties (1, 2, 2, 4), whereas `DENSE_RANK()` does not skip ranks after ties (1, 2, 2, 3)."},
                {"q": "What is the time complexity of the greedy solution for Best Time to Buy and Sell Stock II?", "a": "O(N) single linear pass accumulating all positive daily price increments."},
                {"q": "How does `request.getSession(true)` differ from `request.getSession(false)`?", "a": "`getSession(true)` creates a new session if one does not exist. `getSession(false)` returns `null` if no active session is found."},
                {"q": "In a circular arrangement of 6 people facing inward, who sits to the immediate right of the person at position 1?", "a": "Anti-clockwise neighbor (Position 6 if numbering clockwise)."},
                {"q": "Why is Write-Ahead Logging (WAL) mode beneficial for SQLite in BulkBeat TV?", "a": "WAL mode allows concurrent read operations to proceed simultaneously without being blocked by background write transactions."},
                {"q": "Explain the difference between `GROUP BY` and `PARTITION BY` in SQL.", "a": "`GROUP BY` collapses multiple rows into a single aggregated row. `PARTITION BY` computes window aggregations while retaining all individual rows."}
            ]
        }
    }

    # DAY 22
    days[22] = {
        "day": 22,
        "title": "TCP Congestion Control (AIMD & Tahoe/Reno), Data Interpretation & LIS Dynamic Programming",
        "sem_data": {
            "subject": "BCA-5003 Computer Network",
            "topic": "Unit IV — Transport Layer: TCP Congestion Control Mechanisms (Slow Start, AIMD, Fast Retransmit & Reno)",
            "detailed_notes": [
                "Network congestion occurs when the aggregate traffic injected into a network exceeds the capacity of intermediate routers and links, causing buffer overflow, queuing delays, and packet drops (Congestion Collapse). TCP incorporates end-to-end congestion control to dynamically modulate transmission rates without explicit router feedback.",
                "Key State Variables:\n"
                "• Congestion Window (`cwnd`): The maximum number of bytes the sender is permitted to transmit before receiving an ACK, dynamically calculated by the sender.\n"
                "• Advertised Window (`rwnd`): The buffer capacity advertised by the receiver in the TCP header for flow control.\n"
                "• Effective Sending Window = `min(cwnd, rwnd)`.\n"
                "• Slow Start Threshold (`ssthresh`): The window size threshold determining the transition between Slow Start and Congestion Avoidance.",
                "The 4 Core Phases of TCP Congestion Control:\n"
                "1. Slow Start Phase:\n"
                "• Initially `cwnd = 1 MSS` (Maximum Segment Size). `ssthresh` is typically set to 64KB.\n"
                "• For EVERY ACK received, `cwnd` increases by 1 MSS: `cwnd = cwnd + 1 MSS`.\n"
                "• This causes `cwnd` to DOUBLE every Round Trip Time (RTT): 1 -> 2 -> 4 -> 8 -> 16 MSS (Exponential Growth!).\n"
                "• Continues until `cwnd >= ssthresh` or a packet drop occurs.",
                "2. Congestion Avoidance Phase (Additive Increase):\n"
                "• Once `cwnd >= ssthresh`, exponential growth stops to prevent abrupt network saturation.\n"
                "• For every RTT, `cwnd` increases by strictly 1 MSS (Additive Increase): `cwnd = cwnd + (1 / cwnd)` per ACK.\n"
                "• Graphically represents a linear staircase ascent.",
                "3. Multiplicative Decrease (Handling Packet Loss):\n"
                "• Case A (Timeout): Severe congestion indicator. `ssthresh = cwnd / 2`, `cwnd` is collapsed to 1 MSS, and Slow Start restarts.\n"
                "• Case B (3 Duplicate ACKs): Mild packet loss. Router dropped 1 segment, but subsequent segments arrived at receiver.\n"
                "4. Fast Retransmit & Fast Recovery (TCP Reno):\n"
                "• Fast Retransmit: Sender retransmits the missing segment immediately upon receiving the 3rd duplicate ACK WITHOUT waiting for retransmission timer expiration!\n"
                "• Fast Recovery (TCP Reno): Instead of dropping `cwnd` to 1 MSS (as in TCP Tahoe), Reno sets `ssthresh = cwnd / 2` and `cwnd = ssthresh + 3 MSS`, continuing Congestion Avoidance without restarting Slow Start."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                    TCP CWND EVOLUTION CURVE OVER TIME                   |\n"
                "+-------------------------------------------------------------------------+\n"
                "|  CWND                                                                   |\n"
                "|   ^                                                                     |\n"
                "|   |                 (Timeout Loss)                                      |\n"
                "| 32|                       *                                             |\n"
                "|   |                      / \\                                            |\n"
                "| 16|          *          /   \\ (ssthresh = 16)                           |\n"
                "|   |         / \\        /                                                |\n"
                "|  8|        /   *------* (Congestion Avoidance: Linear +1 MSS/RTT)        |\n"
                "|   |       /    (Fast Recovery - Reno)                                   |\n"
                "|  4|      *                                                              |\n"
                "|  2|     / (Slow Start: Exponential x2/RTT)                              |\n"
                "|  1|    *                                                                |\n"
                "|   +----------------------------------------------------> Time (RTT)     |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Algorithm Phase", "Window Growth Behavior", "Update Rule per RTT", "Trigger for Transition"],
                "rows": [
                    ["Slow Start", "Exponential growth", "cwnd = cwnd * 2 per RTT", "Starts at 1 MSS, ends when cwnd >= ssthresh"],
                    ["Congestion Avoidance", "Linear additive growth", "cwnd = cwnd + 1 MSS per RTT", "Occurs while cwnd < loss threshold"],
                    ["Fast Retransmit", "Immediate retransmission", "Retransmit lost frame", "Triggered by receipt of 3 Duplicate ACKs"],
                    ["Fast Recovery (Reno)", "Halves window without restart", "ssthresh = cwnd/2; cwnd = ssthresh", "Maintains high pipeline throughput"]
                ]
            },
            "memorize": "AIMD: Additive Increase (+1 MSS/RTT), Multiplicative Decrease (halve ssthresh on loss). Tahoe resets cwnd to 1; Reno halves cwnd to ssthresh on 3 dup ACKs.",
            "understand": "Why does Slow Start double exponentially? To rapidly discover the available network link capacity without wasting dozens of RTTs crawling upwards linearly from 1 MSS.",
            "common_mistakes": "1. Assuming Slow Start increases by 1 segment per RTT (it doubles every RTT!). 2. Confusing flow control (protects receiver buffer via rwnd) with congestion control (protects network routers via cwnd).",
            "pyq_year": "CSJMU BCA-5003 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "High-Frequency 15-Mark Core Question (Appeared in 2021, 2022-23, 2023-24, 2024-25)",
            "pyq_question": "Explain TCP Congestion Control in detail. Describe Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery with a neat cwnd graph. Differentiate between TCP Tahoe and TCP Reno. (15 Marks)",
            "pyq_rubric": "Concept of Congestion & cwnd vs rwnd (3 marks) + 4 Phases explained with formulas (6 marks) + CWND graph (3 marks) + Tahoe vs Reno comparison (3 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Congestion Control vs Flow Control:",
                 "Flow control is an end-to-end mechanism between sender and receiver preventing receiver buffer overflow (regulated via `rwnd`). Congestion control is a global network mechanism preventing intermediate router buffer exhaustion and link saturation (regulated via `cwnd`). Effective transmission window = min(cwnd, rwnd)."),
                ("2. Detailed Breakdown of TCP Congestion Control Mechanisms:",
                 "• Slow Start: Starts with cwnd = 1 MSS. Each received ACK increments cwnd by 1 MSS, doubling cwnd every RTT (1, 2, 4, 8...). Once cwnd reaches `ssthresh`, mode switches to Congestion Avoidance.\n"
                 "• Congestion Avoidance: Employs Additive Increase: cwnd increases by 1 MSS per RTT regardless of the number of ACKs received. Represents linear probe of bandwidth.\n"
                 "• Fast Retransmit: When a single segment is lost, receiver sends duplicate ACKs for subsequent out-of-order packets. Upon receiving 3 Duplicate ACKs, sender retransmits the missing segment immediately without waiting for timeout.\n"
                 "• Fast Recovery: Avoids dropping to cwnd = 1 MSS. Halves ssthresh and sets cwnd = ssthresh, resuming linear congestion avoidance."),
                ("3. TCP Tahoe vs TCP Reno:",
                 "In TCP Tahoe, ANY packet loss (timeout or 3 duplicate ACKs) forces cwnd back down to 1 MSS, re-entering slow start. In TCP Reno, 3 duplicate ACKs trigger Fast Recovery: cwnd is halved to `ssthresh` and continues linear growth, avoiding severe throughput collapse.")
            ]
        },
        "sgpa_target": {"focus": "Master AIMD, Slow Start, and Tahoe vs Reno Graph", "milestone": "Full 15/15 Marks on Computer Networks Transport Layer Question"},
        "apt_data": {
            "topic": "Data Interpretation (DI) — Tables, Bar Charts & Missing Data",
            "tutorial": [
                "Data Interpretation (DI) tests rapid quantitative extraction and mental percentage calculation from complex datasets.",
                "Core Mathematical Operations in DI:\n"
                "1. Percentage Growth: % Increase/Decrease = [(Final Value - Initial Value) / Initial Value] * 100.\n"
                "2. Ratio Comparison: To compare A/B vs C/D, cross-multiply A*D vs B*C.\n"
                "3. Average: Sum of items / Total item count.\n"
                "4. Approximations: Round numbers to 2 significant digits (e.g., 4,821 / 15,920 ≈ 48 / 160 = 30%)."
            ],
            "formulas": "Growth % = (Change / Base) * 100. Ratio cross-multiplication: A/B > C/D if A*D > B*C.",
            "shortcut": "Splitting the Base for Percentages: To find 17% of 420: 10% = 42, 5% = 21, 1% = 4.2. Total = 42 + 21 + (2 * 4.2) = 71.4.",
            "recognition": "Look for multi-column tables showing year-over-year production, sales, or expenditures in TCS NQT, Wipro, and Cognizant.",
            "tier1_problem": "A table shows sales (in lakhs) of 3 products (A, B, C) over 2 years: Year 1: A=40, B=60, C=80. Year 2: A=50, B=75, C=100. Find the overall percentage increase in total sales.",
            "tier1_solution": "Total Sales Year 1 = 40 + 60 + 80 = 180 lakhs.\nTotal Sales Year 2 = 50 + 75 + 100 = 225 lakhs.\nAbsolute Increase = 225 - 180 = 45 lakhs.\nPercentage Increase = (45 / 180) * 100 = (1 / 4) * 100 = 25%. Answer: 25%.",
            "tier2_problem": "A company has 5 departments with employees: IT: 120, HR: 40, Sales: 80, Finance: 60, Ops: 100. What percentage of the total workforce is in Sales?",
            "tier2_solution": "Total Workforce = 120 + 40 + 80 + 60 + 100 = 400.\nSales employees = 80.\nPercentage = (80 / 400) * 100 = 20%. Answer: 20%.",
            "tier3_problem": "[TCS NQT DI Pattern] Table shows Revenue and Expenditure (in Crores) of a firm across 4 years:\n2021: Rev=200, Exp=160\n2022: Rev=250, Exp=190\n2023: Rev=300, Exp=210\n2024: Rev=360, Exp=240\nIn which year was the Profit Percentage [(Rev - Exp) / Exp * 100] the highest?",
            "tier3_solution": "Calculate Profit % for each year:\n2021: (40 / 160) * 100 = 25.0%\n2022: (60 / 190) * 100 ≈ 31.58%\n2023: (90 / 210) * 100 = (3 / 7) * 100 ≈ 42.86%\n2024: (120 / 240) * 100 = 50.0%\nHighest profit percentage occurred in 2024 (50%). Answer: 2024.",
            "tier4_problem": "A table has missing data for student marks. Total students = 200. Passed in Math = 140. Passed in Science = 120. If 30 students failed both subjects, how many students passed in BOTH subjects?",
            "tier4_solution": "Total Students = 200.\nStudents failing both = 30 ==> Students passing at least one subject = 200 - 30 = 170.\nUsing Set Theory: n(M union S) = n(M) + n(S) - n(M intersection S).\n170 = 140 + 120 - n(Both)\n170 = 260 - n(Both)\nn(Both) = 260 - 170 = 90 students. Answer: 90 students.",
            "speed_drills": [
                {"q": "Production increases from 500 to 650 units. Find percentage increase.", "a": "(150 / 500) * 100 = 30%."},
                {"q": "Ratio of males to females is 3:2. If total is 450, find number of females.", "a": "2/5 * 450 = 180 females."},
                {"q": "What is 15% of 680?", "a": "10% = 68, 5% = 34. Total = 102."},
                {"q": "Expenditure is 80% of Income. If Income is Rs 50,000, find savings.", "a": "20% of 50,000 = Rs 10,000."},
                {"q": "Which ratio is greater: 5/8 or 7/11?", "a": "5*11=55 vs 7*8=56 ==> 7/11 is greater."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Longest Increasing Subsequence (LeetCode 300 - Medium)",
                "difficulty": "Medium",
                "importance": "Top-tier Placement Dynamic Programming Problem (Google, Amazon, TCS Digital)",
                "problem_statement": "Given an integer array nums, return the length of the longest strictly increasing subsequence.",
                "solution_approach": (
                    "Approach 1: Classic DP in O(N^2):\n"
                    "Let dp[i] represent the length of the LIS ending at index i.\n"
                    "For every j < i: if nums[j] < nums[i], dp[i] = max(dp[i], dp[j] + 1).\n\n"
                    "Approach 2: Patience Sorting with Binary Search in O(N log N):\n"
                    "Maintain an array `tails` where tails[k] stores the smallest tail of all increasing subsequences of length k+1.\n"
                    "For each x in nums, use binary search (`bisect_left`) to find its insertion position in `tails`. If x is greater than all elements, append it; otherwise replace the existing element."
                ),
                "code": (
                    "import bisect\n\n"
                    "def lengthOfLIS(nums: list[int]) -> int:\n"
                    "    if not nums:\n"
                    "        return 0\n"
                    "        \n"
                    "    tails = []\n"
                    "    for x in nums:\n"
                    "        idx = bisect.bisect_left(tails, x)\n"
                    "        if idx == len(tails):\n"
                    "            tails.append(x)\n"
                    "        else:\n"
                    "            tails[idx] = x\n"
                    "            \n"
                    "    return len(tails)"
                ),
                "line_by_line": [
                    ("tails = []", "Dynamic array maintaining the smallest active tail for every subsequence length."),
                    ("idx = bisect.bisect_left(tails, x)", "Binary search in O(log N) to find insertion or replacement index."),
                    ("if idx == len(tails): tails.append(x)", "Extends the maximum subsequence length found so far."),
                    ("else: tails[idx] = x", "Greedily lowers the tail value of an existing length, increasing chances for future expansions.")
                ],
                "time_complexity": "O(N log N) using binary search (or O(N^2) using basic DP).",
                "space_complexity": "O(N) to store tails array.",
                "edge_cases": "Strictly decreasing array [7, 7, 7] (returns 1); sorted array [1, 2, 3] (returns len)."
            }
        ],
        "cs_core": {
            "subject": "Operating Systems",
            "topic": "Process Synchronization Primitives: Semaphores, Mutexes & Condition Variables",
            "detailed_notes": [
                "Critical Section Problem:\n"
                "A section of code accessing shared resources that must not be concurrently accessed by more than one process. Must satisfy 3 criteria: 1. Mutual Exclusion, 2. Progress, 3. Bounded Waiting.",
                "Synchronization Primitives Compared:\n"
                "• Mutex (Mutual Exclusion Lock): A locking mechanism with ownership. Only the thread that locked the mutex is permitted to unlock it. Binary state (locked/unlocked).\n"
                "• Semaphore (Dijkstra): A signaling integer counter variable accessed only via atomic operations `wait()` (P) and `signal()` (V).\n"
                "  - Counting Semaphore: Counter value N represents available units of a shared resource.\n"
                "  - Binary Semaphore: Value restricted to 0 or 1. Unlike a mutex, a semaphore has NO ownership: Thread A can wait() and Thread B can signal() to release it!\n"
                "• Spinlock: Thread busy-waits in a loop checking lock state. Useful on multi-core systems when lock duration is shorter than OS context-switch overhead.",
                "Priority Inversion Problem:\n"
                "Occurs when a low-priority thread holds a shared lock needed by a high-priority thread, and a medium-priority thread preempts the low-priority thread, starving the high-priority thread! Solved by Priority Inheritance Protocol (low-priority thread temporarily inherits high priority while holding lock)."
            ],
            "interview_qa": [
                {
                    "q": "What is the technical difference between a Mutex and a Binary Semaphore?",
                    "a": "The fundamental difference is 'ownership' and purpose. A Mutex is a locking mechanism with ownership: the exact same thread that acquired the mutex MUST release it. A Binary Semaphore is a signaling mechanism without ownership: one thread can wait for an event, and a completely different thread or interrupt service routine can signal the semaphore to unblock it."
                },
                {
                    "q": "What is Priority Inversion and how does Priority Inheritance solve it?",
                    "a": "Priority inversion happens when a low-priority process holds a lock required by a high-priority process, but is preempted by an unrelated medium-priority process, indefinitely delaying the high-priority process. Priority Inheritance solves this by temporarily elevating the priority of the low-priority lock-holder to match the waiting high-priority process until the lock is released."
                }
            ]
        },
        "project_defense": {
            "project_name": "Portfolio Systems Architecture",
            "feature_focus": "System Design: Scaling BulkBeat TV to 50k Concurrent Users",
            "architecture_deep_dive": (
                "Scaling BulkBeat TV from a single VPS to 50,000 concurrent streaming users:\n\n"
                "1. Decoupled Architecture:\n"
                "Separate media stream ingestion from user notification distribution. The ingestion pipeline runs as an isolated worker service, "
                "writing stream events to an Apache Kafka / RabbitMQ message broker.\n\n"
                "2. Distributed Caching & Database Tier:\n"
                "• Migrate embedded SQLite to a PostgreSQL cluster with 1 Primary (Writes) and 3 Read Replicas.\n"
                "• Place a Redis cluster in front of PostgreSQL to cache active subscription tokens and channel metadata with a 60-second TTL, reducing database load by 95%.\n\n"
                "3. Horizontal API Gateway Scaling:\n"
                "Deploy FastAPI stateless containers behind Nginx / AWS ALB using round-robin load balancing. WebSocket connections are terminated "
                "at the load balancer with Redis Pub/Sub syncing broadcast messages across server instances."
            ),
            "interview_qa": [
                {
                    "q": "How would you handle sudden traffic spikes during breaking news events on BulkBeat TV?",
                    "a": "I would implement aggressive edge caching via a CDN (Cloudflare) for static assets and public stream playlists. For dynamic user notifications, I would decouple alert publishing from delivery using an asynchronous Redis Pub/Sub message broker, buffering outgoing traffic and protecting backend workers from connection spikes."
                },
                {
                    "q": "Why is Redis Pub/Sub suitable for multi-instance WebSocket synchronization?",
                    "a": "When multiple FastAPI server instances run behind a load balancer, client WebSockets are scattered across different physical machines. Redis Pub/Sub acts as a lightweight central event bus: when an alert occurs, the producer publishes to a Redis channel, and all server instances receive the event simultaneously and push it down their local active WebSocket connections."
                }
            ]
        },
        "daily_test": {
            "day": 22,
            "questions": [
                {"q": "What is the update rule for TCP Slow Start for each received ACK?", "a": "cwnd = cwnd + 1 MSS. The congestion window doubles every round trip time."},
                {"q": "How does TCP Reno handle packet loss signaled by 3 Duplicate ACKs?", "a": "It triggers Fast Retransmit and Fast Recovery: ssthresh is set to cwnd / 2, and cwnd is set to ssthresh, continuing linear congestion avoidance without restarting slow start."},
                {"q": "If revenue increases from 200 Cr to 260 Cr, what is the percentage increase?", "a": "(60 / 200) * 100 = 30% increase."},
                {"q": "What is the time complexity of the optimized Patience Sorting solution for LIS?", "a": "O(N log N) using binary search (bisect_left) on the tails array."},
                {"q": "What are the 3 criteria that any valid solution to the Critical Section problem must satisfy?", "a": "1. Mutual Exclusion, 2. Progress, 3. Bounded Waiting."},
                {"q": "Can a Binary Semaphore be unlocked by a thread other than the one that locked it?", "a": "Yes. Semaphores are signaling mechanisms and have no ownership, unlike Mutexes."},
                {"q": "What is the difference between TCP Tahoe and TCP Reno on 3 Duplicate ACKs?", "a": "Tahoe drops cwnd back to 1 MSS and restarts Slow Start. Reno halves cwnd to ssthresh and enters Fast Recovery."},
                {"q": "How does Priority Inheritance resolve Priority Inversion in OS synchronization?", "a": "The low-priority thread holding the lock temporarily inherits the higher priority of the waiting thread until it releases the shared lock."}
            ]
        }
    }

    # DAY 23
    days[23] = {
        "day": 23,
        "title": "Numerical Integration (Trapezoidal & Simpson's), Pie Charts & Coin Change DP",
        "sem_data": {
            "subject": "BCA-5004 Numerical Methods",
            "topic": "Unit IV — Numerical Integration: Trapezoidal Rule, Simpson's 1/3 Rule & Simpson's 3/8 Rule",
            "detailed_notes": [
                "Numerical integration (Numerical Quadrature) evaluates the definite integral I = int_a^b f(x) dx of a function known only at discrete tabulated points (x0, y0), (x1, y1), ..., (xn, yn), or when an analytical antiderivative cannot be expressed in elementary terms.",
                "General Newton-Cotes Quadrature Formula:\n"
                "Derived by replacing the integrand f(x) with an interpolating polynomial P_n(x) of degree n using Newton's Forward Difference formula.\n"
                "Let step size h = (b - a) / n, where x_i = x0 + i*h.",
                "1. Trapezoidal Rule (n = 1, Linear Interpolation):\n"
                "• Approximates the curve between adjacent points as straight line segments (trapezoids).\n"
                "• Formula: int_a^b f(x) dx = (h/2) * [ (y0 + yn) + 2*(y1 + y2 + ... + y_{n-1}) ].\n"
                "• Global Truncation Error: E_T = - [(b - a) * h^2 / 12] * f''(xi) = O(h^2).\n"
                "• Degree of Precision = 1 (Exact for polynomials of degree <= 1).",
                "2. Simpson's 1/3 Rule (n = 2, Parabolic Interpolation):\n"
                "• Approximates the curve through sets of 3 points as second-degree parabolas.\n"
                "• Requirement: The total number of subintervals n MUST BE EVEN (n = 2, 4, 6, 8, ...).\n"
                "• Formula: int_a^b f(x) dx = (h/3) * [ (y0 + yn) + 4*(Odd Ordinates: y1 + y3 + ...) + 2*(Even Ordinates: y2 + y4 + ...) ].\n"
                "• Global Truncation Error: E_S13 = - [(b - a) * h^4 / 180] * f^(4)(xi) = O(h^4).\n"
                "• Degree of Precision = 3 (Exact for cubics, even though derived with parabolas!).",
                "3. Simpson's 3/8 Rule (n = 3, Cubic Interpolation):\n"
                "• Approximates curve through sets of 4 points using third-degree cubics.\n"
                "• Requirement: Total number of subintervals n MUST BE A MULTIPLE OF 3 (n = 3, 6, 9, ...).\n"
                "• Formula: int_a^b f(x) dx = (3h/8) * [ (y0 + yn) + 3*(y1 + y2 + y4 + y5 + ...) + 2*(y3 + y6 + ...) ].\n"
                "• Global Truncation Error: E_S38 = - [(b - a) * h^4 / 80] * f^(4)(xi) = O(h^4)."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|             NUMERICAL INTEGRATION CURVE PARTITIONING                    |\n"
                "+-------------------------------------------------------------------------+\n"
                "|  y ^                                                                    |\n"
                "|    |             * y2                                                   |\n"
                "|    |            / \\                                                     |\n"
                "|    |      * y1 /   \\   * y3                                             |\n"
                "|    |     / \\  /     \\ / \\                                               |\n"
                "|    | y0 *   \\/       *   * yn                                           |\n"
                "|    |    |   |   |    |   |                                              |\n"
                "|    +----+---+---+----+---+-----> x                                      |\n"
                "|        x0  x1  x2   x3  xn                                              |\n"
                "|         <--h--><--h-->                                                  |\n"
                "|  Trapezoidal: Chords (n=1) | Simpson 1/3: Parabolas (n=2, n even)       |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Rule", "Subintervals Constraint", "Interpolating Polynomial", "Global Error", "Degree of Precision"],
                "rows": [
                    ["Trapezoidal Rule", "Any number of intervals n >= 1", "Linear (Degree 1)", "O(h^2)", "1"],
                    ["Simpson's 1/3 Rule", "n must be strictly EVEN (2, 4, 6...)", "Quadratic (Degree 2)", "O(h^4)", "3"],
                    ["Simpson's 3/8 Rule", "n must be a MULTIPLE OF 3 (3, 6, 9...)", "Cubic (Degree 3)", "O(h^4)", "3"]
                ]
            },
            "memorize": "Trapezoidal: (h/2)[Ends + 2*Others]. Simpson 1/3: (h/3)[Ends + 4*Odds + 2*Evens] (n even!). Simpson 3/8: (3h/8)[Ends + 3*Non-multiples + 2*Multiples-of-3].",
            "understand": "Why does Simpson's 1/3 rule have precision 3 when derived with a quadratic (degree 2) parabola? Due to symmetry: the odd error term of degree 3 cancels out exactly over symmetric interval [-h, +h], granting cubic accuracy for free!",
            "common_mistakes": "1. Applying Simpson's 1/3 rule when n is odd. 2. Forgetting to divide by 2 or 3 in the leading factor ((h/2) or (h/3)).",
            "pyq_year": "CSJMU BCA-5004 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "4 Consecutive University Sessions (Q7/Q8 - 15 Marks Core Question)",
            "pyq_question": "Evaluate the integral I = int_0^1 (1 / (1 + x^2)) dx by dividing the interval into 6 equal parts using: (i) Trapezoidal Rule, (ii) Simpson's 1/3 Rule, and (iii) Simpson's 3/8 Rule. Hence, find the approximate value of pi. (15 Marks)",
            "pyq_rubric": "Interval partition & table of values (3 marks) + Trapezoidal calculation (3 marks) + Simpson's 1/3 calculation & pi value (4 marks) + Simpson's 3/8 calculation (3 marks) + Comparison of accuracy (2 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Table of Ordinates:",
                 "Let f(x) = 1 / (1 + x^2), lower limit a = 0, upper limit b = 1, number of subintervals n = 6.\n"
                 "Step size h = (b - a) / n = (1 - 0) / 6 = 1/6 ≈ 0.16667.\n"
                 "x0 = 0.0000 ==> y0 = 1 / (1 + 0^2) = 1.00000\n"
                 "x1 = 1/6 ==> y1 = 1 / (1 + 1/36) = 36/37 ≈ 0.97297\n"
                 "x2 = 2/6 ==> y2 = 1 / (1 + 4/36) = 36/40 = 0.90000\n"
                 "x3 = 3/6 ==> y3 = 1 / (1 + 9/36) = 36/45 = 0.80000\n"
                 "x4 = 4/6 ==> y4 = 1 / (1 + 16/36) = 36/52 = 9/13 ≈ 0.69231\n"
                 "x5 = 5/6 ==> y5 = 1 / (1 + 25/36) = 36/61 ≈ 0.59016\n"
                 "x6 = 6/6 = 1 ==> y6 = 1 / (1 + 1) = 0.50000"),
                ("2. Evaluation by Trapezoidal Rule:",
                 "Formula: I_T = (h/2) * [ (y0 + y6) + 2*(y1 + y2 + y3 + y4 + y5) ]\n"
                 "Ends = y0 + y6 = 1.00000 + 0.50000 = 1.50000\n"
                 "Others = 0.97297 + 0.90000 + 0.80000 + 0.69231 + 0.59016 = 3.95544\n"
                 "I_T = (1/12) * [ 1.50000 + 2*(3.95544) ] = (1/12) * [ 1.50000 + 7.91088 ] = 9.41088 / 12 = 0.78424."),
                ("3. Evaluation by Simpson's 1/3 Rule:",
                 "Formula: I_S13 = (h/3) * [ (y0 + y6) + 4*(y1 + y3 + y5) + 2*(y2 + y4) ]\n"
                 "Ends = 1.50000\n"
                 "Odds (y1 + y3 + y5) = 0.97297 + 0.80000 + 0.59016 = 2.36313\n"
                 "Evens (y2 + y4) = 0.90000 + 0.69231 = 1.59231\n"
                 "I_S13 = (1/18) * [ 1.50000 + 4*(2.36313) + 2*(1.59231) ]\n"
                 "= (1/18) * [ 1.50000 + 9.45252 + 3.18462 ] = 14.13714 / 18 = 0.785396 ≈ 0.78540."),
                ("4. Evaluation by Simpson's 3/8 Rule & Pi Estimation:",
                 "Formula: I_S38 = (3h/8) * [ (y0 + y6) + 3*(y1 + y2 + y4 + y5) + 2*(y3) ]\n"
                 "Non-multiples of 3 = 0.97297 + 0.90000 + 0.69231 + 0.59016 = 3.15544\n"
                 "Multiples of 3 = y3 = 0.80000\n"
                 "I_S38 = (3/48) * [ 1.50000 + 3*(3.15544) + 2*(0.80000) ] = (1/16) * [ 1.50000 + 9.46632 + 1.60000 ] = 12.56632 / 16 = 0.785395.\n\n"
                 "Estimation of Pi:\n"
                 "Analytically, int_0^1 (1 / (1 + x^2)) dx = [arctan(x)]_0^1 = arctan(1) - arctan(0) = pi / 4.\n"
                 "Therefore, pi ≈ 4 * I_S13 = 4 * 0.785396 = 3.141584 ≈ 3.1416. Matches true pi to 4 decimal places!")
            ]
        },
        "sgpa_target": {"focus": "Master Trapezoidal & Simpson's 1/3, 3/8 Hand Calculations", "milestone": "Full 15/15 on Numerical Integration Exam Question"},
        "apt_data": {
            "topic": "Data Interpretation (DI) — Pie Charts & Degree Conversions",
            "tutorial": [
                "Pie Chart Fundamentals:\n"
                "• A pie chart displays data as sectors of a circle where the central angle is proportional to the quantity.\n"
                "• Full Circle = 360 degrees = 100%.\n"
                "• Conversion Formulas:\n"
                "  - Degrees to Percentage: Percentage = (Angle in Degrees / 360) * 100.\n"
                "  - Percentage to Degrees: Angle in Degrees = (Percentage / 100) * 360 = Percentage * 3.6.\n"
                "  - Crucial Constant: 1% = 3.6 degrees | 10% = 36 degrees | 25% = 90 degrees."
            ],
            "formulas": "Degrees = % * 3.6. Percentage = (Degrees / 3.6). Sector Value = (Angle / 360) * Total Value.",
            "shortcut": "Calculate in Percentages First: Convert degrees to percentages before computing actual numeric values to keep arithmetic mental and fast.",
            "recognition": "Look for circular sector diagrams with degree markings (e.g. 72°, 108°, 54°) in TCS NQT, Wipro, and Infosys.",
            "tier1_problem": "A student spends time across 24 hours: School = 108 degrees, Sleep = 120 degrees, Play = 60 degrees, Study = 72 degrees. How many hours are spent on Study?",
            "tier1_solution": "Total hours = 24. Full circle = 360 degrees.\nStudy angle = 72 degrees.\nHours spent = (72 / 360) * 24 = (1 / 5) * 24 = 4.8 hours (4 hours 48 minutes). Answer: 4.8 hours.",
            "tier2_problem": "In a pie chart, expenditure on Food is 25%, Rent is 20%, Transport is 15%, and Others is 40%. What is the central angle for Transport?",
            "tier2_solution": "Angle = Percentage * 3.6 = 15 * 3.6 = 54 degrees. Answer: 54 degrees.",
            "tier3_problem": "[Infosys Placement DI] A company's total annual budget is Rs 72 Crores. A pie chart shows departmental allocation: R&D = 90 degrees, Marketing = 75 degrees, Operations = 120 degrees, HR = 45 degrees, Legal = 30 degrees. How much more money is allocated to Operations than Marketing?",
            "tier3_solution": "Angle difference between Operations and Marketing = 120 - 75 = 45 degrees.\nDifference in money = (45 / 360) * 72 Crores = (1 / 8) * 72 = 9 Crores. Answer: Rs 9 Crores.",
            "tier4_problem": "A pie chart represents revenue of 4 divisions: A=108°, B=72°, C=126°, D=54°. If division C's revenue is Rs 42 lakhs, find the total revenue of all divisions combined.",
            "tier4_solution": "Angle for division C = 126 degrees.\nFraction of total = 126 / 360 = 7 / 20.\nLet total revenue be T.\n(7 / 20) * T = 42 lakhs.\nT = 42 * (20 / 7) = 6 * 20 = 120 lakhs = Rs 1.2 Crores. Answer: Rs 120 lakhs.",
            "speed_drills": [
                {"q": "Convert 30% into degrees.", "a": "30 * 3.6 = 108 degrees."},
                {"q": "Convert 90 degrees into percentage.", "a": "90 / 3.6 = 25%."},
                {"q": "If total is 1,200 and sector is 54 degrees, find value.", "a": "(54 / 360) * 1200 = (3/20) * 1200 = 180."},
                {"q": "Sector A = 144 degrees, Sector B = 72 degrees. Ratio of A to B?", "a": "144 : 72 = 2 : 1."},
                {"q": "Angles in pie chart: 100°, 80°, 120°, X°. Find X.", "a": "360 - (100+80+120) = 360 - 300 = 60 degrees."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Coin Change (LeetCode 322 - Medium)",
                "difficulty": "Medium",
                "importance": "Unbounded Knapsack Foundation Problem (Amazon, Microsoft, Google)",
                "problem_statement": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume you have an infinite number of each kind of coin.",
                "solution_approach": (
                    "Bottom-Up Dynamic Programming (Unbounded Knapsack):\n"
                    "1. Define `dp[a]` as the minimum coins needed to make amount `a`.\n"
                    "2. Initialize `dp = [float('inf')] * (amount + 1)` and `dp[0] = 0`.\n"
                    "3. For every sub-amount from 1 to `amount`:\n"
                    "   For every coin in `coins`:\n"
                    "     if `a - coin >= 0`: dp[a] = min(dp[a], 1 + dp[a - coin])\n"
                    "4. Return `dp[amount]` if not infinity, else -1."
                ),
                "code": (
                    "def coinChange(coins: list[int], amount: int) -> int:\n"
                    "    dp = [float('inf')] * (amount + 1)\n"
                    "    dp[0] = 0\n"
                    "    \n"
                    "    for a in range(1, amount + 1):\n"
                    "        for c in coins:\n"
                    "            if a - c >= 0:\n"
                    "                dp[a] = min(dp[a], 1 + dp[a - c])\n"
                    "                \n"
                    "    return dp[amount] if dp[amount] != float('inf') else -1"
                ),
                "line_by_line": [
                    ("dp = [float('inf')] * (amount + 1)", "Fill DP array with infinity sentinel representing unreachable states."),
                    ("dp[0] = 0", "Base case: 0 coins needed to make amount 0."),
                    ("dp[a] = min(dp[a], 1 + dp[a - c])", "Take minimum between skipping coin and taking coin c.")
                ],
                "time_complexity": "O(amount * len(coins)).",
                "space_complexity": "O(amount) space for DP table.",
                "edge_cases": "amount = 0 (returns 0); no valid combination (returns -1); coin value > amount."
            }
        ],
        "cs_core": {
            "subject": "Computer Networks",
            "topic": "Application Protocols Evolution: HTTP/1.1 vs HTTP/2 vs HTTP/3 (QUIC)",
            "detailed_notes": [
                "The Evolution of Web Transport:\n"
                "1. HTTP/1.1 (1997):\n"
                "• Plaintext protocol using TCP sockets.\n"
                "• Keep-Alive allows persistent TCP connections, but suffers from Head-of-Line (HoL) Blocking at the application layer: subsequent HTTP requests must wait for the preceding response to finish.\n"
                "• Browsers worked around this by opening up to 6 parallel TCP connections per host.\n"
                "2. HTTP/2 (2015):\n"
                "• Binary Framing Layer replacing textual headers.\n"
                "• Multiplexing: Multiple bidirectional request/response streams over a single shared TCP socket, eliminating application-layer HoL blocking.\n"
                "• HPACK Header Compression: Eliminates repetitive header overhead.\n"
                "• Remaining Flaw: TCP-level HoL blocking! If a single TCP packet drops on a lossy Wi-Fi network, the OS kernel stalls all streams until the missing segment is retransmitted.\n"
                "3. HTTP/3 (2022):\n"
                "• Completely replaces TCP with QUIC over UDP!\n"
                "• Stream Independence: Streams are independent at the transport layer; a dropped packet in Stream 1 never blocks Stream 2.\n"
                "• 0-RTT Connection Establishment: Combines transport handshake and TLS 1.3 encryption in 1 round trip.\n"
                "• Connection Migration: Uses Connection IDs instead of IP/Port tuples, allowing smooth roaming from Wi-Fi to 5G without socket teardown."
            ],
            "interview_qa": [
                {
                    "q": "Why did HTTP/3 replace TCP with UDP?",
                    "a": "Because TCP suffers from transport-layer Head-of-Line (HoL) blocking: if one packet is lost, the operating system holds back all subsequent data in its buffer until the lost segment is retransmitted, stalling all multiplexed HTTP/2 streams. HTTP/3 uses QUIC over UDP, implementing independent stream reliability, zero-RTT connection establishment, and connection migration across networks."
                },
                {
                    "q": "What is HPACK compression in HTTP/2?",
                    "a": "HPACK is a specialized header compression algorithm that eliminates redundant HTTP headers. It maintains static and dynamic lookup tables between client and server: headers like `User-Agent` or `Cookie` sent in the first request are indexed, allowing subsequent requests to transmit only a 1-byte integer reference instead of repeating the entire header string."
                }
            ]
        },
        "project_defense": {
            "project_name": "Freelance Proposal Engineering",
            "feature_focus": "Freelancing Scope Definition & Technical Proposal Writing",
            "architecture_deep_dive": (
                "Packaging Technical Competencies into High-Value Client Deliverables:\n\n"
                "1. The 3 Core Freelance Offerings based on verified code:\n"
                "• Offering 1 (Real-Time Market Alert Engines): Event-driven notification pipelines in Python aiohttp with Telegram webhooks and sub-5s latency.\n"
                "• Offering 2 (API Backend & Webhook Integration): Building production FastAPI microservices, JWT authentication, and Telegram/WhatsApp bot notifications.\n"
                "• Offering 3 (Web Scraping & Real-Time Monitoring): Scheduled headless browsers and aiohttp workers with anti-blocking headers.\n\n"
                "2. Statement of Work (SOW) Structure:\n"
                "Every proposal must define: Executive Summary, Exact Deliverables, Acceptance Criteria, Out-of-Scope boundaries (to prevent scope creep), and Milestone-Based Payment schedules (30% upfront, 40% on staging demo, 30% on handover)."
            ),
            "interview_qa": [
                {
                    "q": "How do you protect yourself against scope creep when executing client projects?",
                    "a": "By drafting a strict Statement of Work (SOW) that lists both 'In-Scope' deliverables and explicit 'Out-of-Scope' features before accepting the project. Any client request outside the agreed SOW is formally treated as a Change Request (CR) with a separate timeline and billing quote."
                },
                {
                    "q": "What payment structure do you use for technical freelance contracts?",
                    "a": "I use a 3-stage milestone structure: 30% upfront advance to begin architecture, 40% upon deploying a functional staging demo on a private VPS for client review, and the final 30% prior to releasing repository ownership, production credentials, and final documentation."
                }
            ]
        },
        "daily_test": {
            "day": 23,
            "questions": [
                {"q": "What is the subinterval constraint for Simpson's 1/3 Rule?", "a": "The number of subintervals n must be strictly EVEN (n = 2, 4, 6, 8, ...)."},
                {"q": "What is the global truncation error order of Simpson's 3/8 Rule?", "a": "O(h^4)."},
                {"q": "Convert 72 degrees in a pie chart into a percentage.", "a": "72 / 3.6 = 20%."},
                {"q": "What is the state transition formula for LeetCode 322 (Coin Change)?", "a": "dp[a] = min(dp[a], 1 + dp[a - c]) for every coin c where a - c >= 0."},
                {"q": "What is Head-of-Line (HoL) blocking in HTTP/1.1?", "a": "A condition where subsequent HTTP requests on a persistent TCP connection must wait in line until the current response finishes transferring."},
                {"q": "Why does HTTP/3 use QUIC over UDP instead of TCP?", "a": "To eliminate transport-layer Head-of-Line blocking across streams and support 0-RTT connection establishment and connection migration."},
                {"q": "What is the degree of precision of Simpson's 1/3 Rule?", "a": "3 (Exact for polynomials up to cubic degree due to interval symmetry)."},
                {"q": "Name two key components of a Statement of Work (SOW) in freelancing.", "a": "Acceptance criteria and an explicit list of Out-of-Scope features."}
            ]
        }
    }

    # DAY 24
    days[24] = {
        "day": 24,
        "title": "KM Discovery in Databases (KDD), Speed Math & Longest Common Subsequence DP",
        "sem_data": {
            "subject": "BCA-5001 Knowledge Management",
            "topic": "Unit V — Knowledge Discovery in Databases (KDD 5 Stages) & Association Rule Mining (Apriori)",
            "detailed_notes": [
                "Knowledge Discovery in Databases (KDD) is the non-trivial, iterative process of identifying valid, novel, potentially useful, and ultimately understandable patterns from massive volumes of data stored in data warehouses.",
                "The 5 Sequential Stages of the KDD Process:\n"
                "1. Data Selection: Identifying the target dataset and focusing on a specific subset of variables or data samples relevant to the discovery goal.\n"
                "2. Data Preprocessing (Cleaning): Handling missing values (imputation), removing noise, filtering outliers, and resolving duplicate records.\n"
                "3. Data Transformation: Converting raw data into formats suitable for data mining algorithms through normalization, aggregation, feature selection, and dimensionality reduction.\n"
                "4. Data Mining: The core algorithmic engine. Applying machine learning, statistical modeling, or pattern recognition algorithms to extract underlying models.\n"
                "5. Interpretation and Evaluation: Validating discovered patterns against domain expertise, visualizing results, eliminating redundant findings, and translating patterns into actionable organizational knowledge.",
                "Association Rule Mining & The Apriori Algorithm:\n"
                "• Uncovers interesting relationships among items in large transaction databases (e.g. Market Basket Analysis: 'If a customer buys diapers, they also buy beer 70% of the time').\n"
                "• Key Metrics:\n"
                "  - Support(A -> B) = P(A union B) = (Transactions containing both A and B) / (Total Transactions).\n"
                "  - Confidence(A -> B) = P(B | A) = Support(A union B) / Support(A).\n"
                "  - Lift(A -> B) = Confidence(A -> B) / Support(B). If Lift > 1, item B is positively correlated with item A.\n"
                "• Apriori Principle (Anti-monotone Property): All non-empty subsets of a frequent itemset must also be frequent! If an itemset {A, B} is infrequent, no superset {A, B, C} can ever be frequent."
            ],
            "diagram_ascii": (
                "+-------------------------------------------------------------------------+\n"
                "|                      THE 5 STAGES OF THE KDD PROCESS                    |\n"
                "+-------------------------------------------------------------------------+\n"
                "|                                                                         |\n"
                "|  [ RAW DATA ]                                                           |\n"
                "|       |                                                                 |\n"
                "|       v  (Stage 1: Selection)                                           |\n"
                "|  [ TARGET DATA ]                                                        |\n"
                "|       |                                                                 |\n"
                "|       v  (Stage 2: Preprocessing / Cleaning)                            |\n"
                "|  [ PREPROCESSED DATA ]                                                  |\n"
                "|       |                                                                 |\n"
                "|       v  (Stage 3: Transformation / Reduction)                          |\n"
                "|  [ TRANSFORMED DATA ]                                                   |\n"
                "|       |                                                                 |\n"
                "|       v  (Stage 4: Data Mining / Pattern Extraction)                    |\n"
                "|  [ PATTERNS & MODELS ]                                                  |\n"
                "|       |                                                                 |\n"
                "|       v  (Stage 5: Interpretation & Evaluation)                         |\n"
                "|  [ ACTIONABLE KNOWLEDGE ]                                               |\n"
                "+-------------------------------------------------------------------------+"
            ),
            "comparison_table": {
                "headers": ["Comparison Aspect", "Online Analytical Processing (OLAP)", "Knowledge Discovery / Data Mining (KDD)"],
                "rows": [
                    ["Operation Paradigm", "User-driven verification (Top-down inquiry)", "Algorithm-driven discovery (Bottom-up pattern mining)"],
                    ["Primary Question", "'What happened and why did it happen?'", "'What hidden patterns exist that we did not ask for?'"],
                    ["Data Structure", "Multidimensional cubes (Star/Snowflake)", "Raw, transformed, or relational tables"],
                    ["Output Type", "Aggregated reports, charts, slice/dice cubes", "Predictive models, association rules, clusters"],
                    ["User Role", "Analyst formulates hypotheses", "Algorithm uncovers non-obvious hypotheses"]
                ]
            },
            "memorize": "KDD 5 Stages: Selection -> Preprocessing -> Transformation -> Data Mining -> Evaluation. Apriori rule: All subsets of a frequent itemset must be frequent. Support = P(A union B), Confidence = Support(A union B) / Support(A).",
            "understand": "Why is Data Mining only 1 step of KDD? Many practitioners confuse Data Mining with KDD. Data Mining is merely the algorithmic extraction step (Stage 4). Without preceding data cleaning (Stage 2) and succeeding human interpretation (Stage 5), data mining produces noisy, meaningless correlations ('Garbage In, Garbage Out').",
            "common_mistakes": "1. Treating Data Mining and KDD as identical terms. 2. Confusing Support (fraction of all transactions) with Confidence (conditional probability).",
            "pyq_year": "CSJMU BCA-5001 (2021, 2022-23, 2023-24, 2024-25)",
            "pyq_freq": "Appeared in 2021 (Q8 - 15m), 2022-23 (Q7 - 15m), 2023-24 (Q8 - 15m), 2024-25 (Q7 - 15m)",
            "pyq_question": "Explain the Knowledge Discovery in Databases (KDD) process in detail with its 5 stages. What is Data Mining? Explain Association Rule Mining with Support, Confidence, and the Apriori algorithm. (15 Marks)",
            "pyq_rubric": "Concept of KDD & Architecture diagram (4 marks) + 5 Stages detailed explanation (5 marks) + Association Rule Mining: Support, Confidence, Lift formulas (3 marks) + Apriori algorithm principle (3 marks) = 15 Marks.",
            "model_answer_paragraphs": [
                ("1. Definition of KDD and Data Mining:",
                 "Knowledge Discovery in Databases (KDD) is an organized multi-stage engineering process aimed at turning raw data into actionable business insight. Data Mining is the central mathematical phase within KDD that uses specialized algorithms to find recurring associations, clusters, and predictive models."),
                ("2. The 5 Sequential Stages of KDD:",
                 "• 1. Data Selection: Isolates relevant subsets of enterprise data from heterogeneous warehouses.\n"
                 "• 2. Data Preprocessing: Imputes missing values, eliminates noise, and standardizes data formats.\n"
                 "• 3. Data Transformation: Scales continuous variables, encodes categorical attributes, and aggregates granular records.\n"
                 "• 4. Data Mining: Executes algorithms such as Apriori, K-Means clustering, or Decision Trees.\n"
                 "• 5. Interpretation/Evaluation: Subject matter experts inspect patterns to filter out trivial correlations and visualize actionable rules."),
                ("3. Association Rule Mining & The Apriori Algorithm:",
                 "Association rules capture co-occurrence relationships (X => Y). Metrics:\n"
                 "• Support(X => Y) = Number of transactions containing both X and Y / Total transactions.\n"
                 "• Confidence(X => Y) = Number of transactions containing both X and Y / Number of transactions containing X.\n"
                 "• Lift(X => Y) = Confidence(X => Y) / Support(Y).\n"
                 "The Apriori Algorithm leverages the anti-monotone property: an itemset can only be frequent if all its subsets are frequent. This allows aggressive pruning of candidate itemsets, reducing search space from 2^N to manageable sets.")
            ]
        },
        "sgpa_target": {"focus": "Master 5 Stages of KDD & Apriori Algorithm Mathematics", "milestone": "Full 15/15 on KM Unit V Exam Question"},
        "apt_data": {
            "topic": "Quantitative Aptitude — Speed Math, Vedic Approximations & Mental Division",
            "tutorial": [
                "Placement quantitative rounds require solving questions in under 60 seconds. Speed math eliminates manual scratchwork.",
                "Key Mental Math Techniques:\n"
                "1. Squaring Numbers Ending in 5: (N5)^2 = [N * (N + 1)] followed by 25. Example: 75^2 = [7 * 8] 25 = 5625.\n"
                "2. Base Multiplication (Near 100): To multiply (100 + a) * (100 + b) = (100 + a + b) * 100 + (a * b). Example: 104 * 107 = (104 + 7) = 111, followed by (4 * 7 = 28) = 11128.\n"
                "3. Digital Sum Method: The sum of digits of a number modulo 9. If LHS digital sum != RHS digital sum, eliminate that option immediately!\n"
                "4. Division by 25: Multiply by 4 and shift decimal 2 places left (e.g. 340 / 25 = 340 * 4 / 100 = 13.6)."
            ],
            "formulas": "(N5)^2 = [N*(N+1)] 25. (100+a)*(100+b) = (100+a+b)*100 + a*b. Digital sum reduces numbers to single digits.",
            "shortcut": "Multiply any number by 11: Write outer digits, insert sum of adjacent digits in between. Example: 35 * 11 = 3 [3+5] 5 = 385.",
            "recognition": "Use these mental tricks across all numerical, percentage, and time-speed-distance questions in TCS, Infosys, and Cognizant.",
            "tier1_problem": "Compute mentally: 85^2 + 105 * 108.",
            "tier1_solution": "1. 85^2 = 8 * 9 followed by 25 = 7225.\n2. 105 * 108 = (105 + 8) followed by (5 * 8 = 40) = 11340.\n3. Sum = 7225 + 11340 = 18565. Answer: 18565.",
            "tier2_problem": "Calculate: 1475 / 25 mentally in 5 seconds.",
            "tier2_solution": "Divide by 25 = Multiply by 4 and divide by 100.\n1475 * 2 = 2950.\n2950 * 2 = 5900.\n5900 / 100 = 59. Answer: 59.",
            "tier3_problem": "[Digital Sum Elimination] Find the value of: 4182 + 5928 - 3841 = ? Options: (A) 6259, (B) 6269, (C) 6179, (D) 6369.",
            "tier3_solution": "Compute digital sum (casting out 9s):\n4182 ==> 4+1+8+2 = 15 ==> 1+5 = 6.\n5928 ==> 5+9+2+8 = 24 ==> 2+4 = 6.\n3841 ==> 3+8+4+1 = 16 ==> 1+6 = 7.\nExpression digital sum = 6 + 6 - 7 = 5.\nCheck options digital sums:\n(A) 6259 ==> 6+2+5+9 = 22 ==> 4 (Incorrect)\n(B) 6269 ==> 6+2+6+9 = 23 ==> 5 (MATCH!)\n(C) 6179 ==> 6+1+7+9 = 23 ==> 5 (Check last digit: 2 + 8 - 1 = 9)\nUnit digit check: 2 + 8 - 1 = 9. Last two digits: 82 + 28 - 41 = 110 - 41 = 69 ==> (B) 6269. Answer: 6269.",
            "tier4_problem": "Evaluate the square root of 7056 mentally.",
            "tier4_solution": "1. Unit digit is 6 ==> Last digit of square root is either 4 or 6 (since 4^2=16, 6^2=36).\n2. Group into pairs: 70 and 56.\n3. Largest square <= 70 is 64 (8^2 = 64) ==> Tens digit is 8.\n4. Possible roots: 84 or 86.\n5. Compare with 85: 85^2 = 8 * 9 followed by 25 = 7225.\n6. Since 7056 < 7225, the square root must be 84. Answer: 84.",
            "speed_drills": [
                {"q": "Compute 65^2.", "a": "6 * 7 = 42 followed by 25 = 4225."},
                {"q": "Compute 103 * 106.", "a": "(103 + 6) = 109 followed by (3 * 6 = 18) = 10918."},
                {"q": "What is 42 * 11?", "a": "4 [4+2] 2 = 462."},
                {"q": "Divide 750 by 25.", "a": "750 * 4 / 100 = 30."},
                {"q": "Compute 95^2.", "a": "9 * 10 = 90 followed by 25 = 9025."}
            ]
        },
        "dsa_problems": [
            {
                "title": "Longest Common Subsequence (LeetCode 1143 - Medium)",
                "difficulty": "Medium",
                "importance": "The Definitive 2D Dynamic Programming Interview Problem",
                "problem_statement": "Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.",
                "solution_approach": (
                    "2D Dynamic Programming Matrix:\n"
                    "Let dp[i][j] represent the length of the LCS of text1[0..i-1] and text2[0..j-1].\n"
                    "State Transition:\n"
                    "1. If characters match (`text1[i-1] == text2[j-1]`):\n"
                    "   dp[i][j] = 1 + dp[i-1][j-1]\n"
                    "2. If characters do NOT match:\n"
                    "   dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n"
                    "Base Case: dp[0][j] = 0 and dp[i][0] = 0."
                ),
                "code": (
                    "def longestCommonSubsequence(text1: str, text2: str) -> int:\n"
                    "    m, n = len(text1), len(text2)\n"
                    "    dp = [[0] * (n + 1) for _ in range(m + 1)]\n"
                    "    \n"
                    "    for i in range(1, m + 1):\n"
                    "        for j in range(1, n + 1):\n"
                    "            if text1[i - 1] == text2[j - 1]:\n"
                    "                dp[i][j] = 1 + dp[i - 1][j - 1]\n"
                    "            else:\n"
                    "                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\n"
                    "                \n"
                    "    return dp[m][n]"
                ),
                "line_by_line": [
                    ("dp = [[0] * (n + 1) for _ in range(m + 1)]", "Initialize (M+1)x(N+1) DP grid with 0s for base cases."),
                    ("if text1[i - 1] == text2[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]", "Characters match: extend LCS length from diagonal predecessor."),
                    ("else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])", "Characters mismatch: inherit maximum from left or top cell.")
                ],
                "time_complexity": "O(M * N) where M and N are string lengths.",
                "space_complexity": "O(M * N) auxiliary memory for DP matrix.",
                "edge_cases": "No common characters ('abc', 'def' returns 0); identical strings (returns len); empty string."
            }
        ],
        "cs_core": {
            "subject": "Database Management Systems (DBMS)",
            "topic": "SQL vs NoSQL Architectural Trade-offs: PostgreSQL vs MongoDB",
            "detailed_notes": [
                "Database Paradigms Compared:\n"
                "1. Relational DBMS (PostgreSQL, MySQL):\n"
                "• Structured tabular schema (Rows & Columns) with predefined column types.\n"
                "• ACID Transactions: Strong consistency, atomic commits, referential integrity via Foreign Keys.\n"
                "• Complex relational queries with SQL JOINS, indexing (B+ Tree), and normalization to eliminate redundancy.\n"
                "• Scaling: Primarily vertical scaling (larger CPU/RAM); horizontal sharding is complex.\n"
                "2. NoSQL Document Stores (MongoDB):\n"
                "• Schema-flexible JSON/BSON document model.\n"
                "• Denormalized data embedding: Nested arrays and sub-documents eliminate expensive joins.\n"
                "• BASE Consistency (Basically Available, Soft-state, Eventual consistency).\n"
                "• Scaling: Seamless horizontal scaling across distributed clusters via native automatic sharding."
            ],
            "interview_qa": [
                {
                    "q": "When would you choose PostgreSQL over MongoDB for a software project?",
                    "a": "I would choose PostgreSQL when the data model is highly relational with strict integrity requirements (such as financial transactions or e-commerce orders in CSMS where data corruption cannot be tolerated), when complex analytical aggregations and ACID transactions across multiple entities are essential, and when the schema is relatively stable."
                },
                {
                    "q": "What is the CAP Theorem and how does it relate to distributed databases?",
                    "a": "The CAP Theorem states that a distributed data store can guarantee at most TWO of the following three properties simultaneously: Consistency (all nodes see identical data at the same time), Availability (every non-failing node returns a response), and Partition Tolerance (system functions despite network communication partitions). Because network partitions are inevitable in distributed systems, databases must trade off between CP (e.g. MongoDB/HBase prioritizing consistency) and AP (e.g. Cassandra/DynamoDB prioritizing availability)."
                }
            ]
        },
        "project_defense": {
            "project_name": "Freelance Contracts & Delivery",
            "feature_focus": "Freelance Milestone Execution & Client Retainer Agreements",
            "architecture_deep_dive": (
                "Transitioning One-Off Projects into Recurring Monthly Retainers:\n\n"
                "1. Post-Deployment Maintenance Packaging:\n"
                "After delivering an initial project (e.g., custom FastAPI microservice or notification pipeline), clients face ongoing operational concerns: server downtime, "
                "API updates, dependency vulnerability patches, and backup management.\n\n"
                "2. Retainer Deliverables:\n"
                "• Tier 1: System Monitoring, monthly dependency updates, automated offsite database backups, and 4 hours of emergency bug fixes for a fixed monthly fee (e.g., ₹15,000/month).\n"
                "• Tier 2: Active feature extensions and prompt engineer updates.\n\n"
                "3. Value to Student Developer:\n"
                "Transforms erratic one-time project payouts into predictable recurring cash flow while building long-term client trust."
            ),
            "interview_qa": [
                {
                    "q": "How do you structure a monthly maintenance retainer for a client?",
                    "a": "I define a concrete SLA (Service Level Agreement) offering: 99% uptime monitoring, weekly automated offsite backups, dependency security updates, and a dedicated monthly bucket of 4 development hours for minor adjustments. Any feature work exceeding the monthly allocation is billed at a pre-agreed hourly rate."
                },
                {
                    "q": "How do you ensure smooth handover when concluding a development project?",
                    "a": "I provide a clean Git repository with an exhaustive README, environment variable `.env.example` templates, Docker Compose files for one-command local launching, interactive OpenAPI documentation, and a 15-minute recorded Loom video demonstrating deployment and configuration."
                }
            ]
        },
        "daily_test": {
            "day": 24,
            "questions": [
                {"q": "Name the 5 stages of the KDD process in order.", "a": "1. Data Selection, 2. Data Preprocessing, 3. Data Transformation, 4. Data Mining, 5. Interpretation/Evaluation."},
                {"q": "State the Apriori principle.", "a": "All non-empty subsets of a frequent itemset must also be frequent (anti-monotone property)."},
                {"q": "Compute 75^2 mentally.", "a": "7 * 8 = 56 followed by 25 = 5625."},
                {"q": "What is the time complexity of 2D DP for Longest Common Subsequence?", "a": "O(M * N) where M and N are the lengths of the two input strings."},
                {"q": "What does the 'C' stand for in the CAP Theorem?", "a": "Consistency — every read receives the most recent write or an error."},
                {"q": "How does Support differ from Confidence in Association Rule Mining?", "a": "Support is the fraction of total transactions containing both X and Y. Confidence is the conditional probability that a transaction contains Y given that it contains X."},
                {"q": "When is MongoDB preferable over a relational database?", "a": "When dealing with rapidly evolving unstructured/hierarchical documents, high-volume ingestion, and requirements for native horizontal sharding."},
                {"q": "Explain the concept of an SLA in freelance technical services.", "a": "A Service Level Agreement specifying measurable commitments regarding server uptime, bug response times, and monthly maintenance hours."}
            ]
        }
    }

    return days
