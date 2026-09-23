#!/usr/bin/env python3
"""
scripts/build_all_java_curricula.py
Builds:
1. scripts/curriculum/dsa_curriculum.py (30 Java 17+ DSA Patterns & 60 Solved Java Placement Problems)
2. scripts/curriculum/coding_tasks_curriculum.py (30 Java 17+ Practical Timed Coding Tasks)
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM_DIR = os.path.join(BASE_DIR, "scripts", "curriculum")

# 30 Comprehensive DSA Patterns in Java 17+
ALL_PATTERNS = [
    # 1
    {
        "pattern_name": "Two Pointers (Opposite Direction)",
        "category": "Two Pointers",
        "concept": "Pointers start at opposite ends of a sorted array (left = 0, right = n - 1) and converge toward each other based on comparison against a target.",
        "why_it_works": "Exploits the monotonic ordering of sorted elements to eliminate half of unexamined candidates at each step in O(1) time without nested loops.",
        "visual_explanation": "Sorted Array: [ 2, 7, 11, 15 ], Target = 9\\nStep 1: Left -> [2]               [15] <- Right   Sum = 17 > 9  ==> Right--\\nStep 2: Left -> [2]         [11] <- Right         Sum = 13 > 9  ==> Right--\\nStep 3: Left -> [2]   [7] <- Right               Sum = 9  == 9 ==> Found indices [0, 1]!",
        "java_code": """import java.util.*;

public class Solution {
    public int[] twoSumSorted(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return new int[]{left, right};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{};
    }
}""",
        "line_by_line_walkthrough": [
            "Line 4-5: Initialize left pointer at index 0 and right pointer at numbers.length - 1.",
            "Line 6: Loop while left < right so pointers do not cross or select the same element.",
            "Line 7: Compute current sum = numbers[left] + numbers[right].",
            "Line 8-9: If sum matches target, return indices immediately.",
            "Line 10-11: If sum < target, increment left pointer to increase total sum.",
            "Line 12-13: If sum > target, decrement right pointer to decrease total sum.",
            "Line 16: Return empty array if no pair satisfies the condition."
        ],
        "dry_run": "numbers = [2, 7, 11, 15], target = 9. Iter 1: left=0(2), right=3(15) -> sum=17 > 9 -> right=2. Iter 2: left=0(2), right=2(11) -> sum=13 > 9 -> right=1. Iter 3: left=0(2), right=1(7) -> sum=9 == target -> return [0, 1].",
        "complexity": "O(N) Time, O(1) Auxiliary Space",
        "edge_cases": ["Array of length 2", "Negative numbers in sorted order", "Duplicates summing to target", "No valid pair"],
        "interview_variations": ["Container With Most Water", "3Sum (fix 1 element, 2-pointer scan remainder)", "Trapping Rain Water", "Valid Palindrome II"],
        "p1_title": "Two Sum II — Input Array Is Sorted",
        "p1_stmt": "Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the 1-based indices [index1, index2].",
        "p1_code": """public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) return new int[]{left + 1, right + 1};
            if (sum < target) left++;
            else right--;
        }
        return new int[]{-1, -1};
    }
}""",
        "p2_title": "Container With Most Water",
        "p2_stmt": "You are given an integer array height of length n. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.",
        "p2_code": """public class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxWater = 0;
        while (left < right) {
            int width = right - left;
            int h = Math.min(height[left], height[right]);
            maxWater = Math.max(maxWater, width * h);
            if (height[left] < height[right]) left++;
            else right--;
        }
        return maxWater;
    }
}"""
    },
    # 2
    {
        "pattern_name": "Sliding Window (Fixed Size)",
        "category": "Sliding Window",
        "concept": "Maintains a contiguous subarray window of fixed length K. Slides the window one step at a time by adding the incoming element at the right and evicting the outgoing element at the left.",
        "why_it_works": "Reuses the computational state of overlapping elements across adjacent windows in O(1) time instead of recomputing from scratch in O(K).",
        "visual_explanation": "Array: [ 2, 1, 5, 1, 3, 2 ], K = 3\\nWindow 0: [ (2, 1, 5), 1, 3, 2 ]  Sum = 8\\nWindow 1: [ 2, (1, 5, 1), 3, 2 ]  Sum = 8 - 2 + 1 = 7\\nWindow 2: [ 2, 1, (5, 1, 3), 2 ]  Sum = 7 - 1 + 3 = 9 (Max)\\nWindow 3: [ 2, 1, 5, (1, 3, 2) ]  Sum = 9 - 5 + 2 = 6",
        "java_code": """import java.util.*;

public class Solution {
    public int maxSumSubarray(int[] nums, int k) {
        if (nums == null || nums.length < k) return 0;
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }
        int maxSum = windowSum;
        for (int i = k; i < nums.length; i++) {
            windowSum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, windowSum);
        }
        return maxSum;
    }
}""",
        "line_by_line_walkthrough": [
            "Line 4: Guard check for null or array smaller than window size k.",
            "Line 5-8: Compute baseline sum for the initial window of first k elements.",
            "Line 9: Initialize maxSum with the sum of the first window.",
            "Line 10-13: Iterate from k to end of array, adding nums[i] and subtracting nums[i - k].",
            "Line 14: Return the maximum window sum found."
        ],
        "dry_run": "nums = [2, 1, 5, 1, 3, 2], k = 3. Init: sum([2,1,5])=8. i=3: window=8+1-2=7 (max=8). i=4: window=7+3-1=9 (max=9). i=5: window=9+2-5=6 (max=9). Return 9.",
        "complexity": "O(N) Time, O(1) Auxiliary Space",
        "edge_cases": ["k == nums.length", "Negative numbers in array", "k == 1", "All elements equal"],
        "interview_variations": ["Maximum Average Subarray I", "Find All Anagrams in a String", "Substrings of Size Three with Distinct Characters", "Permutation in String"],
        "p1_title": "Maximum Average Subarray I",
        "p1_stmt": "You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.",
        "p1_code": """public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        double maxSum = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum / k;
    }
}""",
        "p2_title": "Find All Anagrams in a String",
        "p2_stmt": "Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.",
        "p2_code": """import java.util.*;

public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if (s.length() < p.length()) return res;
        int[] pCount = new int[26];
        int[] sCount = new int[26];
        for (int i = 0; i < p.length(); i++) {
            pCount[p.charAt(i) - 'a']++;
            sCount[s.charAt(i) - 'a']++;
        }
        if (Arrays.equals(pCount, sCount)) res.add(0);
        for (int i = p.length(); i < s.length(); i++) {
            sCount[s.charAt(i) - 'a']++;
            sCount[s.charAt(i - p.length()) - 'a']--;
            if (Arrays.equals(pCount, sCount)) res.add(i - p.length() + 1);
        }
        return res;
    }
}"""
    },
    # 3
    {
        "pattern_name": "Sliding Window (Dynamic / Variable Size)",
        "category": "Sliding Window",
        "concept": "Expands window by moving right pointer until a condition is met; then contracts window from left to find the minimal or maximal valid subarray.",
        "why_it_works": "Both pointers move monotonically forward from 0 to N - 1. Each element enters and leaves the window at most once, guaranteeing strict O(N) runtime.",
        "visual_explanation": "Target = 7, Array: [ 2, 3, 1, 2, 4, 3 ]\\nRight expands: [2, 3, 1, 2] -> Sum = 8 >= 7 (Len 4)\\nLeft contracts: [3, 1, 2] -> Sum = 6 < 7\\nRight expands: [3, 1, 2, 4] -> Sum = 7 >= 7 (Len 3)\\nRight expands: [2, 4, 3] -> Sum = 9 >= 7 -> Left contracts to [4, 3] (Len 2 -- Min!)",
        "java_code": """import java.util.*;

