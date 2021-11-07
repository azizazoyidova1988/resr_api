from rest_framework import routers
from .views import AuthorView, GenreView, BookView, author_list, author_details
from django.urls import path, include

# router = routers.DefaultRouter()
# router.register(r"author", AuthorViewSets)
# router.register(r"genre",GenreViewSets)
# router.register(r"book", BookViewSets)

urlpatterns = [

    path('author/', AuthorView.as_view()),
    path('author/<int:pk>/', AuthorView.as_view()),

    path('genre/', GenreView.as_view()),
    path('genre/<int:pk>/', GenreView.as_view()),

    path('book/', BookView.as_view()),
    path('book/<int:pk>/', BookView.as_view()),

    # path('author/', author_list),
    # path('author/<int:pk>/', author_details)

    # path('', include(router.urls))
]
