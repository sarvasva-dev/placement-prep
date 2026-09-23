import os
import sys
import json

# Add previous handbook src to sys.path to ingest verified days 1 to 18
HANDBOOK_SRC = r"D:\Projects\Placement_Master_Handbook\src"
if HANDBOOK_SRC not in sys.path:
    sys.path.insert(0, HANDBOOK_SRC)

WEB_ROOT = r"D:\Projects\Placement_Master_Handbook_Web"
CONTENT_DIR = os.path.join(WEB_ROOT, "content")
DAYS_DIR = os.path.join(CONTENT_DIR, "days")
os.makedirs(DAYS_DIR, exist_ok=True)

# Container for captured days
captured_days = {}

def mock_render_day_block(doc, day_num, title, **kwargs):
    sem = kwargs.get('sem_data', {})
    if 'comparison_table' in sem and sem['comparison_table']:
        table = sem['comparison_table']
        headers = table[0]
        rows = table[1]
        sem['comparison_table'] = {'headers': headers, 'rows': rows}
    
    # Clean up any non-serializable objects if present
    captured_days[day_num] = {
        'day': day_num,
        'title': title,
        'sem_data': kwargs.get('sem_data', {}),
        'sgpa_target': kwargs.get('sgpa_target', {}),
        'apt_data': kwargs.get('apt_data', {}),
        'dsa_problems': kwargs.get('dsa_problems', []),
        'cs_core': kwargs.get('cs_core', {}),
        'project_defense': kwargs.get('project_defense', {}),
        'daily_test': kwargs.get('daily_test', {})
    }

# Mock the render function
import part13_textbook_days
part13_textbook_days.render_day_block = mock_render_day_block

print("--> Ingesting Days 1 to 18 from verified curriculum...")
for i in range(1, 19):
    mod_name = f"curriculum.day{i:02d}"
    try:
        mod = __import__(mod_name, fromlist=['render'])
        mod.render(None)
        print(f"    Ingested Day {i:02d}: {captured_days[i]['title']}")
    except Exception as e:
        print(f"    Error on Day {i:02d}: {e}")

# Now define Days 19 to 30 with publication-grade pedagogical depth
print("--> Generating Days 19 to 30 with complete textbook depth...")

