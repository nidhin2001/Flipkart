from bs4 import BeautifulSoup
import requests






try:
    for a in range(1,30):
        res = requests.get(f"https://www.flipkart.com/search?q=smart+phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&sort=relevance&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DInfinix&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DASUS&page={a}")
        soup =BeautifulSoup(res.text, "html.parser")
        phone=soup.find_all("div", class_="_3pLy-c row")

        for i in phone:
            phone_name=i.find("div",class_="col col-7-12").div.text
            price=i.find("div",class_="_30jeq3 _1_WHN1").text
            #rateing = i.find("div", class_="_3LWZlK").text
            #views = i.find('span', class_="_2_R_DZ").text
            print(phone_name,price)

            break


except:
    print('e')

