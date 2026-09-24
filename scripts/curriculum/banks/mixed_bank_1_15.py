#!/usr/bin/env python3
"""
scripts/curriculum/banks/mixed_bank_1_15.py
Authentic Mixed Test MCQs for Days 1 to 15 (20 MCQs/day).
"""

MIXED_DAYS_1_15 = {
  "1": [
    {
      "id": "TEST-01-01",
      "category": "Academic (Knowledge Management)",
      "question": "According to Herbert A. Simon, in which phase of the decision-making process does an executive identify problems and scan the operational environment?",
      "options": [
        "Design Phase",
        "Intelligence Phase",
        "Choice Phase",
        "Implementation Phase"
      ],
      "correct_answer": "B",
      "explanation": "Simon's Intelligence phase involves environmental scanning, data acquisition, and identifying conditions or anomalies that necessitate decision making."
    },
    {
      "id": "TEST-01-02",
      "category": "Academic (Knowledge Management)",
      "question": "What core cognitive principle explains why managerial decision makers select 'satisficing' alternatives instead of global optimal solutions?",
      "options": [
        "Bounded Rationality",
        "Pareto Efficiency",
        "Linear Programming",
        "Deterministic Optimization"
      ],
      "correct_answer": "A",
      "explanation": "Herbert Simon's Bounded Rationality states that human cognition is limited by information asymmetry, finite computing capacity, and time, leading to satisficing behavior."
    },
    {
      "id": "TEST-01-03",
      "category": "Academic (Knowledge Management)",
      "question": "Which phase was explicitly added to complete the four-stage decision-making model by Simon to track execution feedback?",
      "options": [
        "Verification Phase",
        "Formulation Phase",
        "Implementation Phase",
        "Optimization Phase"
      ],
      "correct_answer": "C",
      "explanation": "Simon originally formulated a 3-phase model (Intelligence, Design, Choice) and subsequently added Implementation to monitor execution and feed telemetry back."
    },
    {
      "id": "TEST-01-04",
      "category": "Academic (Knowledge Management)",
      "question": "In Herbert Simon's framework, what type of decisions can be handled entirely by established algorithms and automated rules without executive intervention?",
      "options": [
        "Unstructured decisions",
        "Strategic decisions",
        "Structured decisions",
        "Subjective decisions"
      ],
      "correct_answer": "C",
      "explanation": "Structured decisions are routine, repetitive, and possess a definite methodology for handling, making them programmable via computer systems."
    },
    {
      "id": "TEST-01-05",
      "category": "Academic (Knowledge Management)",
      "question": "Which technology directly assists executive decision making in the Design phase by simulating business consequences of generated alternatives?",
      "options": [
        "Transaction Processing Systems (TPS)",
        "Model Base Management Systems (MBMS)",
        "Network Interface Cards",
        "BIOS firmware"
      ],
      "correct_answer": "B",
      "explanation": "MBMS provides quantitative and simulation models (linear programming, forecasting) to analyze decision alternatives during the Design phase."
    },
    {
      "id": "TEST-01-06",
      "category": "Placement Aptitude",
      "question": "The population of a town increases by 10% in the first year and decreases by 10% in the second year. If the population at the end of the second year is 39,600, what was the original population?",
      "options": [
        "40,000",
        "42,000",
        "39,000",
        "41,500"
      ],
      "correct_answer": "A",
      "explanation": "Let initial population be P. After 1st year: 1.10 P. After 2nd year: 1.10 * 0.90 P = 0.99 P. Given 0.99 P = 39,600 => P = 39,600 / 0.99 = 40,000."
    },
    {
      "id": "TEST-01-07",
      "category": "Placement Aptitude",
      "question": "In an examination, 35% of candidates failed in Mathematics and 42% failed in English. If 15% failed in both subjects, what percentage of candidates passed in both subjects?",
      "options": [
        "38%",
        "42%",
        "35%",
        "40%"
      ],
      "correct_answer": "A",
      "explanation": "Failed in at least one = P(M or E) = 35% + 42% - 15% = 62%. Candidates passing in both subjects = 100% - 62% = 38%."
    },
    {
      "id": "TEST-01-08",
      "category": "Placement Aptitude",
      "question": "A's salary is increased by 10% and then decreased by 10%. What is the net change in his salary?",
      "options": [
        "1% decrease",
        "No change",
        "1% increase",
        "2% decrease"
      ],
      "correct_answer": "A",
      "explanation": "Net percentage change = 10 - 10 - (10 * 10 / 100) = -1%. Hence, salary decreases by 1%."
    },
    {
      "id": "TEST-01-09",
      "category": "Placement Aptitude",
      "question": "If 20% of a number is added to 80, the result is the number itself. What is the number?",
      "options": [
        "100",
        "80",
        "120",
        "90"
      ],
      "correct_answer": "A",
      "explanation": "0.20x + 80 = x => 0.80x = 80 => x = 80 / 0.80 = 100."
    },
    {
      "id": "TEST-01-10",
      "category": "Placement Aptitude",
      "question": "In a college election between two candidates, the winning candidate received 58% of the valid votes and won by a majority of 960 votes. What was the total number of valid votes polled?",
      "options": [
        "6,000",
        "5,800",
        "6,400",
        "5,000"
      ],
      "correct_answer": "A",
      "explanation": "Majority margin = 58% - 42% = 16%. 16% of Total = 960 => Total = 960 / 0.16 = 6,000 votes."
    },
    {
      "id": "TEST-01-11",
      "category": "Core CS (Operating Systems)",
      "question": "Which of the following resources is NOT shared between threads belonging to the same process?",
      "options": [
        "Heap memory",
        "Open file descriptors",
        "CPU registers and Call Stack",
        "Global variables in Data section"
      ],
      "correct_answer": "C",
      "explanation": "Threads share text, data, and heap segments along with OS resources, but maintain private CPU registers and call stacks."
    },
    {
      "id": "TEST-01-12",
      "category": "Core CS (Operating Systems)",
      "question": "What is the primary cause of CPU overhead during a process context switch?",
      "options": [
        "Re-compiling source code",
        "Saving/restoring PCB registers, TLB cache invalidation, and memory map reloads",
        "Disk head movement",
        "Allocating new socket connections"
      ],
      "correct_answer": "B",
      "explanation": "Context switching requires saving state to PCB, switching page tables, and invalidating CPU/TLB caches."
    },
    {
      "id": "TEST-01-13",
      "category": "Core CS (Operating Systems)",
      "question": "A process that has finished execution but still occupies an entry in the process table is known as a:",
      "options": [
        "Daemon process",
        "Orphan process",
        "Zombie process",
        "Background process"
      ],
      "correct_answer": "C",
      "explanation": "A zombie process remains until its parent executes wait() to retrieve its termination status."
    },
    {
      "id": "TEST-01-14",
      "category": "Core CS (Operating Systems)",
      "question": "When a parent process terminates before its child process in Linux/Unix, the child process becomes:",
      "options": [
        "Terminated immediately",
        "A zombie process",
        "Re-parented to init/systemd (PID 1)",
        "Suspended indefinitely"
      ],
      "correct_answer": "C",
      "explanation": "Orphaned processes are adopted by init/systemd (PID 1), which reaps their termination status."
    },
    {
      "id": "TEST-01-15",
      "category": "Core CS (Operating Systems)",
      "question": "In which memory segment are dynamically allocated variables (via malloc in C or new in C++) stored?",
      "options": [
        "Stack",
        "Data section",
        "BSS segment",
        "Heap"
      ],
      "correct_answer": "D",
      "explanation": "Dynamic runtime memory allocations reside on the Heap, which grows upward toward higher addresses."
    },
    {
      "id": "TEST-01-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Two Pointers (Opposite Direction)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Two Pointers (Opposite Direction)' pattern operates with O(N) Time, O(1) Auxiliary Space: Exploits the monotonic ordering of sorted elements to eliminate half of unexamined candidates at each step in O(1) time without nested loops.."
    },
    {
      "id": "TEST-01-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Two Pointers (Opposite Direction)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Array of length 2.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Two Pointers (Opposite Direction) include Array of length 2, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-01-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Two Sum II — Input Array Is Sorted', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-01-19",
      "category": "Projects (SmartGalla)",
      "question": "In Sarthak's project 'SmartGalla', what is the core architectural principle regarding 'Multi-Tenant Architecture & Tech Stack Selection (Next.js 16, React 19, Supabase)'?",
      "options": [
        "Next.js App Router server components execute on the server, streaming HTML with zero client bundle overhead for catalog views.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For SmartGalla, the architectural invariant is: Next.js App Router server components execute on the server, streaming HTML with zero client bundle overhead for catalog views.."
    },
    {
      "id": "TEST-01-20",
      "category": "Projects (SmartGalla)",
      "question": "Regarding 'SmartGalla', how should you defend this design decision in a technical interview: 'Why did you choose Next.js 16 with Supabase for SmartGalla instead of a standard MERN stack?'?",
      "options": [
        "SmartGalla is a multi-tenant retail and inventory platform where catalog SEO, fast cold starts, and strict tenant isolation are vital. Next.js 16 provides Serve...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: SmartGalla is a multi-tenant retail and inventory platform where catalog SEO, fast cold starts, and strict tenant isolation are vital. Next.."
    }
  ],
  "2": [
    {
      "id": "TEST-02-01",
      "category": "Academic (Knowledge Management)",
      "question": "Which of the following is NOT one of the three primary architectural subsystems of a classical Decision Support System (DSS)?",
      "options": [
        "Database Management Subsystem (DBMS)",
        "Model Base Management Subsystem (MBMS)",
        "User Interface / Dialog Subsystem",
        "Packet Switching Subsystem"
      ],
      "correct_answer": "D",
      "explanation": "A DSS architecture consists of three fundamental components: Data Management (DBMS), Model Management (MBMS), and Dialog/User Interface."
    },
    {
      "id": "TEST-02-02",
      "category": "Academic (Knowledge Management)",
      "question": "How does a Management Information System (MIS) fundamentally differ from a Decision Support System (DSS)?",
      "options": [
        "MIS focuses on ad-hoc interactive simulation, while DSS provides static scheduled reports",
        "MIS produces structured periodic summaries of past operational data, while DSS provides interactive 'what-if' modeling for semi-structured decisions",
        "MIS is only used by top executives, while DSS is used by data entry clerks",
        "MIS does not require a database, whereas DSS requires a data warehouse"
      ],
      "correct_answer": "B",
      "explanation": "MIS supports structured, routine operations with fixed scheduled reports; DSS is designed for ad-hoc, flexible, what-if exploratory modeling of semi-structured problems."
    },
    {
      "id": "TEST-02-03",
      "category": "Academic (Knowledge Management)",
      "question": "What is the primary function of the Model Base Management Subsystem (MBMS) in a DSS?",
      "options": [
        "Storing raw SQL transaction tables",
        "Managing, updating, and executing mathematical, financial, and simulation models",
        "Rendering HTML CSS graphics on the client",
        "Encrypting database disk partitions"
      ],
      "correct_answer": "B",
      "explanation": "MBMS manages the catalog of quantitative models (statistical, financial, optimization, forecasting) and couples them with data to generate scenarios."
    },
    {
      "id": "TEST-02-04",
      "category": "Academic (Knowledge Management)",
      "question": "In DSS sensitivity analysis, what does a 'Goal Seeking' query determine?",
      "options": [
        "The output metric given fixed input parameters",
        "The required value of an input variable needed to achieve a specified target output",
        "The maximum bandwidth of the network connection",
        "The number of concurrent database sessions"
      ],
      "correct_answer": "B",
      "explanation": "Goal seeking (backward sensitivity analysis) calculates the input variable adjustments required to reach a specific desired target result."
    },
    {
      "id": "TEST-02-05",
      "category": "Academic (Knowledge Management)",
      "question": "Executive Information Systems (EIS) are distinguished from general DSS by their strong emphasis on:",
      "options": [
        "Low-level assembly language programming",
        "High-level graphical KPI dashboards, drill-down capabilities, and internal/external critical success factors",
        "Batch card punch processing",
        "Hardware register allocation"
      ],
      "correct_answer": "B",
      "explanation": "EIS is tailored for senior leadership, emphasizing intuitive visual interfaces, drill-down summaries, and status tracking of Critical Success Factors (CSFs)."
    },
    {
      "id": "TEST-02-06",
      "category": "Placement Aptitude",
      "question": "A vendor bought lemons at 6 for Rs. 10 and sold them at 4 for Rs. 9. Find his gain or loss percentage.",
      "options": [
        "35% gain",
        "25% gain",
        "20% loss",
        "30% gain"
      ],
      "correct_answer": "A",
      "explanation": "CP of 1 lemon = 10/6 = Rs. 5/3. SP of 1 lemon = 9/4 = Rs. 2.25. Gain = 9/4 - 5/3 = (27 - 20) / 12 = 7/12. Gain % = (7/12) / (5/3) * 100% = (7/20) * 100% = 35%."
    },
    {
      "id": "TEST-02-07",
      "category": "Placement Aptitude",
      "question": "A grocer marks an article at Rs. 500. After allowing two successive discounts of 20% and 10%, what is the final selling price?",
      "options": [
        "Rs. 360",
        "Rs. 350",
        "Rs. 380",
        "Rs. 340"
      ],
      "correct_answer": "A",
      "explanation": "SP = 500 * (1 - 0.20) * (1 - 0.10) = 500 * 0.80 * 0.90 = 500 * 0.72 = Rs. 360."
    },
    {
      "id": "TEST-02-08",
      "category": "Placement Aptitude",
      "question": "If a trader sells an article at Rs. 450, he incurs a 10% loss. At what price should he sell it to gain 20%?",
      "options": [
        "Rs. 600",
        "Rs. 580",
        "Rs. 620",
        "Rs. 550"
      ],
      "correct_answer": "A",
      "explanation": "CP = 450 / 0.90 = Rs. 500. To gain 20%, target SP = 500 * 1.20 = Rs. 600."
    },
    {
      "id": "TEST-02-09",
      "category": "Placement Aptitude",
      "question": "By selling 33 meters of cloth, a merchant gains the selling price of 11 meters. What is his gain percentage?",
      "options": [
        "50%",
        "33.33%",
        "25%",
        "66.67"
      ],
      "correct_answer": "A",
      "explanation": "Profit = 11 SP => 33 SP - 33 CP = 11 SP => 22 SP = 33 CP => SP/CP = 33/22 = 3/2. Gain % = [(3 - 2)/2] * 100% = 50%."
    },
    {
      "id": "TEST-02-10",
      "category": "Placement Aptitude",
      "question": "A watch was sold at 5% loss. Had it been sold for Rs. 56 more, there would have been a gain of 9%. What is the cost price of the watch?",
      "options": [
        "Rs. 400",
        "Rs. 450",
        "Rs. 380",
        "Rs. 500"
      ],
      "correct_answer": "A",
      "explanation": "Total percentage difference = 9% - (-5%) = 14%. 14% of CP = 56 => CP = 56 / 0.14 = Rs. 400."
    },
    {
      "id": "TEST-02-11",
      "category": "Core CS (Operating Systems)",
      "question": "Which CPU scheduling algorithm provides the theoretical minimum average waiting time for a given set of processes?",
      "options": [
        "First-Come, First-Served",
        "Round Robin",
        "Shortest Job First",
        "Priority Scheduling"
      ],
      "correct_answer": "C",
      "explanation": "SJF is provably optimal for minimizing average waiting time by executing shorter bursts first."
    },
    {
      "id": "TEST-02-12",
      "category": "Core CS (Operating Systems)",
      "question": "The technique of gradually increasing the priority of processes that wait in the system for a long time is called:",
      "options": [
        "Paging",
        "Aging",
        "Throttling",
        "Belady's adjustment"
      ],
      "correct_answer": "B",
      "explanation": "Aging prevents starvation in priority queues by systematically boosting waiting processes."
    },
    {
      "id": "TEST-02-13",
      "category": "Core CS (Operating Systems)",
      "question": "If the time quantum of a Round Robin scheduler is extremely large, it behaves identically to:",
      "options": [
        "SJF",
        "SRTF",
        "FCFS",
        "Multilevel Feedback Queue"
      ],
      "correct_answer": "C",
      "explanation": "When quantum exceeds the longest burst, every process completes in arrival order without preemption, mimicking FCFS."
    },
    {
      "id": "TEST-02-14",
      "category": "Core CS (Operating Systems)",
      "question": "Turnaround time of a process is calculated as:",
      "options": [
        "Waiting Time - Burst Time",
        "Completion Time - Arrival Time",
        "Completion Time - Burst Time",
        "Arrival Time + Burst Time"
      ],
      "correct_answer": "B",
      "explanation": "Turnaround time represents total elapsed lifetime: Completion Time minus Arrival Time."
    },
    {
      "id": "TEST-02-15",
      "category": "Core CS (Operating Systems)",
      "question": "Which algorithm is the preemptive variant of Shortest Job First?",
      "options": [
        "Round Robin",
        "Priority Inversion",
        "Shortest Remaining Time First (SRTF)",
        "Multilevel Queue"
      ],
      "correct_answer": "C",
      "explanation": "SRTF preempts the CPU if a newly arrived process has a remaining burst shorter than current execution."
    },
    {
      "id": "TEST-02-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Sliding Window (Fixed Size)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Sliding Window (Fixed Size)' pattern operates with O(N) Time, O(1) Auxiliary Space: Reuses the computational state of overlapping elements across adjacent windows in O(1) time instead of recomputing from scratch in O(K).."
    },
    {
      "id": "TEST-02-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Sliding Window (Fixed Size)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: k == nums.length.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Sliding Window (Fixed Size) include k == nums.length, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-02-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Maximum Average Subarray I', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-02-19",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "In Sarthak's project 'NSE2 / BulkBeat TV', what is the core architectural principle regarding 'Real-Time Financial Media Ingestion & Concurrency Architecture (Python AsyncIO & aiohttp)'?",
      "options": [
        "AsyncIO runs a single-threaded cooperative event loop where coroutines yield control via `await`, allowing thousands of idle I/O sockets without OS thread overhead.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For NSE2 / BulkBeat TV, the architectural invariant is: AsyncIO runs a single-threaded cooperative event loop where coroutines yield control via `await`, allowing thousands of idle I/O sockets without OS thread overhead.."
    },
    {
      "id": "TEST-02-20",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "Regarding 'NSE2 / BulkBeat TV', how should you defend this design decision in a technical interview: 'How does the NSE2 ingestion engine achieve sub-50ms announcement processing?'?",
      "options": [
        "The engine uses a dedicated `aiohttp.ClientSession` pool with HTTP keep-alive to poll NSE corporate announcement feeds and market disclosure endpoints every 500...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: The engine uses a dedicated `aiohttp.ClientSession` pool with HTTP keep-alive to poll NSE corporate announcement feeds and market disclosure."
    }
  ],
  "3": [
    {
      "id": "TEST-03-01",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which component of the JVM Execution Engine compiles frequently executed bytecode hot-spots into native machine instructions at runtime?",
      "options": [
        "Interpreter",
        "Just-In-Time (JIT) Compiler",
        "Garbage Collector",
        "ClassLoader"
      ],
      "correct_answer": "B",
      "explanation": "The JIT compiler profiles running bytecode and dynamically compiles high-frequency code paths ('hot spots') into native CPU instructions for near-native performance."
    },
    {
      "id": "TEST-03-02",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which runtime data area in the JVM is shared among all concurrent threads?",
      "options": [
        "Java Virtual Machine Stack",
        "Program Counter (PC) Register",
        "Heap Memory Area",
        "Native Method Stack"
      ],
      "correct_answer": "C",
      "explanation": "The Heap and Method Area are created upon JVM startup and shared across all threads. Stacks and PC registers are private to individual threads."
    },
    {
      "id": "TEST-03-03",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What principle governs the ClassLoader subsystem hierarchy when resolving and loading Java classes?",
      "options": [
        "Round-Robin Principle",
        "Delegation-Hierarchy Principle",
        "Least-Recently-Used Principle",
        "First-In-First-Out Principle"
      ],
      "correct_answer": "B",
      "explanation": "Java ClassLoaders follow delegation: a ClassLoader delegates class requests upward to its parent before attempting to load the class itself."
    },
    {
      "id": "TEST-03-04",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which phase of ClassLoader Linking ensures that bytecode conforms to the JVM specification and cannot compromise system security?",
      "options": [
        "Preparation",
        "Resolution",
        "Verification",
        "Initialization"
      ],
      "correct_answer": "C",
      "explanation": "Bytecode Verification checks structural correctness, stack overflow limits, type safety, and memory access integrity before execution."
    },
    {
      "id": "TEST-03-05",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What is stored inside a stack frame allocated on the Java Thread Stack during method execution?",
      "options": [
        "All newly instantiated objects via the 'new' operator",
        "Static class metadata and bytecodes",
        "Local variables table, operand stack, and frame data (return pointer)",
        "Database connection pool sockets"
      ],
      "correct_answer": "C",
      "explanation": "Each method invocation pushes a stack frame containing local variables, the operand stack for calculations, and frame linkage references."
    },
    {
      "id": "TEST-03-06",
      "category": "Placement Aptitude",
      "question": "In how many years will a sum of money double itself at 12.5% per annum simple interest?",
      "options": [
        "8 years",
        "6 years",
        "10 years",
        "7 years"
      ],
      "correct_answer": "A",
      "explanation": "For principal P to double, SI = P. P = (P * 12.5 * T) / 100 => T = 100 / 12.5 = 8 years."
    },
    {
      "id": "TEST-03-07",
      "category": "Placement Aptitude",
      "question": "A sum invested at compound interest doubles itself in 4 years. In how many years will it amount to 8 times the original sum?",
      "options": [
        "12 years",
        "16 years",
        "8 years",
        "10 years"
      ],
      "correct_answer": "A",
      "explanation": "If amount = 2P in 4 years, then 8P = (2^3)P takes 3 * 4 = 12 years."
    },
    {
      "id": "TEST-03-08",
      "category": "Placement Aptitude",
      "question": "What is the simple interest on Rs. 4,500 at 8% per annum for 3 years and 4 months?",
      "options": [
        "Rs. 1,200",
        "Rs. 1,180",
        "Rs. 1,250",
        "Rs. 1,150"
      ],
      "correct_answer": "A",
      "explanation": "Time = 3 + 4/12 = 3 + 1/3 = 10/3 years. SI = (4,500 * 8 * 10) / (100 * 3) = 15 * 80 = Rs. 1,200."
    },
    {
      "id": "TEST-03-09",
      "category": "Placement Aptitude",
      "question": "What is the compound interest on Rs. 10,000 for 2 years at 10% per annum, compounded annually?",
      "options": [
        "Rs. 2,100",
        "Rs. 2,000",
        "Rs. 2,200",
        "Rs. 1,900"
      ],
      "correct_answer": "A",
      "explanation": "Amount = 10,000 * (1.10)^2 = 10,000 * 1.21 = Rs. 12,100. CI = 12,100 - 10,000 = Rs. 2,100."
    },
    {
      "id": "TEST-03-10",
      "category": "Placement Aptitude",
      "question": "The difference between CI and SI on a certain sum at 5% per annum for 2 years is Rs. 15. What is the principal sum?",
      "options": [
        "Rs. 6,000",
        "Rs. 5,000",
        "Rs. 6,500",
        "Rs. 5,500"
      ],
      "correct_answer": "A",
      "explanation": "Difference = P * (R/100)^2 => 15 = P * (5/100)^2 = P * (1/400) => P = 15 * 400 = Rs. 6,000."
    },
    {
      "id": "TEST-03-11",
      "category": "Core CS (Operating Systems)",
      "question": "Which of the following is NOT a mandatory condition for solving the Critical Section problem?",
      "options": [
        "Mutual Exclusion",
        "Progress",
        "Preemptive Priority Assignment",
        "Bounded Waiting"
      ],
      "correct_answer": "C",
      "explanation": "The three requirements are Mutual Exclusion, Progress, and Bounded Waiting."
    },
    {
      "id": "TEST-03-12",
      "category": "Core CS (Operating Systems)",
      "question": "A counting semaphore initialized to 7 has 4 wait() operations and 2 signal() operations applied. Its final value is:",
      "options": [
        "3",
        "5",
        "9",
        "1"
      ],
      "correct_answer": "B",
      "explanation": "Initial = 7. 4 wait() decrement by 4 (7 - 4 = 3). 2 signal() increment by 2 (3 + 2 = 5)."
    },
    {
      "id": "TEST-03-13",
      "category": "Core CS (Operating Systems)",
      "question": "A major difference between a Mutex and a Semaphore is:",
      "options": [
        "Semaphores cannot be used in multithreading",
        "A Mutex can only be unlocked by the thread that acquired it",
        "Mutex values can be negative",
        "Semaphores cannot enforce mutual exclusion"
      ],
      "correct_answer": "B",
      "explanation": "Mutexes enforce strict thread ownership; semaphores can be signaled by any thread."
    },
    {
      "id": "TEST-03-14",
      "category": "Core CS (Operating Systems)",
      "question": "A situation where a high-priority thread is indirectly delayed by a medium-priority thread preempting a low-priority lock holder is called:",
      "options": [
        "Deadlock",
        "Priority Inversion",
        "Convoy Effect",
        "Thrashing"
      ],
      "correct_answer": "B",
      "explanation": "Priority Inversion occurs when a medium-priority process blocks a lower-priority process holding a resource needed by a high-priority process."
    },
    {
      "id": "TEST-03-15",
      "category": "Core CS (Operating Systems)",
      "question": "In a spinlock, a thread waiting for a resource:",
      "options": [
        "Transitions to the blocked/sleep state",
        "Continuously loops in user space checking the lock",
        "Releases its virtual address space",
        "Is re-parented to init"
      ],
      "correct_answer": "B",
      "explanation": "Spinlocks use busy-waiting loops, holding the CPU while polling the lock condition."
    },
    {
      "id": "TEST-03-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Sliding Window (Dynamic / Variable Size)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Sliding Window (Dynamic / Variable Size)' pattern operates with O(N) Time, O(1) Auxiliary Space: Both pointers move monotonically forward from 0 to N - 1. Each element enters and leaves the window at most once, guaranteeing strict O(N) runtime.."
    },
    {
      "id": "TEST-03-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Sliding Window (Dynamic / Variable Size)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Sum of all elements < target.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Sliding Window (Dynamic / Variable Size) include Sum of all elements < target, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-03-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Minimum Size Subarray Sum', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-03-19",
      "category": "Projects (Caloriv)",
      "question": "In Sarthak's project 'Caloriv', what is the core architectural principle regarding 'Cross-Platform Mobile App Architecture with React Native & Expo'?",
      "options": [
        "React Native renders real native Android and iOS UI components via the native bridge, offering 60 FPS scrolling compared to webview wrappers.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Caloriv, the architectural invariant is: React Native renders real native Android and iOS UI components via the native bridge, offering 60 FPS scrolling compared to webview wrappers.."
    },
    {
      "id": "TEST-03-20",
      "category": "Projects (Caloriv)",
      "question": "Regarding 'Caloriv', how should you defend this design decision in a technical interview: 'Why build Caloriv with React Native Expo instead of native Kotlin/Swift?'?",
      "options": [
        "Caloriv required rapid feature iteration across both Android and iOS with a single unified TypeScript codebase. Expo provides pre-built native module bindings f...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Caloriv required rapid feature iteration across both Android and iOS with a single unified TypeScript codebase. Expo provides pre-built nati."
    }
  ],
  "4": [
    {
      "id": "TEST-04-01",
      "category": "Academic (Computer Networks)",
      "question": "In the ISO-OSI 7-Layer Reference Model, which layer is responsible for dialog control, token management, and session checkpointing?",
      "options": [
        "Transport Layer",
        "Session Layer",
        "Presentation Layer",
        "Data Link Layer"
      ],
      "correct_answer": "B",
      "explanation": "Layer 5 (Session Layer) establishes, manages, synchronizes, and terminates sessions between end-user applications with checkpoints."
    },
    {
      "id": "TEST-04-02",
      "category": "Academic (Computer Networks)",
      "question": "What is the Protocol Data Unit (PDU) name at the Network Layer of the OSI model?",
      "options": [
        "Frame",
        "Segment",
        "Packet",
        "Bit"
      ],
      "correct_answer": "C",
      "explanation": "PDU names across layers: Physical = Bit, Data Link = Frame, Network = Packet, Transport = Segment, Application = Data/Message."
    },
    {
      "id": "TEST-04-03",
      "category": "Academic (Computer Networks)",
      "question": "Which layer in the OSI reference model handles data syntax conversion, compression, and encryption/decryption (e.g., ASN.1, SSL/TLS)?",
      "options": [
        "Presentation Layer",
        "Application Layer",
        "Session Layer",
        "Network Layer"
      ],
      "correct_answer": "A",
      "explanation": "Layer 6 (Presentation Layer) standardizes data formats, handles character set translations (ASCII/EBCDIC), data compression, and cryptographic encryption."
    },
    {
      "id": "TEST-04-04",
      "category": "Academic (Computer Networks)",
      "question": "How does the TCP/IP architectural suite map the top three layers of the OSI reference model (Session, Presentation, Application)?",
      "options": [
        "They are split across Network Access and Internet layers",
        "They are combined into a single unified Application Layer",
        "They are moved into operating system kernel device drivers",
        "They are replaced by the Transport Layer"
      ],
      "correct_answer": "B",
      "explanation": "The 4-layer TCP/IP model consolidates OSI's Application, Presentation, and Session layers into a single top-level Application Layer."
    },
    {
      "id": "TEST-04-05",
      "category": "Academic (Computer Networks)",
      "question": "Which layer provides true end-to-end reliability and process-to-process communication using port numbers?",
      "options": [
        "Network Layer",
        "Transport Layer",
        "Data Link Layer",
        "Physical Layer"
      ],
      "correct_answer": "B",
      "explanation": "The Transport Layer (TCP/UDP) uses 16-bit port addresses to deliver data process-to-process with end-to-end flow and error control."
    },
    {
      "id": "TEST-04-06",
      "category": "Placement Aptitude",
      "question": "If A : B = 2 : 3 and B : C = 4 : 5, find the compound ratio A : B : C.",
      "options": [
        "8 : 12 : 15",
        "6 : 9 : 15",
        "8 : 10 : 15",
        "2 : 4 : 5"
      ],
      "correct_answer": "A",
      "explanation": "A : B = 8 : 12 (multiplying by 4). B : C = 12 : 15 (multiplying by 3). Hence A : B : C = 8 : 12 : 15."
    },
    {
      "id": "TEST-04-07",
      "category": "Placement Aptitude",
      "question": "Divide Rs. 1,050 among A, B, and C in the ratio 2 : 3 : 5. What is C's share?",
      "options": [
        "Rs. 525",
        "Rs. 450",
        "Rs. 500",
        "Rs. 550"
      ],
      "correct_answer": "A",
      "explanation": "Total ratio units = 2 + 3 + 5 = 10 units. Value of 1 unit = 1,050 / 10 = Rs. 105. C's share = 5 * 105 = Rs. 525."
    },
    {
      "id": "TEST-04-08",
      "category": "Placement Aptitude",
      "question": "Two numbers are in the ratio 3 : 5. If 9 is subtracted from each, the new ratio becomes 12 : 23. What is the smaller number?",
      "options": [
        "33",
        "27",
        "30",
        "36"
      ],
      "correct_answer": "A",
      "explanation": "Let numbers be 3x and 5x. (3x - 9)/(5x - 9) = 12/23 => 23(3x - 9) = 12(5x - 9) => 69x - 207 = 60x - 108 => 9x = 99 => x = 11. Smaller = 3 * 11 = 33."
    },
    {
      "id": "TEST-04-09",
      "category": "Placement Aptitude",
      "question": "What is the fourth proportional to 4, 9, and 12?",
      "options": [
        "27",
        "24",
        "28",
        "30"
      ],
      "correct_answer": "A",
      "explanation": "4 / 9 = 12 / x => 4x = 108 => x = 27."
    },
    {
      "id": "TEST-04-10",
      "category": "Placement Aptitude",
      "question": "Three partners A, B, and C invest capital in the ratio 5 : 7 : 6. If their profit sharing ratio at the end of the year is 5 : 7 : 6, what is their investment duration ratio?",
      "options": [
        "1 : 1 : 1",
        "2 : 3 : 4",
        "5 : 7 : 6",
        "6 : 7 : 5"
      ],
      "correct_answer": "A",
      "explanation": "Profit = Capital * Time. Since profit ratio equals capital ratio, Time ratio must be 1 : 1 : 1."
    },
    {
      "id": "TEST-04-11",
      "category": "Core CS (Operating Systems)",
      "question": "In the Bounded Buffer problem of size N, what are the initial values of semaphores empty, full, and mutex?",
      "options": [
        "empty = 0, full = N, mutex = 0",
        "empty = N, full = 0, mutex = 1",
        "empty = 1, full = 1, mutex = N",
        "empty = N, full = N, mutex = 1"
      ],
      "correct_answer": "B",
      "explanation": "Initially all N slots are empty (empty = N), 0 slots are filled (full = 0), and mutex is unlocked (1)."
    },
    {
      "id": "TEST-04-12",
      "category": "Core CS (Operating Systems)",
      "question": "If all philosophers pick up their left chopstick simultaneously in Dining Philosophers, the system experiences:",
      "options": [
        "Thrashing",
        "Deadlock",
        "High throughput",
        "Cache invalidation"
      ],
      "correct_answer": "B",
      "explanation": "All philosophers hold one chopstick and wait for the other, forming an unbreakable circular wait deadlock."
    },
    {
      "id": "TEST-04-13",
      "category": "Core CS (Operating Systems)",
      "question": "Which Readers-Writers solution policy risks writer starvation?",
      "options": [
        "Writer-preference",
        "Fair FIFO queue",
        "Reader-preference",
        "Strict alternating"
      ],
      "correct_answer": "C",
      "explanation": "In reader-preference, as long as readers keep arriving, writers are indefinitely postponed."
    },
    {
      "id": "TEST-04-14",
      "category": "Core CS (Operating Systems)",
      "question": "In the Bounded Buffer solution, reversing wait(mutex) and wait(empty) in the producer causes:",
      "options": [
        "Faster throughput",
        "Buffer overflow",
        "Potential deadlock when buffer is full",
        "Data corruption"
      ],
      "correct_answer": "C",
      "explanation": "Holding mutex while blocked on empty prevents the consumer from entering to free up buffer space, causing deadlock."
    },
    {
      "id": "TEST-04-15",
      "category": "Core CS (Operating Systems)",
      "question": "An asymmetric solution to the Dining Philosophers problem specifies that:",
      "options": [
        "Philosophers eat with only one chopstick",
        "Odd philosophers pick left first, even philosophers pick right first",
        "All philosophers pick right first",
        "Philosophers never release chopsticks"
      ],
      "correct_answer": "B",
      "explanation": "Alternating the pickup order breaks the circular wait condition necessary for deadlock."
    },
    {
      "id": "TEST-04-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Fast & Slow Pointers (Floyd's Tortoise and Hare)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Fast & Slow Pointers (Floyd's Tortoise and Hare)' pattern operates with O(N) Time, O(1) Auxiliary Space: In a cycle of length C, the relative distance between slow and fast decreases by exactly 1 in each step. Hence, fast must overtake slow within C iterations without using extra memory.."
    },
    {
      "id": "TEST-04-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Fast & Slow Pointers (Floyd's Tortoise and Hare)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Empty list (null head).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Fast & Slow Pointers (Floyd's Tortoise and Hare) include Empty list (null head), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-04-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Middle of the Linked List', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-04-19",
      "category": "Projects (Biometric Electronic Voting System (BEVM))",
      "question": "In Sarthak's project 'Biometric Electronic Voting System (BEVM)', what is the core architectural principle regarding 'Tamper-Evident Cryptographic Ledger & Chained SHA-256 Audit Hashes'?",
      "options": [
        "Sequential cryptographic hash chaining guarantees historical immutability. If any past ballot is modified, all descendant block hashes fail validation.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Biometric Electronic Voting System (BEVM), the architectural invariant is: Sequential cryptographic hash chaining guarantees historical immutability. If any past ballot is modified, all descendant block hashes fail validation.."
    },
    {
      "id": "TEST-04-20",
      "category": "Projects (Biometric Electronic Voting System (BEVM))",
      "question": "Regarding 'Biometric Electronic Voting System (BEVM)', how should you defend this design decision in a technical interview: 'How does the Biometric Electronic Voting System (BEVM) prevent retroactive ballot tampering?'?",
      "options": [
        "BEVM implements an append-only cryptographic ledger. Each cast vote record includes the SHA-256 hash of the immediately preceding ballot block alongside timesta...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: BEVM implements an append-only cryptographic ledger. Each cast vote record includes the SHA-256 hash of the immediately preceding ballot blo."
    }
  ],
  "5": [
    {
      "id": "TEST-05-01",
      "category": "Academic (Numerical Methods)",
      "question": "If the true value is X and the computed approximate value is X*, what is the mathematical formula for Relative Error (Er)?",
      "options": [
        "|X - X*|",
        "|X - X*| / |X|",
        "(|X - X*| / |X|) * 100",
        "|X - X*| * |X|"
      ],
      "correct_answer": "B",
      "explanation": "Absolute Error Ea = |X - X*|. Relative Error Er = Ea / |X| = |X - X*| / |X|. Percentage Error Ep = Er * 100%."
    },
    {
      "id": "TEST-05-02",
      "category": "Academic (Numerical Methods)",
      "question": "What is the rate of convergence of the Bisection Method for finding the real root of a continuous equation f(x) = 0?",
      "options": [
        "Quadratic (order 2)",
        "Linear (order 1) with convergence factor 0.5",
        "Superlinear (order 1.618)",
        "Cubic (order 3)"
      ],
      "correct_answer": "B",
      "explanation": "The Bisection method halves the interval bracket at each step (e_{n+1} = 0.5 * e_n), giving linear convergence with an asymptotic error factor of 1/2."
    },
    {
      "id": "TEST-05-03",
      "category": "Academic (Numerical Methods)",
      "question": "According to the Intermediate Value Theorem, what condition must continuous function f(x) satisfy on interval [a, b] to guarantee at least one real root?",
      "options": [
        "f(a) * f(b) > 0",
        "f(a) * f(b) < 0",
        "f'(a) = f'(b)",
        "f(a) + f(b) = 0"
      ],
      "correct_answer": "B",
      "explanation": "If f(x) is continuous and f(a) and f(b) have opposite signs (f(a)*f(b) < 0), Bolzano's theorem guarantees at least one root c in (a, b) such that f(c) = 0."
    },
    {
      "id": "TEST-05-04",
      "category": "Academic (Numerical Methods)",
      "question": "What is Truncation Error in numerical computation?",
      "options": [
        "Error introduced by hardware word-length rounding (e.g., 32-bit float limits)",
        "Error resulting from replacing an infinite mathematical process with a finite approximation (e.g., truncating a Taylor series)",
        "Mistakes made by the programmer entering data",
        "Error caused by noisy transmission channels"
      ],
      "correct_answer": "B",
      "explanation": "Truncation error occurs when an exact mathematical operation (like infinite series summation or differentiation limits) is truncated to a finite formula."
    },
    {
      "id": "TEST-05-05",
      "category": "Academic (Numerical Methods)",
      "question": "To achieve an accuracy of epsilon = 10^-3 starting from an initial bracket of length (b - a) = 1, approximately how many Bisection iterations are required?",
      "options": [
        "4 iterations",
        "7 iterations",
        "10 iterations",
        "25 iterations"
      ],
      "correct_answer": "C",
      "explanation": "Interval length after n steps is (b - a)/2^n <= epsilon => 1/2^n <= 10^-3 => 2^n >= 1000 => n >= 10 (since 2^10 = 1024)."
    },
    {
      "id": "TEST-05-06",
      "category": "Placement Aptitude",
      "question": "The average of 7 consecutive numbers is 20. What is the largest of these numbers?",
      "options": [
        "23",
        "22",
        "24",
        "25"
      ],
      "correct_answer": "A",
      "explanation": "In 7 consecutive numbers, the average 20 is the middle (4th) number. The numbers are 17, 18, 19, 20, 21, 22, 23. The largest is 23."
    },
    {
      "id": "TEST-05-07",
      "category": "Placement Aptitude",
      "question": "A batsman in his 17th innings makes a score of 85, thereby increasing his average by 3 runs. What is his average after the 17th innings?",
      "options": [
        "37",
        "34",
        "39",
        "35"
      ],
      "correct_answer": "A",
      "explanation": "Let previous average be x. Total runs in 17 innings = 16x + 85 = 17(x + 3) => 16x + 85 = 17x + 51 => x = 34. New average = 34 + 3 = 37."
    },
    {
      "id": "TEST-05-08",
      "category": "Placement Aptitude",
      "question": "In what ratio must grocer mix coffee powder costing Rs. 250/kg with coffee powder costing Rs. 150/kg so that the mixture is worth Rs. 210/kg?",
      "options": [
        "3 : 2",
        "2 : 3",
        "4 : 3",
        "3 : 1"
      ],
      "correct_answer": "A",
      "explanation": "By Alligation: Ratio of Expensive (250) to Cheaper (150) with Mean (210) = (210 - 150) / (250 - 210) = 60 / 40 = 3 : 2."
    },
    {
      "id": "TEST-05-09",
      "category": "Placement Aptitude",
      "question": "The average age of 24 students and their teacher is 15 years. If the teacher's age is excluded, the average age decreases by 1 year. What is the teacher's age?",
      "options": [
        "39 years",
        "38 years",
        "40 years",
        "35 years"
      ],
      "correct_answer": "A",
      "explanation": "Total age with teacher = 25 * 15 = 375. Total age of 24 students = 24 * 14 = 336. Teacher's age = 375 - 336 = 39 years."
    },
    {
      "id": "TEST-05-10",
      "category": "Placement Aptitude",
      "question": "The average of 50 numbers is 38. If two numbers namely 45 and 55 are discarded, what is the average of the remaining numbers?",
      "options": [
        "37.5",
        "37",
        "38",
        "36.5"
      ],
      "correct_answer": "A",
      "explanation": "Sum of 50 numbers = 50 * 38 = 1,900. Discarded sum = 45 + 55 = 100. Remaining sum = 1,800. Remaining count = 48. New average = 1,800 / 48 = 37.5."
    },
    {
      "id": "TEST-05-11",
      "category": "Core CS (Operating Systems)",
      "question": "Which of the following is NOT one of the 4 Coffman conditions for deadlock?",
      "options": [
        "Mutual Exclusion",
        "Hold and Wait",
        "Process Aging",
        "Circular Wait"
      ],
      "correct_answer": "C",
      "explanation": "The 4 conditions are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait."
    },
    {
      "id": "TEST-05-12",
      "category": "Core CS (Operating Systems)",
      "question": "If a Resource Allocation Graph contains a cycle and every resource type has exactly one single instance, then:",
      "options": [
        "A deadlock definitely exists",
        "A deadlock may or may not exist",
        "The system is guaranteed safe",
        "The CPU enters thrashing"
      ],
      "correct_answer": "A",
      "explanation": "With single-instance resources, a cycle in the RAG is both necessary and sufficient for deadlock."
    },
    {
      "id": "TEST-05-13",
      "category": "Core CS (Operating Systems)",
      "question": "The Banker's Algorithm is primarily used for:",
      "options": [
        "Deadlock Prevention",
        "Deadlock Avoidance",
        "Deadlock Detection",
        "Memory Compaction"
      ],
      "correct_answer": "B",
      "explanation": "Banker's Algorithm is a dynamic deadlock avoidance technique that checks for safe execution sequences."
    },
    {
      "id": "TEST-05-14",
      "category": "Core CS (Operating Systems)",
      "question": "In a system with Need matrix, how is Need calculated in Banker's Algorithm?",
      "options": [
        "Allocation - Available",
        "Max - Allocation",
        "Max + Available",
        "Allocation - Max"
      ],
      "correct_answer": "B",
      "explanation": "Need represents remaining resources a process may claim: Need = Max - Allocation."
    },
    {
      "id": "TEST-05-15",
      "category": "Core CS (Operating Systems)",
      "question": "Assigning global numerical IDs to resources and enforcing acquisition in ascending order eliminates which condition?",
      "options": [
        "Mutual Exclusion",
        "Hold and Wait",
        "No Preemption",
        "Circular Wait"
      ],
      "correct_answer": "D",
      "explanation": "Strict resource ordering prevents cycles from forming, eliminating Circular Wait."
    },
    {
      "id": "TEST-05-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Monotonic Stack (Next Greater Element)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(N) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Monotonic Stack (Next Greater Element)' pattern operates with O(N) Time, O(N) Auxiliary Space: Every element is pushed onto the stack exactly once and popped at most once, yielding strictly linear O(N) aggregate runtime.."
    },
    {
      "id": "TEST-05-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Monotonic Stack (Next Greater Element)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Strictly decreasing sequence (all answers 0).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Monotonic Stack (Next Greater Element) include Strictly decreasing sequence (all answers 0), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-05-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Daily Temperatures', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(N) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(N) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-05-19",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "In Sarthak's project 'College Student Management System (CSMS)', what is the core architectural principle regarding 'Multi-Role Authentication & Bcrypt Password Security in CSMS'?",
      "options": [
        "Passwords are never stored in plaintext; `bcrypt` salt rounds ensure cryptographic resistance against dictionary attacks.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For College Student Management System (CSMS), the architectural invariant is: Passwords are never stored in plaintext; `bcrypt` salt rounds ensure cryptographic resistance against dictionary attacks.."
    },
    {
      "id": "TEST-05-20",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "Regarding 'College Student Management System (CSMS)', how should you defend this design decision in a technical interview: 'How is authentication handled in CSMS across different academic roles?'?",
      "options": [
        "In `backend/routers/auth.py`, the login endpoint authenticates both faculty/administrators via email from the `admins` table and students via their University E...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: In `backend/routers/auth.py`, the login endpoint authenticates both faculty/administrators via email from the `admins` table and students vi."
    }
  ],
  "6": [
    {
      "id": "TEST-06-01",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which method in Java is invoked to initiate the concurrent execution of a new thread created via Thread class or Runnable interface?",
      "options": [
        "run()",
        "start()",
        "init()",
        "execute()"
      ],
      "correct_answer": "B",
      "explanation": "Calling start() requests the JVM to allocate a new native thread call stack and invoke the run() method asynchronously. Calling run() directly runs synchronously on the caller's thread."
    },
    {
      "id": "TEST-06-02",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What happens when a thread enters a method marked with the 'synchronized' keyword in Java?",
      "options": [
        "The thread acquires the intrinsic lock (monitor) associated with the target object",
        "The thread is immediately put into the DEAD state",
        "The JVM disables garbage collection for all heaps",
        "The thread's priority is automatically raised to MAX_PRIORITY"
      ],
      "correct_answer": "A",
      "explanation": "Every Java object has an intrinsic monitor lock. Synchronized methods/blocks acquire this lock, preventing other threads from executing synchronized code on that object until released."
    },
    {
      "id": "TEST-06-03",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which method releases the monitor lock and suspends the calling thread until another thread invokes notify() or notifyAll() on the same object?",
      "options": [
        "sleep()",
        "yield()",
        "wait()",
        "join()"
      ],
      "correct_answer": "C",
      "explanation": "Object.wait() must be called from within a synchronized context; it atomically releases the object monitor and places the thread into the object's wait set."
    },
    {
      "id": "TEST-06-04",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What is the primary advantage of implementing the Runnable interface over extending the Thread class in Java?",
      "options": [
        "Runnable threads execute 10x faster than Thread subclasses",
        "Since Java does not support multiple class inheritance, implementing Runnable leaves the class free to extend another base class",
        "Runnable does not require overriding the run() method",
        "Runnable automatically prevents deadlocks"
      ],
      "correct_answer": "B",
      "explanation": "Java supports single class inheritance. Implementing Runnable allows the class to extend another business class while decoupling the task from the thread runner."
    },
    {
      "id": "TEST-06-05",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What happens to a Daemon thread in Java when all non-daemon user threads finish executing?",
      "options": [
        "The JVM continues running until the daemon thread finishes",
        "The JVM terminates immediately, abruptly stopping all daemon threads",
        "The daemon thread is automatically converted into a user thread",
        "The JVM throws a ThreadDeathException"
      ],
      "correct_answer": "B",
      "explanation": "Daemon threads (like GC) provide background services. The JVM exits as soon as all user (non-daemon) threads terminate, killing any active daemon threads."
    },
    {
      "id": "TEST-06-06",
      "category": "Placement Aptitude",
      "question": "A can complete a work in 10 days and B can complete it in 15 days. Working together, in how many days can they complete the work?",
      "options": [
        "6 days",
        "5 days",
        "7 days",
        "8 days"
      ],
      "correct_answer": "A",
      "explanation": "Total work = LCM(10, 15) = 30 units. A's rate = 3 units/day, B's rate = 2 units/day. Combined rate = 5 units/day. Time = 30 / 5 = 6 days."
    },
    {
      "id": "TEST-06-07",
      "category": "Placement Aptitude",
      "question": "A and B together can do a piece of work in 12 days, B and C in 15 days, and C and A in 20 days. In how many days can A, B, and C together finish it?",
      "options": [
        "10 days",
        "8 days",
        "12 days",
        "15 days"
      ],
      "correct_answer": "A",
      "explanation": "LCM(12, 15, 20) = 60 units. 2(A + B + C) = 5 + 4 + 3 = 12 units/day => A + B + C = 6 units/day. Time = 60 / 6 = 10 days."
    },
    {
      "id": "TEST-06-08",
      "category": "Placement Aptitude",
      "question": "A is twice as efficient as B and takes 30 days less than B to complete a piece of work. In how many days can B alone complete the work?",
      "options": [
        "60 days",
        "50 days",
        "40 days",
        "75 days"
      ],
      "correct_answer": "A",
      "explanation": "Efficiency ratio A : B = 2 : 1 => Time ratio A : B = 1 : 2. Difference in time = 1 unit = 30 days. B's time = 2 * 30 = 60 days."
    },
    {
      "id": "TEST-06-09",
      "category": "Placement Aptitude",
      "question": "12 men can complete a work in 8 days. After 3 days of work, 3 more men joined them. How many more days will they take to complete the remaining work?",
      "options": [
        "4 days",
        "5 days",
        "3.5 days",
        "4.5 days"
      ],
      "correct_answer": "A",
      "explanation": "Total work = 12 * 8 = 96 man-days. Work done in 3 days = 12 * 3 = 36 man-days. Remaining work = 96 - 36 = 60 man-days. New men count = 15. Days needed = 60 / 15 = 4 days."
    },
    {
      "id": "TEST-06-10",
      "category": "Placement Aptitude",
      "question": "A can do a piece of work in 14 days and B in 21 days. They begin together but 3 days before the completion of the work, A leaves. What is the total duration of the work?",
      "options": [
        "10.2 days",
        "9 days",
        "11 days",
        "12 days"
      ],
      "correct_answer": "A",
      "explanation": "LCM(14, 21) = 42 units. A=3 u/d, B=2 u/d. In the last 3 days, B works alone: 3 * 2 = 6 units. Remaining 36 units done by (A+B): 36 / 5 = 7.2 days. Total = 7.2 + 3 = 10.2 days."
    },
    {
      "id": "TEST-06-11",
      "category": "Core CS (Operating Systems)",
      "question": "In a paging memory system, which type of fragmentation can still occur?",
      "options": [
        "External fragmentation only",
        "Internal fragmentation only",
        "Both internal and external",
        "Neither type"
      ],
      "correct_answer": "B",
      "explanation": "Paging eliminates external fragmentation, but the last allocated page may not be completely filled, causing internal fragmentation."
    },
    {
      "id": "TEST-06-12",
      "category": "Core CS (Operating Systems)",
      "question": "A system uses 4KB pages. How many bits are needed for the page offset?",
      "options": [
        "10 bits",
        "12 bits",
        "16 bits",
        "20 bits"
      ],
      "correct_answer": "B",
      "explanation": "4 KB = 4096 bytes = 2^12 bytes, so 12 bits are needed for offset."
    },
    {
      "id": "TEST-06-13",
      "category": "Core CS (Operating Systems)",
      "question": "The hardware component that maps virtual addresses to physical addresses at runtime is the:",
      "options": [
        "ALU",
        "MMU (Memory Management Unit)",
        "DMA Controller",
        "Interrupt Handler"
      ],
      "correct_answer": "B",
      "explanation": "The MMU contains the hardware logic and TLB to translate virtual memory addresses to physical RAM."
    },
    {
      "id": "TEST-06-14",
      "category": "Core CS (Operating Systems)",
      "question": "If TLB access takes 10ns and RAM access takes 100ns, what is access time on a TLB hit?",
      "options": [
        "10ns",
        "100ns",
        "110ns",
        "210ns"
      ],
      "correct_answer": "C",
      "explanation": "On a TLB hit, the MMU accesses the TLB (10ns) then fetches data from RAM (100ns), totaling 110ns."
    },
    {
      "id": "TEST-06-15",
      "category": "Core CS (Operating Systems)",
      "question": "In Segmentation, a logical address consists of:",
      "options": [
        "Page number and frame offset",
        "Segment number and offset",
        "Base register and limit register",
        "PID and socket ID"
      ],
      "correct_answer": "B",
      "explanation": "Segmentation addresses specify a segment identifier and offset within that segment."
    },
    {
      "id": "TEST-06-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Binary Search on Sorted Arrays' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(log N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Binary Search on Sorted Arrays' pattern operates with O(log N) Time, O(1) Auxiliary Space: Eliminates 50% of candidate search space each step: T(n) = T(n/2) + O(1) => O(log N).."
    },
    {
      "id": "TEST-06-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Binary Search on Sorted Arrays' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Target smaller than nums[0].",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Binary Search on Sorted Arrays include Target smaller than nums[0], which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-06-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Search Insert Position', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(1) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(log N) Time, O(1) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-06-19",
      "category": "Projects (SmartGalla)",
      "question": "In Sarthak's project 'SmartGalla', what is the core architectural principle regarding 'Payment Gateway Integration & Webhook Idempotency (Razorpay & COD Ledger)'?",
      "options": [
        "HMAC-SHA256 signature verification prevents man-in-the-middle payment spoofing.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For SmartGalla, the architectural invariant is: HMAC-SHA256 signature verification prevents man-in-the-middle payment spoofing.."
    },
    {
      "id": "TEST-06-20",
      "category": "Projects (SmartGalla)",
      "question": "Regarding 'SmartGalla', how should you defend this design decision in a technical interview: 'How do you handle Razorpay webhook idempotency in SmartGalla?'?",
      "options": [
        "When a customer pays, Razorpay sends an asynchronous webhook (`payment.captured` or `order.paid`). Because network retries can send the same webhook multiple ti...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: When a customer pays, Razorpay sends an asynchronous webhook (`payment.captured` or `order.paid`). Because network retries can send the same."
    }
  ],
  "7": [
    {
      "id": "TEST-07-01",
      "category": "Academic (Knowledge Management)",
      "question": "In the Cyclic Redundancy Check (CRC) error detection mechanism, what mathematical operation is used in the polynomial modulo-2 arithmetic?",
      "options": [
        "Standard integer long division with carry",
        "Bitwise XOR (Exclusive-OR) without carry",
        "Bitwise AND operation",
        "Floating point division"
      ],
      "correct_answer": "B",
      "explanation": "Modulo-2 polynomial arithmetic uses XOR for both addition and subtraction, with zero carry or borrow operations."
    },
    {
      "id": "TEST-07-02",
      "category": "Academic (Knowledge Management)",
      "question": "If a generator polynomial G(x) has degree r, how many zero bits are appended to the original message bitstream before performing CRC division?",
      "options": [
        "r - 1 zeros",
        "r zeros",
        "r + 1 zeros",
        "2r zeros"
      ],
      "correct_answer": "B",
      "explanation": "To calculate the r-bit remainder (FCS checksum), exactly r zeros (corresponding to the polynomial degree) are appended to the message bit sequence."
    },
    {
      "id": "TEST-07-03",
      "category": "Academic (Knowledge Management)",
      "question": "To detect 'd' single-bit transmission errors in a block of data, the minimum Hamming distance of the code must be:",
      "options": [
        "d",
        "d + 1",
        "2d",
        "2d + 1"
      ],
      "correct_answer": "B",
      "explanation": "To detect d single-bit errors, minimum Hamming distance d_min >= d + 1. To correct t single-bit errors, d_min >= 2t + 1."
    },
    {
      "id": "TEST-07-04",
      "category": "Academic (Knowledge Management)",
      "question": "In byte stuffing (character-oriented framing), what escape character is inserted when the data payload itself contains the special FLAG byte?",
      "options": [
        "SYN",
        "ESC",
        "ETX",
        "SOH"
      ],
      "correct_answer": "B",
      "explanation": "Byte stuffing prefixes an ESC (Escape) byte before any accidental occurrence of FLAG or ESC bytes in the data payload."
    },
    {
      "id": "TEST-07-05",
      "category": "Academic (Knowledge Management)",
      "question": "In bit-oriented framing (HDLC protocol), bit stuffing inserts a '0' bit after encountering:",
      "options": [
        "Three consecutive 1s",
        "Five consecutive 1s",
        "Seven consecutive 1s",
        "Eight consecutive 0s"
      ],
      "correct_answer": "B",
      "explanation": "To prevent user data from mimicking the 01111110 FLAG delimiter, the sender automatically stuffs a '0' after any sequence of five consecutive '1's."
    },
    {
      "id": "TEST-07-06",
      "category": "Placement Aptitude",
      "question": "Two pipes A and B can fill a tank in 20 minutes and 30 minutes respectively. If both pipes are opened together, how long will it take to fill the tank?",
      "options": [
        "12 minutes",
        "10 minutes",
        "15 minutes",
        "14 minutes"
      ],
      "correct_answer": "A",
      "explanation": "LCM(20, 30) = 60 units. A rate = 3 u/min, B rate = 2 u/min. Joint rate = 5 u/min. Time = 60 / 5 = 12 minutes."
    },
    {
      "id": "TEST-07-07",
      "category": "Placement Aptitude",
      "question": "A pipe can fill a cistern in 12 hours. Due to a leak in the bottom, it takes 15 hours to fill it. If the cistern is full, how long will the leak take to empty it?",
      "options": [
        "60 hours",
        "50 hours",
        "45 hours",
        "75 hours"
      ],
      "correct_answer": "A",
      "explanation": "Pipe rate = +1/12. Net rate = +1/15. Leak rate = 1/12 - 1/15 = (5 - 4) / 60 = 1/60. The leak will empty the cistern in 60 hours."
    },
    {
      "id": "TEST-07-08",
      "category": "Placement Aptitude",
      "question": "Pipe A can fill a tank in 16 hours and Pipe B in 24 hours. A third pipe C can empty it in 48 hours. If all three are opened together, how long to fill the tank?",
      "options": [
        "12 hours",
        "10 hours",
        "14 hours",
        "15 hours"
      ],
      "correct_answer": "A",
      "explanation": "LCM(16, 24, 48) = 48 units. A = +3, B = +2, C = -1. Net rate = 3 + 2 - 1 = 4 units/hour. Time = 48 / 4 = 12 hours."
    },
    {
      "id": "TEST-07-09",
      "category": "Placement Aptitude",
      "question": "A cistern has two taps which fill it in 12 minutes and 15 minutes respectively. There is also a waste pipe. When all three are open, the empty cistern is full in 20 minutes. How long will the waste pipe take to empty the full cistern?",
      "options": [
        "10 minutes",
        "12 minutes",
        "15 minutes",
        "8 minutes"
      ],
      "correct_answer": "A",
      "explanation": "LCM(12, 15, 20) = 60. T1 = +5, T2 = +4, Net = +3. Waste pipe rate = 5 + 4 - 3 = 6 units/min. Time to empty = 60 / 6 = 10 minutes."
    },
    {
      "id": "TEST-07-10",
      "category": "Placement Aptitude",
      "question": "Two pipes can fill a tank in 18 hours and 24 hours. Both pipes are opened together. After how much time should the first pipe be closed so that the tank is full in 16 hours?",
      "options": [
        "6 hours",
        "8 hours",
        "5 hours",
        "7 hours"
      ],
      "correct_answer": "A",
      "explanation": "LCM(18, 24) = 72 units. P1 = 4 u/hr, P2 = 3 u/hr. Pipe 2 runs for the entire 16 hours: 16 * 3 = 48 units. Pipe 1 fills remaining 72 - 48 = 24 units: 24 / 4 = 6 hours."
    },
    {
      "id": "TEST-07-11",
      "category": "Core CS (Operating Systems)",
      "question": "Belady's Anomaly is observed in which page replacement algorithm?",
      "options": [
        "LRU",
        "Optimal",
        "FIFO",
        "MRU"
      ],
      "correct_answer": "C",
      "explanation": "FIFO does not satisfy the inclusion property, causing Belady's anomaly where more frames cause more faults."
    },
    {
      "id": "TEST-07-12",
      "category": "Core CS (Operating Systems)",
      "question": "What is the primary indicator that an OS has entered Thrashing?",
      "options": [
        "CPU utilization near 100% with no page faults",
        "Excessive disk swap I/O and collapsing CPU utilization",
        "Network latency spikes",
        "Deadlock on thread mutexes"
      ],
      "correct_answer": "B",
      "explanation": "Thrashing manifests as continuous page swapping and low CPU utilization."
    },
    {
      "id": "TEST-07-13",
      "category": "Core CS (Operating Systems)",
      "question": "The Dirty Bit (Modify Bit) in a page table entry indicates whether the page has been:",
      "options": [
        "Read by CPU",
        "Modified in RAM since being loaded from disk",
        "Referenced by another thread",
        "Allocated in BSS"
      ],
      "correct_answer": "B",
      "explanation": "The dirty bit tracks writes to determine if the page must be written back to disk on eviction."
    },
    {
      "id": "TEST-07-14",
      "category": "Core CS (Operating Systems)",
      "question": "Which page replacement algorithm is theoretically optimal but impossible to implement in practice?",
      "options": [
        "FIFO",
        "LRU",
        "OPT (Belady's Optimal)",
        "Second-Chance"
      ],
      "correct_answer": "C",
      "explanation": "OPT requires future knowledge of memory references, which cannot be known in advance."
    },
    {
      "id": "TEST-07-15",
      "category": "Core CS (Operating Systems)",
      "question": "A Page Fault is serviced by:",
      "options": [
        "The application runtime",
        "The CPU ALU",
        "The Operating System Kernel",
        "The Network Interface Card"
      ],
      "correct_answer": "C",
      "explanation": "Page faults trigger a kernel interrupt, which schedules disk I/O to load the page."
    },
    {
      "id": "TEST-07-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Binary Search on Rotated Sorted Arrays' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(log N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Binary Search on Rotated Sorted Arrays' pattern operates with O(log N) Time, O(1) Auxiliary Space: Preserves the O(log N) divide-and-conquer property by discarding one half at each decision point.."
    },
    {
      "id": "TEST-07-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Binary Search on Rotated Sorted Arrays' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Rotation at index 0 (unrotated).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Binary Search on Rotated Sorted Arrays include Rotation at index 0 (unrotated), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-07-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Find Minimum in Rotated Sorted Array', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(1) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(log N) Time, O(1) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-07-19",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "In Sarthak's project 'NSE2 / BulkBeat TV', what is the core architectural principle regarding 'Database Concurrency & Lock Elimination in SQLite (Write-Ahead Logging & Single-Writer Queue)'?",
      "options": [
        "PRAGMA journal_mode=WAL; allows readers to query previous database snapshots while a writer appends to the -wal file.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For NSE2 / BulkBeat TV, the architectural invariant is: PRAGMA journal_mode=WAL; allows readers to query previous database snapshots while a writer appends to the -wal file.."
    },
    {
      "id": "TEST-07-20",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "Regarding 'NSE2 / BulkBeat TV', how should you defend this design decision in a technical interview: 'Why did SQLite throw 'database is locked' errors in NSE2, and how did you permanently fix it?'?",
      "options": [
        "Default SQLite uses rollback journaling, where any write operation places an exclusive write lock on the entire database file, preventing concurrent reads. Duri...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Default SQLite uses rollback journaling, where any write operation places an exclusive write lock on the entire database file, preventing co."
    }
  ],
  "8": [
    {
      "id": "TEST-08-01",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "In Nonaka and Takeuchi's SECI model of Knowledge Creation, what transformation mode represents converting Tacit Knowledge into Explicit Knowledge?",
      "options": [
        "Socialization",
        "Externalization",
        "Combination",
        "Internalization"
      ],
      "correct_answer": "B",
      "explanation": "Externalization articulates unspoken, subjective tacit insights into explicit concepts, metaphors, models, and written diagrams."
    },
    {
      "id": "TEST-08-02",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which SECI quadrant describes apprentices learning tacit craft skills from a master artisan through shared observation, imitation, and practice without written manuals?",
      "options": [
        "Socialization (Tacit to Tacit)",
        "Combination (Explicit to Explicit)",
        "Internalization (Explicit to Tacit)",
        "Externalization (Tacit to Explicit)"
      ],
      "correct_answer": "A",
      "explanation": "Socialization transfers tacit knowledge directly between individuals through shared physical experience, apprenticeship, and informal dialogue."
    },
    {
      "id": "TEST-08-03",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What is the defining characteristic of Tacit Knowledge compared to Explicit Knowledge?",
      "options": [
        "It is easily indexed, codified, and stored in relational database tables",
        "It is personal, context-specific, rooted in action, commitment, and heuristics, making it hard to formalize",
        "It can be transmitted instantly over a network socket as JSON",
        "It is only possessed by machines and software algorithms"
      ],
      "correct_answer": "B",
      "explanation": "Tacit knowledge is intuitive, deeply ingrained in human experience and mental models ('we know more than we can tell', Michael Polanyi)."
    },
    {
      "id": "TEST-08-04",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "In the DIKW hierarchy, which layer adds actionable rules, context, and experience to raw processed information?",
      "options": [
        "Data",
        "Information",
        "Knowledge",
        "Wisdom"
      ],
      "correct_answer": "C",
      "explanation": "DIKW pyramid: Data (raw symbols) -> Information (contextualized data) -> Knowledge (actionable understanding and rules) -> Wisdom (evaluated judgment)."
    },
    {
      "id": "TEST-08-05",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which SECI quadrant involves integrating multiple documents, databases, and financial spreadsheets into a unified organizational repository?",
      "options": [
        "Internalization",
        "Externalization",
        "Socialization",
        "Combination"
      ],
      "correct_answer": "D",
      "explanation": "Combination synthesizes disparate pieces of explicit knowledge by sorting, aggregating, and re-categorizing them into new explicit documents."
    },
    {
      "id": "TEST-08-06",
      "category": "Placement Aptitude",
      "question": "A train 150 meters long passes an electric pole in 10 seconds. What is the speed of the train in km/hr?",
      "options": [
        "54 km/hr",
        "45 km/hr",
        "60 km/hr",
        "50 km/hr"
      ],
      "correct_answer": "A",
      "explanation": "Speed = Distance / Time = 150 / 10 = 15 m/s. Convert to km/hr: 15 * (18 / 5) = 54 km/hr."
    },
    {
      "id": "TEST-08-07",
      "category": "Placement Aptitude",
      "question": "A train 280 meters long is traveling at 63 km/hr. How much time will it take to pass a railway platform 420 meters long?",
      "options": [
        "40 seconds",
        "35 seconds",
        "45 seconds",
        "50 seconds"
      ],
      "correct_answer": "A",
      "explanation": "Total distance = 280 + 420 = 700 meters. Speed = 63 * (5/18) = 17.5 m/s. Time = 700 / 17.5 = 40 seconds."
    },
    {
      "id": "TEST-08-08",
      "category": "Placement Aptitude",
      "question": "Two trains 140 m and 160 m long run at speeds of 60 km/hr and 48 km/hr respectively in opposite directions on parallel tracks. In what time will they cross each other?",
      "options": [
        "10 seconds",
        "12 seconds",
        "8 seconds",
        "15 seconds"
      ],
      "correct_answer": "A",
      "explanation": "Total distance = 140 + 160 = 300 m. Relative speed = 60 + 48 = 108 km/hr = 108 * (5/18) = 30 m/s. Time = 300 / 30 = 10 seconds."
    },
    {
      "id": "TEST-08-09",
      "category": "Placement Aptitude",
      "question": "A man walking at 5 km/hr crosses a bridge in 15 minutes. What is the length of the bridge in meters?",
      "options": [
        "1,250 meters",
        "1,500 meters",
        "1,000 meters",
        "1,200 meters"
      ],
      "correct_answer": "A",
      "explanation": "Speed = 5 * (5/18) = 25/18 m/s. Time = 15 * 60 = 900 seconds. Distance = (25/18) * 900 = 1,250 meters."
    },
    {
      "id": "TEST-08-10",
      "category": "Placement Aptitude",
      "question": "If a person walks at 14 km/hr instead of 10 km/hr, he would have walked 20 km more in the same time. What was the actual distance traveled by him?",
      "options": [
        "50 km",
        "60 km",
        "45 km",
        "70 km"
      ],
      "correct_answer": "A",
      "explanation": "Let time be t hours. 14t - 10t = 20 => 4t = 20 => t = 5 hours. Actual distance = 10 * 5 = 50 km."
    },
    {
      "id": "TEST-08-11",
      "category": "Core CS (DBMS)",
      "question": "Which level of the ANSI-SPARC 3-tier architecture describes the physical storage of data on disk?",
      "options": [
        "External level",
        "Conceptual level",
        "Internal level",
        "Logical level"
      ],
      "correct_answer": "C",
      "explanation": "The Internal (Physical) level describes how data is organized as blocks and indexes on disk."
    },
    {
      "id": "TEST-08-12",
      "category": "Core CS (DBMS)",
      "question": "The rule stating that a Foreign Key value must either match a Primary Key in the referenced relation or be NULL is:",
      "options": [
        "Domain Constraint",
        "Entity Integrity",
        "Referential Integrity",
        "Key Constraint"
      ],
      "correct_answer": "C",
      "explanation": "Referential Integrity ensures child foreign keys point to valid existing parent rows."
    },
    {
      "id": "TEST-08-13",
      "category": "Core CS (DBMS)",
      "question": "Which SQL command is a DDL command that removes all rows from a table by deallocating data pages?",
      "options": [
        "DELETE",
        "TRUNCATE",
        "DROP TABLE",
        "REMOVE"
      ],
      "correct_answer": "B",
      "explanation": "TRUNCATE deallocates data pages quickly without individual row logging."
    },
    {
      "id": "TEST-08-14",
      "category": "Core CS (DBMS)",
      "question": "The ability to modify the conceptual schema without altering existing user views is known as:",
      "options": [
        "Physical Data Independence",
        "Logical Data Independence",
        "Data Redundancy",
        "Transaction Isolation"
      ],
      "correct_answer": "B",
      "explanation": "Logical Data Independence shields user views from modifications to logical tables."
    },
    {
      "id": "TEST-08-15",
      "category": "Core CS (DBMS)",
      "question": "Entity Integrity rule explicitly prohibits which of the following?",
      "options": [
        "Duplicate foreign keys",
        "A Primary Key containing a NULL value",
        "Secondary indexes",
        "Composite attributes"
      ],
      "correct_answer": "B",
      "explanation": "Entity Integrity dictates that primary key attributes cannot be NULL."
    },
    {
      "id": "TEST-08-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Linked List In-Place Reversal' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Linked List In-Place Reversal' pattern operates with O(N) Time, O(1) Auxiliary Space: Mutates next pointers directly in a single linear pass with O(1) auxiliary space.."
    },
    {
      "id": "TEST-08-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Linked List In-Place Reversal' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Empty list (head == null).",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Linked List In-Place Reversal include Empty list (head == null), which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-08-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Reverse Linked List II', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-08-19",
      "category": "Projects (Caloriv)",
      "question": "In Sarthak's project 'Caloriv', what is the core architectural principle regarding 'Android Build Toolchain, SDK Management & Production Gradle Orchestration'?",
      "options": [
        "`./gradlew assembleRelease` compiles native Java/Kotlin code, packages Hermes bytecode, and signs the release APK.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Caloriv, the architectural invariant is: `./gradlew assembleRelease` compiles native Java/Kotlin code, packages Hermes bytecode, and signs the release APK.."
    },
    {
      "id": "TEST-08-20",
      "category": "Projects (Caloriv)",
      "question": "Regarding 'Caloriv', how should you defend this design decision in a technical interview: 'What challenges did you face configuring the Android build toolchain for Caloriv, and how did you resolve them?'?",
      "options": [
        "Upgrading to modern React Native versions introduced build failures with Java 17 and Android Gradle Plugin (AGP) incompatibilities. I resolved this by authoring...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Upgrading to modern React Native versions introduced build failures with Java 17 and Android Gradle Plugin (AGP) incompatibilities. I resolv."
    }
  ],
  "9": [
    {
      "id": "TEST-09-01",
      "category": "Academic (Computer Networks)",
      "question": "What is the order of convergence for the Newton-Raphson iterative method for solving f(x) = 0 with simple roots?",
      "options": [
        "1 (Linear)",
        "1.618 (Golden ratio)",
        "2 (Quadratic)",
        "3 (Cubic)"
      ],
      "correct_answer": "C",
      "explanation": "Newton-Raphson exhibits quadratic convergence (order 2), meaning the number of correct decimal places approximately doubles each iteration."
    },
    {
      "id": "TEST-09-02",
      "category": "Academic (Computer Networks)",
      "question": "What is the Newton-Raphson iteration formula for finding root x_{n+1} from current estimate x_n?",
      "options": [
        "x_{n+1} = x_n - f(x_n) / f'(x_n)",
        "x_{n+1} = x_n + f(x_n) / f'(x_n)",
        "x_{n+1} = x_n - f'(x_n) / f(x_n)",
        "x_{n+1} = [x_n + f(x_n)] / 2"
      ],
      "correct_answer": "A",
      "explanation": "Newton-Raphson uses the tangent slope at x_n: x_{n+1} = x_n - f(x_n) / f'(x_n)."
    },
    {
      "id": "TEST-09-03",
      "category": "Academic (Computer Networks)",
      "question": "Under what condition does the Newton-Raphson method fail or breakdown completely?",
      "options": [
        "When f(x_n) = 0",
        "When f'(x_n) = 0 (tangent line is parallel to x-axis)",
        "When f''(x_n) > 0",
        "When the initial guess is an integer"
      ],
      "correct_answer": "B",
      "explanation": "If the first derivative f'(x_n) becomes zero, division by zero occurs because the tangent line is horizontal and never intersects the x-axis."
    },
    {
      "id": "TEST-09-04",
      "category": "Academic (Computer Networks)",
      "question": "How does the Regula-Falsi (False Position) method differ geometrically from the Bisection method?",
      "options": [
        "It uses the arithmetic midpoint (a + b) / 2 to divide the interval",
        "It connects (a, f(a)) and (b, f(b)) with a secant straight line and finds its x-intercept",
        "It uses the tangent line at the midpoint",
        "It requires evaluating the second derivative"
      ],
      "correct_answer": "B",
      "explanation": "Regula-Falsi replaces the midpoint subdivision with the x-intercept of the secant chord joining (a, f(a)) and (b, f(b)): c = [a*f(b) - b*f(a)] / [f(b) - f(a)]."
    },
    {
      "id": "TEST-09-05",
      "category": "Academic (Computer Networks)",
      "question": "Using the Newton-Raphson iteration formula x_{n+1} = 0.5 * (x_n + N / x_n), what value is being computed?",
      "options": [
        "N^2",
        "1 / N",
        "sqrt(N)",
        "log(N)"
      ],
      "correct_answer": "C",
      "explanation": "Applying Newton-Raphson to f(x) = x^2 - N = 0 yields x_{n+1} = x_n - (x_n^2 - N)/(2x_n) = 0.5 * (x_n + N / x_n), which computes sqrt(N)."
    },
    {
      "id": "TEST-09-06",
      "category": "Placement Aptitude",
      "question": "A boat can travel with a speed of 13 km/hr in still water. If the speed of the stream is 4 km/hr, find the time taken by the boat to go 68 km downstream.",
      "options": [
        "4 hours",
        "5 hours",
        "3.5 hours",
        "4.5 hours"
      ],
      "correct_answer": "A",
      "explanation": "Downstream speed = 13 + 4 = 17 km/hr. Time = 68 / 17 = 4 hours."
    },
    {
      "id": "TEST-09-07",
      "category": "Placement Aptitude",
      "question": "A boat running upstream takes 8 hours 48 minutes to cover a certain distance, while it takes 4 hours to cover the same distance downstream. What is the ratio between the speed of the boat and speed of the water current?",
      "options": [
        "8 : 3",
        "7 : 3",
        "5 : 2",
        "9 : 4"
      ],
      "correct_answer": "A",
      "explanation": "Upstream time = 8 + 48/60 = 8.8 hrs = 44/5 hrs. Downstream time = 4 hrs. Distance is equal: (u - v) * (44/5) = (u + v) * 4 => 11(u - v) = 5(u + v) => 6u = 16v => u/v = 16/6 = 8/3."
    },
    {
      "id": "TEST-09-08",
      "category": "Placement Aptitude",
      "question": "A man rows downstream 32 km and 14 km upstream, taking 6 hours for each journey. What is the velocity of the current?",
      "options": [
        "1.5 km/hr",
        "2 km/hr",
        "1 km/hr",
        "2.5 km/hr"
      ],
      "correct_answer": "A",
      "explanation": "Downstream speed D = 32 / 6 km/hr. Upstream speed U = 14 / 6 km/hr. Speed of current = (D - U) / 2 = [(32 - 14)/6] / 2 = (18 / 6) / 2 = 3 / 2 = 1.5 km/hr."
    },
    {
      "id": "TEST-09-09",
      "category": "Placement Aptitude",
      "question": "A motorboat whose speed in still water is 15 km/hr goes 30 km downstream and comes back in a total of 4 hours 30 minutes. What is the speed of the stream?",
      "options": [
        "5 km/hr",
        "4 km/hr",
        "6 km/hr",
        "3 km/hr"
      ],
      "correct_answer": "A",
      "explanation": "30/(15 + v) + 30/(15 - v) = 4.5 => 30 [ 30 / (225 - v^2) ] = 4.5 => 900 / (225 - v^2) = 4.5 => 225 - v^2 = 200 => v^2 = 25 => v = 5 km/hr."
    },
    {
      "id": "TEST-09-10",
      "category": "Placement Aptitude",
      "question": "Two cyclists start from the same point on a circular track of 600 meters in the same direction at speeds of 10 m/s and 15 m/s. When will they meet for the first time?",
      "options": [
        "120 seconds",
        "60 seconds",
        "90 seconds",
        "150 seconds"
      ],
      "correct_answer": "A",
      "explanation": "Relative speed in same direction = 15 - 10 = 5 m/s. Time to meet = Track length / Relative speed = 600 / 5 = 120 seconds."
    },
    {
      "id": "TEST-09-11",
      "category": "Core CS (DBMS)",
      "question": "Which relational algebra operator selects specific columns from a relation?",
      "options": [
        "Selection (sigma)",
        "Projection (pi)",
        "Cartesian Product (X)",
        "Join (bowtie)"
      ],
      "correct_answer": "B",
      "explanation": "Projection (pi) extracts specified attribute columns and removes duplicate rows."
    },
    {
      "id": "TEST-09-12",
      "category": "Core CS (DBMS)",
      "question": "Which clause must be used to filter groups based on aggregate function values in SQL?",
      "options": [
        "WHERE",
        "HAVING",
        "GROUP BY",
        "ORDER BY"
      ],
      "correct_answer": "B",
      "explanation": "HAVING filters groups post-aggregation; WHERE cannot take aggregate functions."
    },
    {
      "id": "TEST-09-13",
      "category": "Core CS (DBMS)",
      "question": "If Table A has 5 rows and Table B has 4 rows, how many rows are returned by a CROSS JOIN?",
      "options": [
        "9",
        "20",
        "1",
        "5"
      ],
      "correct_answer": "B",
      "explanation": "CROSS JOIN produces the Cartesian product: 5 * 4 = 20 rows."
    },
    {
      "id": "TEST-09-14",
      "category": "Core CS (DBMS)",
      "question": "If two employees tie for salary rank 2, what rank will DENSE_RANK() assign to the next employee?",
      "options": [
        "3",
        "4",
        "2",
        "NULL"
      ],
      "correct_answer": "A",
      "explanation": "DENSE_RANK() does not skip rank values after ties: 1, 2, 2, 3."
    },
    {
      "id": "TEST-09-15",
      "category": "Core CS (DBMS)",
      "question": "A LEFT OUTER JOIN returns:",
      "options": [
        "Only matching rows from both tables",
        "All rows from the left table and matched rows from the right table",
        "Only non-matching rows from left table",
        "All rows from right table only"
      ],
      "correct_answer": "B",
      "explanation": "LEFT JOIN preserves every row from the left relation, filling NULL for unmatched right attributes."
    },
    {
      "id": "TEST-09-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Fast & Slow Pointers (Cycle & Midpoint)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Fast & Slow Pointers (Cycle & Midpoint)' pattern operates with O(N) Time, O(1) Auxiliary Space: If list head is distance L from cycle entry, and collision occurs at distance k from entry: L = (m * C) - k. Resetting one pointer to head aligns both at cycle entry.."
    },
    {
      "id": "TEST-09-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Fast & Slow Pointers (Cycle & Midpoint)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: No cycle present.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Fast & Slow Pointers (Cycle & Midpoint) include No cycle present, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-09-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Find the Duplicate Number', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-09-19",
      "category": "Projects (Biometric Electronic Voting System (BEVM))",
      "question": "In Sarthak's project 'Biometric Electronic Voting System (BEVM)', what is the core architectural principle regarding 'Symmetric Ballot Payload Encryption with Fernet AES-256 & Key Management'?",
      "options": [
        "Fernet AES-256 provides both confidentiality and message integrity; without the physical `secret.key`, database files cannot be decrypted or inspected.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Biometric Electronic Voting System (BEVM), the architectural invariant is: Fernet AES-256 provides both confidentiality and message integrity; without the physical `secret.key`, database files cannot be decrypted or inspected.."
    },
    {
      "id": "TEST-09-20",
      "category": "Projects (Biometric Electronic Voting System (BEVM))",
      "question": "Regarding 'Biometric Electronic Voting System (BEVM)', how should you defend this design decision in a technical interview: 'Why use Fernet encryption rather than storing raw vote tallies in SQLite?'?",
      "options": [
        "In electronic voting, physical access to the polling terminal could allow malicious actors to inspect intermediate voting trends before polling closes. Storing ...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: In electronic voting, physical access to the polling terminal could allow malicious actors to inspect intermediate voting trends before poll."
    }
  ],
  "10": [
    {
      "id": "TEST-10-01",
      "category": "Academic (Numerical Methods)",
      "question": "In the Java Collections Framework, what is the key difference between ArrayList and LinkedList for positional index-based retrieval (get(i))?",
      "options": [
        "ArrayList is O(1) random access, while LinkedList is O(N) sequential traversal",
        "ArrayList is O(N) and LinkedList is O(1)",
        "Both provide O(1) lookup",
        "LinkedList consumes less memory per node than ArrayList"
      ],
      "correct_answer": "A",
      "explanation": "ArrayList is backed by a contiguous array, allowing O(1) random index access. LinkedList requires traversing node pointers from head/tail in O(N)."
    },
    {
      "id": "TEST-10-02",
      "category": "Academic (Numerical Methods)",
      "question": "How does HashMap in Java 8+ handle severe hash collisions inside a single bucket when the chain length exceeds TREEIFY_THRESHOLD (8)?",
      "options": [
        "It drops incoming keys with a HashCollisionException",
        "It converts the linked list bucket into a balanced Red-Black Tree, improving lookup from O(N) to O(log N)",
        "It increases heap allocation by 10x immediately",
        "It converts the hash table into an array of linked lists"
      ],
      "correct_answer": "B",
      "explanation": "Java 8 optimizes hash collisions: once a bucket's linked list reaches 8 nodes (and table capacity >= 64), it morphs into a Red-Black Tree for O(log N) search."
    },
    {
      "id": "TEST-10-03",
      "category": "Academic (Numerical Methods)",
      "question": "Which of the following collection classes is synchronized and thread-safe by default in Java?",
      "options": [
        "java.util.ArrayList",
        "java.util.HashMap",
        "java.util.Vector",
        "java.util.HashSet"
      ],
      "correct_answer": "C",
      "explanation": "Vector and Hashtable are legacy collections whose methods are synchronized. Modern code uses ConcurrentHashMap or Collections.synchronizedList()."
    },
    {
      "id": "TEST-10-04",
      "category": "Academic (Numerical Methods)",
      "question": "What is the default initial capacity and default load factor of a java.util.HashMap?",
      "options": [
        "Capacity = 10, Load Factor = 0.5",
        "Capacity = 16, Load Factor = 0.75",
        "Capacity = 32, Load Factor = 0.8",
        "Capacity = 64, Load Factor = 1.0"
      ],
      "correct_answer": "B",
      "explanation": "By default, HashMap initializes with a bucket array capacity of 16 and a load factor of 0.75 (rehashing occurs when size reaches 16 * 0.75 = 12)."
    },
    {
      "id": "TEST-10-05",
      "category": "Academic (Numerical Methods)",
      "question": "What contract must be maintained between the equals() and hashCode() methods in Java?",
      "options": [
        "If two objects have the same hashCode, they must be equal via equals()",
        "If two objects are equal according to equals(), they must produce the same integer hashCode",
        "hashCode() must return a prime number for all objects",
        "equals() cannot be overridden without declaring the class final"
      ],
      "correct_answer": "B",
      "explanation": "The Java contract requires: if `a.equals(b)` is true, then `a.hashCode() == b.hashCode()` must strictly hold to ensure correct behavior in hash collections."
    },
    {
      "id": "TEST-10-06",
      "category": "Placement Aptitude",
      "question": "In how many different ways can the letters of the word 'OPTICAL' be arranged so that the vowels always come together?",
      "options": [
        "720",
        "120",
        "480",
        "5040"
      ],
      "correct_answer": "A",
      "explanation": "Vowels: O, I, A (3 vowels). Consonants: P, T, C, L (4 consonants). Treat (OIA) as 1 unit. Total units = 5. Arrangements = 5! * 3! = 120 * 6 = 720."
    },
    {
      "id": "TEST-10-07",
      "category": "Placement Aptitude",
      "question": "How many 4-digit numbers can be formed using the digits 1, 2, 3, 4, 5, 6 without any repetition of digits?",
      "options": [
        "360",
        "720",
        "120",
        "240"
      ],
      "correct_answer": "A",
      "explanation": "Number of permutations = P(6, 4) = 6 * 5 * 4 * 3 = 360."
    },
    {
      "id": "TEST-10-08",
      "category": "Placement Aptitude",
      "question": "In how many ways can a cricket team of 11 players be chosen from 15 players if a particular player is always selected?",
      "options": [
        "1,001",
        "1,365",
        "960",
        "1,200"
      ],
      "correct_answer": "A",
      "explanation": "Since 1 player is fixed, choose 10 remaining players from 14: 14C10 = 14C4 = (14 * 13 * 12 * 11) / (4 * 3 * 2 * 1) = 1,001."
    },
    {
      "id": "TEST-10-09",
      "category": "Placement Aptitude",
      "question": "How many chords can be drawn through 21 points situated on a circle?",
      "options": [
        "210",
        "190",
        "220",
        "180"
      ],
      "correct_answer": "A",
      "explanation": "A chord requires selecting 2 points from 21: 21C2 = (21 * 20) / 2 = 210 chords."
    },
    {
      "id": "TEST-10-10",
      "category": "Placement Aptitude",
      "question": "In how many ways can 5 distinct books be arranged on a shelf?",
      "options": [
        "120",
        "24",
        "60",
        "720"
      ],
      "correct_answer": "A",
      "explanation": "5! = 5 * 4 * 3 * 2 * 1 = 120 ways."
    },
    {
      "id": "TEST-10-11",
      "category": "Core CS (DBMS)",
      "question": "A table is in 2NF if it is in 1NF and contains no:",
      "options": [
        "Transitive dependencies",
        "Partial functional dependencies",
        "Foreign keys",
        "Composite candidate keys"
      ],
      "correct_answer": "B",
      "explanation": "2NF mandates that all non-prime attributes are fully dependent on the complete candidate key."
    },
    {
      "id": "TEST-10-12",
      "category": "Core CS (DBMS)",
      "question": "In 3NF, for every non-trivial functional dependency X -> Y, which condition must hold?",
      "options": [
        "X must be a candidate key and Y must be NULL",
        "X is a Superkey OR Y is a Prime attribute",
        "Both X and Y must be superkeys",
        "Y must be a foreign key"
      ],
      "correct_answer": "B",
      "explanation": "3NF relaxes BCNF by permitting Y to be a prime attribute."
    },
    {
      "id": "TEST-10-13",
      "category": "Core CS (DBMS)",
      "question": "Which normal form requires every determinant to be a Superkey for all non-trivial dependencies?",
      "options": [
        "1NF",
        "2NF",
        "3NF",
        "BCNF"
      ],
      "correct_answer": "D",
      "explanation": "BCNF strictly requires the determinant X to be a superkey for every non-trivial FD X -> Y."
    },
    {
      "id": "TEST-10-14",
      "category": "Core CS (DBMS)",
      "question": "A 1NF relation whose primary key consists of a single column is guaranteed to be in:",
      "options": [
        "2NF",
        "3NF",
        "BCNF",
        "4NF"
      ],
      "correct_answer": "A",
      "explanation": "A single-column key has no proper subkeys, so partial dependencies cannot exist."
    },
    {
      "id": "TEST-10-15",
      "category": "Core CS (DBMS)",
      "question": "The property ensuring that joining decomposed relations does not produce spurious tuples is called:",
      "options": [
        "Dependency Preservation",
        "Lossless Join Property",
        "Referential Closure",
        "Atomicity"
      ],
      "correct_answer": "B",
      "explanation": "Lossless join decomposition ensures original relations can be reconstructed without phantom rows."
    },
    {
      "id": "TEST-10-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Monotonic Deque (Sliding Window Maximum)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(K) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Monotonic Deque (Sliding Window Maximum)' pattern operates with O(N) Time, O(K) Auxiliary Space: Smaller elements that appear before newer larger elements can never be the maximum of any subsequent window and are evicted immediately in O(1) amortized.."
    },
    {
      "id": "TEST-10-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Monotonic Deque (Sliding Window Maximum)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: k == 1.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Monotonic Deque (Sliding Window Maximum) include k == 1, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-10-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Sliding Window Maximum', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(K) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(K) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-10-19",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "In Sarthak's project 'College Student Management System (CSMS)', what is the core architectural principle regarding 'Relational Database Schema Design & Attendance Shortage Engine'?",
      "options": [
        "Attendance threshold formula: Attendance % = (Total Present Days / Total Recorded Class Days) * 100; triggered alerts when < 75%.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For College Student Management System (CSMS), the architectural invariant is: Attendance threshold formula: Attendance % = (Total Present Days / Total Recorded Class Days) * 100; triggered alerts when < 75%.."
    },
    {
      "id": "TEST-10-20",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "Regarding 'College Student Management System (CSMS)', how should you defend this design decision in a technical interview: 'Explain the relational schema design for attendance and grade tracking in CSMS.'?",
      "options": [
        "In `schema.sql`, the schema utilizes PostgreSQL with UUID primary keys. The `attendance` table maintains a compound unique constraint `(student_id, record_date)...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: In `schema.sql`, the schema utilizes PostgreSQL with UUID primary keys. The `attendance` table maintains a compound unique constraint `(stud."
    }
  ],
  "11": [
    {
      "id": "TEST-11-01",
      "category": "Academic (Knowledge Management)",
      "question": "What is the maximum sender window size in the Go-Back-N ARQ protocol using m-bit sequence numbers?",
      "options": [
        "2^m",
        "2^m - 1",
        "2^(m-1)",
        "m^2"
      ],
      "correct_answer": "B",
      "explanation": "In GBN, window size is 2^m - 1 to prevent ambiguity when all ACKs are lost."
    },
    {
      "id": "TEST-11-02",
      "category": "Academic (Knowledge Management)",
      "question": "In Stop-and-Wait ARQ, what sequence numbers are required for packet transmission?",
      "options": [
        "0 and 1 only (1-bit)",
        "0 to 15",
        "0 to 255",
        "Any 32-bit integer"
      ],
      "correct_answer": "A",
      "explanation": "Stop-and-Wait alternates between sequence numbers 0 and 1, requiring only a 1-bit sequence field."
    },
    {
      "id": "TEST-11-03",
      "category": "Academic (Knowledge Management)",
      "question": "What happens in Selective Repeat ARQ when a single frame in the transmission window is corrupted?",
      "options": [
        "Sender retransmits all subsequent frames from that frame onwards",
        "Sender retransmits ONLY the specific unacknowledged frame via NAK/timeout",
        "Receiver resets the entire connection",
        "Sender terminates flow control"
      ],
      "correct_answer": "B",
      "explanation": "Selective Repeat buffers out-of-order frames and requests retransmission of only the lost frame."
    },
    {
      "id": "TEST-11-04",
      "category": "Academic (Knowledge Management)",
      "question": "What is the sender window size in Selective Repeat ARQ using m-bit sequence numbering?",
      "options": [
        "2^m - 1",
        "2^(m - 1)",
        "2^m",
        "m / 2"
      ],
      "correct_answer": "B",
      "explanation": "In Selective Repeat, sender and receiver window sizes are equal to at most 2^(m - 1) to avoid overlap."
    },
    {
      "id": "TEST-11-05",
      "category": "Academic (Knowledge Management)",
      "question": "How is channel link utilization (efficiency U) defined in Stop-and-Wait protocol where propagation time is Tp and transmission time is Tt?",
      "options": [
        "1 / (1 + 2a), where a = Tp / Tt",
        "1 + 2a",
        "2a / (1 + a)",
        "Tt / Tp"
      ],
      "correct_answer": "A",
      "explanation": "Efficiency U = Tt / (Tt + 2Tp) = 1 / (1 + 2a), showing performance degradation over high-latency links."
    },
    {
      "id": "TEST-11-06",
      "category": "Placement Aptitude",
      "question": "A card is drawn at random from a standard deck of 52 cards. What is the probability that the card drawn is a face card (Jack, Queen, King)?",
      "options": [
        "3/13",
        "1/13",
        "4/13",
        "1/4"
      ],
      "correct_answer": "A",
      "explanation": "Total face cards = 4 suits * 3 face cards = 12 cards. Probability = 12 / 52 = 3 / 13."
    },
    {
      "id": "TEST-11-07",
      "category": "Placement Aptitude",
      "question": "Two unbiased dice are tossed. What is the probability that the sum of the scores is a prime number?",
      "options": [
        "5/12",
        "7/18",
        "1/2",
        "1/3"
      ],
      "correct_answer": "A",
      "explanation": "Prime sums can be 2, 3, 5, 7, 11. Counts: 2 (1), 3 (2), 5 (4), 7 (6), 11 (2) = 15 outcomes. Total = 36. Probability = 15 / 36 = 5 / 12."
    },
    {
      "id": "TEST-11-08",
      "category": "Placement Aptitude",
      "question": "A box contains 20 electric bulbs, out of which 4 are defective. Two bulbs are drawn at random without replacement. What is the probability that both are defective?",
      "options": [
        "3/95",
        "1/25",
        "1/20",
        "2/95"
      ],
      "correct_answer": "A",
      "explanation": "Probability = (4/20) * (3/19) = (1/5) * (3/19) = 3 / 95."
    },
    {
      "id": "TEST-11-09",
      "category": "Placement Aptitude",
      "question": "Four fair coins are tossed simultaneously. What is the probability of obtaining exactly two heads?",
      "options": [
        "3/8",
        "1/4",
        "1/2",
        "5/16"
      ],
      "correct_answer": "A",
      "explanation": "Total outcomes = 2^4 = 16. Favorable outcomes = 4C2 = 6. Probability = 6 / 16 = 3 / 8."
    },
    {
      "id": "TEST-11-10",
      "category": "Placement Aptitude",
      "question": "Tickets numbered 1 to 20 are mixed thoroughly and then a ticket is drawn at random. What is the probability that the drawn ticket has a number which is a multiple of 3 or 7?",
      "options": [
        "2/5",
        "1/2",
        "3/10",
        "7/20"
      ],
      "correct_answer": "A",
      "explanation": "Multiples of 3: {3, 6, 9, 12, 15, 18} (6 numbers). Multiples of 7: {7, 14} (2 numbers). No overlap below 20. Total favorable = 8. Probability = 8 / 20 = 2 / 5."
    },
    {
      "id": "TEST-11-11",
      "category": "Core CS (DBMS)",
      "question": "Which ACID property guarantees that all operations of a transaction succeed or none do?",
      "options": [
        "Atomicity",
        "Consistency",
        "Isolation",
        "Durability"
      ],
      "correct_answer": "A",
      "explanation": "Atomicity ensures 'all-or-nothing' execution."
    },
    {
      "id": "TEST-11-12",
      "category": "Core CS (DBMS)",
      "question": "Write-Ahead Logging (WAL) requires that:",
      "options": [
        "Data pages are written before log records",
        "Log records are flushed to non-volatile storage before corresponding data pages are written",
        "Transactions commit without logs",
        "Checkpoints run before every query"
      ],
      "correct_answer": "B",
      "explanation": "WAL mandates logging modifications before data pages touch persistent storage."
    },
    {
      "id": "TEST-11-13",
      "category": "Core CS (DBMS)",
      "question": "A transaction enters the 'Partially Committed' state when:",
      "options": [
        "It begins execution",
        "Its final statement has executed, prior to log disk flush",
        "Its changes are rolled back",
        "A deadlock is detected"
      ],
      "correct_answer": "B",
      "explanation": "Partially committed occurs right after the last operation executes, before log flush."
    },
    {
      "id": "TEST-11-14",
      "category": "Core CS (DBMS)",
      "question": "Which ACID property ensures that committed transactions survive power failures and system crashes?",
      "options": [
        "Atomicity",
        "Consistency",
        "Isolation",
        "Durability"
      ],
      "correct_answer": "D",
      "explanation": "Durability guarantees committed changes persist permanently."
    },
    {
      "id": "TEST-11-15",
      "category": "Core CS (DBMS)",
      "question": "Checkpoints are used in database recovery systems to:",
      "options": [
        "Speed up SQL join processing",
        "Reduce the log volume that must be scanned during recovery",
        "Encrypt password fields",
        "Enforce 3NF schema constraints"
      ],
      "correct_answer": "B",
      "explanation": "Checkpoints limit how far back the recovery manager must scan WAL logs on reboot."
    },
    {
      "id": "TEST-11-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Merge Intervals & Overlap Detection' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N log N) Time, O(N) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Merge Intervals & Overlap Detection' pattern operates with O(N log N) Time, O(N) Auxiliary Space: Sorting imposes monotonic order on start coordinates, guaranteeing that all potential overlaps are contiguous in the sequence.."
    },
    {
      "id": "TEST-11-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Merge Intervals & Overlap Detection' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Single interval.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Merge Intervals & Overlap Detection include Single interval, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-11-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Merge Intervals', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-11-19",
      "category": "Projects (SmartGalla)",
      "question": "In Sarthak's project 'SmartGalla', what is the core architectural principle regarding 'Geospatial Logistics & Automated Delivery Assignment (Google Maps & Leaflet)'?",
      "options": [
        "The Haversine formula calculates great-circle distance between store coordinates and customer addresses: d = 2R * arcsin(sqrt(sin^2(dlat/2) + cos(lat1)*cos(lat2)*sin^2(dlon/2))).",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For SmartGalla, the architectural invariant is: The Haversine formula calculates great-circle distance between store coordinates and customer addresses: d = 2R * arcsin(sqrt(sin^2(dlat/2) + cos(lat1)*cos(lat2)*sin^2(dlon/2))).."
    },
    {
      "id": "TEST-11-20",
      "category": "Projects (SmartGalla)",
      "question": "Regarding 'SmartGalla', how should you defend this design decision in a technical interview: 'How does SmartGalla assign nearby delivery agents to new orders?'?",
      "options": [
        "When an order enters the 'READY_FOR_PICKUP' state, the logistics assignment engine runs a spatial query over active riders within a 5km radius of the merchant's...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: When an order enters the 'READY_FOR_PICKUP' state, the logistics assignment engine runs a spatial query over active riders within a 5km radi."
    }
  ],
  "12": [
    {
      "id": "TEST-12-01",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "In dimensional data warehouse modeling, how is a Star Schema structured?",
      "options": [
        "A central fact table linked directly to denormalized dimension tables",
        "A normalized fact table with multiple parent tables",
        "A completely flat single CSV spreadsheet",
        "A peer-to-peer network of dimension tables"
      ],
      "correct_answer": "A",
      "explanation": "A star schema features a central numeric fact table surrounded by single-level denormalized dimension tables."
    },
    {
      "id": "TEST-12-02",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "How does a Snowflake Schema differ fundamentally from a Star Schema?",
      "options": [
        "The fact table is split into multiple sub-facts",
        "Dimension tables are normalized into 3NF hierarchies, splitting into sub-dimension tables",
        "It does not use foreign keys",
        "It cannot store historical time-series data"
      ],
      "correct_answer": "B",
      "explanation": "Snowflake normalizes dimension tables into multiple related tables, reducing redundancy but increasing join complexity."
    },
    {
      "id": "TEST-12-03",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What characterizes a Fact Table in a Data Warehouse?",
      "options": [
        "Contains descriptive textual names and addresses",
        "Contains quantitative numerical measures (metrics) and foreign keys referencing dimensions",
        "Contains only SQL stored procedures",
        "Stores only network routing tables"
      ],
      "correct_answer": "B",
      "explanation": "Fact tables store additive, semi-additive numerical metrics (e.g., units sold, total revenue) and dimension foreign keys."
    },
    {
      "id": "TEST-12-04",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What are the three tiers in the standard Data Warehouse 3-tier architecture?",
      "options": [
        "Client Tier, Web Server Tier, Application Tier",
        "Bottom Tier (Warehouse DB Server), Middle Tier (OLAP Server), Top Tier (Front-end Client Tools)",
        "Physical Layer, Data Link Layer, Network Layer",
        "Compiler, Assembler, Linker"
      ],
      "correct_answer": "B",
      "explanation": "The 3 tiers are: Bottom (Relational DBMS & ETL staging), Middle (OLAP multidimensional engine), Top (BI query/reporting)."
    },
    {
      "id": "TEST-12-05",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What is the primary difference between ROLAP and MOLAP?",
      "options": [
        "ROLAP uses relational tables with star schemas; MOLAP uses precomputed multi-dimensional array cubes",
        "ROLAP is always faster than MOLAP",
        "MOLAP does not support slicing and dicing",
        "ROLAP can only store images"
      ],
      "correct_answer": "A",
      "explanation": "ROLAP accesses relational databases directly via SQL; MOLAP stores data in optimized multidimensional array data cubes."
    },
    {
      "id": "TEST-12-06",
      "category": "Placement Aptitude",
      "question": "What is the greatest number that will divide 43, 91, and 183 so as to leave the same remainder in each case?",
      "options": [
        "4",
        "7",
        "9",
        "13"
      ],
      "correct_answer": "A",
      "explanation": "Required number = HCF(|91 - 43|, |183 - 91|, |183 - 43|) = HCF(48, 92, 140) = 4."
    },
    {
      "id": "TEST-12-07",
      "category": "Placement Aptitude",
      "question": "What is the least number of soldiers that can be drawn up in troops of 12, 15, and 18, and also in form of a solid square?",
      "options": [
        "900",
        "400",
        "1,600",
        "3,600"
      ],
      "correct_answer": "A",
      "explanation": "LCM(12, 15, 18) = 180 = 2^2 * 3^2 * 5^1. To make a perfect square, multiply by 5: 180 * 5 = 900 soldiers."
    },
    {
      "id": "TEST-12-08",
      "category": "Placement Aptitude",
      "question": "What is the unit digit in (3^65 * 6^59 * 7^71)?",
      "options": [
        "4",
        "6",
        "2",
        "8"
      ],
      "correct_answer": "A",
      "explanation": "Unit digit of 3^65 (65 mod 4 = 1) is 3^1 = 3. Unit digit of 6^59 is always 6. Unit digit of 7^71 (71 mod 4 = 3) is 7^3 = 343 => 3. Product = 3 * 6 * 3 = 54 => unit digit 4."
    },
    {
      "id": "TEST-12-09",
      "category": "Placement Aptitude",
      "question": "How many numbers between 100 and 300 are divisible by both 4 and 6?",
      "options": [
        "17",
        "16",
        "18",
        "15"
      ],
      "correct_answer": "A",
      "explanation": "Divisible by LCM(4, 6) = 12. Smallest multiple of 12 > 100 is 108 (12 * 9). Largest multiple < 300 is 288 (12 * 24). Total = 24 - 9 + 1 = 16 numbers (or if inclusive 100-300: 300 is 12*25, 25 - 9 + 1 = 17)."
    },
    {
      "id": "TEST-12-10",
      "category": "Placement Aptitude",
      "question": "What is the remainder when (9^6 + 1) is divided by 8?",
      "options": [
        "2",
        "1",
        "0",
        "7"
      ],
      "correct_answer": "A",
      "explanation": "9 = 1 (mod 8). Therefore 9^6 + 1 = 1^6 + 1 = 2 (mod 8). Remainder is 2."
    },
    {
      "id": "TEST-12-11",
      "category": "Core CS (DBMS)",
      "question": "Which SQL isolation level allows Dirty Reads?",
      "options": [
        "Read Uncommitted",
        "Read Committed",
        "Repeatable Read",
        "Serializable"
      ],
      "correct_answer": "A",
      "explanation": "Read Uncommitted allows reading uncommitted, dirty rows."
    },
    {
      "id": "TEST-12-12",
      "category": "Core CS (DBMS)",
      "question": "A transaction re-executes a range query and discovers newly inserted rows that match the predicate. This is a:",
      "options": [
        "Dirty Read",
        "Non-Repeatable Read",
        "Phantom Read",
        "Lost Update"
      ],
      "correct_answer": "C",
      "explanation": "Newly appearing rows in a range query are Phantom Reads."
    },
    {
      "id": "TEST-12-13",
      "category": "Core CS (DBMS)",
      "question": "What is the core principle of Multi-Version Concurrency Control (MVCC)?",
      "options": [
        "All transactions execute strictly serially",
        "Readers never block writers, and writers never block readers",
        "Exclusive locks are acquired for every SELECT",
        "Rollbacks are prohibited"
      ],
      "correct_answer": "B",
      "explanation": "MVCC creates versioned snapshots, allowing non-blocking reads and concurrent writes."
    },
    {
      "id": "TEST-12-14",
      "category": "Core CS (DBMS)",
      "question": "Which isolation level completely prevents all read phenomena, ensuring equivalence to serial execution?",
      "options": [
        "Read Committed",
        "Repeatable Read",
        "Serializable",
        "Snapshot Isolation"
      ],
      "correct_answer": "C",
      "explanation": "Serializable isolation guarantees equivalent results to a serial schedule."
    },
    {
      "id": "TEST-12-15",
      "category": "Core CS (DBMS)",
      "question": "What is the default isolation level in PostgreSQL?",
      "options": [
        "Read Uncommitted",
        "Read Committed",
        "Repeatable Read",
        "Serializable"
      ],
      "correct_answer": "B",
      "explanation": "PostgreSQL uses Read Committed as its default isolation level."
    },
    {
      "id": "TEST-12-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Two Pointers (Dutch National Flag)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(1) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Two Pointers (Dutch National Flag)' pattern operates with O(N) Time, O(1) Auxiliary Space: Maintains four regions: [0..low-1] contains 0s, [low..mid-1] contains 1s, [mid..high] unexamined, [high+1..n-1] contains 2s.."
    },
    {
      "id": "TEST-12-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Two Pointers (Dutch National Flag)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: All elements equal.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Two Pointers (Dutch National Flag) include All elements equal, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-12-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Sort Colors', what Java collection or data structure provides the optimal auxiliary space bounds?",
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
      "id": "TEST-12-19",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "In Sarthak's project 'NSE2 / BulkBeat TV', what is the core architectural principle regarding 'Telegram Push Notification Infrastructure & Webhook Architecture'?",
      "options": [
        "Webhooks allow Telegram's edge servers to push user messages directly to our API server, eliminating idle socket polling.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For NSE2 / BulkBeat TV, the architectural invariant is: Webhooks allow Telegram's edge servers to push user messages directly to our API server, eliminating idle socket polling.."
    },
    {
      "id": "TEST-12-20",
      "category": "Projects (NSE2 / BulkBeat TV)",
      "question": "Regarding 'NSE2 / BulkBeat TV', how should you defend this design decision in a technical interview: 'Why migrate from Telegram long polling to Webhook architecture in NSE2?'?",
      "options": [
        "Long polling requires continuous outgoing HTTP requests every 1-2 seconds, which exhausts network sockets, consumes idle CPU, and increases latency when thousan...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: Long polling requires continuous outgoing HTTP requests every 1-2 seconds, which exhausts network sockets, consumes idle CPU, and increases ."
    }
  ],
  "13": [
    {
      "id": "TEST-13-01",
      "category": "Academic (Computer Networks)",
      "question": "In Gauss Elimination, what is the purpose of 'Partial Pivoting'?",
      "options": [
        "To reduce execution time by 50%",
        "To prevent division by zero and minimize floating-point round-off errors by selecting the largest magnitude pivot element",
        "To invert the matrix automatically",
        "To compute eigenvalues directly"
      ],
      "correct_answer": "B",
      "explanation": "Partial pivoting swaps rows so the largest absolute value in the current column becomes the pivot, preventing instability."
    },
    {
      "id": "TEST-13-02",
      "category": "Academic (Computer Networks)",
      "question": "What triangular matrix form does the coefficient matrix assume at the end of the forward elimination phase of Gauss Elimination?",
      "options": [
        "Lower Triangular Matrix",
        "Upper Triangular Matrix",
        "Diagonal Matrix",
        "Identity Matrix"
      ],
      "correct_answer": "A",
      "explanation": "Forward elimination zeroes out elements below the main diagonal, transforming the system into an Upper Triangular Matrix."
    },
    {
      "id": "TEST-13-03",
      "category": "Academic (Computer Networks)",
      "question": "How does the Gauss-Jordan method differ from standard Gauss Elimination?",
      "options": [
        "It uses random guessing instead of algebra",
        "It eliminates elements both below AND above the main diagonal, directly yielding an Identity Matrix without back substitution",
        "It only works on 2x2 matrices",
        "It requires evaluating determinants at each step"
      ],
      "correct_answer": "B",
      "explanation": "Gauss-Jordan reduces the augmented matrix to reduced row echelon form (identity matrix), yielding solutions directly."
    },
    {
      "id": "TEST-13-04",
      "category": "Academic (Computer Networks)",
      "question": "What is the computational operation count (time complexity) of Gauss Elimination for an n x n system?",
      "options": [
        "O(n)",
        "O(n^2)",
        "O(n^3 / 3)",
        "O(2^n)"
      ],
      "correct_answer": "C",
      "explanation": "Gauss Elimination requires approximately (2/3)n^3 arithmetic operations for forward elimination and O(n^2) for back substitution."
    },
    {
      "id": "TEST-13-05",
      "category": "Academic (Computer Networks)",
      "question": "A system of linear equations AX = B has a unique solution if and only if:",
      "options": [
        "det(A) = 0",
        "det(A) != 0 (A is non-singular)",
        "Rank of A < Rank of [A|B]",
        "Matrix A is asymmetric"
      ],
      "correct_answer": "B",
      "explanation": "A unique solution exists when the coefficient matrix A is non-singular with non-zero determinant (full rank)."
    },
    {
      "id": "TEST-13-06",
      "category": "Placement Aptitude",
      "question": "Statements: All birds are animals. All animals are creatures. Conclusions: I. All birds are creatures. II. Some creatures are birds.",
      "options": [
        "Both conclusions I and II follow",
        "Only conclusion I follows",
        "Only conclusion II follows",
        "Neither follows"
      ],
      "correct_answer": "A",
      "explanation": "Birds subset Animals subset Creatures => All birds are creatures (I follows). Conversion of 'All birds are creatures' gives 'Some creatures are birds' (II follows)."
    },
    {
      "id": "TEST-13-07",
      "category": "Placement Aptitude",
      "question": "Statements: Some mangos are yellow. Some tiffins are mangos. Conclusions: I. Some mangos are green. II. Tiffin is yellow.",
      "options": [
        "Neither conclusion follows",
        "Only I follows",
        "Only II follows",
        "Both follow"
      ],
      "correct_answer": "A",
      "explanation": "Neither conclusion follows from two particular premises without connecting affirmative universal quantifiers."
    },
    {
      "id": "TEST-13-08",
      "category": "Placement Aptitude",
      "question": "Statements: All pens are pencils. No pencil is an eraser. Conclusions: I. No pen is an eraser. II. Some pencils are pens.",
      "options": [
        "Both conclusions I and II follow",
        "Only I follows",
        "Only II follows",
        "Neither follows"
      ],
      "correct_answer": "A",
      "explanation": "Pens are contained within pencils, which are entirely disjoint from erasers => no pen can be an eraser (I follows). Conversion of 'All pens are pencils' gives II."
    },
    {
      "id": "TEST-13-09",
      "category": "Placement Aptitude",
      "question": "Statements: Some shirts are pants. All pants are jackets. Conclusions: I. Some shirts are jackets. II. All jackets are pants.",
      "options": [
        "Only conclusion I follows",
        "Only conclusion II follows",
        "Both follow",
        "Neither follows"
      ],
      "correct_answer": "A",
      "explanation": "Shirts overlap pants, which are completely inside jackets => shirts overlap jackets (I follows). II is invalid conversion of universal affirmative."
    },
    {
      "id": "TEST-13-10",
      "category": "Placement Aptitude",
      "question": "Statements: No cow is a chair. All chairs are tables. Conclusions: I. Some tables are chairs. II. Some tables are not cows.",
      "options": [
        "Both conclusions I and II follow",
        "Only I follows",
        "Only II follows",
        "Neither follows"
      ],
      "correct_answer": "A",
      "explanation": "Conversion of 'All chairs are tables' gives 'Some tables are chairs' (I follows). The tables that are chairs can never be cows (II follows)."
    },
    {
      "id": "TEST-13-11",
      "category": "Core CS (DBMS)",
      "question": "What is the primary guarantee provided by the Two-Phase Locking (2PL) protocol?",
      "options": [
        "Deadlock freedom",
        "Conflict Serializability",
        "Zero disk latency",
        "Automatic index selection"
      ],
      "correct_answer": "B",
      "explanation": "2PL mathematically guarantees conflict serializable execution schedules."
    },
    {
      "id": "TEST-13-12",
      "category": "Core CS (DBMS)",
      "question": "In Strict 2PL, when are Exclusive locks released?",
      "options": [
        "During the shrinking phase immediately after use",
        "Only after the transaction commits or aborts",
        "When a Shared lock is requested",
        "At the lock point"
      ],
      "correct_answer": "B",
      "explanation": "Strict 2PL holds exclusive locks until commit or abort to avoid cascading rollbacks."
    },
    {
      "id": "TEST-13-13",
      "category": "Core CS (DBMS)",
      "question": "A schedule is Conflict Serializable if its Precedence Graph has:",
      "options": [
        "At least one cycle",
        "No directed cycles (DAG)",
        "Equal in-degree and out-degree",
        "Only self-loops"
      ],
      "correct_answer": "B",
      "explanation": "Acycle precedence graphs indicate conflict serializable schedules."
    },
    {
      "id": "TEST-13-14",
      "category": "Core CS (DBMS)",
      "question": "In the Wound-Wait deadlock prevention scheme, if an older transaction requests a resource held by a younger transaction, the older transaction:",
      "options": [
        "Aborts immediately",
        "Preempts (wounds) the younger transaction",
        "Waits indefinitely",
        "Downgrades to a read lock"
      ],
      "correct_answer": "B",
      "explanation": "In Wound-Wait, older transactions preempt younger transactions holding needed locks."
    },
    {
      "id": "TEST-13-15",
      "category": "Core CS (DBMS)",
      "question": "Which pair of concurrent operations on the same data item does NOT conflict?",
      "options": [
        "Read - Write",
        "Write - Write",
        "Read - Read",
        "Write - Read"
      ],
      "correct_answer": "C",
      "explanation": "Read-Read operations do not alter data and can proceed concurrently."
    },
    {
      "id": "TEST-13-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Top-K Elements via PriorityQueue (Min/Max Heap)' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N log K) Time, O(K) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Top-K Elements via PriorityQueue (Min/Max Heap)' pattern operates with O(N log K) Time, O(K) Auxiliary Space: At all times the heap contains the K largest elements seen so far. Root is guaranteed to be the Kth largest.."
    },
    {
      "id": "TEST-13-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Top-K Elements via PriorityQueue (Min/Max Heap)' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: k == 1.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Top-K Elements via PriorityQueue (Min/Max Heap) include k == 1, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-13-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Kth Largest Element in an Array', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(K) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N log K) Time, O(K) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-13-19",
      "category": "Projects (Caloriv)",
      "question": "In Sarthak's project 'Caloriv', what is the core architectural principle regarding 'Nutrition Analytics Engine: Calorie Budgeting & Macronutrient Algorithms'?",
      "options": [
        "Mifflin-St Jeor Formula: BMR = (10 * weight in kg) + (6.25 * height in cm) - (5 * age) + s (where s = +5 for men, -161 for women).",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Caloriv, the architectural invariant is: Mifflin-St Jeor Formula: BMR = (10 * weight in kg) + (6.25 * height in cm) - (5 * age) + s (where s = +5 for men, -161 for women).."
    },
    {
      "id": "TEST-13-20",
      "category": "Projects (Caloriv)",
      "question": "Regarding 'Caloriv', how should you defend this design decision in a technical interview: 'How does Caloriv compute personalized calorie and macronutrient targets for users?'?",
      "options": [
        "The app implements the Mifflin-St Jeor formula to determine the user's Basal Metabolic Rate (BMR), multiplies it by an activity multiplier (1.2 to 1.9) to compu...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: The app implements the Mifflin-St Jeor formula to determine the user's Basal Metabolic Rate (BMR), multiplies it by an activity multiplier (."
    }
  ],
  "14": [
    {
      "id": "TEST-14-01",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What mechanism does the Java compiler use to implement Generics while maintaining backward compatibility with older JVM versions?",
      "options": [
        "Dynamic byte generation",
        "Type Erasure (replacing generic types with their bounds or Object at compile time)",
        "C++ template specialization",
        "Multiple virtual tables"
      ],
      "correct_answer": "B",
      "explanation": "Type Erasure removes all generic type information during compilation, inserting necessary casts and keeping bytecode backward compatible."
    },
    {
      "id": "TEST-14-02",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "In Java Generics, what does the wildcard expression `List<? extends Number>` signify?",
      "options": [
        "A list that can store any Object",
        "An upper-bounded wildcard: a list of elements of type Number or any subtype of Number (read-only producer)",
        "A lower-bounded wildcard accepting only Object",
        "A synchronized thread-safe array"
      ],
      "correct_answer": "B",
      "explanation": "Upper bounded wildcard `? extends T` enforces covariance: the collection produces elements of type T (PECS: Producer Extends)."
    },
    {
      "id": "TEST-14-03",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "Which Java API allows runtime inspection of classes, methods, fields, and constructors, including invoking private methods dynamically?",
      "options": [
        "Java Collections API",
        "Java Reflection API (java.lang.reflect)",
        "Java NIO API",
        "Java Native Interface (JNI)"
      ],
      "correct_answer": "B",
      "explanation": "Reflection provides programmatic introspection and dynamic invocation of class metadata and private members at runtime."
    },
    {
      "id": "TEST-14-04",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What retention policy must be specified on a custom Java annotation so it remains available in bytecode and inspectable via Reflection at runtime?",
      "options": [
        "RetentionPolicy.SOURCE",
        "RetentionPolicy.CLASS",
        "RetentionPolicy.RUNTIME",
        "RetentionPolicy.SYSTEM"
      ],
      "correct_answer": "C",
      "explanation": "RetentionPolicy.RUNTIME records annotations in the .class file and makes them accessible to the JVM Reflection engine at runtime."
    },
    {
      "id": "TEST-14-05",
      "category": "Academic (Java Programming & Dynamic Webpage Design)",
      "question": "What is the effect of PECS (Producer Extends, Consumer Super) in Java Generics?",
      "options": [
        "Use 'extends' when you only read from a collection; use 'super' when you only write to a collection",
        "Use 'super' for return values and 'extends' for method arguments always",
        "Generics cannot be combined with wildcards",
        "Extends allows adding any object to the collection"
      ],
      "correct_answer": "A",
      "explanation": "PECS rule: If a parameterized collection produces data (read-only), use `? extends`; if it consumes data (write-only), use `? super`."
    },
    {
      "id": "TEST-14-06",
      "category": "Placement Aptitude",
      "question": "Pointing to a gentleman, Prabhat remarked, 'His only son is my son's uncle.' How is the gentleman related to Prabhat?",
      "options": [
        "Father",
        "Uncle",
        "Brother",
        "Grandfather"
      ],
      "correct_answer": "A",
      "explanation": "'My son's uncle' = Prabhat's brother. The gentleman's only son is Prabhat's brother => The gentleman is Prabhat's father."
    },
    {
      "id": "TEST-14-07",
      "category": "Placement Aptitude",
      "question": "Introducing a man, a woman said, 'His wife is the only daughter of my father.' How is the man related to the woman?",
      "options": [
        "Husband",
        "Brother",
        "Maternal Uncle",
        "Father-in-law"
      ],
      "correct_answer": "A",
      "explanation": "'Only daughter of my father' = the woman herself. The man's wife is the woman herself => the man is her husband."
    },
    {
      "id": "TEST-14-08",
      "category": "Placement Aptitude",
      "question": "In a family tree code, if 'P $ Q' means P is father of Q, 'P # Q' means P is mother of Q, and 'P & Q' means P is sister of Q. In the expression X $ Y & Z # W, how is X related to W?",
      "options": [
        "Maternal Grandfather",
        "Paternal Grandfather",
        "Uncle",
        "Brother"
      ],
      "correct_answer": "A",
      "explanation": "Z is mother of W, Y is sister of Z, and X is father of Y (and Z). Therefore X is the maternal grandfather of W."
    },
    {
      "id": "TEST-14-09",
      "category": "Placement Aptitude",
      "question": "A is the mother of B. C is the father of A. D is the brother of E. E is the daughter of B. How is C related to E?",
      "options": [
        "Maternal Great-Grandfather",
        "Maternal Grandfather",
        "Paternal Grandfather",
        "Uncle"
      ],
      "correct_answer": "A",
      "explanation": "E is daughter of B, who is child of A, who is daughter of C. Hence C is the maternal great-grandfather of E."
    },
    {
      "id": "TEST-14-10",
      "category": "Placement Aptitude",
      "question": "Pointing to a man in a photograph, Anita said, 'His brother's father is the only son of my grandfather.' How is Anita related to the man in the photograph?",
      "options": [
        "Sister",
        "Aunt",
        "Mother",
        "Daughter"
      ],
      "correct_answer": "A",
      "explanation": "'Only son of my grandfather' = Anita's father. 'His brother's father' = the man's father. Both share the same father => Anita is his sister."
    },
    {
      "id": "TEST-14-11",
      "category": "Core CS (DBMS)",
      "question": "Why are B+ Trees preferred over B-Trees for database disk indexing?",
      "options": [
        "B+ trees require no sorting",
        "Internal nodes store only keys, maximizing fan-out, and leaf nodes form a linked list for range scans",
        "B+ trees are binary trees",
        "B+ trees store data in RAM only"
      ],
      "correct_answer": "B",
      "explanation": "B+ trees pack more keys per internal page and link leaves for rapid range scanning."
    },
    {
      "id": "TEST-14-12",
      "category": "Core CS (DBMS)",
      "question": "How many Clustered Indexes can exist on a single database table?",
      "options": [
        "Zero",
        "Exactly one",
        "Up to 16",
        "Unlimited"
      ],
      "correct_answer": "B",
      "explanation": "Because physical disk rows can only be ordered in one sequence, only one clustered index can exist."
    },
    {
      "id": "TEST-14-13",
      "category": "Core CS (DBMS)",
      "question": "An index that contains every column requested by a query, avoiding physical table page lookups, is called a:",
      "options": [
        "Bitmap Index",
        "Covering Index",
        "Dense Index",
        "Hash Index"
      ],
      "correct_answer": "B",
      "explanation": "Covering indexes satisfy the query directly from leaf nodes without fetching base table pages."
    },
    {
      "id": "TEST-14-14",
      "category": "Core CS (DBMS)",
      "question": "In a B+ tree of order m, all leaf nodes reside at:",
      "options": [
        "Different depths",
        "The exact same depth",
        "Depth 1",
        "Random positions"
      ],
      "correct_answer": "B",
      "explanation": "B+ trees are strictly height-balanced; all leaf nodes reside at the exact same depth."
    },
    {
      "id": "TEST-14-15",
      "category": "Core CS (DBMS)",
      "question": "Creating an index on a boolean column (e.g., is_active) with 50/50 distribution is usually ineffective because:",
      "options": [
        "B+ trees cannot store booleans",
        "The column has very low selectivity",
        "The index would be larger than the table",
        "Foreign keys cannot be booleans"
      ],
      "correct_answer": "B",
      "explanation": "Low selectivity causes the query optimizer to choose a full table scan over the index."
    },
    {
      "id": "TEST-14-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'K-Way Merge of Sorted Arrays / Lists' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N log K) Time, O(K) Auxiliary Space.",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'K-Way Merge of Sorted Arrays / Lists' pattern operates with O(N log K) Time, O(K) Auxiliary Space: At each step, selecting the next smallest element across K lists takes O(log K) rather than O(K) linear comparison.."
    },
    {
      "id": "TEST-14-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'K-Way Merge of Sorted Arrays / Lists' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Empty lists array.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for K-Way Merge of Sorted Arrays / Lists include Empty lists array, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-14-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Merge k Sorted Lists', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(K) Auxiliary Space.",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N log K) Time, O(K) Auxiliary Space by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-14-19",
      "category": "Projects (Biometric Electronic Voting System (BEVM))",
      "question": "In Sarthak's project 'Biometric Electronic Voting System (BEVM)', what is the core architectural principle regarding 'Biometric Authentication Workflow & Zero-Knowledge Role Separation'?",
      "options": [
        "Role separation guarantees that polling booth operators cannot modify candidate rosters once an election commences.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For Biometric Electronic Voting System (BEVM), the architectural invariant is: Role separation guarantees that polling booth operators cannot modify candidate rosters once an election commences.."
    },
    {
      "id": "TEST-14-20",
      "category": "Projects (Biometric Electronic Voting System (BEVM))",
      "question": "Regarding 'Biometric Electronic Voting System (BEVM)', how should you defend this design decision in a technical interview: 'How does BEVM enforce role-based privilege separation between election officers and voters?'?",
      "options": [
        "BEVM establishes two distinct software modes: Admin Mode and Polling Mode. Admin Mode requires administrative credentials to configure candidates, register vote...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: BEVM establishes two distinct software modes: Admin Mode and Polling Mode. Admin Mode requires administrative credentials to configure candi."
    }
  ],
  "15": [
    {
      "id": "TEST-15-01",
      "category": "Academic (Numerical Methods)",
      "question": "How many host addresses can be assigned to devices on a subnetwork configured with a `/26` CIDR prefix?",
      "options": [
        "64 hosts",
        "62 hosts (2^6 - 2)",
        "32 hosts",
        "30 hosts"
      ],
      "correct_answer": "B",
      "explanation": "A /26 mask leaves 32 - 26 = 6 host bits. Total addresses = 2^6 = 64. Subtracting network and broadcast addresses leaves 62 usable hosts."
    },
    {
      "id": "TEST-15-02",
      "category": "Academic (Numerical Methods)",
      "question": "What is the default subnet mask for an IPv4 Class B network address?",
      "options": [
        "255.0.0.0 (/8)",
        "255.255.0.0 (/16)",
        "255.255.255.0 (/24)",
        "255.255.255.240 (/28)"
      ],
      "correct_answer": "B",
      "explanation": "Class B addresses (first octet 128-191) use a 16-bit network prefix: 255.255.0.0 (/16)."
    },
    {
      "id": "TEST-15-03",
      "category": "Academic (Numerical Methods)",
      "question": "What is the primary purpose of Classless Inter-Domain Routing (CIDR)?",
      "options": [
        "To encrypt IP packets on public Wi-Fi",
        "To slow the exhaustion of IPv4 addresses and reduce global router routing table size via route aggregation (supernetting)",
        "To replace MAC addresses with domain names",
        "To convert IPv4 packets directly into IPv6"
      ],
      "correct_answer": "B",
      "explanation": "CIDR eliminates rigid A/B/C classes, allowing arbitrary prefix lengths (/n) and hierarchical route summarization."
    },
    {
      "id": "TEST-15-04",
      "category": "Academic (Numerical Methods)",
      "question": "Which of the following IP addresses represents a private IPv4 address defined in RFC 1918?",
      "options": [
        "8.8.8.8",
        "172.20.14.5",
        "198.51.100.1",
        "127.0.0.1"
      ],
      "correct_answer": "B",
      "explanation": "RFC 1918 private ranges: 10.0.0.0/8, 172.16.0.0/12 (172.16 - 172.31), and 192.168.0.0/16. 172.20.14.5 is private."
    },
    {
      "id": "TEST-15-05",
      "category": "Academic (Numerical Methods)",
      "question": "What is the broadcast address for the subnet `192.168.1.32/27`?",
      "options": [
        "192.168.1.32",
        "192.168.1.63",
        "192.168.1.64",
        "192.168.1.255"
      ],
      "correct_answer": "B",
      "explanation": "A /27 subnet has block size 2^(32-27) = 32. Subnet starts at .32 and ends at .63 (broadcast address is .63)."
    },
    {
      "id": "TEST-15-06",
      "category": "Placement Aptitude",
      "question": "A man walks 6 km South, turns left and walks 4 km, then turns left again and walks 6 km. How far is he from his starting point?",
      "options": [
        "4 km",
        "6 km",
        "8 km",
        "2 km"
      ],
      "correct_answer": "A",
      "explanation": "Walking 6 km South and 6 km North cancel out vertically, leaving a net displacement of 4 km East."
    },
    {
      "id": "TEST-15-07",
      "category": "Placement Aptitude",
      "question": "One morning after sunrise, Vimal was standing in front of a pole. The shadow of the pole fell directly to his left. In which direction was Vimal facing?",
      "options": [
        "North",
        "South",
        "East",
        "West"
      ],
      "correct_answer": "A",
      "explanation": "In the morning, shadows point West. If West is to his left, Vimal is facing North."
    },
    {
      "id": "TEST-15-08",
      "category": "Placement Aptitude",
      "question": "A child is looking for his father. He went 90 m in the East before turning to his right. He went 20 m before turning to his right again to look for his father at his uncle's place 30 m from this point. How far is he from the starting point?",
      "options": [
        "100 m",
        "80 m",
        "120 m",
        "90 m"
      ],
      "correct_answer": "A",
      "explanation": "Displacement: x = 90 - 30 = 60 m; y = -20 m (Wait, if he turns right again and goes 60m more North: Euclidean distance = sqrt(60^2 + 80^2) = 100 m)."
    },
    {
      "id": "TEST-15-09",
      "category": "Placement Aptitude",
      "question": "If South-East becomes North, North-East becomes West and so on, what will West become?",
      "options": [
        "South-East",
        "North-East",
        "South-West",
        "North-West"
      ],
      "correct_answer": "A",
      "explanation": "The compass is rotated 135 degrees counter-clockwise. West rotated 135 degrees CCW becomes South-East."
    },
    {
      "id": "TEST-15-10",
      "category": "Placement Aptitude",
      "question": "A clock is so placed that at 12 noon its minute hand points towards North-East. In which direction does its hour hand point at 1:30 PM?",
      "options": [
        "East",
        "South-East",
        "North",
        "North-East"
      ],
      "correct_answer": "A",
      "explanation": "At 12:00, minute hand normally points North. Here it is rotated 45 deg clockwise to NE. At 1:30 PM, hour hand is at 45 deg (normally NE). Rotated 45 deg CW, it points East."
    },
    {
      "id": "TEST-15-11",
      "category": "Core CS (Computer Networks)",
      "question": "What is the Protocol Data Unit (PDU) at the Network layer of the OSI model?",
      "options": [
        "Frame",
        "Segment",
        "Packet",
        "Bit"
      ],
      "correct_answer": "C",
      "explanation": "Network layer units are called Packets (or Datagrams)."
    },
    {
      "id": "TEST-15-12",
      "category": "Core CS (Computer Networks)",
      "question": "Which layer of the OSI model is responsible for encryption, compression, and character syntax translation?",
      "options": [
        "Application layer",
        "Presentation layer",
        "Session layer",
        "Transport layer"
      ],
      "correct_answer": "B",
      "explanation": "The Presentation layer handles data formatting, compression, and cryptography."
    },
    {
      "id": "TEST-15-13",
      "category": "Core CS (Computer Networks)",
      "question": "What is the standard port number for secure HTTPS communication?",
      "options": [
        "80",
        "8080",
        "443",
        "22"
      ],
      "correct_answer": "C",
      "explanation": "HTTPS runs over well-known port 443."
    },
    {
      "id": "TEST-15-14",
      "category": "Core CS (Computer Networks)",
      "question": "At which layer of the OSI model do network switches primarily operate?",
      "options": [
        "Physical (Layer 1)",
        "Data Link (Layer 2)",
        "Network (Layer 3)",
        "Transport (Layer 4)"
      ],
      "correct_answer": "B",
      "explanation": "Standard network switches operate at Layer 2 (Data Link), forwarding frames by MAC address."
    },
    {
      "id": "TEST-15-15",
      "category": "Core CS (Computer Networks)",
      "question": "In the TCP/IP 4-layer model, the Internet layer corresponds to which OSI layer?",
      "options": [
        "Data Link layer",
        "Network layer",
        "Transport layer",
        "Session layer"
      ],
      "correct_answer": "B",
      "explanation": "The TCP/IP Internet layer maps directly to the OSI Network layer."
    },
    {
      "id": "TEST-15-16",
      "category": "Java DSA & Coding",
      "question": "In Java 17+, how is the 'Tree Traversals: BFS Level-Order' algorithmic pattern optimal for placement coding problems?",
      "options": [
        "It satisfies optimal asymptotic complexity: O(N) Time, O(W) Auxiliary Space (W = maximum width of tree).",
        "It uses recursion with infinite call stack depth.",
        "It allocates O(N^2) dynamic heap memory unnecessarily.",
        "It requires native C++ pointer arithmetic."
      ],
      "correct_answer": "A",
      "explanation": "The 'Tree Traversals: BFS Level-Order' pattern operates with O(N) Time, O(W) Auxiliary Space (W = maximum width of tree): The queue size at the start of each level loop reflects exactly the count of nodes present on that level.."
    },
    {
      "id": "TEST-15-17",
      "category": "Java DSA & Coding",
      "question": "When implementing 'Tree Traversals: BFS Level-Order' in Java, which edge case must be guarded against to avoid runtime exceptions?",
      "options": [
        "Handling boundary conditions such as: Null root.",
        "Using only primitive floats instead of double.",
        "Declaring all methods native.",
        "Disabling JVM garbage collection."
      ],
      "correct_answer": "A",
      "explanation": "Critical edge cases for Tree Traversals: BFS Level-Order include Null root, which must be validated with guard clauses before executing loop pointers."
    },
    {
      "id": "TEST-15-18",
      "category": "Java DSA & Coding",
      "question": "For 'Problem 1: Binary Tree Level Order Traversal', what Java collection or data structure provides the optimal auxiliary space bounds?",
      "options": [
        "Standard array or standard collection adhering to O(W) Auxiliary Space (W = maximum width of tree).",
        "A nested 3D LinkedList.",
        "External disk-backed SQL table.",
        "Unbounded blocking queue."
      ],
      "correct_answer": "A",
      "explanation": "The optimal Java 17+ implementation achieves O(N) Time, O(W) Auxiliary Space (W = maximum width of tree) by avoiding unneeded object allocations."
    },
    {
      "id": "TEST-15-19",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "In Sarthak's project 'College Student Management System (CSMS)', what is the core architectural principle regarding 'Academic Grading Engine & Semester Fee Ledger Management'?",
      "options": [
        "Composite scores translate deterministically: >=90% -> A, 80-89% -> B, 70-79% -> C, 60-69% -> D, <60% -> F.",
        "Using unencrypted HTTP requests over public ports.",
        "Storing passwords in plaintext inside localStorage.",
        "Restarting the production server on every user request."
      ],
      "correct_answer": "A",
      "explanation": "For College Student Management System (CSMS), the architectural invariant is: Composite scores translate deterministically: >=90% -> A, 80-89% -> B, 70-79% -> C, 60-69% -> D, <60% -> F.."
    },
    {
      "id": "TEST-15-20",
      "category": "Projects (College Student Management System (CSMS))",
      "question": "Regarding 'College Student Management System (CSMS)', how should you defend this design decision in a technical interview: 'How does the academic grading engine calculate student performance in CSMS?'?",
      "options": [
        "In `backend/routers/grades.py`, scores across class tests, assignments, and mid-terms from `test_marks` are aggregated into a composite percentage. A determinis...",
        "Claim that standard frameworks are obsolete and write custom assembly.",
        "State that testing was skipped to ship faster.",
        "Acknowledge that security was ignored."
      ],
      "correct_answer": "A",
      "explanation": "In technical interviews, anchor your defense in engineering metrics: In `backend/routers/grades.py`, scores across class tests, assignments, and mid-terms from `test_marks` are aggregated into a composite perc."
    }
  ]
}

def get_mixed_mcqs_half1(day: int) -> list:
    return MIXED_DAYS_1_15.get(day, [])
