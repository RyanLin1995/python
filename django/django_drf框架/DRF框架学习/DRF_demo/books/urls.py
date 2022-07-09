from django.urls import path, re_path
from books import views

urlpatterns = [
    path('books/', views.BooksView.as_view()),
    re_path(r'books/(?P<pk>\d+)', views.BookView.as_view())
]