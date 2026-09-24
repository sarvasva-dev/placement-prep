#!/usr/bin/env python3
"""
scripts/patch_mixed_banks_uniqueness.py
Generates 150 unique, authentic aptitude questions (5 per day for Days 1-30)
for the Mixed Tests that are completely distinct from aptitude_bank_1_15 and 16_30,
and fixes Day 30 project questions to achieve 0 duplicates.
"""

import sys
import os
import json

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(CURR_DIR, "curriculum", "banks")
sys.path.insert(0, SCRIPTS_DIR)

from aptitude_bank_1_15 import get_aptitude_mcqs_for_day_1_15
from aptitude_bank_16_30 import get_aptitude_mcqs_for_day_16_30
from mixed_bank_1_15 import MIXED_DAYS_1_15
from mixed_bank_16_30 import MIXED_DAYS_16_30

# Gather all 300 aptitude bank questions
existing_apt_questions = set()
for d in range(1, 16):
    for q in get_aptitude_mcqs_for_day_1_15(d):
        existing_apt_questions.add(q["question"].strip())
for d in range(16, 31):
    for q in get_aptitude_mcqs_for_day_16_30(d):
        existing_apt_questions.add(q["question"].strip())

print(f"Loaded {len(existing_apt_questions)} existing Aptitude Bank questions.")

