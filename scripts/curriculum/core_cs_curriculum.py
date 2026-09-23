#!/usr/bin/env python3
"""
scripts/curriculum/core_cs_curriculum.py
Complete 30-Day Core Computer Science Curriculum for Placement & Technical Interviews.

Subjects covered across 30 days:
- Days 1-7: Operating Systems (Process, Threads, CPU Scheduling, Synchronization, Deadlocks, Memory, Virtual Memory)
- Days 8-14: Database Management Systems (Architecture, Relational Algebra & Joins, Normalization, ACID, Concurrency & Isolation, Locking & 2PL, Indexing B/B+ Trees)
- Days 15-21: Computer Networks (OSI vs TCP/IP, Data Link & Error Control, MAC/CSMA, IPv4 Subnetting, Routing OSPF/BGP, TCP 3-Way Handshake, TCP Congestion Control)
- Days 22-26: Python Internals & Advanced Programming (Memory & GC, GIL vs Multiprocessing/AsyncIO, Decorators & Generators, OOP & MRO, REST & ASGI Architecture)
- Days 27-30: System Design Fundamentals (Scalability & Load Balancing, Caching Strategies & Redis, DB Scaling & CAP Theorem, Rate Limiter & URL Shortener Design)

Every day provides:
- subject
- topic
- concept_lesson (thorough, technical, and concrete)
- key_definitions (list of dicts)
- interview_questions (5 high-yield placement interview Q&A)
- mcqs (5 multiple choice questions with answers and explanations)
"""

