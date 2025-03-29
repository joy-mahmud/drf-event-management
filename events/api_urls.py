from django.urls import path
from . import api_views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('api/token/',obtain_auth_token,name='api_token'),
    path('api/events',api_views.EventListView.as_view(),name="event-list"),
    path('api/events/<int:event_id>',api_views.EventDetailsView.as_view(),name="api-event-details"),
    path('api/booking/<int:event_id>',api_views.EventBookingApiView.as_view(),name="api-event-booking"),
    path('api/my-bookings',api_views.MyBookingsView.as_view(),name='my-bookings'),
    path('api/cancel-booking/<int:booking_id>/',api_views.CancelBookingView.as_view(),name="api-cancel-booking")
]