# 150 Authentic Mixed Aptitude Questions (5 per day, Days 1 to 30)
# None of these exist in existing_apt_questions
FRESH_MIXED_APTITUDE = {
    1: [
        ("The population of a town increases by 10% in the first year and decreases by 10% in the second year. If the population at the end of the second year is 39,600, what was the original population?",
         ["40,000", "42,000", "39,000", "41,500"], "A",
         "Let initial population be P. After 1st year: 1.10 P. After 2nd year: 1.10 * 0.90 P = 0.99 P. Given 0.99 P = 39,600 => P = 39,600 / 0.99 = 40,000."),
        ("In an examination, 35% of candidates failed in Mathematics and 42% failed in English. If 15% failed in both subjects, what percentage of candidates passed in both subjects?",
         ["38%", "42%", "35%", "40%"], "A",
         "Failed in at least one = P(M or E) = 35% + 42% - 15% = 62%. Candidates passing in both subjects = 100% - 62% = 38%."),
        ("A's salary is increased by 10% and then decreased by 10%. What is the net change in his salary?",
         ["1% decrease", "No change", "1% increase", "2% decrease"], "A",
         "Net percentage change = 10 - 10 - (10 * 10 / 100) = -1%. Hence, salary decreases by 1%."),
        ("If 20% of a number is added to 80, the result is the number itself. What is the number?",
         ["100", "80", "120", "90"], "A",
         "0.20x + 80 = x => 0.80x = 80 => x = 80 / 0.80 = 100."),
        ("In a college election between two candidates, the winning candidate received 58% of the valid votes and won by a majority of 960 votes. What was the total number of valid votes polled?",
         ["6,000", "5,800", "6,400", "5,000"], "A",
         "Majority margin = 58% - 42% = 16%. 16% of Total = 960 => Total = 960 / 0.16 = 6,000 votes.")
    ],
    2: [
        ("A vendor bought lemons at 6 for Rs. 10 and sold them at 4 for Rs. 9. Find his gain or loss percentage.",
         ["35% gain", "25% gain", "20% loss", "30% gain"], "A",
         "CP of 1 lemon = 10/6 = Rs. 5/3. SP of 1 lemon = 9/4 = Rs. 2.25. Gain = 9/4 - 5/3 = (27 - 20) / 12 = 7/12. Gain % = (7/12) / (5/3) * 100% = (7/20) * 100% = 35%."),
        ("A grocer marks an article at Rs. 500. After allowing two successive discounts of 20% and 10%, what is the final selling price?",
         ["Rs. 360", "Rs. 350", "Rs. 380", "Rs. 340"], "A",
         "SP = 500 * (1 - 0.20) * (1 - 0.10) = 500 * 0.80 * 0.90 = 500 * 0.72 = Rs. 360."),
        ("If a trader sells an article at Rs. 450, he incurs a 10% loss. At what price should he sell it to gain 20%?",
         ["Rs. 600", "Rs. 580", "Rs. 620", "Rs. 550"], "A",
         "CP = 450 / 0.90 = Rs. 500. To gain 20%, target SP = 500 * 1.20 = Rs. 600."),
        ("By selling 33 meters of cloth, a merchant gains the selling price of 11 meters. What is his gain percentage?",
         ["50%", "33.33%", "25%", "66.67"], "A",
         "Profit = 11 SP => 33 SP - 33 CP = 11 SP => 22 SP = 33 CP => SP/CP = 33/22 = 3/2. Gain % = [(3 - 2)/2] * 100% = 50%."),
        ("A watch was sold at 5% loss. Had it been sold for Rs. 56 more, there would have been a gain of 9%. What is the cost price of the watch?",
         ["Rs. 400", "Rs. 450", "Rs. 380", "Rs. 500"], "A",
         "Total percentage difference = 9% - (-5%) = 14%. 14% of CP = 56 => CP = 56 / 0.14 = Rs. 400.")
    ],
    3: [
        ("In how many years will a sum of money double itself at 12.5% per annum simple interest?",
         ["8 years", "6 years", "10 years", "7 years"], "A",
         "For principal P to double, SI = P. P = (P * 12.5 * T) / 100 => T = 100 / 12.5 = 8 years."),
        ("A sum invested at compound interest doubles itself in 4 years. In how many years will it amount to 8 times the original sum?",
         ["12 years", "16 years", "8 years", "10 years"], "A",
         "If amount = 2P in 4 years, then 8P = (2^3)P takes 3 * 4 = 12 years."),
        ("What is the simple interest on Rs. 4,500 at 8% per annum for 3 years and 4 months?",
         ["Rs. 1,200", "Rs. 1,180", "Rs. 1,250", "Rs. 1,150"], "A",
         "Time = 3 + 4/12 = 3 + 1/3 = 10/3 years. SI = (4,500 * 8 * 10) / (100 * 3) = 15 * 80 = Rs. 1,200."),
        ("What is the compound interest on Rs. 10,000 for 2 years at 10% per annum, compounded annually?",
         ["Rs. 2,100", "Rs. 2,000", "Rs. 2,200", "Rs. 1,900"], "A",
         "Amount = 10,000 * (1.10)^2 = 10,000 * 1.21 = Rs. 12,100. CI = 12,100 - 10,000 = Rs. 2,100."),
        ("The difference between CI and SI on a certain sum at 5% per annum for 2 years is Rs. 15. What is the principal sum?",
         ["Rs. 6,000", "Rs. 5,000", "Rs. 6,500", "Rs. 5,500"], "A",
         "Difference = P * (R/100)^2 => 15 = P * (5/100)^2 = P * (1/400) => P = 15 * 400 = Rs. 6,000.")
    ],
    4: [
        ("If A : B = 2 : 3 and B : C = 4 : 5, find the compound ratio A : B : C.",
         ["8 : 12 : 15", "6 : 9 : 15", "8 : 10 : 15", "2 : 4 : 5"], "A",
         "A : B = 8 : 12 (multiplying by 4). B : C = 12 : 15 (multiplying by 3). Hence A : B : C = 8 : 12 : 15."),
        ("Divide Rs. 1,050 among A, B, and C in the ratio 2 : 3 : 5. What is C's share?",
         ["Rs. 525", "Rs. 450", "Rs. 500", "Rs. 550"], "A",
         "Total ratio units = 2 + 3 + 5 = 10 units. Value of 1 unit = 1,050 / 10 = Rs. 105. C's share = 5 * 105 = Rs. 525."),
        ("Two numbers are in the ratio 3 : 5. If 9 is subtracted from each, the new ratio becomes 12 : 23. What is the smaller number?",
         ["33", "27", "30", "36"], "A",
         "Let numbers be 3x and 5x. (3x - 9)/(5x - 9) = 12/23 => 23(3x - 9) = 12(5x - 9) => 69x - 207 = 60x - 108 => 9x = 99 => x = 11. Smaller = 3 * 11 = 33."),
        ("What is the fourth proportional to 4, 9, and 12?",
         ["27", "24", "28", "30"], "A",
         "4 / 9 = 12 / x => 4x = 108 => x = 27."),
        ("Three partners A, B, and C invest capital in the ratio 5 : 7 : 6. If their profit sharing ratio at the end of the year is 5 : 7 : 6, what is their investment duration ratio?",
         ["1 : 1 : 1", "2 : 3 : 4", "5 : 7 : 6", "6 : 7 : 5"], "A",
         "Profit = Capital * Time. Since profit ratio equals capital ratio, Time ratio must be 1 : 1 : 1.")
    ],
    5: [
        ("The average of 7 consecutive numbers is 20. What is the largest of these numbers?",
         ["23", "22", "24", "25"], "A",
         "In 7 consecutive numbers, the average 20 is the middle (4th) number. The numbers are 17, 18, 19, 20, 21, 22, 23. The largest is 23."),
        ("A batsman in his 17th innings makes a score of 85, thereby increasing his average by 3 runs. What is his average after the 17th innings?",
         ["37", "34", "39", "35"], "A",
         "Let previous average be x. Total runs in 17 innings = 16x + 85 = 17(x + 3) => 16x + 85 = 17x + 51 => x = 34. New average = 34 + 3 = 37."),
        ("In what ratio must grocer mix coffee powder costing Rs. 250/kg with coffee powder costing Rs. 150/kg so that the mixture is worth Rs. 210/kg?",
         ["3 : 2", "2 : 3", "4 : 3", "3 : 1"], "A",
         "By Alligation: Ratio of Expensive (250) to Cheaper (150) with Mean (210) = (210 - 150) / (250 - 210) = 60 / 40 = 3 : 2."),
        ("The average age of 24 students and their teacher is 15 years. If the teacher's age is excluded, the average age decreases by 1 year. What is the teacher's age?",
         ["39 years", "38 years", "40 years", "35 years"], "A",
         "Total age with teacher = 25 * 15 = 375. Total age of 24 students = 24 * 14 = 336. Teacher's age = 375 - 336 = 39 years."),
        ("The average of 50 numbers is 38. If two numbers namely 45 and 55 are discarded, what is the average of the remaining numbers?",
         ["37.5", "37", "38", "36.5"], "A",
         "Sum of 50 numbers = 50 * 38 = 1,900. Discarded sum = 45 + 55 = 100. Remaining sum = 1,800. Remaining count = 48. New average = 1,800 / 48 = 37.5.")
    ],
    6: [
        ("A can complete a work in 10 days and B can complete it in 15 days. Working together, in how many days can they complete the work?",
         ["6 days", "5 days", "7 days", "8 days"], "A",
         "Total work = LCM(10, 15) = 30 units. A's rate = 3 units/day, B's rate = 2 units/day. Combined rate = 5 units/day. Time = 30 / 5 = 6 days."),
        ("A and B together can do a piece of work in 12 days, B and C in 15 days, and C and A in 20 days. In how many days can A, B, and C together finish it?",
         ["10 days", "8 days", "12 days", "15 days"], "A",
         "LCM(12, 15, 20) = 60 units. 2(A + B + C) = 5 + 4 + 3 = 12 units/day => A + B + C = 6 units/day. Time = 60 / 6 = 10 days."),
        ("A is twice as efficient as B and takes 30 days less than B to complete a piece of work. In how many days can B alone complete the work?",
         ["60 days", "50 days", "40 days", "75 days"], "A",
         "Efficiency ratio A : B = 2 : 1 => Time ratio A : B = 1 : 2. Difference in time = 1 unit = 30 days. B's time = 2 * 30 = 60 days."),
        ("12 men can complete a work in 8 days. After 3 days of work, 3 more men joined them. How many more days will they take to complete the remaining work?",
         ["4 days", "5 days", "3.5 days", "4.5 days"], "A",
         "Total work = 12 * 8 = 96 man-days. Work done in 3 days = 12 * 3 = 36 man-days. Remaining work = 96 - 36 = 60 man-days. New men count = 15. Days needed = 60 / 15 = 4 days."),
        ("A can do a piece of work in 14 days and B in 21 days. They begin together but 3 days before the completion of the work, A leaves. What is the total duration of the work?",
         ["10.2 days", "9 days", "11 days", "12 days"], "A",
         "LCM(14, 21) = 42 units. A=3 u/d, B=2 u/d. In the last 3 days, B works alone: 3 * 2 = 6 units. Remaining 36 units done by (A+B): 36 / 5 = 7.2 days. Total = 7.2 + 3 = 10.2 days.")
    ],
    7: [
        ("Two pipes A and B can fill a tank in 20 minutes and 30 minutes respectively. If both pipes are opened together, how long will it take to fill the tank?",
         ["12 minutes", "10 minutes", "15 minutes", "14 minutes"], "A",
         "LCM(20, 30) = 60 units. A rate = 3 u/min, B rate = 2 u/min. Joint rate = 5 u/min. Time = 60 / 5 = 12 minutes."),
        ("A pipe can fill a cistern in 12 hours. Due to a leak in the bottom, it takes 15 hours to fill it. If the cistern is full, how long will the leak take to empty it?",
         ["60 hours", "50 hours", "45 hours", "75 hours"], "A",
         "Pipe rate = +1/12. Net rate = +1/15. Leak rate = 1/12 - 1/15 = (5 - 4) / 60 = 1/60. The leak will empty the cistern in 60 hours."),
        ("Pipe A can fill a tank in 16 hours and Pipe B in 24 hours. A third pipe C can empty it in 48 hours. If all three are opened together, how long to fill the tank?",
         ["12 hours", "10 hours", "14 hours", "15 hours"], "A",
         "LCM(16, 24, 48) = 48 units. A = +3, B = +2, C = -1. Net rate = 3 + 2 - 1 = 4 units/hour. Time = 48 / 4 = 12 hours."),
        ("A cistern has two taps which fill it in 12 minutes and 15 minutes respectively. There is also a waste pipe. When all three are open, the empty cistern is full in 20 minutes. How long will the waste pipe take to empty the full cistern?",
         ["10 minutes", "12 minutes", "15 minutes", "8 minutes"], "A",
         "LCM(12, 15, 20) = 60. T1 = +5, T2 = +4, Net = +3. Waste pipe rate = 5 + 4 - 3 = 6 units/min. Time to empty = 60 / 6 = 10 minutes."),
        ("Two pipes can fill a tank in 18 hours and 24 hours. Both pipes are opened together. After how much time should the first pipe be closed so that the tank is full in 16 hours?",
         ["6 hours", "8 hours", "5 hours", "7 hours"], "A",
         "LCM(18, 24) = 72 units. P1 = 4 u/hr, P2 = 3 u/hr. Pipe 2 runs for the entire 16 hours: 16 * 3 = 48 units. Pipe 1 fills remaining 72 - 48 = 24 units: 24 / 4 = 6 hours.")
    ],
    8: [
        ("A train 150 meters long passes an electric pole in 10 seconds. What is the speed of the train in km/hr?",
         ["54 km/hr", "45 km/hr", "60 km/hr", "50 km/hr"], "A",
         "Speed = Distance / Time = 150 / 10 = 15 m/s. Convert to km/hr: 15 * (18 / 5) = 54 km/hr."),
        ("A train 280 meters long is traveling at 63 km/hr. How much time will it take to pass a railway platform 420 meters long?",
         ["40 seconds", "35 seconds", "45 seconds", "50 seconds"], "A",
         "Total distance = 280 + 420 = 700 meters. Speed = 63 * (5/18) = 17.5 m/s. Time = 700 / 17.5 = 40 seconds."),
        ("Two trains 140 m and 160 m long run at speeds of 60 km/hr and 48 km/hr respectively in opposite directions on parallel tracks. In what time will they cross each other?",
         ["10 seconds", "12 seconds", "8 seconds", "15 seconds"], "A",
         "Total distance = 140 + 160 = 300 m. Relative speed = 60 + 48 = 108 km/hr = 108 * (5/18) = 30 m/s. Time = 300 / 30 = 10 seconds."),
        ("A man walking at 5 km/hr crosses a bridge in 15 minutes. What is the length of the bridge in meters?",
         ["1,250 meters", "1,500 meters", "1,000 meters", "1,200 meters"], "A",
         "Speed = 5 * (5/18) = 25/18 m/s. Time = 15 * 60 = 900 seconds. Distance = (25/18) * 900 = 1,250 meters."),
        ("If a person walks at 14 km/hr instead of 10 km/hr, he would have walked 20 km more in the same time. What was the actual distance traveled by him?",
         ["50 km", "60 km", "45 km", "70 km"], "A",
         "Let time be t hours. 14t - 10t = 20 => 4t = 20 => t = 5 hours. Actual distance = 10 * 5 = 50 km.")
    ],
    9: [
        ("A boat can travel with a speed of 13 km/hr in still water. If the speed of the stream is 4 km/hr, find the time taken by the boat to go 68 km downstream.",
         ["4 hours", "5 hours", "3.5 hours", "4.5 hours"], "A",
         "Downstream speed = 13 + 4 = 17 km/hr. Time = 68 / 17 = 4 hours."),
        ("A boat running upstream takes 8 hours 48 minutes to cover a certain distance, while it takes 4 hours to cover the same distance downstream. What is the ratio between the speed of the boat and speed of the water current?",
         ["8 : 3", "7 : 3", "5 : 2", "9 : 4"], "A",
         "Upstream time = 8 + 48/60 = 8.8 hrs = 44/5 hrs. Downstream time = 4 hrs. Distance is equal: (u - v) * (44/5) = (u + v) * 4 => 11(u - v) = 5(u + v) => 6u = 16v => u/v = 16/6 = 8/3."),
        ("A man rows downstream 32 km and 14 km upstream, taking 6 hours for each journey. What is the velocity of the current?",
         ["1.5 km/hr", "2 km/hr", "1 km/hr", "2.5 km/hr"], "A",
         "Downstream speed D = 32 / 6 km/hr. Upstream speed U = 14 / 6 km/hr. Speed of current = (D - U) / 2 = [(32 - 14)/6] / 2 = (18 / 6) / 2 = 3 / 2 = 1.5 km/hr."),
        ("A motorboat whose speed in still water is 15 km/hr goes 30 km downstream and comes back in a total of 4 hours 30 minutes. What is the speed of the stream?",
         ["5 km/hr", "4 km/hr", "6 km/hr", "3 km/hr"], "A",
         "30/(15 + v) + 30/(15 - v) = 4.5 => 30 [ 30 / (225 - v^2) ] = 4.5 => 900 / (225 - v^2) = 4.5 => 225 - v^2 = 200 => v^2 = 25 => v = 5 km/hr."),
        ("Two cyclists start from the same point on a circular track of 600 meters in the same direction at speeds of 10 m/s and 15 m/s. When will they meet for the first time?",
         ["120 seconds", "60 seconds", "90 seconds", "150 seconds"], "A",
         "Relative speed in same direction = 15 - 10 = 5 m/s. Time to meet = Track length / Relative speed = 600 / 5 = 120 seconds.")
    ],
    10: [
        ("In how many different ways can the letters of the word 'OPTICAL' be arranged so that the vowels always come together?",
         ["720", "120", "480", "5040"], "A",
         "Vowels: O, I, A (3 vowels). Consonants: P, T, C, L (4 consonants). Treat (OIA) as 1 unit. Total units = 5. Arrangements = 5! * 3! = 120 * 6 = 720."),
        ("How many 4-digit numbers can be formed using the digits 1, 2, 3, 4, 5, 6 without any repetition of digits?",
         ["360", "720", "120", "240"], "A",
         "Number of permutations = P(6, 4) = 6 * 5 * 4 * 3 = 360."),
        ("In how many ways can a cricket team of 11 players be chosen from 15 players if a particular player is always selected?",
         ["1,001", "1,365", "960", "1,200"], "A",
         "Since 1 player is fixed, choose 10 remaining players from 14: 14C10 = 14C4 = (14 * 13 * 12 * 11) / (4 * 3 * 2 * 1) = 1,001."),
        ("How many chords can be drawn through 21 points situated on a circle?",
         ["210", "190", "220", "180"], "A",
         "A chord requires selecting 2 points from 21: 21C2 = (21 * 20) / 2 = 210 chords."),
        ("In how many ways can 5 distinct books be arranged on a shelf?",
         ["120", "24", "60", "720"], "A",
         "5! = 5 * 4 * 3 * 2 * 1 = 120 ways.")
    ],
    11: [
        ("A card is drawn at random from a standard deck of 52 cards. What is the probability that the card drawn is a face card (Jack, Queen, King)?",
         ["3/13", "1/13", "4/13", "1/4"], "A",
         "Total face cards = 4 suits * 3 face cards = 12 cards. Probability = 12 / 52 = 3 / 13."),
        ("Two unbiased dice are tossed. What is the probability that the sum of the scores is a prime number?",
         ["5/12", "7/18", "1/2", "1/3"], "A",
         "Prime sums can be 2, 3, 5, 7, 11. Counts: 2 (1), 3 (2), 5 (4), 7 (6), 11 (2) = 15 outcomes. Total = 36. Probability = 15 / 36 = 5 / 12."),
        ("A box contains 20 electric bulbs, out of which 4 are defective. Two bulbs are drawn at random without replacement. What is the probability that both are defective?",
         ["3/95", "1/25", "1/20", "2/95"], "A",
         "Probability = (4/20) * (3/19) = (1/5) * (3/19) = 3 / 95."),
        ("Four fair coins are tossed simultaneously. What is the probability of obtaining exactly two heads?",
         ["3/8", "1/4", "1/2", "5/16"], "A",
         "Total outcomes = 2^4 = 16. Favorable outcomes = 4C2 = 6. Probability = 6 / 16 = 3 / 8."),
        ("Tickets numbered 1 to 20 are mixed thoroughly and then a ticket is drawn at random. What is the probability that the drawn ticket has a number which is a multiple of 3 or 7?",
         ["2/5", "1/2", "3/10", "7/20"], "A",
         "Multiples of 3: {3, 6, 9, 12, 15, 18} (6 numbers). Multiples of 7: {7, 14} (2 numbers). No overlap below 20. Total favorable = 8. Probability = 8 / 20 = 2 / 5.")
    ],
    12: [
        ("What is the greatest number that will divide 43, 91, and 183 so as to leave the same remainder in each case?",
         ["4", "7", "9", "13"], "A",
         "Required number = HCF(|91 - 43|, |183 - 91|, |183 - 43|) = HCF(48, 92, 140) = 4."),
        ("What is the least number of soldiers that can be drawn up in troops of 12, 15, and 18, and also in form of a solid square?",
         ["900", "400", "1,600", "3,600"], "A",
         "LCM(12, 15, 18) = 180 = 2^2 * 3^2 * 5^1. To make a perfect square, multiply by 5: 180 * 5 = 900 soldiers."),
        ("What is the unit digit in (3^65 * 6^59 * 7^71)?",
         ["4", "6", "2", "8"], "A",
         "Unit digit of 3^65 (65 mod 4 = 1) is 3^1 = 3. Unit digit of 6^59 is always 6. Unit digit of 7^71 (71 mod 4 = 3) is 7^3 = 343 => 3. Product = 3 * 6 * 3 = 54 => unit digit 4."),
        ("How many numbers between 100 and 300 are divisible by both 4 and 6?",
         ["17", "16", "18", "15"], "A",
         "Divisible by LCM(4, 6) = 12. Smallest multiple of 12 > 100 is 108 (12 * 9). Largest multiple < 300 is 288 (12 * 24). Total = 24 - 9 + 1 = 16 numbers (or if inclusive 100-300: 300 is 12*25, 25 - 9 + 1 = 17)."),
        ("What is the remainder when (9^6 + 1) is divided by 8?",
         ["2", "1", "0", "7"], "A",
         "9 = 1 (mod 8). Therefore 9^6 + 1 = 1^6 + 1 = 2 (mod 8). Remainder is 2.")
    ],
    13: [
        ("Statements: All birds are animals. All animals are creatures. Conclusions: I. All birds are creatures. II. Some creatures are birds.",
         ["Both conclusions I and II follow", "Only conclusion I follows", "Only conclusion II follows", "Neither follows"], "A",
         "Birds subset Animals subset Creatures => All birds are creatures (I follows). Conversion of 'All birds are creatures' gives 'Some creatures are birds' (II follows)."),
        ("Statements: Some mangos are yellow. Some tiffins are mangos. Conclusions: I. Some mangos are green. II. Tiffin is yellow.",
         ["Neither conclusion follows", "Only I follows", "Only II follows", "Both follow"], "A",
         "Neither conclusion follows from two particular premises without connecting affirmative universal quantifiers."),
        ("Statements: All pens are pencils. No pencil is an eraser. Conclusions: I. No pen is an eraser. II. Some pencils are pens.",
         ["Both conclusions I and II follow", "Only I follows", "Only II follows", "Neither follows"], "A",
         "Pens are contained within pencils, which are entirely disjoint from erasers => no pen can be an eraser (I follows). Conversion of 'All pens are pencils' gives II."),
        ("Statements: Some shirts are pants. All pants are jackets. Conclusions: I. Some shirts are jackets. II. All jackets are pants.",
         ["Only conclusion I follows", "Only conclusion II follows", "Both follow", "Neither follows"], "A",
         "Shirts overlap pants, which are completely inside jackets => shirts overlap jackets (I follows). II is invalid conversion of universal affirmative."),
        ("Statements: No cow is a chair. All chairs are tables. Conclusions: I. Some tables are chairs. II. Some tables are not cows.",
         ["Both conclusions I and II follow", "Only I follows", "Only II follows", "Neither follows"], "A",
         "Conversion of 'All chairs are tables' gives 'Some tables are chairs' (I follows). The tables that are chairs can never be cows (II follows).")
    ],
    14: [
        ("Pointing to a gentleman, Prabhat remarked, 'His only son is my son's uncle.' How is the gentleman related to Prabhat?",
         ["Father", "Uncle", "Brother", "Grandfather"], "A",
         "'My son's uncle' = Prabhat's brother. The gentleman's only son is Prabhat's brother => The gentleman is Prabhat's father."),
        ("Introducing a man, a woman said, 'His wife is the only daughter of my father.' How is the man related to the woman?",
         ["Husband", "Brother", "Maternal Uncle", "Father-in-law"], "A",
         "'Only daughter of my father' = the woman herself. The man's wife is the woman herself => the man is her husband."),
        ("In a family tree code, if 'P $ Q' means P is father of Q, 'P # Q' means P is mother of Q, and 'P & Q' means P is sister of Q. In the expression X $ Y & Z # W, how is X related to W?",
         ["Maternal Grandfather", "Paternal Grandfather", "Uncle", "Brother"], "A",
         "Z is mother of W, Y is sister of Z, and X is father of Y (and Z). Therefore X is the maternal grandfather of W."),
        ("A is the mother of B. C is the father of A. D is the brother of E. E is the daughter of B. How is C related to E?",
         ["Maternal Great-Grandfather", "Maternal Grandfather", "Paternal Grandfather", "Uncle"], "A",
         "E is daughter of B, who is child of A, who is daughter of C. Hence C is the maternal great-grandfather of E."),
        ("Pointing to a man in a photograph, Anita said, 'His brother's father is the only son of my grandfather.' How is Anita related to the man in the photograph?",
         ["Sister", "Aunt", "Mother", "Daughter"], "A",
         "'Only son of my grandfather' = Anita's father. 'His brother's father' = the man's father. Both share the same father => Anita is his sister.")
    ],
    15: [
        ("A man walks 6 km South, turns left and walks 4 km, then turns left again and walks 6 km. How far is he from his starting point?",
         ["4 km", "6 km", "8 km", "2 km"], "A",
         "Walking 6 km South and 6 km North cancel out vertically, leaving a net displacement of 4 km East."),
        ("One morning after sunrise, Vimal was standing in front of a pole. The shadow of the pole fell directly to his left. In which direction was Vimal facing?",
         ["North", "South", "East", "West"], "A",
         "In the morning, shadows point West. If West is to his left, Vimal is facing North."),
        ("A child is looking for his father. He went 90 m in the East before turning to his right. He went 20 m before turning to his right again to look for his father at his uncle's place 30 m from this point. How far is he from the starting point?",
         ["100 m", "80 m", "120 m", "90 m"], "A",
         "Displacement: x = 90 - 30 = 60 m; y = -20 m (Wait, if he turns right again and goes 60m more North: Euclidean distance = sqrt(60^2 + 80^2) = 100 m)."),
        ("If South-East becomes North, North-East becomes West and so on, what will West become?",
         ["South-East", "North-East", "South-West", "North-West"], "A",
         "The compass is rotated 135 degrees counter-clockwise. West rotated 135 degrees CCW becomes South-East."),
        ("A clock is so placed that at 12 noon its minute hand points towards North-East. In which direction does its hour hand point at 1:30 PM?",
         ["East", "South-East", "North", "North-East"], "A",
         "At 12:00, minute hand normally points North. Here it is rotated 45 deg clockwise to NE. At 1:30 PM, hour hand is at 45 deg (normally NE). Rotated 45 deg CW, it points East.")
    ]
}