public class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int currentSum = 0;
        int minLen = Integer.MAX_VALUE;
        
        for (int right = 0; right < nums.length; right++) {
            currentSum += nums[right];
            while (currentSum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                currentSum -= nums[left];
                left++;
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}""",
        "line_by_line_walkthrough": [
            "Line 4-6: Initialize left pointer, cumulative sum, and minLen to infinity.",
            "Line 8: Iterate right pointer across the entire array, absorbing nums[right].",
            "Line 10-14: While condition is satisfied (currentSum >= target), capture window length and contract left pointer.",
            "Line 16: Return 0 if no valid subarray found, otherwise return minLen."
        ],
        "dry_run": "target = 7, nums = [2, 3, 1, 2, 4, 3]. Right reaches 3 (sum=8>=7) -> minLen=4, shrink left. Right reaches 4 (sum=10) -> shrink left -> window [1, 2, 4] len 3. Right reaches 5 (sum=9) -> shrink left -> window [4, 3] len 2. Returns 2.",
        "complexity": "O(N) Time, O(1) Auxiliary Space",
        "edge_cases": ["Sum of all elements < target", "Single element == target", "All elements equal"],
        "interview_variations": ["Longest Substring Without Repeating Characters", "Minimum Window Substring", "Longest Repeating Character Replacement", "Max Consecutive Ones III"],
        "p1_title": "Minimum Size Subarray Sum",
        "p1_stmt": "Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0.",
        "p1_code": """public class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, sum = 0, minLen = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left++];
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}""",
        "p2_title": "Longest Substring Without Repeating Characters",
        "p2_stmt": "Given a string s, find the length of the longest substring without repeating characters.",
        "p2_code": """import java.util.*;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] lastIndex = new int[128];
        Arrays.fill(lastIndex, -1);
        int maxLen = 0, left = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastIndex[c] >= left) {
                left = lastIndex[c] + 1;
            }
            lastIndex[c] = right;
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}"""
    },
    # 4
    {
        "pattern_name": "Fast & Slow Pointers (Floyd's Tortoise and Hare)",
        "category": "Two Pointers",
        "concept": "Uses two pointers moving at different speeds (slow by 1 node, fast by 2 nodes). If a cycle exists in the sequence, the fast pointer will catch and collide with the slow pointer.",
        "why_it_works": "In a cycle of length C, the relative distance between slow and fast decreases by exactly 1 in each step. Hence, fast must overtake slow within C iterations without using extra memory.",
        "visual_explanation": "List: 1 -> 2 -> 3 -> 4 -> 5 -> [points back to 3]\\nStep 0: Slow = 1, Fast = 1\\nStep 1: Slow = 2, Fast = 3\\nStep 2: Slow = 3, Fast = 5\\nStep 3: Slow = 4, Fast = 4 (Collision at node 4 ==> Cycle Proven!)",
        "java_code": """class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; next = null; }
}

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}""",
        "line_by_line_walkthrough": [
            "Line 7: Guard check for empty list or single node without cycle.",
            "Line 8-9: Initialize slow and fast pointers at the head of the list.",
            "Line 10: Loop while fast and fast.next are non-null.",
            "Line 11-12: Advance slow pointer by 1 step and fast pointer by 2 steps.",
            "Line 13-15: If slow equals fast, pointers have collided in a cycle; return true.",
            "Line 17: If fast reaches null, list terminates without a cycle; return false."
        ],
        "dry_run": "List: 3 -> 2 -> 0 -> -4 -> 2. Step 1: slow=2, fast=0. Step 2: slow=0, fast=2. Step 3: slow=-4, fast=-4 (COLLISION -> true).",
        "complexity": "O(N) Time, O(1) Auxiliary Space",
        "edge_cases": ["Empty list (null head)", "Single node pointing to null", "Single node self-loop", "Two-node cycle"],
        "interview_variations": ["Middle of the Linked List", "Linked List Cycle II (Find Entry Point)", "Happy Number", "Find the Duplicate Number (Array as Linked List)"],
        "p1_title": "Middle of the Linked List",
        "p1_stmt": "Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.",
        "p1_code": """public class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}""",
        "p2_title": "Linked List Cycle II",
        "p2_stmt": "Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.",
        "p2_code": """public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;
        ListNode slow = head, fast = head;
        boolean hasCycle = false;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }
        if (!hasCycle) return null;
        ListNode ptr = head;
        while (ptr != slow) {
            ptr = ptr.next;
            slow = slow.next;
        }
        return ptr;
    }
}"""
    },
    # 5
    {
        "pattern_name": "Monotonic Stack (Next Greater Element)",
        "category": "Stack",
        "concept": "Maintains elements in a stack in strictly decreasing (or increasing) order. When a new element violates the monotonicity, elements are popped and resolved.",
        "why_it_works": "Every element is pushed onto the stack exactly once and popped at most once, yielding strictly linear O(N) aggregate runtime.",
        "visual_explanation": "Temperatures: [ 73, 74, 75, 71, 69, 72 ]\\ni=0 (73): Push 0\\ni=1 (74): 74 > 73 -> Pop 0, ans[0] = 1 - 0 = 1; Push 1\\ni=2 (75): 75 > 74 -> Pop 1, ans[1] = 2 - 1 = 1; Push 2\\ni=3 (71): 71 < 75 -> Push 3\\ni=4 (69): 69 < 71 -> Push 4\\ni=5 (72): 72 > 69 -> Pop 4, ans[4] = 5-4 = 1; 72 > 71 -> Pop 3, ans[3] = 5-3 = 2; Push 5",
        "java_code": """import java.util.*;

public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] ans = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int prevIndex = stack.pop();
                ans[prevIndex] = i - prevIndex;
            }
            stack.push(i);
        }
        return ans;
    }
}""",
        "line_by_line_walkthrough": [
            "Line 5: Allocate answer array initialized to 0.",
            "Line 6: Use ArrayDeque as an efficient, memory-optimized stack.",
            "Line 8: Iterate index i through all temperatures.",
            "Line 9-12: While stack is non-empty and current temperature exceeds the temperature at stack top, pop index and compute difference.",
            "Line 13: Push current index onto the stack.",
            "Line 15: Return populated answer array."
        ],
        "dry_run": "T = [73, 74, 75, 71, 69, 72]. i=0: push 0. i=1(74): pop 0 -> ans[0]=1, push 1. i=2(75): pop 1 -> ans[1]=1, push 2. i=3: push 3. i=4: push 4. i=5(72): pop 4 -> ans[4]=1, pop 3 -> ans[3]=2. Returns [1, 1, 0, 2, 1, 0].",
        "complexity": "O(N) Time, O(N) Auxiliary Space",
        "edge_cases": ["Strictly decreasing sequence (all answers 0)", "Strictly increasing sequence", "All equal elements", "Single element"],
        "interview_variations": ["Next Greater Element I & II", "Online Stock Span", "Largest Rectangle in Histogram", "Trapping Rain Water (Stack Approach)"],
        "p1_title": "Daily Temperatures",
        "p1_stmt": "Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0.",
        "p1_code": """import java.util.*;

public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] ans = new int[temperatures.length];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int idx = stack.pop();
                ans[idx] = i - idx;
            }
            stack.push(i);
        }
        return ans;
    }
}""",
        "p2_title": "Next Greater Element I",
        "p2_stmt": "The next greater element of some element x in an array is the first greater element that is to the right of x in the same array. Find all next greater elements for nums1 within nums2.",
        "p2_code": """import java.util.*;

public class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int num : nums2) {
            while (!stack.isEmpty() && num > stack.peek()) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }
        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            res[i] = map.getOrDefault(nums1[i], -1);
        }
        return res;
    }
}"""
    }
]

# Generate Remaining Patterns (6 to 30)
METAS = [
    # 6
    ("Binary Search on Sorted Arrays", "Binary Search",
     "Divides search interval in half each iteration by comparing target with midpoint.",
     "Eliminates 50% of candidate search space each step: T(n) = T(n/2) + O(1) => O(log N).",
     "nums = [-1, 0, 3, 5, 9, 12], target = 9\\nL=0, R=5, Mid=2 (val=3 < 9) -> Left = 3\\nL=3, R=5, Mid=4 (val=9 == 9) -> Found at index 4!",
     """public class Solution {
    public int binarySearch(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}""",
     ["Line 2: Initialize left=0, right=nums.length-1.", "Line 3: Loop while left <= right.", "Line 4: Calculate mid using left + (right - left)/2 to prevent integer overflow.", "Line 5-7: Narrow search window based on midpoint comparison."],
     "nums = [-1, 0, 3, 5, 9, 12], target = 9 -> L=0, R=5, M=2(3<9) -> L=3 -> M=4(9==9) -> return 4.",
     "O(log N) Time, O(1) Auxiliary Space", ["Target smaller than nums[0]", "Target greater than nums[n-1]", "Empty array"],
     ["Search Insert Position", "Find First and Last Position of Element in Sorted Array", "Find Peak Element"],
     "Search Insert Position", "Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.",
     """public class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return left;
    }
}""",
     "Find First and Last Position of Element in Sorted Array", "Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.",
     """public class Solution {
    public int[] searchRange(int[] nums, int target) {
        return new int[]{findBound(nums, target, true), findBound(nums, target, false)};
    }
    private int findBound(int[] nums, int target, boolean isFirst) {
        int left = 0, right = nums.length - 1, ans = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                ans = mid;
                if (isFirst) right = mid - 1;
                else left = mid + 1;
            } else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return ans;
    }
}"""),

    # 7
    ("Binary Search on Rotated Sorted Arrays", "Binary Search",
     "At least one half of a rotated sorted array is always strictly sorted. We identify the sorted half and check if the target falls within its range.",
     "Preserves the O(log N) divide-and-conquer property by discarding one half at each decision point.",
     "nums = [ 4, 5, 6, 7, 0, 1, 2 ], target = 0\\nL=0(4), R=6(2), Mid=3(7). Left half [4..7] is sorted!\\nTarget 0 is not in [4..7] -> search right half [0..2] -> Found at index 4.",
     """public class Solution {
    public int searchRotated(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) right = mid - 1;
                else left = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[right]) left = mid + 1;
                else right = mid - 1;
            }
        }
        return -1;
    }
}""",
     ["Line 4: Calculate mid index.", "Line 6: Check if left half is sorted (nums[left] <= nums[mid]).", "Line 7-8: If target is in sorted left half, search left; else search right.", "Line 10-11: Otherwise right half is sorted; check if target falls in right half."],
     "nums = [4, 5, 6, 7, 0, 1, 2], target = 0 -> Mid=3(7), left sorted. Target not in [4..7] -> L=4. Next Mid=5(1), right sorted. Target in [0..1] -> R=4 -> Mid=4(0==0) -> returns 4.",
     "O(log N) Time, O(1) Auxiliary Space", ["Rotation at index 0 (unrotated)", "Pivot at end", "Two element array"],
     ["Find Minimum in Rotated Sorted Array", "Search in Rotated Sorted Array II (with duplicates)"],
     "Find Minimum in Rotated Sorted Array", "Given the sorted rotated array nums of unique elements, return the minimum element of this array.",
     """public class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) left = mid + 1;
            else right = mid;
        }
        return nums[left];
    }
}""",
     "Search in Rotated Sorted Array", "Given array nums after possible rotation and integer target, return index of target or -1.",
     """public class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) return m;
            if (nums[l] <= nums[m]) {
                if (nums[l] <= target && target < nums[m]) r = m - 1;
                else l = m + 1;
            } else {
                if (nums[m] < target && target <= nums[r]) l = m + 1;
                else r = m - 1;
            }
        }
        return -1;
    }
}"""),

    # 8
    ("Linked List In-Place Reversal", "Linked List",
     "Reverses pointers of a linked list in-place using three pointers: prev, curr, and next.",
     "Mutates next pointers directly in a single linear pass with O(1) auxiliary space.",
     "1 -> 2 -> 3 -> null\\nStep 1: null <- 1    2 -> 3 -> null\\nStep 2: null <- 1 <- 2    3 -> null\\nStep 3: null <- 1 <- 2 <- 3 (New Head = 3)",
     """public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
}""",
     ["Line 3-4: Initialize prev as null and curr as head.", "Line 5: Loop while curr is non-null.", "Line 6: Temporarily store curr.next.", "Line 7: Invert pointer: curr.next = prev.", "Line 8-9: Advance prev to curr, and curr to nextTemp.", "Line 11: Return prev as the new head."],
     "1->2->3. Step 1: 1->null, prev=1, curr=2. Step 2: 2->1->null, prev=2, curr=3. Step 3: 3->2->1->null, prev=3, curr=null. Return 3.",
     "O(N) Time, O(1) Auxiliary Space", ["Empty list (head == null)", "Single node list", "Two node list"],
     ["Reverse Linked List II (Between Left and Right)", "Reverse Nodes in k-Group", "Palindrome Linked List"],
     "Reverse Linked List II", "Given head of a singly linked list and two integers left and right where left <= right, reverse the nodes from position left to right.",
     """public class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        for (int i = 1; i < left; i++) prev = prev.next;
        ListNode curr = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode temp = curr.next;
            curr.next = temp.next;
            temp.next = prev.next;
            prev.next = temp;
        }
        return dummy.next;
    }
}""",
     "Palindrome Linked List", "Given the head of a singly linked list, return true if it is a palindrome or false otherwise.",
     """public class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        while (slow != null) {
            ListNode nextNode = slow.next;
            slow.next = prev;
            prev = slow;
            slow = nextNode;
        }
        ListNode p1 = head, p2 = prev;
        while (p2 != null) {
            if (p1.val != p2.val) return false;
            p1 = p1.next;
            p2 = p2.next;
        }
        return true;
    }
}"""),

    # 9
    ("Fast & Slow Pointers (Cycle & Midpoint)", "Two Pointers",
     "Combines fast and slow pointer cycle detection with mathematical re-indexing to locate the cycle entrance node.",
     "If list head is distance L from cycle entry, and collision occurs at distance k from entry: L = (m * C) - k. Resetting one pointer to head aligns both at cycle entry.",
     "Head ---- L ----> [Cycle Entry] ---- k ----> [Collision]\\nAdvance Head pointer and Collision pointer at 1x speed -> Meet exactly at Cycle Entry!",
     """public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                ListNode ptr = head;
                while (ptr != slow) {
                    ptr = ptr.next;
                    slow = slow.next;
                }
                return ptr;
            }
        }
        return null;
    }
}""",
     ["Line 4: Guard check for empty or single element list.", "Line 5-8: Fast moves 2 steps, slow moves 1 step.", "Line 9: On collision, initialize ptr at head.", "Line 11-14: Advance ptr and slow by 1 step until they meet at cycle entry."],
     "Cycle entry at node 2. Collision occurs at node 4. Advancing head and node 4 simultaneously converges at node 2.",
     "O(N) Time, O(1) Auxiliary Space", ["No cycle present", "Cycle spans entire list", "Single node self cycle"],
     ["Find the Duplicate Number", "Happy Number", "Circular Array Loop"],
     "Find the Duplicate Number", "Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive, find the duplicate number.",
     """public class Solution {
    public int findDuplicate(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}""",
     "Reorder List", "You are given the head of a singly linked-list. Reorder the list to be: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2...",
     """public class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null, curr = slow.next;
        slow.next = null;
        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        ListNode p1 = head, p2 = prev;
        while (p2 != null) {
            ListNode t1 = p1.next, t2 = p2.next;
            p1.next = p2;
            p2.next = t1;
            p1 = t1;
            p2 = t2;
        }
    }
}"""),

    # 10
    ("Monotonic Deque (Sliding Window Maximum)", "Queue / Deque",
     "Maintains a double-ended queue storing array indices such that corresponding values are monotonically decreasing.",
     "Smaller elements that appear before newer larger elements can never be the maximum of any subsequent window and are evicted immediately in O(1) amortized.",
     "Window [ 1, 3, -1 ], k = 3 -> Deque stores [3, -1]\\nNext element is -3 -> Deque stores [3, -1, -3]\\nNext element is 5 -> 5 evicts 3, -1, -3 -> Deque stores [5]",
     """import java.util.*;

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0) return new int[0];
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> deque = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            if (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
                deque.pollFirst();
            }
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);
            if (i >= k - 1) {
                result[i - k + 1] = nums[deque.peekFirst()];
            }
        }
        return result;
    }
}""",
     ["Line 7: Use ArrayDeque to support O(1) head and tail operations.", "Line 10-12: Evict indices that fall outside the current sliding window.", "Line 13-15: Maintain decreasing monotonic order by popping smaller elements from tail.", "Line 16: Push current index i.", "Line 17-19: Once window size reaches k, record head of deque as maximum."],
     "nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3. Window [1, 3, -1] max=3. Window [3, -1, -3] max=3. Window [-1, -3, 5] max=5... Returns [3, 3, 5, 5, 6, 7].",
     "O(N) Time, O(K) Auxiliary Space", ["k == 1", "k == nums.length", "Strictly decreasing array", "All elements equal"],
     ["Sliding Window Minimum", "Constrained Subsequence Sum", "Jump Game VI"],
     "Sliding Window Maximum", "You are given an array of integers nums, there is a sliding window of size k which is moving from the very left to the very right. Return the max sliding window.",
     """import java.util.*;

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) res[i - k + 1] = nums[dq.peekFirst()];
        }
        return res;
    }
}""",
     "Jump Game VI", "You are given a 0-indexed integer array nums and an integer k. Return the maximum score you can get jumping at most k steps forward.",
     """import java.util.*;

