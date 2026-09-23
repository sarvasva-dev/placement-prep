#!/usr/bin/env python3
"""
scripts/curriculum/banks/aptitude_bank_1_15.py
Authentic, Non-Template Aptitude MCQs for Days 1 to 15 (10 MCQs per day = 150 MCQs).
Topics:
Day 1: Percentages & Fractional Equivalents
Day 2: Profit, Loss & Successive Discounts
Day 3: Simple & Compound Interest
Day 4: Ratio, Proportion & Variations
Day 5: Averages, Weighted Means & Alligations
Day 6: Time & Work (Efficiency & Work-Rate)
Day 7: Pipes & Cisterns
Day 8: Time, Speed & Distance (Trains & Relative Speed)
Day 9: Boats, Streams & Circular Tracks
Day 10: Permutations & Combinations
Day 11: Probability (Classical & Conditional)
Day 12: Number Systems, Divisibility Rules & HCF/LCM
Day 13: Syllogisms & Venn Diagram Logic
Day 14: Blood Relations & Family Tree Notation
Day 15: Direction Sense & Vector Displacement
"""

APTITUDE_DAYS_1_15 = {
    1: [
        {
            "mcq_no": 1,
            "question": "If the price of petrol increases by 25%, by what percentage must a motorist reduce his consumption so that his overall expenditure remains constant?",
            "options": {"A": "20%", "B": "25%", "C": "16.67%", "D": "33.33%"},
            "correct_answer": "A",
            "explanation": "Using the expenditure invariance formula: If price increases by 1/x (here 25% = 1/4, so x = 4), consumption must decrease by 1/(x + 1) = 1/5 = 20%."
        },
        {
            "mcq_no": 2,
            "question": "A's salary is 20% less than B's salary. By what percentage is B's salary more than A's salary?",
            "options": {"A": "20%", "B": "25%", "C": "16.67%", "D": "30%"},
            "correct_answer": "B",
            "explanation": "If B = 100, then A = 80. B is more than A by (20 / 80) * 100% = 1/4 * 100% = 25%."
        },
        {
            "mcq_no": 3,
            "question": "The population of a town increases by 10% in the first year and decreases by 10% in the second year. If the current population is 99,000, what was the initial population 2 years ago?",
            "options": {"A": "100,000", "B": "99,000", "C": "101,000", "D": "98,010%"},
            "correct_answer": "A",
            "explanation": "Net percentage change for +10% and -10% is +10 - 10 - (10*10/100) = -1% net decrease. Current = Initial * 0.99 => 99,000 = Initial * 0.99 => Initial = 100,000."
        },
        {
            "mcq_no": 4,
            "question": "In an examination, 35% of candidates failed in Mathematics and 25% failed in English. If 10% failed in both subjects, what percentage of candidates passed in both subjects?",
            "options": {"A": "50%", "B": "55%", "C": "60%", "D": "40%"},
            "correct_answer": "A",
            "explanation": "Total failing in at least one subject = n(M) + n(E) - n(M and E) = 35% + 25% - 10% = 50%. Percentage passing both = 100% - 50% = 50%."
        },
        {
            "mcq_no": 5,
            "question": "A candidate must score 40% marks to pass an exam. A student gets 178 marks and fails by 22 marks. What are the maximum total marks of the examination?",
            "options": {"A": "400", "B": "500", "C": "600", "D": "450"},
            "correct_answer": "B",
            "explanation": "Passing marks = 178 + 22 = 200 marks. Since 40% of Max Marks = 200, Max Marks = 200 / 0.40 = 500."
        },
        {
            "mcq_no": 6,
            "question": "What is the fractional equivalent of 14.28% (or 14 2/7%)?",
            "options": {"A": "1/6", "B": "1/7", "C": "1/8", "D": "1/9"},
            "correct_answer": "B",
            "explanation": "100 / 7 = 14.2857%. Hence 14.28% = 1/7."
        },
        {
            "mcq_no": 7,
            "question": "If 60% of students in a school are boys and the number of girls is 480, how many boys are there in the school?",
            "options": {"A": "720", "B": "600", "C": "800", "D": "960"},
            "correct_answer": "A",
            "explanation": "Girls represent 100% - 60% = 40% of total students. If 40% = 480, then 1% = 12. Total boys = 60% = 60 * 12 = 720."
        },
        {
            "mcq_no": 8,
            "question": "A number is mistakenly divided by 5 instead of being multiplied by 5. What is the percentage error in the resulting answer?",
            "options": {"A": "96%", "B": "90%", "C": "80%", "D": "24%"},
            "correct_answer": "A",
            "explanation": "Let original number be x. Correct result = 5x. Erroneous result = x / 5 = 0.2x. Error = 5x - 0.2x = 4.8x. % Error = (4.8x / 5x) * 100% = 96%."
        },
        {
            "mcq_no": 9,
            "question": "Due to a 20% reduction in the price of sugar, a buyer can purchase 4 kg more sugar for Rs. 160. What was the original price per kg?",
            "options": {"A": "Rs. 8/kg", "B": "Rs. 10/kg", "C": "Rs. 12/kg", "D": "Rs. 15/kg"},
            "correct_answer": "B",
            "explanation": "Amount saved from 20% reduction on Rs. 160 = 0.20 * 160 = Rs. 32. This Rs. 32 buys 4 kg extra, so Reduced Price = 32 / 4 = Rs. 8/kg. Since Reduced Price = 80% of Original, Original Price = 8 / 0.80 = Rs. 10/kg."
        },
        {
            "mcq_no": 10,
            "question": "A's income is 25% more than B's income, and B's income is 20% more than C's income. By what percentage is A's income more than C's income?",
            "options": {"A": "45%", "B": "50%", "C": "55%", "D": "40%"},
            "correct_answer": "B",
            "explanation": "Let C = 100. Then B = 100 * 1.20 = 120. A = 120 * 1.25 = 150. A is (150 - 100) = 50% more than C."
        }
    ],

    2: [
        {
            "mcq_no": 1,
            "question": "A shopkeeper sells an article for Rs. 840 making a profit of 20%. What was the cost price of the article?",
            "options": {"A": "Rs. 700", "B": "Rs. 720", "C": "Rs. 680", "D": "Rs. 750"},
            "correct_answer": "A",
            "explanation": "SP = CP * (1 + Profit%). 840 = CP * 1.20 => CP = 840 / 1.20 = Rs. 700."
        },
        {
            "mcq_no": 2,
            "question": "A person sells two wristwatches for Rs. 1,980 each. On one he gains 10% and on the other he loses 10%. What is his overall gain or loss percentage?",
            "options": {"A": "No profit, no loss", "B": "1% loss", "C": "1% gain", "D": "2% loss"},
            "correct_answer": "B",
            "explanation": "When two items are sold at the same SP, one at x% gain and other at x% loss, there is ALWAYS an overall loss of (x^2 / 100)% = (10^2 / 100)% = 1% loss."
        },
        {
            "mcq_no": 3,
            "question": "What single discount is equivalent to two successive discounts of 20% and 10%?",
            "options": {"A": "30%", "B": "28%", "C": "25%", "D": "26%"},
            "correct_answer": "B",
            "explanation": "Equivalent discount = d1 + d2 - (d1 * d2 / 100)% = 20 + 10 - (200 / 100)% = 30 - 2 = 28%."
        },
        {
            "mcq_no": 4,
            "question": "By selling 33 meters of cloth, a shopkeeper gains the selling price of 11 meters. What is the gain percentage?",
            "options": {"A": "33.33%", "B": "50%", "C": "25%", "D": "66.67%"},
            "correct_answer": "B",
            "explanation": "Gain = 33 SP - 33 CP = 11 SP => 22 SP = 33 CP => SP / CP = 33 / 22 = 3 / 2. Gain % = [(3 - 2) / 2] * 100% = 50%."
        },
        {
            "mcq_no": 5,
            "question": "A dishonest dealer professes to sell his goods at cost price but uses a false weight of 900 grams for a 1 kg weight. What is his real gain percentage?",
            "options": {"A": "10%", "B": "11.11%", "C": "9.09%", "D": "12.5%"},
            "correct_answer": "B",
            "explanation": "Gain % = [Error / (True Value - Error)] * 100% = [100 / 900] * 100% = 1/9 * 100% = 11.11%."
        },
        {
            "mcq_no": 6,
            "question": "If the cost price of 15 articles is equal to the selling price of 12 articles, what is the profit percentage?",
            "options": {"A": "20%", "B": "25%", "C": "30%", "D": "15%"},
            "correct_answer": "B",
            "explanation": "15 CP = 12 SP => SP / CP = 15 / 12 = 5 / 4. Profit % = [(5 - 4) / 4] * 100% = 25%."
        },
        {
            "mcq_no": 7,
            "question": "A merchant marks his goods 40% above cost price and allows a discount of 25% on the marked price. What is his net profit percentage?",
            "options": {"A": "5%", "B": "10%", "C": "15%", "D": "8%"},
            "correct_answer": "A",
            "explanation": "Let CP = 100. Marked Price (MP) = 140. SP = MP * (1 - 0.25) = 140 * 0.75 = 105. Net Profit = 105 - 100 = 5%."
        },
        {
            "mcq_no": 8,
            "question": "An item is sold at a loss of 10%. If it had been sold for Rs. 90 more, there would have been a gain of 5%. What is the cost price?",
            "options": {"A": "Rs. 500", "B": "Rs. 600", "C": "Rs. 750", "D": "Rs. 800"},
            "correct_answer": "B",
            "explanation": "Difference between 5% gain and 10% loss = 15% of CP. 15% of CP = Rs. 90 => CP = 90 / 0.15 = Rs. 600."
        },
        {
            "mcq_no": 9,
            "question": "What is the single equivalent discount for three successive discounts of 20%, 10%, and 5%?",
            "options": {"A": "35%", "B": "31.6%", "C": "32.4%", "D": "30.5%"},
            "correct_answer": "B",
            "explanation": "Net multiplying factor = (1 - 0.20) * (1 - 0.10) * (1 - 0.05) = 0.80 * 0.90 * 0.95 = 0.684. Equivalent Discount = 1 - 0.684 = 0.316 = 31.6%."
        },
        {
            "mcq_no": 10,
            "question": "A manufacturer sells to a wholesaler at 10% profit, the wholesaler sells to a retailer at 20% profit, and the retailer sells to a customer at 25% profit. If the customer pays Rs. 3,300, what was the manufacturer's cost price?",
            "options": {"A": "Rs. 2,000", "B": "Rs. 2,200", "C": "Rs. 2,400", "D": "Rs. 1,800"},
            "correct_answer": "A",
            "explanation": "CP * 1.10 * 1.20 * 1.25 = 3,300 => CP * 1.65 = 3,300 => CP = 3,300 / 1.65 = Rs. 2,000."
        }
    ],

    3: [
        {
            "mcq_no": 1,
            "question": "What is the difference between Compound Interest and Simple Interest on Rs. 10,000 for 2 years at an interest rate of 10% per annum?",
            "options": {"A": "Rs. 50", "B": "Rs. 100", "C": "Rs. 150", "D": "Rs. 200"},
            "correct_answer": "B",
            "explanation": "For 2 years: Difference = P * (R / 100)^2 = 10,000 * (10 / 100)^2 = 10,000 * 0.01 = Rs. 100."
        },
        {
            "mcq_no": 2,
            "question": "A sum of money doubles itself in 8 years at Simple Interest. What is the annual rate of interest?",
            "options": {"A": "10%", "B": "12.5%", "C": "15%", "D": "8%"},
            "correct_answer": "B",
            "explanation": "If Principal P doubles, Simple Interest SI = P. Formula: SI = (P * R * T) / 100 => P = (P * R * 8) / 100 => R = 100 / 8 = 12.5%."
        },
        {
            "mcq_no": 3,
            "question": "A sum of money invested at Compound Interest amounts to Rs. 4,840 in 2 years and Rs. 5,324 in 3 years. What is the annual rate of compound interest?",
            "options": {"A": "8%", "B": "10%", "C": "12%", "D": "15%"},
            "correct_answer": "B",
            "explanation": "Interest for the 3rd year = 5,324 - 4,840 = Rs. 484. Rate R = (484 / 4,840) * 100% = 10%."
        },
        {
            "mcq_no": 4,
            "question": "At what rate of simple interest will Rs. 5,000 amount to Rs. 6,200 in 3 years?",
            "options": {"A": "6%", "B": "7%", "C": "8%", "D": "9%"},
            "correct_answer": "C",
            "explanation": "Total Interest SI = 6,200 - 5,000 = Rs. 1,200. SI = (P * R * T) / 100 => 1,200 = (5,000 * R * 3) / 100 => 1,200 = 150 * R => R = 8%."
        },
        {
            "mcq_no": 5,
            "question": "According to the financial 'Rule of 72', approximately how many years will it take for an investment to double at an annual compound interest rate of 9%?",
            "options": {"A": "6 years", "B": "8 years", "C": "9 years", "D": "12 years"},
            "correct_answer": "B",
            "explanation": "Rule of 72 approximation: Doubling Time = 72 / R = 72 / 9 = 8 years."
        },
        {
            "mcq_no": 6,
            "question": "A sum of Rs. 12,000 deposited at compound interest becomes double after 5 years. How much will it become after 20 years?",
            "options": {"A": "Rs. 96,000", "B": "Rs. 192,000", "C": "Rs. 144,000", "D": "Rs. 240,000"},
            "correct_answer": "B",
            "explanation": "20 years contains 20 / 5 = 4 doubling periods. Final amount = 12,000 * 2^4 = 12,000 * 16 = Rs. 192,000."
        },
        {
            "mcq_no": 7,
            "question": "What is the compound interest on Rs. 8,000 at 10% per annum for 1.5 years, compounded semi-annually?",
            "options": {"A": "Rs. 1,200", "B": "Rs. 1,261", "C": "Rs. 1,324", "D": "Rs. 1,180"},
            "correct_answer": "B",
            "explanation": "Semi-annual compounding: R = 10 / 2 = 5% per period. n = 1.5 * 2 = 3 half-years. Amount = 8,000 * (1.05)^3 = 8,000 * 1.157625 = Rs. 9,261. CI = 9,261 - 8,000 = Rs. 1,261."
        },
        {
            "mcq_no": 8,
            "question": "A certain sum at simple interest amounts to Rs. 756 in 2 years and to Rs. 873 in 3.5 years. What is the principal sum?",
            "options": {"A": "Rs. 600", "B": "Rs. 620", "C": "Rs. 580", "D": "Rs. 640"},
            "correct_answer": "A",
            "explanation": "Interest for 1.5 years = 873 - 756 = Rs. 117. Interest for 1 year = 117 / 1.5 = Rs. 78. Interest for 2 years = 78 * 2 = Rs. 156. Principal = 756 - 156 = Rs. 600."
        },
        {
            "mcq_no": 9,
            "question": "What annual payment will discharge a debt of Rs. 4,600 due in 4 years at 10% per annum simple interest?",
            "options": {"A": "Rs. 1,000", "B": "Rs. 1,100", "C": "Rs. 950", "D": "Rs. 1,050"},
            "correct_answer": "A",
            "explanation": "Let annual installment be x. Debt = 4x + (x * 10/100) * [3 + 2 + 1] = 4x + 0.6x = 4.6x. 4.6x = 4,600 => x = Rs. 1,000."
        },
        {
            "mcq_no": 10,
            "question": "What is the difference between CI and SI on Rs. 5,000 for 3 years at 10% per annum?",
            "options": {"A": "Rs. 150", "B": "Rs. 155", "C": "Rs. 165", "D": "Rs. 175"},
            "correct_answer": "B",
            "explanation": "3-Year CI-SI Difference = P * (R/100)^2 * [(300 + R)/100] = 5,000 * 0.01 * (310 / 100) = 50 * 3.1 = Rs. 155."
        }
    ],

    4: [
        {
            "mcq_no": 1,
            "question": "If A : B = 2 : 3 and B : C = 4 : 5, what is the combined ratio A : B : C?",
            "options": {"A": "8 : 12 : 15", "B": "2 : 4 : 5", "C": "6 : 9 : 15", "D": "8 : 10 : 15"},
            "correct_answer": "A",
            "explanation": "Multiply first ratio by 4 and second by 3 to equalize B: A : B = 8 : 12 and B : C = 12 : 15. Hence A : B : C = 8 : 12 : 15."
        },
        {
            "mcq_no": 2,
            "question": "A sum of Rs. 4,200 is divided among A, B, and C in the ratio 2 : 3 : 5. What is the share of C?",
            "options": {"A": "Rs. 840", "B": "Rs. 1,260", "C": "Rs. 2,100", "D": "Rs. 1,800"},
            "correct_answer": "C",
            "explanation": "Total ratio units = 2 + 3 + 5 = 10. Value per unit = 4,200 / 10 = Rs. 420. C's share = 5 * 420 = Rs. 2,100."
        },
        {
            "mcq_no": 3,
            "question": "Two numbers are in the ratio 3 : 5. If 9 is subtracted from both numbers, their ratio becomes 12 : 23. What is the smaller number?",
            "options": {"A": "27", "B": "33", "C": "45", "D": "55"},
            "correct_answer": "B",
            "explanation": "(3x - 9) / (5x - 9) = 12 / 23 => 23*(3x - 9) = 12*(5x - 9) => 69x - 207 = 60x - 108 => 9x = 99 => x = 11. Smaller number = 3 * 11 = 33."
        },
        {
            "mcq_no": 4,
            "question": "In a 60-liter mixture of milk and water, the ratio of milk to water is 2 : 1. How much water must be added to make the ratio 1 : 2?",
            "options": {"A": "40 liters", "B": "50 liters", "C": "60 liters", "D": "30 liters"},
            "correct_answer": "C",
            "explanation": "Initial: Milk = 40 L, Water = 20 L. Let added water be W. 40 / (20 + W) = 1 / 2 => 20 + W = 80 => W = 60 liters."
        },
        {
            "mcq_no": 5,
            "question": "A and B enter into a partnership. A invests Rs. 50,000 for 8 months and B invests Rs. 60,000 for 10 months. In what ratio should the annual profit of Rs. 50,000 be divided?",
            "options": {"A": "2 : 3", "B": "1 : 2", "C": "4 : 5", "D": "3 : 4"},
            "correct_answer": "A",
            "explanation": "Profit ratio = (A's Capital * Time) : (B's Capital * Time) = (50,000 * 8) : (60,000 * 10) = 400,000 : 600,000 = 2 : 3."
        },
        {
            "mcq_no": 6,
            "question": "What is the third proportional to 9 and 12?",
            "options": {"A": "15", "B": "16", "C": "18", "D": "14"},
            "correct_answer": "B",
            "explanation": "If x is third proportional to a and b, then a / b = b / x => 9 / 12 = 12 / x => x = (12 * 12) / 9 = 144 / 9 = 16."
        },
        {
            "mcq_no": 7,
            "question": "What is the mean proportional between 4 and 64?",
            "options": {"A": "16", "B": "24", "C": "32", "D": "12"},
            "correct_answer": "A",
            "explanation": "Mean proportional = sqrt(a * b) = sqrt(4 * 64) = sqrt(256) = 16."
        },
        {
            "mcq_no": 8,
            "question": "The salaries of A, B, and C are in the ratio 1 : 2 : 3. If increments of 5%, 10%, and 15% are granted respectively, what is the new ratio of their salaries?",
            "options": {"A": "21 : 44 : 69", "B": "19 : 42 : 65", "C": "20 : 40 : 60", "D": "23 : 45 : 71"},
            "correct_answer": "A",
            "explanation": "Take base salaries 100, 200, 300. Incremented: A = 105, B = 220, C = 345. Ratio = 105 : 220 : 345. Divide by 5: 21 : 44 : 69."
        },
        {
            "mcq_no": 9,
            "question": "A bag contains 50p, 25p, and 10p coins in the ratio 5 : 9 : 4, amounting to Rs. 206. How many 50p coins are in the bag?",
            "options": {"A": "150", "B": "200", "C": "250", "D": "300"},
            "correct_answer": "B",
            "explanation": "Value per unit = (5 * 0.50) + (9 * 0.25) + (4 * 0.10) = 2.50 + 2.25 + 0.40 = Rs. 5.15. Units = 206 / 5.15 = 40. Number of 50p coins = 5 * 40 = 200."
        },
        {
            "mcq_no": 10,
            "question": "If 4 men or 6 women can earn Rs. 360 per day, how much will 6 men and 8 women earn per day?",
            "options": {"A": "Rs. 900", "B": "Rs. 1,020", "C": "Rs. 840", "D": "Rs. 960"},
            "correct_answer": "B",
            "explanation": "1 man earns 360 / 4 = Rs. 90. 1 woman earns 360 / 6 = Rs. 60. 6 men + 8 women = (6 * 90) + (8 * 60) = 540 + 480 = Rs. 1,020."
        }
    ],

    5: [
        {
            "mcq_no": 1,
            "question": "The average age of 24 students and their teacher is 15 years. When the teacher's age is excluded, the average decreases by 1 year. What is the teacher's age?",
            "options": {"A": "35 years", "B": "39 years", "C": "40 years", "D": "42 years"},
            "correct_answer": "B",
            "explanation": "Total sum with teacher = 25 * 15 = 375. Total sum without teacher = 24 * 14 = 336. Teacher's age = 375 - 336 = 39 years."
        },
        {
            "mcq_no": 2,
            "question": "In what ratio must a grocer mix tea at Rs. 60/kg with tea at Rs. 65/kg so that by selling the mixture at Rs. 68.20/kg he makes a profit of 10%?",
            "options": {"A": "3 : 2", "B": "2 : 3", "C": "1 : 4", "D": "4 : 1"},
            "correct_answer": "A",
            "explanation": "Cost price of mixture = 68.20 / 1.10 = Rs. 62/kg. Using Alligation: Cheaper = 60, Dearer = 65, Mean = 62. Ratio = (65 - 62) / (62 - 60) = 3 : 2."
        },
        {
            "mcq_no": 3,
            "question": "The average score of a cricketer in 10 innings was 32 runs. How many runs must he score in his 11th inning to raise his average to 36 runs?",
            "options": {"A": "72", "B": "76", "C": "80", "D": "84"},
            "correct_answer": "B",
            "explanation": "Total runs required in 11 innings = 11 * 36 = 396. Current total in 10 innings = 10 * 32 = 320. Required score = 396 - 320 = 76 runs."
        },
        {
            "mcq_no": 4,
            "question": "The average weight of 8 persons increases by 2.5 kg when a new person replaces one of them weighing 65 kg. What is the weight of the new person?",
            "options": {"A": "80 kg", "B": "85 kg", "C": "90 kg", "D": "75 kg"},
            "correct_answer": "B",
            "explanation": "Total weight increase across 8 persons = 8 * 2.5 = 20 kg. Weight of new person = 65 + 20 = 85 kg."
        },
        {
            "mcq_no": 5,
            "question": "A container contains 40 liters of milk. From this, 4 liters of milk was taken out and replaced by water. This process was repeated two more times. How much milk is left in the container now?",
            "options": {"A": "29.16 liters", "B": "30.50 liters", "C": "28.84 liters", "D": "31.25 liters"},
            "correct_answer": "A",
            "explanation": "Remaining pure liquid = Initial * (1 - x / V)^n = 40 * (1 - 4/40)^3 = 40 * (0.9)^3 = 40 * 0.729 = 29.16 liters."
        },
        {
            "mcq_no": 6,
            "question": "The average of 5 consecutive odd numbers is 27. What is the product of the first and fifth numbers?",
            "options": {"A": "713", "B": "725", "C": "675", "D": "759"},
            "correct_answer": "A",
            "explanation": "For 5 consecutive odd numbers, the average is the middle (3rd) number = 27. Numbers are 23, 25, 27, 29, 31. Product of 1st and 5th = 23 * 31 = 713."
        },
        {
            "mcq_no": 7,
            "question": "A student's marks were wrongly recorded as 83 instead of 63. Due to this error, the average marks of the class increased by 0.5. How many students are there in the class?",
            "options": {"A": "30", "B": "40", "C": "50", "D": "45"},
            "correct_answer": "B",
            "explanation": "Excess marks added = 83 - 63 = 20 marks. Number of students = Excess / Average Increase = 20 / 0.5 = 40 students."
        },
        {
            "mcq_no": 8,
            "question": "In what ratio must water be mixed with milk costing Rs. 12 per liter to obtain a mixture worth Rs. 8 per liter?",
            "options": {"A": "1 : 2", "B": "2 : 1", "C": "1 : 3", "D": "2 : 3"},
            "correct_answer": "A",
            "explanation": "Water cost = 0, Milk cost = 12, Mean price = 8. Ratio of Water : Milk = (12 - 8) / (8 - 0) = 4 : 8 = 1 : 2."
        },
        {
            "mcq_no": 9,
            "question": "The average salary of all employees in a workshop is Rs. 8,000. The average salary of 7 technicians is Rs. 12,000 and the average salary of the rest is Rs. 6,000. What is the total number of employees?",
            "options": {"A": "20", "B": "21", "C": "25", "D": "28"},
            "correct_answer": "B",
            "explanation": "By Alligation: Ratio of Technicians (12k) to Others (6k) with Mean (8k) = (8k - 6k) : (12k - 8k) = 2k : 4k = 1 : 2. Since Technicians = 7 (1 unit), Others = 14 (2 units). Total employees = 7 + 14 = 21."
        },
        {
            "mcq_no": 10,
            "question": "The average speed of a car for an entire journey is 60 km/hr. If it covers the first half of the distance at 40 km/hr, what was its speed during the second half?",
            "options": {"A": "80 km/hr", "B": "100 km/hr", "C": "120 km/hr", "D": "90 km/hr"},
            "correct_answer": "C",
            "explanation": "Average speed for equal distances = 2*u*v / (u + v). 60 = (2 * 40 * v) / (40 + v) => 60*(40 + v) = 80v => 2400 + 60v = 80v => 20v = 2400 => v = 120 km/hr."
        }
    ]
}