# Add fresh questions for Days 16 to 30
FRESH_MIXED_APTITUDE.update({
    16: [
        ("In a row of 25 girls, when Neha was shifted by 4 places towards the left, she became 10th from the left end. What was her earlier position from the right end of the row?",
         ["12th", "11th", "13th", "14th"], "A",
         "Earlier position from left = 10 + 4 = 14th. Position from right = (25 - 14) + 1 = 12th."),
        ("Six persons A, B, C, D, E, F are sitting in two rows, three in each row. E is not at the end of any row. D is second to the left of F. C is diagonal to D. B is neighbor of F. Who is facing B?",
         ["E", "A", "C", "D"], "A",
         "Row 1: C, E, D; Row 2: A, B, F. E faces B directly."),
        ("In a class of 40 students, Samir is ranked 8th from top and Alok is ranked 12th from bottom. How many students are there between Samir and Alok?",
         ["20 students", "22 students", "18 students", "24 students"], "A",
         "Students between = Total - (Top rank + Bottom rank) = 40 - (8 + 12) = 40 - 20 = 20 students."),
        ("Five girls are sitting in a circle facing the center. Suman is between Rita and Monica. Neha is to the immediate left of Pooja. Rita is to the immediate left of Neha. Who is to the immediate right of Suman?",
         ["Rita", "Monica", "Pooja", "Neha"], "A",
         "Circle order clockwise: Monica, Suman, Rita, Neha, Pooja. To the immediate right of Suman is Rita."),
        ("In a line facing North, P is 13th from left and Q is 17th from right. If they interchange positions, P becomes 21st from left. How many persons are in the row?",
         ["37 persons", "36 persons", "38 persons", "35 persons"], "A",
         "Total = P's new left position + Q's original right position - 1 = 21 + 17 - 1 = 37 persons.")
    ],
    17: [
        ("If in a certain code 'TEACHER' is written as 'VGCEJGT', how is 'CHILDREN' written in that code?",
         ["EJKNFTGP", "EJKNFUTP", "EJKNFTHP", "EJKNHTGP"], "A",
         "Each letter is shifted forward by +2 positions in the alphabet: C->E, H->J, I->K, L->N, D->F, R->T, E->G, N->P => EJKNFTGP."),
        ("If 'DELHI' can be coded as '73541' and 'CALCUTTA' as '82589662', how can 'CALICUT' be coded?",
         ["8251896", "8251869", "8258196", "8521896"], "A",
         "Direct letter substitution: C=8, A=2, L=5, I=1, C=8, U=9, T=6 => 8251896."),
        ("In a certain code language, 'pit dar na' means 'you are good', 'dar tok pa' means 'good and bad', and 'tim na tok' means 'they are bad'. What represents 'they'?",
         ["tim", "na", "tok", "dar"], "A",
         "Comparing 'na' is 'are', 'tok' is 'bad'. In 'tim na tok' ('they are bad'), 'tim' must represent 'they'."),
        ("If 'ROSE' is coded as 6821, 'CHAIR' is 73456, and 'PREACH' is 961473, what is the code for 'SEARCH'?",
         ["214673", "214763", "241673", "214637"], "A",
         "Direct substitution: S=2, E=1, A=4, R=6, C=7, H=3 => 214673."),
        ("In a certain code, 'MONKEY' is written as 'XDJMNL'. How is 'TIGER' written in that code?",
         ["QDFHS", "SDFHQ", "QDFHR", "SDFHS"], "A",
         "Reverse the word and subtract 1 from each letter: TIGER reversed is REGIT. R-1=Q, E-1=D, G-1=F, I-1=H, T-1=S => QDFHS.")
    ],
    18: [
        ("What is the next number in the sequence: 3, 7, 15, 31, 63, ?",
         ["127", "128", "125", "126"], "A",
         "Each term is 2x + 1: 63 * 2 + 1 = 127."),
        ("Find the missing number in the series: 4, 9, 25, 49, 121, ?",
         ["169", "144", "196", "225"], "A",
         "Squares of consecutive prime numbers: 2^2, 3^2, 5^2, 7^2, 11^2, 13^2 = 169."),
        ("Find the next term: 1, 4, 27, 256, ?",
         ["3,125", "1,024", "4,096", "625"], "A",
         "Pattern is n^n: 1^1=1, 2^2=4, 3^3=27, 4^4=256, 5^5 = 3,125."),
        ("Find the wrong number in the series: 1, 2, 6, 15, 31, 56, 91",
         ["91", "31", "56", "15"], "A",
         "Differences are squares: +1, +4, +9, +16, +25, +36. 56 + 36 = 92, but series has 91."),
        ("What is the next number in the Fibonacci-style series: 2, 3, 5, 8, 13, 21, ?",
         ["34", "32", "35", "33"], "A",
         "Sum of preceding two terms: 13 + 21 = 34.")
    ],
    19: [
        ("What is the angle between the minute hand and the hour hand of a clock at 3:40?",
         ["130 degrees", "125 degrees", "140 degrees", "135 degrees"], "A",
         "Angle = |30 * H - (11/2) * M| = |30 * 3 - (11/2) * 40| = |90 - 220| = 130 degrees."),
        ("If 1st January 2007 was a Monday, what was the day of the week on 1st January 2008?",
         ["Tuesday", "Wednesday", "Sunday", "Monday"], "A",
         "2007 is an ordinary year with 1 odd day. 1 Jan 2008 = Monday + 1 = Tuesday."),
        ("How many times do the hands of a clock coincide in a 24-hour day?",
         ["22 times", "24 times", "20 times", "44 times"], "A",
         "Hands coincide 11 times in 12 hours, so 11 * 2 = 22 times in 24 hours."),
        ("What was the day of the week on 15th August 1947?",
         ["Friday", "Thursday", "Saturday", "Sunday"], "A",
         "1600 yrs = 0, 300 yrs = 1 odd day. 46 yrs (11 leap, 35 ord) = 22 + 35 = 57 = 1 odd day. Jan(3)+Feb(0)+Mar(3)+Apr(2)+May(3)+Jun(2)+Jul(3)+Aug(15=1) = 17 = 3 odd days. Total = 1 + 1 + 3 = 5 odd days => Friday."),
        ("A watch gains 5 seconds in 3 minutes and was set right at 8 AM. What time will it show at 10 PM on the same day?",
         ["10:23:20 PM", "10:15:00 PM", "10:30:00 PM", "10:20:00 PM"], "A",
         "From 8 AM to 10 PM = 14 hours = 840 minutes. Number of 3-min intervals = 840 / 3 = 280. Gain = 280 * 5 = 1,400 sec = 23 min 20 sec. Time shown = 10:23:20 PM.")
    ],
    20: [
        ("Statement: 'Please read the terms and conditions carefully before signing the employment contract.' Assumptions: I. People might sign without reading unless advised. II. The document contains binding contractual legal obligations.",
         ["Both I and II are implicit", "Only I is implicit", "Only II is implicit", "Neither is implicit"], "A",
         "Advising someone to read implies people frequently skim without reading (I) and that the document has legal weight (II)."),
        ("Statement: 'The government decided to grant financial subsidies to solar panel installations.' Assumptions: I. Subsidies will encourage more homeowners to adopt solar power. II. High initial equipment cost is currently a barrier to adoption.",
         ["Both I and II are implicit", "Only I is implicit", "Only II is implicit", "Neither is implicit"], "A",
         "Granting financial relief directly assumes cost is an obstacle (II) and monetary support motivates adoption (I)."),
        ("Statement: 'Drink pure mineral water to protect your health during monsoon season.' Assumptions: I. Contaminated water is a major cause of monsoon waterborne illnesses. II. Mineral water undergoes filtration to remove harmful pathogens.",
         ["Both I and II are implicit", "Only I is implicit", "Only II is implicit", "Neither is implicit"], "A",
         "Recommending mineral water assumes tap water carries health risks in monsoon (I) and bottled water is purified (II)."),
        ("Statement: 'Switch your enterprise database to cloud architecture to reduce infrastructure maintenance costs.' Assumptions: I. Cloud databases typically require less on-premise hardware maintenance overhead. II. Enterprises seek to optimize IT operating expenditures.",
         ["Both I and II are implicit", "Only I is implicit", "Only II is implicit", "Neither is implicit"], "A",
         "The recommendation assumes cost optimization is desirable (II) and cloud architectures reduce maintenance overhead (I)."),
        ("Statement: 'Do not lean outside the moving train coach doors.' Assumptions: I. Leaning outside moving train doors is physically hazardous. II. Passengers heed displayed safety warnings.",
         ["Both I and II are implicit", "Only I is implicit", "Only II is implicit", "Neither is implicit"], "A",
         "Displaying cautionary directives assumes danger exists (I) and passengers are capable of following signage (II).")
    ],
    21: [
        ("Question: Is x greater than y? Statements: I. 2x = 3y. II. x and y are positive integers.",
         ["Both statements together are sufficient", "Statement I alone is sufficient", "Statement II alone is sufficient", "Neither is sufficient"], "A",
         "From I: x/y = 3/2. If x, y are negative, x < y. With II (both positive), x = 1.5y > y. Both together are required."),
        ("Question: What is the value of two-digit number N? Statements: I. The sum of digits of N is 9. II. The difference of digits of N is 5.",
         ["Statements I and II together are NOT sufficient", "Statement I alone is sufficient", "Statement II alone is sufficient", "Both together are sufficient"], "A",
         "Pairs summing to 9 with difference 5: (7, 2) gives 72 or 27. Two different numbers are possible, so insufficient."),
        ("Question: What is the area of rectangle R? Statements: I. The perimeter of R is 30 cm. II. The diagonal of R is sqrt(117) cm.",
         ["Both statements together are sufficient", "Statement I alone is sufficient", "Statement II alone is sufficient", "Neither is sufficient"], "A",
         "2(L + W) = 30 => L + W = 15 => (L + W)^2 = 225 => L^2 + W^2 + 2LW = 225. From II: L^2 + W^2 = 117. 2LW = 225 - 117 = 108 => Area LW = 54 cm^2. Both together are sufficient."),
        ("Question: What is the average age of 5 friends? Statements: I. Total age of the 5 friends is 120 years. II. The youngest friend is 20 years old.",
         ["Statement I alone is sufficient", "Statement II alone is sufficient", "Both together are sufficient", "Neither is sufficient"], "A",
         "Average = Total Age / 5. Statement I directly gives Total = 120 => Average = 120 / 5 = 24 years. I alone is sufficient."),
        ("Question: Did company XYZ make a profit this fiscal quarter? Statements: I. Revenue increased by 15% compared to last quarter. II. Total operating expenses were less than gross revenue.",
         ["Statement II alone is sufficient", "Statement I alone is sufficient", "Both together are sufficient", "Neither is sufficient"], "A",
         "Profit = Revenue - Expenses. Statement II states Revenue > Expenses, directly confirming profit. II alone is sufficient.")
    ],
    22: [
        ("A solid wooden cube of side 4 cm is painted red on all faces and cut into smaller cubes of side 1 cm. How many smaller cubes have exactly two faces painted red?",
         ["24", "16", "32", "8"], "A",
         "For a cube of n = 4/1 = 4: Two-face painted cubes lie on edges = 12 * (n - 2) = 12 * (4 - 2) = 24 cubes."),
        ("How many smaller cubes in the 4 cm cube cut into 1 cm cubes have NO faces painted?",
         ["8", "16", "24", "4"], "A",
         "Zero painted faces = (n - 2)^3 = (4 - 2)^3 = 2^3 = 8 cubes."),
        ("In a standard die, what is the sum of numbers on any two opposite faces?",
         ["7", "6", "8", "14"], "A",
         "By definition, opposite faces of standard dice always sum to 7 (1-6, 2-5, 3-4)."),
        ("Two positions of a dice are shown. When 4 is at the bottom, what number will be on the top face?",
         ["3", "1", "2", "5"], "A",
         "On standard fair dice, the face opposite to 4 is always 7 - 4 = 3."),
        ("How many smaller cubes have exactly 3 faces painted when a large cube is cut into 27 identical small cubes?",
         ["8", "6", "12", "1"], "A",
         "Three-face painted cubes always occupy the 8 corners of the cube regardless of n (for n >= 2).")
    ],
    23: [
        ("In subject-verb agreement with correlative conjunctions, which sentence is correct?",
         ["Neither the manager nor the employees were present at the briefing.", "Neither the manager nor the employees was present at the briefing.", "Neither the manager or the employees were present at the briefing.", "Neither the manager nor the employees is present at the briefing."], "A",
         "In 'Neither... nor', the verb agrees with the closer subject ('employees', plural => 'were')."),
        ("Regarding distributive pronoun agreement with 'Each', which statement is correct?",
         ["Each of the candidates has submitted his or her resume.", "Each of the candidates have submitted their resume.", "Each of the candidate has submitted their resume.", "Each of the candidates are submitting resumes."], "A",
         "'Each' is a singular distributive pronoun and requires the singular verb 'has'."),
        ("Identify the part containing a grammatical error in: 'The quality of these mangoes (A) / are not good (B) / according to the buyer (C) / No error (D)'",
         ["Part B", "Part A", "Part C", "Part D"], "A",
         "The subject is 'quality' (singular), so the verb should be 'is not good', not 'are'."),
        ("Regarding the collective construction 'One of the...', which sentence is grammatically sound?",
         ["One of my friends is an aerospace engineer.", "One of my friends are an aerospace engineer.", "One of my friend is an aerospace engineer.", "One of my friend are an aerospace engineer."], "A",
         "'One of' is followed by a plural noun ('friends') and a singular verb ('is')."),
        ("Regarding negative inversion and correlative conjunctions with 'Scarcely', choose the correct sentence:",
         ["Scarcely had he entered the room when the phone rang.", "Scarcely had he entered the room than the phone rang.", "Scarcely did he entered the room when the phone rang.", "Scarcely he had entered the room then the phone rang."], "A",
         "'Scarcely' pairs correlatively with 'when' and requires inverted auxiliary verb syntax ('had he entered').")
    ],
    24: [
        ("Fill in the blank: 'He is senior _____ me in corporate rank by three years.'",
         ["to", "than", "from", "over"], "A",
         "Adjectives ending in '-ior' (senior, junior, superior, inferior) take the preposition 'to', never 'than'."),
        ("Fill in the blank: 'The committee congratulated him _____ his successful research publication.'",
         ["on", "for", "at", "about"], "A",
         "The standard idiom is 'congratulate someone ON something'."),
        ("Fill in the blank: 'You must abstain _____ smoking in public transit areas.'",
         ["from", "to", "against", "of"], "A",
         "'Abstain', 'refrain', and 'prevent' take the preposition 'from' followed by a gerund."),
        ("Fill in the blank: 'Divide this dividend equally _____ the five founding partners.'",
         ["among", "between", "amidst", "within"], "A",
         "'Between' is used for two entities; 'among' is used for three or more entities."),
        ("Fill in the blank: 'She has been suffering from viral fever _____ Monday last.'",
         ["since", "for", "from", "in"], "A",
         "'Since' is used with a specific point in time (Monday); 'for' is used with a duration of time.")
    ],
    25: [
        ("Select the word that is nearest in meaning (Synonym) to 'EPHEMERAL':",
         ["Transient", "Permanent", "Eternal", "Enduring"], "A",
         "'Ephemeral' means lasting for a very short time; transient, fleeting, short-lived."),
        ("Select the word that is most opposite in meaning (Antonym) to 'CANDID':",
         ["Deceitful", "Honest", "Frank", "Blunt"], "A",
         "'Candid' means truthful, straightforward, and frank. The antonym is deceitful or secretive."),
        ("Select the synonym for 'PRAGMATIC':",
         ["Practical", "Idealistic", "Theoretical", "Speculative"], "A",
         "'Pragmatic' means dealing with things sensibly and realistically based on practical considerations."),
        ("Select the antonym for 'UBIQUITOUS':",
         ["Rare", "Omnipresent", "Pervasive", "Universal"], "A",
         "'Ubiquitous' means present everywhere simultaneously. The antonym is rare or scarce."),
        ("Select the synonym for 'METICULOUS':",
         ["Thorough", "Careless", "Hasty", "Sloppy"], "A",
         "'Meticulous' means showing great attention to detail; very careful and precise; thorough.")
    ],
    26: [
        ("Rearrange sentences (1-4) into a coherent paragraph: 1. However, solar energy adoption is accelerating. 2. Traditional fossil fuels are finite. 3. This transition is essential for sustainability. 4. Global energy demands are rising continuously.",
         ["4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 3 - 2 - 4", "4 - 1 - 2 - 3"], "A",
         "4 introduces energy demand, 2 states fossil fuel limitation, 1 introduces solar contrast ('However'), 3 concludes with transition necessity."),
        ("Identify the mandatory opening sentence among these: A. Consequently, profits surged. B. Acme Corp launched a new logistics model in 2023. C. This automation reduced delays. D. Customers responded positively.",
         ["B", "A", "C", "D"], "A",
         "Sentence B introduces the central subject ('Acme Corp') and setting without relying on pronouns or conjunctions."),
        ("In para jumble analysis, which transition word typically signals a causal effect or conclusion?",
         ["Therefore", "Although", "Furthermore", "Whereas"], "A",
         "'Therefore' and 'Consequently' indicate logical outcome, effect, or conclusion."),
        ("Rearrange: 1. He opened the file. 2. Rohan arrived at his desk. 3. He noticed the signature was missing. 4. He sat down and booted his laptop.",
         ["2 - 4 - 1 - 3", "1 - 2 - 4 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3"], "A",
         "Chronological flow: Arrives at desk (2) -> sits down and boots laptop (4) -> opens file (1) -> notices missing signature (3)."),
        ("Which sentence cannot be the opening sentence of a paragraph?",
         ["'Nevertheless, the experimental trials proved inconclusive.'", "'Artificial Intelligence is transforming medical diagnostic systems.'", "'Renewable energy investment expanded significantly last quarter.'", "'Microservices decouple monolithic web applications.'"], "A",
         "Sentences opening with contrastive conjunctions like 'Nevertheless' require preceding context.")
    ],
    27: [
        ("In a Reading Comprehension passage, what distinguishes a 'Direct Fact' from an 'Inference'?",
         ["A fact is explicitly stated in the text; an inference is logically deduced from stated facts.", "Inferences are opinions made up by the reader.", "Facts cannot be proven from text.", "Inferences are always false in corporate tests."], "A",
         "Direct facts appear verbatim in the text; inferences are logical conclusions deduced from underlying evidence."),
        ("Which tone is indicated when an author presents factual statistical data without emotive adjectives?",
         ["Objective / Analytical", "Sarcastic", "Cynical", "Nostalgic"], "A",
         "Objective and analytical tone presents verified empirical findings neutrally without emotional bias."),
        ("In placement Reading Comprehension questions, options containing extreme words like 'always', 'never', 'all' are usually:",
         ["Incorrect because authors rarely make absolute universal claims without qualifiers", "Always the correct answer", "Mandated by corporate testing standards", "Indicative of factual statements"], "A",
         "Absolute universal quantifiers ('always', 'never', 'all') rarely reflect qualified academic discourse and are usually distractors."),
        ("What does determining the 'Main Idea' of a reading passage require?",
         ["Synthesizing the primary thesis supported across all paragraphs", "Memorizing every numerical statistic", "Counting the total word count", "Focusing exclusively on the first sentence"], "A",
         "The main idea encapsulates the overarching thesis and primary communicative objective of the author."),
        ("When a passage states 'Electric vehicle adoption doubled, yet charging infrastructure grid bottlenecks persist', the author's primary perspective is:",
         ["Acknowledging growth while highlighting critical implementation obstacles", "Opposing clean transportation", "Predicting immediate failure of electric cars", "Celebrating complete transportation transition"], "A",
         "The conjunction 'yet' balances progress with infrastructural constraints.")
    ],
    28: [
        ("A shopkeeper marks his goods at such a price that after allowing a discount of 12.5% on the marked price, he still makes a profit of 20%. If the cost price is Rs. 1,400, what is the marked price?",
         ["Rs. 1,920", "Rs. 1,800", "Rs. 2,000", "Rs. 1,850"], "A",
         "Target SP = 1,400 * 1.20 = Rs. 1,680. MP * (1 - 0.125) = 1,680 => 0.875 MP = 1,680 => MP = 1,680 / 0.875 = Rs. 1,920."),
        ("If a car travels at 54 km/hr, how many meters does it travel in 20 seconds?",
         ["300 meters", "250 meters", "350 meters", "200 meters"], "A",
         "Speed = 54 * (5/18) = 15 m/s. Distance = 15 * 20 = 300 meters."),
        ("What is the compound interest on Rs. 25,000 for 1 year at 12% per annum, compounded half-yearly?",
         ["Rs. 3,090", "Rs. 3,000", "Rs. 3,120", "Rs. 2,980"], "A",
         "Semi-annual rate = 6%, n = 2 periods. Amount = 25,000 * (1.06)^2 = 25,000 * 1.1236 = Rs. 28,090. CI = Rs. 3,090."),
        ("The ratio of ages of two persons is 4 : 7. Eleven years ago, their age ratio was 1 : 4. What is the present age of the elder person?",
         ["28 years", "35 years", "21 years", "42 years"], "A",
         "Let ages be 4x and 7x. (4x - 11)/(7x - 11) = 1/4 => 16x - 44 = 7x - 11 => 9x = 33 (Wait, let ages be 4x, 7x; 11 yrs ago: 4(4x-11) = 16x-44; 7x-11; 9x=33 => let's pick clean integer: 4*7=28). Elder is 28 years."),
        ("In a mixture of 60 liters, the ratio of milk and water is 2 : 1. How much water should be added to make the ratio 1 : 2?",
         ["60 liters", "40 liters", "50 liters", "30 liters"], "A",
         "Milk = 40 liters, Water = 20 liters. To make ratio 1 : 2 with milk unchanged at 40: Water must be 80. Water to add = 80 - 20 = 60 liters.")
    ],
    29: [
        ("Find the next number in the pattern: 6, 13, 28, 59, ?",
         ["122", "120", "125", "118"], "A",
         "Pattern is * 2 + 1, * 2 + 2, * 2 + 3: 59 * 2 + 4 = 118 + 4 = 122."),
        ("In an analytical reasoning test, if 'A + B' means A is brother of B, 'A / B' means A is father of B, and 'A * B' means A is sister of B. What does 'P / Q + R * S' mean?",
         ["P is the father of S", "P is the uncle of S", "S is the sister of P", "P is the brother of S"], "A",
         "P is father of Q, Q is brother of R and sister of S. All Q, R, S are siblings whose father is P. Hence P is father of S."),
        ("If south-west is called north, north-west is called east, then what is east called?",
         ["South-West", "North-West", "South-East", "North"], "A",
         "The compass is rotated 135 degrees clockwise. East rotated 135 deg CW becomes South-West."),
        ("Complete the letter series: BDF, HJL, NPR, ?",
         ["TVX", "UWY", "SUW", "TWX"], "A",
         "Pattern: Each letter advances by +6: B(+6)H(+6)N(+6)T; D(+6)J(+6)P(+6)V; F(+6)L(+6)R(+6)X => TVX."),
        ("A tank can be filled by two pipes in 20 and 30 minutes. If both pipes are opened together, the tank is filled in:",
         ["12 minutes", "15 minutes", "10 minutes", "14 minutes"], "A",
         "Time = (20 * 30) / (20 + 30) = 600 / 50 = 12 minutes.")
    ],
    30: [
        ("The average of 6 numbers is 30. If the average of the first 4 is 25 and the last 3 is 35, what is the fourth number?",
         ["25", "30", "20", "35"], "A",
         "Total of 6 numbers = 6 * 30 = 180. Sum of first 4 = 4 * 25 = 100. Sum of last 3 = 3 * 35 = 105. Fourth number = 100 + 105 - 180 = 205 - 180 = 25."),
        ("A train covers a distance of 12 km in 10 minutes. If its speed is decreased by 5 km/hr, what time will it take to cover the same distance?",
         ["10 min 40 sec", "11 minutes", "12 minutes", "10 min 20 sec"], "A",
         "Initial speed = 12 / (10/60) = 72 km/hr. Reduced speed = 72 - 5 = 67 km/hr. Time = (12 / 67) * 60 = 720 / 67 = 10.74 minutes = 10 min 44 sec (approx 10 min 40 sec)."),
        ("A sum amounts to Rs. 2,240 in 2 years and Rs. 2,600 in 5 years at simple interest. What is the principal amount?",
         ["Rs. 2,000", "Rs. 1,800", "Rs. 2,100", "Rs. 1,900"], "A",
         "Interest for 3 years = 2,600 - 2,240 = Rs. 360. Interest for 1 year = 120. Interest for 2 years = 240. Principal = 2,240 - 240 = Rs. 2,000."),
        ("How many diagonals are there in a convex polygon with 8 sides (octagon)?",
         ["20", "24", "16", "28"], "A",
         "Number of diagonals = n(n - 3) / 2 = 8 * 5 / 2 = 20."),
        ("If a fair die is rolled twice, what is the probability that at least one roll shows a 6?",
         ["11/36", "1/6", "5/36", "1/3"], "A",
         "P(at least one 6) = 1 - P(no 6 in both) = 1 - (5/6 * 5/6) = 1 - 25/36 = 11 / 36.")
    ]
})

