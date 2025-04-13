from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Institution(Base):
    __tablename__ = "institution"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    institution_name = Column(String(255), nullable=False)
    institution_location = Column(String(255), nullable=False)

    # Relationships
    educators = relationship("Educator", secondary="educator_institution", back_populates="institutions")
    lectures = relationship("Lecture", back_populates="institution", foreign_keys="[Lecture.institution_id]")

class Educator(Base):
    __tablename__ = "educator"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    educator_name = Column(String(255), nullable=False)
    educator_speciality = Column(String(255), nullable=False)

    # Relationships
    institutions = relationship("Institution", secondary="educator_institution", back_populates="educators")
    lectures = relationship("Lecture", back_populates="educator")

# Junction table for educator-institution many-to-many relationship
educator_institution = Table(
    "educator_institution",
    Base.metadata,
    Column("educator_id", Integer, ForeignKey("educator.id", ondelete="CASCADE"), primary_key=True),
    Column("institution_id", Integer, ForeignKey("institution.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("changed_at", DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
)

class Lecture(Base):
    __tablename__ = "lecture"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    lecture_date = Column(DateTime, nullable=False)
    lecture_title = Column(String(255), nullable=False)
    educator_id = Column(Integer, ForeignKey("educator.id", ondelete="CASCADE"))
    institution_id = Column(Integer, ForeignKey("institution.id", ondelete="CASCADE"))

    # Relationships
    educator = relationship("Educator", back_populates="lectures")
    institution = relationship("Institution", back_populates="lectures", foreign_keys=[institution_id])
    questions = relationship("Question", back_populates="lecture")

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    lecture_id = Column(Integer, ForeignKey("lecture.id", ondelete="CASCADE"))
    question_text = Column(String, nullable=False)
    correct_answer_index = Column(Integer, nullable=False)
    question_created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    lecture = relationship("Lecture", back_populates="questions")
    answer_options = relationship("AnswerOption", back_populates="question")
    student_answers = relationship("StudentAnswer", back_populates="question")

class AnswerOption(Base):
    __tablename__ = "answer_option"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    question_id = Column(Integer, ForeignKey("question.id", ondelete="CASCADE"))
    answer_text = Column(String, nullable=False)
    option_index = Column(Integer, nullable=False)

    # Relationships
    question = relationship("Question", back_populates="answer_options")
    student_answers = relationship("StudentAnswer", back_populates="answer_option")

class StudentAnswer(Base):
    __tablename__ = "student_answer"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    question_id = Column(Integer, ForeignKey("question.id", ondelete="CASCADE"))
    answer_option_id = Column(Integer, ForeignKey("answer_option.id", ondelete="CASCADE"))
    device_id = Column(String(255), nullable=False)
    answer_created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    question = relationship("Question", back_populates="student_answers")
    answer_option = relationship("AnswerOption", back_populates="student_answers") 