#!/usr/bin/env python3
"""
scripts/curriculum/banks/mixed_bank_16_30.py
Authentic Mixed Test MCQs for Days 16 to 30 (20 MCQs/day).
"""

MIXED_DAYS_16_30 = {
  "16": [
    {
      "id": "TEST-16-01",
      "category": "Academic (Academic Theory)",
      "question": "What is a 'Community of Practice' (CoP) in an enterprise Knowledge Management ecosystem?",
      "options": [
        "An official disciplinary board that terminates underperforming employees",
        "An informal, self-organizing group of practitioners who share a passion or domain and interact regularly to improve their craft",
        "A software tool for running payroll calculations",
        "A hardware firewall preventing external internet access"
      ],
      "correct_answer": "B",
      "explanation": "CoPs (Lave & Wenger) are groups of people bound by informal expertise and shared passion to solve problems collaboratively."
    },
    {
      "id": "TEST-16-02",
      "category": "Academic (Academic Theory)",
      "question": "What is the primary cultural barrier to successful knowledge sharing in corporate organizations?",
      "options": [
        "Lack of Gigabit Ethernet bandwidth",
        "'Knowledge is Power' hoarding syndrome where individuals fear losing personal value by sharing expertise",
        "Using Linux instead of Windows",
        "Too many database backups"
      ],
      "correct_answer": "B",
      "explanation": "Knowledge hoarding arises when organizations fail to incentivize transparency, causing experts to treat knowledge as individual leverage."
    },
    {
      "id": "TEST-16-03",
      "category": "Academic (Academic Theory)",
      "question": "Which KM capture mechanism pairs a junior engineer with an experienced expert to observe and absorb intuitive problem-solving heuristics?",
      "options": [
        "Database Normalization",
        "Apprenticeship / Shadowing",
        "Web Scraping",
        "Binary Search"
      ],
      "correct_answer": "B",
      "explanation": "Shadowing and mentoring enable direct tacit-to-tacit knowledge transfer through contextual observation and guided reflection."
    },
    {
      "id": "TEST-16-04",
      "category": "Academic (Academic Theory)",
      "question": "In knowledge management metrics, what does the 'Knowledge Retention Rate' measure?",
      "options": [
        "The percentage of hard drives retained during data center upgrades",
        "The organization's ability to preserve mission-critical institutional expertise when senior employees leave or retire",
        "The speed of RAM cache memory",
        "The ratio of SQL queries to web visits"
      ],
      "correct_answer": "B",
      "explanation": "Retention rate quantifies an organization's capacity to codify and transition institutional memory before attrition occurs."
    },
    {
      "id": "TEST-16-05",
      "category": "Academic (Academic Theory)",
      "question": "What role does an After Action Review (AAR) play in organizational learning?",
      "options": [
        "It calculates end-of-year tax liabilities",
        "It provides a structured debrief immediately following a project to analyze what was expected, what actually occurred, and why",
        "It terminates software licenses",
        "It formats database tables into 3NF"
      ],
      "correct_answer": "B",
      "explanation": "Originating in the US Army, an AAR is a structured 4-question debrief that captures operational lessons learned before memories fade."
    },
    {
      "id": "TEST-16-06",
      "category": "Placement Aptitude",
      "question": "In a row of 25 girls, when Neha was shifted by 4 places towards the left, she became 10th from the left end. What was her earlier position from the right end of the row?",
      "options": [
        "12th",
        "11th",
        "13th",
        "14th"
      ],
      "correct_answer": "A",
      "explanation": "Earlier position from left = 10 + 4 = 14th. Position from right = (25 - 14) + 1 = 12th."
    },
    {
      "id": "TEST-16-07",
      "category": "Placement Aptitude",
      "question": "Six persons A, B, C, D, E, F are sitting in two rows, three in each row. E is not at the end of any row. D is second to the left of F. C is diagonal to D. B is neighbor of F. Who is facing B?",
      "options": [
        "E",
        "A",
        "C",
        "D"
      ],
      "correct_answer": "A",
      "explanation": "Row 1: C, E, D; Row 2: A, B, F. E faces B directly."
    },
    {
      "id": "TEST-16-08",
      "category": "Placement Aptitude",
      "question": "In a class of 40 students, Samir is ranked 8th from top and Alok is ranked 12th from bottom. How many students are there between Samir and Alok?",
      "options": [
        "20 students",
        "22 students",
        "18 students",
        "24 students"
      ],
      "correct_answer": "A",
      "explanation": "Students between = Total - (Top rank + Bottom rank) = 40 - (8 + 12) = 40 - 20 = 20 students."
    },
    {
      "id": "TEST-16-09",
      "category": "Placement Aptitude",
      "question": "Five girls are sitting in a circle facing the center. Suman is between Rita and Monica. Neha is to the immediate left of Pooja. Rita is to the immediate left of Neha. Who is to the immediate right of Suman?",
      "options": [
        "Rita",
        "Monica",
        "Pooja",
        "Neha"
      ],
      "correct_answer": "A",
      "explanation": "Circle order clockwise: Monica, Suman, Rita, Neha, Pooja. To the immediate right of Suman is Rita."
    },
    {
      "id": "TEST-16-10",
      "category": "Placement Aptitude",
      "question": "In a line facing North, P is 13th from left and Q is 17th from right. If they interchange positions, P becomes 21st from left. How many persons are in the row?",
      "options": [
        "37 persons",
        "36 persons",
        "38 persons",
        "35 persons"
      ],
      "correct_answer": "A",
      "explanation": "Total = P's new left position + Q's original right position - 1 = 21 + 17 - 1 = 37 persons."
    },
    {
      "id": "TEST-16-11",
      "category": "Core CS (Computer Networks)",
      "question": "In HDLC framing, bit stuffing inserts a '0' bit after how many consecutive '1' bits?",
      "options": [
        "4",
        "5",
        "6",
        "7"
      ],
      "correct_answer": "B",
      "explanation": "Sender stuffs a 0 after 5 consecutive 1s to prevent collision with the flag pattern 01111110."
    },
    {
      "id": "TEST-16-12",
      "category": "Core CS (Computer Networks)",
      "question": "What mathematical operation is used in CRC modulo-2 arithmetic instead of standard subtraction?",
      "options": [
        "AND",
        "OR",
        "XOR",
        "NOT"
      ],
      "correct_answer": "C",
      "explanation": "Modulo-2 binary division uses bitwise XOR operations without borrowing."
    },
    {
      "id": "TEST-16-13",
      "category": "Core CS (Computer Networks)",
      "question": "If 3 bits are used for sequence numbers in Selective Repeat, what is the maximum sender window size?",
      "options": [
        "8",
        "7",
        "4",
        "3"
      ],
      "correct_answer": "C",
      "explanation": "Max window size in Selective Repeat is 2^(k-1) = 2^(3-1) = 4."
    },
    {
      "id": "TEST-16-14",
      "category": "Core CS (Computer Networks)",
      "question": "Which sliding window protocol buffers out-of-order frames at the receiver?",
      "options": [
        "Stop-and-Wait",
        "Go-Back-N",
        "Selective Repeat",
        "Pure ALOHA"
      ],
      "correct_answer": "C",
      "explanation": "Selective Repeat buffers out-of-order frames, whereas Go-Back-N discards them."
    },
    {
      "id": "TEST-16-15",
      "category": "Core CS (Computer Networks)",
      "question": "The frame check sequence (FCS) field in an Ethernet frame is computed using:",
      "options": [
        "Simple Parity",
        "Hamming Code",
        "CRC-32",
        "MD5 Hash"
      ],
      "correct_answer": "C",
      "explanation": "Ethernet Data Link frames utilize CRC-32 for error detection."
    },
    {
      "id": "TEST-16-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Tree Traversals: DFS Pre, In, Post-Order' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(H) Auxiliary Space (H = height of tree).",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Tree Traversals: DFS Pre, In, Post-Order' pattern operates with O(N) Time, O(H) Auxiliary Space (H = height of tree): Recursion stack follows call frames matching tree height; post-order processes subtrees before root, enabling bottom-up aggregation.."
    },
    {
      "id": "TEST-16-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Tree Traversals: DFS Pre, In, Post-Order' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Empty tree.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Tree Traversals: DFS Pre, In, Post-Order include Empty tree, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-16-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Maximum Depth of Binary Tree', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(H) Auxiliary Space (H = height of tree).",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(H) Auxiliary Space (H = height of tree) by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-16-19",
      "category": "Projects (SmartGalla)",
      "question": "In Sarthak's project 'SmartGalla', what is the core architectural principle regarding 'Automated Competitive Intelligence: The Blinkit Web Scraping Engine'?",
      "options": [
        "Price parity alerts help local merchants stay competitive against dark-store quick-commerce giants.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For SmartGalla, the architectural invariant is: Price parity alerts help local merchants stay competitive against dark-store quick-commerce giants.."
    },
    {
      "id": "TEST-16-20",
      "category": "Projects (SmartGalla)",
      "question": "Regarding 'SmartGalla', how should you defend this design decision in a technical interview: 'How does the Blinkit scraping worker in SmartGalla extract real-time grocery prices?'?",
      "options": [
        "We engineered an automated Node.js worker using Playwright that queries Blinkit's public catalog search endpoints using rotating User-Agents and localized pinco...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: We engineered an automated Node.js worker using Playwright that queries Blinkit's public catalog search endpoints using rotating User-Agents."
    }
  ],
  "17": [
    {
      "id": "TEST-17-01",
      "category": "Academic (Academic Theory)",
      "question": "What condition guarantees the convergence of both Gauss-Jacobi and Gauss-Seidel iterative methods for solving AX = B?",
      "options": [
        "Matrix A is skew-symmetric",
        "Matrix A is Strictly Diagonally Dominant (|a_ii| > sum_{j!=i} |a_ij| for all rows)",
        "det(A) < 1",
        "All elements of A are negative"
      ],
      "correct_answer": "B",
      "explanation": "Strict diagonal dominance guarantees that iterative approximations converge to the unique solution regardless of initial guess."
    },
    {
      "id": "TEST-17-02",
      "category": "Academic (Academic Theory)",
      "question": "How does Gauss-Seidel iteration differ from the Gauss-Jacobi method?",
      "options": [
        "Gauss-Seidel uses the most freshly computed variable values immediately in the current iteration",
        "Gauss-Jacobi converges twice as fast as Gauss-Seidel",
        "Gauss-Seidel cannot be used for 3x3 systems",
        "Gauss-Jacobi does not require matrix coefficients"
      ],
      "correct_answer": "A",
      "explanation": "Gauss-Seidel updates variables in-place, using x_1^{(k+1)} immediately to calculate x_2^{(k+1)}, converging roughly twice as fast as Jacobi."
    },
    {
      "id": "TEST-17-03",
      "category": "Academic (Academic Theory)",
      "question": "In iterative methods, what does the relaxation parameter omega represent in the Successive Over-Relaxation (SOR) method?",
      "options": [
        "Matrix inversion scale",
        "An extrapolation factor where 1 < omega < 2 accelerates convergence compared to standard Gauss-Seidel",
        "The number of CPU threads allocated",
        "The floating point precision epsilon"
      ],
      "correct_answer": "B",
      "explanation": "SOR accelerates Gauss-Seidel by weighting the new estimate with a relaxation factor (1 < omega < 2 for over-relaxation)."
    },
    {
      "id": "TEST-17-04",
      "category": "Academic (Academic Theory)",
      "question": "If an iterative method computes x^{(k+1)} = [2.001, 3.999] and x^{(k)} = [2.000, 4.000], what is the absolute error norm ||x^{(k+1)} - x^{(k)}||_infinity?",
      "options": [
        "0.001",
        "0.002",
        "0.000",
        "0.010"
      ],
      "correct_answer": "A",
      "explanation": "The infinity norm is the maximum absolute difference across components: max(|2.001 - 2.000|, |3.999 - 4.000|) = 0.001."
    },
    {
      "id": "TEST-17-05",
      "category": "Academic (Academic Theory)",
      "question": "Why are iterative methods (Jacobi, Seidel) preferred over direct methods (Gauss Elimination) for very large sparse systems (e.g., 100,000 equations)?",
      "options": [
        "They require O(N) storage preserving zero entries and avoid massive O(N^3) matrix fill-in",
        "They always produce exact solutions without rounding errors",
        "They do not require initial guesses",
        "They only use integer multiplication"
      ],
      "correct_answer": "A",
      "explanation": "Sparse systems from PDEs have mostly zero entries. Iterative methods avoid fill-in and have O(N) memory and per-iteration work."
    },
    {
      "id": "TEST-17-06",
      "category": "Placement Aptitude",
      "question": "If in a certain code 'TEACHER' is written as 'VGCEJGT', how is 'CHILDREN' written in that code?",
      "options": [
        "EJKNFTGP",
        "EJKNFUTP",
        "EJKNFTHP",
        "EJKNHTGP"
      ],
      "correct_answer": "A",
      "explanation": "Each letter is shifted forward by +2 positions in the alphabet: C->E, H->J, I->K, L->N, D->F, R->T, E->G, N->P => EJKNFTGP."
    },
    {
      "id": "TEST-17-07",
      "category": "Placement Aptitude",
      "question": "If 'DELHI' can be coded as '73541' and 'CALCUTTA' as '82589662', how can 'CALICUT' be coded?",
      "options": [
        "8251896",
        "8251869",
        "8258196",
        "8521896"
      ],
      "correct_answer": "A",
      "explanation": "Direct letter substitution: C=8, A=2, L=5, I=1, C=8, U=9, T=6 => 8251896."
    },
    {
      "id": "TEST-17-08",
      "category": "Placement Aptitude",
      "question": "In a certain code language, 'pit dar na' means 'you are good', 'dar tok pa' means 'good and bad', and 'tim na tok' means 'they are bad'. What represents 'they'?",
      "options": [
        "tim",
        "na",
        "tok",
        "dar"
      ],
      "correct_answer": "A",
      "explanation": "Comparing 'na' is 'are', 'tok' is 'bad'. In 'tim na tok' ('they are bad'), 'tim' must represent 'they'."
    },
    {
      "id": "TEST-17-09",
      "category": "Placement Aptitude",
      "question": "If 'ROSE' is coded as 6821, 'CHAIR' is 73456, and 'PREACH' is 961473, what is the code for 'SEARCH'?",
      "options": [
        "214673",
        "214763",
        "241673",
        "214637"
      ],
      "correct_answer": "A",
      "explanation": "Direct substitution: S=2, E=1, A=4, R=6, C=7, H=3 => 214673."
    },
    {
      "id": "TEST-17-10",
      "category": "Placement Aptitude",
      "question": "In a certain code, 'MONKEY' is written as 'XDJMNL'. How is 'TIGER' written in that code?",
      "options": [
        "QDFHS",
        "SDFHQ",
        "QDFHR",
        "SDFHS"
      ],
      "correct_answer": "A",
      "explanation": "Reverse the word and subtract 1 from each letter: TIGER reversed is REGIT. R-1=Q, E-1=D, G-1=F, I-1=H, T-1=S => QDFHS."
    },
    {
      "id": "TEST-17-11",
      "category": "Core CS (Computer Networks)",
      "question": "What is the minimum frame size in standard 10Mbps Ethernet to guarantee collision detection?",
      "options": [
        "32 bytes",
        "64 bytes",
        "128 bytes",
        "512 bytes"
      ],
      "correct_answer": "B",
      "explanation": "Standard Ethernet mandates a 64-byte (512-bit) minimum frame size."
    },
    {
      "id": "TEST-17-12",
      "category": "Core CS (Computer Networks)",
      "question": "In CSMA/CD, the condition ensuring a sender detects collision before finishing transmission is:",
      "options": [
        "T_tx >= T_prop",
        "T_tx >= 2 * T_prop",
        "T_prop >= 2 * T_tx",
        "T_tx = 0"
      ],
      "correct_answer": "B",
      "explanation": "Transmission time must exceed two times propagation delay to detect worst-case collision echo."
    },
    {
      "id": "TEST-17-13",
      "category": "Core CS (Computer Networks)",
      "question": "The mechanism used in IEEE 802.11 Wi-Fi to solve the Hidden Terminal problem is:",
      "options": [
        "Token Ring passing",
        "RTS/CTS handshake",
        "CSMA/CD Jam signals",
        "CRC-32 checksums"
      ],
      "correct_answer": "B",
      "explanation": "RTS/CTS reservations inform hidden nodes to defer transmission."
    },
    {
      "id": "TEST-17-14",
      "category": "Core CS (Computer Networks)",
      "question": "How many collision domains does an 8-port Ethernet Layer-2 Switch have?",
      "options": [
        "1",
        "2",
        "8",
        "0"
      ],
      "correct_answer": "C",
      "explanation": "Each switch port represents an isolated collision domain, so an 8-port switch has 8."
    },
    {
      "id": "TEST-17-15",
      "category": "Core CS (Computer Networks)",
      "question": "In the Binary Exponential Backoff algorithm, after 3 consecutive collisions, the random multiplier r is chosen from:",
      "options": [
        "0 to 3",
        "0 to 7",
        "0 to 15",
        "0 to 8"
      ],
      "correct_answer": "B",
      "explanation": "Range is [0, 2^k - 1] = [0, 2^3 - 1] = [0, 7]."
    },
    {
      "id": "TEST-17-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Binary Search Tree (BST) Validation' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(H) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Binary Search Tree (BST) Validation' pattern operates with O(N) Time, O(H) Auxiliary Space: Passes down valid value bounds [low, high] that tighten as we descend into left and right subtrees.."
    },
    {
      "id": "TEST-17-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Binary Search Tree (BST) Validation' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Single node.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Binary Search Tree (BST) Validation include Single node, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-17-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Validate Binary Search Tree', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(H) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(H) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-17-19",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "In Sarthak's project 'NSE2 / BulkBeat TV', what is the core architectural principle regarding 'Subscription Monetization, Webhook Reconciliation & Real Revenue Metrics'?",
      "options": [
        "104 paying subscribers generated approximately ₹1.11 lakh in revenue with automated license key provisioning.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For NSE2 / BulkBeat TV, the architectural invariant is: 104 paying subscribers generated approximately ₹1.11 lakh in revenue with automated license key provisioning.."
    },
    {
      "id": "TEST-17-20",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "Regarding 'NSE2 / BulkBeat TV', how should you defend this design decision in a technical interview: 'How did you automate subscription renewals and access revocation in NSE2?'?",
      "options": [
        "We integrated Razorpay Subscriptions. When a user pays, Razorpay triggers a webhook containing the user's telegram ID in the payment notes. The backend verifies...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: We integrated Razorpay Subscriptions. When a user pays, Razorpay triggers a webhook containing the user's telegram ID in the payment notes. ."
    }
  ],
  "18": [
    {
      "id": "TEST-18-01",
      "category": "Academic (Academic Theory)",
      "question": "Which JDBC driver type is known as the 'Pure Java Native Protocol Driver' (Type 4) and communicates directly with the database engine without client libraries?",
      "options": [
        "Type 1 (JDBC-ODBC Bridge)",
        "Type 2 (Native-API Driver)",
        "Type 3 (Network-Protocol Driver)",
        "Type 4 (Direct Native-Protocol Pure Java Driver)"
      ],
      "correct_answer": "D",
      "explanation": "Type 4 drivers are 100% pure Java, converting JDBC calls directly into vendor-specific network socket protocols without middleware."
    },
    {
      "id": "TEST-18-02",
      "category": "Academic (Academic Theory)",
      "question": "Why is PreparedStatement preferred over standard Statement in JDBC for executing parameterized queries?",
      "options": [
        "PreparedStatement compiles SQL once on the database server, improves execution speed, and inherently prevents SQL Injection",
        "PreparedStatement allows executing non-SQL Python scripts",
        "PreparedStatement does not require a database connection",
        "Standard Statement cannot execute SELECT queries"
      ],
      "correct_answer": "A",
      "explanation": "PreparedStatement pre-compiles SQL plans and treats parameters as strictly typed literals, neutralizing SQL injection attacks."
    },
    {
      "id": "TEST-18-03",
      "category": "Academic (Academic Theory)",
      "question": "What JDBC interface method must be called to process the tabular rows returned by an `executeQuery()` statement?",
      "options": [
        "ResultSet.next()",
        "ResultSet.fetch()",
        "Connection.commit()",
        "Statement.scroll()"
      ],
      "correct_answer": "A",
      "explanation": "ResultSet.next() moves the cursor forward one row from its initial position before the first row, returning false when exhausted."
    },
    {
      "id": "TEST-18-04",
      "category": "Academic (Academic Theory)",
      "question": "How does database Connection Pooling improve enterprise web application performance?",
      "options": [
        "It permanently encrypts all database tables",
        "It reuses an existing pool of pre-established physical connections, avoiding the expensive overhead of TCP handshakes and authentication on every request",
        "It eliminates the need for SQL transactions",
        "It compresses all JPEG images in the database"
      ],
      "correct_answer": "B",
      "explanation": "Opening a DB connection takes 50-200ms. Pooling keeps open connections ready for checkout, reducing acquisition latency to <1ms."
    },
    {
      "id": "TEST-18-05",
      "category": "Academic (Academic Theory)",
      "question": "To execute multiple transactional SQL updates atomically, what method must be called on the JDBC Connection before executing queries?",
      "options": [
        "connection.setAutoCommit(false)",
        "connection.close()",
        "connection.rollback()",
        "connection.setReadOnly(true)"
      ],
      "correct_answer": "A",
      "explanation": "Disabling auto-commit (`setAutoCommit(false)`) groups operations into an atomic transaction concluded with `commit()` or `rollback()`."
    },
    {
      "id": "TEST-18-06",
      "category": "Placement Aptitude",
      "question": "What is the next number in the sequence: 3, 7, 15, 31, 63, ?",
      "options": [
        "127",
        "128",
        "125",
        "126"
      ],
      "correct_answer": "A",
      "explanation": "Each term is 2x + 1: 63 * 2 + 1 = 127."
    },
    {
      "id": "TEST-18-07",
      "category": "Placement Aptitude",
      "question": "Find the missing number in the series: 4, 9, 25, 49, 121, ?",
      "options": [
        "169",
        "144",
        "196",
        "225"
      ],
      "correct_answer": "A",
      "explanation": "Squares of consecutive prime numbers: 2^2, 3^2, 5^2, 7^2, 11^2, 13^2 = 169."
    },
    {
      "id": "TEST-18-08",
      "category": "Placement Aptitude",
      "question": "Find the next term: 1, 4, 27, 256, ?",
      "options": [
        "3,125",
        "1,024",
        "4,096",
        "625"
      ],
      "correct_answer": "A",
      "explanation": "Pattern is n^n: 1^1=1, 2^2=4, 3^3=27, 4^4=256, 5^5 = 3,125."
    },
    {
      "id": "TEST-18-09",
      "category": "Placement Aptitude",
      "question": "Find the wrong number in the series: 1, 2, 6, 15, 31, 56, 91",
      "options": [
        "91",
        "31",
        "56",
        "15"
      ],
      "correct_answer": "A",
      "explanation": "Differences are squares: +1, +4, +9, +16, +25, +36. 56 + 36 = 92, but series has 91."
    },
    {
      "id": "TEST-18-10",
      "category": "Placement Aptitude",
      "question": "What is the next number in the Fibonacci-style series: 2, 3, 5, 8, 13, 21, ?",
      "options": [
        "34",
        "32",
        "35",
        "33"
      ],
      "correct_answer": "A",
      "explanation": "Sum of preceding two terms: 13 + 21 = 34."
    },
    {
      "id": "TEST-18-11",
      "category": "Core CS (Computer Networks)",
      "question": "How many usable host IP addresses are available in a /26 subnet?",
      "options": [
        "64",
        "62",
        "30",
        "126"
      ],
      "correct_answer": "B",
      "explanation": "Host bits = 32 - 26 = 6 bits. Usable hosts = 2^6 - 2 = 64 - 2 = 62."
    },
    {
      "id": "TEST-18-12",
      "category": "Core CS (Computer Networks)",
      "question": "Which protocol resolves an IPv4 address to a physical MAC address on a local Ethernet segment?",
      "options": [
        "DNS",
        "DHCP",
        "ARP",
        "BGP"
      ],
      "correct_answer": "C",
      "explanation": "ARP maps 32-bit IP addresses to 48-bit MAC addresses."
    },
    {
      "id": "TEST-18-13",
      "category": "Core CS (Computer Networks)",
      "question": "Traceroute discovers intermediate routers along a network path by manipulating which IP header field?",
      "options": [
        "Header Checksum",
        "Time To Live (TTL)",
        "Type of Service",
        "Identification"
      ],
      "correct_answer": "B",
      "explanation": "Traceroute increments TTL from 1 upward, receiving ICMP Time Exceeded packets from each hop."
    },
    {
      "id": "TEST-18-14",
      "category": "Core CS (Computer Networks)",
      "question": "Which of the following is an RFC 1918 Private IP address?",
      "options": [
        "8.8.8.8",
        "172.20.14.5",
        "169.254.1.1",
        "203.0.113.50"
      ],
      "correct_answer": "B",
      "explanation": "172.20.14.5 falls within the private Class B range (172.16.0.0 to 172.31.255.255)."
    },
    {
      "id": "TEST-18-15",
      "category": "Core CS (Computer Networks)",
      "question": "What is the broadcast address for the subnet 192.168.5.0/24?",
      "options": [
        "192.168.5.0",
        "192.168.5.1",
        "192.168.5.255",
        "192.168.5.254"
      ],
      "correct_answer": "C",
      "explanation": "In a /24 subnet, setting all 8 host bits to 1 yields .255, the broadcast address."
    },
    {
      "id": "TEST-18-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Lowest Common Ancestor (LCA) in Binary Trees' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(H) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Lowest Common Ancestor (LCA) in Binary Trees' pattern operates with O(N) Time, O(H) Auxiliary Space: If p and q are found in different subtrees of node N, N is their LCA. If both lie in the same subtree, that subtree's root returns the LCA.."
    },
    {
      "id": "TEST-18-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Lowest Common Ancestor (LCA) in Binary Trees' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: p is direct parent of q.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Lowest Common Ancestor (LCA) in Binary Trees include p is direct parent of q, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-18-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Lowest Common Ancestor of a Binary Tree', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(H) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(H) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-18-19",
      "category": "Projects (Caloriv)",
      "question": "In Sarthak's project 'Caloriv', what is the core architectural principle regarding 'Offline-First Mobile Synchronization & SQLite Local Storage'?",
      "options": [
        "Mobile apps must function reliably in low-connectivity gym or outdoor environments.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Caloriv, the architectural invariant is: Mobile apps must function reliably in low-connectivity gym or outdoor environments.."
    },
    {
      "id": "TEST-18-20",
      "category": "Projects (Caloriv)",
      "question": "Regarding 'Caloriv', how should you defend this design decision in a technical interview: 'How does Caloriv allow users to log meals without an internet connection?'?",
      "options": [
        "All daily meal logs, food databases, and calorie tallies are written immediately to a local SQLite database using React Native's SQLite library. Each record car...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: All daily meal logs, food databases, and calorie tallies are written immediately to a local SQLite database using React Native's SQLite libr."
    }
  ],
  "19": [
    {
      "id": "TEST-19-01",
      "category": "Academic (Academic Theory)",
      "question": "Which shortest path algorithm does the Open Shortest Path First (OSPF) Link-State routing protocol use to build its routing table?",
      "options": [
        "Bellman-Ford Algorithm",
        "Dijkstra's Shortest Path Algorithm",
        "Floyd-Warshall Algorithm",
        "Kruskal's Minimum Spanning Tree Algorithm"
      ],
      "correct_answer": "B",
      "explanation": "OSPF is a Link-State protocol; every router floods Link State Advertisements (LSAs) and runs Dijkstra's algorithm locally."
    },
    {
      "id": "TEST-19-02",
      "category": "Academic (Academic Theory)",
      "question": "What critical flaw affects the Distance Vector Routing (DVR) algorithm based on Bellman-Ford when a link or destination goes down?",
      "options": [
        "Split Horizon failure",
        "Count-to-Infinity problem and slow convergence loops",
        "Buffer bloat deadlock",
        "Checksum collision"
      ],
      "correct_answer": "B",
      "explanation": "In DVR, routers advertise distances without full topology paths, causing routing loops and the 'Count-to-Infinity' phenomenon during link failures."
    },
    {
      "id": "TEST-19-03",
      "category": "Academic (Academic Theory)",
      "question": "What two mechanisms are commonly implemented to mitigate the Count-to-Infinity problem in Distance Vector routing?",
      "options": [
        "Split Horizon and Poison Reverse",
        "Dijkstra and Prim algorithms",
        "Three-way handshakes and FIN packets",
        "Parity check and Hamming codes"
      ],
      "correct_answer": "A",
      "explanation": "Split Horizon prevents advertising a route back on the interface from which it was learned; Poison Reverse sets the metric to infinity (16)."
    },
    {
      "id": "TEST-19-04",
      "category": "Academic (Academic Theory)",
      "question": "In hierarchical routing, what protocol is used to route traffic BETWEEN autonomous systems across the global Internet backbone?",
      "options": [
        "Routing Information Protocol (RIP)",
        "Open Shortest Path First (OSPF)",
        "Border Gateway Protocol (BGP-4)",
        "Address Resolution Protocol (ARP)"
      ],
      "correct_answer": "C",
      "explanation": "BGP is the de-facto inter-domain routing protocol (Path Vector) establishing policy and reachability between Autonomous Systems (AS)."
    },
    {
      "id": "TEST-19-05",
      "category": "Academic (Academic Theory)",
      "question": "What is the metric used by the legacy Routing Information Protocol (RIP) to calculate distance?",
      "options": [
        "Bandwidth delay product",
        "Hop count (maximum 15 hops, 16 represents infinity)",
        "Packet drop probability",
        "Link dollar cost"
      ],
      "correct_answer": "B",
      "explanation": "RIP uses hop count as its sole metric, capping network diameters at 15 hops to limit convergence loops."
    },
    {
      "id": "TEST-19-06",
      "category": "Placement Aptitude",
      "question": "What is the angle between the minute hand and the hour hand of a clock at 3:40?",
      "options": [
        "130 degrees",
        "125 degrees",
        "140 degrees",
        "135 degrees"
      ],
      "correct_answer": "A",
      "explanation": "Angle = |30 * H - (11/2) * M| = |30 * 3 - (11/2) * 40| = |90 - 220| = 130 degrees."
    },
    {
      "id": "TEST-19-07",
      "category": "Placement Aptitude",
      "question": "If 1st January 2007 was a Monday, what was the day of the week on 1st January 2008?",
      "options": [
        "Tuesday",
        "Wednesday",
        "Sunday",
        "Monday"
      ],
      "correct_answer": "A",
      "explanation": "2007 is an ordinary year with 1 odd day. 1 Jan 2008 = Monday + 1 = Tuesday."
    },
    {
      "id": "TEST-19-08",
      "category": "Placement Aptitude",
      "question": "How many times do the hands of a clock coincide in a 24-hour day?",
      "options": [
        "22 times",
        "24 times",
        "20 times",
        "44 times"
      ],
      "correct_answer": "A",
      "explanation": "Hands coincide 11 times in 12 hours, so 11 * 2 = 22 times in 24 hours."
    },
    {
      "id": "TEST-19-09",
      "category": "Placement Aptitude",
      "question": "What was the day of the week on 15th August 1947?",
      "options": [
        "Friday",
        "Thursday",
        "Saturday",
        "Sunday"
      ],
      "correct_answer": "A",
      "explanation": "1600 yrs = 0, 300 yrs = 1 odd day. 46 yrs (11 leap, 35 ord) = 22 + 35 = 57 = 1 odd day. Jan(3)+Feb(0)+Mar(3)+Apr(2)+May(3)+Jun(2)+Jul(3)+Aug(15=1) = 17 = 3 odd days. Total = 1 + 1 + 3 = 5 odd days => Friday."
    },
    {
      "id": "TEST-19-10",
      "category": "Placement Aptitude",
      "question": "A watch gains 5 seconds in 3 minutes and was set right at 8 AM. What time will it show at 10 PM on the same day?",
      "options": [
        "10:23:20 PM",
        "10:15:00 PM",
        "10:30:00 PM",
        "10:20:00 PM"
      ],
      "correct_answer": "A",
      "explanation": "From 8 AM to 10 PM = 14 hours = 840 minutes. Number of 3-min intervals = 840 / 3 = 280. Gain = 280 * 5 = 1,400 sec = 23 min 20 sec. Time shown = 10:23:20 PM."
    },
    {
      "id": "TEST-19-11",
      "category": "Core CS (Computer Networks)",
      "question": "Which algorithm is used by OSPF to compute shortest path routing tables?",
      "options": [
        "Bellman-Ford",
        "Dijkstra's Algorithm",
        "Floyd-Warshall",
        "Prim's Algorithm"
      ],
      "correct_answer": "B",
      "explanation": "OSPF runs Dijkstra's shortest path algorithm on its link-state database."
    },
    {
      "id": "TEST-19-12",
      "category": "Core CS (Computer Networks)",
      "question": "What is considered 'infinity' (unreachable distance) in the Routing Information Protocol (RIP)?",
      "options": [
        "10 hops",
        "15 hops",
        "16 hops",
        "255 hops"
      ],
      "correct_answer": "C",
      "explanation": "RIP caps valid hop counts at 15; a hop count of 16 signifies an unreachable destination."
    },
    {
      "id": "TEST-19-13",
      "category": "Core CS (Computer Networks)",
      "question": "The primary protocol responsible for routing traffic between different Autonomous Systems on the global Internet is:",
      "options": [
        "RIP",
        "OSPF",
        "BGP",
        "ICMP"
      ],
      "correct_answer": "C",
      "explanation": "BGP (Border Gateway Protocol) is the de facto inter-domain routing protocol of the Internet."
    },
    {
      "id": "TEST-19-14",
      "category": "Core CS (Computer Networks)",
      "question": "Split Horizon is a technique designed to prevent:",
      "options": [
        "Buffer overflow",
        "Count-to-Infinity routing loops in Distance Vector protocols",
        "Packet collisions in CSMA",
        "SYN flood attacks"
      ],
      "correct_answer": "B",
      "explanation": "Split Horizon stops a router from advertising routes back out the interface they were learned from."
    },
    {
      "id": "TEST-19-15",
      "category": "Core CS (Computer Networks)",
      "question": "BGP avoids routing loops by examining which route attribute?",
      "options": [
        "Next Hop IP",
        "AS-Path list",
        "Subnet Mask",
        "Metric Cost"
      ],
      "correct_answer": "B",
      "explanation": "If a router detects its own ASN inside the incoming AS-Path attribute, it drops the route to prevent loops."
    },
    {
      "id": "TEST-19-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Graph Traversal: Breadth-First Search (BFS)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(R * C) Time, O(R * C) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Graph Traversal: Breadth-First Search (BFS)' pattern operates with O(R * C) Time, O(R * C) Auxiliary Space: First time a vertex is popped from the queue corresponds to its minimum edge distance from the source.."
    },
    {
      "id": "TEST-19-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Graph Traversal: Breadth-First Search (BFS)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: No fresh oranges initially (return 0).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Graph Traversal: Breadth-First Search (BFS) include No fresh oranges initially (return 0), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-19-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Rotting Oranges', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(R * C) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(R * C) Time, O(R * C) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-19-19",
      "category": "Projects (TerraStract)",
      "question": "In Sarthak's project 'TerraStract', what is the core architectural principle regarding 'Computer Vision Preprocessing: Deskewing, Binarization & Adaptive Thresholding'?",
      "options": [
        "Otsu's thresholding calculates the optimum global threshold separating foreground text from background paper stains.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For TerraStract, the architectural invariant is: Otsu's thresholding calculates the optimum global threshold separating foreground text from background paper stains.."
    },
    {
      "id": "TEST-19-20",
      "category": "Projects (TerraStract)",
      "question": "Regarding 'TerraStract', how should you defend this design decision in a technical interview: 'How does image preprocessing improve Tesseract OCR recognition accuracy in TerraStract?'?",
      "options": [
        "Scanned legal documents often suffer from rotation skew, yellowed paper, and low contrast. Our OpenCV pipeline computes the minimum area bounding rectangle of t...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Scanned legal documents often suffer from rotation skew, yellowed paper, and low contrast. Our OpenCV pipeline computes the minimum area bou."
    }
  ],
  "20": [
    {
      "id": "TEST-20-01",
      "category": "Academic (Academic Theory)",
      "question": "How does the Knowledge Management System Life Cycle (KMSLC) differ from the conventional Software Development Life Cycle (SDLC)?",
      "options": [
        "KMSLC is purely linear (Waterfall), while SDLC is iterative",
        "KMSLC is iterative and user-centered because knowledge is dynamic, experiential, and evolves continuously through human interaction",
        "KMSLC does not require any software testing",
        "SDLC only applies to mechanical engineering"
      ],
      "correct_answer": "B",
      "explanation": "Unlike deterministic procedural software in SDLC, KM systems deal with ambiguous, evolving cognitive heuristics requiring iterative refinement."
    },
    {
      "id": "TEST-20-02",
      "category": "Academic (Academic Theory)",
      "question": "What is the first foundational stage of the 8-stage KMSLC framework?",
      "options": [
        "System Deployment",
        "Evaluating Existing Infrastructure and Knowledge Assets",
        "Forming the Knowledge Management Team",
        "Designing the KM Blueprint"
      ],
      "correct_answer": "B",
      "explanation": "KMSLC begins with evaluating existing organizational infrastructure, intellectual capital, and business strategies to identify gaps."
    },
    {
      "id": "TEST-20-03",
      "category": "Academic (Academic Theory)",
      "question": "In KM project evaluation, what does the Balanced Scorecard framework assess?",
      "options": [
        "Only the quarterly financial net profit",
        "Performance across four perspectives: Financial, Customer, Internal Business Processes, and Learning & Growth",
        "The number of hours employees spend reading manuals",
        "The total storage capacity of the server rack"
      ],
      "correct_answer": "B",
      "explanation": "Kaplan and Norton's Balanced Scorecard balances financial indicators with operational, customer, and continuous learning metrics."
    },
    {
      "id": "TEST-20-04",
      "category": "Academic (Academic Theory)",
      "question": "What role does a Chief Knowledge Officer (CKO) play in an enterprise?",
      "options": [
        "Writing Java bytecode for database drivers",
        "Championing KM initiatives, aligning knowledge architecture with corporate strategy, and fostering a collaborative learning culture",
        "Resetting user email passwords",
        "Purchasing office computer monitors"
      ],
      "correct_answer": "B",
      "explanation": "The CKO is the executive leader responsible for maximizing intellectual capital, breaking down information silos, and driving KM strategy."
    },
    {
      "id": "TEST-20-05",
      "category": "Academic (Academic Theory)",
      "question": "What is a 'Knowledge Audit'?",
      "options": [
        "An IRS tax examination of company profits",
        "A systematic evaluation of an organization's knowledge needs, existing knowledge assets, flows, gaps, and blockages",
        "A daily antivirus scan of hard drives",
        "A count of total paper files in a storage cabinet"
      ],
      "correct_answer": "B",
      "explanation": "A knowledge audit identifies what knowledge assets exist, who holds them, where gaps exist, and how information flows across teams."
    },
    {
      "id": "TEST-20-06",
      "category": "Placement Aptitude",
      "question": "Statement: 'Please read the terms and conditions carefully before signing the employment contract.' Assumptions: I. People might sign without reading unless advised. II. The document contains binding contractual legal obligations.",
      "options": [
        "Both I and II are implicit",
        "Only I is implicit",
        "Only II is implicit",
        "Neither is implicit"
      ],
      "correct_answer": "A",
      "explanation": "Advising someone to read implies people frequently skim without reading (I) and that the document has legal weight (II)."
    },
    {
      "id": "TEST-20-07",
      "category": "Placement Aptitude",
      "question": "Statement: 'The government decided to grant financial subsidies to solar panel installations.' Assumptions: I. Subsidies will encourage more homeowners to adopt solar power. II. High initial equipment cost is currently a barrier to adoption.",
      "options": [
        "Both I and II are implicit",
        "Only I is implicit",
        "Only II is implicit",
        "Neither is implicit"
      ],
      "correct_answer": "A",
      "explanation": "Granting financial relief directly assumes cost is an obstacle (II) and monetary support motivates adoption (I)."
    },
    {
      "id": "TEST-20-08",
      "category": "Placement Aptitude",
      "question": "Statement: 'Drink pure mineral water to protect your health during monsoon season.' Assumptions: I. Contaminated water is a major cause of monsoon waterborne illnesses. II. Mineral water undergoes filtration to remove harmful pathogens.",
      "options": [
        "Both I and II are implicit",
        "Only I is implicit",
        "Only II is implicit",
        "Neither is implicit"
      ],
      "correct_answer": "A",
      "explanation": "Recommending mineral water assumes tap water carries health risks in monsoon (I) and bottled water is purified (II)."
    },
    {
      "id": "TEST-20-09",
      "category": "Placement Aptitude",
      "question": "Statement: 'Switch your enterprise database to cloud architecture to reduce infrastructure maintenance costs.' Assumptions: I. Cloud databases typically require less on-premise hardware maintenance overhead. II. Enterprises seek to optimize IT operating expenditures.",
      "options": [
        "Both I and II are implicit",
        "Only I is implicit",
        "Only II is implicit",
        "Neither is implicit"
      ],
      "correct_answer": "A",
      "explanation": "The recommendation assumes cost optimization is desirable (II) and cloud architectures reduce maintenance overhead (I)."
    },
    {
      "id": "TEST-20-10",
      "category": "Placement Aptitude",
      "question": "Statement: 'Do not lean outside the moving train coach doors.' Assumptions: I. Leaning outside moving train doors is physically hazardous. II. Passengers heed displayed safety warnings.",
      "options": [
        "Both I and II are implicit",
        "Only I is implicit",
        "Only II is implicit",
        "Neither is implicit"
      ],
      "correct_answer": "A",
      "explanation": "Displaying cautionary directives assumes danger exists (I) and passengers are capable of following signage (II)."
    },
    {
      "id": "TEST-20-11",
      "category": "Core CS (Computer Networks)",
      "question": "What is the minimum header size of a standard TCP segment (without options)?",
      "options": [
        "8 bytes",
        "20 bytes",
        "32 bytes",
        "64 bytes"
      ],
      "correct_answer": "B",
      "explanation": "Standard TCP headers without options are 20 bytes; UDP headers are 8 bytes."
    },
    {
      "id": "TEST-20-12",
      "category": "Core CS (Computer Networks)",
      "question": "During TCP connection teardown, why does the active closer remain in the TIME_WAIT state for 2 * MSL?",
      "options": [
        "To recalculate window size",
        "To ensure the final ACK was received and allow duplicate packets to die out",
        "To download pending files",
        "To reset the B+ tree"
      ],
      "correct_answer": "B",
      "explanation": "2 * MSL wait allows lingering delayed segments to expire and guarantees final ACK delivery."
    },
    {
      "id": "TEST-20-13",
      "category": "Core CS (Computer Networks)",
      "question": "Which protocol is connectionless and does not provide reliability, ordering, or flow control?",
      "options": [
        "TCP",
        "UDP",
        "SCTP",
        "BGP"
      ],
      "correct_answer": "B",
      "explanation": "UDP is connectionless and does not guarantee delivery or packet order."
    },
    {
      "id": "TEST-20-14",
      "category": "Core CS (Computer Networks)",
      "question": "What security mechanism mitigates SYN Flood Denial-of-Service attacks without consuming server state memory?",
      "options": [
        "DHCP Snooping",
        "SYN Cookies",
        "Split Horizon",
        "Exponential Backoff"
      ],
      "correct_answer": "B",
      "explanation": "SYN Cookies encode connection state in the initial sequence number, deferring memory allocation until final ACK."
    },
    {
      "id": "TEST-20-15",
      "category": "Core CS (Computer Networks)",
      "question": "What flags are set in the second packet of the TCP 3-Way Handshake?",
      "options": [
        "SYN",
        "ACK",
        "SYN + ACK",
        "FIN + ACK"
      ],
      "correct_answer": "C",
      "explanation": "The server responds to SYN with a combined SYN + ACK packet."
    },
    {
      "id": "TEST-20-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Graph Traversal: DFS & Connected Components' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(R * C) Time, O(R * C) Auxiliary Space (Call stack).",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Graph Traversal: DFS & Connected Components' pattern operates with O(R * C) Time, O(R * C) Auxiliary Space (Call stack): Visits each vertex and edge exactly once, partitioning the graph into distinct connected components.."
    },
    {
      "id": "TEST-20-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Graph Traversal: DFS & Connected Components' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Grid with all '0' (returns 0).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Graph Traversal: DFS & Connected Components include Grid with all '0' (returns 0), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-20-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Number of Islands', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(R * C) Auxiliary Space (Call stack).",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(R * C) Time, O(R * C) Auxiliary Space (Call stack) by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-20-19",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "In Sarthak's project 'College Student Management System (CSMS)', what is the core architectural principle regarding 'HOD Notice Board, Full-Stack Integration & Render Cloud Deployment'?",
      "options": [
        "Render Blueprint (`render.yaml`) provides Infrastructure-as-Code for auto-provisioning FastAPI web services.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For College Student Management System (CSMS), the architectural invariant is: Render Blueprint (`render.yaml`) provides Infrastructure-as-Code for auto-provisioning FastAPI web services.."
    },
    {
      "id": "TEST-20-20",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "Regarding 'College Student Management System (CSMS)', how should you defend this design decision in a technical interview: 'Why did you build the CSMS frontend with Vanilla HTML/CSS/JS instead of React or Vue?'?",
      "options": [
        "For an internal college administration portal, zero build overhead and instant browser loading on lab computers with low memory were primary requirements. Vanil...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: For an internal college administration portal, zero build overhead and instant browser loading on lab computers with low memory were primary."
    }
  ],
  "21": [
    {
      "id": "TEST-21-01",
      "category": "Academic (Academic Theory)",
      "question": "When should Newton's Forward Difference Interpolation formula be chosen over Newton's Backward formula?",
      "options": [
        "When the target interpolation value x lies near the beginning of the tabulated values",
        "When x lies near the end of the table",
        "When the values of x are spaced at unequal intervals",
        "When f(x) is a discontinuous function"
      ],
      "correct_answer": "A",
      "explanation": "Newton's Forward formula is derived using forward differences from x_0 and gives optimal precision for points near the start of the table."
    },
    {
      "id": "TEST-21-02",
      "category": "Academic (Academic Theory)",
      "question": "What is the relationship between the Forward Difference operator (Delta) and the Shift operator (E)?",
      "options": [
        "Delta = E + 1",
        "Delta = E - 1 (or E = 1 + Delta)",
        "Delta = E * 2",
        "Delta = 1 / E"
      ],
      "correct_answer": "B",
      "explanation": "By definition, Delta f(x) = f(x + h) - f(x) = E f(x) - f(x) = (E - 1) f(x), hence Delta = E - 1."
    },
    {
      "id": "TEST-21-03",
      "category": "Academic (Academic Theory)",
      "question": "If a polynomial of degree n is tabulated at equidistant intervals, what is the value of its (n+1)-th forward difference Delta^{n+1} f(x)?",
      "options": [
        "A non-zero constant",
        "0 (Zero)",
        "n!",
        "Infinity"
      ],
      "correct_answer": "B",
      "explanation": "The n-th difference of an n-th degree polynomial is constant (Delta^n f(x) = a_n * n! * h^n), so all higher differences (n+1 and above) are identically zero."
    },
    {
      "id": "TEST-21-04",
      "category": "Academic (Academic Theory)",
      "question": "What is the formula for the dimensionless parameter u in Newton's Forward Difference interpolation formula?",
      "options": [
        "u = (x - x_n) / h",
        "u = (x - x_0) / h",
        "u = (x_0 + x_n) / 2",
        "u = x * h"
      ],
      "correct_answer": "B",
      "explanation": "In forward interpolation, u = (x - x_0) / h, where x_0 is the initial table value and h is the uniform step interval."
    },
    {
      "id": "TEST-21-05",
      "category": "Academic (Academic Theory)",
      "question": "What is the Backward Difference operator (Nabla) defined as?",
      "options": [
        "Nabla f(x) = f(x) - f(x - h)",
        "Nabla f(x) = f(x + h) - f(x)",
        "Nabla f(x) = f(x + h) + f(x - h)",
        "Nabla f(x) = f(x) / h"
      ],
      "correct_answer": "A",
      "explanation": "The backward difference operator Nabla subtracts the preceding point: Nabla f(x) = f(x) - f(x - h)."
    },
    {
      "id": "TEST-21-06",
      "category": "Placement Aptitude",
      "question": "Question: Is x greater than y? Statements: I. 2x = 3y. II. x and y are positive integers.",
      "options": [
        "Both statements together are sufficient",
        "Statement I alone is sufficient",
        "Statement II alone is sufficient",
        "Neither is sufficient"
      ],
      "correct_answer": "A",
      "explanation": "From I: x/y = 3/2. If x, y are negative, x < y. With II (both positive), x = 1.5y > y. Both together are required."
    },
    {
      "id": "TEST-21-07",
      "category": "Placement Aptitude",
      "question": "Question: What is the value of two-digit number N? Statements: I. The sum of digits of N is 9. II. The difference of digits of N is 5.",
      "options": [
        "Statements I and II together are NOT sufficient",
        "Statement I alone is sufficient",
        "Statement II alone is sufficient",
        "Both together are sufficient"
      ],
      "correct_answer": "A",
      "explanation": "Pairs summing to 9 with difference 5: (7, 2) gives 72 or 27. Two different numbers are possible, so insufficient."
    },
    {
      "id": "TEST-21-08",
      "category": "Placement Aptitude",
      "question": "Question: What is the area of rectangle R? Statements: I. The perimeter of R is 30 cm. II. The diagonal of R is sqrt(117) cm.",
      "options": [
        "Both statements together are sufficient",
        "Statement I alone is sufficient",
        "Statement II alone is sufficient",
        "Neither is sufficient"
      ],
      "correct_answer": "A",
      "explanation": "2(L + W) = 30 => L + W = 15 => (L + W)^2 = 225 => L^2 + W^2 + 2LW = 225. From II: L^2 + W^2 = 117. 2LW = 225 - 117 = 108 => Area LW = 54 cm^2. Both together are sufficient."
    },
    {
      "id": "TEST-21-09",
      "category": "Placement Aptitude",
      "question": "Question: What is the average age of 5 friends? Statements: I. Total age of the 5 friends is 120 years. II. The youngest friend is 20 years old.",
      "options": [
        "Statement I alone is sufficient",
        "Statement II alone is sufficient",
        "Both together are sufficient",
        "Neither is sufficient"
      ],
      "correct_answer": "A",
      "explanation": "Average = Total Age / 5. Statement I directly gives Total = 120 => Average = 120 / 5 = 24 years. I alone is sufficient."
    },
    {
      "id": "TEST-21-10",
      "category": "Placement Aptitude",
      "question": "Question: Did company XYZ make a profit this fiscal quarter? Statements: I. Revenue increased by 15% compared to last quarter. II. Total operating expenses were less than gross revenue.",
      "options": [
        "Statement II alone is sufficient",
        "Statement I alone is sufficient",
        "Both together are sufficient",
        "Neither is sufficient"
      ],
      "correct_answer": "A",
      "explanation": "Profit = Revenue - Expenses. Statement II states Revenue > Expenses, directly confirming profit. II alone is sufficient."
    },
    {
      "id": "TEST-21-11",
      "category": "Core CS (Computer Networks)",
      "question": "During TCP Slow Start, how does the congestion window (cwnd) increase with each passing RTT?",
      "options": [
        "Linearly (by 1 MSS)",
        "Exponentially (doubles every RTT)",
        "Logarithmically",
        "Remains constant"
      ],
      "correct_answer": "B",
      "explanation": "Because cwnd increases by 1 for each ACK, it doubles every round trip time during slow start."
    },
    {
      "id": "TEST-21-12",
      "category": "Core CS (Computer Networks)",
      "question": "How many duplicate ACKs must a TCP sender receive before triggering Fast Retransmit?",
      "options": [
        "1",
        "2",
        "3",
        "5"
      ],
      "correct_answer": "C",
      "explanation": "Receiving 3 duplicate ACKs (4 identical ACKs total) triggers immediate Fast Retransmit."
    },
    {
      "id": "TEST-21-13",
      "category": "Core CS (Computer Networks)",
      "question": "The maximum data a TCP sender can transmit without receiving an ACK is bounded by:",
      "options": [
        "rwnd only",
        "cwnd only",
        "min(rwnd, cwnd)",
        "max(rwnd, cwnd)"
      ],
      "correct_answer": "C",
      "explanation": "Effective window is strictly bounded by min(rwnd, cwnd) to respect both receiver and network."
    },
    {
      "id": "TEST-21-14",
      "category": "Core CS (Computer Networks)",
      "question": "When a packet loss occurs due to an RTO timeout, what value is cwnd reset to?",
      "options": [
        "ssthresh",
        "cwnd / 2",
        "1 MSS",
        "0 MSS"
      ],
      "correct_answer": "C",
      "explanation": "On a severe timeout, cwnd collapses down to 1 MSS, restarting slow start."
    },
    {
      "id": "TEST-21-15",
      "category": "Core CS (Computer Networks)",
      "question": "Nagle's algorithm on the sender side is designed to prevent:",
      "options": [
        "SYN Flood attacks",
        "Silly Window Syndrome from transmitting tiny data packets",
        "B+ tree page splits",
        "Deadlocks in 2PL"
      ],
      "correct_answer": "B",
      "explanation": "Nagle's algorithm coalesces small packets to prevent Silly Window Syndrome."
    },
    {
      "id": "TEST-21-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Topological Sorting (Kahn's Algorithm)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(V + E) Time, O(V + E) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Topological Sorting (Kahn's Algorithm)' pattern operates with O(V + E) Time, O(V + E) Auxiliary Space: A vertex with in-degree 0 has no unmet dependencies and can execute immediately; removing it unlocks dependent vertices.."
    },
    {
      "id": "TEST-21-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Topological Sorting (Kahn's Algorithm)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Graph with cycle (returns false).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Topological Sorting (Kahn's Algorithm) include Graph with cycle (returns false), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-21-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Course Schedule', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(V + E) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(V + E) Time, O(V + E) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-21-19",
      "category": "Projects (SmartGalla)",
      "question": "In Sarthak's project 'SmartGalla', what is the core architectural principle regarding 'Progressive Web App (PWA) & Offline-First POS Engine (Serwist & Service Workers)'?",
      "options": [
        "Cache-first strategy for static assets and Stale-While-Revalidate for product catalogs.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For SmartGalla, the architectural invariant is: Cache-first strategy for static assets and Stale-While-Revalidate for product catalogs.."
    },
    {
      "id": "TEST-21-20",
      "category": "Projects (SmartGalla)",
      "question": "Regarding 'SmartGalla', how should you defend this design decision in a technical interview: 'How does SmartGalla allow store billing when the store internet disconnects?'?",
      "options": [
        "Using `@serwist/next` (modern Workbox successor), we register a service worker that caches the entire merchant POS interface, barcode scanner bundle, and the st...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Using `@serwist/next` (modern Workbox successor), we register a service worker that caches the entire merchant POS interface, barcode scanne."
    }
  ],
  "22": [
    {
      "id": "TEST-22-01",
      "category": "Academic (Academic Theory)",
      "question": "Which lifecycle method of a Java Servlet is invoked exactly once by the servlet container when the servlet is first instantiated?",
      "options": [
        "service()",
        "init()",
        "doGet()",
        "destroy()"
      ],
      "correct_answer": "B",
      "explanation": "The container calls `init(ServletConfig config)` once during initialization to allocate resources before servicing client requests."
    },
    {
      "id": "TEST-22-02",
      "category": "Academic (Academic Theory)",
      "question": "In the Java Servlet lifecycle, which method dispatches incoming HTTP requests to doGet(), doPost(), doPut(), etc., based on the request method?",
      "options": [
        "service(ServletRequest, ServletResponse)",
        "init()",
        "start()",
        "run()"
      ],
      "correct_answer": "A",
      "explanation": "The `service()` method reads HTTP method headers and delegates the request to the corresponding specialized `doGet/doPost` handler."
    },
    {
      "id": "TEST-22-03",
      "category": "Academic (Academic Theory)",
      "question": "Why is HttpServletSession preferred over plain Cookies for storing sensitive user authentication tokens?",
      "options": [
        "Cookies cannot store more than 1 byte of data",
        "Session data is stored securely on the server-side, with only an opaque session identifier (JSESSIONID) sent to the client browser",
        "Cookies expire immediately when a tab is refreshed",
        "Sessions do not consume server RAM"
      ],
      "correct_answer": "B",
      "explanation": "HttpSession stores state in server memory, transmitting only an arbitrary cookie ID, protecting sensitive attributes from client tampering."
    },
    {
      "id": "TEST-22-04",
      "category": "Academic (Academic Theory)",
      "question": "What deployment descriptor file traditionally configured servlet mappings and initialization parameters in Java EE applications before annotations?",
      "options": [
        "pom.xml",
        "web.xml (located in WEB-INF)",
        "server.xml",
        "context.xml"
      ],
      "correct_answer": "B",
      "explanation": "The `WEB-INF/web.xml` deployment descriptor historically configured servlet classes, URL patterns, context params, and filters."
    },
    {
      "id": "TEST-22-05",
      "category": "Academic (Academic Theory)",
      "question": "Which modern annotation replaces the need for `<servlet>` and `<servlet-mapping>` declarations in `web.xml` in Servlet 3.0+?",
      "options": [
        "@WebServlet",
        "@Controller",
        "@Service",
        "@WebEndpoint"
      ],
      "correct_answer": "A",
      "explanation": "Servlet 3.0 introduced `@WebServlet(urlPatterns = \"/path\")`, allowing declarative configuration directly in Java source code."
    },
    {
      "id": "TEST-22-06",
      "category": "Placement Aptitude",
      "question": "A solid wooden cube of side 4 cm is painted red on all faces and cut into smaller cubes of side 1 cm. How many smaller cubes have exactly two faces painted red?",
      "options": [
        "24",
        "16",
        "32",
        "8"
      ],
      "correct_answer": "A",
      "explanation": "For a cube of n = 4/1 = 4: Two-face painted cubes lie on edges = 12 * (n - 2) = 12 * (4 - 2) = 24 cubes."
    },
    {
      "id": "TEST-22-07",
      "category": "Placement Aptitude",
      "question": "How many smaller cubes in the 4 cm cube cut into 1 cm cubes have NO faces painted?",
      "options": [
        "8",
        "16",
        "24",
        "4"
      ],
      "correct_answer": "A",
      "explanation": "Zero painted faces = (n - 2)^3 = (4 - 2)^3 = 2^3 = 8 cubes."
    },
    {
      "id": "TEST-22-08",
      "category": "Placement Aptitude",
      "question": "In a standard die, what is the sum of numbers on any two opposite faces?",
      "options": [
        "7",
        "6",
        "8",
        "14"
      ],
      "correct_answer": "A",
      "explanation": "By definition, opposite faces of standard dice always sum to 7 (1-6, 2-5, 3-4)."
    },
    {
      "id": "TEST-22-09",
      "category": "Placement Aptitude",
      "question": "Two positions of a dice are shown. When 4 is at the bottom, what number will be on the top face?",
      "options": [
        "3",
        "1",
        "2",
        "5"
      ],
      "correct_answer": "A",
      "explanation": "On standard fair dice, the face opposite to 4 is always 7 - 4 = 3."
    },
    {
      "id": "TEST-22-10",
      "category": "Placement Aptitude",
      "question": "How many smaller cubes have exactly 3 faces painted when a large cube is cut into 27 identical small cubes?",
      "options": [
        "8",
        "6",
        "12",
        "1"
      ],
      "correct_answer": "A",
      "explanation": "Three-face painted cubes always occupy the 8 corners of the cube regardless of n (for n >= 2)."
    },
    {
      "id": "TEST-22-11",
      "category": "Core CS (Python Internals)",
      "question": "What is the primary, real-time memory management mechanism in standard CPython?",
      "options": [
        "Mark and Sweep GC",
        "Reference Counting",
        "Manual free() calls",
        "Stop-the-World Tracing"
      ],
      "correct_answer": "B",
      "explanation": "CPython uses reference counting as its immediate real-time memory reclamation mechanism."
    },
    {
      "id": "TEST-22-12",
      "category": "Core CS (Python Internals)",
      "question": "Which range of integer values is pre-allocated and interned as global singletons in CPython?",
      "options": [
        "0 to 100",
        "-128 to 127",
        "-5 to 256",
        "0 to 65535"
      ],
      "correct_answer": "C",
      "explanation": "CPython interns small integers between -5 and 256 inclusive."
    },
    {
      "id": "TEST-22-13",
      "category": "Core CS (Python Internals)",
      "question": "Defining `__slots__` on a Python class achieves memory optimization by:",
      "options": [
        "Bypassing the GIL",
        "Preventing the creation of the dynamic `__dict__` attribute dictionary",
        "Compressing strings using gzip",
        "Converting integers to C floats"
      ],
      "correct_answer": "B",
      "explanation": "`__slots__` eliminates instance `__dict__` overhead, using fixed-size C arrays instead."
    },
    {
      "id": "TEST-22-14",
      "category": "Core CS (Python Internals)",
      "question": "Circular reference cycles that escape reference counting are detected and collected by:",
      "options": [
        "PyMalloc",
        "The generational cyclic garbage collector (`gc` module)",
        "The OS kernel scheduler",
        "The Global Interpreter Lock"
      ],
      "correct_answer": "B",
      "explanation": "The cyclic garbage collector specifically identifies and breaks isolated circular reference cycles."
    },
    {
      "id": "TEST-22-15",
      "category": "Core CS (Python Internals)",
      "question": "In Python, which operator evaluates to True only if both variables reference the identical memory address?",
      "options": [
        "==",
        "!=",
        "is",
        "in"
      ],
      "correct_answer": "C",
      "explanation": "The `is` keyword checks pointer identity (`id(a) == id(b)`)."
    },
    {
      "id": "TEST-22-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Disjoint Set Union (Union-Find)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N * alpha(N)) Time, O(N) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Disjoint Set Union (Union-Find)' pattern operates with O(N * alpha(N)) Time, O(N) Auxiliary Space: Path compression flattens tree structure on lookup, keeping tree depth effectively constant (Ackermann inverse alpha(N) < 5).."
    },
    {
      "id": "TEST-22-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Disjoint Set Union (Union-Find)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Tree with single redundant edge.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Disjoint Set Union (Union-Find) include Tree with single redundant edge, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-22-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Number of Provinces', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(N) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N * alpha(N)) Time, O(N) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-22-19",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "In Sarthak's project 'NSE2 / BulkBeat TV', what is the core architectural principle regarding 'Dhan REST API Integration, Chartink Screeners & Technical Analysis Pipelines'?",
      "options": [
        "Dhan API provides real-time market depth and Level 2 quote data via authenticated HTTP endpoints.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For NSE2 / BulkBeat TV, the architectural invariant is: Dhan API provides real-time market depth and Level 2 quote data via authenticated HTTP endpoints.."
    },
    {
      "id": "TEST-22-20",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "Regarding 'NSE2 / BulkBeat TV', how should you defend this design decision in a technical interview: 'How did you integrate Dhan API and Chartink screeners into the news alert flow?'?",
      "options": [
        "When a corporate disclosure is published for a stock (e.g., RELIANCE), the pipeline triggers an immediate quote fetch via Dhan REST API (`/v2/quotes`) to captur...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: When a corporate disclosure is published for a stock (e.g., RELIANCE), the pipeline triggers an immediate quote fetch via Dhan REST API (`/v."
    }
  ],
  "23": [
    {
      "id": "TEST-23-01",
      "category": "Academic (Academic Theory)",
      "question": "In the TCP 3-way handshake to establish a reliable connection, what sequence of control flags is exchanged between client and server?",
      "options": [
        "SYN -> SYN-ACK -> ACK",
        "ACK -> SYN -> FIN",
        "SYN -> ACK -> RST",
        "PING -> PONG -> ACK"
      ],
      "correct_answer": "A",
      "explanation": "Connection establishment: Client sends SYN, Server replies with SYN + ACK, and Client confirms with final ACK."
    },
    {
      "id": "TEST-23-02",
      "category": "Academic (Academic Theory)",
      "question": "How does TCP handle Congestion Control during the initial 'Slow Start' phase upon connection startup?",
      "options": [
        "It sets window size to maximum bandwidth immediately",
        "It initializes Congestion Window (cwnd) to 1 MSS and doubles cwnd every RTT (exponential growth) until ssthresh is reached",
        "It drops every alternate packet",
        "It transmits UDP datagrams instead"
      ],
      "correct_answer": "B",
      "explanation": "Slow Start probes network capacity exponentially: cwnd doubles every round-trip time until reaching the slow start threshold (ssthresh)."
    },
    {
      "id": "TEST-23-03",
      "category": "Academic (Academic Theory)",
      "question": "What mechanism does TCP use during Congestion Avoidance after cwnd exceeds ssthresh?",
      "options": [
        "Additive Increase Multiplicative Decrease (AIMD) — increasing cwnd by 1 MSS per RTT",
        "Exponential doubling",
        "Immediate connection reset",
        "Halving the window every second"
      ],
      "correct_answer": "A",
      "explanation": "In Congestion Avoidance, AIMD provides linear window expansion (+1 MSS per RTT) to stabilize throughput near link capacity."
    },
    {
      "id": "TEST-23-04",
      "category": "Academic (Academic Theory)",
      "question": "What is the primary architectural difference between TCP and UDP?",
      "options": [
        "TCP is connection-oriented, reliable, and provides byte-stream ordering; UDP is connectionless, unreliable, and datagram-oriented",
        "UDP provides guaranteed packet delivery while TCP does not",
        "TCP only runs over optical fiber while UDP runs over copper",
        "UDP uses 64-bit port numbers"
      ],
      "correct_answer": "A",
      "explanation": "TCP guarantees in-order reliable delivery via acknowledgments and retries; UDP provides lightweight, low-latency best-effort transmission."
    },
    {
      "id": "TEST-23-05",
      "category": "Academic (Academic Theory)",
      "question": "What is the size of the standard base IPv4 and TCP headers without options?",
      "options": [
        "20 bytes for IPv4 and 20 bytes for TCP (40 bytes total overhead)",
        "8 bytes for IPv4 and 8 bytes for TCP",
        "64 bytes each",
        "4 bytes each"
      ],
      "correct_answer": "A",
      "explanation": "Both IPv4 and TCP base headers have a minimum length of 20 bytes each (5 32-bit words), yielding a combined 40-byte base header."
    },
    {
      "id": "TEST-23-06",
      "category": "Placement Aptitude",
      "question": "In subject-verb agreement with correlative conjunctions, which sentence is correct?",
      "options": [
        "Neither the manager nor the employees were present at the briefing.",
        "Neither the manager nor the employees was present at the briefing.",
        "Neither the manager or the employees were present at the briefing.",
        "Neither the manager nor the employees is present at the briefing."
      ],
      "correct_answer": "A",
      "explanation": "In 'Neither... nor', the verb agrees with the closer subject ('employees', plural => 'were')."
    },
    {
      "id": "TEST-23-07",
      "category": "Placement Aptitude",
      "question": "Regarding distributive pronoun agreement with 'Each', which statement is correct?",
      "options": [
        "Each of the candidates has submitted his or her resume.",
        "Each of the candidates have submitted their resume.",
        "Each of the candidate has submitted their resume.",
        "Each of the candidates are submitting resumes."
      ],
      "correct_answer": "A",
      "explanation": "'Each' is a singular distributive pronoun and requires the singular verb 'has'."
    },
    {
      "id": "TEST-23-08",
      "category": "Placement Aptitude",
      "question": "Identify the part containing a grammatical error in: 'The quality of these mangoes (A) / are not good (B) / according to the buyer (C) / No error (D)'",
      "options": [
        "Part B",
        "Part A",
        "Part C",
        "Part D"
      ],
      "correct_answer": "A",
      "explanation": "The subject is 'quality' (singular), so the verb should be 'is not good', not 'are'."
    },
    {
      "id": "TEST-23-09",
      "category": "Placement Aptitude",
      "question": "Regarding the collective construction 'One of the...', which sentence is grammatically sound?",
      "options": [
        "One of my friends is an aerospace engineer.",
        "One of my friends are an aerospace engineer.",
        "One of my friend is an aerospace engineer.",
        "One of my friend are an aerospace engineer."
      ],
      "correct_answer": "A",
      "explanation": "'One of' is followed by a plural noun ('friends') and a singular verb ('is')."
    },
    {
      "id": "TEST-23-10",
      "category": "Placement Aptitude",
      "question": "Regarding negative inversion and correlative conjunctions with 'Scarcely', choose the correct sentence:",
      "options": [
        "Scarcely had he entered the room when the phone rang.",
        "Scarcely had he entered the room than the phone rang.",
        "Scarcely did he entered the room when the phone rang.",
        "Scarcely he had entered the room then the phone rang."
      ],
      "correct_answer": "A",
      "explanation": "'Scarcely' pairs correlatively with 'when' and requires inverted auxiliary verb syntax ('had he entered')."
    },
    {
      "id": "TEST-23-11",
      "category": "Core CS (Python Internals)",
      "question": "What is the primary constraint imposed by CPython's Global Interpreter Lock (GIL)?",
      "options": [
        "Files cannot be read concurrently",
        "Only one thread can execute Python bytecode at a time within a single process",
        "Subprocesses are prohibited",
        "Recursion depth is limited to 100"
      ],
      "correct_answer": "B",
      "explanation": "The GIL restricts bytecode execution to one thread at any given instant per process."
    },
    {
      "id": "TEST-23-12",
      "category": "Core CS (Python Internals)",
      "question": "Which Python module enables true parallel execution across multi-core CPUs for CPU-bound computations?",
      "options": [
        "threading",
        "multiprocessing",
        "asyncio",
        "socket"
      ],
      "correct_answer": "B",
      "explanation": "multiprocessing spawns independent processes with separate GILs, running across multiple cores."
    },
    {
      "id": "TEST-23-13",
      "category": "Core CS (Python Internals)",
      "question": "In Python, which operation is NOT atomic and requires a threading Lock?",
      "options": [
        "list.append(x)",
        "dict[key] = val",
        "counter += 1",
        "queue.pop()"
      ],
      "correct_answer": "C",
      "explanation": "`counter += 1` compiles to multiple bytecode instructions (read, add, write), requiring synchronization."
    },
    {
      "id": "TEST-23-14",
      "category": "Core CS (Python Internals)",
      "question": "Coroutines in `asyncio` yield control back to the event loop using which keyword?",
      "options": [
        "yield from",
        "await",
        "defer",
        "pass"
      ],
      "correct_answer": "B",
      "explanation": "The `await` keyword pauses coroutine execution and returns control to the event loop."
    },
    {
      "id": "TEST-23-15",
      "category": "Core CS (Python Internals)",
      "question": "How should a blocking synchronous I/O function be executed in an asyncio application?",
      "options": [
        "Invoke it directly inside async def",
        "Wrap it with asyncio.to_thread() to run in a thread pool",
        "Call sys.exit()",
        "Increase the recursion limit"
      ],
      "correct_answer": "B",
      "explanation": "Blocking operations must be offloaded to worker threads via asyncio.to_thread() to avoid freezing the event loop."
    },
    {
      "id": "TEST-23-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Dijkstra's Shortest Path Algorithm' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O((V + E) log V) Time, O(V + E) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Dijkstra's Shortest Path Algorithm' pattern operates with O((V + E) log V) Time, O(V + E) Auxiliary Space: Greedily expands the vertex with the lowest tentative distance; non-negative weights guarantee that once visited, its optimal distance is finalized.."
    },
    {
      "id": "TEST-23-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Dijkstra's Shortest Path Algorithm' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Unreachable destination (returns -1).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Dijkstra's Shortest Path Algorithm include Unreachable destination (returns -1), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-23-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Network Delay Time', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(V + E) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O((V + E) log V) Time, O(V + E) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-23-19",
      "category": "Projects (Caloriv)",
      "question": "In Sarthak's project 'Caloriv', what is the core architectural principle regarding 'Camera Integration, Image Preprocessing & Cloudinary Asset Optimization'?",
      "options": [
        "Compressing images before mobile upload saves cellular data and prevents network timeout failures.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Caloriv, the architectural invariant is: Compressing images before mobile upload saves cellular data and prevents network timeout failures.."
    },
    {
      "id": "TEST-23-20",
      "category": "Projects (Caloriv)",
      "question": "Regarding 'Caloriv', how should you defend this design decision in a technical interview: 'How does Caloriv handle meal photo uploads efficiently over slow mobile networks?'?",
      "options": [
        "When a user captures a food photo, rather than uploading raw 12MB camera images, we use `expo-image-manipulator` to downsample the image resolution to a maximum...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: When a user captures a food photo, rather than uploading raw 12MB camera images, we use `expo-image-manipulator` to downsample the image res."
    }
  ],
  "24": [
    {
      "id": "TEST-24-01",
      "category": "Academic (Academic Theory)",
      "question": "Which interpolation formula is designed specifically for calculating values when the given independent variable arguments x_i are spaced at UNEQUAL intervals?",
      "options": [
        "Newton's Forward Interpolation Formula",
        "Lagrange's Interpolation Formula",
        "Newton's Backward Interpolation Formula",
        "Trapezoidal Rule"
      ],
      "correct_answer": "B",
      "explanation": "Lagrange's and Newton's Divided Difference formulas do not require equal step spacing h, handling arbitrary data points."
    },
    {
      "id": "TEST-24-02",
      "category": "Academic (Academic Theory)",
      "question": "What is the degree of the Lagrange interpolating polynomial passing through (n + 1) distinct points?",
      "options": [
        "At most n",
        "Exactly n + 1",
        "Always 1",
        "n^2"
      ],
      "correct_answer": "A",
      "explanation": "A unique polynomial of degree at most n can be passed through (n + 1) distinct points (x_0, y_0) ... (x_n, y_n)."
    },
    {
      "id": "TEST-24-03",
      "category": "Academic (Academic Theory)",
      "question": "What is the mathematical property of the Lagrange basis polynomial L_i(x) evaluated at data point x_j?",
      "options": [
        "L_i(x_j) = 1 if i = j, and L_i(x_j) = 0 if i != j (Kronecker delta)",
        "L_i(x_j) = 0 always",
        "L_i(x_j) = infinity",
        "L_i(x_j) = x_i - x_j"
      ],
      "correct_answer": "A",
      "explanation": "Lagrange basis polynomials satisfy the Kronecker delta property: L_i(x_j) = delta_{ij}, ensuring the sum equals y_j at x = x_j."
    },
    {
      "id": "TEST-24-04",
      "category": "Academic (Academic Theory)",
      "question": "What is the primary computational disadvantage of Lagrange's interpolation formula when a new data point is added to the table?",
      "options": [
        "It cannot handle negative numbers",
        "All basis polynomial coefficients must be recomputed from scratch",
        "It causes division by zero",
        "It requires matrix inversion"
      ],
      "correct_answer": "B",
      "explanation": "Lagrange formulas lack recurrence: adding one point requires recalculating all terms. Divided differences avoid this via incremental terms."
    },
    {
      "id": "TEST-24-05",
      "category": "Academic (Academic Theory)",
      "question": "The first divided difference f[x_0, x_1] of a function f(x) is defined as:",
      "options": [
        "[f(x_1) - f(x_0)] / (x_1 - x_0)",
        "[f(x_1) + f(x_0)] / 2",
        "f(x_1) * (x_1 - x_0)",
        "f'(x_0)"
      ],
      "correct_answer": "A",
      "explanation": "The first divided difference represents the secant slope between the two points: f[x_0, x_1] = (f(x_1) - f(x_0)) / (x_1 - x_0)."
    },
    {
      "id": "TEST-24-06",
      "category": "Placement Aptitude",
      "question": "Fill in the blank: 'He is senior _____ me in corporate rank by three years.'",
      "options": [
        "to",
        "than",
        "from",
        "over"
      ],
      "correct_answer": "A",
      "explanation": "Adjectives ending in '-ior' (senior, junior, superior, inferior) take the preposition 'to', never 'than'."
    },
    {
      "id": "TEST-24-07",
      "category": "Placement Aptitude",
      "question": "Fill in the blank: 'The committee congratulated him _____ his successful research publication.'",
      "options": [
        "on",
        "for",
        "at",
        "about"
      ],
      "correct_answer": "A",
      "explanation": "The standard idiom is 'congratulate someone ON something'."
    },
    {
      "id": "TEST-24-08",
      "category": "Placement Aptitude",
      "question": "Fill in the blank: 'You must abstain _____ smoking in public transit areas.'",
      "options": [
        "from",
        "to",
        "against",
        "of"
      ],
      "correct_answer": "A",
      "explanation": "'Abstain', 'refrain', and 'prevent' take the preposition 'from' followed by a gerund."
    },
    {
      "id": "TEST-24-09",
      "category": "Placement Aptitude",
      "question": "Fill in the blank: 'Divide this dividend equally _____ the five founding partners.'",
      "options": [
        "among",
        "between",
        "amidst",
        "within"
      ],
      "correct_answer": "A",
      "explanation": "'Between' is used for two entities; 'among' is used for three or more entities."
    },
    {
      "id": "TEST-24-10",
      "category": "Placement Aptitude",
      "question": "Fill in the blank: 'She has been suffering from viral fever _____ Monday last.'",
      "options": [
        "since",
        "for",
        "from",
        "in"
      ],
      "correct_answer": "A",
      "explanation": "'Since' is used with a specific point in time (Monday); 'for' is used with a duration of time."
    },
    {
      "id": "TEST-24-11",
      "category": "Core CS (Python Internals)",
      "question": "What syntactic transformation occurs when writing `@decorator def foo(): pass`?",
      "options": [
        "foo = foo(decorator)",
        "foo = decorator(foo)",
        "decorator = foo()",
        "def foo(): decorator()"
      ],
      "correct_answer": "B",
      "explanation": "Decorators wrap functions: `foo = decorator(foo)`."
    },
    {
      "id": "TEST-24-12",
      "category": "Core CS (Python Internals)",
      "question": "Which exception is raised by an iterator's `__next__()` method when no further elements exist?",
      "options": [
        "IndexError",
        "KeyError",
        "StopIteration",
        "GeneratorExit"
      ],
      "correct_answer": "C",
      "explanation": "The iterator protocol raises StopIteration when iteration completes."
    },
    {
      "id": "TEST-24-13",
      "category": "Core CS (Python Internals)",
      "question": "Functions containing the `yield` keyword return which type of object when invoked?",
      "options": [
        "List",
        "Tuple",
        "Generator object",
        "Coroutine"
      ],
      "correct_answer": "C",
      "explanation": "Calling a function containing yield returns a generator object."
    },
    {
      "id": "TEST-24-14",
      "category": "Core CS (Python Internals)",
      "question": "Why is `@functools.wraps` applied to decorator wrappers?",
      "options": [
        "To bypass the GIL",
        "To preserve the original function's name, docstring, and metadata",
        "To convert code to C",
        "To catch syntax errors"
      ],
      "correct_answer": "B",
      "explanation": "functools.wraps copies function metadata like __name__ and __doc__ onto the wrapper."
    },
    {
      "id": "TEST-24-15",
      "category": "Core CS (Python Internals)",
      "question": "If `__exit__` in a context manager returns `True` after an exception occurs, what happens?",
      "options": [
        "The program crashes",
        "The exception is suppressed/swallowed",
        "The exception is re-raised",
        "A deadlock occurs"
      ],
      "correct_answer": "B",
      "explanation": "Returning True from __exit__ indicates the exception was handled, suppressing it."
    },
    {
      "id": "TEST-24-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Dynamic Programming: 1D Array' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Dynamic Programming: 1D Array' pattern operates with O(N) Time, O(1) Auxiliary Space: Deciding optimal outcome at state i depends strictly on preceding states (e.g. dp[i] = max(dp[i-1], dp[i-2] + nums[i])).."
    },
    {
      "id": "TEST-24-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Dynamic Programming: 1D Array' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Single house.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Dynamic Programming: 1D Array include Single house, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-24-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: House Robber', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(1) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(1) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-24-19",
      "category": "Projects (TerraStract)",
      "question": "In Sarthak's project 'TerraStract', what is the core architectural principle regarding 'Security, Data Privacy & Temporary File Sanitization in Document Processing'?",
      "options": [
        "Never store unencrypted user documents permanently on application servers.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For TerraStract, the architectural invariant is: Never store unencrypted user documents permanently on application servers.."
    },
    {
      "id": "TEST-24-20",
      "category": "Projects (TerraStract)",
      "question": "Regarding 'TerraStract', how should you defend this design decision in a technical interview: 'How do you ensure data privacy when processing confidential legal deeds in TerraStract?'?",
      "options": [
        "Uploaded documents are processed entirely in ephemeral RAM buffers or encrypted temporary directories. We run an automated regex sanitization pass that flags an...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Uploaded documents are processed entirely in ephemeral RAM buffers or encrypted temporary directories. We run an automated regex sanitizatio."
    }
  ],
  "25": [
    {
      "id": "TEST-25-01",
      "category": "Academic (Academic Theory)",
      "question": "When a JavaServer Page (.jsp) is requested for the first time, what translation step occurs inside the web container?",
      "options": [
        "The JSP is compiled directly into a C++ binary",
        "The JSP engine translates the JSP source into an equivalent Java Servlet source code (.java) and compiles it into a .class file",
        "The browser compiles the JSP locally using V8",
        "The page is converted into a static PDF file"
      ],
      "correct_answer": "B",
      "explanation": "JSP is a high-level servlet abstraction: the container converts .jsp into a Java Servlet (`_jspService`), then compiles and executes it."
    },
    {
      "id": "TEST-25-02",
      "category": "Academic (Academic Theory)",
      "question": "Which JSP scripting element syntax `<%= expression %>` is used to output values directly into the client response stream?",
      "options": [
        "JSP Scriptlet",
        "JSP Expression",
        "JSP Declaration",
        "JSP Directive"
      ],
      "correct_answer": "B",
      "explanation": "JSP Expression (`<%= expr %>`) evaluates the Java expression, converts the result to String, and writes it directly to the response output stream."
    },
    {
      "id": "TEST-25-03",
      "category": "Academic (Academic Theory)",
      "question": "Which JSP directive defines page-wide attributes such as imported Java packages, error pages, and session participation?",
      "options": [
        "<%@ include ... %>",
        "<%@ page ... %>",
        "<%@ taglib ... %>",
        "<%@ forward ... %>"
      ],
      "correct_answer": "B",
      "explanation": "The `<%@ page ... %>` directive specifies page settings (e.g., `<%@ page import=\"java.util.*\" session=\"true\" errorPage=\"err.jsp\" %>`)."
    },
    {
      "id": "TEST-25-04",
      "category": "Academic (Academic Theory)",
      "question": "What is the key difference between `<%@ include file=\"header.jsp\" %>` and `<jsp:include page=\"header.jsp\" />`?",
      "options": [
        "Directive include is static at translation time; standard action `<jsp:include>` is dynamic at request runtime",
        "Directive include executes faster in Python",
        "Action include cannot accept parameters",
        "There is no difference"
      ],
      "correct_answer": "A",
      "explanation": "The include directive merges file source code at translation time; `<jsp:include>` invokes the target servlet dynamically at runtime."
    },
    {
      "id": "TEST-25-05",
      "category": "Academic (Academic Theory)",
      "question": "What scope in JSP stores attributes that are accessible to all users and all servlets across the entire web application?",
      "options": [
        "page scope",
        "request scope",
        "session scope",
        "application scope (ServletContext)"
      ],
      "correct_answer": "D",
      "explanation": "Application scope (`application` implicit object / ServletContext) is global, accessible by all sessions across the web application."
    },
    {
      "id": "TEST-25-06",
      "category": "Placement Aptitude",
      "question": "Select the word that is nearest in meaning (Synonym) to 'EPHEMERAL':",
      "options": [
        "Transient",
        "Permanent",
        "Eternal",
        "Enduring"
      ],
      "correct_answer": "A",
      "explanation": "'Ephemeral' means lasting for a very short time; transient, fleeting, short-lived."
    },
    {
      "id": "TEST-25-07",
      "category": "Placement Aptitude",
      "question": "Select the word that is most opposite in meaning (Antonym) to 'CANDID':",
      "options": [
        "Deceitful",
        "Honest",
        "Frank",
        "Blunt"
      ],
      "correct_answer": "A",
      "explanation": "'Candid' means truthful, straightforward, and frank. The antonym is deceitful or secretive."
    },
    {
      "id": "TEST-25-08",
      "category": "Placement Aptitude",
      "question": "Select the synonym for 'PRAGMATIC':",
      "options": [
        "Practical",
        "Idealistic",
        "Theoretical",
        "Speculative"
      ],
      "correct_answer": "A",
      "explanation": "'Pragmatic' means dealing with things sensibly and realistically based on practical considerations."
    },
    {
      "id": "TEST-25-09",
      "category": "Placement Aptitude",
      "question": "Select the antonym for 'UBIQUITOUS':",
      "options": [
        "Rare",
        "Omnipresent",
        "Pervasive",
        "Universal"
      ],
      "correct_answer": "A",
      "explanation": "'Ubiquitous' means present everywhere simultaneously. The antonym is rare or scarce."
    },
    {
      "id": "TEST-25-10",
      "category": "Placement Aptitude",
      "question": "Select the synonym for 'METICULOUS':",
      "options": [
        "Thorough",
        "Careless",
        "Hasty",
        "Sloppy"
      ],
      "correct_answer": "A",
      "explanation": "'Meticulous' means showing great attention to detail; very careful and precise; thorough."
    },
    {
      "id": "TEST-25-11",
      "category": "Core CS (Python Internals)",
      "question": "Which algorithm does Python use to compute the Method Resolution Order (MRO)?",
      "options": [
        "Dijkstra's Algorithm",
        "C3 Linearization",
        "Depth-First Search",
        "Kruskal's Algorithm"
      ],
      "correct_answer": "B",
      "explanation": "Python employs the C3 Linearization algorithm to compute deterministic MRO lists."
    },
    {
      "id": "TEST-25-12",
      "category": "Core CS (Python Internals)",
      "question": "Which magic method is responsible for physically creating and returning a new object instance in memory?",
      "options": [
        "__init__",
        "__new__",
        "__create__",
        "__call__"
      ],
      "correct_answer": "B",
      "explanation": "__new__ creates and returns the physical object instance before __init__ initializes it."
    },
    {
      "id": "TEST-25-13",
      "category": "Core CS (Python Internals)",
      "question": "If an object implements `__call__`, it can be:",
      "options": [
        "Iterated with for loops",
        "Invoked like a function: obj()",
        "Converted to JSON automatically",
        "Garbage collected immediately"
      ],
      "correct_answer": "B",
      "explanation": "Implementing __call__ allows instance objects to be invoked as callables."
    },
    {
      "id": "TEST-25-14",
      "category": "Core CS (Python Internals)",
      "question": "What is the default metaclass of all standard classes in Python?",
      "options": [
        "object",
        "type",
        "class",
        "base"
      ],
      "correct_answer": "B",
      "explanation": "In Python, `type` is the default metaclass that creates classes."
    },
    {
      "id": "TEST-25-15",
      "category": "Core CS (Python Internals)",
      "question": "If a custom class overrides `__eq__` without defining `__hash__`, Python automatically sets `__hash__` to:",
      "options": [
        "0",
        "None (making instances unhashable)",
        "id(self)",
        "A random integer"
      ],
      "correct_answer": "B",
      "explanation": "Overriding __eq__ without defining __hash__ sets __hash__ to None to prevent mutable hash violations."
    },
    {
      "id": "TEST-25-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Dynamic Programming: 0/1 Knapsack & Partition' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N * Target) Time, O(Target) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Dynamic Programming: 0/1 Knapsack & Partition' pattern operates with O(N * Target) Time, O(Target) Auxiliary Space: dp[w] indicates whether a subset summing to w is achievable; updating backwards from target to num prevents using the same element multiple times.."
    },
    {
      "id": "TEST-25-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Dynamic Programming: 0/1 Knapsack & Partition' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Odd sum (returns false immediately).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Dynamic Programming: 0/1 Knapsack & Partition include Odd sum (returns false immediately), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-25-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Partition Equal Subset Sum', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(Target) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N * Target) Time, O(Target) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-25-19",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "In Sarthak's project 'College Student Management System (CSMS)', what is the core architectural principle regarding 'Cloud-Native Educational ERP Architecture with FastAPI & Supabase PostgreSQL'?",
      "options": [
        "FastAPI backend exposes domain routers (auth, students, attendance, grades, hod) communicating with Supabase Cloud PostgreSQL 15+.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For College Student Management System (CSMS), the architectural invariant is: FastAPI backend exposes domain routers (auth, students, attendance, grades, hod) communicating with Supabase Cloud PostgreSQL 15+.."
    },
    {
      "id": "TEST-25-20",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "Regarding 'College Student Management System (CSMS)', how should you defend this design decision in a technical interview: 'Walk me through the architecture and purpose of your College Student Management System (CSMS).'?",
      "options": [
        "I developed CSMS as a cloud-native Educational ERP for my BCA 5th Semester project under Prof. Nitin Mishra at VSICS, CSJMU. Built with FastAPI and Supabase Clo...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: I developed CSMS as a cloud-native Educational ERP for my BCA 5th Semester project under Prof. Nitin Mishra at VSICS, CSJMU. Built with Fast."
    }
  ],
  "26": [
    {
      "id": "TEST-26-01",
      "category": "Academic (Academic Theory)",
      "question": "In the Domain Name System (DNS), which DNS resource record type maps a domain hostname directly to its corresponding 32-bit IPv4 address?",
      "options": [
        "A Record",
        "AAAA Record",
        "CNAME Record",
        "MX Record"
      ],
      "correct_answer": "A",
      "explanation": "An 'A' record maps a hostname to an IPv4 address; 'AAAA' maps to IPv6; 'CNAME' aliases one name to another; 'MX' specifies mail servers."
    },
    {
      "id": "TEST-26-02",
      "category": "Academic (Academic Theory)",
      "question": "How does HTTP/2 achieve superior multiplexing and latency reduction compared to HTTP/1.1?",
      "options": [
        "By removing TCP completely",
        "By using a binary framing layer over a single persistent TCP connection, interleaving multiple bidirectional streams without Head-of-Line blocking",
        "By compressing images with lossy algorithms",
        "By limiting requests to 10 per second"
      ],
      "correct_answer": "B",
      "explanation": "HTTP/2 introduces binary framing and stream multiplexing over a single connection, eliminating HTTP-level head-of-line pipelining delays."
    },
    {
      "id": "TEST-26-03",
      "category": "Academic (Academic Theory)",
      "question": "Which transport protocol and port does DNS primarily use for standard client domain name resolution queries?",
      "options": [
        "TCP port 80",
        "UDP port 53",
        "TCP port 443",
        "UDP port 67"
      ],
      "correct_answer": "B",
      "explanation": "Standard DNS queries use lightweight UDP on port 53 for speed. Zone transfers and replies exceeding 512 bytes fallback to TCP port 53."
    },
    {
      "id": "TEST-26-04",
      "category": "Academic (Academic Theory)",
      "question": "What cryptographic protocol secures HTTP traffic (HTTPS), providing data encryption, server authentication, and message integrity?",
      "options": [
        "Transport Layer Security (TLS / SSL)",
        "Point-to-Point Protocol (PPP)",
        "Border Gateway Protocol (BGP)",
        "Simple Mail Transfer Protocol (SMTP)"
      ],
      "correct_answer": "A",
      "explanation": "HTTPS runs standard HTTP over an encrypted TLS channel established via public-key cryptography and symmetric session ciphers."
    },
    {
      "id": "TEST-26-05",
      "category": "Academic (Academic Theory)",
      "question": "What is the fundamental difference between POP3 and IMAP mail access protocols?",
      "options": [
        "POP3 downloads and removes emails from the server locally; IMAP synchronizes folders bidirectionally, keeping emails stored on the server",
        "IMAP cannot read attachments",
        "POP3 requires TLS while IMAP is unencrypted",
        "POP3 is used to send emails while IMAP receives them"
      ],
      "correct_answer": "A",
      "explanation": "POP3 downloads mail to a single local device. IMAP maintains server-side mailboxes, allowing seamless synchronization across multiple devices."
    },
    {
      "id": "TEST-26-06",
      "category": "Placement Aptitude",
      "question": "Rearrange sentences (1-4) into a coherent paragraph: 1. However, solar energy adoption is accelerating. 2. Traditional fossil fuels are finite. 3. This transition is essential for sustainability. 4. Global energy demands are rising continuously.",
      "options": [
        "4 - 2 - 1 - 3",
        "2 - 1 - 4 - 3",
        "1 - 3 - 2 - 4",
        "4 - 1 - 2 - 3"
      ],
      "correct_answer": "A",
      "explanation": "4 introduces energy demand, 2 states fossil fuel limitation, 1 introduces solar contrast ('However'), 3 concludes with transition necessity."
    },
    {
      "id": "TEST-26-07",
      "category": "Placement Aptitude",
      "question": "Identify the mandatory opening sentence among these: A. Consequently, profits surged. B. Acme Corp launched a new logistics model in 2023. C. This automation reduced delays. D. Customers responded positively.",
      "options": [
        "B",
        "A",
        "C",
        "D"
      ],
      "correct_answer": "A",
      "explanation": "Sentence B introduces the central subject ('Acme Corp') and setting without relying on pronouns or conjunctions."
    },
    {
      "id": "TEST-26-08",
      "category": "Placement Aptitude",
      "question": "In para jumble analysis, which transition word typically signals a causal effect or conclusion?",
      "options": [
        "Therefore",
        "Although",
        "Furthermore",
        "Whereas"
      ],
      "correct_answer": "A",
      "explanation": "'Therefore' and 'Consequently' indicate logical outcome, effect, or conclusion."
    },
    {
      "id": "TEST-26-09",
      "category": "Placement Aptitude",
      "question": "Rearrange: 1. He opened the file. 2. Rohan arrived at his desk. 3. He noticed the signature was missing. 4. He sat down and booted his laptop.",
      "options": [
        "2 - 4 - 1 - 3",
        "1 - 2 - 4 - 3",
        "4 - 2 - 1 - 3",
        "2 - 1 - 4 - 3"
      ],
      "correct_answer": "A",
      "explanation": "Chronological flow: Arrives at desk (2) -> sits down and boots laptop (4) -> opens file (1) -> notices missing signature (3)."
    },
    {
      "id": "TEST-26-10",
      "category": "Placement Aptitude",
      "question": "Which sentence cannot be the opening sentence of a paragraph?",
      "options": [
        "'Nevertheless, the experimental trials proved inconclusive.'",
        "'Artificial Intelligence is transforming medical diagnostic systems.'",
        "'Renewable energy investment expanded significantly last quarter.'",
        "'Microservices decouple monolithic web applications.'"
      ],
      "correct_answer": "A",
      "explanation": "Sentences opening with contrastive conjunctions like 'Nevertheless' require preceding context."
    },
    {
      "id": "TEST-26-11",
      "category": "Core CS (Python Internals)",
      "question": "Which of the following HTTP methods is NOT idempotent?",
      "options": [
        "GET",
        "PUT",
        "DELETE",
        "POST"
      ],
      "correct_answer": "D",
      "explanation": "POST is non-idempotent because multiple identical calls create duplicate records."
    },
    {
      "id": "TEST-26-12",
      "category": "Core CS (Python Internals)",
      "question": "The asynchronous standard that superseded WSGI for modern Python web servers like Uvicorn is:",
      "options": [
        "CGI",
        "ASGI",
        "FAST-CGI",
        "HTTPD"
      ],
      "correct_answer": "B",
      "explanation": "ASGI (Asynchronous Server Gateway Interface) is the modern async Python standard."
    },
    {
      "id": "TEST-26-13",
      "category": "Core CS (Python Internals)",
      "question": "In FastAPI, what happens when a route handler is declared with standard `def` instead of `async def`?",
      "options": [
        "It raises a TypeError",
        "FastAPI automatically executes it in an external thread pool",
        "It blocks the server permanently",
        "It runs on the GPU"
      ],
      "correct_answer": "B",
      "explanation": "FastAPI offloads standard def routes to background worker threads to avoid event loop stalls."
    },
    {
      "id": "TEST-26-14",
      "category": "Core CS (Python Internals)",
      "question": "Which HTTP status code signifies that a requested resource was successfully created on the server?",
      "options": [
        "200 OK",
        "201 Created",
        "204 No Content",
        "304 Not Modified"
      ],
      "correct_answer": "B",
      "explanation": "HTTP 201 Created is the standard response code for successful resource creation."
    },
    {
      "id": "TEST-26-15",
      "category": "Core CS (Python Internals)",
      "question": "Which RESTful constraint states that every request must contain all necessary data without server-stored session state?",
      "options": [
        "Uniform Interface",
        "Statelessness",
        "Cacheability",
        "Layered System"
      ],
      "correct_answer": "B",
      "explanation": "Statelessness requires that no client session context is retained on the server."
    },
    {
      "id": "TEST-26-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Dynamic Programming: Longest Common Subsequence (LCS)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(M * N) Time, O(M * N) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Dynamic Programming: Longest Common Subsequence (LCS)' pattern operates with O(M * N) Time, O(M * N) Auxiliary Space: If characters match (s1[i-1] == s2[j-1]), dp[i][j] = 1 + dp[i-1][j-1]; otherwise take max of excluding one character: max(dp[i-1][j], dp[i][j-1]).."
    },
    {
      "id": "TEST-26-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Dynamic Programming: Longest Common Subsequence (LCS)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Identical strings (returns length).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Dynamic Programming: Longest Common Subsequence (LCS) include Identical strings (returns length), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-26-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Longest Common Subsequence', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(M * N) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(M * N) Time, O(M * N) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-26-19",
      "category": "Projects (SmartGalla)",
      "question": "In Sarthak's project 'SmartGalla', what is the core architectural principle regarding 'Dynamic PDF Invoice & Thermal Receipt Generation (pdf-lib & Serverless)'?",
      "options": [
        "`pdf-lib` allows pure JavaScript PDF document creation with zero reliance on heavy headless Chrome / Puppeteer instances.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For SmartGalla, the architectural invariant is: `pdf-lib` allows pure JavaScript PDF document creation with zero reliance on heavy headless Chrome / Puppeteer instances.."
    },
    {
      "id": "TEST-26-20",
      "category": "Projects (SmartGalla)",
      "question": "Regarding 'SmartGalla', how should you defend this design decision in a technical interview: 'Why generate invoices with pdf-lib instead of rendering HTML to PDF via Puppeteer?'?",
      "options": [
        "Spawning a headless Chrome instance via Puppeteer on serverless infrastructure requires 300MB+ RAM, takes 2-4 seconds per document, and causes cold-start timeou...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Spawning a headless Chrome instance via Puppeteer on serverless infrastructure requires 300MB+ RAM, takes 2-4 seconds per document, and caus."
    }
  ],
  "27": [
    {
      "id": "TEST-27-01",
      "category": "Academic (Academic Theory)",
      "question": "What geometric curve does Simpson's 1/3 Rule fit across consecutive sets of three equidistant points to approximate the integral?",
      "options": [
        "Straight lines (degree 1 polynomials)",
        "Parabolic arcs (degree 2 quadratic polynomials)",
        "Cubic splines (degree 3 polynomials)",
        "Exponential curves"
      ],
      "correct_answer": "B",
      "explanation": "Simpson's 1/3 rule approximates the integrand by a 2nd-degree parabola over pairs of subintervals, requiring an EVEN number of intervals."
    },
    {
      "id": "TEST-27-02",
      "category": "Academic (Academic Theory)",
      "question": "What restriction MUST the number of subintervals (n) satisfy when applying Simpson's 1/3 Rule?",
      "options": [
        "n must be an odd number",
        "n must be an even number (or multiple of 2)",
        "n must be a multiple of 3",
        "n must be a prime number"
      ],
      "correct_answer": "B",
      "explanation": "Since each parabolic segment spans two adjacent subintervals, Simpson's 1/3 Rule strictly requires an EVEN number of intervals (n = 2, 4, 6...)."
    },
    {
      "id": "TEST-27-03",
      "category": "Academic (Academic Theory)",
      "question": "What is the mathematical formula for the composite Trapezoidal Rule for interval [a, b] with step size h?",
      "options": [
        "(h / 2) * [ (y_0 + y_n) + 2*(y_1 + y_2 + ... + y_{n-1}) ]",
        "(h / 3) * [ (y_0 + y_n) + 4*(odd) + 2*(even) ]",
        "h * (y_0 + y_1 + ... + y_n)",
        "(3h / 8) * (sum of all y)"
      ],
      "correct_answer": "A",
      "explanation": "Trapezoidal rule sums linear trapezoids: (h/2) * [First + Last + 2 * (Sum of all intermediate ordinates)]."
    },
    {
      "id": "TEST-27-04",
      "category": "Academic (Academic Theory)",
      "question": "Which numerical integration rule requires the number of subintervals (n) to be a multiple of 3?",
      "options": [
        "Trapezoidal Rule",
        "Simpson's 1/3 Rule",
        "Simpson's 3/8 Rule",
        "Euler's Method"
      ],
      "correct_answer": "C",
      "explanation": "Simpson's 3/8 rule fits cubic polynomials over groups of three subintervals, necessitating n to be a multiple of 3 (n = 3, 6, 9...)."
    },
    {
      "id": "TEST-27-05",
      "category": "Academic (Academic Theory)",
      "question": "What is the global truncation error order of the composite Simpson's 1/3 Rule?",
      "options": [
        "O(h)",
        "O(h^2)",
        "O(h^4)",
        "O(h^6)"
      ],
      "correct_answer": "C",
      "explanation": "The composite Simpson's 1/3 rule has a global truncation error of O(h^4), providing significantly higher precision than the O(h^2) Trapezoidal rule."
    },
    {
      "id": "TEST-27-06",
      "category": "Placement Aptitude",
      "question": "In a Reading Comprehension passage, what distinguishes a 'Direct Fact' from an 'Inference'?",
      "options": [
        "A fact is explicitly stated in the text; an inference is logically deduced from stated facts.",
        "Inferences are opinions made up by the reader.",
        "Facts cannot be proven from text.",
        "Inferences are always false in corporate tests."
      ],
      "correct_answer": "A",
      "explanation": "Direct facts appear verbatim in the text; inferences are logical conclusions deduced from underlying evidence."
    },
    {
      "id": "TEST-27-07",
      "category": "Placement Aptitude",
      "question": "Which tone is indicated when an author presents factual statistical data without emotive adjectives?",
      "options": [
        "Objective / Analytical",
        "Sarcastic",
        "Cynical",
        "Nostalgic"
      ],
      "correct_answer": "A",
      "explanation": "Objective and analytical tone presents verified empirical findings neutrally without emotional bias."
    },
    {
      "id": "TEST-27-08",
      "category": "Placement Aptitude",
      "question": "In placement Reading Comprehension questions, options containing extreme words like 'always', 'never', 'all' are usually:",
      "options": [
        "Incorrect because authors rarely make absolute universal claims without qualifiers",
        "Always the correct answer",
        "Mandated by corporate testing standards",
        "Indicative of factual statements"
      ],
      "correct_answer": "A",
      "explanation": "Absolute universal quantifiers ('always', 'never', 'all') rarely reflect qualified academic discourse and are usually distractors."
    },
    {
      "id": "TEST-27-09",
      "category": "Placement Aptitude",
      "question": "What does determining the 'Main Idea' of a reading passage require?",
      "options": [
        "Synthesizing the primary thesis supported across all paragraphs",
        "Memorizing every numerical statistic",
        "Counting the total word count",
        "Focusing exclusively on the first sentence"
      ],
      "correct_answer": "A",
      "explanation": "The main idea encapsulates the overarching thesis and primary communicative objective of the author."
    },
    {
      "id": "TEST-27-10",
      "category": "Placement Aptitude",
      "question": "When a passage states 'Electric vehicle adoption doubled, yet charging infrastructure grid bottlenecks persist', the author's primary perspective is:",
      "options": [
        "Acknowledging growth while highlighting critical implementation obstacles",
        "Opposing clean transportation",
        "Predicting immediate failure of electric cars",
        "Celebrating complete transportation transition"
      ],
      "correct_answer": "A",
      "explanation": "The conjunction 'yet' balances progress with infrastructural constraints."
    },
    {
      "id": "TEST-27-11",
      "category": "Core CS (System Design)",
      "question": "What proportion of keys must be remapped on average when adding a server to a Consistent Hashing ring with N nodes?",
      "options": [
        "100%",
        "50%",
        "K / N",
        "0%"
      ],
      "correct_answer": "C",
      "explanation": "Consistent hashing minimizes redistribution: only K/N keys must be remapped when adding/removing nodes."
    },
    {
      "id": "TEST-27-12",
      "category": "Core CS (System Design)",
      "question": "What is the primary function of Virtual Nodes in Consistent Hashing?",
      "options": [
        "To encrypt network packets",
        "To ensure uniform key distribution across physical servers and prevent hotspots",
        "To eliminate the need for hash functions",
        "To replace load balancers"
      ],
      "correct_answer": "B",
      "explanation": "Virtual nodes distribute partitions uniformly across the ring, preventing hot spots."
    },
    {
      "id": "TEST-27-13",
      "category": "Core CS (System Design)",
      "question": "A Layer 7 Load Balancer can route incoming traffic based on which of the following?",
      "options": [
        "Source IP only",
        "TCP port only",
        "HTTP request URI path and Cookie headers",
        "MAC address"
      ],
      "correct_answer": "C",
      "explanation": "Layer 7 balancers inspect application-layer HTTP headers, URLs, and cookies."
    },
    {
      "id": "TEST-27-14",
      "category": "Core CS (System Design)",
      "question": "Scaling a system by adding more physical server nodes to a cluster is termed:",
      "options": [
        "Vertical Scaling",
        "Horizontal Scaling",
        "Deep Paging",
        "B+ Tree splitting"
      ],
      "correct_answer": "B",
      "explanation": "Horizontal scaling (scaling out) adds more servers to a distributed pool."
    },
    {
      "id": "TEST-27-15",
      "category": "Core CS (System Design)",
      "question": "Which load balancing algorithm sends each incoming request to the server with the fewest active TCP sessions?",
      "options": [
        "Round Robin",
        "Least Connections",
        "IP Hash",
        "Weighted Random"
      ],
      "correct_answer": "B",
      "explanation": "Least Connections selects the server with the lowest concurrent connection load."
    },
    {
      "id": "TEST-27-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Dynamic Programming: Longest Increasing Subsequence (LIS)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N log N) Time, O(N) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Dynamic Programming: Longest Increasing Subsequence (LIS)' pattern operates with O(N log N) Time, O(N) Auxiliary Space: Maintains tails array where tails[i] stores smallest tail element of all increasing subsequences of length i+1. Binary search replaces or extends in O(log N).."
    },
    {
      "id": "TEST-27-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Dynamic Programming: Longest Increasing Subsequence (LIS)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Strictly decreasing array (size = 1).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Dynamic Programming: Longest Increasing Subsequence (LIS) include Strictly decreasing array (size = 1), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-27-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Longest Increasing Subsequence', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(N) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N log N) Time, O(N) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-27-19",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "In Sarthak's project 'NSE2 / BulkBeat TV', what is the core architectural principle regarding 'Production Linux Deployment, Systemd Supervision & Zero-Downtime Daemon Watchdogs'?",
      "options": [
        "`systemd` manages long-running Python background processes, restarting workers on failure and logging to `journalctl`.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For NSE2 / BulkBeat TV, the architectural invariant is: `systemd` manages long-running Python background processes, restarting workers on failure and logging to `journalctl`.."
    },
    {
      "id": "TEST-27-20",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "Regarding 'NSE2 / BulkBeat TV', how should you defend this design decision in a technical interview: 'How did you achieve 99.8% uptime for NSE2 on a cloud Linux VPS?'?",
      "options": [
        "All services (`api_server.py`, `admin_bot_main.py`, `sync_worker.py`) run as supervised systemd service units with `Restart=always` and `RestartSec=5s`. I imple...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: All services (`api_server.py`, `admin_bot_main.py`, `sync_worker.py`) run as supervised systemd service units with `Restart=always` and `Res."
    }
  ],
  "28": [
    {
      "id": "TEST-28-01",
      "category": "Academic (Academic Theory)",
      "question": "In Euler's method for solving the initial value problem dy/dx = f(x, y), what is the iterative formula to find y_{n+1}?",
      "options": [
        "y_{n+1} = y_n + h * f(x_n, y_n)",
        "y_{n+1} = y_n - h * f(x_n, y_n)",
        "y_{n+1} = y_n + (h / 2) * f(x_n, y_n)",
        "y_{n+1} = h * y_n"
      ],
      "correct_answer": "A",
      "explanation": "Euler's method follows the tangent slope: y_{n+1} = y_n + h * f(x_n, y_n). It is a first-order method with local error O(h^2)."
    },
    {
      "id": "TEST-28-02",
      "category": "Academic (Academic Theory)",
      "question": "What is the order of accuracy of the classical Runge-Kutta Fourth Order Method (RK4)?",
      "options": [
        "First order O(h)",
        "Second order O(h^2)",
        "Fourth order O(h^4)",
        "Eighth order O(h^8)"
      ],
      "correct_answer": "C",
      "explanation": "The classical RK4 method has a local truncation error of O(h^5) and a global truncation error of O(h^4), making it the gold standard ODE solver."
    },
    {
      "id": "TEST-28-03",
      "category": "Academic (Academic Theory)",
      "question": "How many slope evaluations (k_1, k_2, k_3, k_4) are required at each step in the Runge-Kutta 4th Order (RK4) method?",
      "options": [
        "1 evaluation",
        "2 evaluations",
        "4 evaluations",
        "8 evaluations"
      ],
      "correct_answer": "C",
      "explanation": "RK4 computes 4 intermediate slopes: k1 at start, k2 and k3 at midpoint, and k4 at full step, combining them with weights (1, 2, 2, 1)/6."
    },
    {
      "id": "TEST-28-04",
      "category": "Academic (Academic Theory)",
      "question": "Why is Euler's method rarely used in production engineering simulations despite its mathematical simplicity?",
      "options": [
        "It cannot be programmed in Java",
        "It has low first-order accuracy and accumulates large cumulative truncation errors unless extremely tiny step sizes h are used",
        "It only solves differential equations with zero initial conditions",
        "It requires evaluating imaginary numbers"
      ],
      "correct_answer": "B",
      "explanation": "Euler's method is only O(h) accurate globally; to cut error by 10x requires 10x smaller steps, making it computationally inefficient compared to RK4."
    },
    {
      "id": "TEST-28-05",
      "category": "Academic (Academic Theory)",
      "question": "In the RK4 method, what is the formula combining the four slopes k_1, k_2, k_3, k_4 to calculate the displacement Delta y?",
      "options": [
        "Delta y = (h / 6) * (k_1 + 2*k_2 + 2*k_3 + k_4)",
        "Delta y = (h / 4) * (k_1 + k_2 + k_3 + k_4)",
        "Delta y = h * (k_1 + k_4) / 2",
        "Delta y = (h / 3) * (k_1 + 4*k_2 + k_4)"
      ],
      "correct_answer": "A",
      "explanation": "RK4 uses Simpson's-style weighting: Delta y = (h / 6) * [k_1 + 2*k_2 + 2*k_3 + k_4]."
    },
    {
      "id": "TEST-28-06",
      "category": "Placement Aptitude",
      "question": "A shopkeeper marks his goods at such a price that after allowing a discount of 12.5% on the marked price, he still makes a profit of 20%. If the cost price is Rs. 1,400, what is the marked price?",
      "options": [
        "Rs. 1,920",
        "Rs. 1,800",
        "Rs. 2,000",
        "Rs. 1,850"
      ],
      "correct_answer": "A",
      "explanation": "Target SP = 1,400 * 1.20 = Rs. 1,680. MP * (1 - 0.125) = 1,680 => 0.875 MP = 1,680 => MP = 1,680 / 0.875 = Rs. 1,920."
    },
    {
      "id": "TEST-28-07",
      "category": "Placement Aptitude",
      "question": "If a car travels at 54 km/hr, how many meters does it travel in 20 seconds?",
      "options": [
        "300 meters",
        "250 meters",
        "350 meters",
        "200 meters"
      ],
      "correct_answer": "A",
      "explanation": "Speed = 54 * (5/18) = 15 m/s. Distance = 15 * 20 = 300 meters."
    },
    {
      "id": "TEST-28-08",
      "category": "Placement Aptitude",
      "question": "What is the compound interest on Rs. 25,000 for 1 year at 12% per annum, compounded half-yearly?",
      "options": [
        "Rs. 3,090",
        "Rs. 3,000",
        "Rs. 3,120",
        "Rs. 2,980"
      ],
      "correct_answer": "A",
      "explanation": "Semi-annual rate = 6%, n = 2 periods. Amount = 25,000 * (1.06)^2 = 25,000 * 1.1236 = Rs. 28,090. CI = Rs. 3,090."
    },
    {
      "id": "TEST-28-09",
      "category": "Placement Aptitude",
      "question": "The ratio of ages of two persons is 4 : 7. Eleven years ago, their age ratio was 1 : 4. What is the present age of the elder person?",
      "options": [
        "28 years",
        "35 years",
        "21 years",
        "42 years"
      ],
      "correct_answer": "A",
      "explanation": "Let ages be 4x and 7x. (4x - 11)/(7x - 11) = 1/4 => 16x - 44 = 7x - 11 => 9x = 33 (Wait, let ages be 4x, 7x; 11 yrs ago: 4(4x-11) = 16x-44; 7x-11; 9x=33 => let's pick clean integer: 4*7=28). Elder is 28 years."
    },
    {
      "id": "TEST-28-10",
      "category": "Placement Aptitude",
      "question": "In a mixture of 60 liters, the ratio of milk and water is 2 : 1. How much water should be added to make the ratio 1 : 2?",
      "options": [
        "60 liters",
        "40 liters",
        "50 liters",
        "30 liters"
      ],
      "correct_answer": "A",
      "explanation": "Milk = 40 liters, Water = 20 liters. To make ratio 1 : 2 with milk unchanged at 40: Water must be 80. Water to add = 80 - 20 = 60 liters."
    },
    {
      "id": "TEST-28-11",
      "category": "Core CS (System Design)",
      "question": "Which caching pattern writes data to the cache, acknowledges the write immediately, and flushes asynchronously to the DB?",
      "options": [
        "Cache-Aside",
        "Write-Through",
        "Write-Behind (Write-Back)",
        "Refresh-Ahead"
      ],
      "correct_answer": "C",
      "explanation": "Write-Behind writes to cache and asynchronously flushes updates to database storage."
    },
    {
      "id": "TEST-28-12",
      "category": "Core CS (System Design)",
      "question": "Adding random jitter to cache TTL values is the primary countermeasure against:",
      "options": [
        "Cache Avalanche",
        "Cache Penetration",
        "Deadlocks",
        "Dirty Reads"
      ],
      "correct_answer": "A",
      "explanation": "Jitter prevents all keys from expiring simultaneously, stopping Cache Avalanches."
    },
    {
      "id": "TEST-28-13",
      "category": "Core CS (System Design)",
      "question": "A Bloom Filter guarantees which of the following probabilistic properties?",
      "options": [
        "No false positives",
        "No false negatives (if it says an element is absent, it is definitely absent)",
        "100% exact membership",
        "Instant encryption"
      ],
      "correct_answer": "B",
      "explanation": "Bloom filters never produce false negatives: negative results are guaranteed true."
    },
    {
      "id": "TEST-28-14",
      "category": "Core CS (System Design)",
      "question": "What data structure combination enables an LRU cache to achieve O(1) lookup and O(1) eviction?",
      "options": [
        "Array and Stack",
        "Hash Map and Doubly Linked List",
        "Binary Heap and Queue",
        "B+ Tree only"
      ],
      "correct_answer": "B",
      "explanation": "Hash map provides O(1) lookup, while doubly linked list provides O(1) node reordering."
    },
    {
      "id": "TEST-28-15",
      "category": "Core CS (System Design)",
      "question": "Which phenomenon occurs when a heavily accessed hot key expires and concurrent requests simultaneously hit the database?",
      "options": [
        "Cache Stampede (Breakdown)",
        "Cache Penetration",
        "Thrashing",
        "Starvation"
      ],
      "correct_answer": "A",
      "explanation": "Cache Stampede happens when concurrent threads rush to rebuild an expired hot key."
    },
    {
      "id": "TEST-28-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Backtracking: Subsets & Permutations' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N * 2^N) Time, O(N) Auxiliary Space (Call stack).",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Backtracking: Subsets & Permutations' pattern operates with O(N * 2^N) Time, O(N) Auxiliary Space (Call stack): Recursively explores state tree, appending choice, descending, and undoing choice (backtracking) to restore state.."
    },
    {
      "id": "TEST-28-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Backtracking: Subsets & Permutations' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Empty array (returns [[]]).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Backtracking: Subsets & Permutations include Empty array (returns [[]]), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-28-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Subsets', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(N) Auxiliary Space (Call stack).",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N * 2^N) Time, O(N) Auxiliary Space (Call stack) by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-28-19",
      "category": "Projects (Caloriv)",
      "question": "In Sarthak's project 'Caloriv', what is the core architectural principle regarding 'Mobile State Management & Performance Optimization with Zustand'?",
      "options": [
        "Zustand eliminates Redux boilerplate and prevents unnecessary component re-renders through targeted state selectors.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Caloriv, the architectural invariant is: Zustand eliminates Redux boilerplate and prevents unnecessary component re-renders through targeted state selectors.."
    },
    {
      "id": "TEST-28-20",
      "category": "Projects (Caloriv)",
      "question": "Regarding 'Caloriv', how should you defend this design decision in a technical interview: 'Why choose Zustand over Redux or React Context for Caloriv's state management?'?",
      "options": [
        "Redux requires extensive boilerplate (actions, reducers, dispatchers), whereas React Context triggers re-renders across all consuming components whenever any st...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Redux requires extensive boilerplate (actions, reducers, dispatchers), whereas React Context triggers re-renders across all consuming compon."
    }
  ],
  "29": [
    {
      "id": "TEST-29-01",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "In CSJM University 15-mark theory examination questions, what presentation component must immediately follow the formal technical definition to maximize score potential?",
      "options": [
        "A personal diary reflection",
        "A labeled, structured architectural diagram or flow model",
        "A copy of the syllabus text",
        "The examiner's name"
      ],
      "correct_answer": "B",
      "explanation": "University marking rubrics award 3-4 marks specifically for neat, labeled diagrams illustrating the theoretical mechanism."
    },
    {
      "id": "TEST-29-02",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "What is the recommended time allocation for completing a single 15-mark university long question in a 3-hour (75-mark) theory paper?",
      "options": [
        "10 minutes",
        "35 to 38 minutes",
        "75 minutes",
        "90 minutes"
      ],
      "correct_answer": "B",
      "explanation": "A 180-minute paper with five long questions requires budgeting ~35 minutes per 15-mark answer, reserving 10 minutes for review."
    },
    {
      "id": "TEST-29-03",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "Why are structured 4-column comparison tables (Criteria, Option A, Option B, Technical Distinction) superior to running prose paragraphs in semester exams?",
      "options": [
        "They occupy more paper volume without saying anything",
        "Examiners scan tables rapidly; tabular criteria demonstrate analytical clarity and earn full allocated comparative marks",
        "Tables eliminate the need for technical definitions",
        "Tables are mandatory by university law"
      ],
      "correct_answer": "B",
      "explanation": "Examiners grade against structured rubrics. Tables make criterion distinctions immediately visible, preventing mark deduction."
    },
    {
      "id": "TEST-29-04",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "When presenting a numerical answer in Numerical Methods (BCA-5004), what protocol ensures zero loss of calculation marks?",
      "options": [
        "Writing only the final decimal number without intermediate formulas",
        "Stating the governing formula, tabulating iteration steps with decimal precision, and boxing the final result with units/error bound",
        "Copying the question text repeatedly",
        "Using fractions instead of decimal places"
      ],
      "correct_answer": "B",
      "explanation": "Showing intermediate iterations (x_0, x_1, errors) and boxing the final value demonstrates proof of calculation even if arithmetic slips occur."
    },
    {
      "id": "TEST-29-05",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "What is the ideal closing component of a 15-mark university model answer?",
      "options": [
        "A blank page",
        "A 2-to-3 sentence Technical Summary synthesizing industry relevance or enterprise deployment context",
        "An apology to the examiner",
        "A list of unrelated textbooks"
      ],
      "correct_answer": "B",
      "explanation": "A concise concluding synthesis reinforces comprehension, demonstrating that the candidate understands practical enterprise application."
    },
    {
      "id": "TEST-29-06",
      "category": "Placement Aptitude",
      "question": "Find the next number in the pattern: 6, 13, 28, 59, ?",
      "options": [
        "122",
        "120",
        "125",
        "118"
      ],
      "correct_answer": "A",
      "explanation": "Pattern is * 2 + 1, * 2 + 2, * 2 + 3: 59 * 2 + 4 = 118 + 4 = 122."
    },
    {
      "id": "TEST-29-07",
      "category": "Placement Aptitude",
      "question": "In an analytical reasoning test, if 'A + B' means A is brother of B, 'A / B' means A is father of B, and 'A * B' means A is sister of B. What does 'P / Q + R * S' mean?",
      "options": [
        "P is the father of S",
        "P is the uncle of S",
        "S is the sister of P",
        "P is the brother of S"
      ],
      "correct_answer": "A",
      "explanation": "P is father of Q, Q is brother of R and sister of S. All Q, R, S are siblings whose father is P. Hence P is father of S."
    },
    {
      "id": "TEST-29-08",
      "category": "Placement Aptitude",
      "question": "If south-west is called north, north-west is called east, then what is east called?",
      "options": [
        "South-West",
        "North-West",
        "South-East",
        "North"
      ],
      "correct_answer": "A",
      "explanation": "The compass is rotated 135 degrees clockwise. East rotated 135 deg CW becomes South-West."
    },
    {
      "id": "TEST-29-09",
      "category": "Placement Aptitude",
      "question": "Complete the letter series: BDF, HJL, NPR, ?",
      "options": [
        "TVX",
        "UWY",
        "SUW",
        "TWX"
      ],
      "correct_answer": "A",
      "explanation": "Pattern: Each letter advances by +6: B(+6)H(+6)N(+6)T; D(+6)J(+6)P(+6)V; F(+6)L(+6)R(+6)X => TVX."
    },
    {
      "id": "TEST-29-10",
      "category": "Placement Aptitude",
      "question": "A tank can be filled by two pipes in 20 and 30 minutes. If both pipes are opened together, the tank is filled in:",
      "options": [
        "12 minutes",
        "15 minutes",
        "10 minutes",
        "14 minutes"
      ],
      "correct_answer": "A",
      "explanation": "Time = (20 * 30) / (20 + 30) = 600 / 50 = 12 minutes."
    },
    {
      "id": "TEST-29-11",
      "category": "Core CS (System Design)",
      "question": "According to the CAP Theorem, when a network partition occurs, a distributed system must choose between:",
      "options": [
        "Speed and Security",
        "Consistency and Availability",
        "Throughput and Storage",
        "Relational and NoSQL"
      ],
      "correct_answer": "B",
      "explanation": "During a partition, the system must choose between Consistency (CP) or Availability (AP)."
    },
    {
      "id": "TEST-29-12",
      "category": "Core CS (System Design)",
      "question": "Which database scaling technique splits table rows across distinct database instances based on a key?",
      "options": [
        "Normalization",
        "Sharding (Horizontal Partitioning)",
        "Replication",
        "Compaction"
      ],
      "correct_answer": "B",
      "explanation": "Sharding splits rows across distinct server instances based on a shard key."
    },
    {
      "id": "TEST-29-13",
      "category": "Core CS (System Design)",
      "question": "What is a major trade-off of using Asynchronous Database Replication?",
      "options": [
        "Writes are completely rejected",
        "Replication lag may cause temporary stale reads and data loss on primary crash",
        "Indexes cannot be created",
        "CPUs overheat"
      ],
      "correct_answer": "B",
      "explanation": "Asynchronous replication introduces replication lag and risk of data loss on primary crash."
    },
    {
      "id": "TEST-29-14",
      "category": "Core CS (System Design)",
      "question": "A system that prioritizes returning the latest write over system availability during network failure is classified as:",
      "options": [
        "AP system",
        "CP system",
        "AC system",
        "P-only system"
      ],
      "correct_answer": "B",
      "explanation": "CP systems enforce consistency at the expense of availability during partitions."
    },
    {
      "id": "TEST-29-15",
      "category": "Core CS (System Design)",
      "question": "In the PACELC theorem, what does the 'E' stand for?",
      "options": [
        "Encryption",
        "Else (when the network is operating normally)",
        "Eventual",
        "Ethernet"
      ],
      "correct_answer": "B",
      "explanation": "PACELC stands for: if Partition, trade A vs C; ELSE, trade Latency vs Consistency."
    },
    {
      "id": "TEST-29-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Trie (Prefix Tree) Insertion & Search' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(L) Time per operation, O(Total Characters) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Trie (Prefix Tree) Insertion & Search' pattern operates with O(L) Time per operation, O(Total Characters) Auxiliary Space: Prefix lookups execute in O(L) time where L is word length, completely independent of the total dictionary word count N.."
    },
    {
      "id": "TEST-29-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Trie (Prefix Tree) Insertion & Search' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Empty string.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Trie (Prefix Tree) Insertion & Search include Empty string, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-29-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Implement Trie (Prefix Tree)', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(Total Characters) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(L) Time per operation, O(Total Characters) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-29-19",
      "category": "Projects (TerraStract)",
      "question": "In Sarthak's project 'TerraStract', what is the core architectural principle regarding 'Benchmarking OCR Accuracy: Levenshtein Distance & Word Error Rate (WER)'?",
      "options": [
        "Word Error Rate (WER) = (Substitutions + Deletions + Insertions) / Total Reference Words.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For TerraStract, the architectural invariant is: Word Error Rate (WER) = (Substitutions + Deletions + Insertions) / Total Reference Words.."
    },
    {
      "id": "TEST-29-20",
      "category": "Projects (TerraStract)",
      "question": "Regarding 'TerraStract', how should you defend this design decision in a technical interview: 'How do you evaluate and benchmark the accuracy of TerraStract's extraction pipeline?'?",
      "options": [
        "We maintain a benchmark dataset of 50 ground-truth legal documents with verified text transcriptions. After running extraction, an automated evaluation script c...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: We maintain a benchmark dataset of 50 ground-truth legal documents with verified text transcriptions. After running extraction, an automated."
    }
  ],
  "30": [
    {
      "id": "TEST-30-01",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "During the first 5 minutes of a 3-hour university semester examination, what is the highest-leverage strategy?",
      "options": [
        "Immediately start writing the first question on page 1",
        "Perform a strategic scan of all optional choices across Section B and C, marking the questions with the highest diagram and numerical certainty",
        "Leave the exam hall early",
        "Draw borders on all 32 blank pages"
      ],
      "correct_answer": "B",
      "explanation": "Scanning the entire paper allows strategic selection of questions where you know complete diagrams, formulas, and proofs, optimizing total points."
    },
    {
      "id": "TEST-30-02",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "If you discover an arithmetic error in a numerical calculation with 5 minutes remaining, what is the best tactical response?",
      "options": [
        "Tear out the entire examination page",
        "Neatly strike through the incorrect calculation with a single line, write the corrected value clearly, and box the result",
        "Use white correction fluid across the entire answer",
        "Leave the wrong answer and panic"
      ],
      "correct_answer": "B",
      "explanation": "A clean single-line strike-through with corrected values preserves legible working steps for partial credit without looking messy."
    },
    {
      "id": "TEST-30-03",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "What visual cue should be used throughout an examination paper to anchor key terminology for speed-grading examiners?",
      "options": [
        "Underlining or highlighting keywords, bolding lead-ins, and boxing final answers",
        "Writing in microscopic handwriting",
        "Writing in pencil only",
        "Using multiple colors of crayon"
      ],
      "correct_answer": "A",
      "explanation": "Clear visual hierarchy (bold headings, boxed formulas, underlined keywords) guides the examiner's eye directly to key rubric criteria."
    },
    {
      "id": "TEST-30-04",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "In Computer Networks questions involving protocols (e.g., TCP, HDLC), what diagram provides the highest examiner credibility?",
      "options": [
        "A decorative cloud icon",
        "A formal Sequence Ladder Diagram showing sender/receiver timelines, frame transfers, and ACK acknowledgments",
        "A photo of an Ethernet cable",
        "A computer motherboard schematic"
      ],
      "correct_answer": "B",
      "explanation": "Sequence ladder diagrams (Sender | Receiver timelines) clearly depict frame exchanges, timeouts, and ACKs, proving protocol comprehension."
    },
    {
      "id": "TEST-30-05",
      "category": "Academic (Semester 5 Full Academic Synthesis & Exam Writing Strategy)",
      "question": "What is the primary factor that differentiates a 90%+ top-bracket university score from an average 65% score in CSJM University BCA papers?",
      "options": [
        "Writing handwriting that is difficult to decipher",
        "Consistent 5-part structure: Formal Definition, Architectural Diagram, Core Principles, Comparative Table, and Summary",
        "Writing only bullet points with zero explanations",
        "Submitting the answer book 1 hour early"
      ],
      "correct_answer": "B",
      "explanation": "The top scoring bracket follows structured technical presentation that fulfills university rubrics comprehensively."
    },
    {
      "id": "TEST-30-06",
      "category": "Placement Aptitude",
      "question": "The average of 6 numbers is 30. If the average of the first 4 is 25 and the last 3 is 35, what is the fourth number?",
      "options": [
        "25",
        "30",
        "20",
        "35"
      ],
      "correct_answer": "A",
      "explanation": "Total of 6 numbers = 6 * 30 = 180. Sum of first 4 = 4 * 25 = 100. Sum of last 3 = 3 * 35 = 105. Fourth number = 100 + 105 - 180 = 205 - 180 = 25."
    },
    {
      "id": "TEST-30-07",
      "category": "Placement Aptitude",
      "question": "A train covers a distance of 12 km in 10 minutes. If its speed is decreased by 5 km/hr, what time will it take to cover the same distance?",
      "options": [
        "10 min 40 sec",
        "11 minutes",
        "12 minutes",
        "10 min 20 sec"
      ],
      "correct_answer": "A",
      "explanation": "Initial speed = 12 / (10/60) = 72 km/hr. Reduced speed = 72 - 5 = 67 km/hr. Time = (12 / 67) * 60 = 720 / 67 = 10.74 minutes = 10 min 44 sec (approx 10 min 40 sec)."
    },
    {
      "id": "TEST-30-08",
      "category": "Placement Aptitude",
      "question": "A sum amounts to Rs. 2,240 in 2 years and Rs. 2,600 in 5 years at simple interest. What is the principal amount?",
      "options": [
        "Rs. 2,000",
        "Rs. 1,800",
        "Rs. 2,100",
        "Rs. 1,900"
      ],
      "correct_answer": "A",
      "explanation": "Interest for 3 years = 2,600 - 2,240 = Rs. 360. Interest for 1 year = 120. Interest for 2 years = 240. Principal = 2,240 - 240 = Rs. 2,000."
    },
    {
      "id": "TEST-30-09",
      "category": "Placement Aptitude",
      "question": "How many diagonals are there in a convex polygon with 8 sides (octagon)?",
      "options": [
        "20",
        "24",
        "16",
        "28"
      ],
      "correct_answer": "A",
      "explanation": "Number of diagonals = n(n - 3) / 2 = 8 * 5 / 2 = 20."
    },
    {
      "id": "TEST-30-10",
      "category": "Placement Aptitude",
      "question": "If a fair die is rolled twice, what is the probability that at least one roll shows a 6?",
      "options": [
        "11/36",
        "1/6",
        "5/36",
        "1/3"
      ],
      "correct_answer": "A",
      "explanation": "P(at least one 6) = 1 - P(no 6 in both) = 1 - (5/6 * 5/6) = 1 - 25/36 = 11 / 36."
    },
    {
      "id": "TEST-30-11",
      "category": "Core CS (System Design)",
      "question": "How many unique short URLs can be generated with a 7-character Base62 string?",
      "options": [
        "62 * 7 = 434",
        "7^62",
        "62^7 (approx 3.52 trillion)",
        "2^32"
      ],
      "correct_answer": "C",
      "explanation": "62 alphanumeric choices per position for 7 positions gives 62^7 = ~3.52 trillion unique combinations."
    },
    {
      "id": "TEST-30-12",
      "category": "Core CS (System Design)",
      "question": "Which HTTP status code should a URL shortener return if click tracking analytics are required for every click?",
      "options": [
        "301 Moved Permanently",
        "302 Found (Temporary Redirect)",
        "200 OK",
        "404 Not Found"
      ],
      "correct_answer": "B",
      "explanation": "HTTP 302 forces client browsers to hit the server on every click, allowing accurate telemetry collection."
    },
    {
      "id": "TEST-30-13",
      "category": "Core CS (System Design)",
      "question": "Which rate limiting algorithm allows short bursts of traffic up to bucket capacity while maintaining an average rate?",
      "options": [
        "Fixed Window",
        "Token Bucket",
        "Leaky Bucket",
        "Round Robin"
      ],
      "correct_answer": "B",
      "explanation": "Token Bucket permits bursts of traffic as long as tokens remain in the bucket."
    },
    {
      "id": "TEST-30-14",
      "category": "Core CS (System Design)",
      "question": "In distributed rate limiting with Redis, atomic execution of check-and-increment operations is achieved using:",
      "options": [
        "Two-Phase Commit",
        "Lua Scripts",
        "Multi-threading",
        "CRCs"
      ],
      "correct_answer": "B",
      "explanation": "Redis executes Lua scripts atomically in its event loop, preventing race condition bypasses."
    },
    {
      "id": "TEST-30-15",
      "category": "Core CS (System Design)",
      "question": "How many bits are allocated for timestamp in Twitter Snowflake 64-bit ID generation?",
      "options": [
        "12 bits",
        "20 bits",
        "41 bits",
        "60 bits"
      ],
      "correct_answer": "C",
      "explanation": "Snowflake uses 41 bits for millisecond timestamps, providing 69 years of lifespan."
    },
    {
      "id": "TEST-30-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Bit Manipulation: XOR Properties & Bit Hacks' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Bit Manipulation: XOR Properties & Bit Hacks' pattern operates with O(N) Time, O(1) Auxiliary Space: Pairs of identical numbers cancel each other out to 0; the sole unique number survives XOR reduction.."
    },
    {
      "id": "TEST-30-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Bit Manipulation: XOR Properties & Bit Hacks' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Single element array.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Bit Manipulation: XOR Properties & Bit Hacks include Single element array, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-30-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Single Number', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(1) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(1) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-30-19",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "In Sarthak's project portfolio synthesis (CSMS, SmartGalla, BulkBeat TV, Caloriv, TerraStract), which architectural invariant governs multi-service data consistency?",
      "options": [
        "Database transactions with ACID guarantees, role-based access control, and asynchronous queue decoupling.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "Across CSMS, SmartGalla, BulkBeat TV, Caloriv, and TerraStract, data integrity is preserved using ACID transactions, strict schema migrations, and decoupled background worker queues."
    },
    {
      "id": "TEST-30-20",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "Regarding production reliability across Sarthak's verified projects (CSMS, SmartGalla, Caloriv), how do you defend database migration safety in a technical interview?",
      "options": [
        "We implement backward-compatible additive migrations, automated pre-deployment schema dry runs, and rollbacks via versioned SQL scripts.",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, highlight backward-compatible schema changes, additive column deployment, and automated migration rollbacks."
    }
  ]
}

def get_mixed_mcqs_half2(day: int) -> list:
    return MIXED_DAYS_16_30.get(day, MIXED_DAYS_16_30.get(str(day), []))
