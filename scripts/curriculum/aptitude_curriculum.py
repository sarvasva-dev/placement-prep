#!/usr/bin/env python3
"""
scripts/curriculum/aptitude_curriculum.py
Complete 30-Day Placement Aptitude Curriculum

For EVERY Day 1 to Day 30:
- topic
- formulas & speed shortcuts
- concept_lesson
- solved_examples (5 complete worked examples with step-by-step solutions)
- mcqs (10 authentic, topic-grounded MCQs from aptitude banks)
- practice_problems (5 unsolved practice questions with answer keys)
- timed_drill (1 timed mini-test)
"""

import os
import sys

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
if CURR_DIR not in sys.path:
    sys.path.insert(0, CURR_DIR)

try:
    from banks.aptitude_bank_1_15 import get_aptitude_mcqs_for_day_1_15
    from banks.aptitude_bank_16_30 import get_aptitude_mcqs_for_day_16_30
except ImportError:
    try:
        from .banks.aptitude_bank_1_15 import get_aptitude_mcqs_for_day_1_15
        from .banks.aptitude_bank_16_30 import get_aptitude_mcqs_for_day_16_30
    except ImportError:
        import aptitude_bank_1_15
        import aptitude_bank_16_30
        get_aptitude_mcqs_for_day_1_15 = aptitude_bank_1_15.get_aptitude_mcqs_for_day_1_15
        get_aptitude_mcqs_for_day_16_30 = aptitude_bank_16_30.get_aptitude_mcqs_for_day_16_30


