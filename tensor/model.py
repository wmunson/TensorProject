from bs4 import BeautifulSoup as bs
import requests
import feedparser
import html5lib


title = 'Apple'

url = 'https://en.wikipedia.org/wiki/'+title

wiki_url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json'


content = requests.get(url).content

soup = bs(content,'lxml')
print('========================================================================================================================')
body = soup.find('div',{'id':'mw-content-text'})
# text=body.get_text()
# print(text)



# text = soup.get_text()
# print (text)
# b = body.replace('<a')

# body = soup.findAll('div',{'id':'bodyContent'})

# para = body.findAll('p')
# arr=[]
# for p in para:
# 	# p.replace('<b>','')
# 	# print(p)
# 	arr.append(p)
# print(arr[0].content)
# with urlopen(url) as f:
#     document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())

#     