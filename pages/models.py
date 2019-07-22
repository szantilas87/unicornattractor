from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Model for a new query
class Query(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted  = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #Return url to a specific query
    def get_absolute_url(self):
        return reverse("query-detail", kwargs={"pk": self.pk})
    