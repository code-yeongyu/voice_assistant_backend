#from app.models import Request
#from app.serializers import RequestSerializer

from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from app.models import VoiceAssistant
from app.serializers import RequestSerializer, UserSerializer
import app.command_process.cmd_process as cmd

class Answer(generics.ListCreateAPIView) :
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = VoiceAssistant.objects.all()
    serializer_class = RequestSerializer
    
    def perform_create(self, serializer) :
        serializer.save(requested_user=self.request.user)
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer