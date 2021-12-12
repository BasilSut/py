#from req import weather_
from datetime import datetime
import requests
import json
apikey = '84a7cf571b47081289852de378c8aad0'
city = "Saint Petersburg, RU"


def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("error!")

#pro.openweathermap.org/data/2.5/forecast/hourly?q=
#api.openweathermap.org/data/2.5/weather?q=
#{city name}&appid={API key}
data = get_weather('http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}'.format(city, apikey))

str_data = json.dumps(data)
dict_data = json.loads(str_data)
city_id = dict_data.get('city').get('id')
print(city_id)
#print(datetime.fromtimestamp(dict_data.get("dt")).date())

#print("tempriture",dict_data.get("main").get("temp"))
try:
    for i in dict_data.get('list'):
        print( i.get('dt_txt'), '{0:+3.0f}'.format(i.get('main').get('temp')) )
except Exception as e:
    print("Exception (forecast):", e)
    pass

try:
    for i in range(0,dict_data.get('list'),5):
        print( i.get('dt_txt'), '{0:+3.0f}'.format(i.get('main').get('temp')) )
except Exception as e:
    print("Exception (forecast):", e)
    pass    