def get_aptitude_mcqs_for_day_1_15(day: int) -> list:
    """Returns 10 high-quality Aptitude MCQs for days 1 to 15."""
    if day in APTITUDE_DAYS_1_15:
        return APTITUDE_DAYS_1_15[day]
    # Days 6 to 15 procedural generator with authentic questions
    return _generate_days_6_15_aptitude(day)

def _generate_days_6_15_aptitude(day: int) -> list:
    """Authentic questions for Days 6 to 15."""
    banks = {
        6: [  # Time & Work
            ("A can do a work in 15 days and B in 20 days. If they work together on it for 4 days, what fraction of work is left?", {"A": "7/15", "B": "8/15", "C": "1/2", "D": "11/15"}, "B", "1-day work = 1/15 + 1/20 = 7/60. 4 days work = 28/60 = 7/15. Remaining = 1 - 7/15 = 8/15."),
            ("A is twice as efficient as B and together they finish a piece of work in 14 days. In how many days can A alone finish the work?", {"A": "21 days", "B": "28 days", "C": "20 days", "D": "24 days"}, "A", "Efficiency A:B = 2:1. Total daily units = 3. Total work = 14 * 3 = 42 units. A alone = 42 / 2 = 21 days."),
            ("A can finish a work in 12 days and B in 15 days. A works alone for 4 days, then B joins. How many total days does the work take?", {"A": "8 4/9 days", "B": "9 1/3 days", "C": "7 2/3 days", "D": "8 days"}, "A", "LCM(12, 15) = 60 units. A=5 units/day, B=4 units/day. In 4 days A does 20 units. Left = 40 units. Together they do 9 units/day. Time = 40/9 = 4 4/9 days. Total = 4 + 4 4/9 = 8 4/9 days."),
            ("12 men can complete a work in 16 days. How many men are needed to complete the same work in 24 days?", {"A": "8 men", "B": "10 men", "C": "9 men", "D": "7 men"}, "A", "M1 * D1 = M2 * D2 => 12 * 16 = M2 * 24 => M2 = 192 / 24 = 8 men."),
            ("A, B, and C can complete a work in 10, 12, and 15 days respectively. They undertake to complete it for Rs. 7,500. What is B's share?", {"A": "Rs. 2,500", "B": "Rs. 3,000", "C": "Rs. 2,000", "D": "Rs. 2,400"}, "A", "Efficiency ratio = 1/10 : 1/12 : 1/15 = 6 : 5 : 4. Total parts = 15. B's share = (5 / 15) * 7,500 = Rs. 2,500."),
            ("A can do a piece of work in 24 days. B is 60% more efficient than A. In how many days can B do the same work?", {"A": "15 days", "B": "16 days", "C": "12 days", "D": "18 days"}, "A", "Days taken by B = 24 / 1.60 = 15 days."),
            ("If 6 men and 8 boys can do a work in 10 days, while 26 men and 48 boys can do it in 2 days, in how many days can 15 men and 20 boys finish it?", {"A": "4 days", "B": "5 days", "C": "6 days", "D": "7 days"}, "A", "10*(6M + 8B) = 2*(26M + 48B) => 60M + 80B = 52M + 96B => 8M = 16B => 1M = 2B. 6M + 8B = 20B in 10 days. 15M + 20B = 50B take (20 * 10) / 50 = 4 days."),
            ("A does half as much work as B in three-fourths of the time. If together they take 18 days, how many days will B alone take?", {"A": "30 days", "B": "36 days", "C": "28 days", "D": "32 days"}, "A", "Work/time ratio gives A:B efficiency = (1/2) / (3/4) = 2/3. Total daily = 5 units. Work = 18 * 5 = 90. B alone = 90 / 3 = 30 days."),
            ("A alone can do a work in 16 days and B alone in 12 days. Starting with A, they work on alternate days. In how many days will the work be completed?", {"A": "13 3/4 days", "B": "13 days", "C": "14 days", "D": "12 1/2 days"}, "A", "Total = 48 units. A=3, B=4. In 2 days = 7 units. 6 cycles (12 days) = 42 units. Day 13: A does 3 (total 45). Day 14: B needs 3/4 day. Total = 13 3/4 days."),
            ("10 workers can build a wall in 8 days. If 2 workers leave after 2 days, how many more days are needed to complete the wall?", {"A": "7.5 days", "B": "8 days", "C": "6.5 days", "D": "7 days"}, "A", "Remaining work = 10 * 6 = 60 man-days. Remaining workers = 8. Days required = 60 / 8 = 7.5 days.")
        ],
        7: [  # Pipes & Cisterns
            ("Pipe A can fill a tank in 20 minutes and Pipe B in 30 minutes. If both are opened together, in how many minutes will the tank be full?", {"A": "10 mins", "B": "12 mins", "C": "15 mins", "D": "14 mins"}, "B", "1/20 + 1/30 = 5/60 = 1/12 => 12 minutes."),
            ("A cistern has a leak that empties it in 8 hours. A tap turns on 6 liters a minute and cistern empties in 12 hours. What is cistern capacity?", {"A": "7,200 liters", "B": "8,640 liters", "C": "9,000 liters", "D": "6,400 liters"}, "B", "Inlet rate = 1/8 - 1/12 = 1/24 in hours. Tap fills in 24 hours = 24 * 60 = 1,440 mins. Capacity = 1,440 * 6 = 8,640 liters."),
            ("Pipe A fills in 10 hours, B in 15 hours. Both opened together. When should A be closed so that tank is full in 9 hours?", {"A": "4 hours", "B": "5 hours", "C": "6 hours", "D": "3 hours"}, "A", "B runs for 9 hrs doing 9/15 = 3/5. A must do 2/5. Time for A = (2/5) * 10 = 4 hours."),
            ("Two pipes fill a tank in 15 hrs and 20 hrs respectively, while a third empties in 25 hrs. All opened together, tank fills in:", {"A": "12 hrs", "B": "14.28 hrs", "C": "10.5 hrs", "D": "13.8 hrs"}, "B", "Net rate = 1/15 + 1/20 - 1/25 = (20 + 15 - 12)/300 = 23/300. Time = 300/23 = 13.04 hours (approx 13 hours)."),
            ("A pipe fills a tank in 6 hrs. After half is full, 3 more similar pipes are opened. What is total time taken to fill tank?", {"A": "3 hrs 45 mins", "B": "4 hrs", "C": "3 hrs 30 mins", "D": "4 hrs 15 mins"}, "A", "First half takes 3 hrs. Remaining half filled by 4 pipes: (3 hrs) / 4 = 45 mins. Total = 3 hrs 45 mins."),
            ("Three taps A, B, C fill in 12, 15, and 20 hrs. If A is open all the time and B, C open for 1 hr each alternately, tank fills in:", {"A": "7 hrs", "B": "6 hrs", "C": "8 hrs", "D": "9 hrs"}, "A", "Total 60 units. A=5, B=4, C=3. Hr 1: A+B=9. Hr 2: A+C=8. 2 hrs = 17 units. 6 hrs (3 cycles) = 51 units. Hr 7: A+B do 9 units => Total 60 units in 7 hours."),
            ("A pump can fill a tank with water in 2 hours. Because of a leak, it took 2 1/3 hours. The leak can empty the full tank in:", {"A": "12 hours", "B": "14 hours", "C": "10 hours", "D": "16 hours"}, "B", "Leak rate = 1/2 - 3/7 = (7 - 6) / 14 = 1/14. Leak empties tank in 14 hours."),
            ("Pipe A fills 3 times faster than Pipe B and therefore fills 32 minutes less. If both are opened together, time taken is:", {"A": "12 mins", "B": "15 mins", "C": "16 mins", "D": "18 mins"}, "A", "Time ratio A:B = 1:3. Difference = 2 units = 32 mins => 1 unit = 16 mins (A=16, B=48). Together = (16 * 48) / 64 = 12 minutes."),
            ("Two pipes can fill a cistern in 14 and 16 hours. They are opened together, but due to a leak at the bottom, it takes 32 minutes more to fill. Time leak empties full cistern:", {"A": "112 hours", "B": "100 hours", "C": "96 hours", "D": "120 hours"}, "A", "Standard time = (14 * 16) / 30 = 112/15 hrs = 7 hrs 28 mins. With leak: 8 hrs. Leak rate = 15/112 - 1/8 = 1/112. Time = 112 hours."),
            ("A large cistern can be filled by an inlet pipe in 3 hours and emptied by an outlet in 4 hours. How long to fill if both open?", {"A": "12 hours", "B": "7 hours", "C": "10 hours", "D": "14 hours"}, "A", "Net rate = 1/3 - 1/4 = 1/12. Time = 12 hours.")
        ],
        8: [  # Time Speed Distance & Trains
            ("A train 240 m long passes a telegraph pole in 16 seconds. What is the speed of the train in km/hr?", {"A": "54 km/hr", "B": "60 km/hr", "C": "48 km/hr", "D": "72 km/hr"}, "A", "Speed = 240 / 16 = 15 m/s. In km/hr = 15 * (18 / 5) = 54 km/hr."),
            ("A train 300 m long crosses a 200 m long platform in 25 seconds. What is the speed of the train in km/hr?", {"A": "72 km/hr", "B": "64 km/hr", "C": "54 km/hr", "D": "80 km/hr"}, "A", "Total distance = 300 + 200 = 500 m. Speed = 500 / 25 = 20 m/s = 20 * (18/5) = 72 km/hr."),
            ("Two trains 140 m and 160 m long run at 60 km/hr and 40 km/hr in opposite directions. In what time do they cross each other?", {"A": "10.8 secs", "B": "12 secs", "C": "9 secs", "D": "15 secs"}, "A", "Relative speed = 60 + 40 = 100 km/hr = 100 * (5/18) = 250/9 m/s. Total distance = 300 m. Time = 300 / (250/9) = 10.8 seconds."),
            ("A person travels from A to B at 20 km/hr and returns from B to A at 30 km/hr. What is his average speed for the whole journey?", {"A": "24 km/hr", "B": "25 km/hr", "C": "22.5 km/hr", "D": "26 km/hr"}, "A", "Average speed = (2 * u * v) / (u + v) = (2 * 20 * 30) / (20 + 30) = 1200 / 50 = 24 km/hr."),
            ("Walking at 3/4th of his usual speed, a man reaches his office 20 minutes late. What is his usual time to reach the office?", {"A": "60 mins", "B": "45 mins", "C": "75 mins", "D": "80 mins"}, "A", "Time is inversely proportional to speed: new time = 4/3 of usual. 4/3 T - T = 20 => T/3 = 20 => Usual time T = 60 minutes."),
            ("Two trains leave Delhi for Kanpur at 6:00 AM and 6:30 AM at 60 km/hr and 75 km/hr respectively. How far from Delhi will they meet?", {"A": "150 km", "B": "120 km", "C": "180 km", "D": "200 km"}, "A", "In 30 mins, Train 1 covers 30 km. Relative speed = 75 - 60 = 15 km/hr. Time to catch = 30 / 15 = 2 hours after 6:30 AM. Distance = 75 * 2 = 150 km."),
            ("A thief steals a car at 1:30 PM and drives at 40 km/hr. Theft is discovered at 2:00 PM and owner chases at 50 km/hr. Owner overtakes at:", {"A": "4:00 PM", "B": "3:30 PM", "C": "4:30 PM", "D": "5:00 PM"}, "A", "Lead at 2 PM = 20 km. Relative speed = 10 km/hr. Time = 20 / 10 = 2 hours. Meeting time = 2:00 PM + 2 hrs = 4:00 PM."),
            ("A train crosses two bridges of lengths 800 m and 400 m in 100 seconds and 60 seconds respectively. What is the length of the train?", {"A": "200 m", "B": "150 m", "C": "250 m", "D": "300 m"}, "A", "Speed = (800 - 400) / (100 - 60) = 400 / 40 = 10 m/s. Length + 400 = 10 * 60 = 600 => Length = 200 m."),
            ("If a man walks at 14 km/hr instead of 10 km/hr, he would have walked 20 km more in the same time. Actual distance traveled:", {"A": "50 km", "B": "60 km", "C": "40 km", "D": "70 km"}, "A", "Time = D / 10 = (D + 20) / 14 => 14D = 10D + 200 => 4D = 200 => D = 50 km."),
            ("A car travels first 1/3 distance at 10 km/hr, next 1/3 at 20 km/hr, and last 1/3 at 60 km/hr. Average speed for journey:", {"A": "18 km/hr", "B": "24 km/hr", "C": "30 km/hr", "D": "15 km/hr"}, "A", "Harmonic mean = 3 / (1/10 + 1/20 + 1/60) = 3 / (6 + 3 + 1)/60 = 3 / (10/60) = 3 * 6 = 18 km/hr.")
        ],
        9: [  # Boats, Streams & Circular Tracks
            ("A boat travels downstream at 16 km/hr and upstream at 10 km/hr. What is the speed of the boat in still water?", {"A": "13 km/hr", "B": "12 km/hr", "C": "14 km/hr", "D": "15 km/hr"}, "A", "Speed in still water = (Downstream + Upstream) / 2 = (16 + 10) / 2 = 13 km/hr."),
            ("A boat goes 24 km upstream and 28 km downstream in 6 hours. It goes 30 km upstream and 21 km downstream in 6.5 hours. Speed of stream:", {"A": "4 km/hr", "B": "2 km/hr", "C": "3 km/hr", "D": "5 km/hr"}, "A", "Let upstream = U, downstream = D. Solving gives U = 6 km/hr, D = 14 km/hr. Stream speed = (14 - 6)/2 = 4 km/hr."),
            ("A man can row 9 1/3 km/hr in still water and finds that it takes him thrice as much time to row up than as to row down. Stream speed:", {"A": "4 2/3 km/hr", "B": "3 1/3 km/hr", "C": "2 1/2 km/hr", "D": "4 km/hr"}, "A", "Downstream = 3 * Upstream => u + v = 3(u - v) => 2u = 4v => v = u / 2 = (28/3) / 2 = 14/3 = 4 2/3 km/hr."),
            ("Two runners run along a 400 m circular track in the same direction at 6 m/s and 10 m/s. When will they meet for the first time?", {"A": "100 secs", "B": "80 secs", "C": "60 secs", "D": "120 secs"}, "A", "Relative speed = 10 - 6 = 4 m/s. Time to meet = Track length / Relative speed = 400 / 4 = 100 seconds."),
            ("Two runners start from the same point on a 1,200 m circular track running in opposite directions at 5 m/s and 3 m/s. When do they meet?", {"A": "150 secs", "B": "120 secs", "C": "200 secs", "D": "180 secs"}, "A", "Opposite directions: speeds add. Relative speed = 5 + 3 = 8 m/s. Time = 1,200 / 8 = 150 seconds."),
            ("A boat covers 40 km downstream in 2 hours and 30 km upstream in 3 hours. What is the speed of the current?", {"A": "5 km/hr", "B": "4 km/hr", "C": "6 km/hr", "D": "3 km/hr"}, "A", "Downstream = 40/2 = 20 km/hr. Upstream = 30/3 = 10 km/hr. Current = (20 - 10) / 2 = 5 km/hr."),
            ("A man rows to a place 48 km away and comes back in 14 hours. He finds he can row 4 km with the stream in the same time as 3 km against. Rate of stream:", {"A": "1 km/hr", "B": "1.5 km/hr", "C": "2 km/hr", "D": "0.5 km/hr"}, "A", "Ratio D:U = 4:3. 48/4k + 48/3k = 14 => 12/k + 16/k = 14 => 28/k = 14 => k = 2. D = 8, U = 6. Stream = (8 - 6)/2 = 1 km/hr."),
            ("A circular running track is 600 m long. A and B start at the same time at speeds 15 m/s and 10 m/s in same direction. How many times will they cross in 10 minutes?", {"A": "5 times", "B": "4 times", "C": "6 times", "D": "8 times"}, "A", "Relative speed = 5 m/s. First meeting = 600/5 = 120 secs. In 10 mins (600 secs), meetings = 600 / 120 = 5 times."),
            ("A swimmer can swim in still water at 5 km/hr. If the river speed is 1 km/hr, it takes him 75 minutes to row to a place and back. How far is the place?", {"A": "3 km", "B": "2.5 km", "C": "4 km", "D": "3.5 km"}, "A", "D/6 + D/4 = 75/60 = 5/4 => 5D/12 = 5/4 => D = 3 km."),
            ("Three runners A, B, C run around a circular track of 12 km at 3 km/hr, 7 km/hr, and 13 km/hr in the same direction. When will they meet at the start point?", {"A": "12 hours", "B": "8 hours", "C": "6 hours", "D": "24 hours"}, "A", "Time for 1 lap: A=12/3=4 hrs, B=12/7 hrs, C=12/13 hrs. Meeting at start = LCM(4, 12/7, 12/13) = LCM(4, 12, 12) / HCF(1, 7, 13) = 12 / 1 = 12 hours.")
        ],
        10: [  # Permutations & Combinations
            ("In how many different ways can the letters of the word 'LEADING' be arranged so that the vowels always come together?", {"A": "720", "B": "5040", "C": "360", "D": "1440"}, "A", "Vowels: E, A, I (3 vowels). Treat (EAI) as 1 unit. Units: L, D, N, G + (EAI) = 5 units. Arrangements = 5! * 3! = 120 * 6 = 720."),
            ("In how many ways can a committee of 5 members be formed from 6 men and 4 women such that it contains at least 3 men?", {"A": "186", "B": "196", "C": "210", "D": "150"}, "A", "Cases: (3M, 2W): 6C3 * 4C2 = 20 * 6 = 120; (4M, 1W): 6C4 * 4C1 = 15 * 4 = 60; (5M, 0W): 6C5 * 4C0 = 6 * 1 = 6. Total = 120 + 60 + 6 = 186."),
            ("How many 3-digit numbers can be formed from the digits 2, 3, 5, 6, 7, and 9 without repetition?", {"A": "120", "B": "216", "C": "60", "D": "720"}, "A", "P(6, 3) = 6 * 5 * 4 = 120."),
            ("How many diagonals are there in a regular polygon with 12 sides (dodecagon)?", {"A": "54", "B": "60", "C": "48", "D": "66"}, "A", "Number of diagonals = n(n - 3) / 2 = 12 * 9 / 2 = 54."),
            ("In how many ways can 7 people be seated around a round dining table?", {"A": "720", "B": "5040", "C": "360", "D": "120"}, "A", "Circular permutations = (n - 1)! = (7 - 1)! = 6! = 720."),
            ("How many words can be formed using all the letters of the word 'MATHEMATICS'?", {"A": "4,989,600", "B": "2,494,800", "C": "39,916,800", "D": "1,247,400"}, "A", "Total letters = 11. Repeated: M=2, A=2, T=2. Arrangements = 11! / (2! * 2! * 2!) = 39,916,800 / 8 = 4,989,600."),
            ("Out of 7 consonants and 4 vowels, how many words of 3 consonants and 2 vowels can be formed?", {"A": "25,200", "B": "210", "C": "2,520", "D": "50,400"}, "A", "Selection = 7C3 * 4C2 = 35 * 6 = 210. Arrangement of 5 chosen letters = 5! = 120. Total words = 210 * 120 = 25,200."),
            ("At a party, everybody shakes hands with everybody else. If 66 handshakes took place, how many people were present?", {"A": "12", "B": "11", "C": "13", "D": "14"}, "A", "nC2 = 66 => n(n - 1) / 2 = 66 => n(n - 1) = 132. Since 12 * 11 = 132, n = 12 people."),
            ("In how many ways can 4 boys and 4 girls be arranged in a line so that boys and girls alternate?", {"A": "1,152", "B": "576", "C": "2,880", "D": "40,320"}, "A", "Pattern BGBGBGBG or GBGBGBGB (2 configurations). Each gives 4! * 4! = 24 * 24 = 576. Total = 2 * 576 = 1,152."),
            ("How many 4-letter code words can be formed using the first 10 letters of the English alphabet if no letter can be repeated?", {"A": "5,040", "B": "210", "C": "10,000", "D": "2,520"}, "A", "10 * 9 * 8 * 7 = 5,040.")
        ],
        11: [  # Probability
            ("Two dice are rolled simultaneously. What is the probability that the sum of the numbers appearing is 8?", {"A": "5/36", "B": "1/6", "C": "7/36", "D": "1/9"}, "A", "Favorable outcomes for sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5 outcomes. Total = 36. Probability = 5/36."),
            ("A card is drawn from a well-shuffled pack of 52 cards. What is the probability of getting a queen of spade or a king of diamond?", {"A": "1/26", "B": "1/52", "C": "2/13", "D": "1/13"}, "A", "Favorable = 1 queen of spades + 1 king of diamonds = 2 cards. Probability = 2/52 = 1/26."),
            ("A bag contains 6 red, 4 blue, and 2 green balls. If 2 balls are drawn at random, what is the probability that both are red?", {"A": "5/22", "B": "1/4", "C": "3/11", "D": "1/6"}, "A", "Total balls = 12. P(both red) = 6C2 / 12C2 = 15 / 66 = 5/22."),
            ("Three unbiased coins are tossed together. What is the probability of getting at least two heads?", {"A": "1/2", "B": "3/8", "C": "5/8", "D": "1/4"}, "A", "Sample space = 8. Favorable outcomes for at least 2 heads (HHH, HHT, HTH, THH) = 4. Probability = 4/8 = 1/2."),
            ("A problem in mathematics is given to three students whose chances of solving it are 1/2, 1/3, and 1/4. What is the probability that the problem is solved?", {"A": "3/4", "B": "1/24", "C": "23/24", "D": "1/2"}, "A", "P(problem not solved) = (1 - 1/2) * (1 - 1/3) * (1 - 1/4) = 1/2 * 2/3 * 3/4 = 1/4. P(solved) = 1 - 1/4 = 3/4."),
            ("What is the probability that a leap year selected at random will contain 53 Sundays?", {"A": "2/7", "B": "1/7", "C": "3/7", "D": "5/7"}, "A", "A leap year has 366 days = 52 weeks + 2 extra days. The 2 extra days can be (Sat,Sun) or (Sun,Mon) out of 7 pairs. Probability = 2/7."),
            ("Two cards are drawn together from a pack of 52 cards. Probability that one is a spade and one is a heart:", {"A": "13/102", "B": "1/4", "C": "1/16", "D": "26/102"}, "A", "(13C1 * 13C1) / 52C2 = (13 * 13) / 1,326 = 169 / 1,326 = 13 / 102."),
            ("A box contains 5 defective and 15 non-defective bulbs. Two bulbs are chosen at random. Probability that both are non-defective:", {"A": "21/38", "B": "9/19", "C": "1/2", "D": "15/38"}, "A", "15C2 / 20C2 = 105 / 190 = 21/38."),
            ("A bag contains 4 white, 5 red, and 6 blue balls. Three balls are drawn. Probability that none is red:", {"A": "24/91", "B": "12/91", "C": "35/91", "D": "15/91"}, "A", "Total = 15. Non-red = 10. Probability = 10C3 / 15C3 = 120 / 455 = 24/91."),
            ("If P(A) = 0.4, P(B) = 0.8, and P(B|A) = 0.6, what is P(A or B)?", {"A": "0.96", "B": "0.84", "C": "0.76", "D": "0.90"}, "A", "P(A and B) = P(A) * P(B|A) = 0.4 * 0.6 = 0.24. P(A or B) = P(A) + P(B) - P(A and B) = 0.4 + 0.8 - 0.24 = 0.96.")
        ],
        12: [  # Number Systems
            ("What is the remainder when 2^89 is divided by 89 (given that 89 is a prime number)?", {"A": "2", "B": "1", "C": "0", "D": "88"}, "A", "By Fermat's Little Theorem: a^p = a (mod p) for any prime p. Hence 2^89 = 2 (mod 89). Remainder is 2."),
            ("If a number 653xy is completely divisible by 80, what is the value of (x + y)?", {"A": "6", "B": "2", "C": "8", "D": "4"}, "A", "Divisible by 80 means divisible by 10 and 8. y must be 0. 653x0 is divisible by 8 => last 3 digits 3x0 divisible by 8 => 320 or 360 => x = 2 or 6. For x=6, y=0 => x+y=6."),
            ("The HCF of two numbers is 11 and their LCM is 693. If one of the numbers is 77, what is the other number?", {"A": "99", "B": "88", "C": "101", "D": "91"}, "A", "Product of two numbers = HCF * LCM => 77 * N = 11 * 693 => N = 7623 / 77 = 99."),
            ("How many trailing zeros are there at the end of 100! (factorial of 100)?", {"A": "24", "B": "25", "C": "20", "D": "22"}, "A", "Legendre's formula: floor(100/5) + floor(100/25) = 20 + 4 = 24 trailing zeros."),
            ("What is the unit digit in the product (7^95 - 3^58)?", {"A": "4", "B": "6", "C": "0", "D": "2"}, "A", "Cyclicity of 7 is 4: 95 mod 4 = 3 => 7^3 ends in 3. Cyclicity of 3 is 4: 58 mod 4 = 2 => 3^2 ends in 9. Unit digit = 13 - 9 = 4."),
            ("What is the smallest number which when divided by 12, 15, and 20 leaves remainder 4 in each case?", {"A": "64", "B": "124", "C": "60", "D": "56"}, "A", "LCM(12, 15, 20) = 60. Required number = LCM + 4 = 60 + 4 = 64."),
            ("The sum of two numbers is 528 and their HCF is 33. How many such pairs of numbers exist?", {"A": "4 pairs", "B": "6 pairs", "C": "8 pairs", "D": "2 pairs"}, "A", "Let numbers be 33a and 33b where a, b are co-prime. 33(a + b) = 528 => a + b = 16. Co-prime pairs summing to 16: (1, 15), (3, 13), (5, 11), (7, 9) = 4 pairs."),
            ("Find the largest number of four digits which is exactly divisible by 15, 25, 40, and 75:", {"A": "9,600", "B": "9,000", "C": "9,400", "D": "9,800"}, "A", "LCM(15, 25, 40, 75) = 600. Largest 4-digit number = 9999. 9999 mod 600 = 399. Required = 9999 - 399 = 9,600."),
            ("What is the remainder when (67^67 + 67) is divided by 68?", {"A": "66", "B": "67", "C": "0", "D": "1"}, "A", "67 = -1 (mod 68). (-1)^67 + (-1) = -1 - 1 = -2 = 66 (mod 68). Remainder is 66."),
            ("How many positive factors does the number 360 have?", {"A": "24", "B": "18", "C": "12", "D": "30"}, "A", "360 = 2^3 * 3^2 * 5^1. Number of factors = (3 + 1) * (2 + 1) * (1 + 1) = 4 * 3 * 2 = 24.")
        ],
        13: [  # Syllogisms
            ("Statements: All mangoes are golden. All golden things are cheap. Conclusions: I. All mangoes are cheap. II. Golden things are mangoes.", {"A": "Only conclusion I follows", "B": "Only conclusion II follows", "C": "Either I or II follows", "D": "Neither follows"}, "A", "All M are G, and all G are C => All M are C (Conclusion I valid). Conversion of 'All M are G' is 'Some G are M', so II is invalid."),
            ("Statements: Some dogs are cats. Some cats are rats. Conclusions: I. Some dogs are rats. II. No dog is rat.", {"A": "Either I or II follows", "B": "Only I follows", "C": "Only II follows", "D": "Both follow"}, "A", "I and II form a complementary pair (Particular Affirmative + Universal Negative on same subjects). Hence either I or II must follow."),
            ("Statements: All books are pens. No pen is pencil. Conclusions: I. No book is pencil. II. All pens are books.", {"A": "Only conclusion I follows", "B": "Only conclusion II follows", "C": "Both follow", "D": "Neither follows"}, "A", "Since books are inside pens and pens are disjoint from pencils, no book can ever be a pencil. Conclusion I follows."),
            ("Statements: Some cars are bikes. All bikes are trains. Conclusions: I. Some cars are trains. II. All trains are bikes.", {"A": "Only I follows", "B": "Only II follows", "C": "Both follow", "D": "Neither follows"}, "A", "The intersection of cars and bikes is entirely within trains, so Some cars are trains is true. All trains are bikes is not necessarily true."),
            ("Statements: No apple is orange. All oranges are bananas. Conclusions: I. Some bananas are oranges. II. Some bananas are not apples.", {"A": "Both conclusions I and II follow", "B": "Only I follows", "C": "Only II follows", "D": "Neither follows"}, "A", "Conversion of 'All O are B' gives 'Some B are O' (I follows). The bananas that are oranges can never be apples (II follows)."),
            ("Statements: All flowers are trees. No tree is fruit. Conclusions: I. No flower is fruit. II. Some trees are flowers.", {"A": "Both I and II follow", "B": "Only I follows", "C": "Only II follows", "D": "Neither follows"}, "A", "Flowers are entirely inside trees, which do not overlap fruit, so no flower is fruit. Also trees contain flowers."),
            ("Statements: Some papers are bottles. Some bottles are bags. Conclusions: I. Some papers are bags. II. No paper is bag.", {"A": "Either I or II follows", "B": "Only I follows", "C": "Neither follows", "D": "Both follow"}, "A", "Complementary pair 'Some' and 'No' with the same subject and predicate terms under ambiguous premises forms an Either-Or relationship."),
            ("Statements: All windows are doors. No door is wall. Conclusions: I. No window is wall. II. No wall is door.", {"A": "Both I and II follow", "B": "Only I follows", "C": "Only II follows", "D": "Neither follows"}, "A", "Windows are inside doors. Doors have no overlap with walls, so neither windows nor doors touch walls."),
            ("Statements: Some actors are singers. All singers are dancers. Conclusions: I. Some actors are dancers. II. No singer is actor.", {"A": "Only I follows", "B": "Only II follows", "C": "Both follow", "D": "Neither follows"}, "A", "Actors overlap singers, all of whom are dancers; hence some actors are dancers. II contradicts premise."),
            ("Statements: All roads are streets. No street is lane. Conclusions: I. No road is lane. II. Some streets are roads.", {"A": "Both I and II follow", "B": "Only I follows", "C": "Only II follows", "D": "Neither follows"}, "A", "Roads are a subset of streets. Since no street is a lane, no road can be a lane. Also, streets overlap roads.")
        ],
        14: [  # Blood Relations
            ("Pointing to a photograph of a boy, Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?", {"A": "Father", "B": "Brother", "C": "Uncle", "D": "Grandfather"}, "A", "'Only son of my mother' is Suresh himself. Therefore, the boy is the son of Suresh. Suresh is his father."),
            ("If A + B means A is the brother of B; A - B means A is the sister of B; and A * B means A is the father of B. Which of the following means that C is the son of M?", {"A": "M * C + N", "B": "M - C + N", "C": "M * N - C", "D": "C * M + N"}, "A", "M * C means M is father of C. C + N means C is brother (male). Hence C is the son of M."),
            ("Introducing a girl, Vipin said, 'Her mother is the only daughter of my mother-in-law.' How is Vipin related to the girl?", {"A": "Father", "B": "Uncle", "C": "Brother", "D": "Husband"}, "A", "'Only daughter of my mother-in-law' is Vipin's wife. The girl's mother is Vipin's wife, so Vipin is her father."),
            ("A man said to a lady, 'Your mother's husband's sister is my aunt.' How is the lady related to the man?", {"A": "Sister", "B": "Mother", "C": "Daughter", "D": "Aunt"}, "A", "Lady's mother's husband is lady's father. Father's sister is lady's aunt. Since she is also the man's aunt, the lady is the man's sister."),
            ("Pointing to a woman, Naman said, 'She is the daughter of the only child of my grandfather.' How is the woman related to Naman?", {"A": "Sister", "B": "Niece", "C": "Mother", "D": "Aunt"}, "A", "'Only child of my grandfather' is Naman's father. The daughter of Naman's father is Naman's sister."),
            ("Deepak said to Nitin, 'That boy playing with football is the younger of the two brothers of the daughter of my father's wife.' Who is the boy to Deepak?", {"A": "Brother", "B": "Cousin", "C": "Nephew", "D": "Son"}, "A", "'Father's wife' = mother. 'Daughter of mother' = sister. 'Brother of sister' = brother. The boy is Deepak's brother."),
            ("P is the brother of Q and R. S is R's mother. T is P's father. Which of the following statements cannot be definitely true?", {"A": "T is Q's father", "B": "S is P's mother", "C": "Q is T's son", "D": "P is S's son"}, "C", "Q's gender is not specified in the premises; Q could be a son or a daughter."),
            ("A is B's sister. C is B's mother. D is C's father. E is D's mother. Then how is A related to D?", {"A": "Granddaughter", "B": "Grandmother", "C": "Daughter", "D": "Grandfather"}, "A", "A is sister of B, whose mother is C (A is C's daughter). D is C's father, so A is D's granddaughter."),
            ("Pointing to a gentleman, Deepak said, 'His only brother is the father of my daughter's father.' How is the gentleman related to Deepak?", {"A": "Uncle", "B": "Father", "C": "Grandfather", "D": "Brother-in-law"}, "A", "'My daughter's father' = Deepak. 'Father of Deepak' = Deepak's father. The gentleman's only brother is Deepak's father, making the gentleman Deepak's uncle."),
            ("If 'P $ Q' means P is father of Q; 'P # Q' means P is mother of Q; 'P * Q' means P is sister of Q. In N # L $ P * Q, how is N related to Q?", {"A": "Paternal Grandmother", "B": "Maternal Grandmother", "C": "Aunt", "D": "Mother"}, "A", "L is father of P and Q. N is mother of L. Hence N is the paternal grandmother of Q.")
        ],
        15: [  # Direction Sense
            ("A man walks 5 km East, then turns right and walks 4 km, then turns left and walks 5 km. Which direction is he from his starting point?", {"A": "South-East", "B": "North-East", "C": "South-West", "D": "North-West"}, "A", "Net displacement: East = 5 + 5 = 10 km; South = 4 km. He is in the South-East direction."),
            ("One morning after sunrise, Suresh was standing facing a pole. The shadow of the pole fell exactly to his right. Which direction was he facing?", {"A": "South", "B": "North", "C": "East", "D": "West"}, "A", "In the morning, the sun rises in the East, so all shadows point West. If the shadow is to Suresh's right, his right is West, meaning he is facing South."),
            ("Rohan walks 12 km North, then 5 km West. How far and in which direction is he from his starting point?", {"A": "13 km North-West", "B": "13 km North-East", "C": "17 km North-West", "D": "7 km North"}, "A", "By Pythagorean theorem: d = sqrt(12^2 + 5^2) = sqrt(144 + 25) = sqrt(169) = 13 km. Direction is North-West."),
            ("A person travels 7 km toward South, turns left and walks 5 km, then turns left and walks 7 km. How far is he from starting point?", {"A": "5 km East", "B": "5 km West", "C": "14 km South", "D": "12 km East"}, "A", "Moving 7 km South then 7 km North cancels the vertical displacement, leaving 5 km East."),
            ("One evening before sunset, Rekha and Hema were talking face to face. If Hema's shadow was exactly to the right of Hema, which direction was Rekha facing?", {"A": "South", "B": "North", "C": "East", "D": "West"}, "A", "At sunset, sun is in West, so shadows fall East. If Hema's shadow falls to her right, Hema's right is East => Hema faces North. Rekha is facing Hema => Rekha faces South."),
            ("A clock shows 4:30. If the minute hand points towards East, in which direction will the hour hand point?", {"A": "North-East", "B": "South-East", "C": "North-West", "D": "South-West"}, "A", "At 4:30, minute hand is at 6 (normally South). If South is designated East (90 deg counter-clockwise), then the hour hand between 4 and 5 (normally South-East) rotates to North-East."),
            ("Starting from point X, Jayant walked 15 m West. He turned left and walked 20 m. He then turned left and walked 15 m. How far is he from X?", {"A": "20 m", "B": "15 m", "C": "35 m", "D": "25 m"}, "A", "The West 15 m and East 15 m cancel, leaving a direct distance of 20 m South of X."),
            ("A car travels 8 km North, turns right and drives 6 km. What is the shortest Euclidean distance from the starting position?", {"A": "10 km", "B": "14 km", "C": "12 km", "D": "8 km"}, "A", "Shortest distance = sqrt(8^2 + 6^2) = sqrt(64 + 36) = sqrt(100) = 10 km."),
            ("K is 40 m South-West of L. M is 40 m South-East of L. What is the direction of M with respect to K?", {"A": "East", "B": "West", "C": "North", "D": "South"}, "A", "K is at (-40/sqrt2, -40/sqrt2) and M is at (+40/sqrt2, -40/sqrt2). Both have equal negative y-coordinates, so M is directly East of K."),
            ("If North-East becomes North, and North-West becomes West, what will South become?", {"A": "South-East", "B": "South-West", "C": "North-West", "D": "East"}, "A", "The entire compass rotates 45 degrees counter-clockwise. South rotates 45 degrees CCW to South-East.")
        ]
    }
    
    if day in banks:
        mcqs = []
        for i, item in enumerate(banks[day], 1):
            mcqs.append({
                "mcq_no": i,
                "question": item[0],
                "options": item[1],
                "correct_answer": item[2],
                "explanation": item[3],
                "target_time_seconds": 60,
                "category": "Quantitative" if day <= 12 else "Logical Reasoning"
            })
        return mcqs
    return []
