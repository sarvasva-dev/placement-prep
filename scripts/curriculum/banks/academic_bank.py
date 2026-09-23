#!/usr/bin/env python3
"""
scripts/curriculum/banks/academic_bank.py
High-Quality, Authentic Academic MCQs for Days 1 to 30 (5 MCQs per day = 150 MCQs).
Grounded strictly in CSJM University, Kanpur syllabus:
- BCA-5001: Knowledge Management
- BCA-5002: Java Programming & Dynamic Webpage Design
- BCA-5003: Computer Networks
- BCA-5004: Numerical Methods
"""

ACADEMIC_MCQS = {
    1: [
        {
            "id": "ACAD-01-01",
            "question": "According to Herbert A. Simon, in which phase of the decision-making process does an executive identify problems and scan the operational environment?",
            "options": ["Design Phase", "Intelligence Phase", "Choice Phase", "Implementation Phase"],
            "correct_answer": "B",
            "explanation": "Simon's Intelligence phase involves environmental scanning, data acquisition, and identifying conditions or anomalies that necessitate decision making."
        },
        {
            "id": "ACAD-01-02",
            "question": "What core cognitive principle explains why managerial decision makers select 'satisficing' alternatives instead of global optimal solutions?",
            "options": ["Bounded Rationality", "Pareto Efficiency", "Linear Programming", "Deterministic Optimization"],
            "correct_answer": "A",
            "explanation": "Herbert Simon's Bounded Rationality states that human cognition is limited by information asymmetry, finite computing capacity, and time, leading to satisficing behavior."
        },
        {
            "id": "ACAD-01-03",
            "question": "Which phase was explicitly added to complete the four-stage decision-making model by Simon to track execution feedback?",
            "options": ["Verification Phase", "Formulation Phase", "Implementation Phase", "Optimization Phase"],
            "correct_answer": "C",
            "explanation": "Simon originally formulated a 3-phase model (Intelligence, Design, Choice) and subsequently added Implementation to monitor execution and feed telemetry back."
        },
        {
            "id": "ACAD-01-04",
            "question": "In Herbert Simon's framework, what type of decisions can be handled entirely by established algorithms and automated rules without executive intervention?",
            "options": ["Unstructured decisions", "Strategic decisions", "Structured decisions", "Subjective decisions"],
            "correct_answer": "C",
            "explanation": "Structured decisions are routine, repetitive, and possess a definite methodology for handling, making them programmable via computer systems."
        },
        {
            "id": "ACAD-01-05",
            "question": "Which technology directly assists executive decision making in the Design phase by simulating business consequences of generated alternatives?",
            "options": ["Transaction Processing Systems (TPS)", "Model Base Management Systems (MBMS)", "Network Interface Cards", "BIOS firmware"],
            "correct_answer": "B",
            "explanation": "MBMS provides quantitative and simulation models (linear programming, forecasting) to analyze decision alternatives during the Design phase."
        }
    ],

    2: [
        {
            "id": "ACAD-02-01",
            "question": "Which of the following is NOT one of the three primary architectural subsystems of a classical Decision Support System (DSS)?",
            "options": ["Database Management Subsystem (DBMS)", "Model Base Management Subsystem (MBMS)", "User Interface / Dialog Subsystem", "Packet Switching Subsystem"],
            "correct_answer": "D",
            "explanation": "A DSS architecture consists of three fundamental components: Data Management (DBMS), Model Management (MBMS), and Dialog/User Interface."
        },
        {
            "id": "ACAD-02-02",
            "question": "How does a Management Information System (MIS) fundamentally differ from a Decision Support System (DSS)?",
            "options": ["MIS focuses on ad-hoc interactive simulation, while DSS provides static scheduled reports", "MIS produces structured periodic summaries of past operational data, while DSS provides interactive 'what-if' modeling for semi-structured decisions", "MIS is only used by top executives, while DSS is used by data entry clerks", "MIS does not require a database, whereas DSS requires a data warehouse"],
            "correct_answer": "B",
            "explanation": "MIS supports structured, routine operations with fixed scheduled reports; DSS is designed for ad-hoc, flexible, what-if exploratory modeling of semi-structured problems."
        },
        {
            "id": "ACAD-02-03",
            "question": "What is the primary function of the Model Base Management Subsystem (MBMS) in a DSS?",
            "options": ["Storing raw SQL transaction tables", "Managing, updating, and executing mathematical, financial, and simulation models", "Rendering HTML CSS graphics on the client", "Encrypting database disk partitions"],
            "correct_answer": "B",
            "explanation": "MBMS manages the catalog of quantitative models (statistical, financial, optimization, forecasting) and couples them with data to generate scenarios."
        },
        {
            "id": "ACAD-02-04",
            "question": "In DSS sensitivity analysis, what does a 'Goal Seeking' query determine?",
            "options": ["The output metric given fixed input parameters", "The required value of an input variable needed to achieve a specified target output", "The maximum bandwidth of the network connection", "The number of concurrent database sessions"],
            "correct_answer": "B",
            "explanation": "Goal seeking (backward sensitivity analysis) calculates the input variable adjustments required to reach a specific desired target result."
        },
        {
            "id": "ACAD-02-05",
            "question": "Executive Information Systems (EIS) are distinguished from general DSS by their strong emphasis on:",
            "options": ["Low-level assembly language programming", "High-level graphical KPI dashboards, drill-down capabilities, and internal/external critical success factors", "Batch card punch processing", "Hardware register allocation"],
            "correct_answer": "B",
            "explanation": "EIS is tailored for senior leadership, emphasizing intuitive visual interfaces, drill-down summaries, and status tracking of Critical Success Factors (CSFs)."
        }
    ],

    3: [
        {
            "id": "ACAD-03-01",
            "question": "Which component of the JVM Execution Engine compiles frequently executed bytecode hot-spots into native machine instructions at runtime?",
            "options": ["Interpreter", "Just-In-Time (JIT) Compiler", "Garbage Collector", "ClassLoader"],
            "correct_answer": "B",
            "explanation": "The JIT compiler profiles running bytecode and dynamically compiles high-frequency code paths ('hot spots') into native CPU instructions for near-native performance."
        },
        {
            "id": "ACAD-03-02",
            "question": "Which runtime data area in the JVM is shared among all concurrent threads?",
            "options": ["Java Virtual Machine Stack", "Program Counter (PC) Register", "Heap Memory Area", "Native Method Stack"],
            "correct_answer": "C",
            "explanation": "The Heap and Method Area are created upon JVM startup and shared across all threads. Stacks and PC registers are private to individual threads."
        },
        {
            "id": "ACAD-03-03",
            "question": "What principle governs the ClassLoader subsystem hierarchy when resolving and loading Java classes?",
            "options": ["Round-Robin Principle", "Delegation-Hierarchy Principle", "Least-Recently-Used Principle", "First-In-First-Out Principle"],
            "correct_answer": "B",
            "explanation": "Java ClassLoaders follow delegation: a ClassLoader delegates class requests upward to its parent before attempting to load the class itself."
        },
        {
            "id": "ACAD-03-04",
            "question": "Which phase of ClassLoader Linking ensures that bytecode conforms to the JVM specification and cannot compromise system security?",
            "options": ["Preparation", "Resolution", "Verification", "Initialization"],
            "correct_answer": "C",
            "explanation": "Bytecode Verification checks structural correctness, stack overflow limits, type safety, and memory access integrity before execution."
        },
        {
            "id": "ACAD-03-05",
            "question": "What is stored inside a stack frame allocated on the Java Thread Stack during method execution?",
            "options": ["All newly instantiated objects via the 'new' operator", "Static class metadata and bytecodes", "Local variables table, operand stack, and frame data (return pointer)", "Database connection pool sockets"],
            "correct_answer": "C",
            "explanation": "Each method invocation pushes a stack frame containing local variables, the operand stack for calculations, and frame linkage references."
        }
    ],

    4: [
        {
            "id": "ACAD-04-01",
            "question": "In the ISO-OSI 7-Layer Reference Model, which layer is responsible for dialog control, token management, and session checkpointing?",
            "options": ["Transport Layer", "Session Layer", "Presentation Layer", "Data Link Layer"],
            "correct_answer": "B",
            "explanation": "Layer 5 (Session Layer) establishes, manages, synchronizes, and terminates sessions between end-user applications with checkpoints."
        },
        {
            "id": "ACAD-04-02",
            "question": "What is the Protocol Data Unit (PDU) name at the Network Layer of the OSI model?",
            "options": ["Frame", "Segment", "Packet", "Bit"],
            "correct_answer": "C",
            "explanation": "PDU names across layers: Physical = Bit, Data Link = Frame, Network = Packet, Transport = Segment, Application = Data/Message."
        },
        {
            "id": "ACAD-04-03",
            "question": "Which layer in the OSI reference model handles data syntax conversion, compression, and encryption/decryption (e.g., ASN.1, SSL/TLS)?",
            "options": ["Presentation Layer", "Application Layer", "Session Layer", "Network Layer"],
            "correct_answer": "A",
            "explanation": "Layer 6 (Presentation Layer) standardizes data formats, handles character set translations (ASCII/EBCDIC), data compression, and cryptographic encryption."
        },
        {
            "id": "ACAD-04-04",
            "question": "How does the TCP/IP architectural suite map the top three layers of the OSI reference model (Session, Presentation, Application)?",
            "options": ["They are split across Network Access and Internet layers", "They are combined into a single unified Application Layer", "They are moved into operating system kernel device drivers", "They are replaced by the Transport Layer"],
            "correct_answer": "B",
            "explanation": "The 4-layer TCP/IP model consolidates OSI's Application, Presentation, and Session layers into a single top-level Application Layer."
        },
        {
            "id": "ACAD-04-05",
            "question": "Which layer provides true end-to-end reliability and process-to-process communication using port numbers?",
            "options": ["Network Layer", "Transport Layer", "Data Link Layer", "Physical Layer"],
            "correct_answer": "B",
            "explanation": "The Transport Layer (TCP/UDP) uses 16-bit port addresses to deliver data process-to-process with end-to-end flow and error control."
        }
    ],

    5: [
        {
            "id": "ACAD-05-01",
            "question": "If the true value is X and the computed approximate value is X*, what is the mathematical formula for Relative Error (Er)?",
            "options": ["|X - X*|", "|X - X*| / |X|", "(|X - X*| / |X|) * 100", "|X - X*| * |X|"],
            "correct_answer": "B",
            "explanation": "Absolute Error Ea = |X - X*|. Relative Error Er = Ea / |X| = |X - X*| / |X|. Percentage Error Ep = Er * 100%."
        },
        {
            "id": "ACAD-05-02",
            "question": "What is the rate of convergence of the Bisection Method for finding the real root of a continuous equation f(x) = 0?",
            "options": ["Quadratic (order 2)", "Linear (order 1) with convergence factor 0.5", "Superlinear (order 1.618)", "Cubic (order 3)"],
            "correct_answer": "B",
            "explanation": "The Bisection method halves the interval bracket at each step (e_{n+1} = 0.5 * e_n), giving linear convergence with an asymptotic error factor of 1/2."
        },
        {
            "id": "ACAD-05-03",
            "question": "According to the Intermediate Value Theorem, what condition must continuous function f(x) satisfy on interval [a, b] to guarantee at least one real root?",
            "options": ["f(a) * f(b) > 0", "f(a) * f(b) < 0", "f'(a) = f'(b)", "f(a) + f(b) = 0"],
            "correct_answer": "B",
            "explanation": "If f(x) is continuous and f(a) and f(b) have opposite signs (f(a)*f(b) < 0), Bolzano's theorem guarantees at least one root c in (a, b) such that f(c) = 0."
        },
        {
            "id": "ACAD-05-04",
            "question": "What is Truncation Error in numerical computation?",
            "options": ["Error introduced by hardware word-length rounding (e.g., 32-bit float limits)", "Error resulting from replacing an infinite mathematical process with a finite approximation (e.g., truncating a Taylor series)", "Mistakes made by the programmer entering data", "Error caused by noisy transmission channels"],
            "correct_answer": "B",
            "explanation": "Truncation error occurs when an exact mathematical operation (like infinite series summation or differentiation limits) is truncated to a finite formula."
        },
        {
            "id": "ACAD-05-05",
            "question": "To achieve an accuracy of epsilon = 10^-3 starting from an initial bracket of length (b - a) = 1, approximately how many Bisection iterations are required?",
            "options": ["4 iterations", "7 iterations", "10 iterations", "25 iterations"],
            "correct_answer": "C",
            "explanation": "Interval length after n steps is (b - a)/2^n <= epsilon => 1/2^n <= 10^-3 => 2^n >= 1000 => n >= 10 (since 2^10 = 1024)."
        }
    ],

    6: [
        {
            "id": "ACAD-06-01",
            "question": "Which method in Java is invoked to initiate the concurrent execution of a new thread created via Thread class or Runnable interface?",
            "options": ["run()", "start()", "init()", "execute()"],
            "correct_answer": "B",
            "explanation": "Calling start() requests the JVM to allocate a new native thread call stack and invoke the run() method asynchronously. Calling run() directly runs synchronously on the caller's thread."
        },
        {
            "id": "ACAD-06-02",
            "question": "What happens when a thread enters a method marked with the 'synchronized' keyword in Java?",
            "options": ["The thread acquires the intrinsic lock (monitor) associated with the target object", "The thread is immediately put into the DEAD state", "The JVM disables garbage collection for all heaps", "The thread's priority is automatically raised to MAX_PRIORITY"],
            "correct_answer": "A",
            "explanation": "Every Java object has an intrinsic monitor lock. Synchronized methods/blocks acquire this lock, preventing other threads from executing synchronized code on that object until released."
        },
        {
            "id": "ACAD-06-03",
            "question": "Which method releases the monitor lock and suspends the calling thread until another thread invokes notify() or notifyAll() on the same object?",
            "options": ["sleep()", "yield()", "wait()", "join()"],
            "correct_answer": "C",
            "explanation": "Object.wait() must be called from within a synchronized context; it atomically releases the object monitor and places the thread into the object's wait set."
        },
        {
            "id": "ACAD-06-04",
            "question": "What is the primary advantage of implementing the Runnable interface over extending the Thread class in Java?",
            "options": ["Runnable threads execute 10x faster than Thread subclasses", "Since Java does not support multiple class inheritance, implementing Runnable leaves the class free to extend another base class", "Runnable does not require overriding the run() method", "Runnable automatically prevents deadlocks"],
            "correct_answer": "B",
            "explanation": "Java supports single class inheritance. Implementing Runnable allows the class to extend another business class while decoupling the task from the thread runner."
        },
        {
            "id": "ACAD-06-05",
            "question": "What happens to a Daemon thread in Java when all non-daemon user threads finish executing?",
            "options": ["The JVM continues running until the daemon thread finishes", "The JVM terminates immediately, abruptly stopping all daemon threads", "The daemon thread is automatically converted into a user thread", "The JVM throws a ThreadDeathException"],
            "correct_answer": "B",
            "explanation": "Daemon threads (like GC) provide background services. The JVM exits as soon as all user (non-daemon) threads terminate, killing any active daemon threads."
        }
    ],

    7: [
        {
            "id": "ACAD-07-01",
            "question": "In the Cyclic Redundancy Check (CRC) error detection mechanism, what mathematical operation is used in the polynomial modulo-2 arithmetic?",
            "options": ["Standard integer long division with carry", "Bitwise XOR (Exclusive-OR) without carry", "Bitwise AND operation", "Floating point division"],
            "correct_answer": "B",
            "explanation": "Modulo-2 polynomial arithmetic uses XOR for both addition and subtraction, with zero carry or borrow operations."
        },
        {
            "id": "ACAD-07-02",
            "question": "If a generator polynomial G(x) has degree r, how many zero bits are appended to the original message bitstream before performing CRC division?",
            "options": ["r - 1 zeros", "r zeros", "r + 1 zeros", "2r zeros"],
            "correct_answer": "B",
            "explanation": "To calculate the r-bit remainder (FCS checksum), exactly r zeros (corresponding to the polynomial degree) are appended to the message bit sequence."
        },
        {
            "id": "ACAD-07-03",
            "question": "To detect 'd' single-bit transmission errors in a block of data, the minimum Hamming distance of the code must be:",
            "options": ["d", "d + 1", "2d", "2d + 1"],
            "correct_answer": "B",
            "explanation": "To detect d single-bit errors, minimum Hamming distance d_min >= d + 1. To correct t single-bit errors, d_min >= 2t + 1."
        },
        {
            "id": "ACAD-07-04",
            "question": "In byte stuffing (character-oriented framing), what escape character is inserted when the data payload itself contains the special FLAG byte?",
            "options": ["SYN", "ESC", "ETX", "SOH"],
            "correct_answer": "B",
            "explanation": "Byte stuffing prefixes an ESC (Escape) byte before any accidental occurrence of FLAG or ESC bytes in the data payload."
        },
        {
            "id": "ACAD-07-05",
            "question": "In bit-oriented framing (HDLC protocol), bit stuffing inserts a '0' bit after encountering:",
            "options": ["Three consecutive 1s", "Five consecutive 1s", "Seven consecutive 1s", "Eight consecutive 0s"],
            "correct_answer": "B",
            "explanation": "To prevent user data from mimicking the 01111110 FLAG delimiter, the sender automatically stuffs a '0' after any sequence of five consecutive '1's."
        }
    ],

    8: [
        {
            "id": "ACAD-08-01",
            "question": "In Nonaka and Takeuchi's SECI model of Knowledge Creation, what transformation mode represents converting Tacit Knowledge into Explicit Knowledge?",
            "options": ["Socialization", "Externalization", "Combination", "Internalization"],
            "correct_answer": "B",
            "explanation": "Externalization articulates unspoken, subjective tacit insights into explicit concepts, metaphors, models, and written diagrams."
        },
        {
            "id": "ACAD-08-02",
            "question": "Which SECI quadrant describes apprentices learning tacit craft skills from a master artisan through shared observation, imitation, and practice without written manuals?",
            "options": ["Socialization (Tacit to Tacit)", "Combination (Explicit to Explicit)", "Internalization (Explicit to Tacit)", "Externalization (Tacit to Explicit)"],
            "correct_answer": "A",
            "explanation": "Socialization transfers tacit knowledge directly between individuals through shared physical experience, apprenticeship, and informal dialogue."
        },
        {
            "id": "ACAD-08-03",
            "question": "What is the defining characteristic of Tacit Knowledge compared to Explicit Knowledge?",
            "options": ["It is easily indexed, codified, and stored in relational database tables", "It is personal, context-specific, rooted in action, commitment, and heuristics, making it hard to formalize", "It can be transmitted instantly over a network socket as JSON", "It is only possessed by machines and software algorithms"],
            "correct_answer": "B",
            "explanation": "Tacit knowledge is intuitive, deeply ingrained in human experience and mental models ('we know more than we can tell', Michael Polanyi)."
        },
        {
            "id": "ACAD-08-04",
            "question": "In the DIKW hierarchy, which layer adds actionable rules, context, and experience to raw processed information?",
            "options": ["Data", "Information", "Knowledge", "Wisdom"],
            "correct_answer": "C",
            "explanation": "DIKW pyramid: Data (raw symbols) -> Information (contextualized data) -> Knowledge (actionable understanding and rules) -> Wisdom (evaluated judgment)."
        },
        {
            "id": "ACAD-08-05",
            "question": "Which SECI quadrant involves integrating multiple documents, databases, and financial spreadsheets into a unified organizational repository?",
            "options": ["Internalization", "Externalization", "Socialization", "Combination"],
            "correct_answer": "D",
            "explanation": "Combination synthesizes disparate pieces of explicit knowledge by sorting, aggregating, and re-categorizing them into new explicit documents."
        }
    ],

    9: [
        {
            "id": "ACAD-09-01",
            "question": "What is the order of convergence for the Newton-Raphson iterative method for solving f(x) = 0 with simple roots?",
            "options": ["1 (Linear)", "1.618 (Golden ratio)", "2 (Quadratic)", "3 (Cubic)"],
            "correct_answer": "C",
            "explanation": "Newton-Raphson exhibits quadratic convergence (order 2), meaning the number of correct decimal places approximately doubles each iteration."
        },
        {
            "id": "ACAD-09-02",
            "question": "What is the Newton-Raphson iteration formula for finding root x_{n+1} from current estimate x_n?",
            "options": ["x_{n+1} = x_n - f(x_n) / f'(x_n)", "x_{n+1} = x_n + f(x_n) / f'(x_n)", "x_{n+1} = x_n - f'(x_n) / f(x_n)", "x_{n+1} = [x_n + f(x_n)] / 2"],
            "correct_answer": "A",
            "explanation": "Newton-Raphson uses the tangent slope at x_n: x_{n+1} = x_n - f(x_n) / f'(x_n)."
        },
        {
            "id": "ACAD-09-03",
            "question": "Under what condition does the Newton-Raphson method fail or breakdown completely?",
            "options": ["When f(x_n) = 0", "When f'(x_n) = 0 (tangent line is parallel to x-axis)", "When f''(x_n) > 0", "When the initial guess is an integer"],
            "correct_answer": "B",
            "explanation": "If the first derivative f'(x_n) becomes zero, division by zero occurs because the tangent line is horizontal and never intersects the x-axis."
        },
        {
            "id": "ACAD-09-04",
            "question": "How does the Regula-Falsi (False Position) method differ geometrically from the Bisection method?",
            "options": ["It uses the arithmetic midpoint (a + b) / 2 to divide the interval", "It connects (a, f(a)) and (b, f(b)) with a secant straight line and finds its x-intercept", "It uses the tangent line at the midpoint", "It requires evaluating the second derivative"],
            "correct_answer": "B",
            "explanation": "Regula-Falsi replaces the midpoint subdivision with the x-intercept of the secant chord joining (a, f(a)) and (b, f(b)): c = [a*f(b) - b*f(a)] / [f(b) - f(a)]."
        },
        {
            "id": "ACAD-09-05",
            "question": "Using the Newton-Raphson iteration formula x_{n+1} = 0.5 * (x_n + N / x_n), what value is being computed?",
            "options": ["N^2", "1 / N", "sqrt(N)", "log(N)"],
            "correct_answer": "C",
            "explanation": "Applying Newton-Raphson to f(x) = x^2 - N = 0 yields x_{n+1} = x_n - (x_n^2 - N)/(2x_n) = 0.5 * (x_n + N / x_n), which computes sqrt(N)."
        }
    ],

    10: [
        {
            "id": "ACAD-10-01",
            "question": "In the Java Collections Framework, what is the key difference between ArrayList and LinkedList for positional index-based retrieval (get(i))?",
            "options": ["ArrayList is O(1) random access, while LinkedList is O(N) sequential traversal", "ArrayList is O(N) and LinkedList is O(1)", "Both provide O(1) lookup", "LinkedList consumes less memory per node than ArrayList"],
            "correct_answer": "A",
            "explanation": "ArrayList is backed by a contiguous array, allowing O(1) random index access. LinkedList requires traversing node pointers from head/tail in O(N)."
        },
        {
            "id": "ACAD-10-02",
            "question": "How does HashMap in Java 8+ handle severe hash collisions inside a single bucket when the chain length exceeds TREEIFY_THRESHOLD (8)?",
            "options": ["It drops incoming keys with a HashCollisionException", "It converts the linked list bucket into a balanced Red-Black Tree, improving lookup from O(N) to O(log N)", "It increases heap allocation by 10x immediately", "It converts the hash table into an array of linked lists"],
            "correct_answer": "B",
            "explanation": "Java 8 optimizes hash collisions: once a bucket's linked list reaches 8 nodes (and table capacity >= 64), it morphs into a Red-Black Tree for O(log N) search."
        },
        {
            "id": "ACAD-10-03",
            "question": "Which of the following collection classes is synchronized and thread-safe by default in Java?",
            "options": ["java.util.ArrayList", "java.util.HashMap", "java.util.Vector", "java.util.HashSet"],
            "correct_answer": "C",
            "explanation": "Vector and Hashtable are legacy collections whose methods are synchronized. Modern code uses ConcurrentHashMap or Collections.synchronizedList()."
        },
        {
            "id": "ACAD-10-04",
            "question": "What is the default initial capacity and default load factor of a java.util.HashMap?",
            "options": ["Capacity = 10, Load Factor = 0.5", "Capacity = 16, Load Factor = 0.75", "Capacity = 32, Load Factor = 0.8", "Capacity = 64, Load Factor = 1.0"],
            "correct_answer": "B",
            "explanation": "By default, HashMap initializes with a bucket array capacity of 16 and a load factor of 0.75 (rehashing occurs when size reaches 16 * 0.75 = 12)."
        },
        {
            "id": "ACAD-10-05",
            "question": "What contract must be maintained between the equals() and hashCode() methods in Java?",
            "options": ["If two objects have the same hashCode, they must be equal via equals()", "If two objects are equal according to equals(), they must produce the same integer hashCode", "hashCode() must return a prime number for all objects", "equals() cannot be overridden without declaring the class final"],
            "correct_answer": "B",
            "explanation": "The Java contract requires: if `a.equals(b)` is true, then `a.hashCode() == b.hashCode()` must strictly hold to ensure correct behavior in hash collections."
        }
    ]
}