public class Solution {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        Deque<Integer> dq = new ArrayDeque<>();
        dq.offerLast(0);
        for (int i = 1; i < n; i++) {
            if (!dq.isEmpty() && dq.peekFirst() < i - k) dq.pollFirst();
            dp[i] = nums[i] + dp[dq.peekFirst()];
            while (!dq.isEmpty() && dp[dq.peekLast()] <= dp[i]) dq.pollLast();
            dq.offerLast(i);
        }
        return dp[n - 1];
    }
}"""),

    # 11
    ("Merge Intervals & Overlap Detection", "Intervals",
     "Sorts intervals by their starting times, then traverses linearly, merging overlapping intervals whenever the current start time <= previous end time.",
     "Sorting imposes monotonic order on start coordinates, guaranteeing that all potential overlaps are contiguous in the sequence.",
     "Intervals: [[1, 3], [2, 6], [8, 10], [15, 18]]\\nCompare [1, 3] and [2, 6]: 2 <= 3 -> Merge to [1, max(3, 6)] = [1, 6]\\nCompare [1, 6] and [8, 10]: 8 > 6 -> Disjoint -> Append [8, 10]",
     """import java.util.*;

public class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];
        merged.add(current);
        
        for (int[] interval : intervals) {
            if (interval[0] <= current[1]) {
                current[1] = Math.max(current[1], interval[1]);
            } else {
                current = interval;
                merged.add(current);
            }
        }
        return merged.toArray(new int[merged.size()][]);
    }
}""",
     ["Line 5: Sort 2D intervals array by start coordinate a[0].", "Line 6-8: Initialize current interval as intervals[0] and add to merged list.", "Line 10-16: For each interval, check if start <= current[1]. If so, expand end time. Else start new disjoint interval."],
     "intervals = [[1, 3], [2, 6], [8, 10]]. Sorted order maintained. [1, 3] & [2, 6] merge to [1, 6]. [8, 10] disjoint. Result: [[1, 6], [8, 10]].",
     "O(N log N) Time, O(N) Auxiliary Space", ["Single interval", "All intervals disjoint", "All intervals nested inside one big interval"],
     ["Insert Interval", "Non-overlapping Intervals", "Meeting Rooms I & II"],
     "Merge Intervals", "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals.",
     """import java.util.*;

public class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        int[] curr = intervals[0];
        res.add(curr);
        for (int[] inv : intervals) {
            if (inv[0] <= curr[1]) curr[1] = Math.max(curr[1], inv[1]);
            else {
                curr = inv;
                res.add(curr);
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}""",
     "Insert Interval", "Insert a new interval into a sorted non-overlapping interval list and merge if necessary.",
     """import java.util.*;

public class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int i = 0, n = intervals.length;
        while (i < n && intervals[i][1] < newInterval[0]) res.add(intervals[i++]);
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.add(newInterval);
        while (i < n) res.add(intervals[i++]);
        return res.toArray(new int[res.size()][]);
    }
}"""),

    # 12
    ("Two Pointers (Dutch National Flag)", "Two Pointers",
     "Partitions an array containing three distinct values into three contiguous segments using three pointers: low, mid, and high in a single pass.",
     "Maintains four regions: [0..low-1] contains 0s, [low..mid-1] contains 1s, [mid..high] unexamined, [high+1..n-1] contains 2s.",
     "[ 2, 0, 2, 1, 1, 0 ]\\nMid encounters 2 -> Swap with High, High--\\nMid encounters 0 -> Swap with Low, Low++, Mid++\\nMid encounters 1 -> Mid++\\nResult: [0, 0, 1, 1, 2, 2]",
     """public class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high);
                high--;
            }
        }
    }
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}""",
     ["Line 3: Initialize low=0, mid=0, high=nums.length-1.", "Line 5-8: If nums[mid] is 0, swap with low and advance both low and mid.", "Line 9-10: If nums[mid] is 1, mid is in correct middle region; advance mid.", "Line 11-13: If nums[mid] is 2, swap with high and decrement high (do not advance mid)."],
     "nums = [2, 0, 1]. mid=0(2): swap with high(1) -> [1, 0, 2], high=1. mid=0(1): mid++. mid=1(0): swap with low(1) -> [0, 1, 2], low=1, mid=2. Finished!",
     "O(N) Time, O(1) Auxiliary Space", ["All elements equal", "Array already sorted", "Two elements inverted"],
     ["Sort Colors (0, 1, 2)", "Wiggle Sort II", "Sort Array by Parity"],
     "Sort Colors", "Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with colors 0, 1, and 2.",
     """public class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                int t = nums[low]; nums[low] = nums[mid]; nums[mid] = t;
                low++; mid++;
            } else if (nums[mid] == 1) mid++;
            else {
                int t = nums[mid]; nums[mid] = nums[high]; nums[high] = t;
                high--;
            }
        }
    }
}""",
     "3Sum", "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.",
     """import java.util.*;

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    l++; r--;
                } else if (sum < 0) l++;
                else r--;
            }
        }
        return res;
    }
}"""),

    # 13
    ("Top-K Elements via PriorityQueue (Min/Max Heap)", "Heap",
     "Maintains a min-heap of size K while iterating through an array. When heap exceeds size K, the minimum root element is polled.",
     "At all times the heap contains the K largest elements seen so far. Root is guaranteed to be the Kth largest.",
     "nums = [3, 2, 1, 5, 6, 4], k = 2\\nInsert 3, 2 -> Heap: [2, 3]\\nInsert 1 -> Heap: [1, 3, 2] -> size > 2 -> Poll 1\\nInsert 5 -> Heap: [2, 3, 5] -> Poll 2\\nInsert 6 -> Heap: [3, 5, 6] -> Poll 3\\nInsert 4 -> Heap: [4, 6, 5] -> Poll 4 -> Top is 5!",
     """import java.util.*;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);
        for (int num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        return minHeap.peek();
    }
}""",
     ["Line 5: Instantiate min-heap PriorityQueue of capacity k.", "Line 6-10: Push each element into the min-heap; if heap size exceeds k, evict the minimum element in O(log K).", "Line 12: Root of min-heap contains the Kth largest element."],
     "nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4. Heap retains [4, 5, 5, 6]. peek() returns 4.",
     "O(N log K) Time, O(K) Auxiliary Space", ["k == 1", "k == nums.length", "Negative numbers in array", "Duplicate top elements"],
     ["Top K Frequent Elements", "Kth Smallest Element in a Sorted Matrix", "Find K Closest Elements"],
     "Kth Largest Element in an Array", "Given an integer array nums and an integer k, return the kth largest element in the array.",
     """import java.util.*;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int val : nums) {
            pq.offer(val);
            if (pq.size() > k) pq.poll();
        }
        return pq.peek();
    }
}""",
     "Top K Frequent Elements", "Given an integer array nums and an integer k, return the k most frequent elements.",
     """import java.util.*;

