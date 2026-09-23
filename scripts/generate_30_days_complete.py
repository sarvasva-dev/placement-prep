#!/usr/bin/env python3
"""
scripts/generate_30_days_complete.py
Master Generator for the 30-Day Placement & Semester Study System.

Generates:
1. content/days/day01.json through day30.json (Complete, self-contained, canonical schemas with dual aliases)
2. content/days_index.json (Lightweight 30-day index for timeline navigation)
3. Global resource libraries:
   - content/pyqs/all_pyqs.json
   - content/aptitude/all_aptitude.json
   - content/coding/all_coding.json (Flattened 60 problems + 30 tasks for search/filtering)
   - content/core_cs/all_core_cs.json
   - content/projects/projects_all.json (Rich project metadata + daily study sessions)
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
CURRICULUM_DIR = os.path.join(SCRIPTS_DIR, "curriculum")
CONTENT_DIR = os.path.join(BASE_DIR, "content")
DAYS_DIR = os.path.join(CONTENT_DIR, "days")
os.makedirs(DAYS_DIR, exist_ok=True)
for sub in ["pyqs", "aptitude", "coding", "core_cs", "projects"]:
    os.makedirs(os.path.join(CONTENT_DIR, sub), exist_ok=True)

if CURRICULUM_DIR not in sys.path:
    sys.path.insert(0, CURRICULUM_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

import academic_curriculum
import aptitude_curriculum
import dsa_curriculum
import project_curriculum
import core_cs_curriculum
import placement_curriculum
import revision_curriculum
import mixed_tests_curriculum
import coding_tasks_curriculum
import gen_project_hub_data

def get_base_projects():
    """Initializes rich project metadata from gen_project_hub_data."""
    evidence_file = os.path.join(BASE_DIR, "evidence", "project_evidence.json")
    with open(evidence_file, "r", encoding="utf-8") as f:
        evidence = json.load(f)

    projects_hub = {}
    for proj in evidence:
        p_id = proj.get("project_id", "")
        p_name = proj.get("actual_project_name", "")

        if "CSMS" in p_id or "College Student Management System" in p_name:
            key = "csms"
            category = "Academic ERP & Multi-Role Administration"
            metrics = {
                "users": "VSICS Faculty, HOD & Student Cohort (CSJMU Kanpur)",
                "revenue": "Academic BCA 5th Sem Capstone Project",
                "verified_technical": "100% FastAPI + Supabase PostgreSQL + Vanilla JS • 6 Database Tables • 6 REST Endpoints • <75% Shortage Engine"
            }
            flow = [
                "1. User Authentication: Faculty & HOD authenticate via email; students authenticate via University Enrollment No. (e.g. CSJMA24000004738). Bcrypt verifies hash.",
                "2. Session Verification: FastAPI dependency injection verifies role privileges (HOD, Section Incharge, Faculty, Student) before granting route execution.",
                "3. Attendance Ingestion: Daily class attendance is recorded with compound unique constraint (student_id, record_date) to prevent duplicates.",
                "4. Shortage Calculation: Automated aggregation query detects attendance < 75% and flags student to HOD and Section Incharge.",
                "5. Academic Grading: Test scores from test_marks are aggregated into composite percentages, mapping to grades A-F.",
                "6. Fee Ledger: Dynamic calculation of Paid/Pending/Partial fees per student semester."
            ]
            resume = [
                "Architected College Student Management System (CSMS) for BCA 5th Semester project using FastAPI and Supabase PostgreSQL with Vanilla JS client.",
                "Engineered multi-role authentication with Bcrypt password hashing supporting HOD, Section Incharge, Faculty, and Student access levels.",
                "Designed relational PostgreSQL schema with compound unique constraints preventing duplicate daily attendance and automating <75% shortage alerts.",
                "Developed academic grading engine mapping composite test marks to letter grades and integrated semester fee ledger tracking balances."
            ]
        elif "SMARTGALLA" in p_id or "SmartGalla" in p_name:
            key = "smartgalla"
            category = "Hyper-Local Kirana Retail SaaS & Logistics"
            metrics = {
                "users": "Local Kirana & Retail Merchant Pilots",
                "revenue": "B2B SaaS Subscription + Razorpay Transaction Fees",
                "verified_technical": "Next.js 16 + React 19 + Supabase RLS + Serwist PWA + Razorpay Webhook Idempotency + Leaflet/Google Maps"
            }
            flow = [
                "1. Merchant Store Hydration: Next.js 16 App Router streams server components with zero client JS overhead for catalog views.",
                "2. Multi-Tenant Isolation: PostgreSQL Row-Level Security (RLS) policies enforce store isolation at the database layer.",
                "3. Payment Webhook Ingestion: Razorpay webhooks verify HMAC-SHA256 signatures with unique payment ID deduplication.",
                "4. COD Ledger Reconciliation: Double-entry delivery agent cash bags reconcile collected physical cash with OTP merchant handover.",
                "5. Geospatial Dispatch: Haversine distance ranking dispatches orders to nearest active delivery partners within a 5km geofence.",
                "6. Offline PWA Sync: Serwist service workers cache retail catalogs for uninterrupted order entry during wholesale market network drops."
            ]
            resume = [
                "Engineered SmartGalla multi-tenant retail SaaS using Next.js 16, React 19, Supabase RLS, and Tailwind CSS PostCSS 4.",
                "Implemented secure Razorpay payment gateway integration with HMAC-SHA256 signature verification and idempotent webhook event handlers.",
                "Designed double-entry Cash-on-Delivery (COD) reconciliation ledger and dispatch engine with 5km Haversine geofenced order routing.",
                "Developed offline-first PWA caching with Serwist service workers and automated competitive price intelligence worker with Playwright."
            ]
        elif "NSE" in p_id or "BulkBeat" in p_name:
            key = "nse2"
            category = "Financial Ingestion & Regulatory Surveillance"
            metrics = {
                "users": "Algorithmic Traders & HNI Portfolio Managers",
                "revenue": "Commercial Software Contract (Sitekraft.dev / Ref: SKD-2026-BLK-001)",
                "verified_technical": "Python 3.10+ AsyncIO (aiohttp) + SQLite WAL Concurrency + Dhan API v2 + Telegram Webhook Worker"
            }
            flow = [
                "1. Market Feed Ingestion: Asynchronous aiohttp client continuously polls NSE circulars, corporate announcements, and bulk deals.",
                "2. Concurrency Isolation: SQLite configured with Write-Ahead Logging (WAL) and busy_timeout=5000ms enables concurrent writes without database lock contention.",
                "3. Signal Filtering: NLP keywords and corporate filing regex extract high-impact catalysts (mergers, buybacks, board meetings).",
                "4. Dhan Broker Bridge: Order execution gateway integrates Dhan API v2 for rapid position entry upon verified regulatory disclosures.",
                "5. Real-Time Telegram Broadcast: Async webhook dispatcher sends formatted alerts with direct exchange document links to subscriber channels."
            ]
            resume = [
                "Developed high-throughput market intelligence platform (NSE2 / BulkBeat TV) monitoring real-time regulatory filings and corporate actions.",
                "Architected asynchronous ingestion pipeline in Python using aiohttp, polling NSE feeds with resilient exponential backoff retry policies.",
                "Configured SQLite Write-Ahead Logging (WAL) mode with busy timeout handling, achieving concurrent reader-writer operations without locking.",
                "Integrated Dhan Broker API v2 for automated trade execution and built Telegram webhook worker delivering real-time filing intelligence."
            ]
        elif "CALORIV" in p_id or "Caloriv" in p_name:
            key = "caloriv"
            category = "Mobile Nutrition Intelligence & Offline Analytics"
            metrics = {
                "users": "Android Health & Fitness Beta Users",
                "revenue": "Freemium Mobile App Architecture",
                "verified_technical": "React Native Expo + Gradle Build Toolchain + SQLite WatermelonDB Offline Sync + Macro Nutrient Analytics"
            }
            flow = [
                "1. User Intake Logging: React Native Expo interface captures daily caloric, macronutrient, and micronutrient intake.",
                "2. Local-First Storage: WatermelonDB / SQLite local storage records intake events instantly with zero network latency.",
                "3. Delta Sync Engine: Background synchronization worker pushes batched meal logs to cloud API when network connectivity resumes.",
                "4. Nutrition Derivation: Automated macro engine computes Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE).",
                "5. Native Build Orchestration: Custom Gradle build pipeline compiles hermetic Android APKs with ProGuard code shrinking."
            ]
            resume = [
                "Developed Caloriv cross-platform mobile nutrition analytics application using React Native Expo and TypeScript.",
                "Implemented offline-first data persistence using local SQLite storage with background delta synchronization for cloud backup.",
                "Engineered automated macronutrient derivation algorithms calculating BMR, TDEE, and daily target calorie distributions.",
                "Configured production Android Gradle build orchestration with ProGuard optimization and hermetic asset bundling."
            ]
        elif "CFTN" in p_id or "Code for the Nation" in p_name:
            key = "cftn"
            category = "Civic Tech Platform & Open Source Community"
            metrics = {
                "users": "Open Source Developers & Civic Contributors",
                "revenue": "Public Good / Open Source Initiative",
                "verified_technical": "Full-Stack Web Portal + GitHub OAuth + Contribution Tracking + Resource Aggregation"
            }
            flow = [
                "1. Developer Onboarding: Contributors authenticate via GitHub OAuth.",
                "2. Civic Project Registry: Public repository catalog lists active civic technology initiatives.",
                "3. Contribution Tracking: Webhook receiver monitors PR merges and commits, updating community leaderboards.",
                "4. Resource Hub: Curated guides for contributing to digital public infrastructure."
            ]
            resume = [
                "Contributed to Code for the Nation civic technology platform, building contributor onboarding and project directory modules.",
                "Integrated GitHub OAuth authentication and webhook handlers to track community contributions and repository activity.",
                "Designed responsive user interfaces using modern CSS and accessible component patterns for public open source collaboration."
            ]
        else:
            continue

        used = [t["tech"] for t in proj.get("verified_technologies", []) if t.get("classification") == "DIRECTLY_VERIFIED_USED"]
        understood = [
            "PostgreSQL Concurrency & ACID Guarantees",
            "RESTful API & Swagger OpenAPI Standards",
            "Asynchronous Event Loops & Worker Pipelines",
            "Row-Level Security & Cryptographic Hashing"
        ]
        explored = [
            "Distributed Message Queues (Kafka / RabbitMQ)",
            "Kubernetes Orchestration & Helm Charts"
        ]

        interview_defense = []
        if key == "csms":
            interview_defense = [
                {
                    "q": "Walk me through the architecture and purpose of your College Student Management System (CSMS).",
                    "a": "I developed CSMS as a cloud-native Educational ERP for my BCA 5th Semester project under Prof. Nitin Mishra at VSICS, CSJMU. Built with FastAPI and Supabase Cloud PostgreSQL with a lightweight Vanilla JS frontend, it automates student lifecycle management across four roles: HOD, Section Incharge, Faculty, and Students. It covers attendance tracking with automated <75% shortage alerts, internal test mark entry with auto-grade calculation, semester fee balance monitoring, and official HOD circular distribution."
                },
                {
                    "q": "How does the attendance shortage engine detect defaulters?",
                    "a": "In schema.sql, the attendance table enforces a composite unique constraint on (student_id, record_date). An automated FastAPI aggregation endpoint calculates total present days over total recorded class sessions. When a student's percentage drops below 75%, the engine flags the record, placing them on the HOD and Section Incharge defaulter roster."
                },
                {
                    "q": "Why use Vanilla JS instead of a heavyweight framework like React for CSMS?",
                    "a": "For an internal college administration portal, zero build overhead and instant browser loading on lab computers with low memory were primary requirements. Vanilla ES6+ JavaScript with native Fetch API consumes less than 20MB of RAM, requires no Webpack/Babel compilation steps, and provides instant cold-start times on any institutional device."
                }
            ]
        elif key == "smartgalla":
            interview_defense = [
                {
                    "q": "Why did you choose Next.js 16 with Supabase for SmartGalla?",
                    "a": "SmartGalla is a multi-tenant retail platform where catalog SEO, fast cold starts, and tenant isolation are vital. Next.js 16 Server Components stream HTML with sub-800ms FCP, while Supabase provides PostgreSQL with Row-Level Security (RLS) to enforce tenant isolation at the database layer rather than relying entirely on application code."
                },
                {
                    "q": "How do you handle Razorpay webhook idempotency?",
                    "a": "Incoming webhooks contain unique razorpay_payment_id values. We record every event in a dedicated payment_transactions table with a UNIQUE constraint. If an event is received twice due to network retries, the duplicate insert fails gracefully and returns HTTP 200 immediately, preventing duplicate order fulfillments."
                }
            ]
        elif key == "nse2":
            interview_defense = [
                {
                    "q": "How do you achieve high concurrency without database lockups in NSE2?",
                    "a": "We configured SQLite in Write-Ahead Logging (WAL) mode with PRAGMA journal_mode=WAL and PRAGMA busy_timeout=5000. In WAL mode, writes append to a separate WAL file, allowing concurrent read operations without blocking writers, while busy_timeout prevents SQLITE_BUSY lock exceptions during concurrent ingestion."
                },
                {
                    "q": "How does the ingestion crawler handle exchange rate limits?",
                    "a": "The aiohttp crawler uses jittered exponential backoff retries, user-agent rotation, and session connection pooling to respect exchange boundaries while maintaining sub-second alert latency."
                }
            ]
        elif key == "caloriv":
            interview_defense = [
                {
                    "q": "How does Caloriv handle meal tracking when the user has no internet connection?",
                    "a": "Caloriv employs a local-first offline architecture using SQLite. Meal logs are saved locally first with immediate UI updates. A background delta sync worker monitors network state and synchronizes dirty local records with the cloud API when connectivity is restored."
                }
            ]
        else:
            interview_defense = [
                {
                    "q": f"What was your primary technical contribution to {p_name}?",
                    "a": "I designed and implemented core modules with clean separation of concerns, secure authentication, and robust error handling backed by automated testing."
                }
            ]

        projects_hub[key] = {
            "name": p_name,
            "category": category,
            "repo_path": proj.get("source_paths", [""])[0],
            "git_remote": proj.get("git_remote", ""),
            "academic_context": proj.get("academic_context", ""),
            "metrics": metrics,
            "tech_stack": {
                "used": used,
                "understood": understood,
                "explored": explored
            },
            "architecture_flow": flow,
            "interview_defense": interview_defense,
            "resume_bullets": resume,
            "sessions": []
        }

    return projects_hub

def generate_all():
    print("=" * 60)
    print("STARTING 30-DAY MASTER CONTENT GENERATION WITH CANONICAL SCHEMAS")
    print("=" * 60)

    days_index = []
    all_pyqs = []
    all_aptitude = []
    all_coding = []
    all_core_cs = []
    all_projects = get_base_projects()

    for day in range(1, 31):
        print(f"Generating Day {day:02d}...", end=" ")

        # 1. Academic Module
        acad = academic_curriculum.get_academic_for_day(day)
        day_pyqs = acad.get("pyqs", [])
        all_pyqs.extend(day_pyqs)

        # 2. Aptitude Module & Solved Normalization
        apt = aptitude_curriculum.get_aptitude_for_day(day)
        norm_solved = []
        for s_idx, ex in enumerate(apt.get("solved_examples", [])):
            q_text = ex.get("question", ex.get("problem", ""))
            sol_text = ex.get("step_by_step_solution", ex.get("solution", []))
            ans_text = ex.get("final_answer", ex.get("answer", ""))
            t_title = ex.get("title", f"Tier {s_idx + 1}: Worked Placement Problem")
            norm_solved.append({
                "example_no": s_idx + 1,
                "title": t_title,
                "tier": f"Tier {s_idx + 1}: " + ("Foundation Concept" if s_idx == 0 else "Standard Placement" if s_idx == 1 else "Company Exam Pattern" if s_idx == 2 else "Time-Pressure Challenge"),
                "difficulty": f"Tier {s_idx + 1}",
                "source": ex.get("source", "Placement Exam Pattern"),
                "target_time_seconds": ex.get("target_time_seconds", 45),
                "question": q_text,
                "problem": q_text,
                "step_by_step_solution": sol_text,
                "solution": sol_text,
                "final_answer": ans_text,
                "answer": ans_text
            })

        # 3. DSA Module & Problem Normalization
        dsa = dsa_curriculum.get_dsa_for_day(day)
        norm_coding_probs = []
        for c_idx, p in enumerate(dsa.get("coding_problems", [])):
            stmt = p.get("statement", p.get("problem_statement", ""))
            appr = p.get("approach", p.get("solution_approach", ""))
            java_c = p.get("solution_java", p.get("java_code", p.get("code", "")))
            t_comp = p.get("time_complexity", "O(N) Time")
            s_comp = p.get("space_complexity", "O(1) Auxiliary Space")
            prob_obj = {
                "problem_id": p.get("problem_id", f"CODE-{day:02d}-{c_idx + 1}"),
                "title": p.get("title", f"Problem {c_idx + 1}"),
                "difficulty": p.get("difficulty", "Medium"),
                "companies": p.get("companies", ["TCS NQT", "Infosys", "Wipro", "Cognizant"]),
                "statement": stmt,
                "problem_statement": stmt,
                "problem": stmt,
                "constraints": p.get("constraints", "Standard campus placement execution budget: 1.0 second."),
                "example_input": p.get("example_input", "Standard sample test case input"),
                "example_output": p.get("example_output", "Expected test case output"),
                "examples": p.get("examples", [{"input": p.get("example_input", ""), "output": p.get("example_output", "")}]),
                "approach": appr,
                "solution_approach": appr,
                "intuition": appr,
                "java_solution": java_c,
                "java_code": java_c,
                "solution_java": java_c,
                "code": java_c,
                "time_complexity": t_comp,
                "space_complexity": s_comp,
                "complexity": f"{t_comp}, {s_comp}",
                "edge_cases": p.get("edge_cases", p.get("constraints", ""))
            }
            norm_coding_probs.append(prob_obj)

            # Flatten into all_coding for global directory
            all_coding.append({
                "day": day,
                "pattern": dsa.get("pattern_name", ""),
                "problem_id": prob_obj["problem_id"],
                "title": prob_obj["title"],
                "difficulty": prob_obj["difficulty"],
                "companies": prob_obj["companies"],
                "problem": stmt,
                "statement": stmt,
                "intuition": appr,
                "approach": appr,
                "time_complexity": t_comp,
                "space_complexity": s_comp,
                "java_code": java_c,
                "code": java_c
            })

        pat_name = dsa.get("pattern_name", "")
        j_code = dsa.get("java_code", dsa.get("code", dsa.get("java_solution", "")))
        why = dsa.get("why_it_works", dsa.get("concept", ""))
        lbl = dsa.get("line_by_line_walkthrough", dsa.get("line_by_line", []))
        dsa_norm = {
            "pattern_name": pat_name,
            "pattern": pat_name,
            "title": f"{pat_name} — Algorithmic Invariants & Implementation",
            "category": dsa.get("category", "Algorithmic Pattern"),
            "concept": dsa.get("concept", ""),
            "why_it_works": why,
            "intuition": why,
            "visual_explanation": dsa.get("visual_explanation", ""),
            "language": "Java",
            "java_code": j_code,
            "java_solution": j_code,
            "code": j_code,
            "line_by_line_walkthrough": lbl,
            "line_by_line": lbl,
            "dry_run": dsa.get("dry_run", ""),
            "complexity": dsa.get("complexity", "O(N) Time, O(1) Auxiliary Space"),
            "time_complexity": dsa.get("complexity", "O(N) Time").split(",")[0].strip(),
            "space_complexity": dsa.get("complexity", "O(1) Space").split(",")[-1].strip() if "," in dsa.get("complexity", "") else "O(1) Auxiliary Space",
            "edge_cases": ", ".join(dsa.get("edge_cases", [])) if isinstance(dsa.get("edge_cases"), list) else str(dsa.get("edge_cases", "")),
            "edge_cases_list": dsa.get("edge_cases", []) if isinstance(dsa.get("edge_cases"), list) else [str(dsa.get("edge_cases", ""))],
            "interview_variations": dsa.get("interview_variations", []),
            "problem": {
                "title": norm_coding_probs[0]["title"] if norm_coding_probs else pat_name,
                "statement": norm_coding_probs[0]["statement"] if norm_coding_probs else "",
                "input": norm_coding_probs[0]["example_input"] if norm_coding_probs else "",
                "output": norm_coding_probs[0]["example_output"] if norm_coding_probs else "",
                "examples": norm_coding_probs[0].get("examples", []) if norm_coding_probs else []
            }
        }

        # 4. Timed Practical Coding Challenge
        task = coding_tasks_curriculum.get_coding_task_for_day(day)
        t_stmt = task.get("problem_statement", task.get("statement", ""))
        t_starter = task.get("java_starter_code", task.get("starter_code", ""))
        t_sol = task.get("java_solution_code", task.get("solution_code", ""))
        task_norm = {
            "task_id": task.get("task_id", f"TASK-{day:02d}"),
            "title": task.get("title", f"Day {day:02d} Coding Challenge"),
            "time_limit_minutes": task.get("time_limit_minutes", 30),
            "difficulty": task.get("difficulty", "Medium"),
            "problem_statement": t_stmt,
            "statement": t_stmt,
            "input_format": task.get("input_format", "Standard Java method parameters."),
            "output_format": task.get("output_format", "Calculated optimal return value."),
            "starter_code": t_starter,
            "java_starter_code": t_starter,
            "solution_code": t_sol,
            "java_solution_code": t_sol,
            "java_solution": t_sol,
            "test_cases": task.get("test_cases", []),
            "rubric": task.get("rubric", {})
        }

        # 5. Core CS
        cs = core_cs_curriculum.get_core_cs_for_day(day)
        cs_norm = {
            "subject": cs.get("subject", ""),
            "topic": cs.get("topic", ""),
            "lesson": cs.get("concept_lesson", cs.get("lesson", "")),
            "concept_lesson": cs.get("concept_lesson", cs.get("lesson", "")),
            "lecture": cs.get("concept_lesson", cs.get("lesson", "")),
            "key_definitions": cs.get("key_definitions", []),
            "interview_questions": cs.get("interview_questions", []),
            "interview_qa": cs.get("interview_questions", []),
            "mcqs": cs.get("mcqs", [])
        }

        # 6. Project Preparation
        proj = project_curriculum.get_project_for_day(day)
        p_name = proj.get("project_name", "")
        proj_norm = {
            "project_name": p_name,
            "name": p_name,
            "repo_path": proj.get("repo_path", ""),
            "topic": proj.get("topic", ""),
            "feature_focus": proj.get("topic", ""),
            "what_to_understand": proj.get("what_to_understand", ""),
            "architecture_deep_dive": f"WHAT TO UNDERSTAND:\n{proj.get('what_to_understand', '')}\n\nWHAT TO MEMORIZE:\n{proj.get('what_to_memorize', '')}\n\n60-SECOND INTERVIEW PITCH:\n{proj.get('interview_pitch_exercise', '')}",
            "what_to_memorize": proj.get("what_to_memorize", ""),
            "interview_questions": proj.get("interview_questions", []),
            "interview_qa": proj.get("interview_questions", []),
            "interview_pitch_exercise": proj.get("interview_pitch_exercise", ""),
            "pitch": proj.get("interview_pitch_exercise", "")
        }

        # Associate session with global projects hub
        target_p_key = None
        if "CSMS" in p_name or "College Student" in p_name:
            target_p_key = "csms"
        elif "SmartGalla" in p_name:
            target_p_key = "smartgalla"
        elif "NSE" in p_name or "BulkBeat" in p_name:
            target_p_key = "nse2"
        elif "Caloriv" in p_name:
            target_p_key = "caloriv"
        elif "Code for the Nation" in p_name or "CFTN" in p_name:
            target_p_key = "cftn"

        if target_p_key and target_p_key in all_projects:
            all_projects[target_p_key]["sessions"].append({
                "day": day,
                "topic": proj.get("topic", ""),
                "understand": proj.get("what_to_understand", ""),
                "memorize": proj.get("what_to_memorize", ""),
                "interview_qa": proj.get("interview_questions", []),
                "pitch": proj.get("interview_pitch_exercise", "")
            })

        # 7. Placement Interview
        place = placement_curriculum.get_placement_for_day(day)

        # 8. Daily Revision
        rev = revision_curriculum.get_revision_for_day(day)

        # 9. Mixed Test
        mixed = mixed_tests_curriculum.get_mixed_test_for_day(day)

        # 10. Daily Score Model
        score_model = {
            "total_points": 100,
            "passing_threshold": 80,
            "breakdown": {
                "academic": 15,
                "aptitude": 15,
                "dsa_coding": 20,
                "core_cs": 15,
                "project": 10,
                "placement_interview": 10,
                "mixed_test": 10,
                "practical_task": 5
            }
        }

        # Header Titles
        subject_name = acad.get("subject_name", "Academic Theory")
        topic_name = acad.get("topic", "Core Curriculum")
        day_title = f"Day {day:02d}: {topic_name.split('—')[-1].strip() if '—' in topic_name else topic_name} & {pat_name}"

        # 14 Canonical Streams Container
        streams = {
            "academic": acad,
            "academic_pyqs": day_pyqs,
            "academic_mcqs": acad.get("mcqs", []),
            "aptitude_lesson": {
                "topic": apt.get("topic", ""),
                "category": apt.get("category", ""),
                "subtopic": apt.get("subtopic", ""),
                "formulas": apt.get("formulas", ""),
                "shortcuts": apt.get("shortcuts", ""),
                "tutorial": apt.get("tutorial", [])
            },
            "aptitude_solved": norm_solved,
            "aptitude_mcqs": apt.get("mcqs", []),
            "aptitude_practice": apt.get("practice_problems", []),
            "aptitude_timed_drill": apt.get("timed_drill", {}),
            "dsa_pattern": dsa_norm,
            "coding_problems": norm_coding_probs,
            "core_cs": cs_norm,
            "project_preparation": proj_norm,
            "placement_interview": place,
            "daily_revision": rev,
            "mixed_test": mixed,
            "daily_coding_task": task_norm,
            "daily_score_model": score_model
        }

        # Backward-compatible structures for existing UI renderers
        sem_data = {
            "subject": subject_name,
            "subject_code": acad.get("subject_code", ""),
            "unit": acad.get("unit", 1),
            "topic": acad.get("topic", ""),
            "objectives": acad.get("objectives", []),
            "detailed_notes": [acad.get("explanation", "")] + [s.get("content", "") for s in acad.get("subtopics", [])],
            "diagram_ascii": acad.get("diagram", ""),
            "comparison_table": acad.get("comparison_table"),
            "memorize": acad.get("memorize", ""),
            "understand": acad.get("understand", ""),
            "common_mistakes": acad.get("common_mistakes", ""),
            "pyqs": day_pyqs,
            "mcqs": acad.get("mcqs", []),
            "pyq_year": day_pyqs[0].get("year", "CSJM University") if day_pyqs else "CSJMU",
            "pyq_freq": "Verified University Paper Question",
            "pyq_question": day_pyqs[0].get("question", "") if day_pyqs else "",
            "pyq_rubric": day_pyqs[0].get("rubric", "") if day_pyqs else "",
            "model_answer_paragraphs": [
                ("1. Model Answer & Technical Presentation", day_pyqs[0].get("model_answer", "")),
                ("2. Expected Examiner Criteria", day_pyqs[0].get("expected_examiner_points", ""))
            ] if day_pyqs else []
        }

        apt_data = {
            "topic": apt.get("topic", ""),
            "category": apt.get("category", ""),
            "subtopic": apt.get("subtopic", ""),
            "formulas": apt.get("formulas", ""),
            "shortcut": apt.get("shortcuts", ""),
            "tutorial": apt.get("tutorial", []),
            "tier1_problem": norm_solved[0]["question"] if len(norm_solved) > 0 else "",
            "tier1_solution": "\n".join(norm_solved[0]["step_by_step_solution"]) if len(norm_solved) > 0 and isinstance(norm_solved[0]["step_by_step_solution"], list) else norm_solved[0].get("step_by_step_solution", "") if len(norm_solved) > 0 else "",
            "tier2_problem": norm_solved[1]["question"] if len(norm_solved) > 1 else "",
            "tier2_solution": "\n".join(norm_solved[1]["step_by_step_solution"]) if len(norm_solved) > 1 and isinstance(norm_solved[1]["step_by_step_solution"], list) else norm_solved[1].get("step_by_step_solution", "") if len(norm_solved) > 1 else "",
            "tier3_problem": norm_solved[2]["question"] if len(norm_solved) > 2 else "",
            "tier3_solution": "\n".join(norm_solved[2]["step_by_step_solution"]) if len(norm_solved) > 2 and isinstance(norm_solved[2]["step_by_step_solution"], list) else norm_solved[2].get("step_by_step_solution", "") if len(norm_solved) > 2 else "",
            "tier4_problem": norm_solved[3]["question"] if len(norm_solved) > 3 else "",
            "tier4_solution": "\n".join(norm_solved[3]["step_by_step_solution"]) if len(norm_solved) > 3 and isinstance(norm_solved[3]["step_by_step_solution"], list) else norm_solved[3].get("step_by_step_solution", "") if len(norm_solved) > 3 else "",
            "speed_drills": [{"q": ex["question"], "a": ex["final_answer"]} for ex in norm_solved],
            "solved_examples": norm_solved,
            "mcqs": apt.get("mcqs", []),
            "practice_problems": apt.get("practice_problems", []),
            "timed_drill": apt.get("timed_drill", {})
        }

        daily_test = {
            "title": f"Day {day:02d} Mixed Mastery Test (20 MCQs)",
            "questions": [{"q": m.get("question", ""), "a": f"Answer: {m.get('correct_answer')}\n\n{m.get('explanation')}"} for m in mixed[:8]],
            "mcqs": mixed
        }

        # Build Complete Day Object with Part 3 & Part 4 canonical top-level contracts
        day_payload = {
            "day": day,
            "title": day_title,
            "streams": streams,
            "dsa": dsa_norm,
            "coding": {
                "problems": norm_coding_probs,
                "timed_task": task_norm
            },
            "sem_data": sem_data,
            "apt_data": apt_data,
            "dsa_problems": norm_coding_probs,
            "dsa_pattern": dsa_norm,
            "cs_core": cs_norm,
            "project_defense": proj_norm,
            "placement_interview": place,
            "daily_revision": rev,
            "daily_test": daily_test,
            "daily_coding_task": task_norm,
            "daily_score_model": score_model
        }

        # Save day file
        day_file = os.path.join(DAYS_DIR, f"day{day:02d}.json")
        with open(day_file, "w", encoding="utf-8") as f:
            json.dump(day_payload, f, indent=2, ensure_ascii=False)

        # Index entry
        days_index.append({
            "day": day,
            "title": day_title,
            "subject": subject_name,
            "topic": topic_name,
            "aptitude": apt.get("topic", ""),
            "dsa_pattern": pat_name,
            "dsa": [p.get("title", "") for p in norm_coding_probs],
            "cs_core_topic": cs.get("topic", ""),
            "project": p_name
        })

        # Global aptitude library
        all_aptitude.append({
            "day": day,
            "topic": apt.get("topic", ""),
            "category": apt.get("category", ""),
            "formulas": apt.get("formulas", ""),
            "shortcuts": apt.get("shortcuts", ""),
            "solved_examples": norm_solved,
            "mcqs": apt.get("mcqs", [])
        })

        # Global core CS library
        all_core_cs.append({
            "day": day,
            "subject": cs.get("subject", ""),
            "topic": cs.get("topic", ""),
            "lesson": cs_norm["lesson"],
            "lecture": cs_norm["lecture"],
            "definitions": cs.get("key_definitions", []),
            "interview_questions": cs.get("interview_questions", []),
            "interview_qa": cs.get("interview_questions", []),
            "mcqs": cs.get("mcqs", [])
        })

        print("DONE")

    # Save Days Index
    with open(os.path.join(CONTENT_DIR, "days_index.json"), "w", encoding="utf-8") as f:
        json.dump(days_index, f, indent=2, ensure_ascii=False)
    print(f"\n[+] Saved content/days_index.json ({len(days_index)} days)")

    # Save Global PYQs Library
    with open(os.path.join(CONTENT_DIR, "pyqs", "all_pyqs.json"), "w", encoding="utf-8") as f:
        json.dump(all_pyqs, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/pyqs/all_pyqs.json ({len(all_pyqs)} authentic PYQs)")

    # Save Global Aptitude Library
    with open(os.path.join(CONTENT_DIR, "aptitude", "all_aptitude.json"), "w", encoding="utf-8") as f:
        json.dump(all_aptitude, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/aptitude/all_aptitude.json ({len(all_aptitude)} daily modules)")

    # Save Global Coding Library (flattened 60 problems)
    with open(os.path.join(CONTENT_DIR, "coding", "all_coding.json"), "w", encoding="utf-8") as f:
        json.dump(all_coding, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/coding/all_coding.json ({len(all_coding)} individual problem entries)")

    # Save Global Core CS Library
    with open(os.path.join(CONTENT_DIR, "core_cs", "all_core_cs.json"), "w", encoding="utf-8") as f:
        json.dump(all_core_cs, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/core_cs/all_core_cs.json ({len(all_core_cs)} lessons and interview sets)")

    # Note: content/projects/projects_all.json is strictly maintained by scripts/gen_project_hub_data.py
    # and MUST NOT be overwritten here.

    print("\n" + "=" * 60)
    print("SUCCESS: ALL 30 DAYS AND RESOURCE LIBRARIES COMPILED CLEANLY!")
    print("=" * 60)

if __name__ == "__main__":
    generate_all()