# DAY 19
captured_days[19] = {
    "day": 19,
    "title": "Numerical Iterative Solvers (Gauss-Seidel & Jacobi), Blood Relations & Multi-Source BFS",
    "sem_data": {
        "subject": "BCA-5004 Numerical Methods",
        "topic": "Unit III — Iterative Solvers for Linear Systems: Gauss-Jacobi & Gauss-Seidel Methods",
        "detailed_notes": [
            "Iterative methods compute successive approximations to the solution vector X of a linear system A*X = B, starting from an initial guess X^(0) = (0, 0, ..., 0)^T. Unlike direct elimination methods (which suffer from round-off accumulation), iterative methods are self-correcting and computationally superior for large sparse systems.",
            "1. Strict Diagonal Dominance (Sufficient Condition for Convergence):\n"
            "An n x n matrix A is strictly diagonally dominant if in every row, the absolute value of the diagonal element is strictly greater than the sum of the absolute values of all other off-diagonal elements:\n"
            "|a_ii| > sum_{j != i} |a_ij| for all i = 1, 2, ..., n.\n"
            "If a system is not diagonally dominant, rows must be interchanged (pivoted) before starting iterations.",
            "2. Gauss-Jacobi Iteration Method:\n"
            "From the system:\n"
            "a11*x + a12*y + a13*z = b1\n"
            "a21*x + a22*y + a23*z = b2\n"
            "a31*x + a32*y + a33*z = b3\n"
            "Solve for each diagonal variable:\n"
            "x^(k+1) = (1/a11) * [b1 - a12*y^(k) - a13*z^(k)]\n"
            "y^(k+1) = (1/a22) * [b2 - a21*x^(k) - a23*z^(k)]\n"
            "z^(k+1) = (1/a33) * [b3 - a31*x^(k) - a32*y^(k)]\n"
            "In Jacobi's method, the new vector X^(k+1) is computed using strictly the values from the previous iteration k. No newly computed value is used within the current iteration.",
            "3. Gauss-Seidel Iteration Method (Successive Displacements):\n"
            "Gauss-Seidel accelerates convergence by using newly computed values as soon as they become available:\n"
            "x^(k+1) = (1/a11) * [b1 - a12*y^(k) - a13*z^(k)]\n"
            "y^(k+1) = (1/a22) * [b2 - a21*x^(k+1) - a23*z^(k)]  <-- Uses newly calculated x^(k+1)!\n"
            "z^(k+1) = (1/a33) * [b3 - a31*x^(k+1) - a32*y^(k+1)]  <-- Uses newly calculated x^(k+1) and y^(k+1)!\n"
            "Convergence Rate: The Gauss-Seidel method generally converges approximately TWICE as fast as the Jacobi method because the spectral radius of the Gauss-Seidel iteration matrix is strictly smaller: rho(T_GS) = (rho(T_J))^2."
        ],
        "diagram_ascii": (
            "+-------------------------------------------------------------------------+\n"
            "|                GAUSS-JACOBI VS GAUSS-SEIDEL UPDATE FLOW                 |\n"
            "+-------------------------------------------------------------------------+\n"
            "|  1. GAUSS-JACOBI (Simultaneous Updates from Iteration k):               |\n"
            "|     [ x(k), y(k), z(k) ] ======> [ x(k+1) ]                             |\n"
            "|     [ x(k), y(k), z(k) ] ======> [ y(k+1) ]                             |\n"
            "|     [ x(k), y(k), z(k) ] ======> [ z(k+1) ]                             |\n"
            "|                                                                         |\n"
            "|  2. GAUSS-SEIDEL (Immediate Successive Replacement):                    |\n"
            "|     [ y(k), z(k) ] ------------> [ x(k+1) ]                             |\n"
            "|                                     |                                   |\n"
            "|     [ x(k+1), z(k) ] <--------------+----> [ y(k+1) ]                   |\n"
            "|                                               |                         |\n"
            "|     [ x(k+1), y(k+1) ] <----------------------+----> [ z(k+1) ]         |\n"
            "+-------------------------------------------------------------------------+"
        ),
        "comparison_table": {
            "headers": ["Parameter", "Gauss-Jacobi Method", "Gauss-Seidel Method"],
            "rows": [
                ["Update Strategy", "Simultaneous (uses old values x^(k), y^(k), z^(k))", "Immediate substitution (uses x^(k+1) immediately)"],
                ["Rate of Convergence", "Standard (requires more iterations)", "Twice as fast as Jacobi (rho_GS = (rho_J)^2)"],
                ["Memory Requirement", "Needs 2 complete vectors (X^(k) and X^(k+1)) in RAM", "Needs only 1 vector in RAM (overwritten in-place)"],
                ["Parallelizability", "Highly parallelizable (each row is independent)", "Sequential dependency within iteration"],
                ["Convergence Condition", "Guaranteed if strictly diagonally dominant", "Guaranteed if strictly diagonally dominant or symmetric positive definite"]
            ]
        },
        "memorize": "Strict Diagonal Dominance: |a_ii| > sum_{j!=i} |a_ij|. Gauss-Seidel overwrites in-place and converges ~2x faster. Stop when |x^(k+1) - x^(k)| < epsilon.",
        "understand": "Why does Gauss-Seidel converge faster? Because x^(k+1) is a closer approximation to the true root x* than x^(k). By immediately plugging this improved approximation into the equations for y and z within the same iteration, the error decays exponentially faster.",
        "common_mistakes": "1. Forgetting to rearrange equations into diagonally dominant form before starting iterations. 2. Using old x^(k) in Gauss-Seidel instead of the newly computed x^(k+1).",
        "pyq_year": "CSJMU BCA-5004 (2021, 2022-23, 2023-24, 2024-25)",
        "pyq_freq": "4 Consecutive University Sessions (Q4/Q5 - 15 Marks Core Question)",
        "pyq_question": "State the condition of diagonal dominance. Solve the following system using Gauss-Seidel method correct to 3 decimal places (start with x0=y0=z0=0): 27x + 6y - z = 85; 6x + 15y + 2z = 72; x + y + 54z = 110. (15 Marks)",
        "pyq_rubric": "Diagonal dominance verification (3 marks) + Iteration formulas (3 marks) + 4 Hand iterations with values (6 marks) + Final correct values (3 marks) = 15 Marks.",
        "model_answer_paragraphs": [
            ("1. Condition of Strict Diagonal Dominance:",
             "A system of linear equations A*X = B is strictly diagonally dominant if in each row, the magnitude of the diagonal element exceeds the sum of the magnitudes of the other coefficients in that row:\n"
             "Row 1: |27| = 27 > |6| + |-1| = 7 (Satisfied: 27 > 7)\n"
             "Row 2: |15| = 15 > |6| + |2| = 8 (Satisfied: 15 > 8)\n"
             "Row 3: |54| = 54 > |1| + |1| = 2 (Satisfied: 54 > 2)\n"
             "Since all rows satisfy strict diagonal dominance, the Gauss-Seidel iteration is guaranteed to converge to a unique solution."),
            ("2. Gauss-Seidel Iterative Equations:",
             "x^(k+1) = (85 - 6*y^(k) + z^(k)) / 27\n"
             "y^(k+1) = (72 - 6*x^(k+1) - 2*z^(k)) / 15\n"
             "z^(k+1) = (110 - x^(k+1) - y^(k+1)) / 54\n"
             "Initial approximation: x^(0) = 0, y^(0) = 0, z^(0) = 0."),
            ("3. Step-by-Step Iterations:",
             "• Iteration 1:\n"
             "x^(1) = (85 - 0 + 0) / 27 = 3.1481\n"
             "y^(1) = (72 - 6*(3.1481) - 0) / 15 = (72 - 18.8889) / 15 = 3.5407\n"
             "z^(1) = (110 - 3.1481 - 3.5407) / 54 = 103.3112 / 54 = 1.9132\n\n"
             "• Iteration 2:\n"
             "x^(2) = (85 - 6*(3.5407) + 1.9132) / 27 = (85 - 21.2442 + 1.9132) / 27 = 65.6690 / 27 = 2.4322\n"
             "y^(2) = (72 - 6*(2.4322) - 2*(1.9132)) / 15 = (72 - 14.5932 - 3.8264) / 15 = 53.5804 / 15 = 3.5720\n"
             "z^(2) = (110 - 2.4322 - 3.5720) / 54 = 103.9958 / 54 = 1.9258\n\n"
             "• Iteration 3:\n"
             "x^(3) = (85 - 6*(3.5720) + 1.9258) / 27 = (85 - 21.4320 + 1.9258) / 27 = 65.4938 / 27 = 2.4257\n"
             "y^(3) = (72 - 6*(2.4257) - 2*(1.9258)) / 15 = (72 - 14.5542 - 3.8516) / 15 = 53.5942 / 15 = 3.5730\n"
             "z^(3) = (110 - 2.4257 - 3.5730) / 54 = 104.0013 / 54 = 1.9260\n\n"
             "• Iteration 4:\n"
             "x^(4) = (85 - 6*(3.5730) + 1.9260) / 27 = 2.4255\n"
             "y^(4) = (72 - 6*(2.4255) - 2*(1.9260)) / 15 = 3.5730\n"
             "z^(4) = (110 - 2.4255 - 3.5730) / 54 = 1.9259"),
            ("4. Final Solution:",
             "Rounding to 3 decimal places:\n"
             "x = 2.426\n"
             "y = 3.573\n"
             "z = 1.926\n"
             "Verification: 27*(2.4255) + 6*(3.5730) - 1.9260 = 65.4885 + 21.438 - 1.9260 = 85.0005 ≈ 85. Exact match.")
        ]
    },
    "sgpa_target": {"focus": "Gauss-Seidel Convergence & Hand Calculations", "milestone": "Full 15/15 Marks on Numerical Linear Solvers"},
    "apt_data": {
        "topic": "Logical Reasoning — Blood Relations & Family Tree Deduction",
        "tutorial": [
            "Blood Relations problems evaluate systematic logical deduction. Always draw a 3-tier Family Tree using standardized notation:\n"
            "• Male: [+] or Box. Female: [-] or Circle.\n"
            "• Married Couple: Double horizontal line (=). Siblings: Single horizontal line (-).\n"
            "• Generations: Vertical downward line (|).",
            "Key Relationship Terms:\n"
            "• Maternal: Mother's side (Maternal Uncle = Mother's brother).\n"
            "• Paternal: Father's side (Paternal Uncle = Father's brother).\n"
            "• In-Laws: Spouse's relatives (Father-in-law = Spouse's father; Sister-in-law = Brother's wife or Spouse's sister).\n"
            "• Nephew = Brother's or Sister's son; Niece = Brother's or Sister's daughter.",
            "Coded Relations Method:\n"
            "Break expressions from right to left or create generation tree: e.g., P + Q * R - S where '+' is father, '*' is sister, '-' is brother."
        ],
        "formulas": "Generational delta: Same gen = 0 (brother, wife), Parents = +1, Grandparents = +2, Children = -1, Grandchildren = -2.",
        "shortcut": "Gender Elimination: If asked 'How is P related to Q (e.g. uncle)?', eliminate any option where P's deduced gender is female or undefined.",
        "recognition": "Look for 'Pointing to a photograph, a man said...', or coded expressions 'A @ B # C $ D' in TCS Digital, Infosys, and Cognizant.",
        "tier1_problem": "Pointing to a photograph, Rohit said, 'She is the daughter of my grandfather's only son.' How is the girl in the photograph related to Rohit?",
        "tier1_solution": "Breakdown: 'My grandfather's only son' = Rohit's father. 'Daughter of Rohit's father' = Rohit's sister. Answer: Sister.",
        "tier2_problem": "A is B's brother. C is A's mother. D is C's father. E is B's son. How is D related to E?",
        "tier2_solution": "Generational steps: E is child of B (Gen -1). B and A are siblings (Gen 0). C is mother of A and B (Gen +1). D is father of C (Gen +2). From E to D is 3 generational steps upward: Great-grandfather. Answer: Great-grandfather.",
        "tier3_problem": "[TCS NQT Coded Pattern] If 'P + Q' means P is father of Q; 'P - Q' means P is wife of Q; 'P * Q' means P is brother of Q; 'P / Q' means P is daughter of Q. If equation is S / T + U * V - W, how is S related to W?",
        "tier3_solution": "Analyze: T + U ==> T is father of U. U * V ==> U is brother of V. V - W ==> V is wife of W (so W is husband). S / T ==> S is daughter of T. Since T is father of U, V, and S, S is the sister of V. W is V's husband. Therefore, S is W's wife's sister, which is Sister-in-law. Answer: Sister-in-law.",
        "tier4_problem": "In a family of 6 people (A, B, C, D, E, F), there are 2 married couples. D is grandmother of A and mother of B. C is wife of B and mother of F. F is granddaughter of E. Who is the husband of D?",
        "tier4_solution": "D is grandmother of A and mother of B. C is wife of B ==> Couple 1: B (husband) = C (wife). They have children A and F. Since D is grandmother and there are 2 married couples, D must be married to the grandfather. F is granddaughter of E, so E is the grandfather. Therefore, Couple 2: E (husband) = D (wife). Answer: E.",
        "speed_drills": [
            {"q": "A man said to a lady, 'Your mother's husband's sister is my aunt.' How is the lady related to the man?", "a": "'Your mother's husband' = lady's father. 'Father's sister' = lady's aunt. If lady's aunt is man's aunt, lady is man's Sister."},
            {"q": "Introducing a boy, a girl said, 'He is the son of the daughter of the father of my uncle.' How is boy related to girl?", "a": "'Father of my uncle' = Grandfather. 'Daughter of grandfather' = Mother (or Aunt). 'Son of mother/aunt' = Brother (or Cousin)."},
            {"q": "If M is sister of N, N is brother of P, and P is father of Q, how is M related to Q?", "a": "P is father of Q. M is sister of P. Father's sister is Aunt."},
            {"q": "P is father of R, but R is not his son. What is R to P?", "a": "R is his Daughter."},
            {"q": "A is father of C and D is son of B. E is brother of A. If C is sister of D, how is B related to E?", "a": "C is daughter of A. D is brother of C. D is son of B ==> B is mother of C and D, so B is wife of A. E is brother of A. B is Sister-in-law of E."}
        ]
    },
    "dsa_problems": [
        {
            "title": "Rotting Oranges (LeetCode 994 - Medium)",
            "difficulty": "Medium",
            "importance": "Top-tier Multi-Source BFS Placement Problem (Amazon, Google, TCS Digital)",
            "problem_statement": "You are given an m x n grid where: 0 represents an empty cell, 1 represents a fresh orange, and 2 represents a rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.",
            "solution_approach": (
                "Multi-Source Breadth-First Search (BFS):\n"
                "1. Initialize a queue and count total fresh oranges.\n"
                "2. Add ALL initially rotten oranges (cells with value 2) to the queue simultaneously at minute 0.\n"
                "3. Process queue level by level (each level represents 1 elapsed minute).\n"
                "4. For each rotten orange, infect its 4 neighbors: if neighbor is 1, set to 2, decrement fresh count, and append neighbor to queue.\n"
                "5. Return elapsed minutes if fresh == 0, else -1."
            ),
            "code": (
                "from collections import deque\n\n"
                "def orangesRotting(grid: list[list[int]]) -> int:\n"
                "    rows, cols = len(grid), len(grid[0])\n"
                "    queue = deque()\n"
                "    fresh_count = 0\n"
                "    \n"
                "    # Step 1: Collect all initial rotten oranges & count fresh\n"
                "    for r in range(rows):\n"
                "        for c in range(cols):\n"
                "            if grid[r][c] == 2:\n"
                "                queue.append((r, c))\n"
                "            elif grid[r][c] == 1:\n"
                "                fresh_count += 1\n"
                "                \n"
                "    if fresh_count == 0:\n"
                "        return 0\n"
                "        \n"
                "    minutes = 0\n"
                "    directions = [(1,0), (-1,0), (0,1), (0,-1)]\n"
                "    \n"
                "    # Step 2: Multi-source BFS\n"
                "    while queue and fresh_count > 0:\n"
                "        minutes += 1\n"
                "        for _ in range(len(queue)):\n"
                "            r, c = queue.popleft()\n"
                "            for dr, dc in directions:\n"
                "                nr, nc = r + dr, c + dc\n"
                "                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:\n"
                "                    grid[nr][nc] = 2\n"
                "                    fresh_count -= 1\n"
                "                    queue.append((nr, nc))\n"
                "                    \n"
                "    return minutes if fresh_count == 0 else -1"
            ),
            "line_by_line": [
                ("queue.append((r, c)) if grid[r][c] == 2", "Enqueue all sources of infection simultaneously at time t=0."),
                ("while queue and fresh_count > 0", "Continue while fresh oranges exist to prevent incrementing minutes after all oranges rot."),
                ("for _ in range(len(queue))", "Snapshot queue size to process all nodes at the exact same minute level."),
                ("grid[nr][nc] = 2; fresh_count -= 1", "Infect fresh orange in-place and decrement remaining tally.")
            ],
            "time_complexity": "O(M * N) — Every cell is visited at most twice.",
            "space_complexity": "O(M * N) — Queue stores at most M*N cells in worst case.",
            "edge_cases": "No fresh oranges initially (returns 0); isolated fresh orange surrounded by 0s (returns -1)."
        },
        {
            "title": "Pacific Atlantic Water Flow (LeetCode 417 - Medium)",
            "difficulty": "Medium",
            "importance": "High-Frequency Reverse Graph Traversal Problem",
            "problem_statement": "There is an m x n rectangular island that borders both the Pacific Ocean (top and left edges) and Atlantic Ocean (bottom and right edges). Water can flow from a cell to an adjacent cell of equal or lower height. Return a list of grid coordinates where water can flow to both oceans.",
            "solution_approach": (
                "Reverse Traversal from Ocean Borders:\n"
                "Instead of checking if water from every cell can reach both oceans (slow O((M*N)^2)), reverse the flow!\n"
                "1. Start BFS/DFS from ocean boundary cells and climb uphill (water flows to height >= current height).\n"
                "2. Maintain two visited sets: `pacific_reachable` and `atlantic_reachable`.\n"
                "3. The intersection of both sets `pacific_reachable & atlantic_reachable` gives cells that can reach both oceans."
            ),
            "code": (
                "def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:\n"
                "    if not heights or not heights[0]:\n"
                "        return []\n"
                "    \n"
                "    rows, cols = len(heights), len(heights[0])\n"
                "    pacific = set()\n"
                "    atlantic = set()\n"
                "    \n"
                "    def dfs(r: int, c: int, visited: set):\n"
                "        visited.add((r, c))\n"
                "        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:\n"
                "            nr, nc = r + dr, c + dc\n"
                "            # Climb uphill (heights[nr][nc] >= heights[r][c])\n"
                "            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:\n"
                "                if heights[nr][nc] >= heights[r][c]:\n"
                "                    dfs(nr, nc, visited)\n"
                "                    \n"
                "    # Pacific: Top row & Left col | Atlantic: Bottom row & Right col\n"
                "    for c in range(cols):\n"
                "        dfs(0, c, pacific)\n"
                "        dfs(rows - 1, c, atlantic)\n"
                "    for r in range(rows):\n"
                "        dfs(r, 0, pacific)\n"
                "        dfs(r, cols - 1, atlantic)\n"
                "        \n"
                "    return list(pacific.intersection(atlantic))"
            ),
            "line_by_line": [
                ("dfs(0, c, pacific); dfs(rows - 1, c, atlantic)", "Initialize reverse flood from ocean borders."),
                ("if heights[nr][nc] >= heights[r][c]", "Water flows backwards uphill from ocean towards peak cells."),
                ("pacific.intersection(atlantic)", "Cells present in both reachable sets satisfy bi-ocean drainage.")
            ],
            "time_complexity": "O(M * N) — Each cell visited at most twice (once for Pacific, once for Atlantic).",
            "space_complexity": "O(M * N) — Recursion stack and visited hash sets.",
            "edge_cases": "1x1 grid (always reaches both); all cells same height; strictly strictly descending plateau."
        }
    ],
    "cs_core": {
        "subject": "Operating Systems",
        "topic": "File Systems Architecture: Inodes, Superblocks & Hard vs Soft Links",
        "detailed_notes": [
            "Unix/Linux File System Architecture:\n"
            "1. Boot Block: First sector of storage used by BIOS/UEFI to bootstrap the OS kernel.\n"
            "2. Superblock: Stores metadata about the file system itself: total block count, free block count, inode table size, block size (typically 4KB), and file system status flags.\n"
            "3. Inode Table (Index Nodes): Every file or directory has an Inode storing: file type, permissions, owner UID/GID, size, timestamps (atime, mtime, ctime), and pointers to physical disk data blocks.\n"
            "• Crucial Fact: An Inode does NOT store the filename! Filenames are stored in directory data blocks mapping `filename -> inode_number`.",
            "Hard Links vs Symbolic (Soft) Links:\n"
            "• Hard Link: An additional directory entry pointing directly to the SAME Inode number. Both links share identical permissions, size, and data blocks. Deleting one hard link decrements the Inode's link count; file data is freed only when link count reaches 0 and no open file descriptors exist. Hard links cannot span across different file systems/partitions and cannot link directories.\n"
            "• Soft/Symbolic Link (Symlink): A distinct file with its OWN unique Inode that contains a text string representing the pathname of the target file. If the target file is deleted or renamed, the symlink breaks ('dangling link'). Symlinks can cross file system boundaries and can link directories."
        ],
        "interview_qa": [
            {
                "q": "What happens on disk when you run the command `rm file.txt` in Linux?",
                "a": "The `rm` command invokes the `unlink()` system call. It removes the filename entry mapping from the directory block and decrements the `st_nlink` counter in the file's Inode. If the link count drops to 0 AND no active process currently holds an open file descriptor to that Inode, the OS frees the Inode and marks the allocated data blocks as free in the allocation bitmap for future overwriting. The raw magnetic/SSD bits are not immediately zeroed out."
            },
            {
                "q": "Why can Hard Links not cross filesystem boundaries while Soft Links can?",
                "a": "Because an Inode number is only unique within its local filesystem partition. If a hard link pointed to Inode 1042 on a different partition, Inode 1042 there might represent a completely different file or directory. In contrast, a Soft Link simply stores an absolute or relative filesystem path string (`/mnt/data/doc.pdf`), which the virtual filesystem (VFS) resolves dynamically across mount points."
            }
        ]
    },
    "project_defense": {
        "project_name": "BulkBeat TV (NSE2)",
        "feature_focus": "Telegram Bot Integration & Asynchronous Webhook Architecture",
        "architecture_deep_dive": (
            "In BulkBeat TV, real-time alert broadcasts and interactive administrative controls are delivered via "
            "a Telegram Bot integrated directly into the `aiohttp` web server.\n\n"
            "1. Long Polling vs Webhook Architecture:\n"
            "Long polling requires the backend to keep sending repeated HTTP GET requests to Telegram servers (`getUpdates`), "
            "wasting network bandwidth and introducing latency. BulkBeat TV uses Webhooks: Telegram pushes incoming user commands "
            "instantly via HTTP POST to a secure endpoint `/api/telegram/webhook`.\n\n"
            "2. Security & Verification:\n"
            "• Requests are verified using a custom `X-Telegram-Bot-Api-Secret-Token` header set during webhook registration.\n"
            "• Requests failing HMAC or secret token validation are dropped immediately with HTTP 403 Forbidden.\n\n"
            "3. Non-Blocking Message Dispatching:\n"
            "Broadcasting notifications to thousands of subscribers uses an `asyncio.Queue`. Worker tasks read messages from the queue "
            "and call Telegram's `sendMessage` with exponential backoff on HTTP 429 (Too Many Requests), ensuring API rate limits are never violated."
        ),
        "interview_qa": [
            {
                "q": "Why did you choose Telegram Webhooks over Long Polling in BulkBeat TV?",
                "a": "Webhooks provide event-driven push architecture. Instead of wasting CPU cycles and socket pools continuously polling Telegram's servers every 2 seconds, Telegram pushes messages to my FastAPI/aiohttp server only when an event occurs. This reduced idle CPU utilization and allowed instantaneous delivery of alerts to paying subscribers."
            },
            {
                "q": "How did you prevent Telegram broadcast messages from triggering HTTP 429 Too Many Requests rate limit errors?",
                "a": "Telegram imposes a limit of 30 messages per second across chats and 1 message per second in a specific private chat. I implemented a token bucket rate-limiter over an `asyncio.Queue` that batches messages, limits outbound dispatch to 25 requests/sec, and catches HTTP 429 responses with `Retry-After` backoffs."
            }
        ]
    },
    "daily_test": {
        "day": 19,
        "questions": [
            {"q": "State the condition of strict diagonal dominance for an n x n matrix.", "a": "|a_ii| > sum_{j!=i} |a_ij| for all rows i = 1, 2, ..., n. The diagonal magnitude must strictly exceed the sum of all other off-diagonal magnitudes in that row."},
            {"q": "Why does Gauss-Seidel converge faster than the Gauss-Jacobi method?", "a": "Because Gauss-Seidel utilizes newly computed values x^(k+1), y^(k+1) immediately within the current iteration instead of waiting for the next iteration cycle, reducing the spectral radius of the iteration matrix."},
            {"q": "A is B's sister. C is B's mother. D is C's father. How is A related to D?", "a": "Granddaughter. C is mother of A and B; D is father of C, making A the granddaughter of D."},
            {"q": "What is the time complexity of the Multi-Source BFS in Rotting Oranges (LeetCode 994)?", "a": "O(M * N) where M is rows and N is columns. Every grid cell is processed at most once."},
            {"q": "Does an Inode store the filename in a Linux filesystem? Where is it stored?", "a": "No, an Inode does not store the filename. Filenames are stored inside directory blocks as key-value pairs mapping `filename -> inode_number`."},
            {"q": "What happens to file data when a hard link is deleted?", "a": "The Inode link counter is decremented by 1. The data blocks remain intact as long as the link count is greater than 0."},
            {"q": "In Pacific Atlantic Water Flow, why do we reverse the search from ocean borders instead of searching from each land cell?", "a": "Searching from land cells has worst-case complexity O((M*N)^2). Reversing from ocean borders visits each cell at most twice, reducing complexity to optimal O(M * N)."},
            {"q": "How does BulkBeat TV verify that webhook requests actually originated from Telegram?",
             "a": "By configuring a secret token during `setWebhook` and verifying the incoming `X-Telegram-Bot-Api-Secret-Token` header on every request, rejecting unauthorized traffic with HTTP 403."}
        ]
    }
}

# Write a runner script to populate the remaining days and generate JSONs
print("Day 19 defined successfully.")
