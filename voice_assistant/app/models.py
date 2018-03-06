from django.db import models  
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

import app.command_process.cmd_process as cmd

class VoiceAssistant(models.Model) :
    created = models.DateTimeField(auto_now_add=True)
    requested_content = models.TextField()
    requested_user = models.ForeignKey('auth.User', related_name='app', on_delete=models.CASCADE)
    response_content = models.TextField(blank=True)
    response_action = models.TextField(blank=True, default='')

    def save(self, *args, **kwargs) :
        command = cmd.link_commands(self.requested_content, self.requested_user)
        self.response_content = command['response']
        self.response_action = command['action']
        super(VoiceAssistant, self).save(*args, **kwargs)

    class Meta :
        ordering = ('created', )