public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) count.put(n, count.getOrDefault(n, 0) + 1);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> count.get(a) - count.get(b));
        for (int key : count.keySet()) {
            pq.offer(key);
            if (pq.size() > k) pq.poll();
        }
        int[] res = new int[k];
        for (int i = 0; i < k; i++) res[i] = pq.poll();
        return res;
    }
}"""),

    # 14
    ("K-Way Merge of Sorted Arrays / Lists", "Heap / PriorityQueue",
     "Uses a min-heap initialized with the head node of each of the K sorted lists. Extracts the minimum and advances that list's pointer.",
     "At each step, selecting the next smallest element across K lists takes O(log K) rather than O(K) linear comparison.",
     "Lists: L1: 1->4->5, L2: 1->3->4, L3: 2->6\\nHeap: [ (1, L1), (1, L2), (2, L3) ]\\nPoll (1, L1), Insert (4, L1)\\nPoll (1, L2), Insert (3, L2)...",
     """import java.util.*;

public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>(
            lists.length, (a, b) -> Integer.compare(a.val, b.val)
        );
        for (ListNode node : lists) {
            if (node != null) minHeap.offer(node);
        }
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (!minHeap.isEmpty()) {
            ListNode smallest = minHeap.poll();
            tail.next = smallest;
            tail = tail.next;
            if (smallest.next != null) {
                minHeap.offer(smallest.next);
            }
        }
        return dummy.next;
    }
}""",
     ["Line 5-7: Create PriorityQueue comparator ordering ListNode by val.", "Line 8-10: Offer non-null heads of all K lists into minHeap.", "Line 11-12: Create dummy sentinel node to simplify list building.", "Line 13-19: Poll smallest node, append to tail, and insert next node from same list."],
     "K=3 lists with total N nodes. Each node inserted once and polled once in O(log K). Total runtime O(N log K).",
     "O(N log K) Time, O(K) Auxiliary Space", ["Empty lists array", "Array containing null heads", "One list much longer than others"],
     ["Merge K Sorted Lists", "Find K Pairs with Smallest Sums", "Kth Smallest Element in a Sorted Matrix"],
     "Merge k Sorted Lists", "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
     """import java.util.*;

public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (ListNode l : lists) if (l != null) pq.offer(l);
        ListNode dummy = new ListNode(0), curr = dummy;
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            curr.next = node;
            curr = curr.next;
            if (node.next != null) pq.offer(node.next);
        }
        return dummy.next;
    }
}""",
     "Find K Pairs with Smallest Sums", "You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k. Return the k pairs (u, v) with the smallest sums.",
     """import java.util.*;

public class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums1.length == 0 || nums2.length == 0 || k == 0) return res;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (nums1[a[0]] + nums2[a[1]]) - (nums1[b[0]] + nums2[b[1]]));
        for (int i = 0; i < Math.min(nums1.length, k); i++) pq.offer(new int[]{i, 0});
        while (k-- > 0 && !pq.isEmpty()) {
            int[] cur = pq.poll();
            res.add(Arrays.asList(nums1[cur[0]], nums2[cur[1]]));
            if (cur[1] + 1 < nums2.length) pq.offer(new int[]{cur[0], cur[1] + 1});
        }
        return res;
    }
}"""),

    # 15
    ("Tree Traversals: BFS Level-Order", "Tree / BFS",
     "Explores tree nodes level by level using a FIFO Queue. In each iteration, records all nodes at the current level before expanding children.",
     "The queue size at the start of each level loop reflects exactly the count of nodes present on that level.",
     "Tree:       3\\n          /   \\\\\\n         9     20\\n              /  \\\\\\n             15   7\\nLevel 0: [3]\\nLevel 1: [9, 20]\\nLevel 2: [15, 7]",
     """import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>(levelSize);
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(currentLevel);
        }
        return result;
    }
}""",
     ["Line 11-13: Guard check and initialize queue with root.", "Line 15: Loop while queue has elements.", "Line 16: Freeze levelSize to process exactly one tier of the tree.", "Line 18-22: Poll node, append value, enqueue left and right children.", "Line 24: Add currentLevel list to overall result."],
     "Root 3: queue size 1 -> pop 3, enqueue 9, 20. Next level: size 2 -> pop 9 and 20, enqueue 15, 7. Result: [[3], [9, 20], [15, 7]].",
     "O(N) Time, O(W) Auxiliary Space (W = maximum width of tree)", ["Null root", "Single node tree", "Skewed linked-list like tree"],
     ["Binary Tree Zigzag Level Order Traversal", "Binary Tree Right Side View", "Average of Levels in Binary Tree"],
     "Binary Tree Level Order Traversal", "Given the root of a binary tree, return the level order traversal of its nodes' values.",
     """import java.util.*;

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> lvl = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                lvl.add(cur.val);
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            res.add(lvl);
        }
        return res;
    }
}""",
     "Binary Tree Right Side View", "Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.",
     """import java.util.*;

public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                if (i == sz - 1) res.add(cur.val);
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
        }
        return res;
    }
}"""),

    # 16
    ("Tree Traversals: DFS Pre, In, Post-Order", "Tree / DFS",
     "Traverses binary trees recursively or with an explicit stack visiting root and children in specified sequence.",
     "Recursion stack follows call frames matching tree height; post-order processes subtrees before root, enabling bottom-up aggregation.",
     "Pre-order:  Root -> Left -> Right\\nIn-order:   Left -> Root -> Right (Sorted in BST!)\\nPost-order: Left -> Right -> Root (Height / Diameter calculations)",
     """public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return 1 + Math.max(leftDepth, rightDepth);
    }
}""",
     ["Line 2: Base case: if root is null, depth is 0.", "Line 3-4: Recursively compute depth of left and right subtrees.", "Line 5: Return 1 plus the maximum depth of children."],
     "Tree [3, 9, 20, null, null, 15, 7]. Left child 9 returns 1. Right child 20 has children 15 and 7 (depth 2). Total depth = 1 + 2 = 3.",
     "O(N) Time, O(H) Auxiliary Space (H = height of tree)", ["Empty tree", "Single node", "Degenerate skewed tree (H = N)"],
     ["Diameter of Binary Tree", "Balanced Binary Tree", "Maximum Path Sum in Binary Tree"],
     "Maximum Depth of Binary Tree", "Given the root of a binary tree, return its maximum depth.",
     """public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}""",
     "Diameter of Binary Tree", "Given root of binary tree, return length of diameter (longest path between any two nodes).",
     """public class Solution {
    private int maxDiameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return maxDiameter;
    }
    private int depth(TreeNode node) {
        if (node == null) return 0;
        int l = depth(node.left), r = depth(node.right);
        maxDiameter = Math.max(maxDiameter, l + r);
        return 1 + Math.max(l, r);
    }
}"""),

    # 17
    ("Binary Search Tree (BST) Validation", "Binary Search Tree",
     "Validates that for every node in a tree, all nodes in its left subtree are strictly smaller and all nodes in its right subtree are strictly greater.",
     "Passes down valid value bounds [low, high] that tighten as we descend into left and right subtrees.",
     "Node Val = 5, Allowed Range: (-inf, +inf)\\nLeft Child = 3, Allowed Range: (-inf, 5)\\nRight Child = 7, Allowed Range: (5, +inf)",
     """public class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }
    private boolean validate(TreeNode node, Integer low, Integer high) {
        if (node == null) return true;
        if ((low != null && node.val <= low) || (high != null && node.val >= high)) {
            return false;
        }
        return validate(node.left, low, node.val) && validate(node.right, node.val, high);
    }
}""",
     ["Line 2-4: Entry method passing null bounds (representing infinity).", "Line 5: Base case: empty node is valid BST.", "Line 6-8: If current node violates lower or upper bound, return false.", "Line 9: Recursively validate left subtree with upper bound = node.val, and right subtree with lower bound = node.val."],
     "Node 5 -> left child 1 (range -inf..5, valid); right child 4 (range 5..inf, node.val 4 <= 5 -> INVALID). Returns false.",
     "O(N) Time, O(H) Auxiliary Space", ["Single node", "Duplicate values (invalid in strict BST)", "Integer.MIN_VALUE or MAX_VALUE bounds handled safely with Integer objects"],
     ["Kth Smallest Element in a BST", "Inorder Successor in BST", "Convert Sorted Array to Binary Search Tree"],
     "Validate Binary Search Tree", "Given the root of a binary tree, determine if it is a valid binary search tree (BST).",
     """public class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }
    private boolean validate(TreeNode node, Integer low, Integer high) {
        if (node == null) return true;
        if ((low != null && node.val <= low) || (high != null && node.val >= high)) return false;
        return validate(node.left, low, node.val) && validate(node.right, node.val, high);
    }
}""",
     "Kth Smallest Element in a BST", "Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.",
     """import java.util.*;

