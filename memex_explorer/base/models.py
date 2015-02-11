"""Base models."""

from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator


def alphanumeric_validator():
    return RegexValidator(r'^[a-zA-Z0-9 ]+$',
        'Only numbers, letters, and spaces are allowed.')


class Project(models.Model):
    """Project model.

    Every application that plugs into Memex Explorer should have a
    foreign key relationship to a Project.

    Model Fields
    ------------

    name : str(64)
    slug : str(64)
        The `slug` field is derived from `name` on save, and is restricted
        to URL-safe characters.
    description : str

    """

    name = models.CharField(max_length=64, unique=True,
        validators=[alphanumeric_validator()])
    slug = models.SlugField(max_length=64, unique=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
