from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateField()
    blog_data = models.TextField()
