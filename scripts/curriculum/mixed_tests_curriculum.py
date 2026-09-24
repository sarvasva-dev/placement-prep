#!/usr/bin/env python3
"""
scripts/curriculum/mixed_tests_curriculum.py
Complete 30-Day Mixed Daily MCQ Test Curriculum.

For EVERY Day 1 to Day 30:
Provides exactly 20 unique mixed MCQs from authentic, topic-grounded banks:
- 5 Academic MCQs (BCA 5001, 5002, 5003, 5004)
- 5 Aptitude MCQs (Quantitative, Logical, Verbal)
- 5 Core CS MCQs (OS, DBMS, Networks, Python, System Design)
- 5 Coding & Project MCQs (Java DSA Patterns, CSMS, SmartGalla, BulkBeat TV, DocRoute, Django)

Total = 20 interactive questions per day with options, correct_answer, and explanation.
Zero template placeholders.
"""

import os
import sys

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
if CURR_DIR not in sys.path:
    sys.path.insert(0, CURR_DIR)

try:
    from banks.mixed_bank_1_15 import get_mixed_mcqs_half1
    from banks.mixed_bank_16_30 import get_mixed_mcqs_half2
except ImportError:
    try:
        from .banks.mixed_bank_1_15 import get_mixed_mcqs_half1
        from .banks.mixed_bank_16_30 import get_mixed_mcqs_half2
    except ImportError:
        import mixed_bank_1_15
        import mixed_bank_16_30
        get_mixed_mcqs_half1 = mixed_bank_1_15.get_mixed_mcqs_half1
        get_mixed_mcqs_half2 = mixed_bank_16_30.get_mixed_mcqs_half2


def get_mixed_test_for_day(day: int) -> list:
    """Retrieve 20 authentic, non-template mixed MCQs for the specified day."""
    if day <= 15:
        return get_mixed_mcqs_half1(day)
    else:
        return get_mixed_mcqs_half2(day)
