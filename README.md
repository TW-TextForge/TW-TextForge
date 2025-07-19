# 台灣-學科能力測驗試題資料集

## 使用須知
根據台灣的[著作權法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=J0070017) - 第9條 

> 1. 下列各款不得為著作權之標的︰  
一、憲法、法律、命令或公文。  
二、中央或地方機關就前款著作作成之翻譯物或編輯物。  
三、標語及通用之符號、名詞、公式、數表、表格、簿冊或時曆。  
四、單純為傳達事實之新聞報導所作成之語文著作。  
**五、依法令舉行之各類考試試題及其備用試題。**

學測試題之類的考試試題，是不具備著作權的，可自由使用  
該專案有調整題目敘述，**即重製題目**，讓資料更適合 NLP  
請務必根據**Apache 2.0許可證**使用專案程式碼與資料集

## 快速安裝 - [uv 套件管理工具](https://docs.astral.sh/uv/getting-started/installation/)

### 開發階段

```bash
uv venv
uv pip install -e .[dev]
```

### 生產階段

```bash
uv venv
uv sync
```

## [範本](./samples/)

### [1. 資料集載入(CSV)與上傳(Huggice Face Hub)](./samples/Dataset_Load_And_Upload.ipynb)

載入 CSV 和上傳到雲端中心儲存  
並且可以用 remote 的方式降低硬體需求

### [2. 使用 LLM 生成學測題目的題目解析(開發中)](./samples/Agent_Generate_Analysis.ipynb)

生成題目解析作為訓練資料之一，讓 NLP 相關訓練效果更好

### [3. 修改系統路徑以便即時導入模組，適合於自行調整專案程式碼](./samples/Modules_Hot_Update.ipynb)

以模組熱導入的方式使用套件，讓開發更容易