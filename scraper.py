import urllib.request
from bs4 import BeautifulSoup
import json

url = "https://loteriasdominicanas.com/pagina/ultimos-resultados"

try:
    html = urllib.request.urlopen(url).read()
except:
    print("Error opening the url")
    exit()

soup = BeautifulSoup(html, "html.parser")
numbers = soup.select('div.row div.game-scores span.score')

results = {}

for number in numbers:
    game = number.parent.parent.select('a.game-title span')[0].contents[0].strip()
    lottery = number.parent.parent.select('div.company-title a:first-child')[0].contents[0].strip()
    _number = number.contents[0].strip()
    try:
        results[lottery]['games'][game].append(_number)
    except KeyError:
        if results.get(lottery):
            results[lottery]['games'][game] = [_number]
        else:
            results[lottery] = {
                'games': {
                    game : [_number]
                }
            }


print(json.dumps(results))