from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    student_class = Column(String)
    admission_number = Column(String, unique=True)
    parent_phone = Column(String)
    status = Column(String, default="OUT")