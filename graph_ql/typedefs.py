import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import StudentsTable, TeachersTable, ClassesTable, GradesTable


class Students(SQLAlchemyObjectType):
    class Meta:
        model = StudentsTable


class StudentFields:
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Int()
    country = graphene.String()


class AddStudentFields(graphene.InputObjectType, StudentFields):
    pass


class Teachers(SQLAlchemyObjectType):
    class Meta:
        model = TeachersTable


class Classes(SQLAlchemyObjectType):
    class Meta:
        model = ClassesTable


class Grades(SQLAlchemyObjectType):
    class Meta:
        model = GradesTable
