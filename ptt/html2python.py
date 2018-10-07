i=0
for line in open("index.txt", 'r', encoding = 'utf8'):  
    print("html"+"["+str(i)+"]"+"="+"\""+line.replace("\"","\\\"").replace("\n","")+"\"")
    i=i+1