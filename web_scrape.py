from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def scrape(url):

    headers = {'Accept-Encoding': 'identity'}
    r = requests.get(url, headers=headers)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    #print(soup.prettify())
    mydivs = soup.findAll("span", {"class" : "pull-right"})
    #print(mydivs)

    for m in mydivs:
        print(m.text)


    ajax_call = url + "/data"
    print(ajax_call)
    cookies = {'multiline_session' : 'eyJpdiI6IlJ4N1hsUkU0UGpGQ0NsZGcwdkRHcFE9PSIsInZhbHVlIjoidGhWb3IxVmIxNmtKMnNsYmppSXBMV3pkKzZhOVNaZFRPOUdsWU95OWp2NFwvWmZEMlY1WUxXSXREZEFGNVNyYVkiLCJtYWMiOiI0OTZlZjBkNjA4NWVjMTY0YzgzMjY4MGMxZmVjMTA1NGEyYTNkMjg3NDdiN2Q5MDMyMGUzMGYwNTE3ZGVmMWMxIn0%3D'}
    ajax_r = requests.post(ajax_call, cookies=cookies)
    pprint(ajax_r.headers)
    #pprint(ajax_r.status_code, ajax_r.reason)
    #print(ajax_r.json())
    driver = webdriver.Chrome(r"C:\Users\NPT 10\PycharmProjects\exam\chromedriver.exe")
    driver.get(url)
    #for row in driver.find_element_by_xpath("/html/div[1]/div/table/tbody/tr[2]"):
    #    print(row)
    td = driver.find_element_by_class_name('td-rand-pick')
    #print(dir(td))
    xsoup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    #print(xsoup.prettify())

if __name__ == "__main__":
    scrape("http://multiline.npt/_trade")