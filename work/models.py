import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Work(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    photo1 = models.ImageField(upload_to='news/photos/')
    photo2 = models.ImageField(upload_to='news/photos/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='news/photos/', null=True, blank=True)
    photo4 = models.ImageField(upload_to='news/photos/', null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

