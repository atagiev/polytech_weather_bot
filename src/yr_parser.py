import requests, bs4
import src.phrases as phrases


class Yr_parser:
    def __init__(self):
        self.website = "https://yr.no/?lat={}&lon={}"

    def parse(self, lat, lon):
        try:
            link = self.website.format(lat, lon)

            r = requests.get(link)
            b = bs4.BeautifulSoup(r.content, "html.parser")
            temp = b.find(class_="temperature plus").getText()
            feels_like = b.find(class_="temperature plus").getText()


            weather = phrases.yr.format(temp, feels_like,1,1,1)

            return weather
        except:
            return phrases.yr_error


if __name__ == "__main__":
    yp = Yr_parser()
    print(yp.parse("60", "30"))