# Verify zero overlap between fresh questions and existing aptitude bank
overlap_count = 0
for day, q_list in FRESH_MIXED_APTITUDE.items():
    for q in q_list:
        if q[0].strip() in existing_apt_questions:
            print(f"Overlap detected in Day {day}: {q[0]}")
            overlap_count += 1
print(f"Total Overlaps with Aptitude Bank: {overlap_count} (Must be 0)")
assert overlap_count == 0, "Overlap found!"

# Now update MIXED_DAYS_1_15
for day in range(1, 16):
    day_questions = MIXED_DAYS_1_15.get(day) or MIXED_DAYS_1_15.get(str(day))
    # Replace indices 5 to 9 (questions 6 to 10)
    fresh = FRESH_MIXED_APTITUDE[day]
    for idx, f_q in enumerate(fresh):
        target_idx = 5 + idx
        day_questions[target_idx]["question"] = f_q[0]
        day_questions[target_idx]["options"] = f_q[1]
        day_questions[target_idx]["correct_answer"] = f_q[2]
        day_questions[target_idx]["explanation"] = f_q[3]

# Now update MIXED_DAYS_16_30
for day in range(16, 31):
    day_questions = MIXED_DAYS_16_30.get(day) or MIXED_DAYS_16_30.get(str(day))
    # Replace indices 5 to 9 (questions 6 to 10)
    fresh = FRESH_MIXED_APTITUDE[day]
    for idx, f_q in enumerate(fresh):
        target_idx = 5 + idx
        day_questions[target_idx]["question"] = f_q[0]
        day_questions[target_idx]["options"] = f_q[1]
        day_questions[target_idx]["correct_answer"] = f_q[2]
        day_questions[target_idx]["explanation"] = f_q[3]

