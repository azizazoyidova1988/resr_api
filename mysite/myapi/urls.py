from rest_framework import routers
from .views import AuthorView, GenreView, BookView, author_list, author_details, \
    genre_details, genre_list, book_details, book_list
from django.urls import path, include

# router = routers.DefaultRouter()
# router.register(r"author", AuthorViewSets)
# router.register(r"genre",GenreViewSets)
# router.register(r"book", BookViewSets)

urlpatterns = [

    path('author/', author_list),
    path('author/<int:pk>/', author_details),

    path('genre/', genre_list),
    path('genre/<int:pk>/', genre_details),

    path('book/', book_list),
    path('book/<int:pk>/', book_details),

    # path('author/', AuthorView.as_view()),
    # path('author/<int:pk>/', AuthorView.as_view()),
    #
    # path('genre/', GenreView.as_view()),
    # path('genre/<int:pk>/', GenreView.as_view()),
    #
    # path('book/', BookView.as_view()),
    # path('book/<int:pk>/', BookView.as_view()),

    # path('', include(router.urls))
]
