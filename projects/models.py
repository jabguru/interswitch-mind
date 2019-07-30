from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d/', null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title