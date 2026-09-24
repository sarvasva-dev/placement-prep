# Canonical Multidisciplinary Content Schema Contract

This document defines the strict, authoritative data contract between curriculum generators, daily JSON files, frontend views, and document exporters.

---

## 1. Daily Chapter Schema (`content/days/dayXX.json`)

Each file represents one day of preparation (Day 1 to Day 30) and contains the following root structure:

```json
{
  "day": 1,
  "title": "Day 01: Concept Name & DSA Pattern",
  "streams": { ... },
  "dsa": { ... },
  "coding": { ... }
}
```

---

## 2. Stream Definitions

### Stream 1: `academic` (Semester 5 Theory)
- `unit`: Integer (1 to 5)
- `subject_code`: String (e.g., `"BCA-5001"`)
- `subject_name`: String (e.g., `"Computer Network"`)
- `topic`: String
- `objectives`: Array of Strings
- `explanation`: String (multi-paragraph)
- `subtopics`: Array of `{"title": String, "content": String}`
- `diagram`: String (ASCII or structured text)
- `comparison_table`: `{"headers": Array of Strings, "rows": Array of Arrays}`
- `memorize`: String
- `understand`: String
- `common_mistakes`: String
- `exam_writing_guidance`: String
- `mcqs`: Array of 5 MCQs

### Stream 2: `academic_pyqs` (University Past Year Questions)
Array of 2 objects:
- `university`: `"CSJM University, Kanpur"`
- `subject`: String
- `year`: String (e.g., `"2023-24"`)
- `marks`: `"15 Marks"`
- `type`: `"15-MARK ANSWER PRESENTATION BLUEPRINT"`
- `question`: String (the actual exam question)
- `rubric`: String (e.g., `"Definition (3m) + Architecture Diagram (4m) + Protocol Mechanics (5m) + Summary (3m) = 15 Marks"`)
- `model_answer`: String (detailed, complete 15-mark answer)
- `expected_examiner_points`: String

### Stream 3: `academic_mcqs`
Array of 5 MCQs covering university syllabus topics.

### Stream 4: `aptitude_lesson`
- `topic`: String (e.g., `"Percentages & Fractional Multipliers"`)
- `category`: String (`"Quantitative"`, `"Logical Reasoning"`, or `"Verbal Ability"`)
- `subtopic`: String
- `tutorial`: Array of Strings (or multi-paragraph String)
- `formulas`: String
- `shortcuts`: String (30-second speed shortcut)

### Stream 5: `aptitude_solved` (5 Worked Examples)
Array of 5 objects:
- `example_no`: Integer (1 to 5)
- `tier`: String (e.g., `"Tier 1: Foundation Concept"`, `"Tier 2: Standard Placement"`)
- `difficulty`: String
- `source`: String (e.g., `"TCS NQT / Infosys Placement Pattern"`)
- `target_time_seconds`: Integer (typically 45 to 60)
- `title`: String
- `question`: String (non-empty, authentic problem statement)
- `problem`: Alias for `question`
- `step_by_step_solution`: Array of Strings (or multi-line String)
- `solution`: Alias for `step_by_step_solution`
- `final_answer`: String
- `answer`: Alias for `final_answer`

### Stream 6: `aptitude_mcqs` (10 Interactive Questions)
Array of 10 objects:
- `mcq_no`: Integer (1 to 10)
- `id`: String (e.g., `"APT-01-01"`)
- `company`: String (e.g., `"TCS NQT"`, `"Infosys"`, `"Cognizant"`)
- `question`: String
- `options`: Normalized Array of `{"letter": "A", "text": "..."}` or Object `{"A": "...", ...}`
- `correct_answer`: String (`"A"`, `"B"`, `"C"`, or `"D"`)
- `explanation`: String (step-by-step mathematical reasoning)

### Stream 7: `dsa_pattern` (and top-level `dsa`)
- `pattern_name`: String (e.g., `"Two Pointers (Opposite Direction)"`)
- `pattern`: Alias for `pattern_name`
- `title`: String
- `category`: String
- `concept`: String (algorithmic mechanism)
- `intuition`: String
- `why_it_works`: Alias for `intuition`
- `visual_explanation`: String (ASCII execution trace)
- `language`: `"Java"`
- `java_solution`: String (production Java 17+ code with `class Solution`)
- `java_code`: Alias for `java_solution`
- `code`: Alias for `java_solution`
- `line_by_line`: Array of Strings
- `line_by_line_walkthrough`: Alias for `line_by_line`
- `dry_run`: String
- `complexity`: String (e.g., `"O(N) Time, O(1) Auxiliary Space"`)
- `time_complexity`: String
- `space_complexity`: String
- `edge_cases`: String (and `edge_cases_list`: Array of Strings)
- `interview_variations`: Array of Strings

