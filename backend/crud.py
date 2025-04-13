from sqlalchemy.orm import Session
import models
import schemas
from typing import List, Optional

# Institution CRUD
def get_institution(db: Session, institution_id: int):
    return db.query(models.Institution).filter(models.Institution.id == institution_id).first()

def get_institutions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Institution).offset(skip).limit(limit).all()

def create_institution(db: Session, institution: schemas.InstitutionCreate):
    db_institution = models.Institution(
        institution_name=institution.institution_name,
        institution_location=institution.institution_location
    )
    db.add(db_institution)
    db.commit()
    db.refresh(db_institution)
    return db_institution

def update_institution(db: Session, institution_id: int, institution: schemas.InstitutionUpdate):
    db_institution = get_institution(db, institution_id)
    if db_institution:
        update_data = institution.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_institution, key, value)
        db.commit()
        db.refresh(db_institution)
    return db_institution

def delete_institution(db: Session, institution_id: int):
    db_institution = get_institution(db, institution_id)
    if db_institution:
        db.delete(db_institution)
        db.commit()
        return True
    return False

# Educator CRUD
def get_educator(db: Session, educator_id: int):
    return db.query(models.Educator).filter(models.Educator.id == educator_id).first()

def get_educators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Educator).offset(skip).limit(limit).all()

def create_educator(db: Session, educator: schemas.EducatorCreate):
    db_educator = models.Educator(
        educator_name=educator.educator_name,
        educator_speciality=educator.educator_speciality
    )
    db.add(db_educator)
    db.commit()
    db.refresh(db_educator)
    return db_educator

def update_educator(db: Session, educator_id: int, educator: schemas.EducatorUpdate):
    db_educator = get_educator(db, educator_id)
    if db_educator:
        update_data = educator.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_educator, key, value)
        db.commit()
        db.refresh(db_educator)
    return db_educator

def delete_educator(db: Session, educator_id: int):
    db_educator = get_educator(db, educator_id)
    if db_educator:
        db.delete(db_educator)
        db.commit()
        return True
    return False

# Lecture CRUD
def get_lecture(db: Session, lecture_id: int):
    return db.query(models.Lecture).filter(models.Lecture.id == lecture_id).first()

def get_lectures(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lecture).offset(skip).limit(limit).all()

def create_lecture(db: Session, lecture: schemas.LectureCreate):
    db_lecture = models.Lecture(
        lecture_date=lecture.lecture_date,
        lecture_title=lecture.lecture_title,
        educator_id=lecture.educator_id,
        institution_id=lecture.institution_id
    )
    db.add(db_lecture)
    db.commit()
    db.refresh(db_lecture)
    return db_lecture

def update_lecture(db: Session, lecture_id: int, lecture: schemas.LectureUpdate):
    db_lecture = get_lecture(db, lecture_id)
    if db_lecture:
        update_data = lecture.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_lecture, key, value)
        db.commit()
        db.refresh(db_lecture)
    return db_lecture

def delete_lecture(db: Session, lecture_id: int):
    db_lecture = get_lecture(db, lecture_id)
    if db_lecture:
        db.delete(db_lecture)
        db.commit()
        return True
    return False

# Question CRUD
def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(
        lecture_id=question.lecture_id,
        question_text=question.question_text,
        correct_answer_index=question.correct_answer_index
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def update_question(db: Session, question_id: int, question: schemas.QuestionUpdate):
    db_question = get_question(db, question_id)
    if db_question:
        update_data = question.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_question, key, value)
        db.commit()
        db.refresh(db_question)
    return db_question

def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)
    if db_question:
        db.delete(db_question)
        db.commit()
        return True
    return False

# Answer Option CRUD
def get_answer_option(db: Session, answer_option_id: int):
    return db.query(models.AnswerOption).filter(models.AnswerOption.id == answer_option_id).first()

def get_answer_options(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AnswerOption).offset(skip).limit(limit).all()

def create_answer_option(db: Session, answer_option: schemas.AnswerOptionCreate):
    db_answer_option = models.AnswerOption(
        question_id=answer_option.question_id,
        answer_text=answer_option.answer_text,
        option_index=answer_option.option_index
    )
    db.add(db_answer_option)
    db.commit()
    db.refresh(db_answer_option)
    return db_answer_option

def update_answer_option(db: Session, answer_option_id: int, answer_option: schemas.AnswerOptionUpdate):
    db_answer_option = get_answer_option(db, answer_option_id)
    if db_answer_option:
        update_data = answer_option.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_answer_option, key, value)
        db.commit()
        db.refresh(db_answer_option)
    return db_answer_option

def delete_answer_option(db: Session, answer_option_id: int):
    db_answer_option = get_answer_option(db, answer_option_id)
    if db_answer_option:
        db.delete(db_answer_option)
        db.commit()
        return True
    return False

# Student Answer CRUD
def get_student_answer(db: Session, student_answer_id: int):
    return db.query(models.StudentAnswer).filter(models.StudentAnswer.id == student_answer_id).first()

def get_student_answers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StudentAnswer).offset(skip).limit(limit).all()

def get_student_answers_by_device(db: Session, device_id: str):
    return db.query(models.StudentAnswer).filter(models.StudentAnswer.device_id == device_id).all()

def create_student_answer(db: Session, student_answer: schemas.StudentAnswerCreate):
    db_student_answer = models.StudentAnswer(
        question_id=student_answer.question_id,
        answer_option_id=student_answer.answer_option_id,
        device_id=student_answer.device_id
    )
    db.add(db_student_answer)
    db.commit()
    db.refresh(db_student_answer)
    return db_student_answer

def update_student_answer(db: Session, student_answer_id: int, student_answer: schemas.StudentAnswerUpdate):
    db_student_answer = get_student_answer(db, student_answer_id)
    if db_student_answer:
        update_data = student_answer.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_student_answer, key, value)
        db.commit()
        db.refresh(db_student_answer)
    return db_student_answer

def delete_student_answer(db: Session, student_answer_id: int):
    db_student_answer = get_student_answer(db, student_answer_id)
    if db_student_answer:
        db.delete(db_student_answer)
        db.commit()
        return True
    return False 