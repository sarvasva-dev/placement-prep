/**
 * DSA Animated Visualizer Engine
 * ================================
 * Provides real interactive step-by-step animated visualizations for DSA patterns.
 *
 * Visualizer types:
 *   - ArrayVisualizer      (colored cells + value labels)
 *   - PointerVisualizer    (array + L/R pointer arrows with labels)
 *   - SlidingWindowViz     (array + highlighted window region)
 *   - BinarySearchViz      (array + lo/mid/hi markers)
 *   - LinkedListViz        (nodes + next arrows)
 *   - StackViz             (vertical push/pop)
 *   - QueueViz             (horizontal enqueue/dequeue)
 *   - TreeViz              (binary tree traversal highlight)
 *   - SortingViz           (animated bar chart)
 *
 * Each visualizer supports:
 *   - Play / Pause
 *   - Next Step / Previous Step
 *   - Reset to initial state
 *   - Speed control: 0.5x / 1x / 1.5x / 2x
 *   - Step counter: "Step X / N"
 *   - Action label + Explanation
 *   - Code-line highlight (if code lines provided in dry_run)
 */

// ── Dry-run step data derivation ─────────────────────────────────────────────

/**
 * Build dry-run steps from dsaPattern.dry_run text + dsaPattern data.
 * Falls back to pattern-type-specific demo steps if no structured dry_run.
 */
function buildDryRunSteps(dsaPattern) {
  const patternName = (dsaPattern.pattern_name || '').toLowerCase();
  const dryRun = dsaPattern.dry_run || dsaPattern.dry_run_steps || '';

  // If structured steps exist
  if (Array.isArray(dsaPattern.dry_run_steps)) {
    return dsaPattern.dry_run_steps;
  }

  // Build from pattern type
  if (patternName.includes('two pointer') || patternName.includes('two-pointer') ||
      patternName.includes('opposite direction')) {
    return buildTwoPointersSteps();
  }
  if (patternName.includes('sliding window') || patternName.includes('fixed size')) {
    return buildSlidingWindowSteps();
  }
  if (patternName.includes('fast') && patternName.includes('slow')) {
    return buildFastSlowSteps();
  }
  if (patternName.includes('binary search')) {
    return buildBinarySearchSteps();
  }
  if (patternName.includes('stack') || patternName.includes('monotonic stack')) {
    return buildStackSteps();
  }
  if (patternName.includes('queue')) {
    return buildQueueSteps();
  }
  if (patternName.includes('linked list')) {
    return buildLinkedListSteps();
  }
  if (patternName.includes('tree') || patternName.includes('traversal') || patternName.includes('bfs') ||
      patternName.includes('dfs') || patternName.includes('bst') || patternName.includes('lca')) {
    return buildTreeSteps();
  }
  if (patternName.includes('sort')) {
    return buildSortingSteps();
  }
  if (patternName.includes('heap') || patternName.includes('priority')) {
    return buildHeapSteps();
  }
  if (patternName.includes('dp') || patternName.includes('dynamic programming') ||
      patternName.includes('knapsack') || patternName.includes('lcs') || patternName.includes('lis')) {
    return buildDPSteps();
  }
  if (patternName.includes('graph') || patternName.includes('bfs') || patternName.includes('dijkstra') ||
      patternName.includes('topological') || patternName.includes('union-find') || patternName.includes('disjoint')) {
    return buildGraphSteps();
  }

  // Generic array demonstration
  return buildGenericArraySteps();
}

// ── Specific step builders ─────────────────────────────────────────────────

function buildTwoPointersSteps() {
  const arr = [2, 7, 11, 15];
  const target = 9;
  return [
    { step: 1, type: 'two_pointer', array: arr, left: 0, right: 3, highlight: [], action: 'Initialize: L=0 (val=2), R=3 (val=15)', explanation: 'Place left pointer at index 0 and right pointer at last index', code_lines: [4, 5] },
    { step: 2, type: 'two_pointer', array: arr, left: 0, right: 3, highlight: [0, 3], action: `sum = arr[L]+arr[R] = 2+15 = 17 > target(${target}) → R--`, explanation: 'Sum 17 exceeds target 9, so we need a smaller value — move right pointer left', code_lines: [7, 8] },
    { step: 3, type: 'two_pointer', array: arr, left: 0, right: 2, highlight: [0, 2], action: `sum = arr[L]+arr[R] = 2+11 = 13 > target(${target}) → R--`, explanation: 'Sum 13 still exceeds target 9, move right pointer left again', code_lines: [7, 8] },
    { step: 4, type: 'two_pointer', array: arr, left: 0, right: 1, highlight: [0, 1], action: `sum = arr[L]+arr[R] = 2+7 = 9 = target(${target}) ✓ FOUND!`, explanation: 'Sum equals target! Answer is indices [1, 2] (1-indexed)', code_lines: [9, 10] },
    { step: 5, type: 'two_pointer', array: arr, left: 0, right: 1, highlight: [0, 1], action: 'Return [1, 2] — Done!', explanation: 'Two Pointers converged to the solution in O(N) time, O(1) space', code_lines: [10] }
  ];
}

function buildSlidingWindowSteps() {
  const arr = [1, 3, -1, -3, 5, 3, 6, 7];
  const k = 3;
  return [
    { step: 1, type: 'sliding_window', array: arr, window_start: 0, window_end: 2, highlight: [0, 1, 2], action: 'Initialize window [0..2]: sum = 1+3+(-1) = 3', explanation: 'Open the first window of size k=3', code_lines: [1, 2] },
    { step: 2, type: 'sliding_window', array: arr, window_start: 1, window_end: 3, highlight: [1, 2, 3], action: 'Slide window: remove arr[0]=1, add arr[3]=-3 → sum = 2+(-3) = -1', explanation: 'Slide the window right by removing left element and adding new right', code_lines: [5, 6] },
    { step: 3, type: 'sliding_window', array: arr, window_start: 2, window_end: 4, highlight: [2, 3, 4], action: 'Slide window: remove arr[1]=3, add arr[4]=5 → sum = -4+5 = 1', explanation: 'Window continues sliding', code_lines: [5, 6] },
    { step: 4, type: 'sliding_window', array: arr, window_start: 3, window_end: 5, highlight: [3, 4, 5], action: 'Slide window → sum = 5', explanation: 'Tracking current window sum', code_lines: [5, 6] },
    { step: 5, type: 'sliding_window', array: arr, window_start: 4, window_end: 6, highlight: [4, 5, 6], action: 'Slide window → sum = 14', explanation: 'Window [5,3,6] has sum 14', code_lines: [5, 6] },
    { step: 6, type: 'sliding_window', array: arr, window_start: 5, window_end: 7, highlight: [5, 6, 7], action: 'Final window → sum = 16. Max sum = 16!', explanation: 'Window [3,6,7] is the maximum sum subarray of size k', code_lines: [7, 8] }
  ];
}

