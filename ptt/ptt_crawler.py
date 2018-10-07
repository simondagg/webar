import requests
import json
import os
from bs4 import BeautifulSoup
from time import sleep
import re
def get_soup(url):
    # resp = requests.get(
    #     url=url,
    #     cookies={'over18': '1'}
    # )
    resp=requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup

def crawler_page(url,page_number):
	
	soup = get_soup(url)
	divs = soup.find_all('div', 'btn-group-paging')

	last_page=""

	for a in divs:
		last_page=a.find_all('a')

	num=""
	last_page=last_page[1]
	for x in last_page.get('href'):
		if(x.isdigit()):
			num=num+x;
	i=int(num)+1;

	articles = []

	j=0
	while len(articles)<page_number:

	    url="https://www.ptt.cc/bbs/Beauty/index"+str(i)+".html"
	    soup = get_soup(url)
	    divs = soup.find_all('div', 'r-ent')

	    for d in divs:
	                 
	        push_count=d.find('div', 'nrec').string
	        if d.find('a') and push_count=="爆" and d.find('a').string[1]!="公"and d.find('a').string[1]!="新": 
	            href = "https://www.ptt.cc"+d.find('a')['href']
	            title = d.find('a').string
	            date=d.find('div', 'date').string
	            push=""
	            content=""
	            content_href=""
	            ptt_id=str(j)
	            articles.append({
	            	'id':ptt_id,
	                'title': title,
	                'href': href,
	                'date':date,
	                'push':push,
	                'content':content,
	                'content_href':content_href
	            })
	            j=j+1
	            print('#'*j)
	            
	            os.system('cls')

	    i=i-1;
	return articles

def get_push(soup):
	push = soup.find_all('div', 'push')
	push_content=[]
	i=0
	push_amount=3
	for p in push:
		s=p.find('span', 'push-content')
		push_c=str(s.string).replace(": ", "")
		push_content.append({
	                'push_content': push_c
	            })
		i=i+1
		if i==push_amount:
			break
	content="有人直呼"+"「"+push_content[0]['push_content']+"」"+"，"+"網友說"+"「"+push_content[1]['push_content']+"」"+"，"+"也有網友認為"+"「"+push_content[2]['push_content']+"」"
	return content

def get_content(soup):
	article=soup.find_all('span','article-meta-value')
	date=article[3].string
	content = soup.find(id="main-content").text
	target_content = "--"
            #u'※ 發信站: 批踢踢實業坊(ptt.cc),'
	content = content.split(target_content)
	content = content[0].split(date)
	main_content = content[1]
	main_content =main_content.replace("\n", "<br>")
	return main_content

def get_urlofcontent(content):
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.', content)
	return urls

def get_push_content(articles):
	i=0
	while i<len(articles):
		soup=get_soup(articles[i]['href'])
		articles[i]['push']=get_push(soup)
		content=get_content(soup)
		articles[i]['content']=content
		articles[i]['content_href']=get_urlofcontent(content)
		i=i+1

	return articles

#main

url="https://www.ptt.cc/bbs/Beauty/index.html"#35行一起改
page_number=100
articles=crawler_page(url,page_number)
ptt=get_push_content(articles)

with open("ptt2.json","w+",encoding='utf8') as f:
    json.dump(ptt,f,ensure_ascii=False)
print("已抓取ptt內容")