import requests
import re
import json
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 以dict儲存所有爬下來的文章項目
pttArticledict = {}

# ptt的path，因為爬下來的網址需加進此path才能link
pttpath = "https://www.ptt.cc"

# post的payload
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

# 進入文章列表
req = requests.session()

# 先post解決18禁按鈕問題
res = req.post('https://www.ptt.cc/ask/over18', verify=False, data=payload)
res = req.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify=False)
soup = BeautifulSoup(res.text, "lxml")

index = 0
for entry in soup.select('.r-ent')[:-5]:
    index = index + 1
    
    # 以tempdict暫存資料，再加入pttArticledict
    tempdict = {}
    # path, no path -> deleted article
    try:
        partpath = entry.select('a')[0]['href']
        articleNum = partpath.split('/')[3].split('.html')[0]
        path = pttpath + partpath
        # author
        author = entry.select('.author')[0].text
        # title
        title = entry.select('.title')[0].text[1:-1]
        
        tempdict['a_連結'] = path
        tempdict['b_作者'] = author
        tempdict['c_標題'] = title

        # 進入文章頁面
        res1 = req.get(path, verify=False)
        soup1 = BeautifulSoup(res1.text, "lxml")
        # ip
        ip =  soup1.find_all(text=re.compile('發信站: 批踢踢實業坊'))[0].split(':')[-1][1:-1]
        # date
        date = soup1.select('#main-container #main-content div.article-metaline .article-meta-value')[2].text
        # content
        content = soup1.find(id="main-content").text.split('※ 發信站: 批踢踢實業坊(ptt.cc)')
        content = content[0].split(date)[1].replace('\n',' ')
        tempdict['d_日期'] = date
        tempdict['e_ip'] = ip
        tempdict['f_內文'] = content
        # push state
        num, b, g, n, messageSet = 0, 0, 0, 0, {}
        for entry in soup1.select('.push'):
            push_messenger = entry.select('span')[1].text
            push_content = entry.select('span')[2].text[2:]
            push_time = entry.select('span')[3].text[1:-1]
            
            message = {}
            pushstateStat = {}
            num += 1
            push_state = entry.select('span')[0].text[:-1]
            if push_state==u'推':
                b += 1
            elif push_state==u'噓':
                g += 1
            else:
                n += 1
            
            message['push_state'] = push_state
            message['push_content'] = push_content
            message['push_time'] = push_time
            message['push_messenger'] = push_messenger
            messageSet[num] = message
        tempdict['g_推文'] = messageSet
        pushstateStat['all'] = b+g+n
        pushstateStat['b'] = b
        pushstateStat['g'] = g
        pushstateStat['n'] = n
        tempdict['h_推文'] = pushstateStat
        
    except:
        articleNum = 'deleted_article'
    
    pttArticledict[articleNum] = tempdict

    print("---第{0}篇文章爬蟲完成！---".format(index))

outputJson = json.dumps(pttArticledict,ensure_ascii=False)
print(outputJson)