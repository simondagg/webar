import json
import os

open_file = open( 'ptt2.json', 'r', encoding = 'utf8' )
s = open_file.read()

#print(json.loads(s))
ptt=json.loads(s)
i=0

while i<=len(ptt)-1:
	try:
		url=str(ptt[i]['content_href']).split("'")
		url=str(url[1]).split("<br>")
	except:
		url=["https://i.imgur.com/UfFhMnW.jpg",""]

	c1=(i+1) % len(ptt)
	c2=(i+2) % len(ptt)
	c3=(i+3) % len(ptt)
	print('#'*i)
	
	os.system('cls')
	try:
		url1=str(ptt[c1]['content_href']).split("'")
		url1=str(url1[1]).split("<br>")
	except:
		url1=["https://i.imgur.com/UfFhMnW.jpg",""]
	try:
		url2=str(ptt[c2]['content_href']).split("'")
		url2=str(url2[1]).split("<br>")
	except:
		url2=["https://i.imgur.com/UfFhMnW.jpg",""]
	try:
		url3=str(ptt[c3]['content_href']).split("'")
		url3=str(url3[1]).split("<br>")
	except:
		url3=["https://i.imgur.com/UfFhMnW.jpg",""]
	

	html=[]
	h=0
	
	while h<=147:
		html.append("")
		h=h+1
	html[0]="<!DOCTYPE html>"
	html[1]="<html lang=\"en\">"
	html[2]="  <head>"
	html[3]="    <meta charset=\"utf-8\">"
	html[4]="    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
	html[5]="    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
	html[6]=""
	html[7]="    <title>ptt新聞</title>"
	html[8]=""
	html[9]=""
	html[10]=""
	html[11]="    <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">"
	html[12]="    <link href=\"css/style.css\" rel=\"stylesheet\">"
	html[13]=""
	html[14]="  </head>"
	html[15]="  <body>"
	html[16]=""
	html[17]="    <div class=\"container-fluid\">"
	html[18]="	<div class=\"row\">"
	html[19]="		<div class=\"col-md-12\">"
	html[20]="			<nav class=\"navbar navbar-default\" role=\"navigation\">"
	html[21]="				<div class=\"navbar-header\">"
	html[22]="					 "
	html[23]="					<button type=\"button\" class=\"navbar-toggle\" data-toggle=\"collapse\" data-target=\"#bs-example-navbar-collapse-1\">"
	html[24]="						 <span class=\"sr-only\">Toggle navigation</span><span class=\"icon-bar\"></span><span class=\"icon-bar\"></span><span class=\"icon-bar\"></span>"
	html[25]="					</button> <a class=\"navbar-brand\" href=\"#\">新聞產生器</a>"
	html[26]="				</div>"
	html[27]="				"
	html[28]="				<div class=\"collapse navbar-collapse\" id=\"bs-example-navbar-collapse-1\">"
	html[29]="					<ul class=\"nav navbar-nav\">"
	html[30]="						<li class=\"active\">"
	html[31]="							<a href=\""+"index.html"+"\">首頁</a>"
	html[32]="						</li>"
	html[33]="						"
	html[34]="						<li class=\"dropdown\">"
	html[35]="							 <a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\">其他版<strong class=\"caret\"></strong></a>"
	html[36]="							<ul class=\"dropdown-menu\">"
	html[37]="								<li>"
	html[38]="									<a href=\"#\">八卦版</a>"
	html[39]="								</li>"
	html[40]="								<li>"
	html[41]="									<a href=\"#\">表特版</a>"
	html[42]="								</li>"
	html[43]="								<li>"
	html[44]="									<a href=\"#\">西施版</a>"
	html[45]="								</li>"
	html[46]="								"
	html[47]="								<li class=\"divider\">"
	html[48]="								</li>"
	html[49]="								<li>"
	html[50]="									<a href=\"#\">ptt網站版</a>"
	html[51]="								</li>"
	html[52]="							</ul>"
	html[53]="						</li>"
	html[54]="					</ul>"
	html[55]="					<form class=\"navbar-form navbar-left\" role=\"search\">"
	html[56]="						<div class=\"form-group\">"
	html[57]="							<input type=\"text\" class=\"form-control\">"
	html[58]="						</div> "
	html[59]="						<button type=\"submit\" class=\"btn btn-default\">"
	html[60]="							搜尋"
	html[61]="						</button>"
	html[62]="					</form>"
	html[63]="					"
	html[64]="				</div>"
	html[65]="				"
	html[66]="			</nav>"
	html[67]="			<div class=\"row\">"
	html[68]="				<div class=\"col-md-4\">"
	html[69]="				</div>"
	html[70]="				<div class=\"col-md-4\">"
	html[71]="					<h3>"
	html[72]=ptt[i]['title']
	html[73]="					</h3>"
	html[74]="					<p>"
	html[75]="網友在ptt上表示"+ptt[i]['content']
	html[76]="					</p>"
	count=0
	img=""
	amaount=len(url)
	while count<amaount:
		img=img+"<img src=\""+url[count]+"\" height=\"300\">"+"<br>"

		count=count+1
	img=img+ptt[i]['push']
	html[77]="				</div>"
	html[78]="				<div class=\"col-md-4\">"
	html[79]="				</div>"
	html[80]="			</div>"
	html[81]="			<div class=\"row\">"
	html[82]="				<div class=\"col-md-4\">"
	html[83]="				</div>"
	html[84]="				<div class=\"col-md-4\">"
	html[85]="					<div class=\"row\">"
	html[86]="						<div class=\"col-md-4\">"
	html[87]="							<div class=\"thumbnail\">"
	html[88]="								<img alt=\"Bootstrap Thumbnail First\" src=\""+url1[0]+"\">"
	html[89]="								<div class=\"caption\">"
	html[90]="									<h3>"
	html[91]=ptt[c1]['title']
	html[92]="									</h3>"
	html[93]="									<p>"
	html[94]=ptt[c1]['content'][0:20]
	html[95]="									</p>"
	html[96]="									<p>"
	html[97]="										<a class=\"btn btn-primary\" href=\""+"web"+str(c1)+".html"+"\">點我看新聞</a>"
	html[98]="									</p>"
	html[99]="								</div>"
	html[100]="							</div>"
	html[101]="						</div>"
	html[102]="						<div class=\"col-md-4\">"
	html[103]="							<div class=\"thumbnail\">"
	html[104]="								<img alt=\"Bootstrap Thumbnail Second\" src=\""+url2[0]+"\">"
	html[105]="								<div class=\"caption\">"
	html[106]="									<h3>"
	html[107]=ptt[c2]['title']
	html[108]="									</h3>"
	html[109]="									<p>"
	html[110]=ptt[c2]['content'][0:20]
	html[111]="									</p>"
	html[112]="									<p>"
	html[113]="										<a class=\"btn btn-primary\" href=\""+"web"+str(c2)+".html"+"\">點我看新聞</a>"
	html[114]="									</p>"
	html[115]="								</div>"
	html[116]="							</div>"
	html[117]="						</div>"
	html[118]="						<div class=\"col-md-4\">"
	html[119]="							<div class=\"thumbnail\">"
	html[120]="								<img alt=\"Bootstrap Thumbnail Third\" src=\""+url3[0]+"\">"
	html[121]="								<div class=\"caption\">"
	html[122]="									<h3>"
	html[123]=ptt[c3]['title']
	html[124]="									</h3>"
	html[125]="									<p>"
	html[126]=ptt[c3]['content'][0:20]
	html[127]="									</p>"
	html[128]="									<p>"
	html[129]="										<a class=\"btn btn-primary\" href=\""+"web"+str(c3)+".html"+"\">點我看新聞</a>"
	html[130]="									</p>"
	html[131]="								</div>"
	html[132]="							</div>"
	html[133]="						</div>"
	html[134]="					</div>"
	html[135]="				</div>"
	html[136]="				<div class=\"col-md-4\">"
	html[137]="				</div>"
	html[138]="			</div>"
	html[139]="		</div>"
	html[140]="	</div>"
	html[141]="</div>"
	html[142]=""
	html[143]="    <script src=\"js/jquery.min.js\"></script>"
	html[144]="    <script src=\"js/bootstrap.min.js\"></script>"
	html[145]="    <script src=\"js/scripts.js\"></script>"
	html[146]="  </body>"
	html[147]="</html>"
	j=0
	ptt_content=""
	while j<=76:
		ptt_content=ptt_content+html[j]
		j=j+1
	ptt_content=ptt_content+img
	while j<=147:
		ptt_content=ptt_content+html[j]
		j=j+1
	output="web"+str(i)+".html"
	g = open(output,'w+', encoding = 'utf8')	
	g.write(ptt_content)
	i=i+1
print("轉換成網頁")
