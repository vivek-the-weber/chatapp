from django.db import models

# Create your models here.
class ChatModel(models.Model):
    all_chats = models.TextField()