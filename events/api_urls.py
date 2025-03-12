from django.urls import path
from . import api_views
urlpatterns=[
    path('api/events',api_views.EventListView.as_view(),name="event-list")
]