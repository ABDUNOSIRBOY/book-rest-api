
from django.urls import path
from api.admin.views.users_list import UserListApiView
from api.admin.views.book_list import BookListApiView
from api.admin.views.author_list import AuthorListApiView
from api.admin.views.my_list import MyListApiView

urlpatterns = [
    path("user/list/", UserListApiView.as_view()),
    path("book/list/", BookListApiView.as_view()),
    path("author/list/", AuthorListApiView.as_view()),
    path("my/list/", MyListApiView.as_view()),
]

