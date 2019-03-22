"""
urls for the team routes.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.TeamMatesView.as_view(), name='allteammates'),
]