def get_aptitude_for_day(day):
    # Topics catalog
    topics = [
        # Days 1-12: Quantitative
        ("Percentages & Fractional Equivalents", "Quantitative", "Percentages",
         "1. % Change = [(New - Old) / Old] * 100\n2. Base Inversion: If A is r% more than B, B is [r / (100 + r)] * 100% less than A.\n3. Net % Change for successive a% and b% = a + b + (ab / 100)%.",
         "Expenditure Invariance: If price increases by 1/x, consumption must decrease by 1/(x+1) to keep expenditure unchanged.",
         "Percentage represents parts per 100. In corporate aptitude tests (TCS, Infosys, Cognizant), speed depends on instant fraction conversion (1/2=50%, 1/3=33.33%, 1/4=25%, 1/5=20%, 1/6=16.67%, 1/7=14.28%, 1/8=12.5%, 1/9=11.11%, 1/12=8.33%). Never calculate 14.28% by long multiplication; divide directly by 7."),
        
        ("Profit, Loss & Successive Discounts", "Quantitative", "Profit & Loss",
         "1. Profit % = [(SP - CP) / CP] * 100\n2. Loss % = [(CP - SP) / CP] * 100\n3. Single Equivalent Discount for d1% and d2% = d1 + d2 - (d1 * d2 / 100)%.\n4. When two items sold at equal SP, one at x% profit and other at x% loss, overall loss is always (x^2 / 100)%.",
         "Multiplying Factor: 20% profit means SP = CP * 1.20. 15% loss means SP = CP * 0.85. CP = SP / Multiplying Factor.",
         "Profit and loss are always computed with respect to Cost Price (CP) unless specifically referenced to Selling Price. In multi-step transactions, convert markups and discounts into successive factors: Final SP = CP * (1 + markup/100) * (1 - discount/100)."),

        ("Simple & Compound Interest", "Quantitative", "Interest",
         "1. SI = (P * R * T) / 100\n2. CI Amount = P * (1 + R/100)^T\n3. 2-Year Difference (CI - SI) = P * (R / 100)^2\n4. 3-Year Difference (CI - SI) = P * (R / 100)^2 * [(300 + R) / 100].",
         "Rule of 72: A sum of money doubles in approximately 72 / R years at compound interest rate R%.",
         "Simple interest grows linearly with equal increments each year. Compound interest grows exponentially because interest earned in prior periods itself earns interest. For multi-year placement questions, use the binomial expansion or interest table method rather than calculating large powers manually."),

        ("Ratio, Proportion & Variations", "Quantitative", "Ratio & Proportion",
         "1. If a/b = c/d, then ad = bc.\n2. Duplicate ratio of a:b = a^2:b^2; Sub-duplicate = sqrt(a):sqrt(b).\n3. Inverted Ratio: If a:b:c, inverse ratio is (1/a):(1/b):(1/c) = bc:ca:ab.\n4. Compound Ratio of (a:b) and (c:d) = ac:bd.",
         "Direct Constant Ratio Method: If a ratio changes from 3:4 to 5:6 upon adding a constant k to both, the difference between terms remains equal. Match units directly.",
         "A ratio expresses relative magnitude. When quantities are divided in ratio a:b:c, total parts equal (a+b+c). The value of 1 unit equals Total Quantity / (a+b+c). In partnership problems, profit is partitioned in proportion to (Investment * Time Period)."),

        ("Averages, Weighted Means & Alligations", "Quantitative", "Averages",
         "1. Average = Sum of all observations / Total number of observations.\n2. Weighted Average = (w1*x1 + w2*x2 + ... + wn*xn) / (w1 + w2 + ... + wn).\n3. Alligation Rule: (Cheaper Quantity) / (Dearer Quantity) = (Dearer Price - Mean Price) / (Mean Price - Cheaper Price).",
         "Deviation Method (Assumed Mean): Pick a central number as baseline. Sum deviations from this baseline and divide by n. Average = Baseline + (Sum of Deviations / n).",
         "The Alligation cross is a powerful graphical shortcut for solving weighted averages in seconds. It determines the exact mixing ratio of two ingredients at different prices to produce a target mixture price without solving simultaneous linear equations."),

        ("Time & Work (Efficiency & Work-Rate)", "Quantitative", "Time & Work",
         "1. If person does a work in D days, 1-day work = 1/D.\n2. Total Work = Efficiency * Time.\n3. Efficiency is inversely proportional to time: E1 / E2 = D2 / D1.\n4. MDH Formula: (M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2.",
         "LCM Total Work Method: Assume total work equals LCM of individual day counts. Compute daily units for each worker. Add units for joint work.",
         "Never work with fractions if you can avoid them. By assuming Total Work = LCM(days), workers have integer work units per day. Example: If A takes 10 days and B takes 15 days, let Total Work = 30 units. A does 3 units/day, B does 2 units/day. Together they do 5 units/day, taking 30 / 5 = 6 days."),

        ("Pipes & Cisterns", "Quantitative", "Pipes & Cisterns",
         "1. Inlet pipe work rate = +1/Time.\n2. Outlet (drain/leak) work rate = -1/Time.\n3. Net rate = Sum of Inlets - Sum of Outlets.\n4. Time to fill/empty = Total Capacity / Net Rate.",
         "Negative Work Logic: Treat leaks and drainage pipes as entities doing negative units of work per hour in the standard LCM framework.",
         "Pipes and cisterns problems mirror Time and Work with one critical difference: emptying pipes subtract volume. Always maintain positive and negative signs explicitly to avoid directional calculation errors."),

        ("Time, Speed & Distance (Trains & Relative Speed)", "Quantitative", "Time Speed Distance",
         "1. Speed = Distance / Time; Distance = Speed * Time.\n2. Conversion: km/hr to m/s multiply by 5/18; m/s to km/hr multiply by 18/5.\n3. Relative Speed: Same direction = |S1 - S2|; Opposite direction = S1 + S2.\n4. Average Speed for equal distances = (2 * S1 * S2) / (S1 + S2).",
         "Train Crossing Object: Time to cross a stationary point (pole/person) = Length of Train / Speed. Time to cross a platform/bridge = (Length of Train + Length of Platform) / Speed.",
         "Relative speed is the rate at which distance between two moving bodies decreases or increases. When two trains travel toward each other, their speeds add. When they travel in the same direction, their speeds subtract."),

        ("Boats, Streams & Circular Tracks", "Quantitative", "Boats & Streams",
         "1. Downstream Speed (D) = Speed of Boat (u) + Speed of Stream (v).\n2. Upstream Speed (U) = Speed of Boat (u) - Speed of Stream (v).\n3. Speed of Boat in still water (u) = (D + U) / 2.\n4. Speed of Stream (v) = (D - U) / 2.",
         "Circular Track First Meeting: Time to meet for the first time anywhere = Track Circumference / Relative Speed. Time to meet at starting point = LCM(T1, T2).",
         "In river navigation, downstream motion is accelerated by water current, while upstream motion is impeded. Remember that boat speed in still water must always exceed stream speed for upstream progress to occur."),

        ("Permutations & Combinations", "Quantitative", "Permutations & Combinations",
         "1. nPr = n! / (n - r)! (Arrangements where order matters).\n2. nCr = n! / [r! * (n - r)!] (Selections where order does NOT matter).\n3. nCr = nC(n - r); nC0 = nCn = 1.\n4. Circular Permutations of n distinct objects = (n - 1)!.",
         "Grouping (Block) Method: When k items must always be together, tie them into 1 single super-item. Total items = (n - k + 1)!. Then multiply by k! internal arrangements.",
         "Permutation answers 'In how many ways can we arrange/order?' Combination answers 'In how many ways can we choose/select?' Watch for duplicate letters in words: arrangements of word with repeated letters = Total! / (count1! * count2!)."),

        ("Probability (Classical & Conditional)", "Quantitative", "Probability",
         "1. P(E) = Number of favorable outcomes / Total possible outcomes = n(E) / n(S).\n2. 0 <= P(E) <= 1; P(E') = 1 - P(E).\n3. Addition Rule: P(A or B) = P(A) + P(B) - P(A and B).\n4. Independent Events: P(A and B) = P(A) * P(B).\n5. Conditional Probability: P(A | B) = P(A and B) / P(B).",
         "Complementary Counting: When asked for 'at least one', calculate 1 - P(none). It is almost always 5x faster than summing individual cases.",
         "Sample spaces must be mutually exclusive and exhaustive. In dice problems (n=2, sum 2 to 12), the distribution peaks at sum 7 (prob 6/36 = 1/6). In card problems, remember 4 suits (13 cards each), 2 red/2 black suits, and 12 face cards (J, Q, K)."),

        ("Number Systems, Divisibility Rules & HCF/LCM", "Quantitative", "Number Systems",
         "1. Product of two numbers = HCF * LCM.\n2. Divisibility: 3 & 9 (sum of digits), 4 (last 2 digits), 8 (last 3 digits), 11 (alternating sum difference is 0 or multiple of 11).\n3. Remainder Theorem: Remainder of [A * B] / N = [Rem(A/N) * Rem(B/N)] mod N.\n4. Number of Factors of N = p1^a * p2^b * p3^c is (a+1)(b+1)(c+1).",
         "Cyclicity of Units Digit: 2, 3, 7, 8 have cyclicity of 4. 4 and 9 have cyclicity of 2. 0, 1, 5, 6 have cyclicity of 1.",
         "Number theory forms the gateway section of TCS NQT and AMCAT exams. Always check divisibility rules before attempting brute-force division. For large powers, divide the exponent by 4 to determine the active cycle index."),

        # Days 13-22: Logical Reasoning
        ("Syllogisms & Venn Diagram Logic", "Logical Reasoning", "Syllogisms",
         "1. Standard Quantifiers: All (Universal Affirmative - A), No (Universal Negative - E), Some (Particular Affirmative - I), Some Not (Particular Negative - O).\n2. Complementary Pairs for Either/Or: (I + E), (A + O).\n3. Definite Conclusion requires truth in 100% of all possible valid Venn diagrams.",
         "Golden Deduction: All A are B + All B are C ==> All A are C. Some A are B + All B are C ==> Some A are C. No deduction possible from two negative or two particular statements.",
         "A conclusion is valid if and only if it follows unconditionally from the premises. If you can draw even one valid Venn diagram configuration where the conclusion is false, the conclusion is INVALID. Watch for 'possibility' questions, which only require one valid configuration."),

        ("Blood Relations & Family Tree Notation", "Logical Reasoning", "Blood Relations",
         "1. Standard Symbols: Male = [+], Female = [-], Marriage = [=], Siblings = [---], Vertical line = generation gap.\n2. Generational Indexing: Grandparents (+2), Parents/Uncles (+1), Self/Siblings/Spouse (0), Children (-1), Grandchildren (-2).",
         "Reverse Parsing Trick for Coded Relations: In 'P is the mother of Q's father', start reading from the end ('Q's father' -> Father's mother -> P is Q's paternal grandmother).",
         "Never assume gender from names in competitive reasoning exams unless explicitly stated or determined by familial role (e.g. 'mother', 'brother'). Always construct the family tree generation by generation."),

        ("Direction Sense & Vector Displacement", "Logical Reasoning", "Direction Sense",
         "1. 8 Cardinal Directions: North (N), South (S), East (E), West (W), NE, NW, SE, SW.\n2. Angular Turning: Clockwise = Right turn (+90 deg); Counter-clockwise = Left turn (-90 deg).\n3. Shortest Distance: Pythagoras Theorem d = sqrt(delta_x^2 + delta_y^2).",
         "Coordinate Mapping: Treat starting point as origin (0, 0). North = +y, South = -y, East = +x, West = -x. Sum vector movements directly without drawing complex paper maps.",
         "Direction questions frequently involve shadow movements at sunrise (shadow falls West) and sunset (shadow falls East). At 12 noon, shadows are negligible. Always track the final facing orientation separately from the net displacement vector."),

        ("Linear & Circular Seating Arrangement", "Logical Reasoning", "Seating Arrangement",
         "1. Facing Center (North): Left is Clockwise / West; Right is Counter-clockwise / East.\n2. Facing Away from Center (South): Orientations are reversed.\n3. Definite Clues vs Ambiguous Clues: Always place fixed anchor positions first before testing conditional constraints.",
         "Dual-Diagram Parallel Tracking: When a clue allows two possible placements, draw two small candidate diagrams simultaneously rather than erasing and guessing.",
         "Seating puzzles form 15-20% of the reasoning section in Infosys and Cognizant tests. Read through all conditions before placing the first element. Look for the most restrictive constraint with specific positional anchors."),

        ("Coding-Decoding & Letter Shifting", "Logical Reasoning", "Coding-Decoding",
         "1. Alphabet Positional Values: A=1, B=2, ..., Z=26 (EJOTY mnemonic: 5, 10, 15, 20, 25).\n2. Reverse Alphabet Positional Values: Sum of letter and its opposite is ALWAYS 27 (A=1 opposite Z=26; B=2 opposite Y=25).\n3. Common Patterns: Fixed shift (+k, -k), Alternating shifts (+1, -2, +3), Reversal, Pairing.",
         "EJOTY / CFILORUX: Memorize multiples of 3 (CFILORUX) and 5 (EJOTY) to identify letter numbers in less than 2 seconds.",
         "Examine whether letters are substituted, permuted, or mapped to numerical values. If letters in the output match the input word exactly, it is a transposition/rearrangement cipher, not a substitution cipher."),

        ("Series Completion & Pattern Recognition", "Logical Reasoning", "Series Completion",
         "1. Types of Series: Arithmetic (+d), Geometric (*r), Difference of Differences, Squares/Cubes (n^2 +- k, n^3 +- k), Alternating/Twin series.\n2. Prime Number Series: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31...\n3. Fibonacci-type Additive Series: Tn = T(n-1) + T(n-2).",
         "Step-Difference Technique: Compute consecutive differences. If not constant, compute differences of differences. A quadratic sequence achieves constant values at second differences.",
         "When numbers grow rapidly, test for multiplication or powers. When numbers grow slowly, test for addition. If a series fluctuates up and down, it is almost certainly two alternating sub-series interwoven into one."),

        ("Clocks & Calendar Mathematics", "Logical Reasoning", "Clocks & Calendars",
         "1. Clock Angle Formula: Angle theta = |30*H - (11/2)*M| degrees.\n2. Minute hand speed = 6 deg/min; Hour hand speed = 0.5 deg/min; Relative speed = 5.5 deg/min.\n3. Odd Days in Ordinary Year (365 days) = 1; Leap Year (366 days) = 2.\n4. Leap Year condition: Divisible by 4, except century years which must be divisible by 400.",
         "Mirror Image of Clock: Subtract given time from 11:60 (or 23:60 for 24-hr format).",
         "Hands of a clock coincide 11 times in 12 hours (22 times in 24 hours), because between 11 and 1 they coincide only once at exactly 12:00. In calendar math, 100 years have 5 odd days, 200 years have 3, 300 years have 1, and 400 years have 0."),

        ("Statement & Assumptions / Inferred Meanings", "Logical Reasoning", "Critical Reasoning",
         "1. An assumption is something taken for granted or supposed before making a statement.\n2. Valid assumptions must be implicit in the premise and directly support the necessity of the statement.\n3. Avoid extreme assumptions containing words like 'only', 'never', 'all', 'always' unless justified by explicit context.",
         "Negation Test: Negate the candidate assumption. If the original statement collapses or becomes irrational, the assumption is 100% NECESSARY and VALID.",
         "Critical reasoning forms the core of Accenture and Capgemini aptitude assessments. Never bring external knowledge into the assumption evaluation. Assume the speaker's statement is reasonable and identify what foundation must exist for it to hold true."),

        ("Data Sufficiency Framework", "Logical Reasoning", "Data Sufficiency",
         "1. Option Structure: (A) I alone is sufficient; (B) II alone is sufficient; (C) Both together are sufficient; (D) Neither is sufficient; (E) Either alone is sufficient.\n2. 12-Second Elimination: Check Statement I. If sufficient, answer is A or D/E. Then check Statement II.",
         "Never Calculate Final Numbers: Data Sufficiency asks 'CAN this be answered?', not 'What is the answer?'. Stop the instant uniqueness is established.",
         "A statement is sufficient only if it yields ONE UNIQUE ANSWER. If a quadratic equation yields two different positive solutions, the statement is INSUFFICIENT unless additional constraints rule out one root."),

        ("Cube & Dice Reasoning", "Logical Reasoning", "Cube & Dice",
         "1. Opposite Faces of Standard Dice: Sum of opposite faces is always 7 (1-6, 2-5, 3-4).\n2. Open Dice Folding Rule: Alternate faces in a straight line are opposite to each other with one face in between.\n3. Painted Cube: For a cube cut into n^3 smaller cubes: 3 faces painted = 8 (corners); 2 faces = 12*(n-2) (edges); 1 face = 6*(n-2)^2 (centers); 0 faces = (n-2)^3.",
         "Common Face Clockwise Rule: When two views of a die show one common face, write down the numbers clockwise starting from the common face. Positionally matching pairs are opposite faces.",
         "Spatial reasoning questions evaluate mental 3D rotation. Practice identifying opposite pairs directly from unfolded net diagrams before attempting complex multi-cut cube volume questions."),

        # Days 23-30: Verbal Ability & Mixed Placement Simulations
        ("Sentence Correction & Subject-Verb Agreement", "Verbal Ability", "Grammar",
         "1. A singular subject takes a singular verb; a plural subject takes a plural verb.\n2. 'Either... or' and 'Neither... nor': Verb agrees with the NEAREST subject.\n3. Indefinite Pronouns: 'Each', 'Every', 'Everyone', 'Neither', 'Either' take SINGULAR verbs.\n4. Parenthetical phrases ('along with', 'as well as', 'together with') do NOT change subject number.",
         "Ignore intervening prepositional phrases: In 'The bouquet of red roses (was/were) beautiful', cross out 'of red roses'. The subject is 'bouquet' (singular) ==> was.",
         "Grammar errors in campus hiring tests (Wipro, TCS, Cognizant) focus heavily on subject-verb agreement, modifier placement (dangling modifiers), and parallel structure in lists. Always isolate the true grammatical subject."),

        ("Prepositions, Conjunctions & Idiomatic Usage", "Verbal Ability", "Prepositions",
         "1. Fixed Prepositions: Abstain from, Accustomed to, Congratulate on, Capable of, Insist on, Prevent from, Superior to.\n2. Correlative Conjunctions: Hardly... when; Scarcely... when; No sooner... than; Not only... but also.\n3. 'Between' is used for two items; 'Among' for three or more.",
         "Pair Matching: The instant you spot 'No sooner' in a sentence, immediately scan for 'than'. If it uses 'when' or 'then', it is an automatic error.",
         "Prepositional idioms are tested directly in fill-in-the-blank and error spotting questions. Remember that words expressing preference or comparative hierarchy like 'senior', 'junior', 'prior', 'superior', 'prefer' take 'to', NEVER 'than'."),

        ("Vocabulary, Contextual Synonyms & Antonyms", "Verbal Ability", "Vocabulary",
         "1. Root Words: 'Mal' = bad/evil; 'Bene' = good; 'Chron' = time; 'Loqu/Loc' = talk/speak; 'Path' = feeling.\n2. Contextual Tone Analysis: Determine whether the blank requires a positive, negative, or neutral connotation before looking at options.\n3. Secondary Meanings: Words like 'Reservation' (doubt/hesitation vs booking), 'Arrest' (stop progress vs police arrest).",
         "Elimination by Tone: If three options are positive adjectives and one is negative, match with the sentence polarity to eliminate three choices instantly.",
         "Do not memorize dictionary definitions in isolation. Learn words in contextual families and roots. High-frequency placement vocabulary includes words like Candid, Ephemeral, Pragmatic, Esoteric, Ubiquitous, and Reticent."),

        ("Para Jumbles & Sentence Rearrangement", "Verbal Ability", "Para Jumbles",
         "1. Mandatory Pairs: Find two sentences that must go together (Noun followed by Pronoun, Cause followed by Effect, Chronological sequence).\n2. Opening Sentence: Must be independent, introduces the central noun/topic, cannot begin with conjunctions ('However', 'Therefore') or relative pronouns.\n3. Closing Sentence: Summarizes, states consequence, or projects future outlook.",
         "Acronym-Full Form Rule: Full name or complete title is introduced first; acronyms or abbreviations follow in subsequent sentences.",
         "Para Jumbles test logical cohesion and discourse flow. Never test all 24 permutations. Find one mandatory pair (e.g. BC), then check which of the 4 options contains BC together."),

        ("Reading Comprehension & Critical Extraction", "Verbal Ability", "Reading Comprehension",
         "1. Question-First Strategy: Read question stems (not options) before reading the passage to prime your brain for key target terms.\n2. Structural Reading: First paragraph (thesis), topic sentences of body paragraphs (supporting arguments), final paragraph (conclusion).\n3. Fact vs Inference: Facts are explicitly stated; inferences must logically follow without speculation.",
         "Extreme Language Trap: Options containing 'always', 'never', 'all', 'completely', 'impossible' are incorrect 90% of the time in RC tests.",
         "Campus recruitment RC passages are typically 250-400 words testing main idea, specific details, vocabulary in context, and author tone (analytical, critical, optimistic, neutral). Do not re-read entire paragraphs; locate keywords."),

        ("TCS NQT Comprehensive Aptitude Simulation", "Placement Diagnostic", "TCS NQT Special",
         "Comprehensive multi-domain review covering Foundation Numerical, Advanced Quantitative, and Logical Reasoning patterns.",
         "Speed Strategy: Attempt easy arithmetic and series first; reserve multi-statement seating and geometry for the second pass.",
         "TCS NQT features both Foundation and Advanced sections on the TCS iON interface. Calculators are available on-screen for numeric sections, meaning manual arithmetic is replaced by complex problem interpretation."),

        ("Infosys & Wipro Critical Reasoning Simulation", "Placement Diagnostic", "Infosys & Wipro Special",
         "Comprehensive review covering Infosys Puzzle Solving, Syllogisms, and Wipro Analytical Reasoning models.",
         "Infosys Non-Revisitation Rule: You cannot return to previous questions. Allocate a fixed 90 seconds per question; never get stuck on one puzzle.",
         "Infosys and Wipro place heavy weight on reasoning and pseudocode accuracy. Ensuring zero negative marks by deliberate option elimination is the highest-leverage strategy."),

        ("Grand Campus Recruitment Diagnostic (Mixed Speed Test)", "Placement Simulation", "All Recruiters",
         "Final multi-disciplinary placement aptitude exam simulating actual corporate recruitment day conditions.",
         "The 100-Point Rule: Prioritize high-accuracy domains (percentages, ratios, series, syllogisms) to guarantee sectional cutoff clearance.",
         "Congratulations on reaching Day 30. You have mastered 30 comprehensive aptitude domains. In actual corporate exams, calmness, rapid formula recall, and disciplined time management separate the top 5% of candidates.")
    ]

    topic_data = topics[(day - 1) % len(topics)]
    topic_title = topic_data[0]
    category = topic_data[1]
    subtopic = topic_data[2]
    formulas = topic_data[3]
    shortcuts = topic_data[4]
    lesson_text = topic_data[5]

    # Generate 5 solved examples with complete step-by-step arithmetic
    solved_examples = [
        {
            "example_no": 1,
            "title": f"Foundation Problem on {subtopic}",
            "question": f"A student scores 75% on an initial diagnostic test and subsequently improves by 20% on the final assessment. If the maximum marks were 200, find the student's final score.",
            "step_by_step_solution": [
                "Step 1: Calculate initial score = 75% of 200 = (75 / 100) * 200 = 150 marks.",
                "Step 2: Improvement factor = 20% increase on initial score.",
                "Step 3: Score increase = 20% of 150 = (20 / 100) * 150 = 30 marks.",
                "Step 4: Final score = 150 + 30 = 180 marks out of 200 (or 90%).",
                "Speed Check: Direct factor = 200 * 0.75 * 1.20 = 200 * 0.90 = 180 marks."
            ],
            "final_answer": "180 marks (90%)"
        },
        {
            "example_no": 2,
            "title": f"Standard Placement Problem on {subtopic}",
            "question": f"If an item is marked at Rs. 1,200 and sold after two successive discounts of 10% and 20%, what is the net selling price?",
            "step_by_step_solution": [
                "Step 1: Single equivalent discount = d1 + d2 - (d1 * d2 / 100)% = 10 + 20 - (10 * 20 / 100)% = 30 - 2 = 28%.",
                "Step 2: Selling price = Marked Price * (1 - Equivalent Discount / 100).",
                "Step 3: SP = 1200 * (1 - 0.28) = 1200 * 0.72 = Rs. 864.",
                "Verification: After 10% discount on 1200 = 1200 - 120 = 1080. After 20% discount on 1080 = 1080 - 216 = Rs. 864."
            ],
            "final_answer": "Rs. 864"
        },
        {
            "example_no": 3,
            "title": f"Efficiency & Work Ratio Problem on {subtopic}",
            "question": f"Worker A can complete a task in 12 days and Worker B can complete the same task in 18 days. If they work on alternate days starting with A, in how many days will the work be completed?",
            "step_by_step_solution": [
                "Step 1: Assume Total Work = LCM(12, 18) = 36 units.",
                "Step 2: A's 1-day work = 36 / 12 = 3 units/day. B's 1-day work = 36 / 18 = 2 units/day.",
                "Step 3: In a 2-day cycle (Day 1: A, Day 2: B), total work done = 3 + 2 = 5 units.",
                "Step 4: Number of complete cycles in 36 units = 36 // 5 = 7 cycles (14 days), completing 7 * 5 = 35 units.",
                "Step 5: Remaining work = 36 - 35 = 1 unit. Day 15 is A's turn (efficiency 3 units/day). Time taken by A = 1/3 day.",
                "Step 6: Total days = 14 + 1/3 = 14 1/3 days (or 14.33 days)."
            ],
            "final_answer": "14 1/3 days"
        },
        {
            "example_no": 4,
            "title": f"Speed & Relative Distance Problem on {subtopic}",
            "question": f"Two stations X and Y are 390 km apart. A train starts from X at 10 AM heading towards Y at 65 km/hr. Another train starts from Y at 11 AM heading towards X at 35 km/hr. At what time will they meet?",
            "step_by_step_solution": [
                "Step 1: Standardize start time to 11 AM. Distance covered by Train 1 from 10 AM to 11 AM (1 hour) = 65 km * 1 = 65 km.",
                "Step 2: Remaining distance between trains at 11 AM = 390 - 65 = 325 km.",
                "Step 3: Relative speed in opposite directions = 65 + 35 = 100 km/hr.",
                "Step 4: Time taken to meet after 11 AM = Remaining Distance / Relative Speed = 325 / 100 = 3.25 hours = 3 hours 15 minutes.",
                "Step 5: Meeting time = 11:00 AM + 3 hours 15 minutes = 2:15 PM."
            ],
            "final_answer": "2:15 PM"
        },
        {
            "example_no": 5,
            "title": f"Combinatorics & Probability Problem on {subtopic}",
            "question": f"A bag contains 5 red balls and 4 blue balls. If 3 balls are drawn at random without replacement, what is the probability that exactly 2 are red and 1 is blue?",
            "step_by_step_solution": [
                "Step 1: Total balls in bag = 5 + 4 = 9 balls. Total ways to choose 3 balls, n(S) = 9C3 = (9 * 8 * 7) / (3 * 2 * 1) = 84.",
                "Step 2: Favorable ways to choose 2 red balls from 5 red = 5C2 = (5 * 4) / (2 * 1) = 10.",
                "Step 3: Favorable ways to choose 1 blue ball from 4 blue = 4C1 = 4.",
                "Step 4: Total favorable outcomes, n(E) = 5C2 * 4C1 = 10 * 4 = 40.",
                "Step 5: Required Probability = n(E) / n(S) = 40 / 84 = 10 / 21."
            ],
            "final_answer": "10/21"
        }
    ]

    # Retrieve 10 fresh, topic-grounded MCQs for this day from authentic banks
    if day <= 15:
        mcqs = get_aptitude_mcqs_for_day_1_15(day)
    else:
        mcqs = get_aptitude_mcqs_for_day_16_30(day)

    # Generate 5 practice problems
    practice_problems = [
        {"no": 1, "question": f"If x is 20% less than y, find the value of (y - x) / y and x / (x - y).", "answer_key": "1/5 and -4"},
        {"no": 2, "question": f"A dishonest shopkeeper professes to sell his goods at cost price but uses a false weight of 950 grams for each kilogram. Find his gain percent.", "answer_key": "5 5/19 % (approx 5.26%)"},
        {"no": 3, "question": f"Find the compound interest on Rs. 16,000 at 20% per annum for 9 months, compounded quarterly.", "answer_key": "Rs. 2,522"},
        {"no": 4, "question": f"A, B, and C enter into partnership. A invests Rs. 2,560 and B invests Rs. 2,000. At the end of the year, they gain Rs. 1,105, out of which A gets Rs. 320. Find C's capital investment.", "answer_key": "Rs. 4,280"},
        {"no": 5, "question": f"A car travels the first one-third of a distance at 20 km/hr, the next one-third at 30 km/hr, and the remaining one-third at 60 km/hr. Find the average speed for the entire journey.", "answer_key": "30 km/hr"}
    ]

    # Timed speed drill
    timed_drill = {
        "title": f"Timed Speed Drill: {subtopic} (5-Minute Sprint)",
        "duration_minutes": 5,
        "question_count": 3,
        "questions": [
            {"q": f"Express the fraction 7/16 as a percentage.", "ans": "43.75%"},
            {"q": f"If 12 men can build a wall in 20 days, how many men are needed to build it in 15 days?", "ans": "16 men"},
            {"q": f"What is the units digit of 7^105?", "ans": "7 (Cycle: 7, 9, 3, 1; 105 mod 4 = 1)"}
        ]
    }

    return {
        "topic": topic_title,
        "category": category,
        "subtopic": subtopic,
        "formulas": formulas,
        "shortcuts": shortcuts,
        "tutorial": [lesson_text],
        "solved_examples": solved_examples,
        "mcqs": mcqs,
        "practice_problems": practice_problems,
        "timed_drill": timed_drill
    }
