from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25)
    
class Post(models.Model):
    post_header = models.CharField(max_length=50)
    post_text = models.TextField()
    post_author = models.CharField(max_length=50)
    post_datatime = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT, default="no category")