import os
import pytest
from datasets import load_dataset
from tw_textforge.data.GSAT.csv import GSAT_DATA
from tw_textforge.config.settings import setting

def test_upload_pass():
    """測試上傳資料集到 Hugging Face Hub"""
    url = next(item["url"] for item in GSAT_DATA if item["name"] == "114_國綜")
    dataset = load_dataset(
        "csv",
        data_files=url,
        download_mode="force_redownload", # 每次都會重新下載 csv 檔案
    )
    assert dataset.push_to_hub("TsukiOwO/TW-GSAT-114-Chinese-General", token=setting.hf_token, private=False)

if __name__ == "__main__":
    pytest.main([__file__])