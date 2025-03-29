from django.shortcuts import render,redirect
import requests

# Create your views here.
def home(request):
    api_url="http://127.0.0.1:8000/api/events"
    token = request.user.auth_token.key  # Get the token dynamically
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.get(api_url,headers=headers)
    if response.status_code == 200:
        events = response.json()
        print(events)
    return render(request,'events/home.html', {'events':events})

def event_details(request,event_id):
    api_url=f"http://127.0.0.1:8000/api/events/{event_id}"
    token = request.user.auth_token.key  # Get the token dynamically
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.get(api_url,headers=headers)
    
    if response.status_code == 200:
        event = response.json()
        return render(request,'events/events_details.html',{'event':event})

def book_event(request,event_id):
    api_url= f"http://127.0.0.1:8000/api/booking/{event_id}" 
    token = request.user.auth_token.key  # Get the token dynamically
    headers = {
        'Authorization': f'Token {token}',
    }
    response = requests.post(api_url,headers=headers)
    
    if response.status_code==201:
        return redirect('bookings')
    
    return redirect('bookings')
    
     
def my_bookings(request):
    api_url = "http://127.0.0.1:8000/api/my-bookings"
    token = request.user.auth_token.key  # Get the token dynamically
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.get(api_url, headers=headers)
    print(response)
    bookings = response.json()
    return render(request,'events/my_bookings.html',{'bookings':bookings})

def cancel_booking(request,booking_id):
    api_url = f"http://127.0.0.1:8000/api/cancel-booking/{booking_id}/"  

    token = request.user.auth_token.key
    headers = {"Authorization": f'Token {token}'}
    response = requests.delete(api_url, headers=headers)
    if response.status_code == 204:
        return redirect('bookings')

    return redirect('bookings')