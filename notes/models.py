from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from datetime import datetime

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    description  = models.TextField()
    is_deleted   = models.BooleanField(default=False)
    is_archived  = models.BooleanField(default=False)
    label        = models.CharField(max_length=20)
    mydate       = models.DateField(null=True, blank=True)
    collaborate  = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='collaborated_user')
    is_pinned    = models.NullBooleanField(blank=True, null=True, default=None)
    color        = models.CharField(default=None, max_length=20, blank=True,null=True)
    user         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
