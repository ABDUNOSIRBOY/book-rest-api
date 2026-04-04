
from django.urls import path
from api.admin.views.users_list import UserListApiView
from api.admin.views.book_list import BookListApiView
from api.admin.views.author_list import AuthorListApiView
from api.admin.views.my_list import MyListApiView
from api.admin.views.book_create import BookCreateApiView
from api.admin.views.book_update import BookUpdateApiView
from api.admin.views.book_delete import BookDeleteApiView
from api.admin.views.author_login import AuthorLoginApiView
from api.admin.views.author_register import AuthorRegisterApiView
from api.admin.views.author_logout import AuthorLogoutApiView
from api.admin.views.book_detail import BookDetailApiView

urlpatterns = [
    path("user/list/", UserListApiView.as_view()),
    path("book/list/", BookListApiView.as_view()),
    path("author/list/", AuthorListApiView.as_view()),
    path("my/list/", MyListApiView.as_view()),
    path("book/create/", BookCreateApiView.as_view()),
    path("book/update/1/", BookUpdateApiView.as_view()),
    path("book/delete/1/", BookDeleteApiView.as_view()),
    path("author/login/", AuthorLoginApiView.as_view()),
    path("author/register/", AuthorRegisterApiView.as_view()),
    path("author/logout/", AuthorLogoutApiView.as_view()),
    path("book/detail/", BookDetailApiView.as_view()),
]

