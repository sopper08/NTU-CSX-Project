# README  

## 客戶分群與實驗規劃  
**slide**: https://drive.google.com/open?id=10Mx4_SRAY1XVbIMDz-y3VirwhLns-JUQNl-RjMnXPCM  

## 數據前處理
### dataPreprocessing_Orders&Member.ipynb
### dataMerge_Order&Member.ipynb
### markByNumofOrder.ipynba

## 分配 Training Data & Testing Data  
### segMarkData.ipynb


## Useless
### finalProjectGrouping：  
* 針對data/NTU_1317_PromotionOrders進行分析。  
### finalProjectGrouping1：  
* 都是以每個客戶。  
* 針對data/Ntu_Order進行分析，繪製成散點圖。  
* x軸為 (促銷活動訂單+折扣卷訂單)/總訂單  
* y軸為 折扣金額/總訂單金額。  
* 分析時間：201701~201712，以每個月為標準。  
### finalProjectGrouping1_filter：  
* 將Ntu_Order的失敗訂單濾除，再做一次一樣的分析，並加上訂單量做深淺對比。  
* 剔除少筆訂單的客戶。  
* 完成後發現需要再更改一次兩軸，並以消費金額當作深淺來作圖！  
### finalProjectGrouping2：  
* 都是以每個客戶。  
* 橫軸為總訂單量，縱軸為actOrderPercent(%)，深淺為平均每筆消費金額(原價)。  
## finalProjectGrouping3：  
* 都是以每個客戶。  
* 原本都是用訂單量，現在使用購物車為單筆訂單。  
## shoppingBehaviorByMemberId:
* 分析客戶的購物行為。  