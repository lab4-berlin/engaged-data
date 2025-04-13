from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv
from typing import List
import models
import schemas
import crud
from database import SessionLocal, engine
from sqladmin import Admin, ModelView
from admin import (InstitutionAdmin, EducatorAdmin, LectureAdmin, 
                  QuestionAdmin, AnswerOptionAdmin, StudentAnswerAdmin)

# Load environment variables
load_dotenv()

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/engaged_data")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="Engaged Data API",
    description="API for managing educational data including institutions, educators, lectures, questions, and student answers",
    version="1.0.0"
)

# Set up admin interface
admin = Admin(app, engine)

# Add model views to admin
admin.add_view(InstitutionAdmin)
admin.add_view(EducatorAdmin)
admin.add_view(LectureAdmin)
admin.add_view(QuestionAdmin)
admin.add_view(AnswerOptionAdmin)
admin.add_view(StudentAnswerAdmin)

@app.get("/")
async def root():
    return {"message": "Welcome to the Engaged Data API"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Institution endpoints
@app.post("/institutions/", response_model=schemas.Institution)
def create_institution(institution: schemas.InstitutionCreate, db: Session = Depends(get_db)):
    return crud.create_institution(db=db, institution=institution)

@app.get("/institutions/", response_model=List[schemas.Institution])
def read_institutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    institutions = crud.get_institutions(db, skip=skip, limit=limit)
    return institutions

@app.get("/institutions/{institution_id}", response_model=schemas.Institution)
def read_institution(institution_id: int, db: Session = Depends(get_db)):
    db_institution = crud.get_institution(db, institution_id=institution_id)
    if db_institution is None:
        raise HTTPException(status_code=404, detail="Institution not found")
    return db_institution

@app.put("/institutions/{institution_id}", response_model=schemas.Institution)
def update_institution(institution_id: int, institution: schemas.InstitutionUpdate, db: Session = Depends(get_db)):
    db_institution = crud.update_institution(db, institution_id=institution_id, institution=institution)
    if db_institution is None:
        raise HTTPException(status_code=404, detail="Institution not found")
    return db_institution

@app.delete("/institutions/{institution_id}")
def delete_institution(institution_id: int, db: Session = Depends(get_db)):
    success = crud.delete_institution(db, institution_id=institution_id)
    if not success:
        raise HTTPException(status_code=404, detail="Institution not found")
    return {"message": "Institution deleted successfully"}

# Educator endpoints
@app.post("/educators/", response_model=schemas.Educator)
def create_educator(educator: schemas.EducatorCreate, db: Session = Depends(get_db)):
    return crud.create_educator(db=db, educator=educator)

@app.get("/educators/", response_model=List[schemas.Educator])
def read_educators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    educators = crud.get_educators(db, skip=skip, limit=limit)
    return educators

@app.get("/educators/{educator_id}", response_model=schemas.Educator)
def read_educator(educator_id: int, db: Session = Depends(get_db)):
    db_educator = crud.get_educator(db, educator_id=educator_id)
    if db_educator is None:
        raise HTTPException(status_code=404, detail="Educator not found")
    return db_educator

@app.put("/educators/{educator_id}", response_model=schemas.Educator)
def update_educator(educator_id: int, educator: schemas.EducatorUpdate, db: Session = Depends(get_db)):
    db_educator = crud.update_educator(db, educator_id=educator_id, educator=educator)
    if db_educator is None:
        raise HTTPException(status_code=404, detail="Educator not found")
    return db_educator

@app.delete("/educators/{educator_id}")
def delete_educator(educator_id: int, db: Session = Depends(get_db)):
    success = crud.delete_educator(db, educator_id=educator_id)
    if not success:
        raise HTTPException(status_code=404, detail="Educator not found")
    return {"message": "Educator deleted successfully"}

# Lecture endpoints
@app.post("/lectures/", response_model=schemas.Lecture)
def create_lecture(lecture: schemas.LectureCreate, db: Session = Depends(get_db)):
    return crud.create_lecture(db=db, lecture=lecture)

@app.get("/lectures/", response_model=List[schemas.Lecture])
def read_lectures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lectures = crud.get_lectures(db, skip=skip, limit=limit)
    return lectures

@app.get("/lectures/{lecture_id}", response_model=schemas.Lecture)
def read_lecture(lecture_id: int, db: Session = Depends(get_db)):
    db_lecture = crud.get_lecture(db, lecture_id=lecture_id)
    if db_lecture is None:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return db_lecture

@app.put("/lectures/{lecture_id}", response_model=schemas.Lecture)
def update_lecture(lecture_id: int, lecture: schemas.LectureUpdate, db: Session = Depends(get_db)):
    db_lecture = crud.update_lecture(db, lecture_id=lecture_id, lecture=lecture)
    if db_lecture is None:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return db_lecture

@app.delete("/lectures/{lecture_id}")
def delete_lecture(lecture_id: int, db: Session = Depends(get_db)):
    success = crud.delete_lecture(db, lecture_id=lecture_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return {"message": "Lecture deleted successfully"}

# Question endpoints
@app.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db=db, question=question)

@app.get("/questions/", response_model=List[schemas.Question])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, skip=skip, limit=limit)
    return questions

