# README  

## 客戶分群與實驗規劃  
**客戶分群與實驗規劃**: https://drive.google.com/open?id=10Mx4_SRAY1XVbIMDz-y3VirwhLns-JUQNl-RjMnXPCM  
**提案說明**: https://drive.google.com/open?id=16V9w0s-zYQdXPxJl0B3-oJn28fReU-VhFQGch3sQJ3s  
**期末報告**: https://drive.google.com/open?id=11MGk_Lhe6OpgLEpmnn4GEe6IYPWDt6px-N_KlaP2W3Q  

## 數據前處理  
### dataPreprocessing_Orders&Member.ipynb [link](./dataPreprocessing_Orders&Member.ipynb)  
挑出需要的欄位：  
* Member.csv  
    * MemberId  
    * GenderTypeDef  
    * RegisterSourceTypeDef  
    * OpenCardPresent  
    * IsInBlackList  
* Orders.csv  
    * MemberId  
    * OrderGroupCode  
    * DateId  
    * TrackSourceTypeDef  
    * TrackDeviceTypeDef  
    * PromotionDiscount  
    * ECouponDiscount  
    * SalesOrderSlaveTotalPayment  
    * SalesOrderSlaveDateTime  
    * City  

並做轉換：
* Orders.csv  
    * **MemberId**  
        * NAN: 0  
    > 無須處理  
    * **GenderTypeDef**  
        * NAN: 621870  
        * Female: 234540  
        * Male: 2736  
    > 新增兩個欄位 Female, Male  
    * **RegisterSourceTypeDef**  
        * NAN: 3  
        * Web: 624375  
        * AndroidApp: 109704  
        * iOSApp: 95064  
    > 更改內容 web->1, App->0  
    * **OpenCardPresent**  
        * NAN: 0  
        * 0: 624888  
        * others: 234258  
    > 更改內容 0->1, others&NAN->0  
    * **IsInBlackList**  
        * NAN: 858142  
        * 是: 680  
        * 否: 324  
    > 更改內容 是->1, 否&NAN->0  

* Member.csv  
    先進行聚合運算  
    * by  
        * MemberId  
        * OrderGroupCode  
    * Item  
        * DateId: first  
        * TrackSourceTypeDef: first  
        * TrackDeviceTypeDef: first  
        * PromotionDiscount: sum  
        * ECouponDiscount: sum  
        * SalesOrderSlaveTotalPayment: sum  
        * SalesOrderSlaveDateTime: first  
        * City: first  

    再進行欄位轉換  
    * **TrackSourceTypeDef**  
        * NAN: 0  
        * Web: 817281  
        * AndroidApp: 272290  
        * iOSApp: 254363  
    > 更改內容： Web->0, AndroidApp&iOSApp->1  

    * **TrackDeviceTypeDef**  
        * Mobile: 1140763  
        * PC: 203097  
        * Pad: 74  
    > 更改內容： Mobile->0, PC&Pad->1  

    * **City**  
        * 新北市: 280053  
        * 台中市: 194912  
        * 台北市: 162884  
        * 桃園市: 143239  
        * 高雄市: 142018  
        * 台南市: 100734  
        * 彰化縣:  49809  
        * 新竹市:  34922  
        * 屏東縣:  32269  
        * 新竹縣:  30720  
        * 苗栗縣:  26422  
        * 雲林縣:  22382  
        * 基隆市:  21302  
        * 宜蘭縣:  21296  
        * 南投縣:  18975  
        * 嘉義縣:  17372  
        * 花蓮縣:  17180  
        * 嘉義市:  13838  
        * 台東縣:   8797  
        * 澎湖縣:   4397  
        * 屏東市:    201  
        * 台東市:    122  
        * 桃園縣:     21  
        * 1st: 16  
        * New: 10  
        * <fo: 7  
        * Tao: 5  
        * Nan: 5  
        * Tai: 3  
        * 25:  3  
        * No.: 2  
        * Daf: 2  
        * Jia: 2  
        * Kot: 2  
        * Aya: 1  
        * Keb: 1  
        * Cha: 1  
        * Kao: 1  
        * Đại: 1  
        * Ins: 1  
        * Hy:  1  
        * Hsi: 1  
        * Quậ: 1  
        * Xin: 1  
        * NAN: 2  
    > 刪除缺失資料   
    > 新增欄位：  
            * 台北市: A  
            * 台中市: B  
            * 基隆市: C  
            * 台南市: D  
            * 高雄市: E  
            * 新北市: F  
            * 宜蘭縣: G  
            * 桃園市: H  
            * 嘉義市: I  
            * 新竹縣: J  
            * 苗栗縣: K  
            * 台中市: L  
            * 南投縣: M  
            * 彰化縣: N  
            * 新竹市: O  
            * 雲林縣: P  
            * 嘉義縣: Q  
            * 台南縣: R  
            * 高雄縣: S  
            * 屏東縣: T  
            * 花蓮縣: U  
            * 台東縣: V  
            * 金門縣: W  
            * 澎湖縣: X  
            * 陽明山: Y  
            * 連江縣: Z  

分別儲存成 df_Mem.csv & df_O.csv  

### dataMerge_Order&Member.ipynb [link](./dataMerge_Order&Member.ipynb )  
讀取 df_Mem.csv & df_O.csv ，並透過 pandas.merge 來結合兩個 dataframe。  
儲存成 mergeData.csv 。  

### markByNumofOrder.ipynb [link](./markByNumofOrder.ipynb)  
讀取 mergeData.csv 加註是該用戶的第幾筆訂單。  
儲存成 df_mark.csv 。  

## 分成 Training Data & Testing Data  
### segMarkData.ipynb [link](./segMarkData.ipynb)  
讀取 df_mark.csv 並以第 N 筆訂單來做區分，分成 df_seg1~20 並儲存。  

### PCAwithDividedintoTraining&TestingData.ipynb [link](./PCAwithDividedintoTraining&TestingData.ipynb)  
讀取 df_seg1~20 後分成 Training&TestingData ，做 PCA 分析。  
等同於 PCA.py [link](./PCA.py)，可直接使用，使用方法如下。  
```
$ python PCA.py ratio
```
其中 ratio: Training Data 佔的比例，範圍為 0 ~ 1。  

---  

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