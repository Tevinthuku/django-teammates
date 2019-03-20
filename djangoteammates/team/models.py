"""
This is the teams model file
"""

from django.db import models
# Create your models here.


class TeamQuerySet(models.QuerySet):
    """
        Query set class for the Teammates
    """

    def serialize(self):
        """
            Turn the list of objects to a list of records
        """
        return list(self.values("name", "email", "slackhandle"))


class TeamManager(models.Manager):
    """
        Manager class. Its the middleman between model and the db
    """

    def get_queryset(self):
        """
            Instanciate new obj with the serialize function

        """
        return TeamQuerySet(self.model, using=self.db)


class Team(models.Model):
    """
        The team model class
        with the 3 field attributes
    """
    name = models.TextField()
    email = models.EmailField()
    slackhandle = models.TextField()

    objects = TeamManager()

    def __str__(self):
        return str(self.name)