function buildFastSlowSteps() {
  // Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle back to 3)
  return [
    { step: 1, type: 'linked_list', nodes: [1, 2, 3, 4, 5], slow: 0, fast: 0, highlight: [0], action: 'Init: slow = head(1), fast = head(1)', explanation: 'Both pointers start at head', code_lines: [1, 2] },
    { step: 2, type: 'linked_list', nodes: [1, 2, 3, 4, 5], slow: 1, fast: 2, highlight: [1, 2], action: 'slow → 2 (1 step), fast → 3 (2 steps)', explanation: 'Slow moves 1 step, fast moves 2 steps', code_lines: [5, 6] },
    { step: 3, type: 'linked_list', nodes: [1, 2, 3, 4, 5], slow: 2, fast: 4, highlight: [2, 4], action: 'slow → 3, fast → 5', explanation: 'Slow and fast diverge', code_lines: [5, 6] },
    { step: 4, type: 'linked_list', nodes: [1, 2, 3, 4, 5], slow: 3, fast: 2, highlight: [3, 2], action: 'slow → 4, fast → 3 (cycle!)', explanation: 'Fast pointer wraps around — cycle exists!', code_lines: [5, 6] },
    { step: 5, type: 'linked_list', nodes: [1, 2, 3, 4, 5], slow: 4, fast: 4, highlight: [4, 4], action: 'slow == fast → CYCLE DETECTED!', explanation: 'Floyd\'s algorithm: when slow == fast, a cycle is confirmed', code_lines: [8, 9] }
  ];
}

function buildBinarySearchSteps() {
  const arr = [-1, 0, 3, 5, 9, 12];
  const target = 9;
  return [
    { step: 1, type: 'binary_search', array: arr, lo: 0, hi: 5, mid: 2, highlight: [2], action: 'lo=0, hi=5, mid=2 → arr[2]=3 < target(9) → lo=mid+1', explanation: 'Search right half', code_lines: [3, 4, 5] },
    { step: 2, type: 'binary_search', array: arr, lo: 3, hi: 5, mid: 4, highlight: [4], action: 'lo=3, hi=5, mid=4 → arr[4]=9 = target → FOUND!', explanation: 'Target found at index 4', code_lines: [6] },
    { step: 3, type: 'binary_search', array: arr, lo: 3, hi: 5, mid: 4, highlight: [4], action: 'Return index 4. Done!', explanation: 'Binary Search found target in O(log N) time', code_lines: [7] }
  ];
}

function buildStackSteps() {
  return [
    { step: 1, type: 'stack', stack: [], action: 'Initialize empty stack', explanation: 'Stack starts empty', code_lines: [1] },
    { step: 2, type: 'stack', stack: [3], action: 'Push 3 → stack: [3]', explanation: '3 has no greater element to its left yet', code_lines: [4] },
    { step: 3, type: 'stack', stack: [3, 4], action: 'Push 4 → stack: [3, 4]', explanation: 'Stack grows', code_lines: [4] },
    { step: 4, type: 'stack', stack: [4, 7], action: 'Pop 3 (4>3), push 7 → stack: [4, 7]', explanation: '7 > 4, pop 4, NGE of 4 is 7', code_lines: [5, 6] },
    { step: 5, type: 'stack', stack: [], action: 'Pop all remaining → NGE = -1', explanation: 'Elements remaining in stack have no greater element to right', code_lines: [8] }
  ];
}

function buildQueueSteps() {
  return [
    { step: 1, type: 'queue', queue: [], action: 'Initialize empty queue', explanation: 'BFS queue starts empty', code_lines: [1] },
    { step: 2, type: 'queue', queue: [1], action: 'Enqueue root: queue=[1]', explanation: 'Add root node to begin BFS', code_lines: [3] },
    { step: 3, type: 'queue', queue: [2, 3], action: 'Dequeue 1, enqueue children [2,3]', explanation: 'Process level 1', code_lines: [6, 7] },
    { step: 4, type: 'queue', queue: [3, 4, 5], action: 'Dequeue 2, enqueue children [4,5]', explanation: 'Process level 2 (left side)', code_lines: [6, 7] },
    { step: 5, type: 'queue', queue: [], action: 'BFS complete — all nodes visited', explanation: 'Queue drains level by level', code_lines: [9] }
  ];
}

function buildLinkedListSteps() {
  return [
    { step: 1, type: 'linked_list', nodes: [1, 2, 3, 4, 5], prev: -1, curr: 0, next_ptr: 1, action: 'Init: prev=null, curr=head(1), next=2', explanation: 'In-place reversal: track prev, curr, next', code_lines: [2, 3] },
    { step: 2, type: 'linked_list', nodes: [1, 2, 3, 4, 5], prev: 0, curr: 1, next_ptr: 2, action: 'curr.next=prev(1), advance: prev=1, curr=2', explanation: 'Reverse the link: node 2 now points back to node 1', code_lines: [5, 6, 7] },
    { step: 3, type: 'linked_list', nodes: [1, 2, 3, 4, 5], prev: 1, curr: 2, next_ptr: 3, action: 'curr.next=prev(2), advance: prev=2, curr=3', explanation: 'Node 3 now points back to node 2', code_lines: [5, 6, 7] },
    { step: 4, type: 'linked_list', nodes: [1, 2, 3, 4, 5], prev: 2, curr: 3, next_ptr: 4, action: 'Reverse: 4→3→2→1, curr=4', explanation: 'Continuing reversal', code_lines: [5, 6, 7] },
    { step: 5, type: 'linked_list', nodes: [5, 4, 3, 2, 1], prev: 3, curr: 4, next_ptr: -1, action: 'curr=null → Done! new head = prev(5)', explanation: 'Reversal complete. 5→4→3→2→1→null', code_lines: [9] }
  ];
}

