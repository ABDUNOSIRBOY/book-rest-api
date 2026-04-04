from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Author


class AuthorListApiView(APIView):

    def get(self, request):
        author = Author.objects.all()
        author_data = []

        for author in author:
            author_data.append({
                "id":author.id,
                "name":author.name,
                "is_dead": author.is_dead,
            })
            data = {
            "message": "ok",
            "status": "backenddan salomlar",
            "author": author_data
        }
        return Response(data, status=status.HTTP_200_OK)
