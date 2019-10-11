from django.db import models

class Content(models.Model):
    name = models.CharField(max_length=30)
    data = models.CharField(max_length=200)

    def __str__(self):
        return self.name
