from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    limit_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

#class File(models.Model):
#    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    name = models.CharField(max_length=150, blank=True)
#    file = models.FileField(upload_to='yourappname/files/')'

'https://medium.com/@zachstumpf/django-5-models-filefield-88f96ca52c08'