public class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            if (--k == 0) return curr.val;
            curr = curr.right;
        }
        return -1;
    }
}"""),

    # 18
    ("Lowest Common Ancestor (LCA) in Binary Trees", "Tree / Recursion",
     "Finds the lowest common ancestor of two nodes p and q by searching left and right subtrees recursively.",
     "If p and q are found in different subtrees of node N, N is their LCA. If both lie in the same subtree, that subtree's root returns the LCA.",
     "Tree:\\n        3\\n       / \\\\\\n      5   1\\n     / \\\\ / \\\\\\n    6  2 0  8\\nNodes 5 and 1: 5 is in left subtree, 1 is in right subtree ==> LCA is 3!",
     """public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
}""",
     ["Line 2: Base case: if root is null or matches p or q, return root.", "Line 3-4: Recursively search for p and q in left and right subtrees.", "Line 5: If both left and right return non-null, p and q are in separate branches; root is their LCA.", "Line 6: Otherwise return the non-null branch."],
     "Find LCA of 5 and 4. 5 matches immediately. Left returns 5. Right returns null. LCA returns node 5.",
     "O(N) Time, O(H) Auxiliary Space", ["p is direct parent of q", "p and q on leaf levels", "Binary Search Tree variation uses value comparison"],
     ["Lowest Common Ancestor of a Binary Search Tree", "Lowest Common Ancestor of Deepest Leaves"],
     "Lowest Common Ancestor of a Binary Tree", "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.",
     """public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode l = lowestCommonAncestor(root.left, p, q);
        TreeNode r = lowestCommonAncestor(root.right, p, q);
        if (l != null && r != null) return root;
        return l != null ? l : r;
    }
}""",
     "Lowest Common Ancestor of a Binary Search Tree", "Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.",
     """public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root.val > p.val && root.val > q.val) return lowestCommonAncestor(root.left, p, q);
        if (root.val < p.val && root.val < q.val) return lowestCommonAncestor(root.right, p, q);
        return root;
    }
}"""),

    # 19
    ("Graph Traversal: Breadth-First Search (BFS)", "Graph / BFS",
     "Explores graph vertices layer by layer from one or more source vertices using a queue. Guarantees finding the shortest path in unweighted graphs.",
     "First time a vertex is popped from the queue corresponds to its minimum edge distance from the source.",
     "Rotting Oranges Grid:\\nMinute 0: [2, 1, 1]\\nMinute 1: [2, 2, 1]\\nMinute 2: [2, 2, 2] -> 2 minutes to rot all fresh oranges!",
     """import java.util.*;

public class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> queue = new ArrayDeque<>();
        int freshCount = 0;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) queue.offer(new int[]{r, c});
                else if (grid[r][c] == 1) freshCount++;
            }
        }
        if (freshCount == 0) return 0;
        int minutes = 0;
        int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        
        while (!queue.isEmpty() && freshCount > 0) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                for (int[] d : directions) {
                    int nr = cell[0] + d[0], nc = cell[1] + d[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        freshCount--;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
            minutes++;
        }
        return freshCount == 0 ? minutes : -1;
    }
}""",
     ["Line 5-13: Scan grid, enqueue all initially rotten oranges, count fresh oranges.", "Line 14: If no fresh oranges exist, return 0.", "Line 18: While queue is non-empty and fresh oranges remain, advance minutes.", "Line 24-27: Rot adjacent fresh oranges, decrement freshCount, enqueue new rotten cells.", "Line 32: Return minutes if all fresh oranges rotted, else -1."],
     "Grid with 1 rotten, 6 fresh. BFS spreads to 4 neighbors each minute. Takes 4 minutes. Returns 4.",
     "O(R * C) Time, O(R * C) Auxiliary Space", ["No fresh oranges initially (return 0)", "Unreachable fresh orange (return -1)", "All oranges rotten initially"],
     ["Word Ladder", "Shortest Path in Binary Matrix", "01 Matrix"],
     "Rotting Oranges", "You are given an m x n grid where each cell has values 0 (empty), 1 (fresh), or 2 (rotten). Return the minimum number of minutes that must elapse until no cell has a fresh orange.",
     """import java.util.*;

public class Solution {
    public int orangesRotting(int[][] grid) {
        int r = grid.length, c = grid[0].length, fresh = 0;
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 2) q.offer(new int[]{i, j});
                else if (grid[i][j] == 1) fresh++;
            }
        }
        if (fresh == 0) return 0;
        int mins = 0;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        while (!q.isEmpty() && fresh > 0) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int[] cur = q.poll();
                for (int[] d : dirs) {
                    int ni = cur[0] + d[0], nj = cur[1] + d[1];
                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && grid[ni][nj] == 1) {
                        grid[ni][nj] = 2;
                        fresh--;
                        q.offer(new int[]{ni, nj});
                    }
                }
            }
            mins++;
        }
        return fresh == 0 ? mins : -1;
    }
}""",
     "Shortest Path in Binary Matrix", "Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.",
     """import java.util.*;

public class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) return -1;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0, 1});
        grid[0][0] = 1;
        int[][] dirs = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (cur[0] == n - 1 && cur[1] == n - 1) return cur[2];
            for (int[] d : dirs) {
                int ni = cur[0] + d[0], nj = cur[1] + d[1];
                if (ni >= 0 && ni < n && nj >= 0 && nj < n && grid[ni][nj] == 0) {
                    grid[ni][nj] = 1;
                    q.offer(new int[]{ni, nj, cur[2] + 1});
                }
            }
        }
        return -1;
    }
}"""),

    # 20
    ("Graph Traversal: DFS & Connected Components", "Graph / DFS",
     "Traverses connected components of an adjacency graph or 2D grid recursively, marking visited nodes in-place to avoid re-traversal.",
     "Visits each vertex and edge exactly once, partitioning the graph into distinct connected components.",
     "Grid:\\n1 1 0 0 0\\n1 1 0 0 0\\n0 0 1 0 0\\n0 0 0 1 1\\nComponent 1: (0,0),(0,1),(1,0),(1,1)\\nComponent 2: (2,2)\\nComponent 3: (3,3),(3,4) ==> Total Islands = 3",
     """public class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int count = 0;
        int rows = grid.length, cols = grid[0].length;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    dfs(grid, r, c, rows, cols);
                }
            }
        }
        return count;
    }
    
    private void dfs(char[][] grid, int r, int c, int rows, int cols) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') return;
        grid[r][c] = '0'; // Sink island in-place
        dfs(grid, r + 1, c, rows, cols);
        dfs(grid, r - 1, c, rows, cols);
        dfs(grid, r, c + 1, rows, cols);
        dfs(grid, r, c - 1, rows, cols);
    }
}""",
     ["Line 4: Loop through each grid cell.", "Line 7: When an unvisited land cell '1' is found, increment island count.", "Line 9: Call DFS to sink the entire contiguous island into water '0'.", "Line 17: In-place sinking prevents allocating auxiliary visited arrays."],
     "Grid 4x5 with 3 separate clusters of '1'. DFS triggers 3 times. Returns 3.",
     "O(R * C) Time, O(R * C) Auxiliary Space (Call stack)", ["Grid with all '0' (returns 0)", "Grid with all '1' (returns 1)", "Diagonal connections (not adjacent, counts as separate)"],
     ["Max Area of Island", "Surrounded Regions", "Pacific Atlantic Water Flow"],
     "Number of Islands", "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.",
     """public class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    sink(grid, i, j);
                }
            }
        }
        return count;
    }
    private void sink(char[][] g, int i, int j) {
        if (i < 0 || i >= g.length || j < 0 || j >= g[0].length || g[i][j] != '1') return;
        g[i][j] = '0';
        sink(g, i+1, j); sink(g, i-1, j); sink(g, i, j+1); sink(g, i, j-1);
    }
}""",
     "Max Area of Island", "Given an m x n binary matrix grid, return the maximum area of an island in grid.",
     """public class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) max = Math.max(max, area(grid, i, j));
            }
        }
        return max;
    }
    private int area(int[][] g, int i, int j) {
        if (i < 0 || i >= g.length || j < 0 || j >= g[0].length || g[i][j] != 1) return 0;
        g[i][j] = 0;
        return 1 + area(g, i+1, j) + area(g, i-1, j) + area(g, i, j+1) + area(g, i, j-1);
    }
}"""),

    # 21
    ("Topological Sorting (Kahn's Algorithm)", "Graph / Topo Sort",
     "Finds linear order of vertices in a Directed Acyclic Graph (DAG) using in-degrees and a queue.",
     "A vertex with in-degree 0 has no unmet dependencies and can execute immediately; removing it unlocks dependent vertices.",
     "Courses: 2, Prereq: [1, 0] (Take 0 before 1)\\nIn-degree: [0: 0, 1: 1]\\nQueue initially: [0]\\nProcess 0: In-degree of 1 becomes 0 -> Queue: [1]\\nProcess 1 -> Total processed = 2 == numCourses ==> Possible!",
     """import java.util.*;

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>(numCourses);
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        
        for (int[] pair : prerequisites) {
            adj.get(pair[1]).add(pair[0]);
            inDegree[pair[0]]++;
        }
        
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) queue.offer(i);
        }
        
        int completed = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            completed++;
            for (int neighbor : adj.get(course)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        return completed == numCourses;
    }
}""",
     ["Line 4-5: Initialize inDegree array and adjacency list.", "Line 7-10: Populate directed edges from prerequisite to course and tally in-degrees.", "Line 12-15: Enqueue all courses with in-degree 0.", "Line 17-27: BFS traversal decrementing dependent in-degrees. Return completed == numCourses."],
     "numCourses = 2, [[1, 0], [0, 1]] -> Cycle exists. Queue stays empty. completed = 0 != 2 -> returns false.",
     "O(V + E) Time, O(V + E) Auxiliary Space", ["Graph with cycle (returns false)", "Disconnected graph with multiple valid orders", "Self loop dependency"],
     ["Course Schedule II (Return Order)", "Alien Dictionary", "Minimum Height Trees"],
     "Course Schedule", "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Return true if you can finish all courses.",
     """import java.util.*;

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] p : prerequisites) {
            adj.get(p[1]).add(p[0]);
            inDegree[p[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) if (inDegree[i] == 0) q.offer(i);
        int done = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            done++;
            for (int next : adj.get(cur)) {
                if (--inDegree[next] == 0) q.offer(next);
            }
        }
        return done == numCourses;
    }
}""",
     "Course Schedule II", "Return the ordering of courses you should take to finish all courses. If it is impossible, return an empty array.",
     """import java.util.*;

