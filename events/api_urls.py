from django.urls import path
from . import api_views
urlpatterns=[
    path('api/events',api_views.EventListView.as_view(),name="event-list"),
    path('api/events/<int:event_id>',api_views.EventDetailsView.as_view(),name="api-event-details")
]