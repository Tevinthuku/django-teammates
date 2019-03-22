"""
This is the team views file
"""
from rest_framework import generics
from rest_framework.response import Response
from .serializer import TeamSerializers
from .models import Team


class TeamMatesView(generics.ListCreateAPIView):
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

    def create(self, request, *args, **kwargs):
        """
            custom create function with custom response
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={"data": serializer.data, "status": 201}, status=201, headers=headers)
