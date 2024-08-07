from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  line_id = models.CharField(max_length=255, unique=True)
  is_new_user = models.BooleanField(default=True)

  def __str__(self):
    return self.user.username
