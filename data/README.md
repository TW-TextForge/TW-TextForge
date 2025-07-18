# 學測試題資料集

## 線上網頁

- [114 學科能力測驗試題](https://docs.google.com/spreadsheets/d/e/2PACX-1vRtnMPEutqfeoQS2BNu2MGvSfM-ti-dNJTIDkd3BxMyAh7E0w-bbIShMgafX805UHSyyexNs_LxU0So/pubhtml)
- [113 學科能力測驗試題](https://docs.google.com/spreadsheets/d/e/2PACX-1vSLkF8eAaSPLn8tfS0gL93lPLJC5DSHeqeNf-B63fmXnqTU-6xuDH4wJqea1mQumvnlJnFtB463ZW5S/pubhtml)

## 資料來源

網站: [大考中心](https://www.ceec.edu.tw/)  
使用: 自由。  
法規: [著作權法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=J0070017) - 第9條 

> 1. 下列各款不得為著作權之標的︰  
一、憲法、法律、命令或公文。  
二、中央或地方機關就前款著作作成之翻譯物或編輯物。  
三、標語及通用之符號、名詞、公式、數表、表格、簿冊或時曆。  
四、單純為傳達事實之新聞報導所作成之語文著作。  
**五、依法令舉行之各類考試試題及其備用試題。** 

## 須知

1. 文字敘述有許多被修改為 Markdown 格式，適合 NLP 訓練
2. 因為試題使用 Word 下底線作為標記，但該功能非電腦標準字符，故無法作為文字輸入。解決方案：使用`___`作為填充標記，`**文字**`代替文字下底線(該字符為 Markdown 格式的粗體)
3. 圖片使用文字代替，故題目敘述會進行修改

## 欄位

- id:
    - 儲存內容: 題號
- question_type:
    - 儲存內容: 題目類型
        - single: 單選題
        - multiple: 多選題
        - filling: 填充題
- article:
    - 儲存內容: 前述文章
- question:
    - 儲存內容: 題目敘述
- A:
    - 儲存內容: 選項A
- B:
    - 儲存內容: 選項B
- C:
    - 儲存內容: 選項C
- D:
    - 儲存內容: 選項D
- E:
    - 儲存內容: 選項E
- answer:
    - 儲存內容: 答案，注意題目類型會有不同的內容形式
- answer_images:
    - 儲存內容: 答案包含圖片的網址
- answer_rate:
    - 儲存內容: 全體考生的回答率，來自大考中心提供的統計資料
- grading_criteria:
    - 儲存內容: 評分標準