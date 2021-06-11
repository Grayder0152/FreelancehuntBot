import requests
from bs4 import BeautifulSoup as Bs

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
BASE_URL = 'https://freelancehunt.com/projects/skill/'
project_filter = 'parsing-dannyih/169.html'


def parse_projects():
    page = requests.get(BASE_URL + project_filter, headers=HEADERS)
    html = Bs(page.content, 'html.parser')

    return html.find_all('a', {'class': 'bigger visitable'})



