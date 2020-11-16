from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///schooldb.sqlite3", convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class ClassesTable(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    optional = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))


class TeachersTable(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    classes = relationship(ClassesTable, backref="teachers")


class GradesTable(Base):
    __tablename__ = "grades"

    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    # Workaround to SQLAlchemy's requirement for table primary key,
    # despite the grade column not being such
    grade = Column(Float, primary_key=True)


class StudentsTable(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    country = Column(String)

    grades = relationship(GradesTable, backref="students")