def get_core_cs_for_day(day: int) -> dict:
    modules = {
        # --- DAYS 1-7: OPERATING SYSTEMS ---
        1: {
            "subject": "Operating Systems",
            "topic": "Processes, Threads, Context Switching & Process Control Blocks",
            "concept_lesson": (
                "An operating system process is an executing instance of a program in active memory. "
                "A process comprises five distinct address space segments: the Text section (compiled machine instructions), "
                "Data section (initialized global and static variables), BSS section (uninitialized globals), "
                "Heap (dynamically allocated memory via malloc/new, growing upward), and Stack (local variables, function call frames, "
                "return pointers, growing downward towards the heap).\n\n"
                "A Thread is the smallest unit of execution scheduled by the OS, often described as a lightweight process (LWP). "
                "Threads within the same process share the Text, Data, BSS, Heap, and open file descriptors, but each thread maintains "
                "its own private Program Counter (PC), CPU registers, and independent Call Stack.\n\n"
                "The Process Control Block (PCB) is the primary OS kernel data structure representing a process. It contains: "
                "PID (Process ID), Process State (New, Ready, Running, Waiting, Terminated), Program Counter, CPU registers, "
                "CPU scheduling priority, memory-management information (page table pointers), accounting data, and I/O status info.\n\n"
                "Context Switching is the mechanism of saving the state of the currently executing process/thread into its PCB/TCB "
                "and loading the state of another ready process into CPU registers. Because the CPU cannot do useful user-space computation "
                "during context switching, it represents pure computational overhead, heavily influenced by hardware cache misses and TLB flushes."
            ),
            "key_definitions": [
                {"term": "Process", "definition": "A program in execution, with its own independent address space (Stack, Heap, Data, Text)."},
                {"term": "Thread", "definition": "A lightweight unit of CPU utilization within a process, sharing code, data, and resources but possessing a private stack and registers."},
                {"term": "Context Switch", "definition": "The kernel switching CPU control from one process/thread to another by saving and restoring register states and memory maps."}
            ],
            "interview_questions": [
                {
                    "q": "What is the key difference between a process and a thread in terms of memory sharing?",
                    "a": "Processes run in isolated virtual address spaces; memory cannot be shared directly without explicit IPC (Inter-Process Communication like pipes, shared memory, or sockets). Threads belonging to the same process share the same virtual address space—including heap, global variables, and open files—which allows ultra-fast data sharing but introduces race conditions requiring synchronization."
                },
                {
                    "q": "What happens in the OS during a context switch?",
                    "a": "The CPU switches to kernel mode via an interrupt or system call. The kernel saves the program counter, registers, and stack pointer of the currently running process into its PCB. The scheduler selects a new process from the Ready queue. The kernel restores the new process's saved CPU registers and page table pointers (flushing or tagging TLB entries), switches the CPU back to user mode, and branches to the new program counter."
                },
                {
                    "q": "Why is thread switching faster than process switching?",
                    "a": "Thread switching does not require changing the virtual memory address space or flushing the Translation Lookaside Buffer (TLB). Only the thread's CPU registers and stack pointer are swapped, avoiding costly cache invalidations and memory mapping recalculations."
                },
                {
                    "q": "What is a Zombie process vs an Orphan process?",
                    "a": "A Zombie process has completed execution (terminated) but still holds an entry in the process table because its parent has not yet read its exit status via wait() or waitpid(). An Orphan process is one whose parent terminated before the child; the kernel automatically re-parents orphans to process 1 (init or systemd), which regularly invokes wait() to reap them."
                },
                {
                    "q": "Explain User-level Threads (ULT) vs Kernel-level Threads (KLT).",
                    "a": "User-level threads are managed by user-space runtime libraries without kernel awareness; switching requires no kernel context switch, but if one ULT makes a blocking system call, the entire process blocks. Kernel-level threads are scheduled directly by the OS kernel; blocking one thread allows other threads of the process to continue running, though thread creation and switching incur kernel mode-switch overhead."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-01-01",
                    "question": "Which of the following resources is NOT shared between threads belonging to the same process?",
                    "options": ["Heap memory", "Open file descriptors", "CPU registers and Call Stack", "Global variables in Data section"],
                    "correct_answer": "C",
                    "explanation": "Threads share text, data, and heap segments along with OS resources, but maintain private CPU registers and call stacks."
                },
                {
                    "id": "CS-01-02",
                    "question": "What is the primary cause of CPU overhead during a process context switch?",
                    "options": ["Re-compiling source code", "Saving/restoring PCB registers, TLB cache invalidation, and memory map reloads", "Disk head movement", "Allocating new socket connections"],
                    "correct_answer": "B",
                    "explanation": "Context switching requires saving state to PCB, switching page tables, and invalidating CPU/TLB caches."
                },
                {
                    "id": "CS-01-03",
                    "question": "A process that has finished execution but still occupies an entry in the process table is known as a:",
                    "options": ["Daemon process", "Orphan process", "Zombie process", "Background process"],
                    "correct_answer": "C",
                    "explanation": "A zombie process remains until its parent executes wait() to retrieve its termination status."
                },
                {
                    "id": "CS-01-04",
                    "question": "When a parent process terminates before its child process in Linux/Unix, the child process becomes:",
                    "options": ["Terminated immediately", "A zombie process", "Re-parented to init/systemd (PID 1)", "Suspended indefinitely"],
                    "correct_answer": "C",
                    "explanation": "Orphaned processes are adopted by init/systemd (PID 1), which reaps their termination status."
                },
                {
                    "id": "CS-01-05",
                    "question": "In which memory segment are dynamically allocated variables (via malloc in C or new in C++) stored?",
                    "options": ["Stack", "Data section", "BSS segment", "Heap"],
                    "correct_answer": "D",
                    "explanation": "Dynamic runtime memory allocations reside on the Heap, which grows upward toward higher addresses."
                }
            ]
        },

        2: {
            "subject": "Operating Systems",
            "topic": "CPU Scheduling Algorithms (FCFS, SJF, SRTF, Round Robin & Priority)",
            "concept_lesson": (
                "CPU Scheduling is the process by which the short-term scheduler (CPU scheduler) allocates the CPU core to one "
                "of the ready processes. Schedulers operate in two modes: Non-preemptive (once allocated, the process retains CPU until "
                "it terminates or voluntarily yields for I/O) and Preemptive (the kernel can interrupt a running process when a higher-priority "
                "process arrives or its time slice expires).\n\n"
                "Key Algorithms:\n"
                "1. First-Come, First-Served (FCFS): Non-preemptive. Suffers from the Convoy Effect, where small I/O-bound processes "
                "queue behind a CPU-heavy process, drastically increasing average waiting time.\n"
                "2. Shortest Job First (SJF): Non-preemptive. Mathematically optimal in minimizing average waiting time, but impossible to "
                "implement perfectly in practice because future CPU burst lengths are unknown (estimated using exponential smoothing).\n"
                "3. Shortest Remaining Time First (SRTF): Preemptive version of SJF. Preempts current process if an incoming process has "
                "a shorter remaining burst. Can lead to starvation of long CPU bursts.\n"
                "4. Round Robin (RR): Preemptive, designed for time-sharing. Each process gets a fixed time quantum 'q'. If q is too small, "
                "context switch overhead dominates; if q is too large, RR degrades to FCFS.\n"
                "5. Priority Scheduling: Can be preemptive or non-preemptive. Can cause indefinite blocking (starvation), solved by Aging "
                "(gradually increasing the priority of processes that wait in the ready queue for long periods)."
            ),
            "key_definitions": [
                {"term": "Turnaround Time", "definition": "Total time interval from process submission to completion: Completion Time - Arrival Time."},
                {"term": "Waiting Time", "definition": "Total duration spent waiting in the Ready queue: Turnaround Time - Burst Time."},
                {"term": "Convoy Effect", "definition": "A phenomenon in FCFS where numerous short processes wait behind one long CPU-bound process."}
            ],
            "interview_questions": [
                {
                    "q": "What is the Convoy Effect in CPU scheduling, and which algorithm causes it?",
                    "a": "The Convoy Effect occurs in FCFS scheduling when a CPU-intensive process holds the processor for a long duration, forcing all shorter, I/O-bound processes to wait idle in the ready queue. This severely degrades CPU and device utilization and inflates average waiting times."
                },
                {
                    "q": "Why is Shortest Job First (SJF) considered optimal, and why is it hard to implement in real OS kernels?",
                    "a": "SJF is provably optimal because scheduling the shortest job first minimizes the waiting time for all subsequent jobs in the queue. However, an OS cannot know the exact length of a process's next CPU burst in advance. Kernels approximate it using exponential averaging of historical bursts (tau_{n+1} = alpha * t_n + (1 - alpha) * tau_n)."
                },
                {
                    "q": "How does the choice of Time Quantum impact Round Robin performance?",
                    "a": "If the time quantum is extremely small (e.g., 1 microsecond), the CPU spends a disproportionate amount of time on context switches rather than executing user code. If the quantum is extremely large, Round Robin degenerates into FCFS, causing poor interactive response times. Rule of thumb: 80% of CPU bursts should be shorter than the time quantum."
                },
                {
                    "q": "What is Starvation in Priority Scheduling, and how is it resolved?",
                    "a": "Starvation (indefinite blocking) occurs when low-priority processes never get CPU time because a steady stream of higher-priority processes keeps arriving. It is resolved using Aging: dynamically incrementing a waiting process's priority over elapsed time until it becomes high enough to execute."
                },
                {
                    "q": "Explain the difference between Preemptive and Non-Preemptive scheduling.",
                    "a": "In non-preemptive scheduling, once a process is in the running state, it holds the CPU until it terminates or blocks for I/O. In preemptive scheduling, the OS can forcibly interrupt and move a running process back to the ready state when a higher-priority process arrives, a timer interrupt fires, or a higher-priority I/O event completes."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-02-01",
                    "question": "Which CPU scheduling algorithm provides the theoretical minimum average waiting time for a given set of processes?",
                    "options": ["First-Come, First-Served", "Round Robin", "Shortest Job First", "Priority Scheduling"],
                    "correct_answer": "C",
                    "explanation": "SJF is provably optimal for minimizing average waiting time by executing shorter bursts first."
                },
                {
                    "id": "CS-02-02",
                    "question": "The technique of gradually increasing the priority of processes that wait in the system for a long time is called:",
                    "options": ["Paging", "Aging", "Throttling", "Belady's adjustment"],
                    "correct_answer": "B",
                    "explanation": "Aging prevents starvation in priority queues by systematically boosting waiting processes."
                },
                {
                    "id": "CS-02-03",
                    "question": "If the time quantum of a Round Robin scheduler is extremely large, it behaves identically to:",
                    "options": ["SJF", "SRTF", "FCFS", "Multilevel Feedback Queue"],
                    "correct_answer": "C",
                    "explanation": "When quantum exceeds the longest burst, every process completes in arrival order without preemption, mimicking FCFS."
                },
                {
                    "id": "CS-02-04",
                    "question": "Turnaround time of a process is calculated as:",
                    "options": ["Waiting Time - Burst Time", "Completion Time - Arrival Time", "Completion Time - Burst Time", "Arrival Time + Burst Time"],
                    "correct_answer": "B",
                    "explanation": "Turnaround time represents total elapsed lifetime: Completion Time minus Arrival Time."
                },
                {
                    "id": "CS-02-05",
                    "question": "Which algorithm is the preemptive variant of Shortest Job First?",
                    "options": ["Round Robin", "Priority Inversion", "Shortest Remaining Time First (SRTF)", "Multilevel Queue"],
                    "correct_answer": "C",
                    "explanation": "SRTF preempts the CPU if a newly arrived process has a remaining burst shorter than current execution."
                }
            ]
        },

        3: {
            "subject": "Operating Systems",
            "topic": "Process Synchronization, Race Conditions, Critical Section & Semaphores",
            "concept_lesson": (
                "When concurrent processes or threads access shared resources (memory variables, files, tables), non-atomic concurrent "
                "operations lead to a Race Condition—a state where the final outcome depends on the arbitrary order of thread scheduling.\n\n"
                "The Critical Section Problem requires any valid synchronization solution to satisfy three strict criteria:\n"
                "1. Mutual Exclusion: If process P is executing in its critical section, no other process can execute in theirs.\n"
                "2. Progress: If no process is executing in its critical section and some wish to enter, selection of the next process cannot "
                "be postponed indefinitely.\n"
                "3. Bounded Waiting: A bound must exist on the number of times other processes are allowed to enter their critical sections "
                "after a process has made a request to enter, preventing starvation.\n\n"
                "Synchronization Primitives:\n"
                "- Mutex (Mutual Exclusion Lock): A binary locking mechanism with ownership semantics (only the thread that acquired the mutex can release it).\n"
                "- Semaphore: An integer variable accessed only through two standard atomic operations: wait() (also called P) and signal() (also called V).\n"
                "  - wait(S): while (S <= 0) do wait; S--;\n"
                "  - signal(S): S++;\n"
                "- Counting Semaphore: Controls access to a finite pool of identical resources, initialized to available instance count N.\n"
                "- Binary Semaphore: Value restricted between 0 and 1; functions like a mutex but lacks ownership constraints (any thread can signal it)."
            ),
            "key_definitions": [
                {"term": "Critical Section", "definition": "A code segment accessing shared resources that must not be concurrently executed by multiple threads."},
                {"term": "Race Condition", "definition": "An undesirable situation where the system's output depends on the non-deterministic sequence or timing of concurrent execution."},
                {"term": "Semaphore", "definition": "A protected integer synchronization variable modified exclusively by atomic wait() and signal() operations."}
            ],
            "interview_questions": [
                {
                    "q": "What is the difference between a Mutex and a Binary Semaphore?",
                    "a": "A Mutex has ownership: the thread that locks the mutex must be the exact same thread that unlocks it. A Semaphore has no concept of ownership: any thread can invoke signal() to increment the count, making semaphores suitable for signaling events between threads (e.g., producer signaling consumer) whereas mutexes are designed strictly for mutual exclusion."
                },
                {
                    "q": "What three conditions must any valid solution to the Critical Section problem satisfy?",
                    "a": "1. Mutual Exclusion: At most one process can execute in the critical section at any instant. 2. Progress: Only processes waiting to enter can participate in deciding who enters next, and this choice cannot be indefinitely delayed. 3. Bounded Waiting: There is a strict limit on the number of times other processes can enter before a waiting process's request is granted."
                },
                {
                    "q": "What is busy waiting (Spinlock), and when is a spinlock preferred over a sleep lock?",
                    "a": "Busy waiting means a thread loops continuously checking a condition (e.g., while (flag == true);), consuming CPU cycles without productive work. A spinlock is preferred in multi-core systems when the expected lock holding time is extremely short, because spinning avoids the expensive overhead of context switching the thread into sleep and waking it later."
                },
                {
                    "q": "What are the atomic hardware instructions used to implement locks?",
                    "a": "Modern CPUs provide atomic instructions like Test-and-Set and Compare-And-Swap (CAS). These instructions execute uninterrupted at the hardware bus level, allowing software to test and update a memory location in a single clock cycle without race conditions."
                },
                {
                    "q": "What is Priority Inversion, and how does Priority Inheritance solve it?",
                    "a": "Priority Inversion occurs when a high-priority task is blocked waiting for a lock held by a low-priority task, and a medium-priority task preempts the low-priority task, indirectly delaying the high-priority task indefinitely. Priority Inheritance solves this by temporarily promoting the priority of the low-priority lock holder to match that of the highest-priority waiting task until the lock is released."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-03-01",
                    "question": "Which of the following is NOT a mandatory condition for solving the Critical Section problem?",
                    "options": ["Mutual Exclusion", "Progress", "Preemptive Priority Assignment", "Bounded Waiting"],
                    "correct_answer": "C",
                    "explanation": "The three requirements are Mutual Exclusion, Progress, and Bounded Waiting."
                },
                {
                    "id": "CS-03-02",
                    "question": "A counting semaphore initialized to 7 has 4 wait() operations and 2 signal() operations applied. Its final value is:",
                    "options": ["3", "5", "9", "1"],
                    "correct_answer": "B",
                    "explanation": "Initial = 7. 4 wait() decrement by 4 (7 - 4 = 3). 2 signal() increment by 2 (3 + 2 = 5)."
                },
                {
                    "id": "CS-03-03",
                    "question": "A major difference between a Mutex and a Semaphore is:",
                    "options": ["Semaphores cannot be used in multithreading", "A Mutex can only be unlocked by the thread that acquired it", "Mutex values can be negative", "Semaphores cannot enforce mutual exclusion"],
                    "correct_answer": "B",
                    "explanation": "Mutexes enforce strict thread ownership; semaphores can be signaled by any thread."
                },
                {
                    "id": "CS-03-04",
                    "question": "A situation where a high-priority thread is indirectly delayed by a medium-priority thread preempting a low-priority lock holder is called:",
                    "options": ["Deadlock", "Priority Inversion", "Convoy Effect", "Thrashing"],
                    "correct_answer": "B",
                    "explanation": "Priority Inversion occurs when a medium-priority process blocks a lower-priority process holding a resource needed by a high-priority process."
                },
                {
                    "id": "CS-03-05",
                    "question": "In a spinlock, a thread waiting for a resource:",
                    "options": ["Transitions to the blocked/sleep state", "Continuously loops in user space checking the lock", "Releases its virtual address space", "Is re-parented to init"],
                    "correct_answer": "B",
                    "explanation": "Spinlocks use busy-waiting loops, holding the CPU while polling the lock condition."
                }
            ]
        },

        4: {
            "subject": "Operating Systems",
            "topic": "Classical Synchronization Problems (Producer-Consumer, Dining Philosophers, Readers-Writers)",
            "concept_lesson": (
                "Classical synchronization problems serve as universal test cases for evaluating concurrency paradigms.\n\n"
                "1. Producer-Consumer Problem (Bounded Buffer):\n"
                "Producers generate items and append to a fixed-size buffer (size N); Consumers remove items. "
                "Three synchronization primitives are needed:\n"
                "- `mutex = 1`: Enforces mutual exclusion on buffer insert/delete.\n"
                "- `empty = N`: Counting semaphore tracking available empty slots. Producer calls `wait(empty)`.\n"
                "- `full = 0`: Counting semaphore tracking populated slots. Consumer calls `wait(full)`.\n\n"
                "2. Readers-Writers Problem:\n"
                "Multiple readers can concurrently read data without conflict, but a writer requires exclusive access. "
                "First Readers-Writers variation prioritizes readers, risking writer starvation; Second variation prioritizes "
                "writers to ensure write updates are not starved by a continuous stream of readers.\n\n"
                "3. Dining Philosophers Problem:\n"
                "Five philosophers sit around a circular table with 5 chopsticks; each alternates between thinking and eating. "
                "To eat, a philosopher requires both left and right chopsticks. If every philosopher picks up their left chopstick "
                "simultaneously, a circular wait occurs, resulting in total Deadlock. Solutions include: asymmetric pickup (odd philosophers "
                "pick left first, even pick right first), limiting table capacity to 4, or using an atomic monitor condition."
            ),
            "key_definitions": [
                {"term": "Bounded Buffer", "definition": "A shared circular queue of fixed capacity accessible by concurrent producer and consumer threads."},
                {"term": "Reader-Writer Lock", "definition": "A concurrency lock allowing shared access for multiple readers or exclusive access for one writer."},
                {"term": "Asymmetric Allocation", "definition": "Breaking symmetry in resource acquisition order to eliminate circular wait conditions."}
            ],
            "interview_questions": [
                {
                    "q": "How does the Producer-Consumer problem avoid race conditions and deadlocks using semaphores?",
                    "a": "It uses three semaphores: a binary semaphore 'mutex' (1) to protect buffer modifications, a counting semaphore 'empty' (initialized to buffer capacity N), and a counting semaphore 'full' (initialized to 0). The producer does wait(empty), wait(mutex), writes, signal(mutex), signal(full). The consumer does wait(full), wait(mutex), reads, signal(mutex), signal(empty). Swapping wait(empty) and wait(mutex) would cause a deadlock if the buffer is full."
                },
                {
                    "q": "Why does the naive Dining Philosophers implementation deadlock, and how is it solved?",
                    "a": "Deadlock occurs because if all 5 philosophers get hungry at the same moment and pick up their left chopstick, all chopsticks are taken, and every philosopher blocks waiting for the right chopstick (Circular Wait). Solutions include: 1) Asymmetric strategy: odd-numbered philosophers pick left then right, even pick right then left; 2) Allow at most 4 philosophers to sit at the table simultaneously; 3) Pick both chopsticks atomically inside a critical section."
                },
                {
                    "q": "Explain the difference between Reader-Preference and Writer-Preference in the Readers-Writers problem.",
                    "a": "In Reader-Preference, if at least one reader is actively reading, incoming readers are immediately granted access, which can starve waiting writers indefinitely. In Writer-Preference, once a writer signals its intention to write, no new readers are allowed to start reading; existing readers finish, and the writer acquires the lock, preventing writer starvation."
                },
                {
                    "q": "What is the consequence of reversing wait(empty) and wait(mutex) in Producer-Consumer?",
                    "a": "If the producer executes wait(mutex) first when the buffer is full (empty = 0), it locks the mutex and then blocks on wait(empty). The consumer needs to acquire the mutex to consume an item and signal empty, but cannot do so because the producer holds the mutex. Both threads block forever in a deadlock."
                },
                {
                    "q": "How can Java or Python Monitors simplify synchronization compared to semaphores?",
                    "a": "Monitors encapsulate shared state, locks, and condition variables within an object class. Only one thread can execute an object's synchronized method at a time. Programmers do not need to manually pair wait() and signal() across multiple semaphores, dramatically reducing human locking bugs like forgotten unlocks or out-of-order acquisitions."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-04-01",
                    "question": "In the Bounded Buffer problem of size N, what are the initial values of semaphores empty, full, and mutex?",
                    "options": ["empty = 0, full = N, mutex = 0", "empty = N, full = 0, mutex = 1", "empty = 1, full = 1, mutex = N", "empty = N, full = N, mutex = 1"],
                    "correct_answer": "B",
                    "explanation": "Initially all N slots are empty (empty = N), 0 slots are filled (full = 0), and mutex is unlocked (1)."
                },
                {
                    "id": "CS-04-02",
                    "question": "If all philosophers pick up their left chopstick simultaneously in Dining Philosophers, the system experiences:",
                    "options": ["Thrashing", "Deadlock", "High throughput", "Cache invalidation"],
                    "correct_answer": "B",
                    "explanation": "All philosophers hold one chopstick and wait for the other, forming an unbreakable circular wait deadlock."
                },
                {
                    "id": "CS-04-03",
                    "question": "Which Readers-Writers solution policy risks writer starvation?",
                    "options": ["Writer-preference", "Fair FIFO queue", "Reader-preference", "Strict alternating"],
                    "correct_answer": "C",
                    "explanation": "In reader-preference, as long as readers keep arriving, writers are indefinitely postponed."
                },
                {
                    "id": "CS-04-04",
                    "question": "In the Bounded Buffer solution, reversing wait(mutex) and wait(empty) in the producer causes:",
                    "options": ["Faster throughput", "Buffer overflow", "Potential deadlock when buffer is full", "Data corruption"],
                    "correct_answer": "C",
                    "explanation": "Holding mutex while blocked on empty prevents the consumer from entering to free up buffer space, causing deadlock."
                },
                {
                    "id": "CS-04-05",
                    "question": "An asymmetric solution to the Dining Philosophers problem specifies that:",
                    "options": ["Philosophers eat with only one chopstick", "Odd philosophers pick left first, even philosophers pick right first", "All philosophers pick right first", "Philosophers never release chopsticks"],
                    "correct_answer": "B",
                    "explanation": "Alternating the pickup order breaks the circular wait condition necessary for deadlock."
                }
            ]
        },

        5: {
            "subject": "Operating Systems",
            "topic": "Deadlocks: 4 Coffman Conditions, Resource Allocation Graphs & Banker's Algorithm",
            "concept_lesson": (
                "A Deadlock is a state in which a set of concurrent processes are blocked because each process holds resources "
                "and waits for other resources held by other processes in the same set.\n\n"
                "The 4 Coffman Conditions (All must hold simultaneously for a deadlock to occur):\n"
                "1. Mutual Exclusion: At least one resource must be held in a non-shareable mode.\n"
                "2. Hold and Wait: A process must be holding at least one resource and waiting to acquire additional resources held by others.\n"
                "3. No Preemption: Resources cannot be forcibly confiscated from a process; they can only be released voluntarily.\n"
                "4. Circular Wait: A closed chain of processes exists {P0, P1, ..., Pn} such that P0 waits for a resource held by P1, "
                "P1 waits for P2, and Pn waits for P0.\n\n"
                "Handling Strategies:\n"
                "- Deadlock Prevention: Invalidate at least one Coffman condition (e.g., impose global linear resource ordering to eliminate Circular Wait).\n"
                "- Deadlock Avoidance: System evaluates dynamic state before granting allocations to ensure the system remains in a 'Safe State'. "
                "The Banker's Algorithm uses vectors (Available, Max, Allocation, Need = Max - Allocation) to test whether there exists a safe sequence "
                "where all processes can finish.\n"
                "- Deadlock Detection & Recovery: Allow deadlocks to occur, run detection algorithms (wait-for graphs), and recover via process termination "
                "or resource preemption.\n"
                "- Ostrich Algorithm: Ignore the problem entirely (used by most general-purpose OS kernels due to the high cost of continuous prevention)."
            ),
            "key_definitions": [
                {"term": "Safe State", "definition": "A system state where there exists at least one execution sequence of all processes that avoids deadlock."},
                {"term": "Banker's Algorithm", "definition": "A deadlock avoidance algorithm that tests for safety by simulating the allocation of predetermined maximum resources."},
                {"term": "Resource Allocation Graph (RAG)", "definition": "A directed graph with process nodes and resource nodes showing request and assignment edges."}
            ],
            "interview_questions": [
                {
                    "q": "What are the four necessary and sufficient conditions for a deadlock to occur?",
                    "a": "The Coffman conditions: 1. Mutual Exclusion (resources cannot be shared), 2. Hold and Wait (processes retain allocated resources while requesting new ones), 3. No Preemption (resources cannot be forcibly revoked), and 4. Circular Wait (a circular chain of processes each waiting for a resource held by the next)."
                },
                {
                    "q": "How does the Banker's Algorithm determine if a state is safe?",
                    "a": "It calculates Need = Max - Allocation for each process. It simulates execution using Work = Available vector. It finds a process Pi whose Need <= Work. If found, it assumes Pi completes, returns its resources (Work = Work + Allocation_i), marks Pi finished, and repeats. If all processes can be marked finished, a 'safe sequence' exists and the state is safe; otherwise, it is unsafe."
                },
                {
                    "q": "Is an unsafe state always a deadlocked state?",
                    "a": "No. An unsafe state is not necessarily deadlocked; it is simply a state from which the OS cannot guarantee avoiding a deadlock if all processes simultaneously demand their maximum resource limits. If processes do not request their maximum claims, execution may still complete without deadlock."
                },
                {
                    "q": "How can Circular Wait be prevented in practice?",
                    "a": "By imposing a strict global total ordering on all resource types (e.g., Lock 1 has ID 10, Lock 2 has ID 20). Processes must request resources strictly in monotonically increasing order of resource IDs. If a process holds Lock 20, it is forbidden from requesting Lock 10, mathematically preventing circular dependency cycles."
                },
                {
                    "q": "What is the difference between a Deadlock and a Livelock?",
                    "a": "In a deadlock, processes are in a blocked (sleeping) state, waiting for events that will never occur, consuming zero CPU cycles. In a livelock, processes actively change their internal states in response to each other (e.g., repeatedly yielding and retrying a lock), remaining busy and consuming 100% CPU, but making zero forward progress."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-05-01",
                    "question": "Which of the following is NOT one of the 4 Coffman conditions for deadlock?",
                    "options": ["Mutual Exclusion", "Hold and Wait", "Process Aging", "Circular Wait"],
                    "correct_answer": "C",
                    "explanation": "The 4 conditions are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait."
                },
                {
                    "id": "CS-05-02",
                    "question": "If a Resource Allocation Graph contains a cycle and every resource type has exactly one single instance, then:",
                    "options": ["A deadlock definitely exists", "A deadlock may or may not exist", "The system is guaranteed safe", "The CPU enters thrashing"],
                    "correct_answer": "A",
                    "explanation": "With single-instance resources, a cycle in the RAG is both necessary and sufficient for deadlock."
                },
                {
                    "id": "CS-05-03",
                    "question": "The Banker's Algorithm is primarily used for:",
                    "options": ["Deadlock Prevention", "Deadlock Avoidance", "Deadlock Detection", "Memory Compaction"],
                    "correct_answer": "B",
                    "explanation": "Banker's Algorithm is a dynamic deadlock avoidance technique that checks for safe execution sequences."
                },
                {
                    "id": "CS-05-04",
                    "question": "In a system with Need matrix, how is Need calculated in Banker's Algorithm?",
                    "options": ["Allocation - Available", "Max - Allocation", "Max + Available", "Allocation - Max"],
                    "correct_answer": "B",
                    "explanation": "Need represents remaining resources a process may claim: Need = Max - Allocation."
                },
                {
                    "id": "CS-05-05",
                    "question": "Assigning global numerical IDs to resources and enforcing acquisition in ascending order eliminates which condition?",
                    "options": ["Mutual Exclusion", "Hold and Wait", "No Preemption", "Circular Wait"],
                    "correct_answer": "D",
                    "explanation": "Strict resource ordering prevents cycles from forming, eliminating Circular Wait."
                }
            ]
        },

        6: {
            "subject": "Operating Systems",
            "topic": "Memory Management: Contiguous Allocation, Paging, Segmentation & TLB",
            "concept_lesson": (
                "Memory management bridges logical process address space to physical hardware RAM.\n\n"
                "Contiguous Allocation & Fragmentation:\n"
                "- Internal Fragmentation: Allocated memory block is larger than requested memory; unused memory inside the partition is wasted.\n"
                "- External Fragmentation: Total free memory space exists to satisfy a request, but it is split into non-contiguous fragments. "
                "Resolved via Compaction (costly memory copying) or Non-contiguous Paging.\n\n"
                "Paging Architecture:\n"
                "Physical memory is broken into fixed-size blocks called Frames. Logical address space is broken into blocks of identical size "
                "called Pages (commonly 4KB). The CPU generates logical addresses split into: Page Number (p) and Page Offset (d).\n"
                "The Page Table maps page number p to frame number f. Physical address = (f * page_size) + d. Paging completely eliminates "
                "external fragmentation, but introduces slight internal fragmentation on the final page of a process.\n\n"
                "Translation Lookaside Buffer (TLB):\n"
                "Accessing a page table in RAM requires two memory accesses per data lookup (one for page table entry, one for physical data). "
                "The TLB is an ultra-fast hardware associative associative cache inside the MMU (Memory Management Unit). If page p is found "
                "in TLB (TLB Hit), frame f is retrieved in ~1 nanosecond. Effective Memory Access Time (EMAT) = Hit_Rate * (TLB_time + RAM_time) + "
                "(1 - Hit_Rate) * (TLB_time + 2 * RAM_time).\n\n"
                "Segmentation:\n"
                "Divides memory into variable-sized logical segments reflecting programmer view (Code, Stack, Heap, Functions). Each entry in the "
                "Segment Table contains Base (physical starting address) and Limit (segment length), checking against boundary violations."
            ),
            "key_definitions": [
                {"term": "Page vs Frame", "definition": "A Page is a fixed-size block of logical address space; a Frame is an identically-sized block of physical RAM."},
                {"term": "TLB (Translation Lookaside Buffer)", "definition": "A high-speed hardware cache in the MMU storing recent logical-to-physical address translations."},
                {"term": "Internal Fragmentation", "definition": "Wasted space within an allocated memory block because the allocated unit exceeds process demand."}
            ],
            "interview_questions": [
                {
                    "q": "Explain the difference between Internal and External Fragmentation.",
                    "a": "Internal fragmentation occurs when memory is allocated in fixed-size blocks (e.g., 4KB pages) and a process requests less than the block size (e.g., 1KB), leaving 3KB unused inside the block. External fragmentation occurs in variable-partition systems when total free memory is sufficient to satisfy a request, but the space is scattered into small non-contiguous holes across RAM, preventing a large process from fitting."
                },
                {
                    "q": "How does Paging eliminate External Fragmentation?",
                    "a": "In paging, any logical page of a process can be placed into any available physical frame anywhere in RAM, regardless of whether the frames are physically contiguous. Because no contiguous chunk of physical memory is required, external fragmentation cannot occur."
                },
                {
                    "q": "What is the Translation Lookaside Buffer (TLB), and what is a TLB Miss?",
                    "a": "The TLB is an associative hardware cache inside the Memory Management Unit (MMU) that stores recent page-to-frame translations. On a memory reference, the MMU checks the TLB. If present (TLB hit), physical frame address is obtained immediately. On a TLB miss, the MMU must read the multi-level page table from RAM (adding memory latency), load the translation into the TLB, and then perform the data lookup."
                },
                {
                    "q": "Given a 32-bit logical address with 4KB page size, calculate the number of bits for Page Number and Offset.",
                    "a": "Page size = 4KB = 2^12 bytes. Therefore, 12 bits are required for the Page Offset (d). The remaining 32 - 12 = 20 bits specify the Page Number (p). A process can thus have 2^20 pages (1,048,576 pages)."
                },
                {
                    "q": "What is Multi-level Paging, and why is it necessary for 64-bit architectures?",
                    "a": "A linear page table for a 32-bit system with 2^20 entries at 4 bytes each takes 4MB of contiguous RAM per process. In 64-bit systems, a single linear page table would require petabytes of storage. Multi-level paging breaks the page table itself into pages, allowing non-contiguous allocation and letting the OS allocate page tables only for virtual address regions that are actually in use, avoiding massive memory waste."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-06-01",
                    "question": "In a paging memory system, which type of fragmentation can still occur?",
                    "options": ["External fragmentation only", "Internal fragmentation only", "Both internal and external", "Neither type"],
                    "correct_answer": "B",
                    "explanation": "Paging eliminates external fragmentation, but the last allocated page may not be completely filled, causing internal fragmentation."
                },
                {
                    "id": "CS-06-02",
                    "question": "A system uses 4KB pages. How many bits are needed for the page offset?",
                    "options": ["10 bits", "12 bits", "16 bits", "20 bits"],
                    "correct_answer": "B",
                    "explanation": "4 KB = 4096 bytes = 2^12 bytes, so 12 bits are needed for offset."
                },
                {
                    "id": "CS-06-03",
                    "question": "The hardware component that maps virtual addresses to physical addresses at runtime is the:",
                    "options": ["ALU", "MMU (Memory Management Unit)", "DMA Controller", "Interrupt Handler"],
                    "correct_answer": "B",
                    "explanation": "The MMU contains the hardware logic and TLB to translate virtual memory addresses to physical RAM."
                },
                {
                    "id": "CS-06-04",
                    "question": "If TLB access takes 10ns and RAM access takes 100ns, what is access time on a TLB hit?",
                    "options": ["10ns", "100ns", "110ns", "210ns"],
                    "correct_answer": "C",
                    "explanation": "On a TLB hit, the MMU accesses the TLB (10ns) then fetches data from RAM (100ns), totaling 110ns."
                },
                {
                    "id": "CS-06-05",
                    "question": "In Segmentation, a logical address consists of:",
                    "options": ["Page number and frame offset", "Segment number and offset", "Base register and limit register", "PID and socket ID"],
                    "correct_answer": "B",
                    "explanation": "Segmentation addresses specify a segment identifier and offset within that segment."
                }
            ]
        },

        7: {
            "subject": "Operating Systems",
            "topic": "Virtual Memory: Demand Paging, Page Faults, Page Replacement & Thrashing",
            "concept_lesson": (
                "Virtual memory decouples the programmer's logical address space from physical RAM capacity, allowing execution "
                "of processes whose total memory footprint exceeds physical RAM.\n\n"
                "Demand Paging & Page Fault Handling:\n"
                "Pages are loaded into RAM only when referenced during execution. Each page table entry includes a Valid/Invalid bit "
                "(Valid: page is in RAM; Invalid: page is on swap disk or unallocated). When the CPU references an invalid page, a "
                "hardware trap called a Page Fault occurs:\n"
                "1. Trap to kernel mode.\n"
                "2. Check if address is valid in process virtual memory.\n"
                "3. Find a free frame in physical RAM.\n"
                "4. Issue disk I/O to read the missing page from swap storage into the frame.\n"
                "5. Update page table entry (valid bit = 1, frame number = f).\n"
                "6. Restart the interrupted machine instruction.\n\n"
                "Page Replacement Algorithms:\n"
                "- FIFO (First-In, First-Out): Replaces oldest page. Suffers from Belady's Anomaly: allocating MORE physical frames can "
                "paradoxically increase the number of page faults.\n"
                "- Optimal Page Replacement (OPT/MIN): Replaces the page that will not be used for the longest period in the future. "
                "Unimplementable in practice; used as a theoretical benchmark.\n"
                "- LRU (Least Recently Used): Replaces the page that has not been referenced for the longest time. Stack algorithm "
                "(immune to Belady's Anomaly), implemented via timestamp counters or reference bits.\n\n"
                "Thrashing:\n"
                "When physical memory is overcommitted and processes lack sufficient frames to hold their 'Working Set', page fault frequency "
                "spikes exponentially. The CPU spends virtually all time swapping pages in/out of disk rather than executing instructions, "
                "causing CPU utilization to collapse to near zero. Resolved using the Working Set Model or local page replacement."
            ),
            "key_definitions": [
                {"term": "Page Fault", "definition": "A hardware interrupt triggered when an executing program accesses a page not currently mapped in physical RAM."},
                {"term": "Belady's Anomaly", "definition": "A phenomenon in FIFO page replacement where adding more page frames leads to an increased number of page faults."},
                {"term": "Thrashing", "definition": "A high-paging state where the operating system spends more time servicing page faults than executing instructions."}
            ],
            "interview_questions": [
                {
                    "q": "Walk through the sequence of events that occurs during a Page Fault.",
                    "a": "1. CPU attempts to access virtual address whose page table entry has valid bit = 0. 2. Hardware triggers a page fault trap to OS kernel. 3. OS checks process memory map: if illegal access, terminate (segmentation fault). 4. If legal, OS finds a free physical frame (or evicts a victim page using LRU). 5. Schedules disk I/O to read page from swap space into selected frame. 6. While disk transfers, CPU context-switches to another ready process. 7. On I/O completion interrupt, OS updates page table with frame number and valid bit = 1. 8. Interrupted instruction is restarted."
                },
                {
                    "q": "What is Belady's Anomaly, and which page replacement algorithms are susceptible to it?",
                    "a": "Belady's Anomaly is the counter-intuitive phenomenon where increasing the number of physical page frames results in an increased number of page faults for a given reference string. It occurs in algorithms that do not satisfy the 'inclusion property' (known as Stack Algorithms), most notably FIFO. Stack algorithms like LRU and Optimal are provably immune to Belady's Anomaly."
                },
                {
                    "q": "What is Thrashing, what causes it, and how can the OS eliminate it?",
                    "a": "Thrashing occurs when the total working sets of all running processes exceed physical RAM capacity. The system spends nearly 100% of time handling page faults and disk I/O, causing CPU utilization to drop. The OS scheduler, seeing low CPU utilization, mistakenly admits more processes, worsening the thrashing. The OS eliminates thrashing by: 1) Suspending (swapping out) one or more active processes to free frames, 2) Applying the Working Set Model to ensure a process is allocated its working set before execution."
                },
                {
                    "q": "How does the Dirty Bit (Modify Bit) optimize page replacement?",
                    "a": "Each page table entry includes a Dirty Bit, set to 1 by hardware whenever a byte in that page is written. When a victim page is selected for replacement: if dirty bit = 0, the page was never modified since being loaded from disk, so it can be discarded immediately without writing to disk. If dirty bit = 1, it must be written back to swap disk, cutting page replacement I/O overhead in half for read-only pages."
                },
                {
                    "q": "Explain the Working Set Model of a process.",
                    "a": "Introduced by Peter Denning, a process's Working Set W(t, delta) is the set of pages referenced by the process during the most recent time window delta. If total working set demand of all active processes exceeds physical frames, thrashing begins. The OS tracks working sets and temporarily suspends processes whose working set cannot fit in RAM."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-07-01",
                    "question": "Belady's Anomaly is observed in which page replacement algorithm?",
                    "options": ["LRU", "Optimal", "FIFO", "MRU"],
                    "correct_answer": "C",
                    "explanation": "FIFO does not satisfy the inclusion property, causing Belady's anomaly where more frames cause more faults."
                },
                {
                    "id": "CS-07-02",
                    "question": "What is the primary indicator that an OS has entered Thrashing?",
                    "options": ["CPU utilization near 100% with no page faults", "Excessive disk swap I/O and collapsing CPU utilization", "Network latency spikes", "Deadlock on thread mutexes"],
                    "correct_answer": "B",
                    "explanation": "Thrashing manifests as continuous page swapping and low CPU utilization."
                },
                {
                    "id": "CS-07-03",
                    "question": "The Dirty Bit (Modify Bit) in a page table entry indicates whether the page has been:",
                    "options": ["Read by CPU", "Modified in RAM since being loaded from disk", "Referenced by another thread", "Allocated in BSS"],
                    "correct_answer": "B",
                    "explanation": "The dirty bit tracks writes to determine if the page must be written back to disk on eviction."
                },
                {
                    "id": "CS-07-04",
                    "question": "Which page replacement algorithm is theoretically optimal but impossible to implement in practice?",
                    "options": ["FIFO", "LRU", "OPT (Belady's Optimal)", "Second-Chance"],
                    "correct_answer": "C",
                    "explanation": "OPT requires future knowledge of memory references, which cannot be known in advance."
                },
                {
                    "id": "CS-07-05",
                    "question": "A Page Fault is serviced by:",
                    "options": ["The application runtime", "The CPU ALU", "The Operating System Kernel", "The Network Interface Card"],
                    "correct_answer": "C",
                    "explanation": "Page faults trigger a kernel interrupt, which schedules disk I/O to load the page."
                }
            ]
        },

        # --- DAYS 8-14: DATABASE MANAGEMENT SYSTEMS ---
        8: {
            "subject": "DBMS",
            "topic": "DBMS Architecture, 3-Tier Schema, Data Independence & Relational Foundations",
            "concept_lesson": (
                "A Database Management System (DBMS) is software designed to store, manage, query, and enforce integrity over structured data.\n\n"
                "The ANSI-SPARC 3-Level Architecture:\n"
                "1. External Level (View Level): Describes user-facing views tailored to specific applications or roles (e.g., Student view vs HOD view in CSMS). Hides non-relevant data.\n"
                "2. Conceptual Level (Logical Level): Describes WHAT data is stored and relationships between entities across the entire database (tables, columns, constraints, foreign keys). Managed by DBA.\n"
                "3. Internal Level (Physical Level): Describes HOW data is physically organized on disk storage (B+ trees, byte offsets, block clustering, index files, compression).\n\n"
                "Data Independence:\n"
                "- Logical Data Independence: The ability to modify conceptual schema (e.g., adding an address column or splitting tables) without modifying external views or application code.\n"
                "- Physical Data Independence: The ability to alter physical storage structures (e.g., rebuilding B+ trees, migrating to SSDs, changing hash partitions) without altering the conceptual schema.\n\n"
                "Relational Model Foundations (Codd's Rules):\n"
                "Data is structured into Relations (tables), Tuples (rows), and Attributes (columns). "
                "Key constraints enforce mathematical validity: Domain Constraint (values must belong to defined data type), Entity Integrity (Primary Key cannot be NULL), "
                "and Referential Integrity (Foreign Key must either match an existing primary key in the referenced relation or be NULL)."
            ),
            "key_definitions": [
                {"term": "Physical Data Independence", "definition": "The capacity to change physical storage structures without altering conceptual schemas or applications."},
                {"term": "Entity Integrity", "definition": "A relational database rule stating that no primary key component can evaluate to NULL."},
                {"term": "Referential Integrity", "definition": "A constraint ensuring foreign key values match existing valid primary keys in referenced parent tables."}
            ],
            "interview_questions": [
                {
                    "q": "What is the difference between Logical and Physical Data Independence?",
                    "a": "Logical Data Independence allows changes to the conceptual schema (adding columns, creating views, modifying entities) without breaking existing application code or user views. Physical Data Independence allows changing physical storage layouts (file organizations, disk paths, B-tree indexes) without altering the logical schema or queries. Logical independence is harder to achieve because applications are tightly coupled to data attributes."
                },
                {
                    "q": "What are Codd's foundational constraints in the relational model?",
                    "a": "1. Domain Constraint: Every column value must be an atomic value from that domain. 2. Entity Integrity Constraint: Every table must have a Primary Key whose attributes cannot be NULL. 3. Referential Integrity Constraint: A Foreign Key in a child table must reference a valid, existing Primary Key in the parent table or be explicitly NULL."
                },
                {
                    "q": "Why is Primary Key required to be NOT NULL in relational databases?",
                    "a": "A primary key uniquely identifies individual tuples within a relation. If a primary key attribute were permitted to be NULL, the database engine could not distinguish between records or enforce unique entity identity, violating the foundational mathematical set definition of a relation."
                },
                {
                    "q": "Explain the difference between DDL, DML, DCL, and TCL in SQL.",
                    "a": "DDL (Data Definition Language: CREATE, ALTER, DROP, TRUNCATE) defines database schemas and structure. DML (Data Manipulation Language: SELECT, INSERT, UPDATE, DELETE) queries and alters data rows. DCL (Data Control Language: GRANT, REVOKE) manages security permissions. TCL (Transaction Control Language: COMMIT, ROLLBACK, SAVEPOINT) manages transaction execution."
                },
                {
                    "q": "What is the difference between DROP, TRUNCATE, and DELETE?",
                    "a": "DELETE is a DML command that removes rows one-by-one, logs each deletion in transaction logs, activates triggers, and can be rolled back. TRUNCATE is a DDL command that deallocates entire data pages, removing all rows ultra-fast with minimal logging; it cannot be filtered with WHERE and cannot activate delete triggers. DROP is a DDL command that destroys the entire table structure and its data from the database catalog."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-08-01",
                    "question": "Which level of the ANSI-SPARC 3-tier architecture describes the physical storage of data on disk?",
                    "options": ["External level", "Conceptual level", "Internal level", "Logical level"],
                    "correct_answer": "C",
                    "explanation": "The Internal (Physical) level describes how data is organized as blocks and indexes on disk."
                },
                {
                    "id": "CS-08-02",
                    "question": "The rule stating that a Foreign Key value must either match a Primary Key in the referenced relation or be NULL is:",
                    "options": ["Domain Constraint", "Entity Integrity", "Referential Integrity", "Key Constraint"],
                    "correct_answer": "C",
                    "explanation": "Referential Integrity ensures child foreign keys point to valid existing parent rows."
                },
                {
                    "id": "CS-08-03",
                    "question": "Which SQL command is a DDL command that removes all rows from a table by deallocating data pages?",
                    "options": ["DELETE", "TRUNCATE", "DROP TABLE", "REMOVE"],
                    "correct_answer": "B",
                    "explanation": "TRUNCATE deallocates data pages quickly without individual row logging."
                },
                {
                    "id": "CS-08-04",
                    "question": "The ability to modify the conceptual schema without altering existing user views is known as:",
                    "options": ["Physical Data Independence", "Logical Data Independence", "Data Redundancy", "Transaction Isolation"],
                    "correct_answer": "B",
                    "explanation": "Logical Data Independence shields user views from modifications to logical tables."
                },
                {
                    "id": "CS-08-05",
                    "question": "Entity Integrity rule explicitly prohibits which of the following?",
                    "options": ["Duplicate foreign keys", "A Primary Key containing a NULL value", "Secondary indexes", "Composite attributes"],
                    "correct_answer": "B",
                    "explanation": "Entity Integrity dictates that primary key attributes cannot be NULL."
                }
            ]
        },

        9: {
            "subject": "DBMS",
            "topic": "Relational Algebra, SQL Joins & Subquery Optimization",
            "concept_lesson": (
                "Relational Algebra is the formal procedural query language underlying SQL query compilation and optimization.\n\n"
                "Fundamental Operators:\n"
                "1. Selection (sigma): Filters tuples satisfying a predicate: sigma_{dept='CS'}(Students).\n"
                "2. Projection (pi): Selects specific columns and eliminates duplicates: pi_{name, roll}(Students).\n"
                "3. Cartesian Product (X): Combines every tuple of R with every tuple of S.\n"
                "4. Set Operations: Union (U), Set Difference (-), Intersection (cap) (require Union Compatibility).\n"
                "5. Natural Join (bowtie): Equijoin on all common attribute names followed by projection eliminating duplicate columns.\n\n"
                "SQL Joins Deep-Dive:\n"
                "- INNER JOIN: Returns rows with matching values in both tables.\n"
                "- LEFT OUTER JOIN: Returns all rows from left table, with matched rows from right table (or NULL if no match).\n"
                "- RIGHT OUTER JOIN: Returns all rows from right table, with matched left rows or NULL.\n"
                "- FULL OUTER JOIN: Combines LEFT and RIGHT join results; returns all rows from both tables, filling NULLs on mismatches.\n"
                "- CROSS JOIN: Cartesian product of both tables (size = N * M).\n"
                "- SELF JOIN: Joining a table to itself using aliases (common for hierarchical manager-employee relationships).\n\n"
                "Subqueries vs Joins:\n"
                "Correlated Subqueries execute once for every candidate row evaluated by the outer query, resulting in O(N*M) execution. "
                "Query optimizers transform correlated subqueries into equivalent Hash Joins or Merge Joins to run in O(N + M) time."
            ),
            "key_definitions": [
                {"term": "Cartesian Product", "definition": "A relational operation combining all tuples of two tables, producing N * M rows."},
                {"term": "Natural Join", "definition": "A join matching tuples on identical column names and projecting out duplicate columns."},
                {"term": "Correlated Subquery", "definition": "A nested SQL query that references columns from the outer query, re-evaluating for every outer row."}
            ],
            "interview_questions": [
                {
                    "q": "What is the difference between WHERE and HAVING clauses in SQL?",
                    "a": "WHERE filters individual rows before any grouping occurs and cannot evaluate aggregate functions (e.g., WHERE count(*) > 5 is illegal). HAVING filters aggregated groups after the GROUP BY clause has executed and is specifically designed to evaluate aggregate conditions (e.g., HAVING sum(salary) > 50000)."
                },
                {
                    "q": "Explain the difference between INNER JOIN, LEFT JOIN, and FULL OUTER JOIN.",
                    "a": "INNER JOIN returns only rows where the join condition evaluates to TRUE in both tables. LEFT JOIN returns all rows from the left table; matching rows from the right table are populated, and unmatched right columns return NULL. FULL OUTER JOIN returns all rows from both tables, populating columns with NULL whenever an opposite record does not exist."
                },
                {
                    "q": "Why are correlated subqueries generally slower than JOINs, and how do database query engines optimize them?",
                    "a": "A correlated subquery references values from the outer query, forcing the engine to execute the inner query once for every single row in the outer table (nested loop, O(N * M)). Modern query planners optimize these by rewriting correlated subqueries into INNER or LEFT JOINs, allowing the query engine to use fast O(N + M) Hash Join or Merge Join algorithms."
                },
                {
                    "q": "Write a query to find the N-th highest salary from an Employee table without using LIMIT/TOP.",
                    "a": "SELECT DISTINCT salary FROM Employee E1 WHERE (N - 1) = (SELECT COUNT(DISTINCT salary) FROM Employee E2 WHERE E2.salary > E1.salary). Alternatively, using modern window functions: WITH RankedSalaries AS (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank_pos FROM Employee) SELECT salary FROM RankedSalaries WHERE rank_pos = N."
                },
                {
                    "q": "What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER() in SQL?",
                    "a": "ROW_NUMBER() assigns a unique sequential integer to every row regardless of ties (1, 2, 3, 4). RANK() assigns the same rank to identical values but leaves gaps in rank sequence after ties (1, 2, 2, 4). DENSE_RANK() assigns the same rank to ties without skipping subsequent ranks (1, 2, 2, 3)."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-09-01",
                    "question": "Which relational algebra operator selects specific columns from a relation?",
                    "options": ["Selection (sigma)", "Projection (pi)", "Cartesian Product (X)", "Join (bowtie)"],
                    "correct_answer": "B",
                    "explanation": "Projection (pi) extracts specified attribute columns and removes duplicate rows."
                },
                {
                    "id": "CS-09-02",
                    "question": "Which clause must be used to filter groups based on aggregate function values in SQL?",
                    "options": ["WHERE", "HAVING", "GROUP BY", "ORDER BY"],
                    "correct_answer": "B",
                    "explanation": "HAVING filters groups post-aggregation; WHERE cannot take aggregate functions."
                },
                {
                    "id": "CS-09-03",
                    "question": "If Table A has 5 rows and Table B has 4 rows, how many rows are returned by a CROSS JOIN?",
                    "options": ["9", "20", "1", "5"],
                    "correct_answer": "B",
                    "explanation": "CROSS JOIN produces the Cartesian product: 5 * 4 = 20 rows."
                },
                {
                    "id": "CS-09-04",
                    "question": "If two employees tie for salary rank 2, what rank will DENSE_RANK() assign to the next employee?",
                    "options": ["3", "4", "2", "NULL"],
                    "correct_answer": "A",
                    "explanation": "DENSE_RANK() does not skip rank values after ties: 1, 2, 2, 3."
                },
                {
                    "id": "CS-09-05",
                    "question": "A LEFT OUTER JOIN returns:",
                    "options": ["Only matching rows from both tables", "All rows from the left table and matched rows from the right table", "Only non-matching rows from left table", "All rows from right table only"],
                    "correct_answer": "B",
                    "explanation": "LEFT JOIN preserves every row from the left relation, filling NULL for unmatched right attributes."
                }
            ]
        },

        10: {
            "subject": "DBMS",
            "topic": "Database Normalization: 1NF, 2NF, 3NF, BCNF & Functional Dependencies",
            "concept_lesson": (
                "Normalization is the systematic process of decomposing database relations to minimize data redundancy and eliminate "
                "Update, Insertion, and Deletion Anomalies while preserving Functional Dependencies and ensuring Lossless Join.\n\n"
                "Functional Dependency (FD: X -> Y):\n"
                "If two tuples agree on attribute set X, they must also agree on attribute set Y. X is the Determinant.\n\n"
                "Normal Forms Progression:\n"
                "1. First Normal Form (1NF): Every attribute value must be atomic (indivisible single values; no repeating groups, arrays, or comma-separated lists).\n"
                "2. Second Normal Form (2NF): Must be in 1NF AND have NO Partial Functional Dependency. Every non-prime attribute must be "
                "fully functionally dependent on the ENTIRE candidate key. (Applies only when candidate key is composite).\n"
                "3. Third Normal Form (3NF): Must be in 2NF AND have NO Transitive Dependency. For every non-trivial FD X -> Y, either "
                "X is a Superkey OR Y is a Prime Attribute (member of a candidate key).\n"
                "4. Boyce-Codd Normal Form (BCNF): A stricter version of 3NF. For every non-trivial FD X -> Y, X MUST be a Superkey. "
                "BCNF completely eliminates all functional redundancy, but decomposing into BCNF may sometimes sacrifice Dependency Preservation.\n\n"
                "Armstrong's Axioms:\n"
                "Reflexivity (if Y subset X, X -> Y), Augmentation (if X -> Y, XZ -> YZ), Transitivity (if X -> Y and Y -> Z, X -> Z)."
            ),
            "key_definitions": [
                {"term": "Functional Dependency", "definition": "A constraint between two sets of attributes in a relation where values of X uniquely determine values of Y."},
                {"term": "Partial Dependency", "definition": "A dependency where a non-prime attribute is determined by a subset of a composite candidate key."},
                {"term": "Transitive Dependency", "definition": "A dependency where a non-prime attribute is determined by another non-prime attribute: X -> Y and Y -> Z."}
            ],
            "interview_questions": [
                {
                    "q": "What are Insertion, Deletion, and Modification anomalies in an unnormalized database?",
                    "a": "Insertion Anomaly: Inability to record certain information without inserting extraneous dummy data (e.g., cannot register a new department without enrolling a student). Deletion Anomaly: Deleting one piece of data inadvertently deletes unrelated vital data (e.g., deleting the last student enrolled in a course deletes the course catalog record). Modification Anomaly: Inconsistent data when updating redundant instances in multiple rows (e.g., updating a professor's phone number in one row but missing other student rows)."
                },
                {
                    "q": "What is the exact distinction between 3NF and BCNF?",
                    "a": "For every non-trivial functional dependency X -> Y: In 3NF, the rule is satisfied if X is a Superkey OR Y is a prime attribute. In BCNF, the rule strictly requires X to be a Superkey with NO exceptions. BCNF is strictly stronger than 3NF. Any relation in BCNF is guaranteed to be in 3NF, but a 3NF relation with overlapping candidate keys may violate BCNF."
                },
                {
                    "q": "Can a table with a single-attribute primary key violate 2NF?",
                    "a": "No. 2NF states that no non-prime attribute can be dependent on a proper subset of a candidate key (no partial dependency). If the candidate key consists of a single attribute, it has no proper subsets other than empty set, making partial dependency mathematically impossible. A 1NF table with a single-column primary key is automatically in 2NF."
                },
                {
                    "q": "What is a Lossless Join Decomposition, and why is it critical?",
                    "a": "A decomposition of relation R into R1 and R2 is lossless if natural join R1 bowtie R2 recovers exactly relation R without generating false 'spurious tuples'. Mathematically, the common attribute must be a superkey in at least one of the decomposed relations: (R1 cap R2 -> R1) OR (R1 cap R2 -> R2)."
                },
                {
                    "q": "What is Denormalization, and when is it recommended in production systems?",
                    "a": "Denormalization is the deliberate re-introduction of redundancy into normalized relations (e.g., storing customer_name directly inside the orders table). It is used in read-heavy analytics, data warehouses, and microservices to avoid expensive multi-table JOIN operations, trading write performance and storage space for ultra-fast query execution speeds."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-10-01",
                    "question": "A table is in 2NF if it is in 1NF and contains no:",
                    "options": ["Transitive dependencies", "Partial functional dependencies", "Foreign keys", "Composite candidate keys"],
                    "correct_answer": "B",
                    "explanation": "2NF mandates that all non-prime attributes are fully dependent on the complete candidate key."
                },
                {
                    "id": "CS-10-02",
                    "question": "In 3NF, for every non-trivial functional dependency X -> Y, which condition must hold?",
                    "options": ["X must be a candidate key and Y must be NULL", "X is a Superkey OR Y is a Prime attribute", "Both X and Y must be superkeys", "Y must be a foreign key"],
                    "correct_answer": "B",
                    "explanation": "3NF relaxes BCNF by permitting Y to be a prime attribute."
                },
                {
                    "id": "CS-10-03",
                    "question": "Which normal form requires every determinant to be a Superkey for all non-trivial dependencies?",
                    "options": ["1NF", "2NF", "3NF", "BCNF"],
                    "correct_answer": "D",
                    "explanation": "BCNF strictly requires the determinant X to be a superkey for every non-trivial FD X -> Y."
                },
                {
                    "id": "CS-10-04",
                    "question": "A 1NF relation whose primary key consists of a single column is guaranteed to be in:",
                    "options": ["2NF", "3NF", "BCNF", "4NF"],
                    "correct_answer": "A",
                    "explanation": "A single-column key has no proper subkeys, so partial dependencies cannot exist."
                },
                {
                    "id": "CS-10-05",
                    "question": "The property ensuring that joining decomposed relations does not produce spurious tuples is called:",
                    "options": ["Dependency Preservation", "Lossless Join Property", "Referential Closure", "Atomicity"],
                    "correct_answer": "B",
                    "explanation": "Lossless join decomposition ensures original relations can be reconstructed without phantom rows."
                }
            ]
        },

        11: {
            "subject": "DBMS",
            "topic": "Transactions & ACID Properties (Atomicity, Consistency, Isolation, Durability)",
            "concept_lesson": (
                "A Database Transaction is a logical unit of work comprising one or more database operations (reads, writes) that must "
                "execute reliably as an indivisible whole.\n\n"
                "The ACID Properties:\n"
                "1. Atomicity ('All or Nothing'): Either all operations of the transaction complete successfully and are committed, "
                "or the entire transaction is aborted and rolled back to its initial state. Enforced by the DBMS Recovery Manager using Write-Ahead Logging (WAL).\n"
                "2. Consistency: A transaction transforms the database from one valid consistent state to another, preserving all declared "
                "schema constraints (primary keys, foreign keys, CHECK constraints, trigger invariants).\n"
                "3. Isolation: The execution of concurrent transactions must occur without mutual interference. The intermediate uncommitted state "
                "of a transaction must remain invisible to other concurrent transactions. Enforced by Concurrency Control Manager.\n"
                "4. Durability: Once a transaction commits, its modifications are permanently recorded in non-volatile storage and will survive "
                "subsequent power failures or system crashes. Enforced via WAL flush to disk.\n\n"
                "Transaction State Diagram:\n"
                "Active -> Partially Committed (after final statement executes) -> Committed (after log flushed to disk).\n"
                "Active -> Failed (on error/abort) -> Aborted (after rollback cleans up uncommitted changes)."
            ),
            "key_definitions": [
                {"term": "Atomicity", "definition": "The ACID property ensuring all transaction operations succeed completely or are rolled back entirely."},
                {"term": "Write-Ahead Logging (WAL)", "definition": "A technique where state changes are recorded on non-volatile disk logs before being applied to data pages."},
                {"term": "Durability", "definition": "The guarantee that committed transaction updates persist permanently across crashes and power outages."}
            ],
            "interview_questions": [
                {
                    "q": "How does a database enforce Atomicity and Durability during a sudden system crash?",
                    "a": "Using Write-Ahead Logging (WAL). Before any data page is modified in RAM or written to disk, an append-only log record describing the change (Undo and Redo logs) is flushed to non-volatile disk. On system restart after a crash, the recovery manager runs the ARIES protocol: Analysis phase identifies dirty pages, Redo phase replays all logged changes to re-establish state (Durability), and Undo phase rolls back all uncommitted transactions (Atomicity)."
                },
                {
                    "q": "What is the difference between a Partially Committed state and a Committed state?",
                    "a": "A transaction enters the Partially Committed state immediately after its final SQL statement has executed in memory, but before its commit log records are permanently written to disk. It transitions to the Committed state only after the WAL commit record has been physically flushed to persistent storage."
                },
                {
                    "q": "Explain the difference between Compensating Transactions and standard Rollback.",
                    "a": "A standard rollback relies on database undo logs within a single ACID transaction to revert uncommitted memory changes. A Compensating Transaction is used in distributed architectures (e.g., Saga Pattern across microservices) where local transactions have already committed; a subsequent failure triggers dedicated business actions (e.g., refunding a captured credit card) to logically offset prior committed steps."
                },
                {
                    "q": "Can Consistency in ACID be guaranteed exclusively by the database engine?",
                    "a": "No. While the DBMS strictly enforces declared schema constraints (unique keys, foreign keys, data types), application-level business consistency (e.g., account balance cannot transfer more than ledger limits) relies heavily on correct application logic written by the software engineer."
                },
                {
                    "q": "What is the Checkpoint mechanism in database recovery?",
                    "a": "A Checkpoint periodically flushes all dirty in-memory data buffer pages and log records to persistent disk, and writes a CHECKPOINT record with active transaction IDs to the log. During crash recovery, the DBMS only needs to scan logs back to the most recent checkpoint rather than replaying the entire history of the database."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-11-01",
                    "question": "Which ACID property guarantees that all operations of a transaction succeed or none do?",
                    "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
                    "correct_answer": "A",
                    "explanation": "Atomicity ensures 'all-or-nothing' execution."
                },
                {
                    "id": "CS-11-02",
                    "question": "Write-Ahead Logging (WAL) requires that:",
                    "options": ["Data pages are written before log records", "Log records are flushed to non-volatile storage before corresponding data pages are written", "Transactions commit without logs", "Checkpoints run before every query"],
                    "correct_answer": "B",
                    "explanation": "WAL mandates logging modifications before data pages touch persistent storage."
                },
                {
                    "id": "CS-11-03",
                    "question": "A transaction enters the 'Partially Committed' state when:",
                    "options": ["It begins execution", "Its final statement has executed, prior to log disk flush", "Its changes are rolled back", "A deadlock is detected"],
                    "correct_answer": "B",
                    "explanation": "Partially committed occurs right after the last operation executes, before log flush."
                },
                {
                    "id": "CS-11-04",
                    "question": "Which ACID property ensures that committed transactions survive power failures and system crashes?",
                    "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
                    "correct_answer": "D",
                    "explanation": "Durability guarantees committed changes persist permanently."
                },
                {
                    "id": "CS-11-05",
                    "question": "Checkpoints are used in database recovery systems to:",
                    "options": ["Speed up SQL join processing", "Reduce the log volume that must be scanned during recovery", "Encrypt password fields", "Enforce 3NF schema constraints"],
                    "correct_answer": "B",
                    "explanation": "Checkpoints limit how far back the recovery manager must scan WAL logs on reboot."
                }
            ]
        },

        12: {
            "subject": "DBMS",
            "topic": "Concurrency Control: Isolation Levels & Read Phenomena",
            "concept_lesson": (
                "Concurrent execution of transactions increases throughput and resource utilization, but uncoordinated access leads to "
                "three classic Concurrency Read Phenomena:\n"
                "1. Dirty Read: Transaction T1 updates a row without committing; Transaction T2 reads the uncommitted row. If T1 rolls back, "
                "T2 has read non-existent data.\n"
                "2. Non-Repeatable Read (Fuzzy Read): T1 reads a row; T2 modifies or deletes that row and commits. T1 re-reads the same row "
                "and finds different values.\n"
                "3. Phantom Read: T1 executes a range query (e.g., SELECT * WHERE age > 20); T2 inserts new matching rows and commits. "
                "T1 re-executes the query and discovers new 'phantom' rows.\n\n"
                "SQL-92 Standard Isolation Levels:\n"
                "- Read Uncommitted: Allows Dirty Reads, Non-Repeatable Reads, Phantom Reads. Highest throughput, lowest consistency.\n"
                "- Read Committed: Prevents Dirty Reads. Still permits Non-Repeatable Reads and Phantom Reads. (Default in PostgreSQL & Oracle).\n"
                "- Repeatable Read: Prevents Dirty Reads and Non-Repeatable Reads. Still permits Phantom Reads in standard definitions (MySQL InnoDB prevents phantoms via Next-Key Locks).\n"
                "- Serializable: Prevents all read phenomena. Concurrent execution produces results identical to serial execution. Lowest throughput.\n\n"
                "Multi-Version Concurrency Control (MVCC):\n"
                "Modern databases (PostgreSQL, MySQL InnoDB) implement isolation via MVCC: Readers never block Writers, and Writers never block Readers. "
                "Each update creates a new row version with transaction timestamp (xmin, xmax). Transactions view a consistent historical snapshot."
            ),
            "key_definitions": [
                {"term": "Dirty Read", "definition": "Reading uncommitted data written by a concurrent transaction that might subsequently roll back."},
                {"term": "Phantom Read", "definition": "A transaction re-executing a range query discovering new rows inserted by a newly committed transaction."},
                {"term": "MVCC", "definition": "Multi-Version Concurrency Control: maintaining multiple row versions so readers read historical snapshots without blocking writers."}
            ],
            "interview_questions": [
                {
                    "q": "Explain the difference between a Non-Repeatable Read and a Phantom Read.",
                    "a": "A Non-Repeatable Read occurs when a transaction re-reads a specific single row and discovers the data inside that row has changed because another transaction modified or deleted it. A Phantom Read occurs during range queries (e.g., WHERE score > 75) when a transaction re-executes the query and finds new rows that were inserted by another transaction fulfilling the range condition."
                },
                {
                    "q": "What is MVCC (Multi-Version Concurrency Control) and why is it preferred over lock-based concurrency?",
                    "a": "MVCC maintains multiple physical versions of each row tagged with creation and deletion transaction IDs (e.g., xmin, xmax in PostgreSQL). When a transaction reads data, it reads the snapshot version visible at its start timestamp. This achieves high concurrency because 'readers never block writers, and writers never block readers', eliminating read lock contention."
                },
                {
                    "q": "What is the default isolation level in PostgreSQL vs MySQL InnoDB?",
                    "a": "PostgreSQL defaults to Read Committed. MySQL InnoDB defaults to Repeatable Read (which additionally prevents phantom reads using Next-Key Locking)."
                },
                {
                    "q": "How does Snapshot Isolation differ from Strict Serializability?",
                    "a": "In Snapshot Isolation, a transaction reads from a private snapshot of the database taken when the transaction started. It avoids dirty reads, non-repeatable reads, and phantom reads. However, it can permit Write Skew anomalies (two concurrent transactions reading overlapping data, modifying disjoint rows, and violating a global constraint). Strict Serializability prevents write skew."
                },
                {
                    "q": "What is Write Skew anomaly, and provide a concrete example?",
                    "a": "Write skew occurs under Snapshot Isolation. Example: A hospital requires at least one doctor on call. Doctors Alice and Bob are both on call. Alice submits a transaction to take leave: her transaction checks the snapshot, sees Bob is on call, and sets her status to inactive. Simultaneously, Bob submits a transaction, checks his snapshot, sees Alice is on call, and sets his status to inactive. Both commit, leaving zero doctors on call."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-12-01",
                    "question": "Which SQL isolation level allows Dirty Reads?",
                    "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
                    "correct_answer": "A",
                    "explanation": "Read Uncommitted allows reading uncommitted, dirty rows."
                },
                {
                    "id": "CS-12-02",
                    "question": "A transaction re-executes a range query and discovers newly inserted rows that match the predicate. This is a:",
                    "options": ["Dirty Read", "Non-Repeatable Read", "Phantom Read", "Lost Update"],
                    "correct_answer": "C",
                    "explanation": "Newly appearing rows in a range query are Phantom Reads."
                },
                {
                    "id": "CS-12-03",
                    "question": "What is the core principle of Multi-Version Concurrency Control (MVCC)?",
                    "options": ["All transactions execute strictly serially", "Readers never block writers, and writers never block readers", "Exclusive locks are acquired for every SELECT", "Rollbacks are prohibited"],
                    "correct_answer": "B",
                    "explanation": "MVCC creates versioned snapshots, allowing non-blocking reads and concurrent writes."
                },
                {
                    "id": "CS-12-04",
                    "question": "Which isolation level completely prevents all read phenomena, ensuring equivalence to serial execution?",
                    "options": ["Read Committed", "Repeatable Read", "Serializable", "Snapshot Isolation"],
                    "correct_answer": "C",
                    "explanation": "Serializable isolation guarantees equivalent results to a serial schedule."
                },
                {
                    "id": "CS-12-05",
                    "question": "What is the default isolation level in PostgreSQL?",
                    "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
                    "correct_answer": "B",
                    "explanation": "PostgreSQL uses Read Committed as its default isolation level."
                }
            ]
        },

        13: {
            "subject": "DBMS",
            "topic": "Lock-Based Protocols, Two-Phase Locking (2PL) & Serializability",
            "concept_lesson": (
                "To guarantee serializability among concurrent transactions, database systems enforce Lock-Based Concurrency Protocols.\n\n"
                "Lock Modes:\n"
                "- Shared Lock (S-Lock / Read Lock): Multiple transactions can acquire shared locks on the same data item concurrently.\n"
                "- Exclusive Lock (X-Lock / Write Lock): Only one transaction can hold an exclusive lock; all other lock requests (S or X) are blocked.\n\n"
                "Two-Phase Locking Protocol (2PL):\n"
                "2PL guarantees Conflict Serializability. A transaction must adhere to two distinct, non-overlapping phases:\n"
                "1. Growing Phase: The transaction may acquire locks, but cannot release any lock.\n"
                "2. Shrinking Phase: The transaction may release locks, but cannot acquire any new locks.\n"
                "The point where the transaction acquires its final lock is the Lock Point.\n\n"
                "Variations of 2PL:\n"
                "- Strict 2PL: All Exclusive locks must be held until the transaction commits or aborts. Prevents Cascading Aborts (Cascadeless schedules).\n"
                "- Rigorous 2PL: ALL locks (both Shared and Exclusive) are held until transaction commits. Guarantees serializability and simplifies recovery.\n\n"
                "Deadlocks in 2PL:\n"
                "2PL guarantees serializability but does NOT prevent Deadlocks. Handled via Wait-For Graphs (cycle detection) or timestamp schemes "
                "(Wait-Die: older waits, younger dies; Wound-Wait: older preempts younger, younger waits)."
            ),
            "key_definitions": [
                {"term": "Two-Phase Locking (2PL)", "definition": "A protocol requiring transactions to acquire all locks in a growing phase and release in a shrinking phase."},
                {"term": "Conflict Serializability", "definition": "A schedule that can be transformed into a serial schedule by swapping non-conflicting concurrent operations."},
                {"term": "Strict 2PL", "definition": "A 2PL variation holding exclusive locks until transaction commit to prevent cascading rollbacks."}
            ],
            "interview_questions": [
                {
                    "q": "Does basic Two-Phase Locking (2PL) prevent deadlocks?",
                    "a": "No. Basic 2PL guarantees Conflict Serializability, but it does NOT prevent deadlocks. Example: T1 holds Lock A and requests Lock B; T2 holds Lock B and requests Lock A. Both transactions are in their growing phase and block indefinitely, forming a deadlock."
                },
                {
                    "q": "What is Cascading Rollback (Cascading Abort) and how does Strict 2PL prevent it?",
                    "a": "Cascading Rollback occurs when an uncommitted transaction T1 modifies a row and releases its lock early in its shrinking phase. T2 reads that updated row and proceeds. If T1 subsequently aborts, T2 must also be aborted, triggering a cascade of rollbacks across multiple transactions. Strict 2PL prevents this by holding all exclusive locks until commit/abort, ensuring uncommitted updates are never visible."
                },
                {
                    "q": "What is the difference between Wait-Die and Wound-Wait deadlock prevention schemes?",
                    "a": "Both assign unique timestamps to transactions (lower timestamp = older transaction). In Wait-Die (non-preemptive): if older requests resource held by younger, older waits; if younger requests resource held by older, younger dies (aborts and restarts). In Wound-Wait (preemptive): if older requests resource held by younger, older 'wounds' (preempts/aborts) younger; if younger requests resource held by older, younger waits."
                },
                {
                    "q": "What defines conflicting operations in transaction schedules?",
                    "a": "Two operations conflict if and only if: 1) They belong to different transactions, 2) They access the exact same data item, and 3) At least one of the two operations is a WRITE operation. Read-Read operations never conflict."
                },
                {
                    "q": "How does a Precedence Graph (Serialization Graph) test for Conflict Serializability?",
                    "a": "Create a directed graph with a node for each committed transaction. Draw a directed edge Ti -> Tj if an operation of Ti conflicts with an operation of Tj and Ti executed before Tj. If the precedence graph contains NO cycles, the schedule is Conflict Serializable; if a cycle exists, it is not conflict serializable."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-13-01",
                    "question": "What is the primary guarantee provided by the Two-Phase Locking (2PL) protocol?",
                    "options": ["Deadlock freedom", "Conflict Serializability", "Zero disk latency", "Automatic index selection"],
                    "correct_answer": "B",
                    "explanation": "2PL mathematically guarantees conflict serializable execution schedules."
                },
                {
                    "id": "CS-13-02",
                    "question": "In Strict 2PL, when are Exclusive locks released?",
                    "options": ["During the shrinking phase immediately after use", "Only after the transaction commits or aborts", "When a Shared lock is requested", "At the lock point"],
                    "correct_answer": "B",
                    "explanation": "Strict 2PL holds exclusive locks until commit or abort to avoid cascading rollbacks."
                },
                {
                    "id": "CS-13-03",
                    "question": "A schedule is Conflict Serializable if its Precedence Graph has:",
                    "options": ["At least one cycle", "No directed cycles (DAG)", "Equal in-degree and out-degree", "Only self-loops"],
                    "correct_answer": "B",
                    "explanation": "Acycle precedence graphs indicate conflict serializable schedules."
                },
                {
                    "id": "CS-13-04",
                    "question": "In the Wound-Wait deadlock prevention scheme, if an older transaction requests a resource held by a younger transaction, the older transaction:",
                    "options": ["Aborts immediately", "Preempts (wounds) the younger transaction", "Waits indefinitely", "Downgrades to a read lock"],
                    "correct_answer": "B",
                    "explanation": "In Wound-Wait, older transactions preempt younger transactions holding needed locks."
                },
                {
                    "id": "CS-13-05",
                    "question": "Which pair of concurrent operations on the same data item does NOT conflict?",
                    "options": ["Read - Write", "Write - Write", "Read - Read", "Write - Read"],
                    "correct_answer": "C",
                    "explanation": "Read-Read operations do not alter data and can proceed concurrently."
                }
            ]
        },

        14: {
            "subject": "DBMS",
            "topic": "Database Indexing: B-Trees, B+ Trees, Clustered vs Non-Clustered Indexes",
            "concept_lesson": (
                "A Database Index is an auxiliary search data structure that optimizes data retrieval without scanning every table page.\n\n"
                "B-Tree vs B+ Tree Architecture:\n"
                "- B-Tree: Stores keys and actual data record pointers in both internal routing nodes and leaf nodes. Searching for keys stored "
                "in top internal nodes can terminate early without reaching leaves.\n"
                "- B+ Tree: The universal choice for relational databases (PostgreSQL, MySQL InnoDB, SQLite). Internal nodes store ONLY routing keys "
                "and child node pointers (maximizing fan-out and reducing tree depth to 3-4 levels for billions of rows). ALL actual record pointers "
                "reside exclusively in the leaf nodes. Furthermore, leaf nodes are linked via a doubly linked list, enabling ultra-fast sequential range scans.\n\n"
                "Clustered vs Non-Clustered Indexes:\n"
                "- Clustered Index: Determines the physical sorting order of rows on disk. A table can have at most ONE clustered index (usually the Primary Key). "
                "In MySQL InnoDB, the clustered index table is the data itself (Index-Organized Table).\n"
                "- Non-Clustered (Secondary) Index: A separate search structure. Leaf nodes store the indexed key along with a pointer to the physical row "
                "(or clustered primary key). Requires a secondary lookup (Bookmark Lookup) to fetch non-indexed columns unless satisfied by a Covering Index."
            ),
            "key_definitions": [
                {"term": "B+ Tree", "definition": "A self-balancing N-ary tree storing keys in internal nodes and all data pointers in doubly-linked leaf nodes."},
                {"term": "Clustered Index", "definition": "An index where the physical order of table rows on disk matches the index key order (1 per table)."},
                {"term": "Covering Index", "definition": "An index containing all columns requested by a query, satisfying execution without touching table data pages."}
            ],
            "interview_questions": [
                {
                    "q": "Why do relational database engines use B+ Trees instead of B-Trees or Binary Search Trees for indexing?",
                    "a": "1. High Fan-out and Shallow Depth: Because internal nodes store only keys without data pointers, thousands of keys fit in a single 16KB disk page, keeping tree height to 3-4 levels for millions of rows (minimizing disk I/O). 2. Range Queries: In a B+ Tree, all leaf nodes are connected in a doubly linked list; range scans simply traverse leaves sequentially without tree back-tracking. 3. Predictable Latency: Every lookup traverses the exact same number of levels to the leaf."
                },
                {
                    "q": "What is the difference between a Clustered and a Non-Clustered index?",
                    "a": "A Clustered Index dictates the actual physical sorting order of table rows on disk; therefore, a table can have only ONE clustered index. In a Non-Clustered Index, data rows are stored independently, and the index contains pointers back to the rows. A table can have multiple non-clustered indexes."
                },
                {
                    "q": "What is a Covering Index in SQL optimization?",
                    "a": "A Covering Index includes all columns referenced in the query's SELECT, WHERE, JOIN, and ORDER BY clauses (e.g., using CREATE INDEX idx_emp ON Employee(dept_id, salary)). The database engine can satisfy the query entirely from the index tree without performing a secondary lookup to read the main table data pages, drastically reducing I/O."
                },
                {
                    "q": "What is Index Selectivity and how does it affect query optimizer decisions?",
                    "a": "Selectivity is the ratio of distinct values in a column to total row count: Cardinality / Total Rows. High selectivity (e.g., primary key or email, near 1.0) makes indexes extremely effective. Low selectivity (e.g., gender with only 2 distinct values) causes the query optimizer to skip the index and perform a Full Table Scan because scanning non-clustered index pointers for 50% of the rows is slower than a sequential disk scan."
                },
                {
                    "q": "What is the write penalty of having too many indexes on a table?",
                    "a": "Every INSERT, UPDATE, or DELETE statement must not only modify the primary table pages, but must also update every single secondary index tree (including balancing node splits or merges). Having excessive indexes slows down write throughput and inflates storage footprint."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-14-01",
                    "question": "Why are B+ Trees preferred over B-Trees for database disk indexing?",
                    "options": ["B+ trees require no sorting", "Internal nodes store only keys, maximizing fan-out, and leaf nodes form a linked list for range scans", "B+ trees are binary trees", "B+ trees store data in RAM only"],
                    "correct_answer": "B",
                    "explanation": "B+ trees pack more keys per internal page and link leaves for rapid range scanning."
                },
                {
                    "id": "CS-14-02",
                    "question": "How many Clustered Indexes can exist on a single database table?",
                    "options": ["Zero", "Exactly one", "Up to 16", "Unlimited"],
                    "correct_answer": "B",
                    "explanation": "Because physical disk rows can only be ordered in one sequence, only one clustered index can exist."
                },
                {
                    "id": "CS-14-03",
                    "question": "An index that contains every column requested by a query, avoiding physical table page lookups, is called a:",
                    "options": ["Bitmap Index", "Covering Index", "Dense Index", "Hash Index"],
                    "correct_answer": "B",
                    "explanation": "Covering indexes satisfy the query directly from leaf nodes without fetching base table pages."
                },
                {
                    "id": "CS-14-04",
                    "question": "In a B+ tree of order m, all leaf nodes reside at:",
                    "options": ["Different depths", "The exact same depth", "Depth 1", "Random positions"],
                    "correct_answer": "B",
                    "explanation": "B+ trees are strictly height-balanced; all leaf nodes reside at the exact same depth."
                },
                {
                    "id": "CS-14-05",
                    "question": "Creating an index on a boolean column (e.g., is_active) with 50/50 distribution is usually ineffective because:",
                    "options": ["B+ trees cannot store booleans", "The column has very low selectivity", "The index would be larger than the table", "Foreign keys cannot be booleans"],
                    "correct_answer": "B",
                    "explanation": "Low selectivity causes the query optimizer to choose a full table scan over the index."
                }
            ]
        },

        # --- DAYS 15-21: COMPUTER NETWORKS ---
        15: {
            "subject": "Computer Networks",
            "topic": "OSI 7-Layer Architecture vs TCP/IP Protocol Suite",
            "concept_lesson": (
                "Computer network communications rely on layered protocol stacks to provide modularity, standardization, and interoperability.\n\n"
                "The OSI 7-Layer Reference Model (Theoretical Framework):\n"
                "1. Physical Layer: Transmission of raw, unstructured bit streams over physical media (voltages, fiber photons, radio waves).\n"
                "2. Data Link Layer: Node-to-node framing, physical MAC addressing, flow control, and error detection (Ethernet, Wi-Fi).\n"
                "3. Network Layer: End-to-end logical addressing and routing packets across heterogeneous networks (IP, ICMP, OSPF, BGP).\n"
                "4. Transport Layer: End-to-end process-to-process communication, port multiplexing, segmentation, error recovery (TCP, UDP).\n"
                "5. Session Layer: Establishes, manages, and terminates presentation dialog sessions between applications (RPC, NetBIOS).\n"
                "6. Presentation Layer: Translation, character encoding, data compression, and encryption/decryption (TLS/SSL, ASCII, JPEG).\n"
                "7. Application Layer: High-level protocols interacting directly with end-user software (HTTP/HTTPS, DNS, SMTP, SSH).\n\n"
                "The TCP/IP 4-Layer Implementation Model:\n"
                "1. Network Access (Link) Layer: Maps to OSI Physical and Data Link.\n"
                "2. Internet Layer: Maps to OSI Network.\n"
                "3. Transport Layer: Maps to OSI Transport.\n"
                "4. Application Layer: Collapses OSI Session, Presentation, and Application layers into a single application stack.\n\n"
                "Data Encapsulation:\n"
                "Data -> Segment (Transport) -> Packet (Network) -> Frame (Data Link) -> Bits (Physical)."
            ),
            "key_definitions": [
                {"term": "Encapsulation", "definition": "The process where each protocol layer wraps data received from higher layers with its own control header."},
                {"term": "PDU (Protocol Data Unit)", "definition": "The unit of data specified in a layer: Data, Segment, Packet, Frame, or Bit."},
                {"term": "Port Number", "definition": "A 16-bit identifier (0-65535) multiplexing network communication to specific software processes."}
            ],
            "interview_questions": [
                {
                    "q": "What are the Protocol Data Units (PDUs) at each layer of the OSI model?",
                    "a": "Physical layer: Bits. Data Link layer: Frames. Network layer: Packets. Transport layer: Segments (for TCP) or Datagrams (for UDP). Application/Presentation/Session layers: Messages or Data."
                },
                {
                    "q": "Why does the practical TCP/IP suite combine OSI Session and Presentation into the Application layer?",
                    "a": "In real-world software, encryption (TLS), compression (gzip), and session management are application-specific concerns handled directly by user-space libraries (like OpenSSL) or web runtimes, rather than generic operating system kernel network drivers."
                },
                {
                    "q": "What happens during network encapsulation as data moves down the stack?",
                    "a": "The application payload is passed to the transport layer, which prefixes a TCP/UDP header containing source/dest ports to form a Segment. The network layer adds an IP header with source/dest IP addresses to form a Packet. The data link layer adds a header (MAC addresses) and trailer (CRC/FCS checksum) to form a Frame. The physical layer encodes the frame into bits for physical transmission."
                },
                {
                    "q": "Explain the difference between End-to-End communication and Hop-by-Hop communication.",
                    "a": "End-to-End communication occurs between the originating source host and final destination host across intermediate routers (governed by Transport and Network layers: TCP/IP). Hop-by-Hop communication occurs only between two physically adjacent network nodes on the same local link (governed by the Data Link layer using MAC addresses)."
                },
                {
                    "q": "What are well-known ports and give examples of standard network protocols?",
                    "a": "Port numbers 0 to 1023 are reserved well-known ports assigned by IANA for core services: Port 80 (HTTP), Port 443 (HTTPS), Port 22 (SSH), Port 53 (DNS), Port 25 (SMTP), Port 21 (FTP)."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-15-01",
                    "question": "What is the Protocol Data Unit (PDU) at the Network layer of the OSI model?",
                    "options": ["Frame", "Segment", "Packet", "Bit"],
                    "correct_answer": "C",
                    "explanation": "Network layer units are called Packets (or Datagrams)."
                },
                {
                    "id": "CS-15-02",
                    "question": "Which layer of the OSI model is responsible for encryption, compression, and character syntax translation?",
                    "options": ["Application layer", "Presentation layer", "Session layer", "Transport layer"],
                    "correct_answer": "B",
                    "explanation": "The Presentation layer handles data formatting, compression, and cryptography."
                },
                {
                    "id": "CS-15-03",
                    "question": "What is the standard port number for secure HTTPS communication?",
                    "options": ["80", "8080", "443", "22"],
                    "correct_answer": "C",
                    "explanation": "HTTPS runs over well-known port 443."
                },
                {
                    "id": "CS-15-04",
                    "question": "At which layer of the OSI model do network switches primarily operate?",
                    "options": ["Physical (Layer 1)", "Data Link (Layer 2)", "Network (Layer 3)", "Transport (Layer 4)"],
                    "correct_answer": "B",
                    "explanation": "Standard network switches operate at Layer 2 (Data Link), forwarding frames by MAC address."
                },
                {
                    "id": "CS-15-05",
                    "question": "In the TCP/IP 4-layer model, the Internet layer corresponds to which OSI layer?",
                    "options": ["Data Link layer", "Network layer", "Transport layer", "Session layer"],
                    "correct_answer": "B",
                    "explanation": "The TCP/IP Internet layer maps directly to the OSI Network layer."
                }
            ]
        },

        16: {
            "subject": "Computer Networks",
            "topic": "Data Link Layer: Framing, Error Detection (CRC) & Sliding Window Protocols",
            "concept_lesson": (
                "The Data Link Layer is responsible for reliable node-to-node frame delivery across a physical link.\n\n"
                "Framing Techniques:\n"
                "1. Character Count: Transmitter includes frame length in the header (fragile: one transmission error corrupts subsequent boundaries).\n"
                "2. Byte Stuffing: Delimits frames with special FLAG bytes; inserts an ESC byte before any data byte that happens to match FLAG.\n"
                "3. Bit Stuffing: Frame boundary is delimited by 01111110 (0 followed by six 1s and a 0). The sender automatically inserts a 0 "
                "after every sequence of five consecutive 1s in data; the receiver strips the stuffed 0.\n\n"
                "Error Detection & Correction:\n"
                "- Parity Bit: Adds a single bit for odd/even parity (detects single-bit errors).\n"
                "- Checksum: 16-bit 1's complement sum of 16-bit words (used in IP/TCP headers).\n"
                "- Cyclic Redundancy Check (CRC): Polynomial division over Galois Field GF(2). Generator polynomial G(x) divides data bits padded "
                "with degree(G) zeroes using XOR. The remainder is appended as the Frame Check Sequence (FCS). Detects all single, double, odd, and burst errors.\n\n"
                "Flow Control Protocols:\n"
                "- Stop-and-Wait: Sender transmits one frame and waits for ACK. Inefficient on high-latency links (bandwidth-delay product waste).\n"
                "- Go-Back-N (GBN): Sender uses sliding window of size N. If frame i is lost, receiver discards all subsequent frames; sender "
                "retransmits all frames from i to N upon timeout (Cumulative ACK).\n"
                "- Selective Repeat (SR): Receiver buffers out-of-order frames within a window; sender retransmits ONLY the specific lost frame (Individual ACK). "
                "Window size must be <= 2^(k-1) to avoid sequence number ambiguity."
            ),
            "key_definitions": [
                {"term": "Bit Stuffing", "definition": "Inserting a 0-bit after every 5 consecutive 1-bits to prevent user data from mimicking the frame delimiter flag."},
                {"term": "CRC (Cyclic Redundancy Check)", "definition": "An error-detecting code based on polynomial binary division with XOR arithmetic."},
                {"term": "Selective Repeat", "definition": "A sliding window protocol where only corrupted or lost frames are retransmitted by the sender."}
            ],
            "interview_questions": [
                {
                    "q": "How does Bit Stuffing work and why is it necessary in HDLC framing?",
                    "a": "HDLC uses the flag pattern 01111110 to designate frame boundaries. To prevent user data from accidentally mimicking this flag and causing premature frame termination, the sender inspects the data stream and automatically stuffs an extra '0' bit after every five consecutive '1' bits. The receiver detects any sequence of five 1s followed by a 0 and automatically strips the 0 bit."
                },
                {
                    "q": "Explain how Cyclic Redundancy Check (CRC) detects errors.",
                    "a": "Let data be D with length k and generator polynomial be G with degree r. 1. Sender appends r zeroes to D. 2. Sender performs modulo-2 binary division (using bitwise XOR without borrows) of padded D by G. 3. The r-bit remainder R is the CRC checksum. 4. Sender transmits (D + R). 5. Receiver divides the incoming frame by G. If remainder is 0, the frame is error-free; if non-zero, a transmission error occurred and the frame is dropped."
                },
                {
                    "q": "Compare Go-Back-N and Selective Repeat sliding window protocols.",
                    "a": "In Go-Back-N (GBN), the receiver accepts frames strictly in sequence and uses cumulative ACKs; if a frame is lost, all subsequent frames are dropped, forcing the sender to retransmit the entire window. In Selective Repeat (SR), the receiver maintains a receive window, accepts out-of-order frames, and sends individual ACKs; the sender retransmits only the single lost frame, saving bandwidth at the cost of receiver buffer memory."
                },
                {
                    "q": "Why must the window size in Selective Repeat be at most half the sequence number space (Ws <= 2^(k-1))?",
                    "a": "If window size exceeds 2^(k-1), an overlap occurs between the current sequence window and the next window. If all ACKs are lost, the sender retransmits old frames; the receiver cannot distinguish whether the incoming frame is a duplicate retransmission of an old frame or a brand-new frame from the next sequence cycle."
                },
                {
                    "q": "What is the Bandwidth-Delay Product (BDP) and why is it important?",
                    "a": "BDP = Bandwidth (bits/sec) * Round Trip Time (seconds). It represents the maximum volume of unacknowledged data in transit across the network pipe at any given instant. To achieve maximum throughput, the sliding window size must be at least equal to the BDP."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-16-01",
                    "question": "In HDLC framing, bit stuffing inserts a '0' bit after how many consecutive '1' bits?",
                    "options": ["4", "5", "6", "7"],
                    "correct_answer": "B",
                    "explanation": "Sender stuffs a 0 after 5 consecutive 1s to prevent collision with the flag pattern 01111110."
                },
                {
                    "id": "CS-16-02",
                    "question": "What mathematical operation is used in CRC modulo-2 arithmetic instead of standard subtraction?",
                    "options": ["AND", "OR", "XOR", "NOT"],
                    "correct_answer": "C",
                    "explanation": "Modulo-2 binary division uses bitwise XOR operations without borrowing."
                },
                {
                    "id": "CS-16-03",
                    "question": "If 3 bits are used for sequence numbers in Selective Repeat, what is the maximum sender window size?",
                    "options": ["8", "7", "4", "3"],
                    "correct_answer": "C",
                    "explanation": "Max window size in Selective Repeat is 2^(k-1) = 2^(3-1) = 4."
                },
                {
                    "id": "CS-16-04",
                    "question": "Which sliding window protocol buffers out-of-order frames at the receiver?",
                    "options": ["Stop-and-Wait", "Go-Back-N", "Selective Repeat", "Pure ALOHA"],
                    "correct_answer": "C",
                    "explanation": "Selective Repeat buffers out-of-order frames, whereas Go-Back-N discards them."
                },
                {
                    "id": "CS-16-05",
                    "question": "The frame check sequence (FCS) field in an Ethernet frame is computed using:",
                    "options": ["Simple Parity", "Hamming Code", "CRC-32", "MD5 Hash"],
                    "correct_answer": "C",
                    "explanation": "Ethernet Data Link frames utilize CRC-32 for error detection."
                }
            ]
        },

        17: {
            "subject": "Computer Networks",
            "topic": "Medium Access Control (MAC): CSMA/CD, CSMA/CA, Ethernet & Collision Handling",
            "concept_lesson": (
                "When multiple nodes share a single broadcast transmission medium, the Medium Access Control (MAC) sublayer manages "
                "channel allocation to prevent and resolve transmission collisions.\n\n"
                "Random Access Protocols Evolution:\n"
                "1. Pure ALOHA: Transmit whenever ready. Throughput max = 18.4% (vulnerable period = 2 * T_frame).\n"
                "2. Slotted ALOHA: Time divided into discrete slots equal to T_frame; transmit only at slot start. Throughput max = 36.8%.\n"
                "3. CSMA (Carrier Sense Multiple Access): 'Listen before talk'. Node senses channel before transmitting (1-persistent, p-persistent, non-persistent).\n\n"
                "CSMA/CD (Collision Detection — Ethernet IEEE 802.3):\n"
                "'Listen while talk'. Sender continuously monitors medium while transmitting. If signal energy exceeds threshold (collision), "
                "the sender immediately aborts transmission, broadcasts a 32-bit Jam Signal to notify all nodes, and waits for a backoff period.\n"
                "- Exponential Backoff Algorithm: After collision k (capped at 10), pick random r in [0, 2^k - 1]; wait r * 51.2 microseconds. "
                "After 16 collisions, abort.\n"
                "- Minimum Frame Size Rule: Frame transmission time must be >= 2 * propagation delay (T_tx >= 2 * T_prop) so sender is still transmitting "
                "when the collision echo returns. In standard 10Mbps Ethernet, min frame size is 64 bytes (512 bits).\n\n"
                "CSMA/CA (Collision Avoidance — Wi-Fi IEEE 802.11):\n"
                "Wireless transceivers cannot transmit and listen simultaneously (transmitted power drowns out received signals). "
                "Uses Interframe Spaces (DIFS, SIFS) and optional RTS/CTS (Request-to-Send / Clear-to-Send) handshakes to solve the Hidden Terminal Problem."
            ),
            "key_definitions": [
                {"term": "CSMA/CD", "definition": "Carrier Sense Multiple Access with Collision Detection: protocol detecting collisions by monitoring energy on wire."},
                {"term": "Exponential Backoff", "definition": "An algorithm multiplying random collision wait intervals to prevent repeated simultaneous retries."},
                {"term": "Hidden Terminal Problem", "definition": "A wireless state where two nodes cannot sense each other but collide at a shared central access point."}
            ],
            "interview_questions": [
                {
                    "q": "Why does Ethernet require a Minimum Frame Size of 64 bytes in CSMA/CD?",
                    "a": "For CSMA/CD to work, the transmitting station must still be transmitting its frame when a collision notification returns from the furthest point on the network. Mathematically, Transmission Time (T_tx) >= 2 * Propagation Delay (T_prop). For 10Mbps Ethernet over a 2.5km collision domain, round-trip time is ~51.2 microseconds. In 51.2 microseconds at 10Mbps, 512 bits (64 bytes) are transmitted. Any frame smaller than 64 bytes could finish before a collision arrives, violating collision detection."
                },
                {
                    "q": "How does Binary Exponential Backoff resolve repeat collisions?",
                    "a": "After the k-th collision, the node chooses a random slot wait time r from the range [0, 2^k - 1] (k is capped at 10). The wait duration is r * slot_time (51.2 microseconds). As collisions repeat, the contention window expands exponentially (1, 2, 4, 8, ... up to 1024), dynamically spreading competing nodes across wider intervals and dramatically reducing re-collision probability."
                },
                {
                    "q": "Why is CSMA/CD not used in wireless Wi-Fi networks?",
                    "a": "In wireless transmission, the transmitted signal from an antenna is millions of times stronger than incoming signals from distant nodes. A wireless radio's own transmission blinds its receiver, making hardware collision detection impossible. Wireless networks instead use CSMA/CA (Collision Avoidance) with RTS/CTS."
                },
                {
                    "q": "Explain the Hidden Terminal Problem and how RTS/CTS resolves it.",
                    "a": "Node A and Node C are both in range of Access Point B, but out of radio range of each other. A senses the channel, detects silence, and transmits to B. Simultaneously, C senses the channel, detects silence, and transmits to B. Their transmissions collide at B. Solved via RTS/CTS: A sends Request-To-Send to B; B broadcasts Clear-To-Send (CTS) containing transmission duration. Node C overhears B's CTS and silences its transmitter."
                },
                {
                    "q": "What is the difference between a Hub, a Switch, and a Router regarding collision and broadcast domains?",
                    "a": "A Hub (Layer 1) has 1 collision domain and 1 broadcast domain across all ports. A Switch (Layer 2) creates a dedicated collision domain per port, but maintains 1 unified broadcast domain. A Router (Layer 3) creates separate collision domains per port AND separates broadcast domains, preventing broadcast packet propagation between subnets."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-17-01",
                    "question": "What is the minimum frame size in standard 10Mbps Ethernet to guarantee collision detection?",
                    "options": ["32 bytes", "64 bytes", "128 bytes", "512 bytes"],
                    "correct_answer": "B",
                    "explanation": "Standard Ethernet mandates a 64-byte (512-bit) minimum frame size."
                },
                {
                    "id": "CS-17-02",
                    "question": "In CSMA/CD, the condition ensuring a sender detects collision before finishing transmission is:",
                    "options": ["T_tx >= T_prop", "T_tx >= 2 * T_prop", "T_prop >= 2 * T_tx", "T_tx = 0"],
                    "correct_answer": "B",
                    "explanation": "Transmission time must exceed two times propagation delay to detect worst-case collision echo."
                },
                {
                    "id": "CS-17-03",
                    "question": "The mechanism used in IEEE 802.11 Wi-Fi to solve the Hidden Terminal problem is:",
                    "options": ["Token Ring passing", "RTS/CTS handshake", "CSMA/CD Jam signals", "CRC-32 checksums"],
                    "correct_answer": "B",
                    "explanation": "RTS/CTS reservations inform hidden nodes to defer transmission."
                },
                {
                    "id": "CS-17-04",
                    "question": "How many collision domains does an 8-port Ethernet Layer-2 Switch have?",
                    "options": ["1", "2", "8", "0"],
                    "correct_answer": "C",
                    "explanation": "Each switch port represents an isolated collision domain, so an 8-port switch has 8."
                },
                {
                    "id": "CS-17-05",
                    "question": "In the Binary Exponential Backoff algorithm, after 3 consecutive collisions, the random multiplier r is chosen from:",
                    "options": ["0 to 3", "0 to 7", "0 to 15", "0 to 8"],
                    "correct_answer": "B",
                    "explanation": "Range is [0, 2^k - 1] = [0, 2^3 - 1] = [0, 7]."
                }
            ]
        },

        18: {
            "subject": "Computer Networks",
            "topic": "Network Layer: IPv4 Addressing, CIDR Subnetting, ARP, ICMP & NAT",
            "concept_lesson": (
                "The Network Layer is responsible for host-to-host packet routing and logical IP addressing across internetworks.\n\n"
                "IPv4 Addressing & CIDR:\n"
                "IPv4 uses 32-bit addresses (4 octets). Historically divided into Classes: Class A (/8, 0.0.0.0 to 127.255.255.255), "
                "Class B (/16, 128.0.0.0 to 191.255.255.255), Class C (/24, 192.0.0.0 to 223.255.255.255), Class D (Multicast), Class E (Reserved).\n"
                "Classless Inter-Domain Routing (CIDR) replaced classful networks: an address is written as IP/prefix (e.g., 192.168.1.0/26). "
                "Prefix bits denote Network ID; remaining (32 - prefix) bits denote Host ID. "
                "Usable hosts = 2^(32 - prefix) - 2 (subtracting Network Address where host bits are all 0s, and Broadcast Address where host bits are all 1s).\n\n"
                "Auxiliary Protocols:\n"
                "- ARP (Address Resolution Protocol): Resolves a known 32-bit IPv4 address to a 48-bit physical MAC address. Broadcasts ARP Request ('Who has IP X?'); "
                "target replies with Unicast ARP Reply containing its MAC.\n"
                "- ICMP (Internet Control Message Protocol): Diagnostics and error reporting (Ping uses Echo Request/Reply; Traceroute uses ICMP Time Exceeded when TTL expires).\n"
                "- NAT (Network Address Translation): Translates private IP addresses (RFC 1918: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) into public routable IPs, "
                "using Port Address Translation (PAT/NAPT) to multiplex thousands of internal hosts over a single public IP."
            ),
            "key_definitions": [
                {"term": "CIDR", "definition": "Classless Inter-Domain Routing: variable-length subnet masking allowing flexible IP allocation without rigid class boundaries."},
                {"term": "ARP", "definition": "Address Resolution Protocol: translates logical IPv4 addresses to local hardware MAC addresses via broadcast/unicast."},
                {"term": "NAT", "definition": "Network Address Translation: mapping private RFC 1918 addresses to public routable IP addresses to conserve IPv4 space."}
            ],
            "interview_questions": [
                {
                    "q": "Given the IP address 172.16.10.45/28, find the Network Address, Broadcast Address, and number of usable host addresses.",
                    "a": "Prefix is /28. Host bits = 32 - 28 = 4 bits. Block size = 2^4 = 16. In the 4th octet, 45 falls into the block [32 to 47]. Network Address = 172.16.10.32. Broadcast Address = 172.16.10.47. Usable Host range = 172.16.10.33 to 172.16.10.46. Number of usable hosts = 2^4 - 2 = 14 hosts."
                },
                {
                    "q": "How does Traceroute work under the hood using IP TTL and ICMP?",
                    "a": "Traceroute sends packets (UDP or ICMP) starting with IP Time-To-Live TTL = 1. The first router decrements TTL to 0, drops the packet, and returns an ICMP Type 11 'Time-to-Live Exceeded' message; traceroute records the router's IP and round-trip time. It then sends a packet with TTL = 2 to discover the second router, incrementing TTL sequentially until the packet reaches the destination, which responds with ICMP Echo Reply or Port Unreachable."
                },
                {
                    "q": "What is the difference between ARP and RARP?",
                    "a": "ARP (Address Resolution Protocol) resolves a known logical IP address to an unknown physical hardware MAC address. RARP (Reverse ARP) allowed a diskless workstation that knows only its physical MAC address to request and discover its assigned IP address from a central server on boot (now superseded by DHCP)."
                },
                {
                    "q": "What are RFC 1918 Private IP ranges and why can't they be routed on the public Internet?",
                    "a": "The three private ranges are: 10.0.0.0/8 (10.0.0.0 - 10.255.255.255), 172.16.0.0/12 (172.16.0.0 - 172.31.255.255), and 192.168.0.0/16 (192.168.0.0 - 192.168.255.255). Public Internet backbone routers are configured to drop packets with private destination addresses because they are reused across millions of internal private LANs globally and lack globally unique routing paths."
                },
                {
                    "q": "How does Port Address Translation (PAT / NAT Overload) allow multiple devices to share one public IP?",
                    "a": "The NAT router maintains a stateful translation table: (Private IP, Private Port <-> Public IP, Translated Port). When an internal host (192.168.1.10:5000) requests an external site, the router rewrites the source IP to its public IP and assigns a unique temporary source port (203.0.113.1:40001). When the response arrives at port 40001, the router matches the entry in its table and forwards the packet back to 192.168.1.10:5000."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-18-01",
                    "question": "How many usable host IP addresses are available in a /26 subnet?",
                    "options": ["64", "62", "30", "126"],
                    "correct_answer": "B",
                    "explanation": "Host bits = 32 - 26 = 6 bits. Usable hosts = 2^6 - 2 = 64 - 2 = 62."
                },
                {
                    "id": "CS-18-02",
                    "question": "Which protocol resolves an IPv4 address to a physical MAC address on a local Ethernet segment?",
                    "options": ["DNS", "DHCP", "ARP", "BGP"],
                    "correct_answer": "C",
                    "explanation": "ARP maps 32-bit IP addresses to 48-bit MAC addresses."
                },
                {
                    "id": "CS-18-03",
                    "question": "Traceroute discovers intermediate routers along a network path by manipulating which IP header field?",
                    "options": ["Header Checksum", "Time To Live (TTL)", "Type of Service", "Identification"],
                    "correct_answer": "B",
                    "explanation": "Traceroute increments TTL from 1 upward, receiving ICMP Time Exceeded packets from each hop."
                },
                {
                    "id": "CS-18-04",
                    "question": "Which of the following is an RFC 1918 Private IP address?",
                    "options": ["8.8.8.8", "172.20.14.5", "169.254.1.1", "203.0.113.50"],
                    "correct_answer": "B",
                    "explanation": "172.20.14.5 falls within the private Class B range (172.16.0.0 to 172.31.255.255)."
                },
                {
                    "id": "CS-18-05",
                    "question": "What is the broadcast address for the subnet 192.168.5.0/24?",
                    "options": ["192.168.5.0", "192.168.5.1", "192.168.5.255", "192.168.5.254"],
                    "correct_answer": "C",
                    "explanation": "In a /24 subnet, setting all 8 host bits to 1 yields .255, the broadcast address."
                }
            ]
        },

        19: {
            "subject": "Computer Networks",
            "topic": "Routing Algorithms: Distance Vector (RIP), Link State (OSPF) & BGP",
            "concept_lesson": (
                "Routing is the process by which intermediate routers select optimal paths through interconnected networks to forward packets.\n\n"
                "Intra-Domain vs Inter-Domain Routing:\n"
                "- Autonomous System (AS): A collection of networks and routers under a single administrative domain.\n"
                "- Interior Gateway Protocols (IGP): Route within an AS (RIP, OSPF).\n"
                "- Exterior Gateway Protocols (EGP): Route between different ASes across the global Internet (BGP).\n\n"
                "Distance Vector Routing (RIP — Bellman-Ford Algorithm):\n"
                "Each router maintains a vector: (Destination, Cost, Next Hop). Routers periodically share their entire routing table only with "
                "immediate neighbors. Distance = hop count (max 15 hops; 16 = infinity). Suffers from the Count-to-Infinity Problem when a link fails, "
                "mitigated using Split Horizon (never advertise a route back out the interface it was learned from) and Poison Reverse.\n\n"
                "Link State Routing (OSPF — Dijkstra's Shortest Path Algorithm):\n"
                "Routers discover neighbors via Hello packets, construct Link State Advertisements (LSAs) containing link costs to neighbors, "
                "and flood LSAs to EVERY router in the domain via reliable flooding. Every router builds an identical complete topology map of the AS, "
                "then independently executes Dijkstra's algorithm to compute the shortest-path forwarding table. Ultra-fast convergence with zero count-to-infinity.\n\n"
                "Border Gateway Protocol (BGP-4):\n"
                "Path Vector protocol governing global Internet transit. Advertises full AS-Paths (e.g., Prefix 1.2.3.0/24 reachable via AS 100 -> AS 200 -> AS 300) "
                "to completely eliminate routing loops. Routing decisions are based on business and peering policies rather than pure hop counts."
            ),
            "key_definitions": [
                {"term": "Distance Vector", "definition": "A routing algorithm where nodes periodically share routing tables with immediate neighbors using Bellman-Ford."},
                {"term": "Link State", "definition": "A routing protocol where nodes flood link states to all routers and compute shortest paths using Dijkstra's algorithm."},
                {"term": "Count-to-Infinity", "definition": "A routing failure in distance vector where neighbor routers endlessly increment hop counts on broken links."}
            ],
            "interview_questions": [
                {
                    "q": "What is the Count-to-Infinity problem in RIP, and how do Split Horizon and Poison Reverse resolve it?",
                    "a": "When a link to destination X fails, router A marks distance to X as infinite. However, neighbor B previously advertised a route to X through A with cost 2. A thinks B has an alternate path and updates its cost to 3; B updates to 4, bouncing back and forth until reaching infinity (16 hops). Split Horizon prevents this by forbidding a router from advertising a learned route back out the same interface it arrived on. Poison Reverse sets the cost of that reversed route explicitly to infinity (16), immediately neutralizing loop formation."
                },
                {
                    "q": "Why does OSPF converge significantly faster than RIP?",
                    "a": "In OSPF, when a link state changes, an LSA is immediately flooded across the entire network, and each router independently recalculates its shortest path tree using Dijkstra's algorithm. In RIP, routers must wait for periodic timer intervals (30s) to slowly propagate distance vectors hop-by-hop through neighbors, leading to slow convergence and transient routing loops."
                },
                {
                    "q": "What is the difference between an Interior Gateway Protocol (IGP) and an Exterior Gateway Protocol (EGP)?",
                    "a": "IGPs (like OSPF and RIP) operate inside a single autonomous organization's network domain, focusing on optimizing technical metrics like path latency, bandwidth, and hop count. EGPs (like BGP) operate between distinct Internet Service Providers and autonomous systems, where routing choices are governed by commercial peering contracts, geopolitical transit rules, and administrative policy rather than lowest cost."
                },
                {
                    "q": "How does BGP prevent routing loops across the global Internet?",
                    "a": "BGP is a Path-Vector protocol. When an AS advertises a route to a BGP neighbor, it prepends its own Autonomous System Number (ASN) to the AS-Path attribute list. When a router receives a BGP advertisement, it checks the AS-Path list: if its own ASN is already present, it rejects the advertisement immediately, mathematically preventing routing loops across autonomous domains."
                },
                {
                    "q": "Explain Dijkstra's shortest path algorithm used in OSPF.",
                    "a": "Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge costs. It maintains a set of visited vertices and a priority queue of candidate vertices ordered by distance from source. In each iteration, it extracts the unvisited vertex with minimal tentative distance, marks it visited, and relaxes all outgoing edges to adjacent unvisited neighbors. It terminates when all vertices are visited in O((V + E) log V) time."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-19-01",
                    "question": "Which algorithm is used by OSPF to compute shortest path routing tables?",
                    "options": ["Bellman-Ford", "Dijkstra's Algorithm", "Floyd-Warshall", "Prim's Algorithm"],
                    "correct_answer": "B",
                    "explanation": "OSPF runs Dijkstra's shortest path algorithm on its link-state database."
                },
                {
                    "id": "CS-19-02",
                    "question": "What is considered 'infinity' (unreachable distance) in the Routing Information Protocol (RIP)?",
                    "options": ["10 hops", "15 hops", "16 hops", "255 hops"],
                    "correct_answer": "C",
                    "explanation": "RIP caps valid hop counts at 15; a hop count of 16 signifies an unreachable destination."
                },
                {
                    "id": "CS-19-03",
                    "question": "The primary protocol responsible for routing traffic between different Autonomous Systems on the global Internet is:",
                    "options": ["RIP", "OSPF", "BGP", "ICMP"],
                    "correct_answer": "C",
                    "explanation": "BGP (Border Gateway Protocol) is the de facto inter-domain routing protocol of the Internet."
                },
                {
                    "id": "CS-19-04",
                    "question": "Split Horizon is a technique designed to prevent:",
                    "options": ["Buffer overflow", "Count-to-Infinity routing loops in Distance Vector protocols", "Packet collisions in CSMA", "SYN flood attacks"],
                    "correct_answer": "B",
                    "explanation": "Split Horizon stops a router from advertising routes back out the interface they were learned from."
                },
                {
                    "id": "CS-19-05",
                    "question": "BGP avoids routing loops by examining which route attribute?",
                    "options": ["Next Hop IP", "AS-Path list", "Subnet Mask", "Metric Cost"],
                    "correct_answer": "B",
                    "explanation": "If a router detects its own ASN inside the incoming AS-Path attribute, it drops the route to prevent loops."
                }
            ]
        },

        20: {
            "subject": "Computer Networks",
            "topic": "Transport Layer: TCP vs UDP, 3-Way Handshake & 4-Way Connection Teardown",
            "concept_lesson": (
                "The Transport Layer delivers process-to-process communication using 16-bit Port numbers.\n\n"
                "TCP (Transmission Control Protocol) vs UDP (User Datagram Protocol):\n"
                "- TCP: Connection-oriented, reliable byte stream. Provides ordered delivery, retransmission of lost segments, flow control, "
                "and congestion control. Header size: 20 to 60 bytes. (Used by HTTP, HTTPS, SSH, SMTP, FTP).\n"
                "- UDP: Connectionless, unreliable datagrams. Zero handshake overhead, no retransmissions, no flow control, minimal 8-byte header. "
                "Provides fast delivery with low latency. (Used by DNS, DHCP, VoIP, video streaming, online gaming, WebRTC).\n\n"
                "TCP 3-Way Handshake (Connection Establishment):\n"
                "1. Client -> Server: SYN (seq = client_isn).\n"
                "2. Server -> Client: SYN-ACK (seq = server_isn, ack = client_isn + 1).\n"
                "3. Client -> Server: ACK (seq = client_isn + 1, ack = server_isn + 1). (Data payload may now be transmitted).\n\n"
                "TCP 4-Way Teardown (Connection Termination):\n"
                "TCP connections are full-duplex and must be closed independently in each direction:\n"
                "1. Client -> Server: FIN (seq = u). Client enters FIN_WAIT_1.\n"
                "2. Server -> Client: ACK (ack = u + 1). Server enters CLOSE_WAIT; Client enters FIN_WAIT_2.\n"
                "3. Server -> Client: FIN (seq = v). Server enters LAST_ACK.\n"
                "4. Client -> Server: ACK (ack = v + 1). Client enters TIME_WAIT (waits 2 * MSL, ~120s), ensuring final ACK arrived and flushing old packets. Server closes."
            ),
            "key_definitions": [
                {"term": "3-Way Handshake", "definition": "The TCP synchronization process (SYN, SYN-ACK, ACK) negotiating initial sequence numbers before data exchange."},
                {"term": "TIME_WAIT State", "definition": "A 2 * MSL client wait period following teardown to guarantee final ACK delivery and prevent duplicate segment confusion."},
                {"term": "Full-Duplex", "definition": "Simultaneous bidirectional transmission capability over a single logical communication connection."}
            ],
            "interview_questions": [
                {
                    "q": "Walk through the TCP 3-Way Handshake and explain why 2 handshakes are insufficient.",
                    "a": "1. Client sends SYN with random Initial Sequence Number (ISN_c). 2. Server replies with SYN-ACK, acknowledging ISN_c + 1 and presenting its own ISN_s. 3. Client replies with ACK for ISN_s + 1. Two handshakes are insufficient because the client must acknowledge the server's sequence number; without the 3rd step, a delayed duplicate SYN from an old dead connection arriving at the server would cause the server to allocate resources and assume an active connection, resulting in half-open phantom connections."
                },
                {
                    "q": "Why is TCP connection termination a 4-way exchange instead of a 3-way exchange?",
                    "a": "TCP is a full-duplex protocol: both directions of data flow are independent. When the client sends FIN, it signals that it has no more data to send, but it can still receive data. The server acknowledges with an ACK, entering CLOSE_WAIT. The server may still have pending outbound buffers to transmit. Once the server finishes sending all remaining data, it sends its own separate FIN, which the client acknowledges."
                },
                {
                    "q": "What is the purpose of the TIME_WAIT state in TCP, and how long does it last?",
                    "a": "The endpoint that actively initiates connection close enters TIME_WAIT after sending its final ACK. It lasts for 2 * Maximum Segment Lifetime (2 * MSL, typically 1 to 2 minutes). It serves two critical functions: 1) Guarantees that the final ACK was received by the peer (if lost, the peer retransmits FIN, which can still be ACKed), and 2) Allows all lingering duplicate segments in the network to expire before the same IP:port pair is reused for a new connection."
                },
                {
                    "q": "What is a SYN Flood attack and how do SYN Cookies mitigate it?",
                    "a": "An attacker floods a server with thousands of TCP SYN packets with spoofed source IPs, ignoring the SYN-ACK responses. The server allocates TCB state memory in its listen backlog queue for each half-open connection until memory is exhausted, denying legitimate clients. SYN Cookies mitigate this by eliminating server state allocation during handshake: the server encodes connection parameters cryptographically into the SYN-ACK Initial Sequence Number; memory state is allocated only when the client returns a valid ACK."
                },
                {
                    "q": "Why does DNS use UDP for queries but TCP for Zone Transfers?",
                    "a": "Standard DNS queries are small, single-packet requests where UDP provides ultra-low latency without handshake delays. If a UDP query packet drops, the client simply re-queries after a timeout. However, DNS Zone Transfers (synchronizing full zone files between primary and secondary nameservers) transmit large, multi-megabyte payloads requiring reliable ordered delivery, making TCP mandatory."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-20-01",
                    "question": "What is the minimum header size of a standard TCP segment (without options)?",
                    "options": ["8 bytes", "20 bytes", "32 bytes", "64 bytes"],
                    "correct_answer": "B",
                    "explanation": "Standard TCP headers without options are 20 bytes; UDP headers are 8 bytes."
                },
                {
                    "id": "CS-20-02",
                    "question": "During TCP connection teardown, why does the active closer remain in the TIME_WAIT state for 2 * MSL?",
                    "options": ["To recalculate window size", "To ensure the final ACK was received and allow duplicate packets to die out", "To download pending files", "To reset the B+ tree"],
                    "correct_answer": "B",
                    "explanation": "2 * MSL wait allows lingering delayed segments to expire and guarantees final ACK delivery."
                },
                {
                    "id": "CS-20-03",
                    "question": "Which protocol is connectionless and does not provide reliability, ordering, or flow control?",
                    "options": ["TCP", "UDP", "SCTP", "BGP"],
                    "correct_answer": "B",
                    "explanation": "UDP is connectionless and does not guarantee delivery or packet order."
                },
                {
                    "id": "CS-20-04",
                    "question": "What security mechanism mitigates SYN Flood Denial-of-Service attacks without consuming server state memory?",
                    "options": ["DHCP Snooping", "SYN Cookies", "Split Horizon", "Exponential Backoff"],
                    "correct_answer": "B",
                    "explanation": "SYN Cookies encode connection state in the initial sequence number, deferring memory allocation until final ACK."
                },
                {
                    "id": "CS-20-05",
                    "question": "What flags are set in the second packet of the TCP 3-Way Handshake?",
                    "options": ["SYN", "ACK", "SYN + ACK", "FIN + ACK"],
                    "correct_answer": "C",
                    "explanation": "The server responds to SYN with a combined SYN + ACK packet."
                }
            ]
        },

        21: {
            "subject": "Computer Networks",
            "topic": "TCP Congestion Control & Flow Control: Sliding Window, Slow Start & Fast Recovery",
            "concept_lesson": (
                "TCP employs distinct mechanisms for Flow Control (protecting the receiver from being overwhelmed) and Congestion Control "
                "(protecting intermediate network routers from buffer collapse).\n\n"
                "Flow Control (Receiver Window — rwnd):\n"
                "The receiver advertises its available buffer space in the 16-bit 'Window Size' field of every TCP ACK. "
                "The sender is strictly constrained: Effective Window = min(rwnd, cwnd). If rwnd drops to 0, sender stops transmitting "
                "and starts a Persist Timer, periodically sending 1-byte Window Probes to detect when the receiver's buffer reopens.\n\n"
                "Congestion Control (Congestion Window — cwnd):\n"
                "Managed dynamically by sender algorithms based on perceived network packet loss:\n"
                "1. Slow Start: cwnd starts at 1 MSS (or initial 10 MSS). For EVERY received ACK, cwnd increments by 1 MSS (exponential growth: 1 -> 2 -> 4 -> 8 MSS). "
                "Continues until cwnd reaches Slow Start Threshold (ssthresh).\n"
                "2. Congestion Avoidance: Once cwnd >= ssthresh, growth shifts to linear: cwnd increases by 1 MSS per Round Trip Time (Additive Increase).\n"
                "3. Multiplicative Decrease:\n"
                "- On Triple Duplicate ACKs (Mild Congestion): Fast Retransmit immediately sends the missing segment without waiting for RTO timer. "
                "ssthresh is set to cwnd / 2, cwnd is set to ssthresh + 3 MSS, and Fast Recovery begins (AIMD: Additive Increase, Multiplicative Decrease).\n"
                "- On Retransmission Timeout (Severe Congestion): ssthresh = cwnd / 2, cwnd collapses to 1 MSS, and execution resets to Slow Start."
            ),
            "key_definitions": [
                {"term": "Flow Control", "definition": "Receiver-driven mechanism matching transmission rate to receiver buffer capacity using rwnd."},
                {"term": "Congestion Control", "definition": "Network-driven mechanism matching transmission rate to intermediate router bandwidth using cwnd."},
                {"term": "Fast Retransmit", "definition": "Retransmitting a lost segment upon receiving 3 duplicate ACKs without waiting for timeout expiration."}
            ],
            "interview_questions": [
                {
                    "q": "What is the critical difference between Flow Control and Congestion Control in TCP?",
                    "a": "Flow Control is an end-to-end mechanism between sender and receiver; it prevents a fast sender from overflowing a slow receiver's local buffer, enforced via the receiver's advertised window (rwnd). Congestion Control is a global mechanism between sender and intermediate network routers; it prevents senders from injecting more traffic than network links and router buffers can handle, enforced via the congestion window (cwnd). Sender transmission limit = min(rwnd, cwnd)."
                },
                {
                    "q": "Why does Slow Start grow exponentially if it is called 'Slow' Start?",
                    "a": "It is called 'Slow' only in comparison to blasting the entire receiver window at full line rate upon connection startup (which would instantly cause router buffer overflows). It starts at 1 MSS, but because cwnd increments by 1 for every ACK received, the window doubles every RTT (1 -> 2 -> 4 -> 8 -> 16 MSS), producing rapid exponential ramp-up until reaching ssthresh."
                },
                {
                    "q": "How does TCP Fast Retransmit identify packet loss before the Retransmission Timeout (RTO) expires?",
                    "a": "When a segment is lost in transit but subsequent segments arrive, the receiver sends duplicate ACKs repeating the exact sequence number of the missing byte for each out-of-order segment received. When the sender receives 3 Duplicate ACKs (total 4 identical ACKs), it treats this as proof that the packet was lost rather than delayed, and retransmits the missing segment immediately without waiting for the slow RTO timer to expire."
                },
                {
                    "q": "What happens to cwnd and ssthresh when a retransmission timeout (RTO) occurs?",
                    "a": "An RTO indicates severe network congestion or link failure. The sender: 1) Sets ssthresh = cwnd / 2 (halving the threshold), 2) Collapses cwnd back down to 1 MSS, and 3) Restarts from the Slow Start phase, slowly probing available network bandwidth again."
                },
                {
                    "q": "What is the Silly Window Syndrome and how does Nagle's Algorithm address it on the sender side?",
                    "a": "Silly Window Syndrome occurs when data is exchanged in tiny 1-byte increments (e.g., Telnet keystrokes), causing massive 40-byte TCP/IP header overhead per byte of data. Nagle's Algorithm solves this on the sender: if a small chunk of data is ready to send, transmit it only if there is no unacknowledged in-flight data; otherwise, buffer outgoing bytes until either a full MSS accumulates or all previous in-flight packets are ACKed."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-21-01",
                    "question": "During TCP Slow Start, how does the congestion window (cwnd) increase with each passing RTT?",
                    "options": ["Linearly (by 1 MSS)", "Exponentially (doubles every RTT)", "Logarithmically", "Remains constant"],
                    "correct_answer": "B",
                    "explanation": "Because cwnd increases by 1 for each ACK, it doubles every round trip time during slow start."
                },
                {
                    "id": "CS-21-02",
                    "question": "How many duplicate ACKs must a TCP sender receive before triggering Fast Retransmit?",
                    "options": ["1", "2", "3", "5"],
                    "correct_answer": "C",
                    "explanation": "Receiving 3 duplicate ACKs (4 identical ACKs total) triggers immediate Fast Retransmit."
                },
                {
                    "id": "CS-21-03",
                    "question": "The maximum data a TCP sender can transmit without receiving an ACK is bounded by:",
                    "options": ["rwnd only", "cwnd only", "min(rwnd, cwnd)", "max(rwnd, cwnd)"],
                    "correct_answer": "C",
                    "explanation": "Effective window is strictly bounded by min(rwnd, cwnd) to respect both receiver and network."
                },
                {
                    "id": "CS-21-04",
                    "question": "When a packet loss occurs due to an RTO timeout, what value is cwnd reset to?",
                    "options": ["ssthresh", "cwnd / 2", "1 MSS", "0 MSS"],
                    "correct_answer": "C",
                    "explanation": "On a severe timeout, cwnd collapses down to 1 MSS, restarting slow start."
                },
                {
                    "id": "CS-21-05",
                    "question": "Nagle's algorithm on the sender side is designed to prevent:",
                    "options": ["SYN Flood attacks", "Silly Window Syndrome from transmitting tiny data packets", "B+ tree page splits", "Deadlocks in 2PL"],
                    "correct_answer": "B",
                    "explanation": "Nagle's algorithm coalesces small packets to prevent Silly Window Syndrome."
                }
            ]
        },

        # --- DAYS 22-26: PYTHON INTERNALS & ADVANCED PROGRAMMING ---
        22: {
            "subject": "Python Internals",
            "topic": "Python Memory Model: Reference Counting, Generational Garbage Collection & Object Model",
            "concept_lesson": (
                "In CPython, EVERYTHING is an object—integers, strings, functions, classes, and modules all allocate a PyObject structure.\n\n"
                "PyObject Structure:\n"
                "Defined in CPython C headers (`object.h`), every PyObject contains:\n"
                "1. `ob_refcnt`: 64-bit integer tracking active references pointing to this object.\n"
                "2. `ob_type`: Pointer to the object's type descriptor (`PyTypeObject`), which defines behavior, method tables, and memory size.\n"
                "Variable-length objects (like strings, lists, dicts) use `PyVarObject`, adding an `ob_size` field.\n\n"
                "Memory Management & Garbage Collection:\n"
                "- Primary Mechanism (Reference Counting): When an object's reference count drops to 0, its memory is deallocated INSTANTLY. "
                "Incremented on variable assignment, passing to function, or appending to container. Decremented on `del`, scope exit, or overwriting.\n"
                "- Cyclical Garbage Collection (The `gc` module):\n"
                "Reference counting CANNOT reclaim self-referencing reference cycles (e.g., `a.child = b; b.parent = a; del a; del b`). "
                "CPython adds a cyclic garbage collector using three Generations (Gen 0, Gen 1, Gen 2). "
                "New objects enter Gen 0. If they survive a GC cycle, they are promoted to Gen 1, then Gen 2 (Generation Hypothesis: most objects die young). "
                "The cyclic GC traverses container object pointers, identifies isolated subgraphs whose external reference count is 0, and frees them.\n\n"
                "Small Object Allocator (PyMalloc):\n"
                "CPython allocates small memory blocks (<= 512 bytes) using a dedicated 3-tier memory pool (Arenas = 256KB, Pools = 4KB, Blocks = 8 to 512 bytes) "
                "to avoid kernel `malloc()` overhead and mitigate OS-level fragmentation."
            ),
            "key_definitions": [
                {"term": "PyObject", "definition": "The foundational C structure in CPython containing reference count and type pointer for every Python object."},
                {"term": "Reference Counting", "definition": "Primary memory management strategy reclaiming memory immediately when reference count reaches zero."},
                {"term": "Cyclic GC", "definition": "A 3-generational collector detecting and breaking isolated circular reference loops between container objects."}
            ],
            "interview_questions": [
                {
                    "q": "Explain how CPython's memory management handles circular references.",
                    "a": "Reference counting cannot collect circular references (e.g., two objects pointing to each other) because their reference counts never drop to zero. CPython solves this using a generational cyclic garbage collector (gc module). It tracks container objects (lists, dicts, custom classes), temporarily isolates their internal reference counts, decrements references within the subgraph, and identifies object groups with zero external incoming references. These unreachable subgraphs are then deallocated."
                },
                {
                    "q": "What is the Generational Hypothesis in garbage collection?",
                    "a": "The Generational Hypothesis observes that in almost all software systems, the vast majority of allocated objects are short-lived (e.g., local variables in function scopes) and die shortly after creation. CPython divides objects into 3 generations (0, 1, 2). Gen 0 is scanned frequently for quick collection; long-surviving objects are promoted to Gen 1 and Gen 2, which are scanned much less frequently, minimizing CPU overhead."
                },
                {
                    "q": "What is PyMalloc and why doesn't Python return all freed memory back to the operating system immediately?",
                    "a": "PyMalloc is CPython's custom memory allocator for objects <= 512 bytes, organizing memory into Arenas (256KB) and Pools (4KB). When Python objects are freed, memory is returned to the pool for reuse by future Python allocations rather than releasing it to the OS kernel via free(). The OS only reclaims memory when an entire 256KB arena becomes completely empty."
                },
                {
                    "q": "Why is `is` different from `==` in Python, and how does integer interning work?",
                    "a": "`==` checks for value equality (invoking `__eq__`), comparing whether two objects contain the same data. `is` checks for object identity (comparing memory addresses, `id(a) == id(b)`). CPython pre-allocates and interns small integers in the range [-5, 256] globally at startup. For integers in this range, `a = 10; b = 10; a is b` evaluates to True because both variables point to the exact same pre-allocated singleton PyObject in memory."
                },
                {
                    "q": "What are `__slots__` in Python classes and how do they optimize memory?",
                    "a": "By default, every Python instance stores its attributes in a dynamic dictionary (`self.__dict__`), which incurs substantial hash table memory overhead (~150-200 bytes per instance). Specifying `__slots__ = ('name', 'age')` in a class prevents the creation of `__dict__` and allocates a compact, fixed-size C array of attribute pointers, reducing memory consumption by over 60% when instantiating millions of objects."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-22-01",
                    "question": "What is the primary, real-time memory management mechanism in standard CPython?",
                    "options": ["Mark and Sweep GC", "Reference Counting", "Manual free() calls", "Stop-the-World Tracing"],
                    "correct_answer": "B",
                    "explanation": "CPython uses reference counting as its immediate real-time memory reclamation mechanism."
                },
                {
                    "id": "CS-22-02",
                    "question": "Which range of integer values is pre-allocated and interned as global singletons in CPython?",
                    "options": ["0 to 100", "-128 to 127", "-5 to 256", "0 to 65535"],
                    "correct_answer": "C",
                    "explanation": "CPython interns small integers between -5 and 256 inclusive."
                },
                {
                    "id": "CS-22-03",
                    "question": "Defining `__slots__` on a Python class achieves memory optimization by:",
                    "options": ["Bypassing the GIL", "Preventing the creation of the dynamic `__dict__` attribute dictionary", "Compressing strings using gzip", "Converting integers to C floats"],
                    "correct_answer": "B",
                    "explanation": "`__slots__` eliminates instance `__dict__` overhead, using fixed-size C arrays instead."
                },
                {
                    "id": "CS-22-04",
                    "question": "Circular reference cycles that escape reference counting are detected and collected by:",
                    "options": ["PyMalloc", "The generational cyclic garbage collector (`gc` module)", "The OS kernel scheduler", "The Global Interpreter Lock"],
                    "correct_answer": "B",
                    "explanation": "The cyclic garbage collector specifically identifies and breaks isolated circular reference cycles."
                },
                {
                    "id": "CS-22-05",
                    "question": "In Python, which operator evaluates to True only if both variables reference the identical memory address?",
                    "options": ["==", "!=", "is", "in"],
                    "correct_answer": "C",
                    "explanation": "The `is` keyword checks pointer identity (`id(a) == id(b)`)."
                }
            ]
        },

        23: {
            "subject": "Python Internals",
            "topic": "Global Interpreter Lock (GIL), Threading vs Multiprocessing & AsyncIO Event Loop",
            "concept_lesson": (
                "Concurrency in Python is shaped by the Global Interpreter Lock (GIL).\n\n"
                "The Global Interpreter Lock (GIL):\n"
                "The GIL is a mutual-exclusion mutex used by CPython to prevent multiple native OS threads from executing Python bytecode "
                "simultaneously on multiple CPU cores. It was introduced to make CPython's memory management (reference count updates) thread-safe "
                "without adding fine-grained lock overhead to every single object.\n\n"
                "Concurrency Paradigms in Python:\n"
                "1. `threading` (Multi-Threading):\n"
                "- Native OS threads managed by the kernel, but constrained by the GIL.\n"
                "- CPU-Bound Tasks: Running multiple threads on CPU-heavy code provides ZERO speedup (and often slows down execution due to GIL contention).\n"
                "- I/O-Bound Tasks: Highly effective. When a thread performs network I/O, file reads, or sleep, CPython voluntarily releases the GIL, "
                "allowing other threads to execute concurrently.\n\n"
                "2. `multiprocessing` (Multi-Processing):\n"
                "- Spawns completely separate OS processes, each with its own independent Python interpreter, memory space, and GIL.\n"
                "- Enables true parallel execution across multi-core CPUs for CPU-bound tasks.\n"
                "- Inter-Process Communication (IPC) requires data serialization (`pickle`) over pipes or queues, incurring IPC overhead.\n\n"
                "3. `asyncio` (Cooperative Asynchronous I/O):\n"
                "- Single-threaded, single-process concurrency based on an Event Loop and Coroutines (`async def`, `await`).\n"
                "- Extremely lightweight (thousands of concurrent connections take minimal RAM). Coroutines cooperatively yield control back "
                "to the event loop during non-blocking socket operations."
            ),
            "key_definitions": [
                {"term": "Global Interpreter Lock (GIL)", "definition": "A mutex in CPython allowing only one thread to execute Python bytecode at any instant."},
                {"term": "Event Loop", "definition": "A single-threaded scheduling engine in asyncio coordinating non-blocking tasks and I/O callbacks."},
                {"term": "Coroutine", "definition": "A Python function defined with async def that can pause execution (await) and yield control back to the event loop."}
            ],
            "interview_questions": [
                {
                    "q": "Why does Python have the GIL, and what are its trade-offs?",
                    "a": "CPython's memory management relies on reference counting (`ob_refcnt`). Without the GIL, every increment/decrement of a reference count would require thread synchronization locks, causing massive performance degradation in single-threaded programs and risking race condition memory corruptions. The GIL simplifies C extensions and guarantees thread-safe memory management, but prevents multi-threaded Python programs from executing CPU-bound code in parallel across multiple cores."
                },
                {
                    "q": "When should you use `threading`, `multiprocessing`, or `asyncio`?",
                    "a": "- Use `multiprocessing` for CPU-bound tasks (image processing, data science, mathematical simulations) to utilize multiple physical CPU cores in parallel. - Use `threading` for legacy I/O-bound tasks where libraries block synchronously (file system reads, synchronous database drivers). - Use `asyncio` for high-concurrency, network-heavy I/O-bound tasks (FastAPI servers, microservices, web scrapers) where tens of thousands of idle socket connections can be handled on a single thread with minimal RAM."
                },
                {
                    "q": "Does Python's GIL prevent race conditions in multi-threaded programs?",
                    "a": "No. The GIL only guarantees CPython internal interpreter memory safety (protecting reference counts and C pointers); it does NOT protect application-level shared state. In Python, an operation like `counter += 1` compiles to multiple bytecode instructions (LOAD_FAST, LOAD_CONST, BINARY_ADD, STORE_FAST). The thread can be context-switched between these instructions, producing race conditions. Programmers must still use `threading.Lock`."
                },
                {
                    "q": "How does an `asyncio` event loop differ from multi-threading?",
                    "a": "Multi-threading uses preemptive scheduling where the OS kernel arbitrarily interrupts threads at any instruction. `asyncio` uses cooperative multitasking on a single thread: coroutines yield execution control explicitly using `await`. Because only one coroutine executes at any millisecond, there is zero thread context-switch overhead and no shared-memory race conditions during synchronous blocks."
                },
                {
                    "q": "What happens if you execute a blocking synchronous operation (like `time.sleep(5)`) inside an `asyncio` coroutine?",
                    "a": "Because `asyncio` runs on a single thread, a blocking synchronous call halts the entire event loop. No other coroutines or tasks can execute or handle incoming network traffic during those 5 seconds. To run blocking operations safely in asyncio, you must offload them to a thread pool executor via `asyncio.to_thread(func)` or `loop.run_in_executor()`."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-23-01",
                    "question": "What is the primary constraint imposed by CPython's Global Interpreter Lock (GIL)?",
                    "options": ["Files cannot be read concurrently", "Only one thread can execute Python bytecode at a time within a single process", "Subprocesses are prohibited", "Recursion depth is limited to 100"],
                    "correct_answer": "B",
                    "explanation": "The GIL restricts bytecode execution to one thread at any given instant per process."
                },
                {
                    "id": "CS-23-02",
                    "question": "Which Python module enables true parallel execution across multi-core CPUs for CPU-bound computations?",
                    "options": ["threading", "multiprocessing", "asyncio", "socket"],
                    "correct_answer": "B",
                    "explanation": "multiprocessing spawns independent processes with separate GILs, running across multiple cores."
                },
                {
                    "id": "CS-23-03",
                    "question": "In Python, which operation is NOT atomic and requires a threading Lock?",
                    "options": ["list.append(x)", "dict[key] = val", "counter += 1", "queue.pop()"],
                    "correct_answer": "C",
                    "explanation": "`counter += 1` compiles to multiple bytecode instructions (read, add, write), requiring synchronization."
                },
                {
                    "id": "CS-23-04",
                    "question": "Coroutines in `asyncio` yield control back to the event loop using which keyword?",
                    "options": ["yield from", "await", "defer", "pass"],
                    "correct_answer": "B",
                    "explanation": "The `await` keyword pauses coroutine execution and returns control to the event loop."
                },
                {
                    "id": "CS-23-05",
                    "question": "How should a blocking synchronous I/O function be executed in an asyncio application?",
                    "options": ["Invoke it directly inside async def", "Wrap it with asyncio.to_thread() to run in a thread pool", "Call sys.exit()", "Increase the recursion limit"],
                    "correct_answer": "B",
                    "explanation": "Blocking operations must be offloaded to worker threads via asyncio.to_thread() to avoid freezing the event loop."
                }
            ]
        },

        24: {
            "subject": "Python Internals",
            "topic": "Python Advanced Patterns: Decorators, Generators, Iterators & Context Managers",
            "concept_lesson": (
                "Python's expressive syntax is built upon first-class functions and standard protocols.\n\n"
                "1. Decorators:\n"
                "A decorator is a higher-order function that takes a function as input, extends its behavior without modifying source code, "
                "and returns a callable: `@my_decorator def func(): ...` translates directly to `func = my_decorator(func)`. "
                "Always apply `@functools.wraps(func)` to preserve original docstrings, names, and argument signatures.\n\n"
                "2. Iterators & Iterable Protocol:\n"
                "- An Iterable implements `__iter__()` returning an Iterator.\n"
                "- An Iterator implements `__next__()` returning successive items, raising `StopIteration` when exhausted. "
                "Every iterator is also an iterable returning itself in `__iter__()`.\n\n"
                "3. Generators (`yield`):\n"
                "A generator is a function containing the `yield` keyword. Calling it returns a generator object without running the body. "
                "Execution resumes only when `next()` is called, pausing at `yield` and preserving local stack frames in heap memory. "
                "Provides Lazy Evaluation: streams infinite or multi-gigabyte datasets with O(1) memory footprint.\n\n"
                "4. Context Managers (`with` statement):\n"
                "Guarantees deterministic resource acquisition and release (e.g., closing file handles or database connections even if exceptions occur). "
                "Implements the Context Management Protocol:\n"
                "- `__enter__(self)`: Acquires resource and returns target to `as` variable.\n"
                "- `__exit__(self, exc_type, exc_val, exc_tb)`: Executes cleanup. Returning True suppresses raised exceptions."
            ),
            "key_definitions": [
                {"term": "Decorator", "definition": "A higher-order function wrapping another callable to extend its behavior dynamically."},
                {"term": "Generator", "definition": "A memory-efficient function using yield to produce values lazily on demand."},
                {"term": "Context Manager", "definition": "An object implementing __enter__ and __exit__ to ensure guaranteed resource allocation and cleanup."}
            ],
            "interview_questions": [
                {
                    "q": "How do Decorators work in Python, and why is `functools.wraps` essential?",
                    "a": "A decorator takes a function as an argument, wraps it inside an inner wrapper function that adds pre/post execution logic, and returns the wrapper. Without `@functools.wraps(original_func)`, the decorated function's metadata (`__name__`, `__doc__`, module, annotations) is overwritten by the wrapper's metadata, breaking reflection, debugging, and documentation tools like Swagger/FastAPI."
                },
                {
                    "q": "What is the difference between a Generator and a standard List in Python?",
                    "a": "A list calculates and allocates all elements in memory simultaneously at creation time (O(N) space). A generator uses lazy evaluation: it computes the next value only when requested via `next()` or a for loop, yielding one item at a time and maintaining internal execution state in O(1) space. A generator reading a 10GB log file consumes negligible RAM."
                },
                {
                    "q": "Explain the difference between `__iter__` and `__next__`.",
                    "a": "`__iter__` must return an iterator object (an object that implements `__next__`). `__next__` retrieves the next value in the iteration sequence and raises `StopIteration` when elements are exhausted. An iterable only needs `__iter__`; an iterator must implement both `__iter__` (returning `self`) and `__next__`."
                },
                {
                    "q": "How does the Context Manager protocol work, and what do the arguments to `__exit__` represent?",
                    "a": "When entering a `with` block, Python calls `__enter__()`. Upon leaving the block (normally or via exception), Python calls `__exit__(exc_type, exc_val, exc_tb)`. If no exception occurred, all three arguments are None. If an exception occurred, they contain the exception class, exception instance, and traceback. If `__exit__` returns True, the exception is swallowed; otherwise, it propagates normally."
                },
                {
                    "q": "How does `contextlib.contextmanager` simplify creating context managers?",
                    "a": "It allows creating a context manager using a single generator function with `yield` instead of writing a full class with `__enter__` and `__exit__`. Code before `yield` runs during `__enter__`, the yielded value is bound to the `as` variable, and code inside `finally:` after `yield` runs automatically during `__exit__`."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-24-01",
                    "question": "What syntactic transformation occurs when writing `@decorator def foo(): pass`?",
                    "options": ["foo = foo(decorator)", "foo = decorator(foo)", "decorator = foo()", "def foo(): decorator()"],
                    "correct_answer": "B",
                    "explanation": "Decorators wrap functions: `foo = decorator(foo)`."
                },
                {
                    "id": "CS-24-02",
                    "question": "Which exception is raised by an iterator's `__next__()` method when no further elements exist?",
                    "options": ["IndexError", "KeyError", "StopIteration", "GeneratorExit"],
                    "correct_answer": "C",
                    "explanation": "The iterator protocol raises StopIteration when iteration completes."
                },
                {
                    "id": "CS-24-03",
                    "question": "Functions containing the `yield` keyword return which type of object when invoked?",
                    "options": ["List", "Tuple", "Generator object", "Coroutine"],
                    "correct_answer": "C",
                    "explanation": "Calling a function containing yield returns a generator object."
                },
                {
                    "id": "CS-24-04",
                    "question": "Why is `@functools.wraps` applied to decorator wrappers?",
                    "options": ["To bypass the GIL", "To preserve the original function's name, docstring, and metadata", "To convert code to C", "To catch syntax errors"],
                    "correct_answer": "B",
                    "explanation": "functools.wraps copies function metadata like __name__ and __doc__ onto the wrapper."
                },
                {
                    "id": "CS-24-05",
                    "question": "If `__exit__` in a context manager returns `True` after an exception occurs, what happens?",
                    "options": ["The program crashes", "The exception is suppressed/swallowed", "The exception is re-raised", "A deadlock occurs"],
                    "correct_answer": "B",
                    "explanation": "Returning True from __exit__ indicates the exception was handled, suppressing it."
                }
            ]
        },

        25: {
            "subject": "Python Internals",
            "topic": "Object-Oriented Python: Dunder Methods, MRO (C3 Linearization) & Metaclasses",
            "concept_lesson": (
                "Object-oriented programming in Python is dynamic and extensible through special 'dunder' (double underscore) magic methods.\n\n"
                "Core Dunder Methods:\n"
                "- `__new__(cls, ...)`: Responsible for physically creating and returning a new instance in memory. Runs before `__init__` (used in Singletons and immutable types).\n"
                "- `__init__(self, ...)`: Initializes instance attributes on the already-created object.\n"
                "- `__repr__` vs `__str__`: `__repr__` provides an unambiguous developer representation (`eval(repr(x)) == x`); `__str__` provides a readable end-user string.\n"
                "- `__call__`: Allows an object instance to be invoked as a function: `obj()`.\n"
                "- `__eq__`, `__hash__`: Dict keys and sets require hashable objects. If a class overrides `__eq__`, Python sets `__hash__ = None` unless explicitly implemented.\n\n"
                "Multiple Inheritance & Method Resolution Order (MRO):\n"
                "When multiple base classes exist (e.g., class D(B, C)), Python resolves attribute lookups using the C3 Linearization Algorithm.\n"
                "Properties of C3 Linearization:\n"
                "1. Children precede their parents (Local Precedence Order).\n"
                "2. Base class declaration order is strictly preserved.\n"
                "3. Monotonicity: A class always appears before its superclasses in every subclass MRO.\n"
                "Inspectable via `ClassName.__mro__` or `ClassName.mro()`.\n\n"
                "`super()` Behavior:\n"
                "`super()` does NOT necessarily call the immediate parent class; it delegates to the NEXT class in the dynamic MRO chain, "
                "enabling cooperative multi-inheritance without duplicate calls in diamond inheritance hierarchies."
            ),
            "key_definitions": [
                {"term": "Method Resolution Order (MRO)", "definition": "The deterministic linear order in which Python searches base classes for attributes and methods."},
                {"term": "C3 Linearization", "definition": "The algorithm used by Python to compute MRO, ensuring consistency and monotonicity in multiple inheritance."},
                {"term": "__new__", "definition": "The static class constructor method that creates and returns the physical object instance before __init__ runs."}
            ],
            "interview_questions": [
                {
                    "q": "What is the difference between `__new__` and `__init__` in Python?",
                    "a": "`__new__` is the actual instance creator; it is a static method taking the class `cls` as its first parameter and must return a newly created object instance (usually via `super().__new__(cls)`). `__init__` is the instance initializer; it takes the newly created instance `self` and populates attributes, returning nothing (`None`). `__new__` is used when subclassing immutable types (int, str, tuple) or implementing the Singleton design pattern."
                },
                {
                    "q": "How does Python solve the Diamond Problem in multiple inheritance?",
                    "a": "In a diamond inheritance (Class D inherits from B and C, both inheriting from A), Python uses the C3 Linearization algorithm to compute a single linear Method Resolution Order (MRO: D -> B -> C -> A -> object). Calls to `super()` follow this exact linear sequence, guaranteeing that base class A's method is executed exactly once without duplicate calls."
                },
                {
                    "q": "What is the difference between `__str__` and `__repr__`?",
                    "a": "`__repr__` is intended for developers and debugging; its output should ideally be unambiguous and look like valid Python code to recreate the object (`eval(repr(x)) == x`). `__str__` is intended for end-users, providing a readable string representation. If `__str__` is not defined, Python falls back to `__repr__`."
                },
                {
                    "q": "Why must an object be immutable to be used as a dictionary key or set element?",
                    "a": "Dictionary lookups rely on hash tables where key positions are determined by `hash(key)`. If an object were mutable (like a list) and its contents changed after being inserted into a dict, its hash value would change. The dictionary would then search for the key in a different hash bucket, making the item unfindable. Thus, dict keys must be hashable and immutable."
                },
                {
                    "q": "What is a Metaclass in Python and give a real-world use case?",
                    "a": "A metaclass is the 'class of a class'—just as an object is an instance of a class, a class is an instance of a metaclass (by default, `type`). Metaclasses allow intercepting and modifying class definition construction at import time. Real-world use cases include ORMs (like SQLAlchemy or Django Models) and validation frameworks (like Pydantic v1), where field declarations are parsed into SQL columns or validation schemas before instantiation."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-25-01",
                    "question": "Which algorithm does Python use to compute the Method Resolution Order (MRO)?",
                    "options": ["Dijkstra's Algorithm", "C3 Linearization", "Depth-First Search", "Kruskal's Algorithm"],
                    "correct_answer": "B",
                    "explanation": "Python employs the C3 Linearization algorithm to compute deterministic MRO lists."
                },
                {
                    "id": "CS-25-02",
                    "question": "Which magic method is responsible for physically creating and returning a new object instance in memory?",
                    "options": ["__init__", "__new__", "__create__", "__call__"],
                    "correct_answer": "B",
                    "explanation": "__new__ creates and returns the physical object instance before __init__ initializes it."
                },
                {
                    "id": "CS-25-03",
                    "question": "If an object implements `__call__`, it can be:",
                    "options": ["Iterated with for loops", "Invoked like a function: obj()", "Converted to JSON automatically", "Garbage collected immediately"],
                    "correct_answer": "B",
                    "explanation": "Implementing __call__ allows instance objects to be invoked as callables."
                },
                {
                    "id": "CS-25-04",
                    "question": "What is the default metaclass of all standard classes in Python?",
                    "options": ["object", "type", "class", "base"],
                    "correct_answer": "B",
                    "explanation": "In Python, `type` is the default metaclass that creates classes."
                },
                {
                    "id": "CS-25-05",
                    "question": "If a custom class overrides `__eq__` without defining `__hash__`, Python automatically sets `__hash__` to:",
                    "options": ["0", "None (making instances unhashable)", "id(self)", "A random integer"],
                    "correct_answer": "B",
                    "explanation": "Overriding __eq__ without defining __hash__ sets __hash__ to None to prevent mutable hash violations."
                }
            ]
        },

        26: {
            "subject": "Python Internals",
            "topic": "RESTful API Design, ASGI Architectures & FastAPI Internals",
            "concept_lesson": (
                "Modern backend architectures rely on REST principles and asynchronous gateway interfaces.\n\n"
                "REST Architectural Constraints (Roy Fielding):\n"
                "1. Client-Server Architecture: Separation of concerns between UI client and backend data storage.\n"
                "2. Statelessness: Each request from client to server must contain all information required to understand and service the request; no session context on server.\n"
                "3. Cacheability: Responses must explicitly label themselves as cacheable or non-cacheable (via `Cache-Control` headers).\n"
                "4. Uniform Interface: Standard HTTP methods (GET: safe & idempotent, POST: non-idempotent, PUT: idempotent replacement, PATCH: partial update, DELETE: idempotent).\n"
                "5. Layered System: Client cannot distinguish whether it connects directly to end server or intermediate proxy/load balancer.\n\n"
                "WSGI vs ASGI Architectures:\n"
                "- WSGI (Web Server Gateway Interface): Synchronous Python standard (`def app(environ, start_response)`). Each request consumes an OS thread; cannot handle WebSockets or long polling.\n"
                "- ASGI (Asynchronous Server Gateway Interface): Asynchronous successor (`async def app(scope, receive, send)`). "
                "Event-driven architecture natively supporting HTTP/2, WebSockets, and long-lived streaming connections (Uvicorn, Hypercorn).\n\n"
                "FastAPI Framework Mechanics:\n"
                "FastAPI is built on Starlette (ASGI toolkit) and Pydantic (data validation via Python type annotations). "
                "Route parameters are parsed into Pydantic models with automatic JSON schema generation (`/docs` OpenAPI/Swagger). "
                "FastAPI handles concurrency smartly: endpoints defined with `async def` run on the main asyncio event loop; endpoints defined with standard "
                "`def` are automatically offloaded to an external thread pool (`anyio` worker threads) to prevent blocking the event loop."
            ),
            "key_definitions": [
                {"term": "ASGI", "definition": "Asynchronous Server Gateway Interface: async standard for Python web servers supporting HTTP and WebSockets."},
                {"term": "Idempotent Method", "definition": "An HTTP method where multiple identical requests produce the exact same server resource state (GET, PUT, DELETE)."},
                {"term": "Statelessness", "definition": "The REST constraint mandating that every request contain all necessary context without server-side session memory."}
            ],
            "interview_questions": [
                {
                    "q": "What is the difference between an Idempotent and a Safe HTTP method?",
                    "a": "A Safe method (like GET or HEAD) does not alter server resource state (read-only). An Idempotent method (like PUT or DELETE) can alter server state, but making the exact same request multiple times produces the identical server state as making it once (e.g., DELETE /students/5 removes student 5; repeating it still leaves student 5 removed). POST is neither safe nor idempotent because multiple POSTs create multiple separate records."
                },
                {
                    "q": "Compare WSGI (e.g., Flask/Django) and ASGI (e.g., FastAPI/Starlette).",
                    "a": "WSGI is synchronous and blocking; each incoming request binds an entire operating system thread. It cannot natively support persistent WebSockets, server-sent events, or asynchronous event loops. ASGI is asynchronous and non-blocking, designed for `asyncio`. It handles thousands of concurrent long-lived connections, HTTP/2, and WebSockets on a single thread using an event loop with minimal memory overhead."
                },
                {
                    "q": "How does FastAPI handle `async def` routes vs standard `def` routes differently?",
                    "a": "If you define a route with `async def`, FastAPI executes it directly on the main `asyncio` event loop; any blocking call inside it freezes the entire server. If you define a route with standard `def`, FastAPI automatically runs it inside a background thread pool (AnyIO worker threads) so that blocking synchronous operations (like legacy database queries) do not block the event loop."
                },
                {
                    "q": "What is the difference between PUT and PATCH in RESTful APIs?",
                    "a": "PUT performs a complete replacement of the target resource; the request payload must contain the entire updated entity, and omitted fields are typically reset to null or defaults. PATCH performs a partial update; only the specific fields provided in the request payload are modified, leaving all other existing entity attributes unchanged."
                },
                {
                    "q": "What is Dependency Injection in FastAPI and how does `Depends()` function?",
                    "a": "Dependency Injection decouples shared logic (database sessions, authentication, permission checks) from route handlers. In FastAPI, `Depends(get_db)` declares a dependency. When a request arrives, FastAPI resolves `get_db`, injects its return value (e.g., active Supabase/SQLAlchemy session) into the route function parameter, and guarantees execution of cleanup/close logic in `finally:` after the response is sent."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-26-01",
                    "question": "Which of the following HTTP methods is NOT idempotent?",
                    "options": ["GET", "PUT", "DELETE", "POST"],
                    "correct_answer": "D",
                    "explanation": "POST is non-idempotent because multiple identical calls create duplicate records."
                },
                {
                    "id": "CS-26-02",
                    "question": "The asynchronous standard that superseded WSGI for modern Python web servers like Uvicorn is:",
                    "options": ["CGI", "ASGI", "FAST-CGI", "HTTPD"],
                    "correct_answer": "B",
                    "explanation": "ASGI (Asynchronous Server Gateway Interface) is the modern async Python standard."
                },
                {
                    "id": "CS-26-03",
                    "question": "In FastAPI, what happens when a route handler is declared with standard `def` instead of `async def`?",
                    "options": ["It raises a TypeError", "FastAPI automatically executes it in an external thread pool", "It blocks the server permanently", "It runs on the GPU"],
                    "correct_answer": "B",
                    "explanation": "FastAPI offloads standard def routes to background worker threads to avoid event loop stalls."
                },
                {
                    "id": "CS-26-04",
                    "question": "Which HTTP status code signifies that a requested resource was successfully created on the server?",
                    "options": ["200 OK", "201 Created", "204 No Content", "304 Not Modified"],
                    "correct_answer": "B",
                    "explanation": "HTTP 201 Created is the standard response code for successful resource creation."
                },
                {
                    "id": "CS-26-05",
                    "question": "Which RESTful constraint states that every request must contain all necessary data without server-stored session state?",
                    "options": ["Uniform Interface", "Statelessness", "Cacheability", "Layered System"],
                    "correct_answer": "B",
                    "explanation": "Statelessness requires that no client session context is retained on the server."
                }
            ]
        },

        # --- DAYS 27-30: SYSTEM DESIGN FUNDAMENTALS ---
        27: {
            "subject": "System Design",
            "topic": "Scalability, High Availability, Load Balancing & Consistent Hashing",
            "concept_lesson": (
                "System design is the process of architecting scalable, reliable, and maintainable software systems serving millions of users.\n\n"
                "Vertical vs Horizontal Scaling:\n"
                "- Vertical Scaling (Scale Up): Adding more CPU, RAM, or disk to a single machine. Hard physical limits, expensive, single point of failure (SPOF).\n"
                "- Horizontal Scaling (Scale Out): Adding more commodity machines to a cluster. Requires stateless application layers and distributed data storage.\n\n"
                "Load Balancing Algorithms:\n"
                "Load balancers (NGINX, HAProxy, AWS ALB) distribute incoming network traffic across backend server pools:\n"
                "1. Round Robin: Distributes requests sequentially across servers.\n"
                "2. Least Connections: Routes traffic to the server with fewest active connections (ideal for long-lived sessions).\n"
                "3. IP Hash: Hashes client IP to ensure session stickiness without server-side shared state.\n"
                "Operates at Layer 4 (Transport/TCP: fast, byte-level routing) or Layer 7 (Application/HTTP: smart routing based on URI, cookies, headers).\n\n"
                "Consistent Hashing:\n"
                "Traditional hash routing (`server = hash(key) % N`) causes catastrophic cache invalidation when server count N changes (almost 100% of keys remap). "
                "Consistent Hashing maps both servers and keys onto a virtual circular 360-degree ring (Hash Ring). A key is assigned to the first server encountered "
                "clockwise. When a server is added or removed, ONLY K/N keys are remapped on average. Virtual Nodes (vnodes) replicate each physical server across "
                "multiple ring positions, preventing hotspot skew and ensuring uniform data distribution."
            ),
            "key_definitions": [
                {"term": "Horizontal Scaling", "definition": "Expanding system capacity by adding more server instances to the resource pool."},
                {"term": "Load Balancer", "definition": "A reverse proxy routing network traffic across multiple servers to prevent overload and ensure availability."},
                {"term": "Consistent Hashing", "definition": "A hashing technique mapping keys and servers to a circular ring so adding/removing nodes remaps only K/N keys."}
            ],
            "interview_questions": [
                {
                    "q": "What problem does Consistent Hashing solve in distributed caching and storage?",
                    "a": "In a distributed system using standard modulo hashing `server = hash(key) % N`, adding or removing a single server changes N, causing nearly 100% of all cached keys to remap to different servers. This triggers a catastrophic cache avalanche where the underlying database is swamped with requests. Consistent Hashing maps both keys and servers to a circular 2^32 hash ring. Adding or removing a server remaps only K/N keys (where K is total keys, N is server count), localizing redistribution."
                },
                {
                    "q": "What are Virtual Nodes in Consistent Hashing, and why are they necessary?",
                    "a": "Without virtual nodes, physical servers placed randomly on the hash ring can lead to non-uniform, highly unequal partition sizes, creating Hotspots where one server receives 80% of traffic. Virtual nodes assign multiple (e.g., 100-200) distinct hash labels across the ring for each physical machine, smoothing out variance and ensuring uniformly balanced load."
                },
                {
                    "q": "Explain the difference between Layer 4 and Layer 7 Load Balancing.",
                    "a": "Layer 4 load balancing operates at the Transport layer (TCP/UDP); it inspects only IP addresses and port numbers, forwarding raw packets without decrypting TLS or inspecting HTTP content (ultra-fast, low CPU). Layer 7 load balancing operates at the Application layer (HTTP/HTTPS); it can inspect URLs, HTTP headers, cookies, and POST bodies, allowing content-based routing (e.g., `/api/payments` routes to payment cluster, `/static` routes to CDN) and TLS termination."
                },
                {
                    "q": "What is a Single Point of Failure (SPOF) and how do redundancy and failover eliminate it?",
                    "a": "A SPOF is any single component whose failure brings down the entire system. It is eliminated through Redundancy (deploying duplicate active or passive components) paired with Automated Failover. For example, deploying redundant load balancers using VRRP / Keepalived with a shared floating IP ensures that if the primary load balancer crashes, the backup takes over the IP within milliseconds."
                },
                {
                    "q": "What is the difference between High Availability (HA) and Fault Tolerance?",
                    "a": "High Availability aims to minimize downtime across a system (e.g., '99.999% uptime', allowing ~5 minutes of downtime per year) through rapid automated recovery and failover. Fault Tolerance guarantees zero interruption or degradation of service even when hardware components fail, typically requiring fully synchronized duplicate hardware executing lockstep."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-27-01",
                    "question": "What proportion of keys must be remapped on average when adding a server to a Consistent Hashing ring with N nodes?",
                    "options": ["100%", "50%", "K / N", "0%"],
                    "correct_answer": "C",
                    "explanation": "Consistent hashing minimizes redistribution: only K/N keys must be remapped when adding/removing nodes."
                },
                {
                    "id": "CS-27-02",
                    "question": "What is the primary function of Virtual Nodes in Consistent Hashing?",
                    "options": ["To encrypt network packets", "To ensure uniform key distribution across physical servers and prevent hotspots", "To eliminate the need for hash functions", "To replace load balancers"],
                    "correct_answer": "B",
                    "explanation": "Virtual nodes distribute partitions uniformly across the ring, preventing hot spots."
                },
                {
                    "id": "CS-27-03",
                    "question": "A Layer 7 Load Balancer can route incoming traffic based on which of the following?",
                    "options": ["Source IP only", "TCP port only", "HTTP request URI path and Cookie headers", "MAC address"],
                    "correct_answer": "C",
                    "explanation": "Layer 7 balancers inspect application-layer HTTP headers, URLs, and cookies."
                },
                {
                    "id": "CS-27-04",
                    "question": "Scaling a system by adding more physical server nodes to a cluster is termed:",
                    "options": ["Vertical Scaling", "Horizontal Scaling", "Deep Paging", "B+ Tree splitting"],
                    "correct_answer": "B",
                    "explanation": "Horizontal scaling (scaling out) adds more servers to a distributed pool."
                },
                {
                    "id": "CS-27-05",
                    "question": "Which load balancing algorithm sends each incoming request to the server with the fewest active TCP sessions?",
                    "options": ["Round Robin", "Least Connections", "IP Hash", "Weighted Random"],
                    "correct_answer": "B",
                    "explanation": "Least Connections selects the server with the lowest concurrent connection load."
                }
            ]
        },

        28: {
            "subject": "System Design",
            "topic": "Caching Strategies, Cache Invalidation, Eviction Policies & Redis",
            "concept_lesson": (
                "Caching stores copies of frequently accessed data in fast, volatile memory (RAM) to minimize disk and database I/O latency.\n\n"
                "Caching Patterns:\n"
                "1. Cache-Aside (Lazy Loading): The application first queries the cache. On Cache Hit, return data. On Cache Miss, query the database, "
                "write the data into the cache, and return it. Highly resilient (cache failure does not break the app), but data can become stale.\n"
                "2. Read-Through: Application treats cache as main data store; the cache provider automatically fetches missing data from DB on misses.\n"
                "3. Write-Through: Data is written to cache AND database synchronously before acknowledging write. High consistency, higher write latency.\n"
                "4. Write-Behind (Write-Back): Data is written directly to cache and acknowledged immediately; the cache asynchronously batches writes to DB. "
                "Ultra-fast write throughput, but risks data loss if the cache node crashes before flushing.\n\n"
                "Cache Invalidation & Problems:\n"
                "- Cache Invalidation: 'There are only two hard things in Computer Science: cache invalidation and naming things' (Phil Karlton). Handled via TTL (Time-To-Live) and event-based purge.\n"
                "- Cache Penetration: Queries for non-existent keys miss cache and repeatedly hit DB. Solved using Bloom Filters or caching null values.\n"
                "- Cache Breakdown (Stampede): A popular key with high traffic expires; thousands of concurrent requests simultaneously hit DB. Solved with Mutex Locks on cache misses.\n"
                "- Cache Avalanche: Thousands of cached keys share identical TTL and expire at the exact same second. Solved by adding random jitter to TTLs.\n\n"
                "Eviction Policies: LRU (Least Recently Used), LFU (Least Frequently Used), FIFO."
            ),
            "key_definitions": [
                {"term": "Cache-Aside", "definition": "A pattern where the application orchestrates reads/writes between cache and database directly."},
                {"term": "Cache Stampede", "definition": "A massive spike in database load when an intensely accessed cached key expires and concurrent requests miss."},
                {"term": "Bloom Filter", "definition": "A space-efficient probabilistic data structure testing whether an element is definitely not present or possibly present."}
            ],
            "interview_questions": [
                {
                    "q": "What is the difference between Cache-Aside and Write-Through caching strategies?",
                    "a": "In Cache-Aside, the application code directly orchestrates caching: it queries the cache, fetches from DB on a miss, and populates the cache. Writes go directly to the DB and invalidate the cache key. In Write-Through, the application writes exclusively to the cache; the cache infrastructure synchronously writes to the database before returning success. Write-Through ensures cache-DB consistency but increases write latency."
                },
                {
                    "q": "Explain Cache Avalanche, Cache Penetration, and Cache Breakdown, along with their solutions.",
                    "a": "1. Cache Avalanche: Massive numbers of keys expire simultaneously, overwhelming the DB. Solution: Add random jitter (e.g., TTL = base + rand(0, 300)s). 2. Cache Penetration: Clients query keys that do not exist in cache or DB (e.g., malicious IDs). Solution: Use Bloom Filters to reject non-existent keys, or cache empty NULL results with short TTL. 3. Cache Breakdown (Stampede): A single mega-popular hot key expires, and thousands of concurrent requests hit the DB. Solution: Use distributed mutex locking so only the first request queries DB while others wait."
                },
                {
                    "q": "How does a Bloom Filter work and why is it useful in front of a database?",
                    "a": "A Bloom Filter is a space-efficient probabilistic bit array. An item is hashed by k independent hash functions, setting corresponding bits to 1. To check membership, the bits are checked: if ANY bit is 0, the item is DEFINITELY NOT in the set (zero false negatives). If all bits are 1, the item is PROBABLY in the set (small false positive rate). Placing it in front of a DB prevents costly disk lookups for non-existent user IDs or URLs."
                },
                {
                    "q": "What is the difference between LRU and LFU cache eviction policies?",
                    "a": "LRU (Least Recently Used) evicts the item that has not been accessed for the longest duration of time, implemented via a Doubly Linked List paired with a Hash Map (O(1) access and update). LFU (Least Frequently Used) tracks access frequency counts and evicts the item with the lowest hit counter, which is ideal when certain static assets are accessed frequently over long time horizons."
                },
                {
                    "q": "Why is Redis preferred as a distributed cache over Memcached in modern architectures?",
                    "a": "Memcached is a multithreaded simple key-value string store. Redis is an in-memory data structures store supporting rich data types (Strings, Hashes, Lists, Sets, Sorted Sets, Bitmaps, HyperLogLogs), disk persistence (RDB snapshots and AOF logs), built-in replication, clustering, pub/sub messaging, and atomic Lua scripting."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-28-01",
                    "question": "Which caching pattern writes data to the cache, acknowledges the write immediately, and flushes asynchronously to the DB?",
                    "options": ["Cache-Aside", "Write-Through", "Write-Behind (Write-Back)", "Refresh-Ahead"],
                    "correct_answer": "C",
                    "explanation": "Write-Behind writes to cache and asynchronously flushes updates to database storage."
                },
                {
                    "id": "CS-28-02",
                    "question": "Adding random jitter to cache TTL values is the primary countermeasure against:",
                    "options": ["Cache Avalanche", "Cache Penetration", "Deadlocks", "Dirty Reads"],
                    "correct_answer": "A",
                    "explanation": "Jitter prevents all keys from expiring simultaneously, stopping Cache Avalanches."
                },
                {
                    "id": "CS-28-03",
                    "question": "A Bloom Filter guarantees which of the following probabilistic properties?",
                    "options": ["No false positives", "No false negatives (if it says an element is absent, it is definitely absent)", "100% exact membership", "Instant encryption"],
                    "correct_answer": "B",
                    "explanation": "Bloom filters never produce false negatives: negative results are guaranteed true."
                },
                {
                    "id": "CS-28-04",
                    "question": "What data structure combination enables an LRU cache to achieve O(1) lookup and O(1) eviction?",
                    "options": ["Array and Stack", "Hash Map and Doubly Linked List", "Binary Heap and Queue", "B+ Tree only"],
                    "correct_answer": "B",
                    "explanation": "Hash map provides O(1) lookup, while doubly linked list provides O(1) node reordering."
                },
                {
                    "id": "CS-28-05",
                    "question": "Which phenomenon occurs when a heavily accessed hot key expires and concurrent requests simultaneously hit the database?",
                    "options": ["Cache Stampede (Breakdown)", "Cache Penetration", "Thrashing", "Starvation"],
                    "correct_answer": "A",
                    "explanation": "Cache Stampede happens when concurrent threads rush to rebuild an expired hot key."
                }
            ]
        },

        29: {
            "subject": "System Design",
            "topic": "Database Scaling: Replication, Sharding, CAP Theorem & PACELC",
            "concept_lesson": (
                "When databases outgrow a single server, distributed architectures scale read and write throughput.\n\n"
                "Replication (Scaling Reads):\n"
                "- Primary-Replica (Master-Slave): All writes go to the Primary node. The Primary streams replication logs to Replicas (Read Slaves). "
                "Reads are distributed across Replicas. If Primary fails, a Replica is promoted.\n"
                "- Synchronous Replication: Primary waits for replicas to confirm write before returning success (strong consistency, higher latency).\n"
                "- Asynchronous Replication: Primary returns immediately after local write; replicas lag slightly (Replication Lag), risking data loss on sudden primary crash.\n\n"
                "Database Sharding (Scaling Writes):\n"
                "Horizontal partitioning: splitting rows of a table across multiple independent physical database instances (Shards). "
                "Partitioned by Shard Key (e.g., hash(user_id) % num_shards). Challenges: Cross-shard joins are extremely slow, distributed transactions "
                "require Two-Phase Commit (2PC), and resharding requires rebalancing.\n\n"
                "The CAP Theorem (Eric Brewer):\n"
                "A distributed data system can simultaneously provide at most TWO of the following three guarantees:\n"
                "1. Consistency (C): Every read receives the most recent write or an error (linearizability).\n"
                "2. Availability (A): Every non-failing node returns a non-error response (without guaranteeing latest data).\n"
                "3. Partition Tolerance (P): The system continues functioning despite dropped or delayed network packets between nodes.\n"
                "Because network cables and switches inevitably fail in physical distributed systems, Partition Tolerance (P) is non-negotiable. "
                "Systems must choose between CP (Consistency over Availability, e.g., Spanner, MongoDB, HBase) or AP (Availability over Consistency, e.g., Cassandra, DynamoDB).\n\n"
                "The PACELC Theorem:\n"
                "Expands CAP: If there is a Partition (P), how does system trade off Availability (A) and Consistency (C); Else (E), "
                "how does system trade off Latency (L) and Consistency (C)? (e.g., DynamoDB is PA/EL)."
            ),
            "key_definitions": [
                {"term": "Sharding", "definition": "Horizontal database partitioning distributing table rows across distinct database servers via a shard key."},
                {"term": "CAP Theorem", "definition": "The theorem stating distributed data stores must choose between Consistency or Availability during network partitions."},
                {"term": "Eventual Consistency", "definition": "A consistency model guaranteeing all replicas will converge to identical values given sufficient time without new writes."}
            ],
            "interview_questions": [
                {
                    "q": "Why is 'CA' (Consistency + Availability without Partition Tolerance) practically impossible in distributed systems?",
                    "a": "In any real-world distributed physical network, network cables can be severed, switches can fail, or routers can drop packets (Network Partition). When two nodes cannot communicate, if a write occurs on Node 1: the system can either 1) Reject the write or block reads on Node 2 to preserve Consistency (CP), sacrificing Availability; or 2) Accept the write and allow Node 2 to serve stale reads to preserve Availability (AP), sacrificing Consistency. Because network partitions cannot be prevented, a distributed system must choose between CP and AP."
                },
                {
                    "q": "What is Database Sharding and what are its major architectural challenges?",
                    "a": "Sharding is horizontal partitioning: splitting rows of a large database across multiple independent servers using a Shard Key (e.g., hash(user_id) % num_shards). Major challenges: 1. Cross-shard JOINs: Queries joining tables across different shards become prohibitively slow and must be executed in application code. 2. Cross-shard Transactions: Enforcing ACID across shards requires slow Two-Phase Commit (2PC). 3. Hotspot Shards: Unequal distribution of active users can overwhelm a single shard. 4. Resharding: Adding shards requires costly data migration."
                },
                {
                    "q": "Explain Replication Lag and how to prevent users from seeing their own stale writes.",
                    "a": "In asynchronous primary-replica architectures, writes commit to the primary and stream asynchronously to replicas. If a replica lags by 500ms and a user updates their profile and immediately refreshes the page (routed to the replica), they see their old profile. Solution ('Read-Your-Own-Writes' consistency): Route read requests for recently updated data directly to the Primary for a short window (e.g., 5 seconds after a user edit), while routing generic reads to replicas."
                },
                {
                    "q": "What is the PACELC theorem and how does it extend the CAP theorem?",
                    "a": "CAP only describes system behavior when a network partition occurs. PACELC states: If there is a Partition (P), trade off Availability (A) vs Consistency (C); ELSE (E), during normal fault-free operation, trade off Latency (L) vs Consistency (C). For example, MongoDB chooses PC/EC (prefers consistency always), whereas Amazon DynamoDB chooses PA/EL (prefers availability and low latency always)."
                },
                {
                    "q": "What is Eventual Consistency and what is a Vector Clock?",
                    "a": "Eventual consistency guarantees that in the absence of new updates, all replicas will eventually synchronize and return the identical value. Vector Clocks are arrays of logical timestamps maintained by distributed nodes to track causal relationships between updates and detect conflicting concurrent writes without relying on synchronized physical wall-clock times."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-29-01",
                    "question": "According to the CAP Theorem, when a network partition occurs, a distributed system must choose between:",
                    "options": ["Speed and Security", "Consistency and Availability", "Throughput and Storage", "Relational and NoSQL"],
                    "correct_answer": "B",
                    "explanation": "During a partition, the system must choose between Consistency (CP) or Availability (AP)."
                },
                {
                    "id": "CS-29-02",
                    "question": "Which database scaling technique splits table rows across distinct database instances based on a key?",
                    "options": ["Normalization", "Sharding (Horizontal Partitioning)", "Replication", "Compaction"],
                    "correct_answer": "B",
                    "explanation": "Sharding splits rows across distinct server instances based on a shard key."
                },
                {
                    "id": "CS-29-03",
                    "question": "What is a major trade-off of using Asynchronous Database Replication?",
                    "options": ["Writes are completely rejected", "Replication lag may cause temporary stale reads and data loss on primary crash", "Indexes cannot be created", "CPUs overheat"],
                    "correct_answer": "B",
                    "explanation": "Asynchronous replication introduces replication lag and risk of data loss on primary crash."
                },
                {
                    "id": "CS-29-04",
                    "question": "A system that prioritizes returning the latest write over system availability during network failure is classified as:",
                    "options": ["AP system", "CP system", "AC system", "P-only system"],
                    "correct_answer": "B",
                    "explanation": "CP systems enforce consistency at the expense of availability during partitions."
                },
                {
                    "id": "CS-29-05",
                    "question": "In the PACELC theorem, what does the 'E' stand for?",
                    "options": ["Encryption", "Else (when the network is operating normally)", "Eventual", "Ethernet"],
                    "correct_answer": "B",
                    "explanation": "PACELC stands for: if Partition, trade A vs C; ELSE, trade Latency vs Consistency."
                }
            ]
        },

        30: {
            "subject": "System Design",
            "topic": "System Design Interview Blueprint: URL Shortener & API Rate Limiter",
            "concept_lesson": (
                "Senior placement interviews evaluate architectural problem-solving through end-to-end design problems.\n\n"
                "System Design 4-Step Framework:\n"
                "1. Scope & Requirements: Clarify functional requirements, non-functional requirements (throughput, latency, availability), and back-of-the-envelope calculations.\n"
                "2. High-Level Design: Define API endpoints, core services, database schema, and high-level data flow diagrams.\n"
                "3. Deep-Dive Design: Address bottlenecks, data partitioning, caching, fault tolerance, and concurrency.\n"
                "4. Wrap-up: Discuss failure modes, monitoring, and telemetry.\n\n"
                "Case 1: Scalable URL Shortener (Bitly):\n"
                "- Requirements: Shorten long URL to 7-character alias (e.g., `bit.ly/3xZ9qL`); redirect short URL with HTTP 301/302; high read/write ratio (100:1).\n"
                "- Base62 Encoding: Characters [0-9, a-z, A-Z] (62 chars). A 7-character string supports 62^7 = 3.52 trillion unique URLs.\n"
                "- ID Generation: Do not use MD5/SHA256 truncation (hash collisions). Use distributed unique 64-bit integer ID generator (Twitter Snowflake or Ticket Server) "
                "and encode the integer directly into Base62.\n"
                "- Redirection: HTTP 301 (Permanent Redirect: browser caches redirect, reducing server load) vs HTTP 302 (Temporary: traffic passes through server for analytics).\n"
                "- Caching: Redis cluster caching top 20% hot URLs (80/20 Pareto principle).\n\n"
                "Case 2: API Rate Limiter:\n"
                "- Algorithms: Token Bucket (refills tokens at rate r, allows bursts), Leaky Bucket (smooth constant output rate via queue), "
                "Fixed Window Counter (vulnerable to 2x boundary spikes), Sliding Window Log (accurate, high memory), Sliding Window Counter (hybrid, memory efficient).\n"
                "- Architecture: Distributed Redis with Lua scripts (`EVAL`) executing atomic token decrement and TTL checks without race conditions."
            ),
            "key_definitions": [
                {"term": "Base62 Encoding", "definition": "Encoding using 62 alphanumeric characters (0-9, a-z, A-Z) to generate compact short URLs from 64-bit integers."},
                {"term": "Token Bucket", "definition": "A rate limiting algorithm where tokens accumulate at a fixed rate, consumed per request and permitting burst capacity."},
                {"term": "HTTP 301 vs 302", "definition": "HTTP 301 is permanently cached by browser; HTTP 302 is temporary, hitting the server on every click for telemetry."}
            ],
            "interview_questions": [
                {
                    "q": "Design a scalable URL Shortener (like TinyURL/Bitly): How do you generate unique 7-character short codes without collisions?",
                    "a": "Avoid hashing long URLs with MD5/SHA256 and taking the first 7 characters, because hash truncations cause collisions requiring expensive DB deduplication. Instead, use a distributed auto-incrementing 64-bit ID generator (like Twitter Snowflake or centralized Redis INCR). Convert the 64-bit integer ID into Base62 (62 characters: [a-zA-Z0-9]). A 7-character Base62 string yields 62^7 = 3.52 trillion unique combinations. Because every integer ID is unique, every Base62 short URL is mathematically guaranteed collision-free."
                },
                {
                    "q": "In a URL shortener, what is the trade-off between returning HTTP 301 Permanent Redirect vs HTTP 302 Temporary Redirect?",
                    "a": "HTTP 301 Permanent Redirect instructs the user's browser to cache the target long URL locally. Subsequent visits redirect instantly from browser cache without hitting the URL shortener server, significantly reducing backend load. However, because the server is bypassed, you lose click analytics (tracking timestamps, user devices, geolocations). HTTP 302 Temporary Redirect forces every request through the shortener, enabling precise real-time analytics at the cost of higher server traffic."
                },
                {
                    "q": "Explain the Token Bucket algorithm for API rate limiting and compare it to Leaky Bucket.",
                    "a": "Token Bucket: A bucket with maximum capacity B holds tokens. Tokens are added at a constant rate R per second. Each incoming request consumes 1 token. If tokens are available, the request proceeds; if empty, it is rejected (HTTP 429 Too Many Requests). Token Bucket allows bursts of traffic up to capacity B. Leaky Bucket: Requests enter a FIFO queue of fixed capacity and leak out at a strictly constant rate. Excess requests overflow and are dropped. Leaky bucket smooths out bursts into a constant flow."
                },
                {
                    "q": "Why must Redis Rate Limiter operations be executed using atomic Lua scripts?",
                    "a": "A rate limiter involves reading the current counter, checking if it exceeds the limit, incrementing the counter, and resetting TTL. In a distributed multi-threaded system, concurrent requests cause race conditions where two simultaneous requests read counter = 99 (limit 100) and both increment, allowing 101 requests through. A Redis Lua script (`EVAL`) executes entirely atomically inside Redis's single-threaded event loop, preventing race conditions without distributed locks."
                },
                {
                    "q": "How does Twitter Snowflake generate unique IDs in a distributed system without coordination?",
                    "a": "Snowflake generates 64-bit integers composed of: 1 bit unused (sign bit = 0), 41 bits timestamp in milliseconds (gives 69 years of IDs), 10 bits machine/worker ID (supports 1024 distinct server nodes), and 12 bits sequence number (allows 4096 IDs per millisecond per machine). Because each machine generates IDs independently using its hardware clock and worker ID, no inter-server network coordination or database locking is needed."
                }
            ],
            "mcqs": [
                {
                    "id": "CS-30-01",
                    "question": "How many unique short URLs can be generated with a 7-character Base62 string?",
                    "options": ["62 * 7 = 434", "7^62", "62^7 (approx 3.52 trillion)", "2^32"],
                    "correct_answer": "C",
                    "explanation": "62 alphanumeric choices per position for 7 positions gives 62^7 = ~3.52 trillion unique combinations."
                },
                {
                    "id": "CS-30-02",
                    "question": "Which HTTP status code should a URL shortener return if click tracking analytics are required for every click?",
                    "options": ["301 Moved Permanently", "302 Found (Temporary Redirect)", "200 OK", "404 Not Found"],
                    "correct_answer": "B",
                    "explanation": "HTTP 302 forces client browsers to hit the server on every click, allowing accurate telemetry collection."
                },
                {
                    "id": "CS-30-03",
                    "question": "Which rate limiting algorithm allows short bursts of traffic up to bucket capacity while maintaining an average rate?",
                    "options": ["Fixed Window", "Token Bucket", "Leaky Bucket", "Round Robin"],
                    "correct_answer": "B",
                    "explanation": "Token Bucket permits bursts of traffic as long as tokens remain in the bucket."
                },
                {
                    "id": "CS-30-04",
                    "question": "In distributed rate limiting with Redis, atomic execution of check-and-increment operations is achieved using:",
                    "options": ["Two-Phase Commit", "Lua Scripts", "Multi-threading", "CRCs"],
                    "correct_answer": "B",
                    "explanation": "Redis executes Lua scripts atomically in its event loop, preventing race condition bypasses."
                },
                {
                    "id": "CS-30-05",
                    "question": "How many bits are allocated for timestamp in Twitter Snowflake 64-bit ID generation?",
                    "options": ["12 bits", "20 bits", "41 bits", "60 bits"],
                    "correct_answer": "C",
                    "explanation": "Snowflake uses 41 bits for millisecond timestamps, providing 69 years of lifespan."
                }
            ]
        }
    }

    return modules.get(day, modules[1])