function buildTreeSteps() {
  return [
    { step: 1, type: 'tree', tree: [1, 2, 3, 4, 5, null, 7], highlight: [0], action: 'Visit root: 1', explanation: 'Pre-order: root first (NLR)', code_lines: [2] },
    { step: 2, type: 'tree', tree: [1, 2, 3, 4, 5, null, 7], highlight: [1], action: 'Go left → Visit: 2', explanation: 'Recurse into left subtree', code_lines: [4] },
    { step: 3, type: 'tree', tree: [1, 2, 3, 4, 5, null, 7], highlight: [3], action: 'Go left → Visit: 4', explanation: 'Recurse into left-left subtree', code_lines: [4] },
    { step: 4, type: 'tree', tree: [1, 2, 3, 4, 5, null, 7], highlight: [4], action: 'Backtrack → Visit: 5', explanation: 'Right child of node 2', code_lines: [5] },
    { step: 5, type: 'tree', tree: [1, 2, 3, 4, 5, null, 7], highlight: [2], action: 'Go right → Visit: 3', explanation: 'Now recurse right subtree of root', code_lines: [5] },
    { step: 6, type: 'tree', tree: [1, 2, 3, 4, 5, null, 7], highlight: [6], action: 'Go right → Visit: 7', explanation: 'Right child of node 3. Pre-order: [1,2,4,5,3,7]', code_lines: [5] }
  ];
}

function buildSortingSteps() {
  return [
    { step: 1, type: 'sorting', array: [5, 3, 8, 1, 9, 2], comparing: [], swapped: [], action: 'Start Bubble Sort: pass 1', explanation: 'Compare adjacent elements', code_lines: [1] },
    { step: 2, type: 'sorting', array: [5, 3, 8, 1, 9, 2], comparing: [0, 1], swapped: [0, 1], action: '5 > 3 → swap → [3,5,8,1,9,2]', explanation: 'Swap 5 and 3', code_lines: [4, 5] },
    { step: 3, type: 'sorting', array: [3, 5, 8, 1, 9, 2], comparing: [2, 3], swapped: [2, 3], action: '8 > 1 → swap → [3,5,1,8,9,2]', explanation: 'Swap 8 and 1', code_lines: [4, 5] },
    { step: 4, type: 'sorting', array: [3, 5, 1, 8, 9, 2], comparing: [4, 5], swapped: [4, 5], action: '9 > 2 → swap → [3,5,1,8,2,9]', explanation: '9 bubbles to end', code_lines: [4, 5] },
    { step: 5, type: 'sorting', array: [1, 2, 3, 5, 8, 9], comparing: [], swapped: [], action: 'Final sorted: [1,2,3,5,8,9]', explanation: 'Array sorted in O(N²) time', code_lines: [8] }
  ];
}

function buildHeapSteps() {
  return [
    { step: 1, type: 'heap', array: [3, 1, 4, 1, 5, 9, 2, 6], highlight: [], action: 'Insert 3 into MinHeap', explanation: 'Add to end, then heapify-up', code_lines: [2] },
    { step: 2, type: 'heap', array: [1, 3, 4, 6, 5, 9, 2], highlight: [0], action: 'Top-K: peek min = 1', explanation: 'MinHeap always keeps smallest at root', code_lines: [5] },
    { step: 3, type: 'heap', array: [2, 3, 4, 6, 5, 9], highlight: [0], action: 'Poll min=1, heapify-down', explanation: 'Remove root, replace with last element, sift down', code_lines: [6, 7] },
    { step: 4, type: 'heap', array: [2, 3, 4, 6, 5, 9], highlight: [0], action: 'Next min = 2 at root', explanation: 'Heap property maintained after poll', code_lines: [8] }
  ];
}

function buildDPSteps() {
  // 0/1 Knapsack: items with weights [1,3,4] values [1,4,5], W=4
  return [
    { step: 1, type: 'dp_table', rows: 4, cols: 5, table: [[0,0,0,0,0],[0,1,1,1,1],[0,1,4,5,5],[0,1,4,5,6]], highlight_cell: [0,0], action: 'Init dp[0][*]=0, dp[*][0]=0', explanation: 'Base case: 0 items or 0 capacity → 0 value', code_lines: [2, 3] },
    { step: 2, type: 'dp_table', rows: 4, cols: 5, table: [[0,0,0,0,0],[0,1,1,1,1],[0,1,4,5,5],[0,1,4,5,6]], highlight_cell: [1,1], action: 'Item 1 (w=1,v=1): dp[1][1]=max(dp[0][1], dp[0][0]+1)=1', explanation: 'Include item 1 in capacity 1', code_lines: [6, 7] },
    { step: 3, type: 'dp_table', rows: 4, cols: 5, table: [[0,0,0,0,0],[0,1,1,1,1],[0,1,4,5,5],[0,1,4,5,6]], highlight_cell: [2,3], action: 'Item 2 (w=3,v=4): dp[2][3]=4', explanation: 'Adding item 2 at capacity 3 gives value 4', code_lines: [6, 7] },
    { step: 4, type: 'dp_table', rows: 4, cols: 5, table: [[0,0,0,0,0],[0,1,1,1,1],[0,1,4,5,5],[0,1,4,5,6]], highlight_cell: [3,4], action: 'Answer: dp[3][4]=6', explanation: 'Maximum value in W=4 capacity with all 3 items = 6', code_lines: [10] }
  ];
}

function buildGraphSteps() {
  return [
    { step: 1, type: 'graph', visited: [], queue: [0], action: 'BFS: Start from node 0, enqueue neighbors', explanation: 'Initialize BFS with source node', code_lines: [1, 2] },
    { step: 2, type: 'graph', visited: [0], queue: [1, 2], action: 'Visit 0, enqueue: 1, 2', explanation: 'Dequeue 0, add its unvisited neighbors', code_lines: [5, 6] },
    { step: 3, type: 'graph', visited: [0, 1], queue: [2, 3], action: 'Visit 1, enqueue: 3', explanation: 'Dequeue 1, add neighbor 3', code_lines: [5, 6] },
    { step: 4, type: 'graph', visited: [0, 1, 2], queue: [3, 4], action: 'Visit 2, enqueue: 4', explanation: 'BFS level by level', code_lines: [5, 6] },
    { step: 5, type: 'graph', visited: [0, 1, 2, 3, 4], queue: [], action: 'All nodes visited! Order: 0,1,2,3,4', explanation: 'BFS complete — shortest path guaranteed', code_lines: [8] }
  ];
}

