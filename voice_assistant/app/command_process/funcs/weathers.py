#open weather map api를 사용했고, weather id별로 상태를 대충 한국어로 바꿔둠.
#https://openweathermap.org/weather-conditions 확인
#sk플래닛의 공기 질 api를 사용함
#https://developers.skplanetx.com/apidoc/kor/weather/living/?leftAppId=15049120#doc1379 확인

import requests, json, math

class Weather :
    location = {'lat':'latitude', 'lon':'longtitude'}
    API_KEY_WEATHER = '<API_KEY_WEATHER>'
    API_KEY_DUSTS = '<API_KEY_DUSTS>'
    USERID_DUSTS = '<your-user-name>'
    WEATHER_API_LINK = 'http://api.openweathermap.org/data/2.5/weather?lat='+location["lat"]+'&lon='+location["lon"]+'&APPID='+API_KEY_WEATHER
    DUSTS_API_LINK = 'http://apis.skplanetx.com/weather/dust?version=1&lat='+location['lat']+'&lon='+location['lon']

    def getWeatherInformation(self) :
        jsonFile = json.loads(requests.get(self.WEATHER_API_LINK).text)
        temperature = (math.ceil((jsonFile['main']['temp']) - 273.15))
        weatherID = (jsonFile['weather'][0]['id'])
        return {'temperature' : temperature, 'weatherID':weatherID}
    def getDustsInformation(self) :
        headers = {'appKey': self.API_KEY_DUSTS, 'x-skpop-userId': self.USERID_DUSTS, 'Accept': 'application/json', 'Accept-Language': 'ko_KR'}
        jsonFile = json.loads(requests.get(self.DUSTS_API_LINK, headers=headers).text)
        return jsonFile['weather']['dust'][0]['pm10']['grade']