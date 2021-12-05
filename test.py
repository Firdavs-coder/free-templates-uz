import requests
from bs4 import BeautifulSoup



sahifa = "https://www.free-css.com/template-categories/hosting"
sahifa2 = "https://www.free-css.com/free-css-templates/page266/data-web"
sahifa3 = "https://www.free-css.com/template-categories"

r = requests.get(sahifa)
soup = BeautifulSoup(r.text, 'html.parser')
news = 'https://www.free-css.com' +  str(soup.select('ul[class="clear"] li img')[0]['src'])
news3 = 'https://www.free-css.com' + str(soup.select('ul[class="clear"] li a')[0]['href'])



r2 = requests.get(sahifa2)
soup = BeautifulSoup(r2.text, 'html.parser')
news2 = soup.select('ul[class="clear"] li[class="dld"] a')[0]["href"]

r3 = requests.get(sahifa3)
soup = BeautifulSoup(r3.text, 'html.parser')
news4 = soup.select('ul[class="clear"] li a')
l = []
for i in news4:
    l.append(i.text)
# # print(get_three_image[0]['src'])
        # image = 'https://www.free-css.com' +  str(soup.select('ul[class="clear"] li img')[0]['src'])
        # href = 'https://www.free-css.com' + str(soup.select('ul[class="clear"] li a')[0]['href'])


        # sahifa2 = href
        # r2 = requests.get(sahifa2)
        # soup = BeautifulSoup(r2.text, 'html.parser')
        # zip = 'https://www.free-css.com' +  soup.select('ul[class="clear"] li[class="dld"] a')[0]["href"]

        # bot.send_photo(message.chat.id, image, caption=href)
        # bot.send_document(message.chat.id, zip)
print(l)




print(news[0])
print('https://www.free-css.com' + news2)