function buildGenericArraySteps() {
  return [
    { step: 1, type: 'array', array: [3, 7, 1, 9, 4], highlight: [], action: 'Initial array state', explanation: 'Starting state of the algorithm' },
    { step: 2, type: 'array', array: [3, 7, 1, 9, 4], highlight: [0, 1], action: 'Examining first two elements', explanation: 'Algorithm begins processing' },
    { step: 3, type: 'array', array: [3, 7, 1, 9, 4], highlight: [2], action: 'Current target element found', explanation: 'Processing continues' }
  ];
}

// ── SVG Rendering Functions ───────────────────────────────────────────────────

function renderStepSvg(step, codeLines) {
  if (!step) return '<div style="padding:20px;text-align:center;color:#888;">No step data</div>';

  const type = step.type || 'array';

  switch (type) {
    case 'two_pointer':
    case 'binary_search':
      return renderArrayWithPointers(step);
    case 'sliding_window':
      return renderSlidingWindow(step);
    case 'sorting':
      return renderSortingBars(step);
    case 'stack':
      return renderStack(step);
    case 'queue':
      return renderQueue(step);
    case 'linked_list':
      return renderLinkedList(step);
    case 'tree':
      return renderTree(step);
    case 'heap':
      return renderHeap(step);
    case 'dp_table':
      return renderDPTable(step);
    case 'graph':
      return renderGraph(step);
    default:
      return renderPlainArray(step);
  }
}

function renderArrayWithPointers(step) {
  const arr = step.array || [];
  const left = step.left !== undefined ? step.left : -1;
  const right = step.right !== undefined ? step.right : -1;
  const lo = step.lo !== undefined ? step.lo : -1;
  const hi = step.hi !== undefined ? step.hi : -1;
  const mid = step.mid !== undefined ? step.mid : -1;
  const highlight = step.highlight || [];

  const cellW = 56, cellH = 48, startX = 30, startY = 60;
  const width = Math.max(400, arr.length * (cellW + 8) + startX * 2);

  let cells = '';
  let pointers = '';

  arr.forEach((val, i) => {
    const x = startX + i * (cellW + 8);
    const isHighlighted = highlight.includes(i);
    const isLeft = i === left;
    const isRight = i === right;
    const isLo = i === lo;
    const isHi = i === hi;
    const isMid = i === mid;

    let fill = '#1e2433';
    let stroke = '#3d4a6b';
    if (isHighlighted) { fill = '#1a3a5c'; stroke = '#4a90d9'; }
    if (isLeft || isLo) { fill = '#1a4a2a'; stroke = '#4adf84'; }
    if (isRight || isHi) { fill = '#4a1a1a'; stroke = '#df4a4a'; }
    if (isMid) { fill = '#4a3a1a'; stroke = '#dfaa4a'; }

    cells += `
      <rect x="${x}" y="${startY}" width="${cellW}" height="${cellH}" rx="6"
            fill="${fill}" stroke="${stroke}" stroke-width="2"/>
      <text x="${x + cellW/2}" y="${startY + cellH/2 + 6}" text-anchor="middle"
            fill="#e8ecff" font-family="monospace" font-size="18" font-weight="700">${val}</text>
      <text x="${x + cellW/2}" y="${startY + cellH + 16}" text-anchor="middle"
            fill="#6a7499" font-family="monospace" font-size="11">[${i}]</text>
    `;

    // Pointer arrows
    if (isLeft || isLo) {
      const label = isLeft ? 'L' : 'lo';
      pointers += `
        <line x1="${x + cellW/2}" y1="${startY - 8}" x2="${x + cellW/2}" y2="${startY - 2}"
              stroke="#4adf84" stroke-width="2" marker-end="url(#arrow-green)"/>
        <text x="${x + cellW/2}" y="${startY - 12}" text-anchor="middle"
              fill="#4adf84" font-family="monospace" font-size="12" font-weight="700">${label}</text>
      `;
    }
    if (isRight || isHi) {
      const label = isRight ? 'R' : 'hi';
      pointers += `
        <line x1="${x + cellW/2}" y1="${startY - 8}" x2="${x + cellW/2}" y2="${startY - 2}"
              stroke="#df4a4a" stroke-width="2" marker-end="url(#arrow-red)"/>
        <text x="${x + cellW/2}" y="${startY - 12}" text-anchor="middle"
              fill="#df4a4a" font-family="monospace" font-size="12" font-weight="700">${label}</text>
      `;
    }
    if (isMid) {
      pointers += `
        <line x1="${x + cellW/2}" y1="${startY - 8}" x2="${x + cellW/2}" y2="${startY - 2}"
              stroke="#dfaa4a" stroke-width="2" marker-end="url(#arrow-gold)"/>
        <text x="${x + cellW/2}" y="${startY - 12}" text-anchor="middle"
              fill="#dfaa4a" font-family="monospace" font-size="12" font-weight="700">mid</text>
      `;
    }
  });

  return `
    <svg viewBox="0 0 ${width} 130" style="width:100%;max-width:${width}px;height:auto;display:block;margin:0 auto">
      <defs>
        ${arrowDefs()}
      </defs>
      ${cells}
      ${pointers}
    </svg>
  `;
}

