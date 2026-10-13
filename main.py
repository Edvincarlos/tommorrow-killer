from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from pydantic import BaseModel

# This creates the students.db file automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Helper to get DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class StudentCreate(BaseModel):
    name: str
    student_class: str
    admission_number: str
    parent_phone: str

@app.get("/")
def home():
    return {"message": "IN/OUT system is running with DB"}

# Add a student
@app.post("/students")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(
        name=student.name,
        student_class=student.student_class,
        admission_number=student.admission_number,
        parent_phone=student.parent_phone
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# See all students
@app.get("/students")
def list_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

# IN / OUT
@app.post("/in/{admission_number}")
def check_in(admission_number: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.admission_number == admission_number).first()
    if not student:
        return {"error": "Student not found"}
    student.status = "IN"
    db.commit()
    return {"message": f"{student.name} is now IN", "parent": student.parent_phone}

@app.post("/out/{admission_number}")
def check_out(admission_number: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.admission_number == admission_number).first()
    if not student:
        return {"error": "Student not found"}
    student.status = "OUT"
    db.commit()
    return {"message": f"{student.name} is now OUT", "parent": student.parent_phone}