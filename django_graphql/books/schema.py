import graphene
from graphene_django import DjangoObjectType
from books.models import Books


class BookType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Books.objects.all()
        # return Books.objects.filter(title="Django")


schema = graphene.Schema(query=Query)