function renderSlidingWindow(step) {
  const arr = step.array || [];
  const wStart = step.window_start !== undefined ? step.window_start : 0;
  const wEnd = step.window_end !== undefined ? step.window_end : 0;

  const cellW = 48, cellH = 44, startX = 20, startY = 50;
  const width = Math.max(400, arr.length * (cellW + 6) + startX * 2);

  let cells = '';
  arr.forEach((val, i) => {
    const x = startX + i * (cellW + 6);
    const inWindow = i >= wStart && i <= wEnd;
    const fill = inWindow ? '#1a3a5c' : '#1e2433';
    const stroke = inWindow ? '#4a90d9' : '#3d4a6b';
    cells += `
      <rect x="${x}" y="${startY}" width="${cellW}" height="${cellH}" rx="5"
            fill="${fill}" stroke="${stroke}" stroke-width="${inWindow ? 2.5 : 1.5}"/>
      <text x="${x + cellW/2}" y="${startY + cellH/2 + 6}" text-anchor="middle"
            fill="${inWindow ? '#70b8ff' : '#9aaabb'}" font-family="monospace" font-size="16" font-weight="700">${val}</text>
    `;
  });

  // Window bracket
  const bx1 = startX + wStart * (cellW + 6) - 4;
  const bx2 = startX + wEnd * (cellW + 6) + cellW + 4;

  return `
    <svg viewBox="0 0 ${width} 110" style="width:100%;max-width:${width}px;height:auto;display:block;margin:0 auto">
      ${cells}
      <rect x="${bx1}" y="${startY - 5}" width="${bx2 - bx1}" height="${cellH + 10}"
            rx="8" fill="none" stroke="#4a90d9" stroke-width="2.5" stroke-dasharray="6,3" opacity="0.8"/>
      <text x="${(bx1 + bx2)/2}" y="${startY + cellH + 20}" text-anchor="middle"
            fill="#4a90d9" font-size="11" font-family="monospace">window[${wStart}..${wEnd}]</text>
    </svg>
  `;
}

function renderSortingBars(step) {
  const arr = step.array || [];
  const comparing = step.comparing || [];
  const swapped = step.swapped || [];
  const maxVal = Math.max(...arr, 1);
  const barW = 40, maxH = 80, startX = 20, baseY = 110;
  const width = arr.length * (barW + 8) + startX * 2;

  let bars = '';
  arr.forEach((val, i) => {
    const x = startX + i * (barW + 8);
    const h = Math.max(8, (val / maxVal) * maxH);
    const y = baseY - h;
    let fill = '#2a3a5a';
    if (comparing.includes(i)) fill = '#4a90d9';
    if (swapped.includes(i)) fill = '#df6a4a';

    bars += `
      <rect x="${x}" y="${y}" width="${barW}" height="${h}" rx="4" fill="${fill}"/>
      <text x="${x + barW/2}" y="${baseY + 16}" text-anchor="middle"
            fill="#9aaabb" font-size="12" font-family="monospace">${val}</text>
    `;
  });

  return `
    <svg viewBox="0 0 ${width} 130" style="width:100%;max-width:${width}px;height:auto;display:block;margin:0 auto">
      ${bars}
      <line x1="${startX - 5}" y1="${baseY}" x2="${width - 10}" y2="${baseY}" stroke="#3d4a6b" stroke-width="1.5"/>
    </svg>
  `;
}

function renderStack(step) {
  const stack = step.stack || [];
  const maxH = 30, w = 100, x = 80, baseY = 160;

  let rects = '';
  stack.forEach((val, i) => {
    const y = baseY - (i + 1) * (maxH + 4);
    rects += `
      <rect x="${x}" y="${y}" width="${w}" height="${maxH}" rx="5"
            fill="${i === stack.length - 1 ? '#1a3a5c' : '#1e2433'}"
            stroke="${i === stack.length - 1 ? '#4a90d9' : '#3d4a6b'}" stroke-width="1.5"/>
      <text x="${x + w/2}" y="${y + maxH/2 + 5}" text-anchor="middle"
            fill="#e8ecff" font-family="monospace" font-size="14" font-weight="600">${val}</text>
    `;
  });

  if (stack.length === 0) {
    rects = `<text x="130" y="90" text-anchor="middle" fill="#6a7499" font-size="13" font-family="monospace">(empty)</text>`;
  }

  return `
    <svg viewBox="0 0 260 180" style="width:100%;max-width:260px;height:auto;display:block;margin:0 auto">
      ${rects}
      <rect x="${x - 4}" y="20" width="${w + 8}" height="${baseY - 18}"
            rx="5" fill="none" stroke="#3d4a6b" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="${x + w/2}" y="14" text-anchor="middle" fill="#6a7499" font-size="10" font-family="monospace">TOP</text>
    </svg>
  `;
}

function renderQueue(step) {
  const queue = step.queue || [];
  const cellW = 50, cellH = 36, startX = 20, y = 50;
  const width = Math.max(300, queue.length * (cellW + 6) + startX * 2 + 60);

  let cells = '';
  queue.forEach((val, i) => {
    const x = startX + 40 + i * (cellW + 6);
    cells += `
      <rect x="${x}" y="${y}" width="${cellW}" height="${cellH}" rx="4"
            fill="${i === 0 ? '#1a4a2a' : '#1e2433'}"
            stroke="${i === 0 ? '#4adf84' : '#3d4a6b'}" stroke-width="1.5"/>
      <text x="${x + cellW/2}" y="${y + cellH/2 + 5}" text-anchor="middle"
            fill="#e8ecff" font-family="monospace" font-size="14" font-weight="600">${val}</text>
    `;
  });

  if (queue.length === 0) {
    cells = `<text x="${width/2}" y="75" text-anchor="middle" fill="#6a7499" font-size="13" font-family="monospace">(empty)</text>`;
  }

  return `
    <svg viewBox="0 0 ${width} 110" style="width:100%;max-width:${width}px;height:auto;display:block;margin:0 auto">
      ${cells}
      <text x="20" y="72" fill="#4adf84" font-size="11" font-family="monospace">HEAD</text>
      <text x="${width - 10}" y="72" text-anchor="end" fill="#df4a4a" font-size="11" font-family="monospace">TAIL</text>
    </svg>
  `;
}

