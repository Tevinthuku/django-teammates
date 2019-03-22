"""
This is the team views file
"""
from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializer import TeamSerializers
from .models import Team


class TeamMatesView(mixins.CreateModelMixin, generics.ListAPIView):
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

    def post(self, request, *args, **kwargs):
        """
            This function is responsible for creating a new teammate member
        """
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
            custom create function with custom response
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={"data": serializer.data, "status": 201}, status=201, headers=headers)
