from plyer import notification
import requests
import time
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="F:\Projects\COVID Notification\icon1.ico",
        timeout=6
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        # notifyMe("Hello", "Lets stop the spread of virus together")
        myHTMLData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHTMLData, 'html.parser')
        myDataStr = ""
        # print(soup.prettify())
        for tr in soup.find_all('tbody')[7].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Chhattisgarh', 'Madhya Pradesh',
                  'Odisha']
        for item in itemList[0:22]:
            dataList = item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State {dataList[1]}\n Indian : {dataList[2]} & Foreign : {dataList[3]}\n Cured : {dataList[4]}\n Deaths : {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