function renderLinkedList(step) {
  const nodes = step.nodes || [];
  const slow = step.slow !== undefined ? step.slow : -1;
  const fast = step.fast !== undefined ? step.fast : -1;
  const curr = step.curr !== undefined ? step.curr : -1;
  const prev = step.prev !== undefined ? step.prev : -1;

  const nodeW = 44, nodeH = 36, startX = 20, y = 50, gap = 24;
  const width = nodes.length * (nodeW + gap) + startX * 2 + 20;

  let cells = '';
  nodes.forEach((val, i) => {
    const x = startX + i * (nodeW + gap);
    const isSlowOrPrev = i === slow || i === prev;
    const isFastOrCurr = i === fast || i === curr;

    cells += `
      <rect x="${x}" y="${y}" width="${nodeW}" height="${nodeH}" rx="6"
            fill="${isSlowOrPrev ? '#1a4a2a' : isFastOrCurr ? '#4a1a1a' : '#1e2433'}"
            stroke="${isSlowOrPrev ? '#4adf84' : isFastOrCurr ? '#df4a4a' : '#3d4a6b'}" stroke-width="1.5"/>
      <text x="${x + nodeW/2}" y="${y + nodeH/2 + 5}" text-anchor="middle"
            fill="#e8ecff" font-family="monospace" font-size="15" font-weight="700">${val}</text>
    `;

    // Arrow to next
    if (i < nodes.length - 1) {
      const ax = x + nodeW + 2;
      cells += `
        <line x1="${ax}" y1="${y + nodeH/2}" x2="${ax + gap - 6}" y2="${y + nodeH/2}"
              stroke="#4a90d9" stroke-width="1.5" marker-end="url(#arrow-blue)"/>
      `;
    } else {
      cells += `<text x="${x + nodeW + 6}" y="${y + nodeH/2 + 5}" fill="#6a7499" font-size="11">null</text>`;
    }

    if (isSlowOrPrev) cells += `<text x="${x + nodeW/2}" y="${y - 8}" text-anchor="middle" fill="#4adf84" font-size="10" font-family="monospace">${slow !== -1 ? 'S' : 'P'}</text>`;
    if (isFastOrCurr) cells += `<text x="${x + nodeW/2}" y="${y - 8}" text-anchor="middle" fill="#df4a4a" font-size="10" font-family="monospace">${fast !== -1 ? 'F' : 'C'}</text>`;
  });

  return `
    <svg viewBox="0 0 ${width} 100" style="width:100%;max-width:${width}px;height:auto;display:block;margin:0 auto">
      <defs>${arrowDefs()}</defs>
      ${cells}
    </svg>
  `;
}

function renderTree(step) {
  const tree = step.tree || [];
  const highlight = step.highlight || [];

  // Draw a binary tree from array representation (0-indexed)
  const nodeR = 20;
  const levelH = 60;
  const svgW = 320, svgH = 200;

  function nodeX(i, level) {
    const levelWidth = svgW;
    const nodesInLevel = Math.pow(2, level);
    const posInLevel = i - (Math.pow(2, level) - 1);
    return (levelWidth / (nodesInLevel + 1)) * (posInLevel + 1);
  }
  function nodeY(level) { return 30 + level * levelH; }
  function level(i) { return Math.floor(Math.log2(i + 1)); }

  let nodes = '';
  for (let i = 0; i < tree.length; i++) {
    if (tree[i] === null) continue;
    const lv = level(i);
    const x = nodeX(i, lv);
    const y = nodeY(lv);
    const isHighlighted = highlight.includes(i);

    // Draw edge to parent
    if (i > 0) {
      const pi = Math.floor((i - 1) / 2);
      if (tree[pi] !== null) {
        const plv = level(pi);
        const px = nodeX(pi, plv);
        const py = nodeY(plv);
        nodes += `<line x1="${px}" y1="${py}" x2="${x}" y2="${y}" stroke="#3d4a6b" stroke-width="1.5"/>`;
      }
    }

    nodes += `
      <circle cx="${x}" cy="${y}" r="${nodeR}"
              fill="${isHighlighted ? '#1a3a5c' : '#1e2433'}"
              stroke="${isHighlighted ? '#4a90d9' : '#3d4a6b'}" stroke-width="2"/>
      <text x="${x}" y="${y + 5}" text-anchor="middle"
            fill="${isHighlighted ? '#70b8ff' : '#9aaabb'}" font-family="monospace"
            font-size="13" font-weight="700">${tree[i]}</text>
    `;
  }

  return `
    <svg viewBox="0 0 ${svgW} ${svgH}" style="width:100%;max-width:${svgW}px;height:auto;display:block;margin:0 auto">
      ${nodes}
    </svg>
  `;
}

function renderHeap(step) {
  const arr = step.array || [];
  const highlight = step.highlight || [];
  return renderPlainArray({ ...step, array: arr, highlight });
}

function renderDPTable(step) {
  const table = step.table || [];
  const hlCell = step.highlight_cell;
  const rows = table.length;
  const cols = rows > 0 ? table[0].length : 0;

  const cellW = 36, cellH = 28, startX = 20, startY = 20;
  const width = cols * (cellW + 2) + startX * 2;
  const height = rows * (cellH + 2) + startY * 2;

  let cells = '';
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const x = startX + c * (cellW + 2);
      const y = startY + r * (cellH + 2);
      const isHL = hlCell && hlCell[0] === r && hlCell[1] === c;
      cells += `
        <rect x="${x}" y="${y}" width="${cellW}" height="${cellH}" rx="3"
              fill="${isHL ? '#1a3a5c' : '#1e2433'}"
              stroke="${isHL ? '#4a90d9' : '#3d4a6b'}" stroke-width="${isHL ? 2 : 1}"/>
        <text x="${x + cellW/2}" y="${y + cellH/2 + 5}" text-anchor="middle"
              fill="${isHL ? '#70b8ff' : '#9aaabb'}" font-family="monospace" font-size="12">${table[r][c]}</text>
      `;
    }
  }

  return `
    <svg viewBox="0 0 ${width} ${height}" style="width:100%;max-width:${width}px;height:auto;display:block;margin:0 auto">
      ${cells}
    </svg>
  `;
}

