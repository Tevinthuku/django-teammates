"""
This is the team views file
"""
from rest_framework import generics
from rest_framework.response import Response
from .serializer import TeamSerializers
from .models import Team


class TeamMatesView(generics.ListAPIView):
    """
        This is the TeammatesView Class
    """
    permission_classes = []
    serializer_class = TeamSerializers

    def get(self, request, *args, **kwargs):
        query_set = Team.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            query_set = query_set.filter(name__icontains=query)

        return Response(data={"data": query_set.serialize(), "status": 200}, status=200)
