# Data Warehousing – MindTrack

## Scenario

I am a Data Engineer at a platform that provides academic planning and tracking tools for university students. The company has developed the **MindTrack** application to help students organize study sessions, monitor their academic progress, and improve performance based on personalized analytics.

## Business Requirements

MindTrack collects data on users' study habits, academic results, and learning progress. The platform provides personalized insights and reports to help students optimize their time and performance during the semester.

## Core Business Goals

- **Study Effort Analysis**– Aggregate and visualize the time spent on each subject to track progress and identify areas needing attention.subject.

- **Study Consistency Trends** – Monitor how study habits evolve over time, highlighting increases or decreases in study effort per week.
- **Goal Achievement Insights** – Evaluate if students are meeting their learning targets and suggest improvements.

## Reports

- Time spent per subject vs. average grade
- Study session frequency by weekday
- Subjects with low topic coverage
- Grade trends over time
- Focus level distribution by session type

## Dashboards

- Total time studied per subject (weekly view)
- Progress coverage % by subject
- Grades before/after intense study periods
- Study planner adherence (planned vs. spontaneous sessions)

## KPIs

- % of syllabus covered
- Efficiency index (grade / time invested)
- Average session duration
- Sessions with focus level ≥ 4

## Data Warehouse Design

The data warehouse is hosted on the server `MindTrack` and the database is named `mindtrack_db`.

## Sources

### users

| Column Name       | Data Type    | Description                      |
| ----------------- | ------------ | -------------------------------- |
| user_id           | VARCHAR(20)  | Unique identifier of the student |
| first_name        | VARCHAR(50)  | Student's first name             |
| last_name         | VARCHAR(50)  | Student's last name              |
| birth_date        | DATE         | Student's date of birth          |
| email             | VARCHAR(100) | Email address                    |
| city              | VARCHAR(50)  | City of residence                |
| registration_date | DATE         | Date of account creation         |

### study_sessions

| Column Name      | Data Type    | Description                                |
| ---------------- | ------------ | ------------------------------------------ |
| session_id       | VARCHAR(50)  | Unique identifier of the session           |
| user_id          | VARCHAR(20)  | Student identifier                         |
| subject_name     | VARCHAR(50)  | Name of the academic subject               |
| topic_name       | VARCHAR(100) | Specific topic studied during the session  |
| date             | DATE         | Study session date                         |
| duration_minutes | INT          | Duration of session in minutes             |
| focus_level      | INT          | Self-reported focus level (1–5 scale)      |
| planned          | BOOLEAN      | Whether the session was planned in advance |

### subject_progress

| Column Name    | Data Type   | Description                           |
| -------------- | ----------- | ------------------------------------- |
| user_id        | VARCHAR(20) | Student identifier                    |
| subject_name   | VARCHAR(50) | Academic subject                      |
| total_topics   | INT         | Total number of topics in the subject |
| topics_covered | INT         | Number of topics already covered      |
| date_updated   | DATE        | Date of the latest progress update    |

### grades

| Column Name  | Data Type   | Description                         |
| ------------ | ----------- | ----------------------------------- |
| user_id      | VARCHAR(20) | Student identifier                  |
| subject_name | VARCHAR(50) | Academic subject                    |
| grade_value  | DECIMAL     | Grade received                      |
| exam_type    | VARCHAR(20) | Type of exam (quiz, midterm, final) |
| exam_date    | DATE        | Date of the exam                    |
