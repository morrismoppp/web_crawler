import  requests

'''?後為參數設定 ex:popular=false(不爬熱門板)，limit=100(爬前100筆)'''
limit=100
r = requests.get("https://www.dcard.tw/service/api/v2/forums/sex/posts?popular=false&limit=%d"%(limit)) 
titles = r.json()


ans=[]
for i in range(len(titles)):
    try:
        ans.append(titles[i]['mediaMeta'][0]['url'])
    except:
        continue
        
for i in range(len(ans)):
    image_url=ans[i]
    try:
        img = requests.get(image_url) 
    except:
        continue
    with open('C:/Users/M10817021/Desktop/webnorm/img/%d.png'%(i+1),'wb') as f: 
        f.write(img.content)#byte格式
