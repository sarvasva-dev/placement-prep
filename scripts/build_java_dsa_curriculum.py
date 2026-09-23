#!/usr/bin/env python3
"""
scripts/build_java_dsa_curriculum.py
Builds:
1. scripts/curriculum/dsa_curriculum.py (30 Java 17+ DSA Patterns & 60 Java Coding Problems)
2. scripts/curriculum/coding_tasks_curriculum.py (30 Java 17+ Practical Timed Coding Tasks)
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM_DIR = os.path.join(BASE_DIR, "scripts", "curriculum")

# 30 Comprehensive DSA Patterns in Java 17+
PATTERNS = [
    # Day 1
    {
        "name": "Two Pointers (Opposite Direction)",
        "category": "Two Pointers",
        "concept": "Two pointers start at opposite ends of a sorted array (left = 0, right = n - 1) and converge toward each other based on comparison against a target.",
        "why": "Exploits the monotonic ordering of sorted elements to eliminate half of unexamined candidates at each step in O(1) time without nested loops.",
        "visual": (
            "Sorted Array: [ 2, 7, 11, 15 ], Target = 9\n"
            "Step 1: Left -> [2]               [15] <- Right   Sum = 17 > 9  ==> Right--\n"
            "Step 2: Left -> [2]         [11] <- Right         Sum = 13 > 9  ==> Right--\n"
            "Step 3: Left -> [2]   [7] <- Right               Sum = 9  == 9 ==> Found indices [0, 1]!"
        ),
        "code": (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public int[] twoSumSorted(int[] numbers, int target) {\n"
            "        int left = 0;\n"
            "        int right = numbers.length - 1;\n"
            "        \n"
            "        while (left < right) {\n"
            "            int sum = numbers[left] + numbers[right];\n"
            "            if (sum == target) {\n"
            "                return new int[]{left, right};\n"
            "            } else if (sum < target) {\n"
            "                left++;\n"
            "            } else {\n"
            "                right--;\n"
            "            }\n"
            "        }\n"
            "        return new int[]{};\n"
            "    }\n"
            "}"
        ),
        "walkthrough": [
            "Line 4-5: Initialize left pointer at index 0 and right pointer at numbers.length - 1.",
            "Line 7: Loop condition (left < right) guarantees distinct element pairing without pointer crossing.",
            "Line 8: Calculate current sum of elements at both pointers.",
            "Line 9-10: If sum equals target, return 0-based indices array immediately.",
            "Line 11-12: If sum is smaller than target, increment left pointer to increase total sum.",
            "Line 13-14: If sum is greater than target, decrement right pointer to decrease total sum.",
            "Line 17: Return empty array if no matching pair exists."
        ],
        "dry_run": "Input: numbers = [2, 7, 11, 15], target = 9. Iteration 1: left=0(2), right=3(15), sum=17 > 9 -> right=2. Iteration 2: left=0(2), right=2(11), sum=13 > 9 -> right=1. Iteration 3: left=0(2), right=1(7), sum=9 == target -> returns [0, 1].",
        "complexity": "O(N) Time, O(1) Auxiliary Space",
        "edge_cases": ["Array of length 2", "Negative numbers in sorted order", "Duplicates summing to target", "No valid pair"],
        "variations": ["Container With Most Water", "3Sum (fix 1 element, 2-pointer scan remainder)", "Trapping Rain Water", "Valid Palindrome II"],
        "prob1_title": "Two Sum II — Input Array Is Sorted",
        "prob1_stmt": "Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the 1-based indices [index1, index2].",
        "prob1_code": (
            "public class Solution {\n"
            "    public int[] twoSum(int[] numbers, int target) {\n"
            "        int left = 0, right = numbers.length - 1;\n"
            "        while (left < right) {\n"
            "            int sum = numbers[left] + numbers[right];\n"
            "            if (sum == target) return new int[]{left + 1, right + 1};\n"
            "            if (sum < target) left++;\n"
            "            else right--;\n"
            "        }\n"
            "        return new int[]{-1, -1};\n"
            "    }\n"
            "}"
        ),
        "prob2_title": "Container With Most Water",
        "prob2_stmt": "You are given an integer array height of length n. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.",
        "prob2_code": (
            "public class Solution {\n"
            "    public int maxArea(int[] height) {\n"
            "        int left = 0, right = height.length - 1;\n"
            "        int maxWater = 0;\n"
            "        while (left < right) {\n"
            "            int width = right - left;\n"
            "            int h = Math.min(height[left], height[right]);\n"
            "            maxWater = Math.max(maxWater, width * h);\n"
            "            if (height[left] < height[right]) left++;\n"
            "            else right--;\n"
            "        }\n"
            "        return maxWater;\n"
            "    }\n"
            "}"
        )
    },
    # Day 2
    {
        "name": "Sliding Window (Fixed Size)",
        "category": "Sliding Window",
        "concept": "Maintains a contiguous subarray window of fixed length K. Slides the window one step at a time by adding the incoming element at the right and evicting the outgoing element at the left.",
        "why": "Reuses the computational state of overlapping elements across adjacent windows in O(1) time instead of recomputing from scratch in O(K).",
        "visual": (
            "Array: [ 2, 1, 5, 1, 3, 2 ], K = 3\n"
            "Window 0: [ (2, 1, 5), 1, 3, 2 ]  Sum = 8\n"
            "Window 1: [ 2, (1, 5, 1), 3, 2 ]  Sum = 8 - 2 + 1 = 7\n"
            "Window 2: [ 2, 1, (5, 1, 3), 2 ]  Sum = 7 - 1 + 3 = 9 (Max)\n"
            "Window 3: [ 2, 1, 5, (1, 3, 2) ]  Sum = 9 - 5 + 2 = 6"
        ),
        "code": (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public int maxSumSubarray(int[] nums, int k) {\n"
            "        if (nums == null || nums.length < k) return 0;\n"
            "        int windowSum = 0;\n"
            "        for (int i = 0; i < k; i++) {\n"
            "            windowSum += nums[i];\n"
            "        }\n"
            "        int maxSum = windowSum;\n"
            "        for (int i = k; i < nums.length; i++) {\n"
            "            windowSum += nums[i] - nums[i - k];\n"
            "            maxSum = Math.max(maxSum, windowSum);\n"
            "        }\n"
            "        return maxSum;\n"
            "    }\n"
            "}"
        ),
        "walkthrough": [
            "Line 4: Guard clause checking for null or array length smaller than window size k.",
            "Line 5-8: Compute baseline sum for the initial window of first k elements.",
            "Line 9: Initialize maxSum with the sum of the first window.",
            "Line 10: Iterate from index k to the end of the array.",
            "Line 11: Add incoming element nums[i] and subtract evicted element nums[i - k] in O(1).",
            "Line 12: Update maxSum with the highest window sum encountered.",
            "Line 14: Return optimal maxSum."
        ],
        "dry_run": "nums = [2, 1, 5, 1, 3, 2], k = 3. Initial window [2, 1, 5] sum=8. i=3: add 1, sub 2 -> sum=7 (max=8). i=4: add 3, sub 1 -> sum=9 (max=9). i=5: add 2, sub 5 -> sum=6 (max=9). Returns 9.",
        "complexity": "O(N) Time, O(1) Auxiliary Space",
        "edge_cases": ["k == nums.length", "Negative numbers in array", "k == 1", "All elements equal"],
        "variations": ["Maximum Average Subarray I", "Find All Anagrams in a String", "Substrings of Size Three with Distinct Characters", "Permutation in String"],
        "prob1_title": "Maximum Average Subarray I",
        "prob1_stmt": "You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.",
        "prob1_code": (
            "public class Solution {\n"
            "    public double findMaxAverage(int[] nums, int k) {\n"
            "        double sum = 0;\n"
            "        for (int i = 0; i < k; i++) sum += nums[i];\n"
            "        double maxSum = sum;\n"
            "        for (int i = k; i < nums.length; i++) {\n"
            "            sum += nums[i] - nums[i - k];\n"
            "            maxSum = Math.max(maxSum, sum);\n"
            "        }\n"
            "        return maxSum / k;\n"
            "    }\n"
            "}"
        ),
        "prob2_title": "Find All Anagrams in a String",
        "prob2_stmt": "Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.",
        "prob2_code": (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public List<Integer> findAnagrams(String s, String p) {\n"
            "        List<Integer> res = new ArrayList<>();\n"
            "        if (s.length() < p.length()) return res;\n"
            "        int[] pCount = new int[26];\n"
            "        int[] sCount = new int[26];\n"
            "        for (int i = 0; i < p.length(); i++) {\n"
            "            pCount[p.charAt(i) - 'a']++;\n"
            "            sCount[s.charAt(i) - 'a']++;\n"
            "        }\n"
            "        if (Arrays.equals(pCount, sCount)) res.add(0);\n"
            "        for (int i = p.length(); i < s.length(); i++) {\n"
            "            sCount[s.charAt(i) - 'a']++;\n"
            "            sCount[s.charAt(i - p.length()) - 'a']--;\n"
            "            if (Arrays.equals(pCount, sCount)) res.add(i - p.length() + 1);\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}"
        )
    },
    # Day 3
    {
        "name": "Sliding Window (Dynamic / Variable Size)",
        "category": "Sliding Window",
        "concept": "Expands window by moving right pointer until a condition is met; then contracts window from left to find the minimal or maximal valid subarray.",
        "why": "Both pointers move monotonically forward from 0 to N - 1. Each element enters and leaves the window at most once, guaranteeing strict O(N) runtime.",
        "visual": (
            "Target = 7, Array: [ 2, 3, 1, 2, 4, 3 ]\n"
            "Right expands: [2, 3, 1, 2] -> Sum = 8 >= 7 (Len 4)\n"
            "Left contracts: [3, 1, 2] -> Sum = 6 < 7\n"
            "Right expands: [3, 1, 2, 4] -> Sum = 10 >= 7\n"
            "Left contracts: [1, 2, 4] -> Sum = 7 >= 7 (Len 3)\n"
            "Left contracts: [2, 4] -> Sum = 6 < 7\n"
            "Right expands: [2, 4, 3] -> Sum = 9 >= 7\n"
            "Left contracts: [4, 3] -> Sum = 7 >= 7 (Len 2 -- Min Length!)"
        ),
        "code": (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public int minSubArrayLen(int target, int[] nums) {\n"
            "        int left = 0;\n"
            "        int currentSum = 0;\n"
            "        int minLen = Integer.MAX_VALUE;\n"
            "        \n"
            "        for (int right = 0; right < nums.length; right++) {\n"
            "            currentSum += nums[right];\n"
            "            while (currentSum >= target) {\n"
            "                minLen = Math.min(minLen, right - left + 1);\n"
            "                currentSum -= nums[left];\n"
            "                left++;\n"
            "            }\n"
            "        }\n"
            "        return minLen == Integer.MAX_VALUE ? 0 : minLen;\n"
            "    }\n"
            "}"
        ),
        "walkthrough": [
            "Line 4-6: Initialize left pointer, cumulative sum, and minLen to infinity.",
            "Line 8: Iterate right pointer across the entire array, absorbing nums[right].",
            "Line 10-14: While condition is satisfied (currentSum >= target), capture window length (right - left + 1) and contract left pointer.",
            "Line 16: Return 0 if no valid subarray found, otherwise return minLen."
        ],
        "dry_run": "target = 7, nums = [2, 3, 1, 2, 4, 3]. Right reaches 3 (sum=8>=7) -> minLen=4, shrink left to 1. Right reaches 4 (sum=10) -> shrink left to 2 -> window [1, 2, 4] len 3. Right reaches 5 (sum=9) -> shrink left to 4 -> window [4, 3] len 2. Returns 2.",
        "complexity": "O(N) Time, O(1) Auxiliary Space",
        "edge_cases": ["Sum of all elements < target", "Single element == target", "All elements equal"],
        "variations": ["Longest Substring Without Repeating Characters", "Minimum Window Substring", "Longest Repeating Character Replacement", "Max Consecutive Ones III"],
        "prob1_title": "Minimum Size Subarray Sum",
        "prob1_stmt": "Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0.",
        "prob1_code": (
            "public class Solution {\n"
            "    public int minSubArrayLen(int target, int[] nums) {\n"
            "        int left = 0, sum = 0, minLen = Integer.MAX_VALUE;\n"
            "        for (int right = 0; right < nums.length; right++) {\n"
            "            sum += nums[right];\n"
            "            while (sum >= target) {\n"
            "                minLen = Math.min(minLen, right - left + 1);\n"
            "                sum -= nums[left++];\n"
            "            }\n"
            "        }\n"
            "        return minLen == Integer.MAX_VALUE ? 0 : minLen;\n"
            "    }\n"
            "}"
        ),
        "prob2_title": "Longest Substring Without Repeating Characters",
        "prob2_stmt": "Given a string s, find the length of the longest substring without repeating characters.",
        "prob2_code": (
            "import java.util.*;\n\n"
            "public class Solution {\n"
            "    public int lengthOfLongestSubstring(String s) {\n"
            "        int[] lastIndex = new int[128];\n"
            "        Arrays.fill(lastIndex, -1);\n"
            "        int maxLen = 0, left = 0;\n"
            "        for (int right = 0; right < s.length(); right++) {\n"
            "            char c = s.charAt(right);\n"
            "            if (lastIndex[c] >= left) {\n"
            "                left = lastIndex[c] + 1;\n"
            "            }\n"
            "            lastIndex[c] = right;\n"
            "            maxLen = Math.max(maxLen, right - left + 1);\n"
            "        }\n"
            "        return maxLen;\n"
            "    }\n"
            "}"
        )
    }
]

print("Building remaining DSA patterns 4 to 30...")
