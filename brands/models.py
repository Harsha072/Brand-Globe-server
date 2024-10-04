from django.db import models

from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # logo = models.ImageField(upload_to='logos/')
    logo = models.TextField()

    def __str__(self):
        return self.name

