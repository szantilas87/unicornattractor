from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#Model for a new query
class Query(models.Model):
    BUG = 'Bug'
    FEATURE = 'Feature'
    QUERY_CHOICES = [
        (BUG, 'Bug'),
        (FEATURE, 'Feature')
    ]
    TO_DO = 'To do'
    IN_PROGRESS = 'In progess'
    DONE = 'Done'
    STATUS_CHOICES = [
    (TO_DO, 'To do'),
    (IN_PROGRESS, 'In progess'),
    (DONE, 'Done')
    ]
    title = models.CharField(max_length=20)
    content = models.TextField(verbose_name='Description')
    date_posted  = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User,related_name='likes', blank=True)
    query_type = models.CharField(
        max_length = 7,
        choices = QUERY_CHOICES,
        default= BUG,
        )
    status = models.CharField(
        max_length = 10,
        choices = STATUS_CHOICES,
        default= TO_DO,
    )
        
    def __str__(self):
        return self.title



    #Return url to a specific query
    def get_absolute_url(self):
        return reverse("query-detail", kwargs={"pk": self.pk})

    # Count total likes
    def total_likes(self):
        return self.likes.count()
    
# Model for a new comment

class Comment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.query.title, str(self.user.username))