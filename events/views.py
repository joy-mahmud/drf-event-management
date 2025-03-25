from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    api_url="http://127.0.0.1:8000/api/events"
    response = requests.get(api_url)
    if response.status_code == 200:
        events = response.json()
        print(events)
    return render(request,'events/home.html', {'events':events})

def event_details(request,event_id):
    api_url=f"http://127.0.0.1:8000/api/events/{event_id}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        event = response.json()
        return render(request,'events/events_details.html',{'event':event})
    
def my_bookings(request):
    api_url=f"http://127.0.0.1:8000/api/my-bookings"
    session_cookie = request.COOKIES.get('sessionid')
    headers = {'Cookie': f'sessionid={session_cookie}'} if session_cookie else {}

    response = requests.get(api_url, headers=headers)
    print(response)
    bookings = response.json()
    return render(request,'events/my_bookings.html',{'bookings':bookings})