import pytest


def test_pdf_extractor():
    """測試 PDF 提取功能"""
    from tw_textforge.utils import extract_pdf_all_text, extract_pdf_pages

    # 測試讀取整個 PDF 的文字內容
    pdf_text = extract_pdf_all_text('data/public-domain/turing.pdf')
    assert isinstance(pdf_text, str)
    assert len(pdf_text) > 0  # 確保讀取到的內容不為空

    # 測試讀取 PDF 每一頁的文字內容
    pages = extract_pdf_pages('data/public-domain/turing.pdf')
    assert isinstance(pages, list)
    assert len(pages) > 0  # 確保至少有一頁內容
    for page in pages:
        assert isinstance(page, str)  # 每一頁應該是字符串


if __name__ == "__main__":
    pytest.main([__file__])