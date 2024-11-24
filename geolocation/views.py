from django.shortcuts import render

from django.conf import settings
from .forms import AddressForm
import requests

def get_latitude_longitude(address):
    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address.replace(' ', '+')}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == "OK":
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    
    return None, None

def address_view(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        
        if form.is_valid():
            address = form.cleaned_data['address']
            latitude, longitude = get_latitude_longitude(address)
            return render(request, "geolocation/result.html", {"latitude": latitude, "longitude": longitude})
    
    else:
        form = AddressForm()
    
    return render(request, "geolocation/address.html", {"form": form})