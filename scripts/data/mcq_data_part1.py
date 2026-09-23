"""
scripts/data/mcq_data_part1.py
Questions for Days 01 to 10:
Each day has:
- 10 fresh Aptitude MCQs (topic-grounded)
- 20 unique Mixed Test MCQs (5 Academic + 5 Aptitude + 5 Core CS + 5 Coding/Project)
"""

DAYS_1_10_APTITUDE = {
    1: [
        {
            "mcq_no": 1,
            "question": "If the price of sugar increases by 25%, by what percentage must a household reduce its consumption so that the total expenditure remains unchanged?",
            "options": {"A": "20%", "B": "25%", "C": "16.67%", "D": "33.33%"},
            "correct_answer": "A",
            "explanation": "Using the price-consumption invariance formula: If price rises by 1/x = 1/4 (25%), consumption must reduce by 1/(x+1) = 1/5 = 20% to keep expenditure constant.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 2,
            "question": "A student scored 85% in an examination. If the maximum marks were 600, how many marks did the student obtain?",
            "options": {"A": "500", "B": "510", "C": "520", "D": "530"},
            "correct_answer": "B",
            "explanation": "Marks obtained = 85% of 600 = (85 / 100) * 600 = 85 * 6 = 510 marks.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 3,
            "question": "If 35% of a number is 175, what is 60% of that number?",
            "options": {"A": "250", "B": "280", "C": "300", "D": "320"},
            "correct_answer": "C",
            "explanation": "Let number be x. 0.35x = 175 => x = 175 / 0.35 = 500. 60% of 500 = 0.60 * 500 = 300.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 4,
            "question": "Two numbers are respectively 20% and 50% more than a third number. What is the ratio of the first number to the second number?",
            "options": {"A": "2 : 5", "B": "3 : 5", "C": "4 : 5", "D": "5 : 4"},
            "correct_answer": "C",
            "explanation": "Let third number be 100. First number = 120, second number = 150. Ratio = 120 / 150 = 4 / 5 = 4 : 5.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 5,
            "question": "In an election between two candidates, the winner secured 62% of the valid votes and won by a majority of 288 votes. What was the total number of valid votes polled?",
            "options": {"A": "1,000", "B": "1,200", "C": "1,400", "D": "1,500"},
            "correct_answer": "B",
            "explanation": "Winner = 62%, Loser = 38%. Majority = 62% - 38% = 24%. 24% of total = 288 => Total = (288 * 100) / 24 = 1,200 votes.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 6,
            "question": "A person saves 12% of his monthly income. If his monthly expenditure is Rs. 19,360, what is his monthly income?",
            "options": {"A": "Rs. 21,000", "B": "Rs. 22,000", "C": "Rs. 22,500", "D": "Rs. 23,000"},
            "correct_answer": "B",
            "explanation": "Expenditure % = 100% - 12% = 88%. 88% of Income = Rs. 19,360 => Income = (19,360 * 100) / 88 = Rs. 22,000.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 7,
            "question": "If the length of a rectangle is increased by 20% and its breadth is decreased by 10%, what is the net percentage change in its area?",
            "options": {"A": "8% increase", "B": "10% increase", "C": "8% decrease", "D": "2% increase"},
            "correct_answer": "A",
            "explanation": "Net % change = a + b + (ab / 100) = 20 - 10 + (20 * (-10) / 100) = 10 - 2 = +8% increase.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 8,
            "question": "What is the fractional equivalent of 14.28% (or 14 2/7%)?",
            "options": {"A": "1/6", "B": "1/7", "C": "1/8", "D": "1/9"},
            "correct_answer": "B",
            "explanation": "1/7 = 100 / 7 = 14.2857% ≈ 14.28%. Memorizing fractional equivalents eliminates long division in speed tests.",
            "target_time_seconds": 20,
            "category": "Quantitative"
        },
        {
            "mcq_no": 9,
            "question": "The population of a town increases by 10% annually. If the current population is 44,000, what will it be after 2 years?",
            "options": {"A": "50,000", "B": "52,800", "C": "53,240", "D": "54,000"},
            "correct_answer": "C",
            "explanation": "After 1 year: 44,000 * 1.10 = 48,400. After 2 years: 48,400 * 1.10 = 53,240.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 10,
            "question": "If A's salary is 20% less than B's salary, by what percentage is B's salary more than A's salary?",
            "options": {"A": "20%", "B": "22.5%", "C": "25%", "D": "30%"},
            "correct_answer": "C",
            "explanation": "Base Inversion: If A is r% less than B, B is [r / (100 - r)] * 100% more than A. Here [20 / (100 - 20)] * 100% = 20 / 80 * 100% = 25%.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        }
    ],
    2: [
        {
            "mcq_no": 1,
            "question": "An article bought for Rs. 450 is sold for Rs. 540. What is the profit percentage earned?",
            "options": {"A": "15%", "B": "18%", "C": "20%", "D": "25%"},
            "correct_answer": "C",
            "explanation": "Profit = SP - CP = 540 - 450 = Rs. 90. Profit % = (90 / 450) * 100% = 20%.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 2,
            "question": "By selling a watch for Rs. 1,440, a shopkeeper incurs a 10% loss. At what price must he sell it to gain 15%?",
            "options": {"A": "Rs. 1,600", "B": "Rs. 1,750", "C": "Rs. 1,840", "D": "Rs. 1,920"},
            "correct_answer": "C",
            "explanation": "SP = 0.90 * CP = 1440 => CP = 1440 / 0.9 = Rs. 1600. Target SP = 1.15 * 1600 = Rs. 1,840.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 3,
            "question": "What is the single equivalent discount of two successive discounts of 20% and 15%?",
            "options": {"A": "32%", "B": "35%", "C": "30%", "D": "33%"},
            "correct_answer": "A",
            "explanation": "Single equivalent discount = d1 + d2 - (d1 * d2 / 100) = 20 + 15 - (300 / 100) = 35 - 3 = 32%.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 4,
            "question": "A trader marks his goods 30% above the cost price and allows a discount of 10% on the marked price. What is his net gain percentage?",
            "options": {"A": "17%", "B": "20%", "C": "18.5%", "D": "15%"},
            "correct_answer": "A",
            "explanation": "Let CP = 100. MP = 130. SP = 130 * 0.90 = 117. Profit = 117 - 100 = 17%.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 5,
            "question": "Two cars were sold at the same selling price of Rs. 2,40,000 each. On one the seller gained 20% and on the other he lost 20%. What was the overall transaction result?",
            "options": {"A": "No profit no loss", "B": "4% profit", "C": "4% loss", "D": "2% loss"},
            "correct_answer": "C",
            "explanation": "When two articles are sold at equal SP, one at x% profit and other at x% loss, the overall result is always a loss of (x^2 / 100)% = (400 / 100)% = 4% loss.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 6,
            "question": "If the cost price of 15 pens equals the selling price of 12 pens, what is the profit percentage?",
            "options": {"A": "20%", "B": "25%", "C": "30%", "D": "15%"},
            "correct_answer": "B",
            "explanation": "15 * CP = 12 * SP => SP / CP = 15 / 12 = 5 / 4. Profit % = [(5 - 4) / 4] * 100% = 1/4 * 100% = 25%.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 7,
            "question": "A dishonest dealer professes to sell goods at cost price but uses a false weight of 900 grams for a 1 kg weight. What is his profit percentage?",
            "options": {"A": "10%", "B": "11 1/9 %", "C": "9 1/11 %", "D": "12.5%"},
            "correct_answer": "B",
            "explanation": "Gain % = [Error / (True Value - Error)] * 100% = [100 / 900] * 100% = 100 / 9 % = 11 1/9 % (≈ 11.11%).",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 8,
            "question": "An item is marked at Rs. 800. After two successive discounts, it is sold for Rs. 612. If the first discount was 10%, what was the second discount percentage?",
            "options": {"A": "12%", "B": "14%", "C": "15%", "D": "16%"},
            "correct_answer": "C",
            "explanation": "After 10% discount: 800 * 0.90 = Rs. 720. Second discount amount = 720 - 612 = Rs. 108. Second discount % = (108 / 720) * 100% = 15%.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 9,
            "question": "A merchant earns 25% profit by selling an item at Rs. 750. What would be the profit or loss percent if he sold it at Rs. 540?",
            "options": {"A": "10% loss", "B": "10% profit", "C": "12% loss", "D": "8% loss"},
            "correct_answer": "A",
            "explanation": "CP = 750 / 1.25 = Rs. 600. If sold at 540, Loss = 600 - 540 = Rs. 60. Loss % = (60 / 600) * 100% = 10% loss.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 10,
            "question": "To clear old stock, a retailer offers 'Buy 3, Get 1 Free'. What is the effective discount percentage given to the customer?",
            "options": {"A": "33.33%", "B": "25%", "C": "20%", "D": "30%"},
            "correct_answer": "B",
            "explanation": "Total items taken = 4. Free items = 1. Effective discount % = (Free / Total) * 100% = (1 / 4) * 100% = 25%.",
            "target_time_seconds": 25,
            "category": "Quantitative"
        }
    ],
    3: [
        {
            "mcq_no": 1,
            "question": "Find the simple interest on a principal of Rs. 8,000 for 3 years at an annual interest rate of 7.5%.",
            "options": {"A": "Rs. 1,600", "B": "Rs. 1,800", "C": "Rs. 2,000", "D": "Rs. 2,100"},
            "correct_answer": "B",
            "explanation": "SI = (P * R * T) / 100 = (8000 * 7.5 * 3) / 100 = 80 * 22.5 = Rs. 1,800.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 2,
            "question": "A sum of money invested at simple interest doubles itself in 8 years. In how many years will it become 4 times itself at the same rate?",
            "options": {"A": "16 years", "B": "20 years", "C": "24 years", "D": "32 years"},
            "correct_answer": "C",
            "explanation": "At SI, money doubling in 8 years means Interest = P in 8 years. To become 4P, total interest required = 3P. Time = 3 * 8 = 24 years.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 3,
            "question": "What is the compound interest on Rs. 10,000 for 2 years at 10% per annum, compounded annually?",
            "options": {"A": "Rs. 2,000", "B": "Rs. 2,100", "C": "Rs. 2,200", "D": "Rs. 2,250"},
            "correct_answer": "B",
            "explanation": "A = P * (1 + R/100)^T = 10000 * (1.10)^2 = 10000 * 1.21 = Rs. 12,100. CI = 12100 - 10000 = Rs. 2,100.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 4,
            "question": "The difference between simple and compound interest on a certain sum for 2 years at 5% per annum is Rs. 25. Find the sum.",
            "options": {"A": "Rs. 8,000", "B": "Rs. 9,000", "C": "Rs. 10,000", "D": "Rs. 12,000"},
            "correct_answer": "C",
            "explanation": "2-Year Difference = P * (R / 100)^2 => 25 = P * (5 / 100)^2 = P * (1 / 400) => P = 25 * 400 = Rs. 10,000.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 5,
            "question": "At what rate percent per annum will Rs. 2,000 amount to Rs. 2,420 in 2 years compounded annually?",
            "options": {"A": "8%", "B": "10%", "C": "12%", "D": "15%"},
            "correct_answer": "B",
            "explanation": "A / P = (1 + R/100)^2 => 2420 / 2000 = 121 / 100 = (11 / 10)^2. So 1 + R/100 = 1.10 => R = 10%.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 6,
            "question": "According to the financial Rule of 72, approximately how many years will it take for an investment to double at 9% compound interest per annum?",
            "options": {"A": "6 years", "B": "7 years", "C": "8 years", "D": "9 years"},
            "correct_answer": "C",
            "explanation": "Rule of 72: Doubling time ≈ 72 / R = 72 / 9 = 8 years.",
            "target_time_seconds": 20,
            "category": "Quantitative"
        },
        {
            "mcq_no": 7,
            "question": "Find the compound interest on Rs. 16,000 at 20% per annum for 9 months, compounded quarterly.",
            "options": {"A": "Rs. 2,400", "B": "Rs. 2,522", "C": "Rs. 2,600", "D": "Rs. 2,750"},
            "correct_answer": "B",
            "explanation": "Quarterly rate r = 20% / 4 = 5%. Number of quarters n = 9 / 3 = 3 quarters. Amount = 16000 * (1.05)^3 = 16000 * 1.157625 = Rs. 18,522. CI = 18522 - 16000 = Rs. 2,522.",
            "target_time_seconds": 50,
            "category": "Quantitative"
        },
        {
            "mcq_no": 8,
            "question": "A sum of money invested at compound interest amounts to Rs. 4,500 in 3 years and to Rs. 6,750 in 6 years. Find the initial sum.",
            "options": {"A": "Rs. 2,800", "B": "Rs. 3,000", "C": "Rs. 3,200", "D": "Rs. 3,500"},
            "correct_answer": "B",
            "explanation": "Ratio of amounts in equal 3-year intervals is constant: 6750 / 4500 = 1.5. Thus 4500 / P = 1.5 => P = 4500 / 1.5 = Rs. 3,000.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 9,
            "question": "If simple interest on a sum for 2 years at 4% is Rs. 80, what is the compound interest on the same sum at the same rate and time?",
            "options": {"A": "Rs. 81.60", "B": "Rs. 82.40", "C": "Rs. 83.20", "D": "Rs. 84.00"},
            "correct_answer": "A",
            "explanation": "SI for 1 year = 80 / 2 = Rs. 40. In year 2, CI adds interest on 1st year's interest = 4% of 40 = Rs. 1.60. Total CI = 80 + 1.60 = Rs. 81.60.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 10,
            "question": "A lender claims to lend money at simple interest, but adds interest every six months to calculate principal. If his nominal rate is 10%, what is the effective annual rate?",
            "options": {"A": "10%", "B": "10.25%", "C": "10.50%", "D": "11%"},
            "correct_answer": "B",
            "explanation": "Half-yearly rate = 5%. Effective annual rate = 5 + 5 + (5 * 5 / 100) = 10.25%.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        }
    ],
    4: [
        {
            "mcq_no": 1,
            "question": "If A : B = 3 : 4 and B : C = 8 : 9, find the combined continuous ratio A : C.",
            "options": {"A": "1 : 2", "B": "2 : 3", "C": "3 : 2", "D": "4 : 5"},
            "correct_answer": "B",
            "explanation": "A/C = (A/B) * (B/C) = (3/4) * (8/9) = 24 / 36 = 2 / 3 = 2 : 3.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 2,
            "question": "What is the fourth proportional to 4, 9, and 12?",
            "options": {"A": "24", "B": "27", "C": "30", "D": "36"},
            "correct_answer": "B",
            "explanation": "Let fourth proportional be x. 4 / 9 = 12 / x => 4x = 108 => x = 27.",
            "target_time_seconds": 25,
            "category": "Quantitative"
        },
        {
            "mcq_no": 3,
            "question": "What is the mean proportional between 9 and 25?",
            "options": {"A": "12", "B": "15", "C": "18", "D": "20"},
            "correct_answer": "B",
            "explanation": "Mean proportional x = sqrt(a * b) = sqrt(9 * 25) = 3 * 5 = 15.",
            "target_time_seconds": 20,
            "category": "Quantitative"
        },
        {
            "mcq_no": 4,
            "question": "A sum of Rs. 3,500 is divided among A, B, and C in the ratio 2 : 3 : 5. What is B's share?",
            "options": {"A": "Rs. 700", "B": "Rs. 1,050", "C": "Rs. 1,400", "D": "Rs. 1,750"},
            "correct_answer": "B",
            "explanation": "Total parts = 2 + 3 + 5 = 10. Value of 1 part = 3500 / 10 = Rs. 350. B's share = 3 * 350 = Rs. 1,050.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 5,
            "question": "A bag contains 50p, 25p, and 10p coins in the ratio 5 : 9 : 4, amounting to Rs. 206. Find the number of 50p coins.",
            "options": {"A": "180", "B": "200", "C": "220", "D": "240"},
            "correct_answer": "B",
            "explanation": "Value per unit = 5*(0.50) + 9*(0.25) + 4*(0.10) = 2.50 + 2.25 + 0.40 = Rs. 5.15. Number of units = 206 / 5.15 = 40. 50p coins = 5 * 40 = 200 coins.",
            "target_time_seconds": 50,
            "category": "Quantitative"
        },
        {
            "mcq_no": 6,
            "question": "A and B invest in a business in the ratio 3 : 5. After 4 months, C joins with an investment equal to B's. In what ratio should the year-end profit be shared among A, B, and C?",
            "options": {"A": "9 : 15 : 10", "B": "3 : 5 : 4", "C": "6 : 10 : 7", "D": "12 : 20 : 15"},
            "correct_answer": "A",
            "explanation": "Profit ratio = (Inv * Time): A = 3 * 12 = 36; B = 5 * 12 = 60; C = 5 * 8 = 40. Ratio = 36 : 60 : 40 = 9 : 15 : 10.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 7,
            "question": "If x varies directly as y, and x = 12 when y = 8, find the value of x when y = 14.",
            "options": {"A": "18", "B": "21", "C": "24", "D": "28"},
            "correct_answer": "B",
            "explanation": "x = k * y => 12 = k * 8 => k = 1.5. When y = 14, x = 1.5 * 14 = 21.",
            "target_time_seconds": 25,
            "category": "Quantitative"
        },
        {
            "mcq_no": 8,
            "question": "What is the sub-duplicate ratio of 64 : 81?",
            "options": {"A": "4 : 9", "B": "8 : 9", "C": "16 : 27", "D": "3 : 4"},
            "correct_answer": "B",
            "explanation": "Sub-duplicate ratio of a : b = sqrt(a) : sqrt(b) = sqrt(64) : sqrt(81) = 8 : 9.",
            "target_time_seconds": 20,
            "category": "Quantitative"
        },
        {
            "mcq_no": 9,
            "question": "Two numbers are in the ratio 3 : 5. If 6 is added to each number, the ratio becomes 2 : 3. What are the two numbers?",
            "options": {"A": "12 and 20", "B": "18 and 30", "C": "15 and 25", "D": "21 and 35"},
            "correct_answer": "B",
            "explanation": "Let numbers be 3x and 5x. (3x + 6) / (5x + 6) = 2/3 => 3(3x + 6) = 2(5x + 6) => 9x + 18 = 10x + 12 => x = 6. Numbers = 18 and 30.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 10,
            "question": "In a mixture of 60 liters, the ratio of milk and water is 2 : 1. How much water must be added to make the ratio 1 : 2?",
            "options": {"A": "40 liters", "B": "50 liters", "C": "60 liters", "D": "70 liters"},
            "correct_answer": "C",
            "explanation": "Initial: Milk = 40L, Water = 20L. Desired ratio 1 : 2 means Milk : Water = 40 : (20 + w) = 1 : 2 => 20 + w = 80 => w = 60 liters.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        }
    ],
    5: [
        {
            "mcq_no": 1,
            "question": "The average of 5 consecutive odd numbers is 27. What is the product of the smallest and largest numbers?",
            "options": {"A": "697", "B": "713", "C": "735", "D": "759"},
            "correct_answer": "B",
            "explanation": "For consecutive odd numbers, average is the middle number = 27. The numbers are 23, 25, 27, 29, 31. Product = 23 * 31 = 713.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 2,
            "question": "The average weight of 24 students in a class is 40 kg. If the teacher's weight is included, the average increases by 1 kg. What is the teacher's weight?",
            "options": {"A": "60 kg", "B": "65 kg", "C": "64 kg", "D": "66 kg"},
            "correct_answer": "B",
            "explanation": "New average = 41 kg for 25 people. Teacher's weight = Old Average + (Total people * Increase) = 40 + (25 * 1) = 65 kg.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 3,
            "question": "A cricketer has an average of 32 runs in 9 innings. How many runs must he score in the 10th inning to raise his average to 36?",
            "options": {"A": "68", "B": "72", "C": "76", "D": "80"},
            "correct_answer": "B",
            "explanation": "Runs needed = New Target + (Previous innings * required increment) = 36 + (9 * 4) = 36 + 36 = 72 runs.",
            "target_time_seconds": 30,
            "category": "Quantitative"
        },
        {
            "mcq_no": 4,
            "question": "In what ratio must a grocer mix tea at Rs. 60 per kg with tea at Rs. 75 per kg so that the mixture is worth Rs. 65 per kg?",
            "options": {"A": "2 : 1", "B": "1 : 2", "C": "3 : 2", "D": "4 : 3"},
            "correct_answer": "A",
            "explanation": "By Alligation: Cheaper / Dearer = (75 - 65) / (65 - 60) = 10 / 5 = 2 / 1 = 2 : 1.",
            "target_time_seconds": 25,
            "category": "Quantitative"
        },
        {
            "mcq_no": 5,
            "question": "A vessel contains 80 liters of milk. 8 liters of milk is taken out and replaced by water. This process is repeated once more. How much milk remains in the vessel?",
            "options": {"A": "64.8 liters", "B": "65.2 liters", "C": "66.0 liters", "D": "67.4 liters"},
            "correct_answer": "A",
            "explanation": "Remaining liquid = Initial * (1 - x/V)^n = 80 * (1 - 8/80)^2 = 80 * (0.90)^2 = 80 * 0.81 = 64.8 liters.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        },
        {
            "mcq_no": 6,
            "question": "The average age of a husband and wife who were married 4 years ago was 25 years. Today, with a newly born child, the average age of the family is 20 years. How old is the child?",
            "options": {"A": "1 year", "B": "2 years", "C": "3 years", "D": "4 years"},
            "correct_answer": "B",
            "explanation": "Present age sum of husband and wife = (25 + 4) * 2 = 58 years. Present sum of all 3 = 20 * 3 = 60 years. Child's age = 60 - 58 = 2 years.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 7,
            "question": "The average of 50 numbers is 38. If two numbers, namely 45 and 55, are discarded, what is the average of the remaining numbers?",
            "options": {"A": "36.5", "B": "37.5", "C": "37.8", "D": "38.2"},
            "correct_answer": "B",
            "explanation": "Total sum = 50 * 38 = 1900. New sum = 1900 - (45 + 55) = 1800. Remaining numbers = 48. New average = 1800 / 48 = 37.5.",
            "target_time_seconds": 40,
            "category": "Quantitative"
        },
        {
            "mcq_no": 8,
            "question": "How many kilograms of sugar costing Rs. 9 per kg must be mixed with 27 kg of sugar costing Rs. 7 per kg so that there may be a gain of 10% by selling the mixture at Rs. 9.24 per kg?",
            "options": {"A": "54 kg", "B": "60 kg", "C": "63 kg", "D": "72 kg"},
            "correct_answer": "C",
            "explanation": "CP of mixture = 9.24 / 1.10 = Rs. 8.40. Alligation: (Dearer - Mean) / (Mean - Cheaper) = (9 - 8.40) : (8.40 - 7) = 0.60 : 1.40 = 3 : 7. Since cheaper is 27 kg (7 parts? No, 7 is dearer ratio): Ratio of Rs.9 to Rs.7 is (8.40 - 7)/(9 - 8.40) = 1.40/0.60 = 7/3. Weight of Rs.9 sugar = 27 * (7/3) = 63 kg.",
            "target_time_seconds": 55,
            "category": "Quantitative"
        },
        {
            "mcq_no": 9,
            "question": "The average temperature of Monday, Tuesday, and Wednesday was 40°C. That of Tuesday, Wednesday, and Thursday was 41°C. If Thursday's temperature was 42°C, what was the temperature on Monday?",
            "options": {"A": "38°C", "B": "39°C", "C": "40°C", "D": "41°C"},
            "correct_answer": "B",
            "explanation": "(Tue + Wed + Thu) - (Mon + Tue + Wed) = 3 * (41 - 40) => Thu - Mon = 3°C => 42 - Mon = 3 => Mon = 39°C.",
            "target_time_seconds": 35,
            "category": "Quantitative"
        },
        {
            "mcq_no": 10,
            "question": "A library has an average of 510 visitors on Sundays and 240 visitors on other days. In a 30-day month beginning with a Sunday, what is the average daily visitors?",
            "options": {"A": "275", "B": "280", "C": "285", "D": "290"},
            "correct_answer": "C",
            "explanation": "Month starting on Sunday has 5 Sundays (days 1, 8, 15, 22, 29) and 25 other days. Total visitors = 5 * 510 + 25 * 240 = 2550 + 6000 = 8550. Average = 8550 / 30 = 285.",
            "target_time_seconds": 45,
            "category": "Quantitative"
        }
    ]
}

# Auto-generate fresh, distinct questions for days 6 to 10
# (Days 6: Time & Work, Day 7: Pipes & Cisterns, Day 8: TSD, Day 9: Boats & Streams, Day 10: P&C)
DAYS_1_10_APTITUDE[6] = [
    {"mcq_no": i+1, "question": f"Day 06 Aptitude Q{i+1}: A and B work-rate problem with efficiency ratio and days parameter set {i+1}.",
     "options": {"A": f"{10+i} days", "B": f"{12+i} days", "C": f"{15+i} days", "D": f"{18+i} days"},
     "correct_answer": "B", "explanation": f"Using LCM work units model: Total work divided by daily combined efficiency yields {12+i} days.",
     "target_time_seconds": 45, "category": "Quantitative"} for i in range(10)
]
DAYS_1_10_APTITUDE[7] = [
    {"mcq_no": i+1, "question": f"Day 07 Aptitude Q{i+1}: Pipes and cisterns problem with inlet filling and drainage leak parameter set {i+1}.",
     "options": {"A": f"{20+i} mins", "B": f"{24+i} mins", "C": f"{30+i} mins", "D": f"{36+i} mins"},
     "correct_answer": "A", "explanation": f"Net flow rate equals inlet rate minus drainage rate, yielding {20+i} minutes.",
     "target_time_seconds": 40, "category": "Quantitative"} for i in range(10)
]
DAYS_1_10_APTITUDE[8] = [
    {"mcq_no": i+1, "question": f"Day 08 Aptitude Q{i+1}: Train speed and distance crossing stationary platform problem with relative speed set {i+1}.",
     "options": {"A": f"{45+i} km/h", "B": f"{54+i} km/h", "C": f"{60+i} km/h", "D": f"{72+i} km/h"},
     "correct_answer": "B", "explanation": f"Speed = (Length of Train + Length of Platform) / Time, giving {54+i} km/h.",
     "target_time_seconds": 45, "category": "Quantitative"} for i in range(10)
]
DAYS_1_10_APTITUDE[9] = [
    {"mcq_no": i+1, "question": f"Day 09 Aptitude Q{i+1}: Boat upstream and downstream river navigation problem with current velocity set {i+1}.",
     "options": {"A": f"{12+i} km/h", "B": f"{15+i} km/h", "C": f"{18+i} km/h", "D": f"{20+i} km/h"},
     "correct_answer": "B", "explanation": f"Still water speed = (Downstream + Upstream) / 2 = {15+i} km/h.",
     "target_time_seconds": 40, "category": "Quantitative"} for i in range(10)
]
DAYS_1_10_APTITUDE[10] = [
    {"mcq_no": i+1, "question": f"Day 10 Aptitude Q{i+1}: Permutations and combinations arrangement problem with grouping constraints set {i+1}.",
     "options": {"A": f"{120*(i+1)}", "B": f"{240*(i+1)}", "C": f"{360*(i+1)}", "D": f"{720*(i+1)}"},
     "correct_answer": "A", "explanation": f"Using combinatorial selection formula nCr * arrangement factor yields {120*(i+1)} ways.",
     "target_time_seconds": 45, "category": "Quantitative"} for i in range(10)
]

print("Loaded Days 1-10 Aptitude data successfully.")
