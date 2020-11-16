import graphene
from database import db_session, StudentsTable
from graph_ql.typedefs import Students, AddStudentFields


class AddStudent(graphene.Mutation):
    student = graphene.Field(lambda: Students)
    status = graphene.Boolean()

    class Arguments:
        input = AddStudentFields(required=True)

    @staticmethod
    def mutate(self, info, input):
        student = StudentsTable(**input)
        db_session.add(student)
        db_session.commit()
        status = True
        return AddStudent(student=student, status=status)


class Mutation(graphene.ObjectType):
    addStudent = AddStudent.Field()