### Stream 8: `coding_problems` (and `coding.problems`)
Array of 2 objects:
- `problem_id`: String (e.g., `"CODE-01-01"`)
- `title`: String
- `difficulty`: String (`"Easy"`, `"Medium"`, or `"Hard"`)
- `companies`: Array of Strings
- `statement`: String (the problem text)
- `problem_statement`: Alias for `statement`
- `constraints`: String
- `examples`: Array of `{"input": String, "output": String, "explanation": String}`
- `approach`: String
- `solution_approach`: Alias for `approach`
- `java_solution`: String (complete Java 17+ class Solution)
- `java_code`: Alias for `java_solution`
- `solution_java`: Alias for `java_solution`
- `code`: Alias for `java_solution`
- `complexity`: String
- `time_complexity`: String
- `space_complexity`: String
- `edge_cases`: String or Array of Strings

### Stream 9: `core_cs`
- `subject`: String (`"Operating Systems"`, `"DBMS"`, `"Computer Networks"`, `"Java & Web"`)
- `topic`: String
- `lesson`: String (deep technical lecture)
- `concept_lesson`: Alias for `lesson`
- `lecture`: Alias for `lesson`
- `key_definitions`: Array of `{"term": String, "definition": String}`
- `interview_questions`: Array of `{"q": String, "a": String}` (5 items)
- `interview_qa`: Alias for `interview_questions`
- `mcqs`: Array of 5 MCQs

### Stream 10: `project_preparation` (and `project_defense`)
- `project_name`: String (`"SmartGalla"`, `"College Student Management System (CSMS)"`, `"NSE2 / BulkBeat TV"`, `"Caloriv"`, `"Biometric Electronic Voting System (BEVM)"`)
- `name`: Alias for `project_name`
- `repo_path`: String (local workstation path)
- `topic`: String (architectural feature focus)
- `what_to_understand`: String
- `what_to_memorize`: String
- `interview_questions`: Array of `{"q": String, "a": String}`
- `interview_qa`: Alias for `interview_questions`
- `interview_pitch_exercise`: String (60-second elevator pitch)

### Stream 11: `placement_interview`
Array of 5 objects:
- `category`: String (`"Technical Core"`, `"STAR Behavioral"`, `"System Design"`, `"HR & Leadership"`)
- `question`: String
- `model_answer`: String
- `key_talking_points`: Array of Strings
- `what_interviewer_evaluates`: String

### Stream 12: `daily_revision`
Object with 7 active recall sections:
- `yesterday_recall`: String
- `today_recall`: String
- `formula_recall`: String
- `pyq_recall`: String
- `dsa_recall`: String
- `project_recall`: String
- `rapid_fire_questions`: Array of 10 `{"q": String, "a": String}`

### Stream 13: `mixed_test` (20 MCQs)
Array of 20 objects (5 Academic + 5 Aptitude + 5 Core CS + 5 Coding/Project):
- `id`: String
- `category`: String
- `question`: String
- `options`: Normalized Array or Dictionary
- `correct_answer`: String (`"A"`, `"B"`, `"C"`, or `"D"`)
- `explanation`: String

### Stream 14: `daily_coding_task` (and `coding.timed_task`)
- `task_id`: String (e.g., `"TASK-01"`)
- `title`: String
- `time_limit_minutes`: Integer (typically 25 to 30)
- `difficulty`: String
- `statement`: String
- `problem_statement`: Alias for `statement`
- `input_format`: String
- `output_format`: String
- `starter_code`: String (Java 17+ template)
- `java_starter_code`: Alias for `starter_code`
- `solution_code`: String (Java 17+ complete solution)
- `java_solution_code`: Alias for `solution_code`
- `java_solution`: Alias for `solution_code`
- `test_cases`: Array of `{"input": String, "expected_output": String, "explanation": String}`
- `rubric`: Object

---

## 3. Global Aggregate Libraries

1. **`content/coding/all_coding.json`**:
   An array of individual solved problem entries:
   ```json
   {
     "day": 1,
     "problem_id": "CODE-01-01",
     "title": "Two Sum II – Input Array Is Sorted",
     "pattern": "Two Pointers (Opposite Direction)",
     "difficulty": "Easy",
     "problem": "Given a 1-indexed array of integers...",
     "statement": "Given a 1-indexed array of integers...",
     "intuition": "Apply Two Pointers...",
     "approach": "Apply Two Pointers...",
     "time_complexity": "O(N) Time",
     "space_complexity": "O(1) Auxiliary Space",
     "java_code": "public class Solution { ... }"
   }
   ```

2. **`content/projects/projects_all.json`**:
   Dictionary of 5 verified engineering projects with `name`, `category`, `repo_path`, `metrics`, `flow`, `resume`, and daily study `sessions`.
