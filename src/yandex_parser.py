import requests, bs4
import src.phrases as phrases
import src.emoji_codes as e


class Yandex_parser:
    def __init__(self):
        self.website = "https://yandex.ru/pogoda/?lat={}&lon={}"

    def parse(self, lat, lon):
        try:
            link = self.website.format(lat, lon)

            r = requests.get(link)
            b = bs4.BeautifulSoup(r.content, "html.parser")
            temp = b.find(class_="temp fact__temp fact__temp_size_s").find(class_="temp__value").getText()
            feels_like = b.find(class_="term term_orient_h fact__feels-like").find(class_="temp__value").getText()
            looks_like = b.find(class_="link__feelings fact__feelings").div.getText()
            emoji = getEmoji(looks_like)
            wind = b.find(class_="wind-speed").getText()
            wind = wind.replace(',', '.')
            rain_next_two_hours = b.find(class_="maps-widget-fact__title").getText()
            weather = phrases.yandex.format(temp, feels_like, looks_like.lower(), emoji, rain_next_two_hours.lower(),
                                            wind)
            return weather
        except:
            return phrases.yandex_error


def getEmoji(looks_like):
    if looks_like:
        if looks_like == 'Гроза':
            return e.thunderstorm
        elif looks_like == 'Небольшой дождь':
            return e.rainWithCloud
        elif looks_like == 'Дождь':
            return e.rainWithCloud + e.umbrella
        elif looks_like == 'Снег':
            return e.snowWithCloud + ' ' + e.snowflake
        elif looks_like == 'Небольшой снег':
            return e.snowflake
        elif looks_like == 'Туман':
            return e.atmosphere
        elif looks_like == 'Ясно':
            return e.clearSky
        elif looks_like == 'Малооблачно':
            return e.sunWithSmallCloud
        elif looks_like == 'Облачно с прояснениями':
            return e.fewClouds
        elif looks_like == 'Пасмурно':
            return e.clouds
        else:
            return e.defaultEmoji  # Default emoji

    else:
        return e.defaultEmoji  # Default emoji


if __name__ == "__main__":
    yp = Yandex_parser()
    print(yp.parse("60", "30"))
