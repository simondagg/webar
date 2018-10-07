

import json

open_file = open( 'ptt2.json', 'r', encoding = 'utf8' )
s = open_file.read()

#print(json.loads(s))
ptt=json.loads(s)


h=0
html=[]
while h<=138:
	html.append("")
	h=h+1

html[0]="<!DOCTYPE html>"
html[1]="<html lang=\"en\">"
html[2]="  <head>"
html[3]="    <meta charset=\"utf-8\">"
html[4]="    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
html[5]="    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
html[6]=""
html[7]="<title>ptt新聞</title>"
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
html[31]="							<a href=\"index.html\">首頁</a>"
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
html[50]="									<a href=\"https://www.ptt.cc/bbs/Gossiping/index.html\">ptt網站版</a>"
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



i=0
card1=""
while i<66:
	card1=card1+html[i]
	i=i+1
#
i=1
card2=""
while i<=3:
	p1=i*3-3
	p2=i*3-2
	p3=i*3-1
	url1=str(ptt[p1]['content_href']).split("'")
	url1=str(url1[1]).split("<br>")
	url2=str(ptt[p2]['content_href']).split("'")
	url2=str(url2[1]).split("<br>")
	url3=str(ptt[p3]['content_href']).split("'")
	url3=str(url3[1]).split("<br>")
	html[67]="			"
	html[68]="			<div class=\"row\">"
	html[69]="				<div class=\"col-md-4\">"
	html[70]="				</div>"
	html[71]="				<div class=\"col-md-4\">"
	html[72]="					<div class=\"row\">"
	html[73]="						<div class=\"col-md-4\">"
	html[74]="							<div class=\"thumbnail\">"
	html[75]="								<img alt=\"Bootstrap Thumbnail First\" src=\""+url1[0]+"\">"
	html[76]="								<div class=\"caption\">"
	html[77]="									<h3>"
	html[78]=ptt[p1]['title']
	html[79]="									</h3>"
	html[80]="									<p>"
	html[81]=ptt[p1]['push']
	html[82]="									</p>"
	html[83]=""
	html[84]="									<p>"
	html[85]="										<a class=\"btn btn-primary\" href=\""+"web"+str(p1)+".html"+"\">點我看新聞</a>"
	html[86]="									</p>"
	html[87]="								</div>"
	html[88]="							</div>"
	html[89]="						</div>"
	html[90]="						<div class=\"col-md-4\">"
	html[91]="							<div class=\"thumbnail\">"
	html[92]="								<img alt=\"Bootstrap Thumbnail Second\" src=\""+url2[0]+"\">"
	html[93]="								<div class=\"caption\">"
	html[94]="									<h3>"
	html[95]=ptt[p2]['title']
	html[96]="									</h3>"
	html[97]="									<p>"
	html[98]=ptt[p2]['push']
	html[99]="									</p>"
	html[100]="									<p>"
	html[101]="										<a class=\"btn btn-primary\" href=\""+"web"+str(p2)+".html"+"\">點我看新聞</a>"
	html[102]="									</p>"
	html[103]="								</div>"
	html[104]="							</div>"
	html[105]="						</div>"
	html[106]="						<div class=\"col-md-4\">"
	html[107]="							<div class=\"thumbnail\">"
	html[108]="								<img alt=\"Bootstrap Thumbnail Third\" src=\""+url3[0]+"\">"
	html[109]="								<div class=\"caption\">"
	html[110]="									<h3>"
	html[111]=ptt[p3]['title']
	html[112]="									</h3>"
	html[113]="									<p>"
	html[114]=ptt[p2]['push']
	html[115]="									</p>"
	html[116]="									<p>"
	html[117]="										<a class=\"btn btn-primary\" href=\""+"web"+str(p3)+".html"+"\">點我看新聞</a>"
	html[118]="									</p>"
	html[119]="								</div>"
	html[120]="							</div>"
	html[121]="						</div>"
	html[122]="					</div>"
	html[123]="				</div>"
	html[124]="				<div class=\"col-md-4\">"
	html[125]="				</div>"
	html[126]="			</div>"
	html[127]=""
	j=67
	while j<127:
		card2=card2+html[j]
		j=j+1
	i=i+1
		



#


html[128]=""
html[129]=""
html[130]="		</div>"
html[131]="	</div>"
html[132]="</div>"
html[133]=""
html[134]="    <script src=\"js/jquery.min.js\"></script>"
html[135]="    <script src=\"js/bootstrap.min.js\"></script>"
html[136]="    <script src=\"js/scripts.js\"></script>"
html[137]="  </body>"
html[138]="</html>"
i=127
card3=""
while i<138:
	card3=card3+html[i]
	i=i+1
output=card1+card2+card3
g = open("index.html",'w+', encoding = 'utf8')	
g.write(output)