from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serilizers import *


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, request, *args, **kwargs):
        data = self.request.data
        data['user'] = request.user.id
        serializer = VideoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticated,)