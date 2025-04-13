from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Institution schemas
class InstitutionBase(BaseModel):
    institution_name: str
    institution_location: str

class InstitutionCreate(InstitutionBase):
    pass

class InstitutionUpdate(InstitutionBase):
    institution_name: Optional[str] = None
    institution_location: Optional[str] = None

class Institution(InstitutionBase):
    id: int
    created_at: datetime
    changed_at: datetime

    class Config:
        from_attributes = True

# Educator schemas
class EducatorBase(BaseModel):
    educator_name: str
    educator_speciality: str

class EducatorCreate(EducatorBase):
    pass

class EducatorUpdate(EducatorBase):
    educator_name: Optional[str] = None
    educator_speciality: Optional[str] = None

class Educator(EducatorBase):
    id: int
    created_at: datetime
    changed_at: datetime

    class Config:
        from_attributes = True

# Lecture schemas
class LectureBase(BaseModel):
    lecture_date: datetime
    lecture_title: str
    educator_id: int
    institution_id: int

class LectureCreate(LectureBase):
    pass

class LectureUpdate(BaseModel):
    lecture_date: Optional[datetime] = None
    lecture_title: Optional[str] = None
    educator_id: Optional[int] = None
    institution_id: Optional[int] = None

class Lecture(LectureBase):
    id: int
    created_at: datetime
    changed_at: datetime

    class Config:
        from_attributes = True

# Question schemas
class QuestionBase(BaseModel):
    lecture_id: int
    question_text: str
    correct_answer_index: int

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(BaseModel):
    lecture_id: Optional[int] = None
    question_text: Optional[str] = None
    correct_answer_index: Optional[int] = None

class Question(QuestionBase):
    id: int
    created_at: datetime
    changed_at: datetime
    question_created_at: datetime

    class Config:
        from_attributes = True

# Answer Option schemas
class AnswerOptionBase(BaseModel):
    question_id: int
    answer_text: str
    option_index: int

class AnswerOptionCreate(AnswerOptionBase):
    pass

class AnswerOptionUpdate(BaseModel):
    question_id: Optional[int] = None
    answer_text: Optional[str] = None
    option_index: Optional[int] = None

class AnswerOption(AnswerOptionBase):
    id: int
    created_at: datetime
    changed_at: datetime

    class Config:
        from_attributes = True

# Student Answer schemas
class StudentAnswerBase(BaseModel):
    question_id: int
    answer_option_id: int
    device_id: str

class StudentAnswerCreate(StudentAnswerBase):
    pass

class StudentAnswerUpdate(BaseModel):
    question_id: Optional[int] = None
    answer_option_id: Optional[int] = None
    device_id: Optional[str] = None

class StudentAnswer(StudentAnswerBase):
    id: int
    created_at: datetime
    changed_at: datetime
    answer_created_at: datetime

    class Config:
        from_attributes = True 