import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

soup = BeautifulSoup(webpage.content, "html.parser")
#print(soup)
ratings=[]
webscrapped = soup.find_all("td", class_="Rating")
for i in webscrapped:
  if i.text=="Rating":
    print(i.text)
  else:
    rate = float(i.text)  
    ratings.append(rate)
plt.hist(ratings)
plt.show()


#print(soup)
webscrappedComp = soup.find_all("td", class_="Company")
#print(len(ratings))
Companies=[]
for z in range(1,len(webscrappedComp)):
  if webscrappedComp[z].text=="Company":
    print(z.text)
  else:
    comp = webscrappedComp[z].text  
    Companies.append(comp)
#companies = np.array(Companies)
#conpanies = np.reshape(companies, (1, len(companies)))
#ratings = np.array(ratings)
#ratings = np.reshape(ratings, (1, len(ratings)))
d = {"Company": Companies, "Rating": ratings}
cacao_df = pd.DataFrame.from_dict(d)
#Lcr=np.vstack((companies,ratings))
#df = pd.DataFrame(Lcr, columns = ['Company','Rating'])

mean_vals = cacao_df.groupby('Company').Rating.mean()
ten_best = mean_vals.nlargest(10)
print(ten_best)

cocoa_percents = []
webscrappedCacao = soup.find_all("td", class_="CocoaPercent")
for z in range(1,len(webscrappedCacao)):
  if webscrappedCacao[z].text=="CacaoPercent":
    print(z.text)
  else:
    cacao = webscrappedCacao[z].text  
    cocoa_percents.append(float(cacao.strip('%')))

d = {"Company": Companies, "Rating": ratings, "CacaoPercentage": cocoa_percents}
df = pd.DataFrame.from_dict(d)
plt.clf()
plt.scatter(df.CacaoPercentage, df.Rating)
a = np.polyfit(df.CacaoPercentage, df.Rating, 1)
line_function = np.poly1d(a)
plt.title("Line")
plt.plot(df.CacaoPercentage, line_function(df.CacaoPercentage), "r--")
plt.show()

