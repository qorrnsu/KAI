import urllib.request, json, pprint

clear = '맑을'
clouds = '구름많을'
haze = '실안개가 낄'
mist = '안개가 낄'
rain = '비가 올'
snow = '눈이 올'
default = '알수없음'

URL = "http://api.openweathermap.org/data/2.5/weather?id=1835847&units=metric&appid=e5ac8528f4fad2daedab51a8a80e333e"
req = urllib.request.Request(URL)

def ask_weather():
    try:
        res = urllib.request.urlopen(req).read()
        data = json.loads(res.decode('utf-8'))

        temp = str(int(data['main']['temp']))
        w = '현재 날씨는 %s °C 입니다. ' % temp  
        
        temp_max = str(int(data['main']['temp_max']))
        temp_min = str(int(data['main']['temp_min']))
        w += "오늘의 최고기온은 %s °C, 최저기온은 %s °C 입니다. " % (temp_max, temp_min)

        weather = str(data['weather'][0]['main'])
        if weather == 'Clear':
            status = clear
        elif weather == 'Clouds':
            status = clouds
        elif weather == 'Haze':
            status = haze
        elif weather == 'Rain':
            status = rain
        elif weather == 'Snow':
            status = snow
        elif weather == 'Mist':
            status = mist 
        else:
            status = default
        w += "%s 것으로 예상 됩니다." % status
    except Exception as e:
        print(e)
        w = "죄송합니다 시스템에 문제가 있습니다." 

    return w

