from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Book
from api.admin.seralizers.book_seralizer import BookSeralizer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        book_data = BookSeralizer(books, many=True)
        data = {
            "message": "ok",
            "status": "backenddan salomlar",
            "books": book_data.data
        }
        return Response(data, status=status.HTTP_200_OK)


    def post(self, request):
        data = {
            "message": "ok",
            "status": "yaratish uchun",
            "books": []
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        data = {
            "message": "ok",
            "status": "bu ozgartirish uchun",
            "books": []
        }
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request):
        data = {
            "message": "ok",
            "status": "yaratish uchun",
            "books": []
        }
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        data = {
            "message": "ok",
            "status": "ochirish uchun",
            "books": []
        }
        return Response(data, status=status.HTTP_200_OK)