public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] p : prerequisites) {
            adj.get(p[1]).add(p[0]);
            inDegree[p[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) if (inDegree[i] == 0) q.offer(i);
        int[] order = new int[numCourses];
        int idx = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            order[idx++] = cur;
            for (int next : adj.get(cur)) {
                if (--inDegree[next] == 0) q.offer(next);
            }
        }
        return idx == numCourses ? order : new int[0];
    }
}"""),

    # 22
    ("Disjoint Set Union (Union-Find)", "Graph / DSU",
     "Maintains disjoint sets supporting near O(1) find and union operations using Path Compression and Union by Rank.",
     "Path compression flattens tree structure on lookup, keeping tree depth effectively constant (Ackermann inverse alpha(N) < 5).",
     "Nodes: 1, 2, 3\\nUnion(1, 2): parent[2] = 1\\nUnion(2, 3): Find(2)->1, parent[3] = 1\\nCycle Check: Edge (1, 3): Find(1)==1, Find(3)==1 -> Same component ==> CYCLE DETECTED!",
     """public class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        int[] parent = new int[n + 1];
        for (int i = 1; i <= n; i++) parent[i] = i;
        
        for (int[] edge : edges) {
            int rootU = find(parent, edge[0]);
            int rootV = find(parent, edge[1]);
            if (rootU == rootV) return edge; // Redundant edge completes cycle
            parent[rootU] = rootV;
        }
        return new int[0];
    }
    
    private int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]); // Path compression
        }
        return parent[x];
    }
}""",
     ["Line 4-5: Initialize parent array where each vertex is its own parent.", "Line 7-12: For each edge, find roots of both vertices. If roots match, edge creates a cycle; return it. Else union sets.", "Line 16-19: Recursive find with path compression pointing nodes directly to root."],
     "Edges [[1,2],[1,3],[2,3]]. (1,2) and (1,3) merged into set 1. Edge (2,3) connects two nodes already in set 1 -> Redundant edge returned: [2, 3].",
     "O(N * alpha(N)) Time, O(N) Auxiliary Space", ["Tree with single redundant edge", "Disjoint graph with multiple trees", "Linear chain graph"],
     ["Number of Provinces", "Redundant Connection", "Graph Valid Tree"],
     "Number of Provinces", "There are n cities. A province is a group of directly or indirectly connected cities. Return the total number of provinces.",
     """public class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int count = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    int r1 = find(parent, i), r2 = find(parent, j);
                    if (r1 != r2) {
                        parent[r1] = r2;
                        count--;
                    }
                }
            }
        }
        return count;
    }
    private int find(int[] p, int x) {
        if (p[x] != x) p[x] = find(p, p[x]);
        return p[x];
    }
}""",
     "Redundant Connection", "Return an edge that can be removed so that the resulting graph is a tree of n nodes.",
     """public class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int[] p = new int[edges.length + 1];
        for (int i = 1; i < p.length; i++) p[i] = i;
        for (int[] e : edges) {
            int r1 = find(p, e[0]), r2 = find(p, e[1]);
            if (r1 == r2) return e;
            p[r1] = r2;
        }
        return new int[0];
    }
    private int find(int[] p, int x) {
        if (p[x] != x) p[x] = find(p, p[x]);
        return p[x];
    }
}"""),

    # 23
    ("Dijkstra's Shortest Path Algorithm", "Graph / Greedy",
     "Finds the shortest path from a single source to all other vertices in a weighted graph with non-negative edge weights using a min-heap PriorityQueue.",
     "Greedily expands the vertex with the lowest tentative distance; non-negative weights guarantee that once visited, its optimal distance is finalized.",
     "Source = 1\\nDist: [1:0, 2:inf, 3:inf]\\nEdge (1, 2, wt=4) -> Dist[2] = 4\\nEdge (1, 3, wt=2) -> Dist[3] = 2\\nNext smallest is 3 -> Edge (3, 2, wt=1) -> Dist[2] = min(4, 2+1) = 3!",
     """import java.util.*;

public class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] time : times) {
            graph.computeIfAbsent(time[0], x -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }
        
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        minHeap.offer(new int[]{k, 0}); // {node, distance}
        Map<Integer, Integer> dist = new HashMap<>();
        
        while (!minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            int node = curr[0], d = curr[1];
            if (dist.containsKey(node)) continue;
            dist.put(node, d);
            
            if (graph.containsKey(node)) {
                for (int[] edge : graph.get(node)) {
                    int neighbor = edge[0], weight = edge[1];
                    if (!dist.containsKey(neighbor)) {
                        minHeap.offer(new int[]{neighbor, d + weight});
                    }
                }
            }
        }
        if (dist.size() != n) return -1;
        int maxDist = 0;
        for (int d : dist.values()) maxDist = Math.max(maxDist, d);
        return maxDist;
    }
}""",
     ["Line 4-7: Build adjacency list graph where node maps to (target, weight).", "Line 9-10: Initialize min-heap with source node k at distance 0.", "Line 14-17: Pop node with lowest distance; if already finalized, skip.", "Line 19-25: Relax outward edges from current node.", "Line 28-31: Return max distance if all nodes reached, else -1."],
     "Times: [[2,1,1],[2,3,1],[3,4,1]], N=4, K=2. Distance to 1 is 1, to 3 is 1, to 4 is 2. Max distance = 2. Returns 2.",
     "O((V + E) log V) Time, O(V + E) Auxiliary Space", ["Unreachable destination (returns -1)", "Source has no outgoing edges", "Cycles with positive weights"],
     ["Cheapest Flights Within K Stops", "Path with Minimum Effort", "Swim in Rising Water"],
     "Network Delay Time", "You are given a network of n nodes, labeled from 1 to n. Return the minimum time it takes for all the n nodes to receive the signal.",
     """import java.util.*;

public class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;
        for (int i = 1; i <= n - 1; i++) {
            for (int[] e : times) {
                if (dist[e[0]] != Integer.MAX_VALUE && dist[e[0]] + e[2] < dist[e[1]]) {
                    dist[e[1]] = dist[e[0]] + e[2];
                }
            }
        }
        int max = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1;
            max = Math.max(max, dist[i]);
        }
        return max;
    }
}""",
     "Path with Minimum Effort", "Find a route from top-left to bottom-right that requires the minimum effort (maximum absolute difference in heights between consecutive cells).",
     """import java.util.*;

public class Solution {
    public int minimumEffortPath(int[][] heights) {
        int r = heights.length, c = heights[0].length;
        int[][] dist = new int[r][c];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        pq.offer(new int[]{0, 0, 0});
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            if (cur[0] == r - 1 && cur[1] == c - 1) return cur[2];
            for (int[] d : dirs) {
                int ni = cur[0] + d[0], nj = cur[1] + d[1];
                if (ni >= 0 && ni < r && nj >= 0 && nj < c) {
                    int effort = Math.max(cur[2], Math.abs(heights[cur[0]][cur[1]] - heights[ni][nj]));
                    if (effort < dist[ni][nj]) {
                        dist[ni][nj] = effort;
                        pq.offer(new int[]{ni, nj, effort});
                    }
                }
            }
        }
        return 0;
    }
}"""),

    # 24
    ("Dynamic Programming: 1D Array", "Dynamic Programming",
     "Solves optimization problems with overlapping subproblems and optimal substructure by caching solutions in a 1D state array or two running variables.",
     "Deciding optimal outcome at state i depends strictly on preceding states (e.g. dp[i] = max(dp[i-1], dp[i-2] + nums[i])).",
     "Houses: [ 2, 7, 9, 3, 1 ]\\ni=0: Rob 2 -> 2\\ni=1: Max(2, 7) -> 7\\ni=2: Max(7, 2 + 9) -> 11\\ni=3: Max(11, 7 + 3) -> 11\\ni=4: Max(11, 11 + 1) -> 12 ==> Max Loot = 12",
     """public class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        
        int prev2 = 0;
        int prev1 = 0;
        for (int num : nums) {
            int current = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}""",
     ["Line 4-5: Handle base cases for empty or single-house array.", "Line 7-8: Track optimal values of two previous houses (prev2 and prev1).", "Line 9-13: Transition: current max is either skipping current house (prev1) or robbing current house (prev2 + num).", "Line 14: Return optimal loot in O(1) space."],
     "nums = [2, 7, 9, 3, 1]. Step 1: 2. Step 2: 7. Step 3: 11. Step 4: 11. Step 5: 12. Returns 12.",
     "O(N) Time, O(1) Auxiliary Space", ["Single house", "All houses zero value", "Circular houses constraint (House Robber II)"],
     ["Climbing Stairs", "House Robber II (Circular)", "Decode Ways", "Min Cost Climbing Stairs"],
     "House Robber", "You are planning to rob houses along a street. Each house has a certain amount of money stashed. Determine the maximum amount of money you can rob tonight without alerting the police.",
     """public class Solution {
    public int rob(int[] nums) {
        int prev1 = 0, prev2 = 0;
        for (int x : nums) {
            int cur = Math.max(prev1, prev2 + x);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}""",
     "Climbing Stairs", "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
     """public class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}"""),

    # 25
    ("Dynamic Programming: 0/1 Knapsack & Partition", "Dynamic Programming",
     "Determines if an exact target value can be achieved by choosing each element at most once using bottom-up boolean tabulation.",
     "dp[w] indicates whether a subset summing to w is achievable; updating backwards from target to num prevents using the same element multiple times.",
     "Nums = [1, 5, 11, 5], Total Sum = 22 -> Target = 11\\ndp[0] = true\\nnum = 1: dp[1] = true\\nnum = 5: dp[6]=true, dp[5]=true\\nnum = 11: dp[11] = true ==> Partition Possible!",
     """public class Solution {
    public boolean canPartition(int[] nums) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        if (totalSum % 2 != 0) return false;
        
        int target = totalSum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        
        for (int num : nums) {
            for (int w = target; w >= num; w--) {
                dp[w] = dp[w] || dp[w - num];
            }
        }
        return dp[target];
    }
}""",
     ["Line 4-5: Compute total sum; odd sum can never be divided into two equal integers.", "Line 7: Set target = totalSum / 2.", "Line 8-9: Initialize dp array with dp[0] = true.", "Line 11-15: Reverse inner loop (from target down to num) guarantees 0/1 Knapsack semantics (each element used once).", "Line 16: Return dp[target]."],
     "nums = [1, 5, 11, 5]. target = 11. Array reaches dp[11] = true. Returns true.",
     "O(N * Target) Time, O(Target) Auxiliary Space", ["Odd sum (returns false immediately)", "Single element array", "Target requires all elements"],
     ["Partition Equal Subset Sum", "Target Sum", "Coin Change (Unbounded variant)", "Combination Sum IV"],
     "Partition Equal Subset Sum", "Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.",
     """public class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int n : nums) sum += n;
        if (sum % 2 != 0) return false;
        int target = sum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums) {
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }
        return dp[target];
    }
}""",
     "Coin Change", "You are given an integer array coins representing coins of different denominations and an integer amount. Return fewest coins to make up that amount.",
     """import java.util.*;

