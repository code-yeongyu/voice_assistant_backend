from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import VoiceAssistant
import app.command_process.cmd_process


class RequestSerializer(serializers.ModelSerializer):
    requested_user = serializers.ReadOnlyField(
        source='requested_user.username')

    class Meta:
        model = VoiceAssistant
        fields = ('id', 'requested_content', 'requested_user',
                  'response_content', 'response_action')


class UserSerializer(serializers.ModelSerializer):
    app = serializers.PrimaryKeyRelatedField(
        many=True, queryset=VoiceAssistant.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'app')