import requests, bs4
import src.phrases as phrases

thunderstorm = u'\U000026C8'
drizzle = u'\U0001F4A7'
rain = u'\U00002614'
rainWithCloud = u'\U0001F327'
umbrella = u'\U00002602'
snowflake = u'\U00002744'
snowman = u'\U000026C4'
snowWithCloud = u'\U0001F328'
atmosphere = u'\U0001F301'
clearSky = u'\U00002600'
sunWithSmallCloud = u'\U0001F324'
fewClouds = u'\U000026C5'
clouds = u'\U00002601'
hot = u'\U0001F525'
defaultEmoji = u'\U0001F300'
star = u'\U0001F320'
quarterMoon = u'\U0001F31C'
defaultEmoji = u'\U0001F300'


class Yr_parser:
    def __init__(self):
        self.website = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}"

    def parse(self, lat, lon):
        try:
            link = self.website.format(lat, lon)

            r = requests.get(link)
            data = r.json()
            description = get_weather_description(data['properties']['timeseries'][0]['data']['next_1_hours']['summary']['symbol_code'])
            weather = phrases.yr.format(data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'],
                                        description,
                                        data['properties']['timeseries'][0]['data']['next_1_hours']['details']['precipitation_amount'],
                                        data['properties']['timeseries'][0]['data']['instant']['details']['wind_speed'])

            return weather.capitalize()
        except:
            return phrases.yr_error

def get_weather_description(data):
    if 'clearsky' in data:
        return 'Ясно ' + clearSky
    elif 'fair_day' in data:
        return 'Малооблачно ' + sunWithSmallCloud
    elif 'cloudy' in data:
        if 'partly' in data:
            return 'Облачно с прояснениями' + fewClouds
        return 'Облачно ' + clouds
    elif 'rain' in data:
        if 'shower' in data:
            return 'Ливень' + rainWithCloud + rain + drizzle
        elif 'light' in data:
            return 'Небольшой дождь ' + rainWithCloud
        elif 'heavy' in data:
            return 'Сильный дождь ' + rainWithCloud + rain
        return 'Дождь ' + rainWithCloud + umbrella
    elif 'snow' in data:
        if 'light' in data:
            return 'Небольшой снег ' + snowflake
        elif 'heavy' in data:
            return 'Сильный снег ' + snowWithCloud + snowWithCloud
        return 'Снег ' + snowflake + snowWithCloud
    elif 'fair_night' in data:
        return 'Безоблачно ' + star + quarterMoon
    else:
        return data

if __name__ == "__main__":
    yp = Yr_parser()
    print(yp.parse("60", "30"))