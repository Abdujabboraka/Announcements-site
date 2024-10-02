from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(default='no description', help_text='Description')
    image = models.ImageField(upload_to='announcement/', null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