function renderGraph(step) {
  const visited = step.visited || [];
  const queue = step.queue || [];
  // Simple 5-node graph visualization
  const nodes = [
    { id: 0, x: 80, y: 100 },
    { id: 1, x: 160, y: 50 },
    { id: 2, x: 160, y: 150 },
    { id: 3, x: 240, y: 50 },
    { id: 4, x: 240, y: 150 }
  ];
  const edges = [[0,1],[0,2],[1,3],[2,4],[1,2]];
  const r = 20;

  let edgeSvg = edges.map(([a, b]) => {
    const na = nodes[a], nb = nodes[b];
    return `<line x1="${na.x}" y1="${na.y}" x2="${nb.x}" y2="${nb.y}" stroke="#3d4a6b" stroke-width="1.5"/>`;
  }).join('');

  let nodeSvg = nodes.map(n => {
    const isVisited = visited.includes(n.id);
    const inQueue = queue.includes(n.id);
    return `
      <circle cx="${n.x}" cy="${n.y}" r="${r}"
              fill="${isVisited ? '#1a4a2a' : inQueue ? '#1a3a5c' : '#1e2433'}"
              stroke="${isVisited ? '#4adf84' : inQueue ? '#4a90d9' : '#3d4a6b'}" stroke-width="2"/>
      <text x="${n.x}" y="${n.y + 5}" text-anchor="middle"
            fill="#e8ecff" font-family="monospace" font-size="13" font-weight="700">${n.id}</text>
    `;
  }).join('');

  return `
    <svg viewBox="0 0 320 200" style="width:100%;max-width:320px;height:auto;display:block;margin:0 auto">
      ${edgeSvg}${nodeSvg}
    </svg>
  `;
}

function renderPlainArray(step) {
  const arr = step.array || [];
  const highlight = step.highlight || [];
  const cellW = 48, cellH = 44, startX = 20, startY = 30;
  const width = arr.length * (cellW + 8) + startX * 2;

  const cells = arr.map((val, i) => {
    const x = startX + i * (cellW + 8);
    const isHL = highlight.includes(i);
    return `
      <rect x="${x}" y="${startY}" width="${cellW}" height="${cellH}" rx="5"
            fill="${isHL ? '#1a3a5c' : '#1e2433'}"
            stroke="${isHL ? '#4a90d9' : '#3d4a6b'}" stroke-width="${isHL ? 2 : 1.5}"/>
      <text x="${x + cellW/2}" y="${startY + cellH/2 + 6}" text-anchor="middle"
            fill="${isHL ? '#70b8ff' : '#9aaabb'}" font-family="monospace" font-size="16" font-weight="700">${val}</text>
    `;
  }).join('');

  return `
    <svg viewBox="0 0 ${Math.max(300, width)} 100" style="width:100%;max-width:${Math.max(300, width)}px;height:auto;display:block;margin:0 auto">
      ${cells}
    </svg>
  `;
}

function arrowDefs() {
  return `
    <defs>
      <marker id="arrow-green" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#4adf84"/>
      </marker>
      <marker id="arrow-red" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#df4a4a"/>
      </marker>
      <marker id="arrow-gold" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#dfaa4a"/>
      </marker>
      <marker id="arrow-blue" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#4a90d9"/>
      </marker>
    </defs>
  `;
}

// ── Main Public API ───────────────────────────────────────────────────────────

/**
 * renderDsaVisualizer(dsaPattern, javaCode)
 *
 * Returns an HTML string containing a fully interactive DSA animated visualizer.
 * Attach event listeners via attachVisualizerInteractivity(container).
 *
 * @param {Object} dsaPattern - the dsa_pattern object from the day JSON
 * @param {string} javaCode   - the Java code string for code-line highlighting
 */
export function renderDsaVisualizer(dsaPattern, javaCode) {
  if (!dsaPattern || !dsaPattern.pattern_name) {
    return `<div class="callout callout-understand"><div class="callout-header">DSA Visualizer</div><p>No pattern data available for this day.</p></div>`;
  }

  const steps = buildDryRunSteps(dsaPattern);
  const totalSteps = steps.length;
  const vizId = `dsa-viz-${Date.now()}-${Math.random().toString(36).slice(2,7)}`;

  // Serialize steps to JSON for inline storage
  const stepsJson = JSON.stringify(steps).replace(/</g, '\\u003c').replace(/>/g, '\\u003e');

  // Code lines for display
  const codeLines = (javaCode || '').split('\n');
  const codeHtml = codeLines.map((line, i) =>
    `<div class="code-line" data-line="${i + 1}" id="${vizId}-line-${i + 1}">${escapeHtml(line)}</div>`
  ).join('');

  return `
<div class="dsa-visualizer" id="${vizId}" data-steps='${stepsJson}' data-current="0">
  <!-- Header -->
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:12px">
    <div>
      <span class="badge badge-success" style="font-size:0.7rem;">ANIMATED VISUALIZER</span>
      <strong style="margin-left:8px;font-size:0.95rem;">${escapeHtml(dsaPattern.pattern_name)}</strong>
    </div>
    <span class="dsa-viz-step-counter" style="font-size:0.75rem;color:var(--text-muted);font-family:var(--font-family-mono)">
      Step <span class="cur-step">1</span> / <span class="tot-step">${totalSteps}</span>
    </span>
  </div>

  <!-- Visualization Canvas -->
  <div class="dsa-viz-canvas" style="
    background:var(--bg-surface-2);
    border:1px solid var(--border-color);
    border-radius:var(--radius-md);
    padding:16px 12px 8px;
    min-height:130px;
    margin-bottom:10px;
    overflow-x:auto;
  ">
    <div class="dsa-viz-svg-area" style="text-align:center;">
      ${renderStepSvg(steps[0], javaCode)}
    </div>
  </div>

  <!-- Action Label + Explanation -->
  <div class="dsa-viz-action" style="
    background:var(--bg-surface);
    border-left:3px solid var(--color-primary);
    padding:10px 14px;
    border-radius:0 var(--radius-sm) var(--radius-sm) 0;
    margin-bottom:8px;
    font-size:0.82rem;
  ">
    <div style="font-weight:700;color:var(--color-primary);margin-bottom:2px;" class="viz-action-text">
      ${escapeHtml(steps[0].action || '')}
    </div>
    <div style="color:var(--text-secondary);" class="viz-explanation-text">
      ${escapeHtml(steps[0].explanation || '')}
    </div>
  </div>

  <!-- Controls Row -->
  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:10px;">
    <button class="btn btn-secondary btn-sm viz-prev-btn" disabled title="Previous Step">
      ◀ Prev
    </button>
    <button class="btn btn-primary btn-sm viz-play-btn" title="Play / Pause Animation">
      ▶ Play
    </button>
    <button class="btn btn-secondary btn-sm viz-next-btn" title="Next Step">
      Next ▶
    </button>
    <button class="btn btn-secondary btn-sm viz-reset-btn" title="Reset to Start">
      ↺ Reset
    </button>
    <div style="display:flex;align-items:center;gap:4px;margin-left:auto;">
      <span style="font-size:0.7rem;color:var(--text-muted);font-family:monospace;">Speed:</span>
      ${['0.5x','1x','1.5x','2x'].map(s =>
        `<button class="btn btn-secondary btn-sm viz-speed-btn${s === '1x' ? ' active' : ''}" data-speed="${s}" style="padding:3px 8px;font-size:0.7rem;">${s}</button>`
      ).join('')}
    </div>
  </div>

  <!-- Step Progress Bar -->
  <div style="height:4px;background:var(--bg-surface-2);border-radius:2px;overflow:hidden;margin-bottom:10px;">
    <div class="viz-progress-bar" style="height:100%;background:var(--color-primary);border-radius:2px;transition:width 0.3s ease;width:${Math.round(100/totalSteps)}%;"></div>
  </div>

  ${javaCode ? `
  <!-- Synchronized Code View -->
  <details style="margin-top:8px;">
    <summary style="font-size:0.75rem;color:var(--text-muted);cursor:pointer;user-select:none;padding:4px 0;">
      🔗 Synchronized Code View (click to expand)
    </summary>
    <div class="code-container" style="margin-top:8px;font-size:0.72rem;">
      <div class="code-header">
        <span>Java 17+ — Active line highlighted in sync with visualizer</span>
      </div>
      <pre class="code-pre" style="font-size:0.72rem;line-height:1.5;"><code class="dsa-viz-code-lines">${codeHtml}</code></pre>
    </div>
  </details>
  ` : ''}
</div>
  `;
}

function escapeHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/**
 * attachVisualizerInteractivity(container)
 *
 * Must be called once after renderDsaVisualizer HTML is inserted into the DOM.
 * Sets up all event listeners for play/pause/step/speed/reset.
 *
 * @param {HTMLElement} container - element containing one or more .dsa-visualizer elements
 */
export function attachVisualizerInteractivity(container) {
  const visualizers = container.querySelectorAll('.dsa-visualizer');

  visualizers.forEach(viz => {
    let steps;
    try {
      steps = JSON.parse(viz.dataset.steps);
    } catch (e) {
      console.warn('Visualizer: failed to parse steps JSON', e);
      return;
    }

    let currentStep = 0;
    let isPlaying = false;
    let playInterval = null;
    let speedMs = 1200; // 1x default

    const totalSteps = steps.length;
    const canvas = viz.querySelector('.dsa-viz-svg-area');
    const actionText = viz.querySelector('.viz-action-text');
    const explanationText = viz.querySelector('.viz-explanation-text');
    const curStepEl = viz.querySelector('.cur-step');
    const playBtn = viz.querySelector('.viz-play-btn');
    const prevBtn = viz.querySelector('.viz-prev-btn');
    const nextBtn = viz.querySelector('.viz-next-btn');
    const resetBtn = viz.querySelector('.viz-reset-btn');
    const progressBar = viz.querySelector('.viz-progress-bar');
    const speedBtns = viz.querySelectorAll('.viz-speed-btn');

    function updateDisplay(stepIdx) {
      const step = steps[stepIdx];
      if (!step) return;

      // Update SVG
      canvas.innerHTML = renderStepSvg(step);

      // Update text
      if (actionText) actionText.textContent = step.action || '';
      if (explanationText) explanationText.textContent = step.explanation || '';
      if (curStepEl) curStepEl.textContent = stepIdx + 1;

      // Update progress bar
      const pct = Math.round(((stepIdx + 1) / totalSteps) * 100);
      if (progressBar) progressBar.style.width = pct + '%';

      // Update button states
      if (prevBtn) prevBtn.disabled = stepIdx === 0;
      if (nextBtn) nextBtn.disabled = stepIdx === totalSteps - 1;

      // Code line highlighting
      const codeContainer = viz.querySelector('.dsa-viz-code-lines');
      if (codeContainer && step.code_lines) {
        codeContainer.querySelectorAll('.code-line').forEach(el => {
          el.style.background = '';
          el.style.color = '';
        });
        step.code_lines.forEach(lineNum => {
          const lineEl = viz.querySelector(`[data-line="${lineNum}"]`);
          if (lineEl) {
            lineEl.style.background = 'rgba(74, 144, 217, 0.2)';
            lineEl.style.color = '#70b8ff';
            lineEl.scrollIntoView && lineEl.scrollIntoView({ block: 'nearest' });
          }
        });
      }

      currentStep = stepIdx;
    }

    function goNext() {
      if (currentStep < totalSteps - 1) {
        updateDisplay(currentStep + 1);
      } else {
        pausePlay();
      }
    }

    function goPrev() {
      if (currentStep > 0) updateDisplay(currentStep - 1);
    }

    function startPlay() {
      if (currentStep >= totalSteps - 1) {
        updateDisplay(0);
      }
      isPlaying = true;
      playBtn.textContent = '⏸ Pause';
      playBtn.classList.add('btn-warning');
      playBtn.classList.remove('btn-primary');
      playInterval = setInterval(() => {
        if (currentStep >= totalSteps - 1) {
          pausePlay();
        } else {
          goNext();
        }
      }, speedMs);
    }

    function pausePlay() {
      isPlaying = false;
      clearInterval(playInterval);
      playInterval = null;
      playBtn.textContent = '▶ Play';
      playBtn.classList.remove('btn-warning');
      playBtn.classList.add('btn-primary');
    }

    // Event listeners
    if (playBtn) {
      playBtn.addEventListener('click', () => {
        if (isPlaying) pausePlay();
        else startPlay();
      });
    }

    if (nextBtn) nextBtn.addEventListener('click', () => { pausePlay(); goNext(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { pausePlay(); goPrev(); });

    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        pausePlay();
        updateDisplay(0);
      });
    }

    speedBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        speedBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const speedStr = btn.dataset.speed;
        const mult = parseFloat(speedStr);
        speedMs = Math.round(1200 / mult);
        if (isPlaying) {
          pausePlay();
          startPlay();
        }
      });
    });

    // Init display
    updateDisplay(0);
  });
}
