from django.db import models

class News(models.Model):
    source = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title
