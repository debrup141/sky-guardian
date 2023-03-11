from django.shortcuts import render
import json
import urllib.request
import urllib.error

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if not city:
            return render(request, 'index.html', {'error': 'Please enter a city name.'})
        city = urllib.parse.quote(city)
        decoded_city = urllib.parse.unquote(city)
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b1c2bd95540dce6f19593055c44d3113').read()
        except urllib.error.HTTPError as e:
            if e.code == 400:
                return render(request, 'index.html', {'error': 'Invalid city name. Please enter a valid city name.'})
            else:
                return render(request, 'index.html', {'error': 'An error occurred. Please try again later.'})
        json_data = json.loads(res)
        data = {
            'decoded_city': decoded_city,
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': '{:.2f}°C'.format(json_data['main']['temp']-273.15),
            'icon_code': json_data['weather'][0]['icon'] ,
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'city': city, 'data': data})
