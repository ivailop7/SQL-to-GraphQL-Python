import graphene
from database import StudentsTable, ClassesTable, GradesTable
from graph_ql.typedefs import Students, Classes, Grades


class Query(graphene.ObjectType):
    get_students = graphene.List(Students)
    students_by_name = graphene.List(Students, name=graphene.String())
    grades_by_class = graphene.List(Grades, name=graphene.String())
    grades_by_student_and_class = graphene.List(
        Grades, student_name=graphene.String(), class_name=graphene.String()
    )

    @staticmethod
    def resolve_get_students(parent, info, **args):
        return Students.get_query(info).all()

    @staticmethod
    def resolve_students_by_name(parent, info, **args):
        student_name = args.get("name")
        students_query = Students.get_query(info)
        return students_query.filter(StudentsTable.name.contains(student_name)).all()

    @staticmethod
    def resolve_grades_by_class(parent, info, **args):
        class_name = args.get("name")
        grades_query = Grades.get_query(info)
        return (
            grades_query.join(ClassesTable)
            .filter(ClassesTable.name == class_name)
            .all()
        )

    @staticmethod
    def resolve_grades_by_student_and_class(parent, info, **args):
        student_name = args.get("student_name")
        class_name = args.get("class_name")
        grades_query = Grades.get_query(info)
        return (
            grades_query.join(StudentsTable)
            .filter(StudentsTable.name.contains(student_name))
            .join(ClassesTable)
            .filter(ClassesTable.name.contains(class_name))
            .all()
        )
