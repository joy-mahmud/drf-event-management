from django.urls import path
from . import api_views
urlpatterns=[
    path('api/events',api_views.EventListView.as_view(),name="event-list"),
    path('api/events/<int:event_id>',api_views.EventDetailsView.as_view(),name="api-event-details"),
    path('api/booking/<int:event_id>',api_views.EventBookingApiView.as_view(),name="api-event-booking"),
    path('api/my-bookings',api_views.MyBookingsView.as_view(),name='my-bookings')
]