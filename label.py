import requests
from bs4 import BeautifulSoup

from requests.api import get



def get_post(address):
    url = f"https://search.naver.com/search.naver?where=nexearch&ie=utf8&X_CSA=address_search&query={address}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    post = soup.find("div", {"id":"place-app-root"}).find('span',{"class":"_3rnws"}).text.strip("우, 편, 번, 호")
    return post