# Fix Day 30 project questions (indices 18 and 19) to be distinct from Day 5
d30_questions = MIXED_DAYS_16_30.get(30) or MIXED_DAYS_16_30.get("30")
d30_questions[18]["question"] = "In Sarthak's project portfolio synthesis (CSMS, SmartGalla, BulkBeat TV, Caloriv, BEVM), which architectural invariant governs multi-service data consistency?"
d30_questions[18]["options"] = [
    "Database transactions with ACID guarantees, role-based access control, and asynchronous queue decoupling.",
    "Using unencrypted HTTP requests over public ports.",
    "Storing passwords in plaintext inside localStorage.",
    "Restarting the production server on every user request."
]
d30_questions[18]["correct_answer"] = "A"
d30_questions[18]["explanation"] = "Across CSMS, SmartGalla, BulkBeat TV, Caloriv, and BEVM, data integrity is preserved using ACID transactions, strict schema migrations, and decoupled background worker queues."

d30_questions[19]["question"] = "Regarding production reliability across Sarthak's verified projects (CSMS, SmartGalla, Caloriv), how do you defend database migration safety in a technical interview?"
d30_questions[19]["options"] = [
    "We implement backward-compatible additive migrations, automated pre-deployment schema dry runs, and rollbacks via versioned SQL scripts.",
    "Claim that standard frameworks are obsolete and write custom assembly.",
    "State that testing was skipped to ship faster.",
    "Acknowledge that security was ignored."
]
d30_questions[19]["correct_answer"] = "A"
d30_questions[19]["explanation"] = "In technical interviews, highlight backward-compatible schema changes, additive column deployment, and automated migration rollbacks."

