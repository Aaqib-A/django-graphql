import graphene
from graphene_django import DjangoObjectType, DjangoListField
from quiz.models import Category, Quizzes, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fileds = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query(graphene.ObjectType):
    # all_quizzes = DjangoListField(QuizzesType)
    # def resolve_all_quizzes(root, info):
    #     return Quizzes.objects.all()
    
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get(pk=id)

    all_answers = graphene.List(AnswerType, id=graphene.Int())
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


    all_questions = graphene.List(QuestionType) # Same as DjangoListField
    def resolve_all_questions(root, info):
        return Question.objects.all()
    


schema = graphene.Schema(query=Query)