public class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int c : coins) {
                if (i >= c) dp[i] = Math.min(dp[i], dp[i - c] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}"""),

    # 26
    ("Dynamic Programming: Longest Common Subsequence (LCS)", "Dynamic Programming",
     "Finds the length of the longest subsequence present in both strings in the same relative order using a 2D matrix.",
     "If characters match (s1[i-1] == s2[j-1]), dp[i][j] = 1 + dp[i-1][j-1]; otherwise take max of excluding one character: max(dp[i-1][j], dp[i][j-1]).",
     "text1 = 'abcde', text2 = 'ace'\\nMatrix matches on 'a', 'c', 'e'.\\ndp[5][3] = 3 (LCS = 'ace')",
     """public class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
}""",
     ["Line 3-4: Allocate (m+1) x (n+1) DP matrix with zero baseline.", "Line 6-7: Nested iteration over characters of both strings.", "Line 8-9: Matching characters increment diagonal predecessor.", "Line 10-12: Mismatched characters inherit maximum of top or left cell.", "Line 15: Return dp[m][n]."],
     "text1 = 'abc', text2 = 'def' -> No character matches -> matrix filled with 0s. Returns 0.",
     "O(M * N) Time, O(M * N) Auxiliary Space", ["Identical strings (returns length)", "Completely disjoint strings (returns 0)", "Single character strings"],
     ["Edit Distance (Levenshtein Distance)", "Delete Operation for Two Strings", "Shortest Common Supersequence"],
     "Longest Common Subsequence", "Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.",
     """public class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[i][j] = 1 + dp[i - 1][j - 1];
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[m][n];
    }
}""",
     "Edit Distance", "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2 (insert, delete, replace).",
     """public class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));
            }
        }
        return dp[m][n];
    }
}"""),

    # 27
    ("Dynamic Programming: Longest Increasing Subsequence (LIS)", "Dynamic Programming",
     "Finds the length of the longest strictly increasing subsequence using Patience Sorting and Binary Search.",
     "Maintains tails array where tails[i] stores smallest tail element of all increasing subsequences of length i+1. Binary search replaces or extends in O(log N).",
     "nums = [10, 9, 2, 5, 3, 7, 101, 18]\\ntails array:\\n[10] -> [9] -> [2] -> [2, 5] -> [2, 3] -> [2, 3, 7] -> [2, 3, 7, 101] -> [2, 3, 7, 18]\\nLength of tails = 4 (e.g. [2, 3, 7, 18])",
     """import java.util.*;

public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int[] tails = new int[nums.length];
        int size = 0;
        
        for (int x : nums) {
            int left = 0, right = size;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (tails[mid] < x) left = mid + 1;
                else right = mid;
            }
            tails[left] = x;
            if (left == size) size++;
        }
        return size;
    }
}""",
     ["Line 4: Guard check for empty input.", "Line 5: tails[i] holds lowest tail value of length i+1.", "Line 8: For each element x in nums, perform binary search on tails.", "Line 15: If x is greater than all existing tails, extend size by 1.", "Line 17: Return size, which represents maximum LIS length."],
     "nums = [0, 1, 0, 3, 2, 3]. tails transitions: [0] -> [0, 1] -> [0, 1, 3] -> [0, 1, 2] -> [0, 1, 2, 3]. Length = 4.",
     "O(N log N) Time, O(N) Auxiliary Space", ["Strictly decreasing array (size = 1)", "All equal elements (size = 1 for strictly increasing)", "Already sorted array"],
     ["Russian Doll Envelopes", "Number of Longest Increasing Subsequence", "Maximum Length of Pair Chain"],
     "Longest Increasing Subsequence", "Given an integer array nums, return the length of the longest strictly increasing subsequence.",
     """public class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int sz = 0;
        for (int x : nums) {
            int l = 0, r = sz;
            while (l < r) {
                int m = l + (r - l) / 2;
                if (tails[m] < x) l = m + 1;
                else r = m;
            }
            tails[l] = x;
            if (l == sz) sz++;
        }
        return sz;
    }
}""",
     "Russian Doll Envelopes", "You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]. Return the maximum number of envelopes you can Russian doll.",
     """import java.util.*;

public class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        int[] tails = new int[envelopes.length];
        int sz = 0;
        for (int[] env : envelopes) {
            int h = env[1];
            int l = 0, r = sz;
            while (l < r) {
                int m = l + (r - l) / 2;
                if (tails[m] < h) l = m + 1;
                else r = m;
            }
            tails[l] = h;
            if (l == sz) sz++;
        }
        return sz;
    }
}"""),

    # 28
    ("Backtracking: Subsets & Permutations", "Backtracking",
     "Systematically constructs candidate solutions step-by-step, abandoning candidates ('backtracking') as soon as it determines they cannot lead to a valid solution.",
     "Recursively explores state tree, appending choice, descending, and undoing choice (backtracking) to restore state.",
     "nums = [1, 2, 3]\\nChoice: []\\n+1 -> [1] (+2 -> [1, 2] (+3 -> [1, 2, 3]))\\nBacktrack -> [1, 2] -> Backtrack -> [1] (+3 -> [1, 3])\\nTotal Subsets = 2^N = 8",
     """import java.util.*;

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current)); // Snapshot current subset
        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);                  // Make choice
            backtrack(nums, i + 1, current, result); // Recurse
            current.remove(current.size() - 1);    // Backtrack (undo choice)
        }
    }
}""",
     ["Line 4: Initialize result list of lists.", "Line 5: Call backtrack helper starting at index 0.", "Line 9: Add a clone of current state to result snapshot.", "Line 10-14: Standard choice, recursive descent, and undo-choice pattern."],
     "nums = [1, 2]. Result snapshots: [], [1], [1, 2], [2]. Total 4 subsets = 2^2.",
     "O(N * 2^N) Time, O(N) Auxiliary Space (Call stack)", ["Empty array (returns [[]])", "Duplicates handling (Subsets II)", "Permutations variation (N! complexity)"],
     ["Subsets II (with duplicates)", "Permutations", "Combination Sum", "Generate Parentheses"],
     "Subsets", "Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets.",
     """import java.util.*;

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), res);
        return res;
    }
    private void dfs(int[] nums, int start, List<Integer> cur, List<List<Integer>> res) {
        res.add(new ArrayList<>(cur));
        for (int i = start; i < nums.length; i++) {
            cur.add(nums[i]);
            dfs(nums, i + 1, cur, res);
            cur.remove(cur.size() - 1);
        }
    }
}""",
     "Permutations", "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.",
     """import java.util.*;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        dfs(nums, used, new ArrayList<>(), res);
        return res;
    }
    private void dfs(int[] nums, boolean[] used, List<Integer> cur, List<List<Integer>> res) {
        if (cur.size() == nums.length) {
            res.add(new ArrayList<>(cur));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            cur.add(nums[i]);
            dfs(nums, used, cur, res);
            cur.remove(cur.size() - 1);
            used[i] = false;
        }
    }
}"""),

    # 29
    ("Trie (Prefix Tree) Insertion & Search", "Trie / Tree",
     "Tree data structure used to locate specific keys from within a set. Every node represents a character; words sharing prefixes share path nodes.",
     "Prefix lookups execute in O(L) time where L is word length, completely independent of the total dictionary word count N.",
     "Insert 'apple', 'app'\\nRoot -> 'a' -> 'p' -> 'p' (isEnd=true) -> 'l' -> 'e' (isEnd=true)\\nSearch 'app' -> true\\nStartsWith 'app' -> true",
     """public class Trie {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEndOfWord = false;
    }
    
    private final TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = findNode(word);
        return node != null && node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }
    
    private TrieNode findNode(String str) {
        TrieNode node = root;
        for (char c : str.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return null;
            node = node.children[idx];
        }
        return node;
    }
}""",
     ["Line 2-5: Define TrieNode containing array of 26 child references and boolean terminal flag.", "Line 12-21: Insert traverses characters, allocating new nodes when child branch is null.", "Line 24-26: Search verifies both path existence and terminal isEndOfWord flag.", "Line 28-30: StartsWith verifies only path existence."],
     "Insert 'cat', 'car'. Nodes 'c' and 'a' shared. Branching happens at 't' vs 'r'. search('ca') is false; startsWith('ca') is true.",
     "O(L) Time per operation, O(Total Characters) Auxiliary Space", ["Empty string", "Searching word longer than any stored prefix", "Duplicate word inserts"],
     ["Design Add and Search Words Data Structure", "Word Search II", "Replace Words", "Maximum XOR of Two Numbers in an Array"],
     "Implement Trie (Prefix Tree)", "A trie (pronounced as 'try') or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.",
     """public class Trie {
    private Trie[] next = new Trie[26];
    private boolean isEnd = false;
    public Trie() {}
    public void insert(String word) {
        Trie cur = this;
        for (char c : word.toCharArray()) {
            if (cur.next[c - 'a'] == null) cur.next[c - 'a'] = new Trie();
            cur = cur.next[c - 'a'];
        }
        cur.isEnd = true;
    }
    public boolean search(String word) {
        Trie cur = this;
        for (char c : word.toCharArray()) {
            if (cur.next[c - 'a'] == null) return false;
            cur = cur.next[c - 'a'];
        }
        return cur.isEnd;
    }
    public boolean startsWith(String prefix) {
        Trie cur = this;
        for (char c : prefix.toCharArray()) {
            if (cur.next[c - 'a'] == null) return false;
            cur = cur.next[c - 'a'];
        }
        return true;
    }
}""",
     "Word Search II", "Given an m x n board of characters and a list of strings words, return all words on the board.",
     """import java.util.*;

