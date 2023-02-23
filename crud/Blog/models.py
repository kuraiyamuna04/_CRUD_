from django.db import models

class Blog(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=200)
    Address = models.CharField(max_length=300)
    Phone = models.CharField(max_length=10)


    class Meta:
        db_table = 'Blog'