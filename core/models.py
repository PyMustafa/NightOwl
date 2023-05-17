from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import timesince

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()


    def time_since_posted(self):
        time_diff = timesince(self.time_posted).split(",")[0]
        exact_date = self.time_posted.strftime("%Y-%m-%d %H:%M:%S")
        return time_diff, exact_date
    
    def __str__(self):
        return f'{self.content[:30]}...'
    

    class Meta:
        ordering = ['-time_posted']