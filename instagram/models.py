from django.db import models
from inf_drf_react_js import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_public = models.BooleanField(default=False,db_index=True)