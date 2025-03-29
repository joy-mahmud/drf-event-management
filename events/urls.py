from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('events/<int:event_id>/',views.event_details,name='event_details'),
    path('book_event/<int:event_id>',views.book_event,name="book_event"),
    path('bookings',views.my_bookings,name='bookings'),
    path('cancel/<int:booking_id>',views.cancel_booking,name='cancel')
]
