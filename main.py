# Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


def tim_link_download(link_khoi_dau):
    list_link_can_download = []
    link_rq = requests.get(link_khoi_dau)
    link_rq_soup = BeautifulSoup(link_rq.text, 'html.parser')
    results = link_rq_soup('div', attrs={'class': 'card-body'})
    print(len(results))

    for results_link in results:
        link_pr = results_link('a', attrs={'href': True})[0]
        k = link_pr['href']
        k = 'https://www.efsa.europa.eu' + k
        link_2 = requests.get(k)
        link_2_soup = BeautifulSoup(link_2.text, 'html.parser')
        result_2 = link_2_soup('a', attrs={'class': 'efsa-file-item--pdf'})
        k2 = result_2[0]['href']
        k3 = k2.replace('epdf', 'pdfdirect') + '?download=true'
        list_link_can_download.append(k3)

    return list_link_can_download

link_khoi_dau = 'https://www.efsa.europa.eu/en/publications?f%5B0%5D=%3A62081&f%5B1%5D=%3Aconclusion_on_pesticides&f%5B2%5D=type%3A331&fbclid=IwAR3zRD1tI9UvPuIt2u1UcM05ZMawI64ztY0RdvzP8PrTr3ObcgWak4jl8PA&s=&page=0'
list_link_download = []
for page in range(62):
    link_page = link_khoi_dau[0:-1] + str(page)
    list_link_download += tim_link_download(link_page)

# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path="chromedriver.exe")

# 2. Mở thử một trang web
for link in list_link_download:
    browser.get(link)
    sleep(3)