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


## 問題



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