@app.get("/questions/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.get_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.put("/questions/{question_id}", response_model=schemas.Question)
def update_question(question_id: int, question: schemas.QuestionUpdate, db: Session = Depends(get_db)):
    db_question = crud.update_question(db, question_id=question_id, question=question)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.delete("/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    success = crud.delete_question(db, question_id=question_id)
    if not success:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}

# Answer Option endpoints
@app.post("/answer-options/", response_model=schemas.AnswerOption)
def create_answer_option(answer_option: schemas.AnswerOptionCreate, db: Session = Depends(get_db)):
    return crud.create_answer_option(db=db, answer_option=answer_option)

@app.get("/answer-options/", response_model=List[schemas.AnswerOption])
def read_answer_options(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    answer_options = crud.get_answer_options(db, skip=skip, limit=limit)
    return answer_options

@app.get("/answer-options/{answer_option_id}", response_model=schemas.AnswerOption)
def read_answer_option(answer_option_id: int, db: Session = Depends(get_db)):
    db_answer_option = crud.get_answer_option(db, answer_option_id=answer_option_id)
    if db_answer_option is None:
        raise HTTPException(status_code=404, detail="Answer option not found")
    return db_answer_option

@app.put("/answer-options/{answer_option_id}", response_model=schemas.AnswerOption)
def update_answer_option(answer_option_id: int, answer_option: schemas.AnswerOptionUpdate, db: Session = Depends(get_db)):
    db_answer_option = crud.update_answer_option(db, answer_option_id=answer_option_id, answer_option=answer_option)
    if db_answer_option is None:
        raise HTTPException(status_code=404, detail="Answer option not found")
    return db_answer_option

@app.delete("/answer-options/{answer_option_id}")
def delete_answer_option(answer_option_id: int, db: Session = Depends(get_db)):
    success = crud.delete_answer_option(db, answer_option_id=answer_option_id)
    if not success:
        raise HTTPException(status_code=404, detail="Answer option not found")
    return {"message": "Answer option deleted successfully"}

# Student Answer endpoints
@app.post("/student-answers/", response_model=schemas.StudentAnswer)
def create_student_answer(student_answer: schemas.StudentAnswerCreate, db: Session = Depends(get_db)):
    return crud.create_student_answer(db=db, student_answer=student_answer)

@app.get("/student-answers/", response_model=List[schemas.StudentAnswer])
def read_student_answers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    student_answers = crud.get_student_answers(db, skip=skip, limit=limit)
    return student_answers

@app.get("/student-answers/{student_answer_id}", response_model=schemas.StudentAnswer)
def read_student_answer(student_answer_id: int, db: Session = Depends(get_db)):
    db_student_answer = crud.get_student_answer(db, student_answer_id=student_answer_id)
    if db_student_answer is None:
        raise HTTPException(status_code=404, detail="Student answer not found")
    return db_student_answer

@app.get("/student-answers/device/{device_id}", response_model=List[schemas.StudentAnswer])
def read_student_answers_by_device(device_id: str, db: Session = Depends(get_db)):
    student_answers = crud.get_student_answers_by_device(db, device_id=device_id)
    return student_answers

@app.put("/student-answers/{student_answer_id}", response_model=schemas.StudentAnswer)
def update_student_answer(student_answer_id: int, student_answer: schemas.StudentAnswerUpdate, db: Session = Depends(get_db)):
    db_student_answer = crud.update_student_answer(db, student_answer_id=student_answer_id, student_answer=student_answer)
    if db_student_answer is None:
        raise HTTPException(status_code=404, detail="Student answer not found")
    return db_student_answer

@app.delete("/student-answers/{student_answer_id}")
def delete_student_answer(student_answer_id: int, db: Session = Depends(get_db)):
    success = crud.delete_student_answer(db, student_answer_id=student_answer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student answer not found")
    return {"message": "Student answer deleted successfully"} 