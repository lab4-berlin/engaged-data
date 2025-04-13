from sqladmin import ModelView
from models import Institution, Educator, Lecture, Question, AnswerOption, StudentAnswer

class InstitutionAdmin(ModelView, model=Institution):
    column_list = [Institution.id, Institution.institution_name, Institution.institution_location]
    form_columns = [Institution.institution_name, Institution.institution_location]

class EducatorAdmin(ModelView, model=Educator):
    column_list = [Educator.id, Educator.educator_name, Educator.educator_speciality]
    form_columns = [Educator.educator_name, Educator.educator_speciality]

class LectureAdmin(ModelView, model=Lecture):
    column_list = [Lecture.id, Lecture.lecture_date, Lecture.lecture_title, Lecture.educator_id, Lecture.institution_id]
    form_columns = [Lecture.lecture_date, Lecture.lecture_title, Lecture.educator_id, Lecture.institution_id]

class QuestionAdmin(ModelView, model=Question):
    column_list = [Question.id, Question.question_text, Question.correct_answer_index, Question.lecture_id]
    form_columns = [Question.question_text, Question.correct_answer_index, Question.lecture_id]

class AnswerOptionAdmin(ModelView, model=AnswerOption):
    column_list = [AnswerOption.id, AnswerOption.answer_text, AnswerOption.option_index, AnswerOption.question_id]
    form_columns = [AnswerOption.answer_text, AnswerOption.option_index, AnswerOption.question_id]

class StudentAnswerAdmin(ModelView, model=StudentAnswer):
    column_list = [StudentAnswer.id, StudentAnswer.device_id, StudentAnswer.answer_option_id]
    form_columns = [StudentAnswer.device_id, StudentAnswer.answer_option_id] 