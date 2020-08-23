from plyer import notification
import requests
from bs4 import BeautifulSoup
from time import sleep

def notifyMe(title,message):
    notification.notify(
        title= title,
        message=message,
        app_icon="E:\python_projects\corona-notification\corona2.ico",
        timeout=5
    )

def getData(url):
    r=requests.get(url)
    return r.text


if __name__=="__main__":
    # notifyMe("Redeye","i am redeye_07")
    url="https://www.deccanherald.com/national/coronavirus-india-update-state-wise-total-number-of-confirmed-cases-deaths-on-july-20-863337.html"
    myData=getData(url)
    # print(myData)
    
    soup = BeautifulSoup(myData, 'html.parser')
    table=soup.find_all('table')
    elements=table[0].find_all('tr')
    # print(tr[0])
    headers=elements[0].find_all('td')
    header1=headers[0].text
    header2=headers[1].text
    header3=headers[2].text
    head=[header1,header2,header3]
    # print(tr)
    # print(len(tr))
    states=['Odisha','West Bengal']
    for element in elements[1:39]:
        body=element.find_all('td')
        if body[0].text in states:
            msg=""
            c=0
            for each in body:
                msg+=f"{head[c]} : {each.text}\n"
                c+=1
            title="Corona Virus Update:"
            
            notifyMe(title,msg)
            sleep(3)


        