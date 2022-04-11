from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TasksList(models.Model):
    tags = [
    ('New', 'New'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]
    user = models.ForeignKey(User, on_delete=models.CASCADE ,blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    rand_tags = models.CharField(max_length=15, choices=tags, default='New')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
    

class History(models.Model):
    
    tags = [
    ('danger', 'New'),
    ('warning', 'Running'),
    ('success', 'Completed'),
]
    user = models.ForeignKey(User, on_delete=models.CASCADE ,blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    rand_tags = models.CharField(max_length=15, choices=tags, default='danger')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']