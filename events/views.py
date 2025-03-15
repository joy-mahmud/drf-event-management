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
    event_id=event_id
    return render(request,'events/events_details.html',{'id':event_id})