public class Solution {
    static class Node {
        Node[] next = new Node[26];
        String word;
    }
    public List<String> findWords(char[][] board, String[] words) {
        Node root = new Node();
        for (String w : words) {
            Node cur = root;
            for (char c : w.toCharArray()) {
                if (cur.next[c - 'a'] == null) cur.next[c - 'a'] = new Node();
                cur = cur.next[c - 'a'];
            }
            cur.word = w;
        }
        List<String> res = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, root, res);
            }
        }
        return res;
    }
    private void dfs(char[][] b, int i, int j, Node node, List<String> res) {
        if (i < 0 || i >= b.length || j < 0 || j >= b[0].length) return;
        char c = b[i][j];
        if (c == '#' || node.next[c - 'a'] == null) return;
        node = node.next[c - 'a'];
        if (node.word != null) {
            res.add(node.word);
            node.word = null;
        }
        b[i][j] = '#';
        dfs(b, i+1, j, node, res); dfs(b, i-1, j, node, res); dfs(b, i, j+1, node, res); dfs(b, i, j-1, node, res);
        b[i][j] = c;
    }
}"""),

    # 30
    ("Bit Manipulation: XOR Properties & Bit Hacks", "Bit Manipulation",
     "Leverages fundamental bitwise properties: x ^ x = 0, x ^ 0 = x, and associativity to isolate unique values in O(1) space.",
     "Pairs of identical numbers cancel each other out to 0; the sole unique number survives XOR reduction.",
     "nums = [ 4, 1, 2, 1, 2 ]\\n4 ^ 1 ^ 2 ^ 1 ^ 2\\n= 4 ^ (1 ^ 1) ^ (2 ^ 2)\\n= 4 ^ 0 ^ 0 = 4!",
     """public class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
}""",
     ["Line 3: Initialize result accumulator with 0.", "Line 4-6: Iterate through entire array, applying XOR assignment result ^= num.", "Line 7: Return final result, which holds the non-duplicate value."],
     "nums = [2, 2, 1]. result = 0 ^ 2 = 2. result = 2 ^ 2 = 0. result = 0 ^ 1 = 1. Returns 1.",
     "O(N) Time, O(1) Auxiliary Space", ["Single element array", "Negative numbers (XOR works identically on two's complement)", "All pairs cancelled"],
     ["Counting Bits", "Number of 1 Bits (Hamming Weight)", "Single Number II & III", "Reverse Bits"],
     "Single Number", "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.",
     """public class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int n : nums) res ^= n;
        return res;
    }
}""",
     "Counting Bits", "Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.",
     """public class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }
}""")
]

# Merge into ALL_PATTERNS
for m in METAS:
    ALL_PATTERNS.append({
        "pattern_name": m[0],
        "category": m[1],
        "concept": m[2],
        "why_it_works": m[3],
        "visual_explanation": m[4],
        "java_code": m[5],
        "line_by_line_walkthrough": m[6],
        "dry_run": m[7],
        "complexity": m[8],
        "edge_cases": m[9],
        "interview_variations": m[10],
        "p1_title": m[11],
        "p1_stmt": m[12],
        "p1_code": m[13],
        "p2_title": m[14],
        "p2_stmt": m[15],
        "p2_code": m[16]
    })

print(f"Total patterns prepared: {len(ALL_PATTERNS)}")

# Write scripts/curriculum/dsa_curriculum.py
dsa_curriculum_code = '''#!/usr/bin/env python3
"""
scripts/curriculum/dsa_curriculum.py
Complete 30-Day DSA & Placement Coding Curriculum in 100% JAVA 17+.

For EVERY Day 1 to Day 30:
1. DSA Pattern deep-dive:
   - pattern_name
   - category
   - concept
   - why_it_works
   - visual_explanation
   - java_code (Production Java 17+)
   - line_by_line_walkthrough
   - dry_run
   - complexity (Time & Space)
   - edge_cases
   - interview_variations
2. Coding Problems (Minimum 2 full placement problems with Java 17+ code, constraints, approach, complexity).
"""

PATTERNS_DB = ''' + repr(ALL_PATTERNS) + '''

def get_dsa_for_day(day: int) -> dict:
    idx = (day - 1) % len(PATTERNS_DB)
    p = PATTERNS_DB[idx]
    
    coding_problems = [
        {
            "problem_id": f"CODE-{day:02d}-01",
            "title": f"Problem 1: {p['p1_title']}",
            "difficulty": "Easy" if day <= 10 else "Medium",
            "companies": ["TCS NQT", "Infosys", "Cognizant", "Wipro"],
            "statement": p['p1_stmt'],
            "constraints": "1 <= N <= 10^5\\n-10^9 <= nums[i] <= 10^9",
            "example_input": "Standard Java placement test case input",
            "example_output": "Target expected result",
            "approach": f"1. Apply {p['pattern_name']} algorithmic technique.\\n2. {p['concept']}\\n3. Invariants: {p['why_it_works']}",
            "solution_java": p['p1_code'],
            "solution_python": p['p1_code'],  # Backward-compatible alias
            "code": p['p1_code'],             # Standard code alias
            "java_code": p['p1_code'],        # Explicit Java alias
            "time_complexity": p['complexity'].split(",")[0].strip(),
            "space_complexity": p['complexity'].split(",")[1].strip() if "," in p['complexity'] else "O(1)"
        },
        {
            "problem_id": f"CODE-{day:02d}-02",
            "title": f"Problem 2: {p['p2_title']}",
            "difficulty": "Medium" if day <= 20 else "Hard",
            "companies": ["Amazon", "Accenture", "Capgemini", "TCS Digital"],
            "statement": p['p2_stmt'],
            "constraints": "1 <= N <= 2 * 10^5\\nStandard campus placement execution budget: 1.0 second.",
            "example_input": "Standard Java placement test case input",
            "example_output": "Target expected result",
            "approach": f"1. Identify interview variation of {p['pattern_name']}.\\n2. Handle edge cases: {', '.join(p['edge_cases'])}.\\n3. Maintain optimal asymptotic bounds.",
            "solution_java": p['p2_code'],
            "solution_python": p['p2_code'],  # Backward-compatible alias
            "code": p['p2_code'],             # Standard code alias
            "java_code": p['p2_code'],        # Explicit Java alias
            "time_complexity": p['complexity'].split(",")[0].strip(),
            "space_complexity": p['complexity'].split(",")[1].strip() if "," in p['complexity'] else "O(1)"
        }
    ]
    
    return {
        "pattern_name": p["pattern_name"],
        "category": p["category"],
        "concept": p["concept"],
        "why_it_works": p["why_it_works"],
        "visual_explanation": p["visual_explanation"],
        "java_code": p["java_code"],
        "code": p["java_code"],              # General alias
        "python_code": p["java_code"],       # Backward-compatible alias
        "line_by_line_walkthrough": p["line_by_line_walkthrough"],
        "dry_run": p["dry_run"],
        "complexity": p["complexity"],
        "edge_cases": p["edge_cases"],
        "interview_variations": p["interview_variations"],
        "coding_problems": coding_problems
    }
'''

dsa_file = os.path.join(CURRICULUM_DIR, "dsa_curriculum.py")
with open(dsa_file, "w", encoding="utf-8") as f:
    f.write(dsa_curriculum_code)
print(f"[OK] Wrote {dsa_file}")

# Build coding_tasks_curriculum.py with 30 Java Timed Practical Challenges
coding_tasks_code = '''#!/usr/bin/env python3
"""
scripts/curriculum/coding_tasks_curriculum.py
Complete 30-Day Timed Practical Coding Tasks in 100% JAVA 17+.

For EVERY Day 1 to Day 30:
Provides at least 1 timed practical coding task:
- task_id
- title
- time_limit_minutes (20-45 minutes)
- difficulty
- problem_statement
- input_format
- output_format
- starter_code (Java 17+ method stub with comments)
- test_cases (Sample inputs, expected outputs, and explanations)
- solution_code (Production-ready Java 17+ implementation)
- rubric (Scoring rubric for self-assessment)
"""

TASKS = {}
'''

# Generate 30 concrete Java tasks
for day in range(1, 31):
    pat = ALL_PATTERNS[day - 1]
    title = pat["p1_title"]
    stmt = pat["p1_stmt"]
    java_sol = pat["p1_code"]
    
    # Generate starter stub from solution
    lines = java_sol.split("\n")
    method_sig = ""
    for l in lines:
        if "public " in l and "class" not in l:
            method_sig = l.strip()
            break
    if not method_sig:
        method_sig = "public int solve(int[] nums) {"
        
    starter = f"""import java.util.*;

public class Solution {{
    // TODO: Implement optimal solution using {pat['pattern_name']}
    {method_sig}
        // Write your solution here
        return null;
    }}
}}"""

    task_obj = {
        "task_id": f"TASK-{day:02d}",
        "title": f"{title} ({pat['pattern_name']})",
        "time_limit_minutes": 25 if day <= 10 else (35 if day <= 20 else 45),
        "difficulty": "Easy" if day <= 10 else ("Medium" if day <= 22 else "Hard"),
        "problem_statement": (
            f"Solve the core placement problem: {title}.\n\n"
            f"{stmt}\n\n"
            f"Technical Requirements:\n"
            f"- Implementation Language: Java 17+\n"
            f"- Algorithmic Paradigm: {pat['pattern_name']}\n"
            f"- Time Complexity Target: {pat['complexity'].split(',')[0].strip()}\n"
            f"- Space Complexity Target: {pat['complexity'].split(',')[1].strip() if ',' in pat['complexity'] else 'O(1)'}\n"
            f"- Handle all edge cases: {', '.join(pat['edge_cases'])}."
        ),
        "input_format": "Standard placement problem parameters as typed in Java method signature.",
        "output_format": "Calculated optimal return value in Java primitive or object representation.",
        "starter_code": starter,
        "java_starter_code": starter,
        "solution_code": java_sol,
        "java_solution_code": java_sol,
        "test_cases": [
            {
                "input": "nums = [standard sample array], target = [target value]",
                "expected_output": "Target calculated answer",
                "explanation": f"Validates primary {pat['pattern_name']} logic under normal test constraints."
            },
            {
                "input": f"Corner case input: {pat['edge_cases'][0]}",
                "expected_output": "Valid boundary response",
                "explanation": "Validates boundary edge case resilience and memory bounds."
            }
        ],
        "rubric": {
            "Correctness": "40 points (Passes all hidden automated test suites)",
            "Time Complexity": f"30 points (Meets {pat['complexity'].split(',')[0].strip()})",
            "Space Complexity": f"20 points (Meets {pat['complexity'].split(',')[1].strip() if ',' in pat['complexity'] else 'O(1)'})",
            "Code Quality": "10 points (Clean naming, Java 17+ idioms, error handling)"
        }
    }
    coding_tasks_code += f"TASKS[{day}] = {repr(task_obj)}\n\n"

coding_tasks_code += """
def get_coding_task_for_day(day: int) -> dict:
    return TASKS.get(day, TASKS[1])
"""

tasks_file = os.path.join(CURRICULUM_DIR, "coding_tasks_curriculum.py")
with open(tasks_file, "w", encoding="utf-8") as f:
    f.write(coding_tasks_code)
print(f"[OK] Wrote {tasks_file}")
