import requests
from bs4 import BeautifulSoup
import time

from requests.api import get

def get_post(address):
    url = f"https://search.naver.com/search.naver?where=nexearch&ie=utf8&X_CSA=address_search&query={address}우편번호"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    post = soup.find("div", {"id":"ds_result"}).find('tbody').find('td',{"class":"tc"}).text
    return post
