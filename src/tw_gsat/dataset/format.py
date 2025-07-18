def gen_text_pre_format(example):
    """
    產生純存字的預處理格式，可用於 NLP 模型的輸入，可行用途包括：
    - N-Shot
    - 產生合成資料
    - 產生額外的資訊...etc.
    
    使用方式：
    ```python
    dataset = dataset.map(gen_text_pre_format)
    ```
    """

    parts = []
    def add(label, content):
        parts.append(label)
        parts.append(str(content) if content is not None else "")
    if example.get("article_title"):
        add("前述文章:", example.get("article"))
    add("題目敘述:", example.get("question"))

    opts = []
    for opt in ("A","B","C","D","E"):
        val = example.get(opt)
        if val:
            opts.append(f"({opt}){val}")
    if opts:
        parts.append("題目選項:")
        parts.extend(opts)

    add("答案:", example.get("answer"))
    
    if example.get("grading_criteria"):
        add("評分標準", example.get("grading_criteria"))

    text = "\n".join(parts)
    return {"text_pre_format": text}