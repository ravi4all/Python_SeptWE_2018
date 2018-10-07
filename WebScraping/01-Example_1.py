import bs4
import urllib.request as url

# Step - 1
web = url.urlopen('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=600ca544-31f5-4bd8-ae38-ea4014c93bab&pf_rd_r=SEDAF8BK7A7XZGM1165W&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1')
# print(web)
# Step - 2
page = bs4.BeautifulSoup(web, 'lxml')
# print(page)

# Step - 3
data = page.find_all('td', class_='titleColumn')
# print(data)

for t in data:
    print(t.text)