import src.phrases as phrases
import src.config as config
import requests
import src.emoji_codes as e


class Owm_parser:
    def __init__(self):
        self.website = "http://api.openweathermap.org/data/2.5/weather"
    def parse(self, lat, lon):
        try:
            r = requests.get(self.website, params={'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'ru', 'APPID': config.owm_api_key})
            data = r.json()
            weatherId = data['weather'][0]['id']
            emoji = getEmoji(weatherId)
            weather = phrases.owm.format(data['main']['temp'], data['main']['feels_like'], data['weather'][0]['description'], emoji, data['wind']['speed'])
            return weather
        except:
            return phrases.owm_error


def getEmoji(weatherID):
    if weatherID:
        if str(weatherID)[0] == '2' or weatherID == 900 or weatherID==901 or weatherID==902 or weatherID==905:
            return e.thunderstorm
        elif str(weatherID)[0] == '3':
            return e.drizzle
        elif str(weatherID)[0] == '5':
            if weatherID == 500:
                return e.rainWithCloud
            return e.rainWithCloud + e.umbrella
        elif str(weatherID)[0] == '6' or weatherID == 903 or weatherID == 906:
            return e.snowWithCloud + e.snowflake
        elif str(weatherID)[0] == '7':
            return e.atmosphere
        elif weatherID == 800:
            return e.clearSky
        elif weatherID == 801 or weatherID == 802 or weatherID == 803:
            return e.fewClouds
        elif weatherID == 804:
            return e.clouds
        elif weatherID == 904:
            return e.hot
        else:
            return e.defaultEmoji    # Default emoji

    else:
        return e.defaultEmoji   # Default emoji

if __name__ == "__main__":
    op = Owm_parser()
    print(op.parse("51", "0"))
