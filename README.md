# README
以下為檔案介紹，標題為檔名(or資料夾)。  

## week_1  
*Pandas*  
熟悉pandas組件。  
#### pandasFunctionTestCode [*(link)*](week_1/pandasFunctionTestCode.ipynb)  

關於pandas函式庫的學習，裡面試做了幾個工具，更詳細可參閱Python/Module/pandas。  
#### week_1_first_meet [*(link)*](week_1/week_1_first_meet.ipynb)  
與上者相同。  

## week_2  
*Web crawler*  
#### webCrawlerForTaobao [*(link)*](week_2/webCrawlerForTaobao/webCrawlerForTaobao.ipynb)  
根據大數學堂的教學影片，進行掏寶網保溫杯的爬蟲。  

## week_3  
*visualization, Web crawler*  
#### orderQuantity [*(link)*](week_3/orderQuantity.ipynb)  
1. 針對訂單來自不同的裝置(web or APP)，做訂單量分析並視覺化。  
2. 將訂單量以每個月分級，並視覺化。  

## week_4  
*Nature language, Jieba, Word Cloud*  
#### SongOfJamHsiao [*(link)*](week_4/SongOfJamHsiao/SongOfJamHsiao.ipynb)  
將蕭敬騰專輯的11首歌分別作字詞分析，並將其視覺化成文字雲。

## week_5  
*Nature language, Jieba, tf-idf*  
#### task5_tfidf [*(link)*](week_5/task5_tfidf.ipynb)  
將task5資料夾裡的文件資料做tf-idf字詞分析。  

## week_8  
*Machine Learning, SVM, Kaggle, TEP*  
#### week_8 [*(link)*](week_8/README.md)  
以 transer.py 轉換欄位，再以 PSA.py 訓練並計算準確率。  

## FinalProjest  
#### finalProjectGrouping [*(link)*](FinalProject/finalProjectGrouping.ipynb)  
* 針對data/NTU_1317_PromotionOrders進行分析。  
#### finalProjectGrouping1 [*(link)*](FinalProject/finalProjectGrouping1.ipynb)
* 都是以每個客戶。
* 針對data/Ntu_Order進行分析，繪製成散點圖。
* x軸為 (促銷活動訂單+折扣卷訂單)/總訂單
* y軸為 折扣金額/總訂單金額。
* 分析時間：201701~201712，以每個月為標準。
#### finalProjectGrouping1_filter [*(link)*](FinalProject/finalProjectGrouping1_filter.ipynb)  
* 將Ntu_Order的失敗訂單濾除，再做一次一樣的分析，並加上訂單量做深淺對比。
* 剔除少筆訂單的客戶。
* 完成後發現需要再更改一次兩軸，並以消費金額當作深淺來作圖！
#### finalProjectGrouping2 [*(link)*](FinalProject/finalProjectGrouping2.ipynb)  
* 都是以每個客戶。  
* 橫軸為總訂單量，縱軸為actOrderPercent(%)，深淺為平均每筆消費金額(原價)。  
#### finalProjectGrouping3 [*(link)*](FinalProject/finalProjectGrouping3.ipynb)  
* 都是以每個客戶。  
* 原本都是用訂單量，現在使用購物車為單筆訂單。  
