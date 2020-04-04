from django.db import models
# from django.urls import reverse
from django.contrib.auth.models import User


class Project(models.Model):
    """Model representing a project."""

    # Fields
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """String for representing the Project object (in Admin site etc.)."""
        return self.title
