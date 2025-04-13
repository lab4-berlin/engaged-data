# Database Schema Documentation

## Overview
This document describes the database schema for the educational platform. The database is designed to manage institutions, educators, lectures, questions, and student responses.

## Tables

### Institution
Stores information about educational institutions.

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| created_at | TIMESTAMP | When the record was created |
| changed_at | TIMESTAMP | When the record was last modified |
| institution_name | VARCHAR(255) | Institution name |
| institution_location | VARCHAR(255) | Institution location |

### Educator
Stores information about educators (teachers, professors, etc.).

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| created_at | TIMESTAMP | When the record was created |
| changed_at | TIMESTAMP | When the record was last modified |
| educator_name | VARCHAR(255) | Educator's name |
| educator_speciality | VARCHAR(255) | Educator's area of expertise |

### Educator_Institution
Junction table for the many-to-many relationship between educators and institutions.

| Column | Type | Description |
|--------|------|-------------|
| educator_id | INTEGER | Foreign key to educator table |
| institution_id | INTEGER | Foreign key to institution table |
| created_at | TIMESTAMP | When the record was created |
| changed_at | TIMESTAMP | When the record was last modified |

### Lecture
Stores information about lectures/sessions.

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| created_at | TIMESTAMP | When the record was created |
| changed_at | TIMESTAMP | When the record was last modified |
| lecture_date | TIMESTAMP | Lecture date and time |
| lecture_title | VARCHAR(255) | Lecture title |
| educator_id | INTEGER | Foreign key to educator table |
| institution_id | INTEGER | Foreign key to institution table |

### Question
Stores questions asked during lectures.

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| created_at | TIMESTAMP | When the record was created |
| changed_at | TIMESTAMP | When the record was last modified |
| lecture_id | INTEGER | Foreign key to lecture table |
| question_text | TEXT | The question content |
| correct_answer_index | INTEGER | Index of the correct answer |
| question_created_at | TIMESTAMP | When the question was created |

### Answer_Option
Stores multiple choice options for questions.

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| created_at | TIMESTAMP | When the record was created |
| changed_at | TIMESTAMP | When the record was last modified |
| question_id | INTEGER | Foreign key to question table |
| answer_text | TEXT | The answer option text |
| option_index | INTEGER | Position of this answer option |

### Student_Answer
Stores anonymous student responses.

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| created_at | TIMESTAMP | When the record was created |
| changed_at | TIMESTAMP | When the record was last modified |
| question_id | INTEGER | Foreign key to question table |
| answer_option_id | INTEGER | Foreign key to answer_option table |
| device_id | VARCHAR(255) | Anonymous identifier for the device |
| answer_created_at | TIMESTAMP | When the answer was submitted |

## Indexes
The following indexes are created for performance optimization:

- `idx_lecture_educator` on `lecture(educator_id)`
- `idx_lecture_institution` on `lecture(institution_id)`
- `idx_question_lecture` on `question(lecture_id)`
- `idx_answer_option_question` on `answer_option(question_id)`
- `idx_student_answer_question` on `student_answer(question_id)`
- `idx_student_answer_device` on `student_answer(device_id)`

## Triggers
The following triggers are created to automatically manage timestamps:

- `update_institution_changed_at`: Updates `changed_at` when an institution record is modified
- `update_educator_changed_at`: Updates `changed_at` when an educator record is modified
- `update_educator_institution_changed_at`: Updates `changed_at` when an educator-institution relationship is modified
- `update_lecture_changed_at`: Updates `changed_at` when a lecture record is modified
- `update_question_changed_at`: Updates `changed_at` when a question record is modified
- `update_answer_option_changed_at`: Updates `changed_at` when an answer option record is modified
- `update_student_answer_changed_at`: Updates `changed_at` when a student answer record is modified

## Relationships

1. **Educator-Institution Relationship**
   - Many-to-many relationship
   - Managed through `educator_institution` junction table
   - CASCADE delete enabled

2. **Lecture Relationships**
   - Belongs to one educator and one institution
   - Must match an existing educator-institution pair

3. **Question Relationships**
   - Belongs to one lecture
   - Has multiple answer options
   - CASCADE delete enabled

4. **Answer Relationships**
   - Each student answer references one question and one answer option
   - Anonymous tracking through device_id
   - CASCADE delete enabled

## Constraints

1. **Primary Keys**
   - All tables have an auto-incrementing `id` as primary key
   - `educator_institution` has a composite primary key

2. **Foreign Keys**
   - All foreign key relationships have CASCADE delete enabled
   - Ensures referential integrity

3. **Unique Constraints**
   - `answer_option` has a unique constraint on `(question_id, option_index)`

## Notes

- The schema supports anonymous student responses through device_id
- All timestamps are automatically set to the current time when records are created
- The `changed_at` timestamp is automatically updated whenever a record is modified
- The schema is designed to maintain data integrity through foreign key constraints
- Indexes are created to optimize common query patterns 