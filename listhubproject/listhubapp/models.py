# appname/models.py
from django.db import models


class ListHubProperty(models.Model):
    address = models.CharField(max_length=255)
    description = models.TextField()
    modified_date = models.DateTimeField()
    # Add other fields as needed
