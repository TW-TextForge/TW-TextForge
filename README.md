# 台灣-學科能力測驗試題資料集

## 使用須知
根據[著作權法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=J0070017) - 第 9 條  
依法令舉行之各類考試試題及其備用試題，是不具備著作權的，可自由使用  
但該專安有調整敘述，**即重製**，讓資料更適合深度學習  
請勿必根據專案、資料集許可證使用專案程式碼與資料集

## 快速啟用
```bash
uv venv
uv sync
```

## [範本](./samples/)

### [1. 資料集載入(CSV)與上傳(Huggice Face Hub)](./samples/Dataset_Load_And_Upload.ipynb)
載入 CSV 和上傳到雲端中心儲存  
並且可以用 remote 的方式降低硬體需求

### [2. 使用 LLM 生成學測題目的題目解析](./samples/Agent_Generate_Analysis.ipynb)
生成題目解析作為訓練資料之一，讓 NLP 相關訓練效果更好

### [3. 修改系統路徑以便即時導入模組](./samples/Modules_Hot_Update.ipynb)
以模組熱導入的方式使用套件，讓開發更容易