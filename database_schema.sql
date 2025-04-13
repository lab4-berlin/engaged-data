-- Create institution table
CREATE TABLE institution (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    institution_name VARCHAR(255) NOT NULL,
    institution_location VARCHAR(255) NOT NULL
);

-- Create educator table
CREATE TABLE educator (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    educator_name VARCHAR(255) NOT NULL,
    educator_speciality VARCHAR(255) NOT NULL
);

-- Create junction table for educator-institution many-to-many relationship
CREATE TABLE educator_institution (
    educator_id INTEGER REFERENCES educator(id) ON DELETE CASCADE,
    institution_id INTEGER REFERENCES institution(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (educator_id, institution_id)
);

-- Create lecture table
CREATE TABLE lecture (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lecture_date TIMESTAMP NOT NULL,
    lecture_title VARCHAR(255) NOT NULL,
    educator_id INTEGER REFERENCES educator(id) ON DELETE CASCADE,
    institution_id INTEGER NOT NULL,
    FOREIGN KEY (educator_id, institution_id) 
        REFERENCES educator_institution(educator_id, institution_id)
);

-- Create question table
CREATE TABLE question (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lecture_id INTEGER REFERENCES lecture(id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    correct_answer_index INTEGER NOT NULL,
    question_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create answer_option table
CREATE TABLE answer_option (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    question_id INTEGER REFERENCES question(id) ON DELETE CASCADE,
    answer_text TEXT NOT NULL,
    option_index INTEGER NOT NULL,
    UNIQUE(question_id, option_index)
);

-- Create student_answer table
CREATE TABLE student_answer (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    question_id INTEGER REFERENCES question(id) ON DELETE CASCADE,
    answer_option_id INTEGER REFERENCES answer_option(id) ON DELETE CASCADE,
    device_id VARCHAR(255) NOT NULL,
    answer_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_lecture_educator ON lecture(educator_id);
CREATE INDEX idx_lecture_institution ON lecture(institution_id);
CREATE INDEX idx_question_lecture ON question(lecture_id);
CREATE INDEX idx_answer_option_question ON answer_option(question_id);
CREATE INDEX idx_student_answer_question ON student_answer(question_id);
CREATE INDEX idx_student_answer_device ON student_answer(device_id);

-- Create function to update changed_at timestamp
CREATE OR REPLACE FUNCTION update_changed_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.changed_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for each table
CREATE TRIGGER update_institution_changed_at
    BEFORE UPDATE ON institution
    FOR EACH ROW
    EXECUTE FUNCTION update_changed_at_column();

CREATE TRIGGER update_educator_changed_at
    BEFORE UPDATE ON educator
    FOR EACH ROW
    EXECUTE FUNCTION update_changed_at_column();

CREATE TRIGGER update_educator_institution_changed_at
    BEFORE UPDATE ON educator_institution
    FOR EACH ROW
    EXECUTE FUNCTION update_changed_at_column();

CREATE TRIGGER update_lecture_changed_at
    BEFORE UPDATE ON lecture
    FOR EACH ROW
    EXECUTE FUNCTION update_changed_at_column();

CREATE TRIGGER update_question_changed_at
    BEFORE UPDATE ON question
    FOR EACH ROW
    EXECUTE FUNCTION update_changed_at_column();

CREATE TRIGGER update_answer_option_changed_at
    BEFORE UPDATE ON answer_option
    FOR EACH ROW
    EXECUTE FUNCTION update_changed_at_column();

CREATE TRIGGER update_student_answer_changed_at
    BEFORE UPDATE ON student_answer
    FOR EACH ROW
    EXECUTE FUNCTION update_changed_at_column(); 