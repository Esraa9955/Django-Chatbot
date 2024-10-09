from django.db import models
from django.contrib.auth.models import User

class Chatbot(models.Model):
    message = models.TextField(default="Default message")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Assuming user with ID 1 exists
    response = models.TextField( default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
