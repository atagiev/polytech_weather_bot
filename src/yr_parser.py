import requests, bs4
import src.phrases as phrases
import src.emoji_codes as e


class Yr_parser:
    def __init__(self):
        self.website = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}"

    def parse(self, lat, lon):
        try:
            link = self.website.format(lat, lon)

            r = requests.get(link)
            data = r.json()
            description = get_weather_description(data['properties']['timeseries'][0]['data']['next_1_hours']['summary']['symbol_code']).lower()
            weather = phrases.yr.format(data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'],
                                        description,
                                        data['properties']['timeseries'][0]['data']['next_1_hours']['details']['precipitation_amount'],
                                        data['properties']['timeseries'][0]['data']['instant']['details']['wind_speed'])

            return weather
        except:
            return phrases.yr_error

def get_weather_description(data):
    if 'clearsky' in data:
        return 'Ясно ' + e.clearSky
    elif 'fair_day' in data:
        return 'Малооблачно ' + e.sunWithSmallCloud
    elif 'cloudy' in data:
        if 'partly' in data:
            return 'Облачно с прояснениями' + e.fewClouds
        return 'Облачно ' + e.clouds
    elif 'rain' in data:
        if 'shower' in data:
            return 'Ливень' + e.rainWithCloud + e.rain + e.drizzle
        elif 'light' in data:
            return 'Небольшой дождь ' + e.rainWithCloud
        elif 'heavy' in data:
            return 'Сильный дождь ' + e.rainWithCloud + e.rain
        return 'Дождь ' + e.rainWithCloud + e.umbrella
    elif 'snow' in data:
        if 'light' in data:
            return 'Небольшой снег ' + e.snowflake
        elif 'heavy' in data:
            return 'Сильный снег ' + e.snowWithCloud + e.snowWithCloud
        return 'Снег ' + e.snowflake + e.snowWithCloud
    elif 'fair_night' in data:
        return 'Безоблачно ' + e.star + e.quarterMoon
    else:
        return data + e.defaultEmoji

#TODO добавить описание к погоде sleet🌀

if __name__ == "__main__":
    yp = Yr_parser()
    print(yp.parse("60", "30"))