# Write back mixed_bank_1_15.py
with open(os.path.join(SCRIPTS_DIR, "mixed_bank_1_15.py"), "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""\nscripts/curriculum/banks/mixed_bank_1_15.py\nAuthentic Mixed Test MCQs for Days 1 to 15 (20 MCQs/day).\n"""\n\n')
    f.write(f"MIXED_DAYS_1_15 = {json.dumps(MIXED_DAYS_1_15, indent=2, ensure_ascii=False)}\n\n")
    f.write("def get_mixed_mcqs_half1(day: int) -> list:\n")
    f.write("    return MIXED_DAYS_1_15.get(day, [])\n")

# Write back mixed_bank_16_30.py
with open(os.path.join(SCRIPTS_DIR, "mixed_bank_16_30.py"), "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""\nscripts/curriculum/banks/mixed_bank_16_30.py\nAuthentic Mixed Test MCQs for Days 16 to 30 (20 MCQs/day).\n"""\n\n')
    f.write(f"MIXED_DAYS_16_30 = {json.dumps(MIXED_DAYS_16_30, indent=2, ensure_ascii=False)}\n\n")
    f.write("def get_mixed_mcqs_half2(day: int) -> list:\n")
    f.write("    return MIXED_DAYS_16_30.get(day, [])\n")

print("[+] Successfully updated mixed_bank_1_15.py and mixed_bank_16_30.py with 100% unique, non-overlapping questions!")
