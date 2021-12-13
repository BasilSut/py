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

# 



data = get_weather('http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}'.format(city, apikey))

str_data = json.dumps(data)
dict_data = json.loads(str_data)
city_id = dict_data.get('city').get('id')
city_name = dict_data.get('city').get('name')
sunrise = datetime.fromtimestamp(int(dict_data.get('city').get('sunrise')))
sunset = datetime.fromtimestamp(int(dict_data.get('city').get('sunset')))
data = datetime.strftime(sunset,'%Y-%m-%d')
print(city_id)
print(city_name)
print(sunrise)
print(sunset)
print(f"{data} - световой день составляет: {sunset-sunrise}\n")


data_str1 = []
index =int(1) 
try:
    for i in dict_data.get('list'):
        # print( i.get('dt_txt'),"  tempriture =",'{0:+1.0f}'.format(i.get('main').get('temp')),  
        #                         "  feels_like =",'{0:+1.0f}'.format(i.get('main').get('feels_like')
        #                        ))
        data_str1 += ( (f"{index}") +" "+ i.get('dt_txt')+"  tempriture ="+(' {0:+1.0f}'.format(i.get('main').get('temp'))),
                               "  feels_like ="+' {0:+1.0f}'.format(i.get('main').get('feels_like')))
        index+=1
except Exception as e:
    print("Exception (forecast):", e)
    pass

for i in data_str1:
    print(i)

#print(data_str1)