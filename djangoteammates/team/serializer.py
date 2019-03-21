"""
responsible for translating django team models into
json/xml format with the required fields so that can be understood by consumers
"""

from rest_framework import serializers
from .models import Team


class TeamSerializers(serializers.ModelSerializer):
    """
    This is the Team serializer class will have
    3 fields, id, name and email
    """
    class Meta:
        model = Team
        fields = [
            "id",
            "name",
            "email",
            "slackhandle"
        ]
