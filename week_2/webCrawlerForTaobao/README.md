# README
|Item       |content
|-----------|---
|Title      |webCrawlerForTaobao
|Description|進階軟體專案開發(107下學期修習)作業, 以python撰寫網路爬蟲程式, 爬取掏寶網資料.
|Author    |Sopper
|E-mail    |sopper08@gmail.com
|Edit Time |2018/3/12

## HOWTODO  
### STEP 1
到掏寶網先查詢保溫杯.  
![](images/searchInsulationCup.png)
### STEP 2  
此次爬蟲使用的方法為: 抓下/上一頁所傳出/入的資料, 通常會包含需要的內容.  
按F12 -> Network -> 先clear.  
![](images/network1.png)
### STEP 3  
按上/下一頁  
![](images/network2.png)
### STEP 4  
從Requests資料中找可以拿來爬蟲的資料(篩選前面的區域).   
![](images/network3.png)
### STEP 5  
找到好爬蟲的資料後, 點擊右邊的Headers, 紀錄Request URL & Request Method.  
![](images/network4.png)
### STEP 6
到Postman以Request URL & Request Method檢查得到的資料是否正確, 並確定資料格式.
![](images/postman.png)
點選postman裡的params可以整理API, 藉由調整參數來知道每個值代表的意義.
![](images/postmanParams.png)  
### STEP 7  
原本API裡有callback參數, 但會影響回傳的資料(使資料不符合Json格式), 但刪掉並不影響回傳內容, 故丟Request時可刪除, 方便爬資料!  
### STEP 8  
Coding!!!  
請參照webCrawlerForTaobao.ipynb  
## 參考資料  
1. 大數學堂: http://www.largitdata.com/course_list/1  
2. 以python來解碼Json格式: http://www.runoob.com/python/python-json.html  
3. python-簡易爬蟲筆記: https://bonze.tw/python-%E7%B0%A1%E6%98%93%E7%88%AC%E8%9F%B2%E7%AD%86%E8%A8%98/  
4. [爬蟲實戰] 如何抓取591租屋網的資訊?(python格式的爬蟲): https://www.youtube.com/watch?v=zzMRbrOHlrk  
5. [爬蟲實戰] 如何突破蝦皮拍賣的重重限制以順利抓取拍賣商品資訊: https://www.youtube.com/watch?v=jV6eHoLzD2E&feature=youtu.be  
6. Pandas在Python上的應用: https://oranwind.org/python-pandas-ji-chu-jiao-xue/  