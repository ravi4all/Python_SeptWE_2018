import bs4
import urllib.request as url
print("Type quit to exit")
while True:
    name = input("Enter movie name : ")
    if name == "quit":
        break
    web = url.urlopen("https://www.imdb.com/find?ref_=nv_sr_fn&q="+name)
    page = bs4.BeautifulSoup(web, 'lxml')
    td = page.find('td', class_='result_text')
    # print(td)
    # print(td.a['href'])
    href = td.a['href']
    newLink = 'https://www.imdb.com/'+href

    web_2 = url.urlopen(newLink)
    page_2 = bs4.BeautifulSoup(web_2, 'lxml')

    data = page_2.find_all('div', class_ = 'titleBar')
    for name in data:
        # print(name.text.replace("\n", ""))
        t = name.text.replace("\n","")
        print(t.replace("  ", ""))

    summary = page_2.find_all('div', class_='summary_text')
    for s in summary:
        print(s.text)

    cast = page_2.find_all('table', class_='cast_list')
    for c in cast:
        print(c.text.replace("\n",""))