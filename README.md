# MapleStoryMonsterDetect

## 目的
原本是想用物件偵測來辨識楓之谷的怪然後再寫個腳本來打怪，但後來發現這樣辨識不能辨識整張地圖只能辨識當前畫面上的怪，這樣會導至畫面外的怪無法被偵測到，所以之後打算換別得方法試試看，雖然說是做一半才打算換方法，但是我還是把整個結果做出來好方便我做個紀錄。

## 幹話
這個專案好像是從2020/10就開始了不過我每次都只研究了一下就不了了之了，一開始是使用yolov4來偵測因為[GCP](https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=japac-AU-all-en-dr-bkwsrmkt-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_540822681061-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP%20~%20General_cloud%20-%20platform-KWID_43700061083014006-kwd-87853815&userloc_9040379-network_g&utm_term=KW_gcp&gclid=Cj0KCQiAubmPBhCyARIsAJWNpiPUNAjDM8V5Y33edlnnamJ9iSPh1t-zB0pqB1MURVRR5WlBf72Xe-UaApQxEALw_wcB&gclsrc=aw.ds)有免費的GPU可以用來訓練模型，所以就想說來試試看訓練楓之谷的怪物偵測，當時GCP只能選擇tensorflow的模型，用tflite的模型來辨識結果影像處理的速度是真的慢，之後改用yolov5和pytorch在使用CPU的情況下一張圖也要1000ms而使用GPU的的情況下只需10ms


# yolov5
## 環境
### 硬體設備
* **CPU**:i5-9400F
* **GPU**:GTX 1660

### 軟體環境

|          | 版本    |
| -------- | -------|
| Python   |  3.8.5 |
| Cuda     |  11.3  |
| Pytorch  |  1.10.0+cu113 |

## 結果
**使用OpenCV**
![](https://i.imgur.com/gQY39TT.png)
**使用PIL**
![](https://i.imgur.com/9IFyd7i.png)
**讀取視窗**
![](https://github.com/U07157135/MapleStoryMonsterDetect/blob/main/img/Hnet-image.gif)


## 問題
* 問題一
    * SearchWindow這個程式當初在抓取MapleStory視窗時常常會顯示黑畫面，後來才發現是因為使用VScode開啟檔案時視窗的名子包含了MapleStory導至有一個以上的MapleStory的視窗才會讓程式抓不到。
* 問題二
    * SearchWindow這個程式是使用win32api來抓取MapleStory的畫面，而取得的影像channel不知道到是RGBA還是BGRA所以後來把影像的Alpha值先去除掉只留下RGB，接著嘗試RGB和BGR到底是哪個通道，結果是BGR，那在把影像傳入模型運算前必須先轉換成RGB通道才能正確的偵測，偵測完後必須再將影像轉回BGR因為要使用OpenCV的imshow而opencv的東西都是走BGR如果直接顯示的話色彩會跑掉。
* 問題三
    * 整體結果不太好，雖然該辨識的都有辨識到但不該辨識的也辨識進去了還有重複辨識也是個問題，但我的訓練樣本才40張圖100多個物件圖片算極少樣本吧。


# yolov4 
## 環境
### 硬體設備
* **CPU**:i5-9400F
* **GPU**:GTX 1660

### 軟體環境
|            | 版本   |
| ---------- |-----  |
| Python     | 3.8.5 |
| Tensorflow | 2.4.0 |
| Cuda       |       |
