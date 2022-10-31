from django.db import models

# Create your models here.


class Github(models.Model):
    username = models.CharField(max_length=255)
    github_username = models.CharField(max_length=255)
    github_image = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.github_image
