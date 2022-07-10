from django.urls import path, re_path
from books import genericapiview_view

urlpatterns = [
    path('books/', genericapiview_view.BooksView.as_view()),
    re_path(r'books/(?P<pk>\d+)', genericapiview_view.BookView.as_view())
]
