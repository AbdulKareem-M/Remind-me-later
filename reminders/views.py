from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer


class ReminderCreateView(APIView):
  def post(self, request):
    serializer = ReminderSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
  