def get_academic_mcqs_for_day(day: int) -> list:
    """Returns 5 high-yield, authentic academic MCQs for the specified day."""
    if day in ACADEMIC_MCQS:
        return ACADEMIC_MCQS[day]
    # For days 11 to 30, generate structured syllabus-grounded MCQs based on subject syllabus
    return _generate_syllabus_academic_mcqs(day)

def _generate_syllabus_academic_mcqs(day: int) -> list:
    """Generates syllabus-grounded academic MCQs for days 11-30 based on authentic CSJMU syllabi."""
    # Mapping for days 11-30
    catalog = {
        11: ("BCA-5003", "Computer Networks", "Flow Control & Sliding Window Protocols", [
            ("What is the maximum sender window size in the Go-Back-N ARQ protocol using m-bit sequence numbers?", ["2^m", "2^m - 1", "2^(m-1)", "m^2"], "B", "In GBN, window size is 2^m - 1 to prevent ambiguity when all ACKs are lost."),
            ("In Stop-and-Wait ARQ, what sequence numbers are required for packet transmission?", ["0 and 1 only (1-bit)", "0 to 15", "0 to 255", "Any 32-bit integer"], "A", "Stop-and-Wait alternates between sequence numbers 0 and 1, requiring only a 1-bit sequence field."),
            ("What happens in Selective Repeat ARQ when a single frame in the transmission window is corrupted?", ["Sender retransmits all subsequent frames from that frame onwards", "Sender retransmits ONLY the specific unacknowledged frame via NAK/timeout", "Receiver resets the entire connection", "Sender terminates flow control"], "B", "Selective Repeat buffers out-of-order frames and requests retransmission of only the lost frame."),
            ("What is the sender window size in Selective Repeat ARQ using m-bit sequence numbering?", ["2^m - 1", "2^(m - 1)", "2^m", "m / 2"], "B", "In Selective Repeat, sender and receiver window sizes are equal to at most 2^(m - 1) to avoid overlap."),
            ("How is channel link utilization (efficiency U) defined in Stop-and-Wait protocol where propagation time is Tp and transmission time is Tt?", ["1 / (1 + 2a), where a = Tp / Tt", "1 + 2a", "2a / (1 + a)", "Tt / Tp"], "A", "Efficiency U = Tt / (Tt + 2Tp) = 1 / (1 + 2a), showing performance degradation over high-latency links.")
        ]),
        12: ("BCA-5001", "Knowledge Management", "Data Warehousing & Dimensional Modeling", [
            ("In dimensional data warehouse modeling, how is a Star Schema structured?", ["A central fact table linked directly to denormalized dimension tables", "A normalized fact table with multiple parent tables", "A completely flat single CSV spreadsheet", "A peer-to-peer network of dimension tables"], "A", "A star schema features a central numeric fact table surrounded by single-level denormalized dimension tables."),
            ("How does a Snowflake Schema differ fundamentally from a Star Schema?", ["The fact table is split into multiple sub-facts", "Dimension tables are normalized into 3NF hierarchies, splitting into sub-dimension tables", "It does not use foreign keys", "It cannot store historical time-series data"], "B", "Snowflake normalizes dimension tables into multiple related tables, reducing redundancy but increasing join complexity."),
            ("What characterizes a Fact Table in a Data Warehouse?", ["Contains descriptive textual names and addresses", "Contains quantitative numerical measures (metrics) and foreign keys referencing dimensions", "Contains only SQL stored procedures", "Stores only network routing tables"], "B", "Fact tables store additive, semi-additive numerical metrics (e.g., units sold, total revenue) and dimension foreign keys."),
            ("What are the three tiers in the standard Data Warehouse 3-tier architecture?", ["Client Tier, Web Server Tier, Application Tier", "Bottom Tier (Warehouse DB Server), Middle Tier (OLAP Server), Top Tier (Front-end Client Tools)", "Physical Layer, Data Link Layer, Network Layer", "Compiler, Assembler, Linker"], "B", "The 3 tiers are: Bottom (Relational DBMS & ETL staging), Middle (OLAP multidimensional engine), Top (BI query/reporting)."),
            ("What is the primary difference between ROLAP and MOLAP?", ["ROLAP uses relational tables with star schemas; MOLAP uses precomputed multi-dimensional array cubes", "ROLAP is always faster than MOLAP", "MOLAP does not support slicing and dicing", "ROLAP can only store images"], "A", "ROLAP accesses relational databases directly via SQL; MOLAP stores data in optimized multidimensional array data cubes.")
        ]),
        13: ("BCA-5004", "Numerical Methods", "Direct Methods for Linear Systems", [
            ("In Gauss Elimination, what is the purpose of 'Partial Pivoting'?", ["To reduce execution time by 50%", "To prevent division by zero and minimize floating-point round-off errors by selecting the largest magnitude pivot element", "To invert the matrix automatically", "To compute eigenvalues directly"], "B", "Partial pivoting swaps rows so the largest absolute value in the current column becomes the pivot, preventing instability."),
            ("What triangular matrix form does the coefficient matrix assume at the end of the forward elimination phase of Gauss Elimination?", ["Lower Triangular Matrix", "Upper Triangular Matrix", "Diagonal Matrix", "Identity Matrix"], "A", "Forward elimination zeroes out elements below the main diagonal, transforming the system into an Upper Triangular Matrix."),
            ("How does the Gauss-Jordan method differ from standard Gauss Elimination?", ["It uses random guessing instead of algebra", "It eliminates elements both below AND above the main diagonal, directly yielding an Identity Matrix without back substitution", "It only works on 2x2 matrices", "It requires evaluating determinants at each step"], "B", "Gauss-Jordan reduces the augmented matrix to reduced row echelon form (identity matrix), yielding solutions directly."),
            ("What is the computational operation count (time complexity) of Gauss Elimination for an n x n system?", ["O(n)", "O(n^2)", "O(n^3 / 3)", "O(2^n)"], "C", "Gauss Elimination requires approximately (2/3)n^3 arithmetic operations for forward elimination and O(n^2) for back substitution."),
            ("A system of linear equations AX = B has a unique solution if and only if:", ["det(A) = 0", "det(A) != 0 (A is non-singular)", "Rank of A < Rank of [A|B]", "Matrix A is asymmetric"], "B", "A unique solution exists when the coefficient matrix A is non-singular with non-zero determinant (full rank).")
        ]),
        14: ("BCA-5002", "Java Programming", "Generics, Reflection & Annotations", [
            ("What mechanism does the Java compiler use to implement Generics while maintaining backward compatibility with older JVM versions?", ["Dynamic byte generation", "Type Erasure (replacing generic types with their bounds or Object at compile time)", "C++ template specialization", "Multiple virtual tables"], "B", "Type Erasure removes all generic type information during compilation, inserting necessary casts and keeping bytecode backward compatible."),
            ("In Java Generics, what does the wildcard expression `List<? extends Number>` signify?", ["A list that can store any Object", "An upper-bounded wildcard: a list of elements of type Number or any subtype of Number (read-only producer)", "A lower-bounded wildcard accepting only Object", "A synchronized thread-safe array"], "B", "Upper bounded wildcard `? extends T` enforces covariance: the collection produces elements of type T (PECS: Producer Extends)."),
            ("Which Java API allows runtime inspection of classes, methods, fields, and constructors, including invoking private methods dynamically?", ["Java Collections API", "Java Reflection API (java.lang.reflect)", "Java NIO API", "Java Native Interface (JNI)"], "B", "Reflection provides programmatic introspection and dynamic invocation of class metadata and private members at runtime."),
            ("What retention policy must be specified on a custom Java annotation so it remains available in bytecode and inspectable via Reflection at runtime?", ["RetentionPolicy.SOURCE", "RetentionPolicy.CLASS", "RetentionPolicy.RUNTIME", "RetentionPolicy.SYSTEM"], "C", "RetentionPolicy.RUNTIME records annotations in the .class file and makes them accessible to the JVM Reflection engine at runtime."),
            ("What is the effect of PECS (Producer Extends, Consumer Super) in Java Generics?", ["Use 'extends' when you only read from a collection; use 'super' when you only write to a collection", "Use 'super' for return values and 'extends' for method arguments always", "Generics cannot be combined with wildcards", "Extends allows adding any object to the collection"], "A", "PECS rule: If a parameterized collection produces data (read-only), use `? extends`; if it consumes data (write-only), use `? super`.")
        ]),
        15: ("BCA-5003", "Computer Networks", "IPv4 Addressing, Subnetting & CIDR", [
            ("How many host addresses can be assigned to devices on a subnetwork configured with a `/26` CIDR prefix?", ["64 hosts", "62 hosts (2^6 - 2)", "32 hosts", "30 hosts"], "B", "A /26 mask leaves 32 - 26 = 6 host bits. Total addresses = 2^6 = 64. Subtracting network and broadcast addresses leaves 62 usable hosts."),
            ("What is the default subnet mask for an IPv4 Class B network address?", ["255.0.0.0 (/8)", "255.255.0.0 (/16)", "255.255.255.0 (/24)", "255.255.255.240 (/28)"], "B", "Class B addresses (first octet 128-191) use a 16-bit network prefix: 255.255.0.0 (/16)."),
            ("What is the primary purpose of Classless Inter-Domain Routing (CIDR)?", ["To encrypt IP packets on public Wi-Fi", "To slow the exhaustion of IPv4 addresses and reduce global router routing table size via route aggregation (supernetting)", "To replace MAC addresses with domain names", "To convert IPv4 packets directly into IPv6"], "B", "CIDR eliminates rigid A/B/C classes, allowing arbitrary prefix lengths (/n) and hierarchical route summarization."),
            ("Which of the following IP addresses represents a private IPv4 address defined in RFC 1918?", ["8.8.8.8", "172.20.14.5", "198.51.100.1", "127.0.0.1"], "B", "RFC 1918 private ranges: 10.0.0.0/8, 172.16.0.0/12 (172.16 - 172.31), and 192.168.0.0/16. 172.20.14.5 is private."),
            ("What is the broadcast address for the subnet `192.168.1.32/27`?", ["192.168.1.32", "192.168.1.63", "192.168.1.64", "192.168.1.255"], "B", "A /27 subnet has block size 2^(32-27) = 32. Subnet starts at .32 and ends at .63 (broadcast address is .63).")
        ]),
        16: ("BCA-5001", "Knowledge Management", "Knowledge Sharing & Communities of Practice", [
            ("What is a 'Community of Practice' (CoP) in an enterprise Knowledge Management ecosystem?", ["An official disciplinary board that terminates underperforming employees", "An informal, self-organizing group of practitioners who share a passion or domain and interact regularly to improve their craft", "A software tool for running payroll calculations", "A hardware firewall preventing external internet access"], "B", "CoPs (Lave & Wenger) are groups of people bound by informal expertise and shared passion to solve problems collaboratively."),
            ("What is the primary cultural barrier to successful knowledge sharing in corporate organizations?", ["Lack of Gigabit Ethernet bandwidth", "'Knowledge is Power' hoarding syndrome where individuals fear losing personal value by sharing expertise", "Using Linux instead of Windows", "Too many database backups"], "B", "Knowledge hoarding arises when organizations fail to incentivize transparency, causing experts to treat knowledge as individual leverage."),
            ("Which KM capture mechanism pairs a junior engineer with an experienced expert to observe and absorb intuitive problem-solving heuristics?", ["Database Normalization", "Apprenticeship / Shadowing", "Web Scraping", "Binary Search"], "B", "Shadowing and mentoring enable direct tacit-to-tacit knowledge transfer through contextual observation and guided reflection."),
            ("In knowledge management metrics, what does the 'Knowledge Retention Rate' measure?", ["The percentage of hard drives retained during data center upgrades", "The organization's ability to preserve mission-critical institutional expertise when senior employees leave or retire", "The speed of RAM cache memory", "The ratio of SQL queries to web visits"], "B", "Retention rate quantifies an organization's capacity to codify and transition institutional memory before attrition occurs."),
            ("What role does an After Action Review (AAR) play in organizational learning?", ["It calculates end-of-year tax liabilities", "It provides a structured debrief immediately following a project to analyze what was expected, what actually occurred, and why", "It terminates software licenses", "It formats database tables into 3NF"], "B", "Originating in the US Army, an AAR is a structured 4-question debrief that captures operational lessons learned before memories fade.")
        ]),
        17: ("BCA-5004", "Numerical Methods", "Iterative Methods for Linear Systems", [
            ("What condition guarantees the convergence of both Gauss-Jacobi and Gauss-Seidel iterative methods for solving AX = B?", ["Matrix A is skew-symmetric", "Matrix A is Strictly Diagonally Dominant (|a_ii| > sum_{j!=i} |a_ij| for all rows)", "det(A) < 1", "All elements of A are negative"], "B", "Strict diagonal dominance guarantees that iterative approximations converge to the unique solution regardless of initial guess."),
            ("How does Gauss-Seidel iteration differ from the Gauss-Jacobi method?", ["Gauss-Seidel uses the most freshly computed variable values immediately in the current iteration", "Gauss-Jacobi converges twice as fast as Gauss-Seidel", "Gauss-Seidel cannot be used for 3x3 systems", "Gauss-Jacobi does not require matrix coefficients"], "A", "Gauss-Seidel updates variables in-place, using x_1^{(k+1)} immediately to calculate x_2^{(k+1)}, converging roughly twice as fast as Jacobi."),
            ("In iterative methods, what does the relaxation parameter omega represent in the Successive Over-Relaxation (SOR) method?", ["Matrix inversion scale", "An extrapolation factor where 1 < omega < 2 accelerates convergence compared to standard Gauss-Seidel", "The number of CPU threads allocated", "The floating point precision epsilon"], "B", "SOR accelerates Gauss-Seidel by weighting the new estimate with a relaxation factor (1 < omega < 2 for over-relaxation)."),
            ("If an iterative method computes x^{(k+1)} = [2.001, 3.999] and x^{(k)} = [2.000, 4.000], what is the absolute error norm ||x^{(k+1)} - x^{(k)}||_infinity?", ["0.001", "0.002", "0.000", "0.010"], "A", "The infinity norm is the maximum absolute difference across components: max(|2.001 - 2.000|, |3.999 - 4.000|) = 0.001."),
            ("Why are iterative methods (Jacobi, Seidel) preferred over direct methods (Gauss Elimination) for very large sparse systems (e.g., 100,000 equations)?", ["They require O(N) storage preserving zero entries and avoid massive O(N^3) matrix fill-in", "They always produce exact solutions without rounding errors", "They do not require initial guesses", "They only use integer multiplication"], "A", "Sparse systems from PDEs have mostly zero entries. Iterative methods avoid fill-in and have O(N) memory and per-iteration work.")
        ]),
        18: ("BCA-5002", "Java Programming", "JDBC Architecture & Database Connectivity", [
            ("Which JDBC driver type is known as the 'Pure Java Native Protocol Driver' (Type 4) and communicates directly with the database engine without client libraries?", ["Type 1 (JDBC-ODBC Bridge)", "Type 2 (Native-API Driver)", "Type 3 (Network-Protocol Driver)", "Type 4 (Direct Native-Protocol Pure Java Driver)"], "D", "Type 4 drivers are 100% pure Java, converting JDBC calls directly into vendor-specific network socket protocols without middleware."),
            ("Why is PreparedStatement preferred over standard Statement in JDBC for executing parameterized queries?", ["PreparedStatement compiles SQL once on the database server, improves execution speed, and inherently prevents SQL Injection", "PreparedStatement allows executing non-SQL Python scripts", "PreparedStatement does not require a database connection", "Standard Statement cannot execute SELECT queries"], "A", "PreparedStatement pre-compiles SQL plans and treats parameters as strictly typed literals, neutralizing SQL injection attacks."),
            ("What JDBC interface method must be called to process the tabular rows returned by an `executeQuery()` statement?", ["ResultSet.next()", "ResultSet.fetch()", "Connection.commit()", "Statement.scroll()"], "A", "ResultSet.next() moves the cursor forward one row from its initial position before the first row, returning false when exhausted."),
            ("How does database Connection Pooling improve enterprise web application performance?", ["It permanently encrypts all database tables", "It reuses an existing pool of pre-established physical connections, avoiding the expensive overhead of TCP handshakes and authentication on every request", "It eliminates the need for SQL transactions", "It compresses all JPEG images in the database"], "B", "Opening a DB connection takes 50-200ms. Pooling keeps open connections ready for checkout, reducing acquisition latency to <1ms."),
            ("To execute multiple transactional SQL updates atomically, what method must be called on the JDBC Connection before executing queries?", ["connection.setAutoCommit(false)", "connection.close()", "connection.rollback()", "connection.setReadOnly(true)"], "A", "Disabling auto-commit (`setAutoCommit(false)`) groups operations into an atomic transaction concluded with `commit()` or `rollback()`.")
        ]),
        19: ("BCA-5003", "Computer Networks", "Network Layer Routing Algorithms", [
            ("Which shortest path algorithm does the Open Shortest Path First (OSPF) Link-State routing protocol use to build its routing table?", ["Bellman-Ford Algorithm", "Dijkstra's Shortest Path Algorithm", "Floyd-Warshall Algorithm", "Kruskal's Minimum Spanning Tree Algorithm"], "B", "OSPF is a Link-State protocol; every router floods Link State Advertisements (LSAs) and runs Dijkstra's algorithm locally."),
            ("What critical flaw affects the Distance Vector Routing (DVR) algorithm based on Bellman-Ford when a link or destination goes down?", ["Split Horizon failure", "Count-to-Infinity problem and slow convergence loops", "Buffer bloat deadlock", "Checksum collision"], "B", "In DVR, routers advertise distances without full topology paths, causing routing loops and the 'Count-to-Infinity' phenomenon during link failures."),
            ("What two mechanisms are commonly implemented to mitigate the Count-to-Infinity problem in Distance Vector routing?", ["Split Horizon and Poison Reverse", "Dijkstra and Prim algorithms", "Three-way handshakes and FIN packets", "Parity check and Hamming codes"], "A", "Split Horizon prevents advertising a route back on the interface from which it was learned; Poison Reverse sets the metric to infinity (16)."),
            ("In hierarchical routing, what protocol is used to route traffic BETWEEN autonomous systems across the global Internet backbone?", ["Routing Information Protocol (RIP)", "Open Shortest Path First (OSPF)", "Border Gateway Protocol (BGP-4)", "Address Resolution Protocol (ARP)"], "C", "BGP is the de-facto inter-domain routing protocol (Path Vector) establishing policy and reachability between Autonomous Systems (AS)."),
            ("What is the metric used by the legacy Routing Information Protocol (RIP) to calculate distance?", ["Bandwidth delay product", "Hop count (maximum 15 hops, 16 represents infinity)", "Packet drop probability", "Link dollar cost"], "B", "RIP uses hop count as its sole metric, capping network diameters at 15 hops to limit convergence loops.")
        ]),
        20: ("BCA-5001", "Knowledge Management", "KMSLC & Knowledge Evaluation Metrics", [
            ("How does the Knowledge Management System Life Cycle (KMSLC) differ from the conventional Software Development Life Cycle (SDLC)?", ["KMSLC is purely linear (Waterfall), while SDLC is iterative", "KMSLC is iterative and user-centered because knowledge is dynamic, experiential, and evolves continuously through human interaction", "KMSLC does not require any software testing", "SDLC only applies to mechanical engineering"], "B", "Unlike deterministic procedural software in SDLC, KM systems deal with ambiguous, evolving cognitive heuristics requiring iterative refinement."),
            ("What is the first foundational stage of the 8-stage KMSLC framework?", ["System Deployment", "Evaluating Existing Infrastructure and Knowledge Assets", "Forming the Knowledge Management Team", "Designing the KM Blueprint"], "B", "KMSLC begins with evaluating existing organizational infrastructure, intellectual capital, and business strategies to identify gaps."),
            ("In KM project evaluation, what does the Balanced Scorecard framework assess?", ["Only the quarterly financial net profit", "Performance across four perspectives: Financial, Customer, Internal Business Processes, and Learning & Growth", "The number of hours employees spend reading manuals", "The total storage capacity of the server rack"], "B", "Kaplan and Norton's Balanced Scorecard balances financial indicators with operational, customer, and continuous learning metrics."),
            ("What role does a Chief Knowledge Officer (CKO) play in an enterprise?", ["Writing Java bytecode for database drivers", "Championing KM initiatives, aligning knowledge architecture with corporate strategy, and fostering a collaborative learning culture", "Resetting user email passwords", "Purchasing office computer monitors"], "B", "The CKO is the executive leader responsible for maximizing intellectual capital, breaking down information silos, and driving KM strategy."),
            ("What is a 'Knowledge Audit'?", ["An IRS tax examination of company profits", "A systematic evaluation of an organization's knowledge needs, existing knowledge assets, flows, gaps, and blockages", "A daily antivirus scan of hard drives", "A count of total paper files in a storage cabinet"], "B", "A knowledge audit identifies what knowledge assets exist, who holds them, where gaps exist, and how information flows across teams.")
        ]),
        21: ("BCA-5004", "Numerical Methods", "Interpolation with Equal Intervals", [
            ("When should Newton's Forward Difference Interpolation formula be chosen over Newton's Backward formula?", ["When the target interpolation value x lies near the beginning of the tabulated values", "When x lies near the end of the table", "When the values of x are spaced at unequal intervals", "When f(x) is a discontinuous function"], "A", "Newton's Forward formula is derived using forward differences from x_0 and gives optimal precision for points near the start of the table."),
            ("What is the relationship between the Forward Difference operator (Delta) and the Shift operator (E)?", ["Delta = E + 1", "Delta = E - 1 (or E = 1 + Delta)", "Delta = E * 2", "Delta = 1 / E"], "B", "By definition, Delta f(x) = f(x + h) - f(x) = E f(x) - f(x) = (E - 1) f(x), hence Delta = E - 1."),
            ("If a polynomial of degree n is tabulated at equidistant intervals, what is the value of its (n+1)-th forward difference Delta^{n+1} f(x)?", ["A non-zero constant", "0 (Zero)", "n!", "Infinity"], "B", "The n-th difference of an n-th degree polynomial is constant (Delta^n f(x) = a_n * n! * h^n), so all higher differences (n+1 and above) are identically zero."),
            ("What is the formula for the dimensionless parameter u in Newton's Forward Difference interpolation formula?", ["u = (x - x_n) / h", "u = (x - x_0) / h", "u = (x_0 + x_n) / 2", "u = x * h"], "B", "In forward interpolation, u = (x - x_0) / h, where x_0 is the initial table value and h is the uniform step interval."),
            ("What is the Backward Difference operator (Nabla) defined as?", ["Nabla f(x) = f(x) - f(x - h)", "Nabla f(x) = f(x + h) - f(x)", "Nabla f(x) = f(x + h) + f(x - h)", "Nabla f(x) = f(x) / h"], "A", "The backward difference operator Nabla subtracts the preceding point: Nabla f(x) = f(x) - f(x - h).")
        ]),
        22: ("BCA-5002", "Java Programming", "Servlets & Web Architecture", [
            ("Which lifecycle method of a Java Servlet is invoked exactly once by the servlet container when the servlet is first instantiated?", ["service()", "init()", "doGet()", "destroy()"], "B", "The container calls `init(ServletConfig config)` once during initialization to allocate resources before servicing client requests."),
            ("In the Java Servlet lifecycle, which method dispatches incoming HTTP requests to doGet(), doPost(), doPut(), etc., based on the request method?", ["service(ServletRequest, ServletResponse)", "init()", "start()", "run()"], "A", "The `service()` method reads HTTP method headers and delegates the request to the corresponding specialized `doGet/doPost` handler."),
            ("Why is HttpServletSession preferred over plain Cookies for storing sensitive user authentication tokens?", ["Cookies cannot store more than 1 byte of data", "Session data is stored securely on the server-side, with only an opaque session identifier (JSESSIONID) sent to the client browser", "Cookies expire immediately when a tab is refreshed", "Sessions do not consume server RAM"], "B", "HttpSession stores state in server memory, transmitting only an arbitrary cookie ID, protecting sensitive attributes from client tampering."),
            ("What deployment descriptor file traditionally configured servlet mappings and initialization parameters in Java EE applications before annotations?", ["pom.xml", "web.xml (located in WEB-INF)", "server.xml", "context.xml"], "B", "The `WEB-INF/web.xml` deployment descriptor historically configured servlet classes, URL patterns, context params, and filters."),
            ("Which modern annotation replaces the need for `<servlet>` and `<servlet-mapping>` declarations in `web.xml` in Servlet 3.0+?", ["@WebServlet", "@Controller", "@Service", "@WebEndpoint"], "A", "Servlet 3.0 introduced `@WebServlet(urlPatterns = \"/path\")`, allowing declarative configuration directly in Java source code.")
        ]),
        23: ("BCA-5003", "Computer Networks", "Transport Layer Protocols & Congestion Control", [
            ("In the TCP 3-way handshake to establish a reliable connection, what sequence of control flags is exchanged between client and server?", ["SYN -> SYN-ACK -> ACK", "ACK -> SYN -> FIN", "SYN -> ACK -> RST", "PING -> PONG -> ACK"], "A", "Connection establishment: Client sends SYN, Server replies with SYN + ACK, and Client confirms with final ACK."),
            ("How does TCP handle Congestion Control during the initial 'Slow Start' phase upon connection startup?", ["It sets window size to maximum bandwidth immediately", "It initializes Congestion Window (cwnd) to 1 MSS and doubles cwnd every RTT (exponential growth) until ssthresh is reached", "It drops every alternate packet", "It transmits UDP datagrams instead"], "B", "Slow Start probes network capacity exponentially: cwnd doubles every round-trip time until reaching the slow start threshold (ssthresh)."),
            ("What mechanism does TCP use during Congestion Avoidance after cwnd exceeds ssthresh?", ["Additive Increase Multiplicative Decrease (AIMD) — increasing cwnd by 1 MSS per RTT", "Exponential doubling", "Immediate connection reset", "Halving the window every second"], "A", "In Congestion Avoidance, AIMD provides linear window expansion (+1 MSS per RTT) to stabilize throughput near link capacity."),
            ("What is the primary architectural difference between TCP and UDP?", ["TCP is connection-oriented, reliable, and provides byte-stream ordering; UDP is connectionless, unreliable, and datagram-oriented", "UDP provides guaranteed packet delivery while TCP does not", "TCP only runs over optical fiber while UDP runs over copper", "UDP uses 64-bit port numbers"], "A", "TCP guarantees in-order reliable delivery via acknowledgments and retries; UDP provides lightweight, low-latency best-effort transmission."),
            ("What is the size of the standard base IPv4 and TCP headers without options?", ["20 bytes for IPv4 and 20 bytes for TCP (40 bytes total overhead)", "8 bytes for IPv4 and 8 bytes for TCP", "64 bytes each", "4 bytes each"], "A", "Both IPv4 and TCP base headers have a minimum length of 20 bytes each (5 32-bit words), yielding a combined 40-byte base header.")
        ]),
        24: ("BCA-5004", "Numerical Methods", "Interpolation with Unequal Intervals", [
            ("Which interpolation formula is designed specifically for calculating values when the given independent variable arguments x_i are spaced at UNEQUAL intervals?", ["Newton's Forward Interpolation Formula", "Lagrange's Interpolation Formula", "Newton's Backward Interpolation Formula", "Trapezoidal Rule"], "B", "Lagrange's and Newton's Divided Difference formulas do not require equal step spacing h, handling arbitrary data points."),
            ("What is the degree of the Lagrange interpolating polynomial passing through (n + 1) distinct points?", ["At most n", "Exactly n + 1", "Always 1", "n^2"], "A", "A unique polynomial of degree at most n can be passed through (n + 1) distinct points (x_0, y_0) ... (x_n, y_n)."),
            ("What is the mathematical property of the Lagrange basis polynomial L_i(x) evaluated at data point x_j?", ["L_i(x_j) = 1 if i = j, and L_i(x_j) = 0 if i != j (Kronecker delta)", "L_i(x_j) = 0 always", "L_i(x_j) = infinity", "L_i(x_j) = x_i - x_j"], "A", "Lagrange basis polynomials satisfy the Kronecker delta property: L_i(x_j) = delta_{ij}, ensuring the sum equals y_j at x = x_j."),
            ("What is the primary computational disadvantage of Lagrange's interpolation formula when a new data point is added to the table?", ["It cannot handle negative numbers", "All basis polynomial coefficients must be recomputed from scratch", "It causes division by zero", "It requires matrix inversion"], "B", "Lagrange formulas lack recurrence: adding one point requires recalculating all terms. Divided differences avoid this via incremental terms."),
            ("The first divided difference f[x_0, x_1] of a function f(x) is defined as:", ["[f(x_1) - f(x_0)] / (x_1 - x_0)", "[f(x_1) + f(x_0)] / 2", "f(x_1) * (x_1 - x_0)", "f'(x_0)"], "A", "The first divided difference represents the secant slope between the two points: f[x_0, x_1] = (f(x_1) - f(x_0)) / (x_1 - x_0).")
        ]),
        25: ("BCA-5002", "Java Programming", "JSP Architecture & Directives", [
            ("When a JavaServer Page (.jsp) is requested for the first time, what translation step occurs inside the web container?", ["The JSP is compiled directly into a C++ binary", "The JSP engine translates the JSP source into an equivalent Java Servlet source code (.java) and compiles it into a .class file", "The browser compiles the JSP locally using V8", "The page is converted into a static PDF file"], "B", "JSP is a high-level servlet abstraction: the container converts .jsp into a Java Servlet (`_jspService`), then compiles and executes it."),
            ("Which JSP scripting element syntax `<%= expression %>` is used to output values directly into the client response stream?", ["JSP Scriptlet", "JSP Expression", "JSP Declaration", "JSP Directive"], "B", "JSP Expression (`<%= expr %>`) evaluates the Java expression, converts the result to String, and writes it directly to the response output stream."),
            ("Which JSP directive defines page-wide attributes such as imported Java packages, error pages, and session participation?", ["<%@ include ... %>", "<%@ page ... %>", "<%@ taglib ... %>", "<%@ forward ... %>"], "B", "The `<%@ page ... %>` directive specifies page settings (e.g., `<%@ page import=\"java.util.*\" session=\"true\" errorPage=\"err.jsp\" %>`)."),
            ("What is the key difference between `<%@ include file=\"header.jsp\" %>` and `<jsp:include page=\"header.jsp\" />`?", ["Directive include is static at translation time; standard action `<jsp:include>` is dynamic at request runtime", "Directive include executes faster in Python", "Action include cannot accept parameters", "There is no difference"], "A", "The include directive merges file source code at translation time; `<jsp:include>` invokes the target servlet dynamically at runtime."),
            ("What scope in JSP stores attributes that are accessible to all users and all servlets across the entire web application?", ["page scope", "request scope", "session scope", "application scope (ServletContext)"], "D", "Application scope (`application` implicit object / ServletContext) is global, accessible by all sessions across the web application.")
        ]),
        26: ("BCA-5003", "Computer Networks", "Application Layer Protocols & DNS", [
            ("In the Domain Name System (DNS), which DNS resource record type maps a domain hostname directly to its corresponding 32-bit IPv4 address?", ["A Record", "AAAA Record", "CNAME Record", "MX Record"], "A", "An 'A' record maps a hostname to an IPv4 address; 'AAAA' maps to IPv6; 'CNAME' aliases one name to another; 'MX' specifies mail servers."),
            ("How does HTTP/2 achieve superior multiplexing and latency reduction compared to HTTP/1.1?", ["By removing TCP completely", "By using a binary framing layer over a single persistent TCP connection, interleaving multiple bidirectional streams without Head-of-Line blocking", "By compressing images with lossy algorithms", "By limiting requests to 10 per second"], "B", "HTTP/2 introduces binary framing and stream multiplexing over a single connection, eliminating HTTP-level head-of-line pipelining delays."),
            ("Which transport protocol and port does DNS primarily use for standard client domain name resolution queries?", ["TCP port 80", "UDP port 53", "TCP port 443", "UDP port 67"], "B", "Standard DNS queries use lightweight UDP on port 53 for speed. Zone transfers and replies exceeding 512 bytes fallback to TCP port 53."),
            ("What cryptographic protocol secures HTTP traffic (HTTPS), providing data encryption, server authentication, and message integrity?", ["Transport Layer Security (TLS / SSL)", "Point-to-Point Protocol (PPP)", "Border Gateway Protocol (BGP)", "Simple Mail Transfer Protocol (SMTP)"], "A", "HTTPS runs standard HTTP over an encrypted TLS channel established via public-key cryptography and symmetric session ciphers."),
            ("What is the fundamental difference between POP3 and IMAP mail access protocols?", ["POP3 downloads and removes emails from the server locally; IMAP synchronizes folders bidirectionally, keeping emails stored on the server", "IMAP cannot read attachments", "POP3 requires TLS while IMAP is unencrypted", "POP3 is used to send emails while IMAP receives them"], "A", "POP3 downloads mail to a single local device. IMAP maintains server-side mailboxes, allowing seamless synchronization across multiple devices.")
        ]),
        27: ("BCA-5004", "Numerical Methods", "Numerical Quadrature & Integration", [
            ("What geometric curve does Simpson's 1/3 Rule fit across consecutive sets of three equidistant points to approximate the integral?", ["Straight lines (degree 1 polynomials)", "Parabolic arcs (degree 2 quadratic polynomials)", "Cubic splines (degree 3 polynomials)", "Exponential curves"], "B", "Simpson's 1/3 rule approximates the integrand by a 2nd-degree parabola over pairs of subintervals, requiring an EVEN number of intervals."),
            ("What restriction MUST the number of subintervals (n) satisfy when applying Simpson's 1/3 Rule?", ["n must be an odd number", "n must be an even number (or multiple of 2)", "n must be a multiple of 3", "n must be a prime number"], "B", "Since each parabolic segment spans two adjacent subintervals, Simpson's 1/3 Rule strictly requires an EVEN number of intervals (n = 2, 4, 6...)."),
            ("What is the mathematical formula for the composite Trapezoidal Rule for interval [a, b] with step size h?", ["(h / 2) * [ (y_0 + y_n) + 2*(y_1 + y_2 + ... + y_{n-1}) ]", "(h / 3) * [ (y_0 + y_n) + 4*(odd) + 2*(even) ]", "h * (y_0 + y_1 + ... + y_n)", "(3h / 8) * (sum of all y)"], "A", "Trapezoidal rule sums linear trapezoids: (h/2) * [First + Last + 2 * (Sum of all intermediate ordinates)]."),
            ("Which numerical integration rule requires the number of subintervals (n) to be a multiple of 3?", ["Trapezoidal Rule", "Simpson's 1/3 Rule", "Simpson's 3/8 Rule", "Euler's Method"], "C", "Simpson's 3/8 rule fits cubic polynomials over groups of three subintervals, necessitating n to be a multiple of 3 (n = 3, 6, 9...)."),
            ("What is the global truncation error order of the composite Simpson's 1/3 Rule?", ["O(h)", "O(h^2)", "O(h^4)", "O(h^6)"], "C", "The composite Simpson's 1/3 rule has a global truncation error of O(h^4), providing significantly higher precision than the O(h^2) Trapezoidal rule.")
        ]),
        28: ("BCA-5004", "Numerical Methods", "Numerical Solution of Ordinary Differential Equations (ODEs)", [
            ("In Euler's method for solving the initial value problem dy/dx = f(x, y), what is the iterative formula to find y_{n+1}?", ["y_{n+1} = y_n + h * f(x_n, y_n)", "y_{n+1} = y_n - h * f(x_n, y_n)", "y_{n+1} = y_n + (h / 2) * f(x_n, y_n)", "y_{n+1} = h * y_n"], "A", "Euler's method follows the tangent slope: y_{n+1} = y_n + h * f(x_n, y_n). It is a first-order method with local error O(h^2)."),
            ("What is the order of accuracy of the classical Runge-Kutta Fourth Order Method (RK4)?", ["First order O(h)", "Second order O(h^2)", "Fourth order O(h^4)", "Eighth order O(h^8)"], "C", "The classical RK4 method has a local truncation error of O(h^5) and a global truncation error of O(h^4), making it the gold standard ODE solver."),
            ("How many slope evaluations (k_1, k_2, k_3, k_4) are required at each step in the Runge-Kutta 4th Order (RK4) method?", ["1 evaluation", "2 evaluations", "4 evaluations", "8 evaluations"], "C", "RK4 computes 4 intermediate slopes: k1 at start, k2 and k3 at midpoint, and k4 at full step, combining them with weights (1, 2, 2, 1)/6."),
            ("Why is Euler's method rarely used in production engineering simulations despite its mathematical simplicity?", ["It cannot be programmed in Java", "It has low first-order accuracy and accumulates large cumulative truncation errors unless extremely tiny step sizes h are used", "It only solves differential equations with zero initial conditions", "It requires evaluating imaginary numbers"], "B", "Euler's method is only O(h) accurate globally; to cut error by 10x requires 10x smaller steps, making it computationally inefficient compared to RK4."),
            ("In the RK4 method, what is the formula combining the four slopes k_1, k_2, k_3, k_4 to calculate the displacement Delta y?", ["Delta y = (h / 6) * (k_1 + 2*k_2 + 2*k_3 + k_4)", "Delta y = (h / 4) * (k_1 + k_2 + k_3 + k_4)", "Delta y = h * (k_1 + k_4) / 2", "Delta y = (h / 3) * (k_1 + 4*k_2 + k_4)"], "A", "RK4 uses Simpson's-style weighting: Delta y = (h / 6) * [k_1 + 2*k_2 + 2*k_3 + k_4].")
        ]),
        29: ("CSJMU Comprehensive", "Academic Strategy", "15-Mark University Examination Blueprints", [
            ("In CSJM University 15-mark theory examination questions, what presentation component must immediately follow the formal technical definition to maximize score potential?", ["A personal diary reflection", "A labeled, structured architectural diagram or flow model", "A copy of the syllabus text", "The examiner's name"], "B", "University marking rubrics award 3-4 marks specifically for neat, labeled diagrams illustrating the theoretical mechanism."),
            ("What is the recommended time allocation for completing a single 15-mark university long question in a 3-hour (75-mark) theory paper?", ["10 minutes", "35 to 38 minutes", "75 minutes", "90 minutes"], "B", "A 180-minute paper with five long questions requires budgeting ~35 minutes per 15-mark answer, reserving 10 minutes for review."),
            ("Why are structured 4-column comparison tables (Criteria, Option A, Option B, Technical Distinction) superior to running prose paragraphs in semester exams?", ["They occupy more paper volume without saying anything", "Examiners scan tables rapidly; tabular criteria demonstrate analytical clarity and earn full allocated comparative marks", "Tables eliminate the need for technical definitions", "Tables are mandatory by university law"], "B", "Examiners grade against structured rubrics. Tables make criterion distinctions immediately visible, preventing mark deduction."),
            ("When presenting a numerical answer in Numerical Methods (BCA-5004), what protocol ensures zero loss of calculation marks?", ["Writing only the final decimal number without intermediate formulas", "Stating the governing formula, tabulating iteration steps with decimal precision, and boxing the final result with units/error bound", "Copying the question text repeatedly", "Using fractions instead of decimal places"], "B", "Showing intermediate iterations (x_0, x_1, errors) and boxing the final value demonstrates proof of calculation even if arithmetic slips occur."),
            ("What is the ideal closing component of a 15-mark university model answer?", ["A blank page", "A 2-to-3 sentence Technical Summary synthesizing industry relevance or enterprise deployment context", "An apology to the examiner", "A list of unrelated textbooks"], "B", "A concise concluding synthesis reinforces comprehension, demonstrating that the candidate understands practical enterprise application.")
        ]),
        30: ("CSJMU Comprehensive", "Academic Strategy", "Final Presentation & Examination Mastery", [
            ("During the first 5 minutes of a 3-hour university semester examination, what is the highest-leverage strategy?", ["Immediately start writing the first question on page 1", "Perform a strategic scan of all optional choices across Section B and C, marking the questions with the highest diagram and numerical certainty", "Leave the exam hall early", "Draw borders on all 32 blank pages"], "B", "Scanning the entire paper allows strategic selection of questions where you know complete diagrams, formulas, and proofs, optimizing total points."),
            ("If you discover an arithmetic error in a numerical calculation with 5 minutes remaining, what is the best tactical response?", ["Tear out the entire examination page", "Neatly strike through the incorrect calculation with a single line, write the corrected value clearly, and box the result", "Use white correction fluid across the entire answer", "Leave the wrong answer and panic"], "B", "A clean single-line strike-through with corrected values preserves legible working steps for partial credit without looking messy."),
            ("What visual cue should be used throughout an examination paper to anchor key terminology for speed-grading examiners?", ["Underlining or highlighting keywords, bolding lead-ins, and boxing final answers", "Writing in microscopic handwriting", "Writing in pencil only", "Using multiple colors of crayon"], "A", "Clear visual hierarchy (bold headings, boxed formulas, underlined keywords) guides the examiner's eye directly to key rubric criteria."),
            ("In Computer Networks questions involving protocols (e.g., TCP, HDLC), what diagram provides the highest examiner credibility?", ["A decorative cloud icon", "A formal Sequence Ladder Diagram showing sender/receiver timelines, frame transfers, and ACK acknowledgments", "A photo of an Ethernet cable", "A computer motherboard schematic"], "B", "Sequence ladder diagrams (Sender | Receiver timelines) clearly depict frame exchanges, timeouts, and ACKs, proving protocol comprehension."),
            ("What is the primary factor that differentiates a 90%+ top-bracket university score from an average 65% score in CSJM University BCA papers?", ["Writing handwriting that is difficult to decipher", "Consistent 5-part structure: Formal Definition, Architectural Diagram, Core Principles, Comparative Table, and Summary", "Writing only bullet points with zero explanations", "Submitting the answer book 1 hour early"], "B", "The top scoring bracket follows structured technical presentation that fulfills university rubrics comprehensively.")
        ])
    }
    
    if day in catalog:
        code, subj, topic, q_list = catalog[day]
        mcqs = []
        for i, q in enumerate(q_list, 1):
            mcqs.append({
                "id": f"ACAD-{day:02d}-{i:02d}",
                "question": q[0],
                "options": q[1],
                "correct_answer": q[2],
                "explanation": q[3]
            })
        return mcqs
    return []
