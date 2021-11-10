from rest_framework import viewsets
from .models import Author, Genre, Book
from .serializers import AuthorSerializers, GenreSerializers, BookSerializers
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from .services import *

""" Funksiyaga asoslangan API yozish usuli """


@api_view(["GET", "POST"])
def author_list(request):
    if request.method == "GET":
        authors = get_authors()
        return Response(authors, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = AuthorSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def author_details(request, pk):
    if request.method == "GET":
        try:
            author = Author.objects.get(pk=pk)
        except:
            raise NotFound(f"Author with {pk} not found")
        serializer = AuthorSerializers(author, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        print("PUT", request.data)
        return Response()

    if request.method == "DELETE":
        print("DELETE", request.data)
        return Response()


@api_view(["GET", "POST"])
def genre_list(request):
    if request.method == "GET":
        genres = get_genres()
        return Response(genres, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = GenreSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def genre_details(request, pk):
    if request.method == "GET":
        try:
            genre = Genre.objects.get(pk=pk)
        except:
            raise NotFound(f"Genre with {pk} not found")
        serializer = GenreSerializers(genre, many=False)
        return Response(serializer.data, status=status)

    if request.method == "PUT":
        print("PUT", request.data)
        return Response()
    if request.method == "DELETE":
        print("DELETE", request.data)
        return Response()


@api_view(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = get_books()
        return Response(books, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = BookSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def book_details(request, pk):
    if request.method == "GET":
        try:
            book = Book.objects.get(pk=pk)
        except:
            raise NotFound(f"Book with {pk} not found")
        serializer = BookSerializers(book, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        print("PUT", request.data)
        return Response()
    if request.method == "DELETE":
        print("DELETE", request.data)
        return Response()


""" Klasslar bilan API yozish usuli """


class AuthorView(GenericAPIView):
    serializer_class = AuthorSerializers

    def get_object(self, *args, **kwargs):
        try:
            author = Author.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return author

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        author = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=author)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        author = self.get_object(pk=pk)
        author.delete()
        return Response({"detail:" f'Author with pk={pk} has been deleted successfully!'})

    def get(self, request, pk=None):
        if pk:
            author = get_author(author_id=pk)
            if not author:
                raise NotFound("Author not found!")
            return Response(author, status=status.HTTP_200_OK)
        else:
            authors = get_authors()
            return Response(authors, status=status.HTTP_200_OK)


class GenreView(GenericAPIView):
    serializer_class = GenreSerializers

    def get_object(self, *args, **kwargs):
        try:
            genre = Genre.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return genre

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        genre = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=genre)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        genre = self.get_object(pk=pk)
        genre.delete()
        return Response({"details:" f"Genre with pk= {pk} has been deleted successfully!"})

    def get(self, request, pk=None):
        if pk:
            genre = get_genre(genre_id=pk)
            if not genre:
                raise NotFound("Genre not found!")
            return Response(genre, status=status.HTTP_200_OK)
        else:
            genres = get_genres()
            return Response(genres, status=status.HTTP_200_OK)


class BookView(GenericAPIView):
    serializer_class = BookSerializers

    def get_object(self, *args, **kwargs):
        try:
            book = Book.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return book

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=book)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = self.get_object(pk=pk)
        book.delete()
        return Response({"details:" f'Book with pk= {pk} has been deleted successfully!'})

    def get(self, request, pk=None):
        if pk:
            book = get_book(book_id=pk)
            if not book:
                raise NotFound("Book not found")
            return Response(book, status=status.HTTP_200_OK)
        else:
            books = get_books()
            return Response(books, status=status.HTTP_200_OK)


class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
