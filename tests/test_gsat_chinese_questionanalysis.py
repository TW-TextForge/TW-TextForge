import pytest

def test_gsat_chinese_question_analysis():
    from tw_textforge.sdk.GSAT.Chinese import GSAT_Chinese_QuestionAnalysis
    import datasets
    ds = datasets.load_dataset("csv", data_files="data/csv/gsat_chinese_sample.csv", split="train")
    try:
        QuestionAnalysiser = GSAT_Chinese_QuestionAnalysis(dataset=ds, break_time=2, interactive=False, test_mode=True)
        QuestionAnalysiser.run()
        merge_dataset = QuestionAnalysiser.checkpoint_mergeTo_datasets()
        print(merge_dataset[0])
        if (merge_dataset[0]["analysis"] == ""):
            pytest.fail("Analysis column is empty after running the analysis.")
        QuestionAnalysiser.remove_checkpoint()
    except Exception as e:
        pytest.fail(f"GSAT_Chinese_QuestionAnalysis failed with exception: {e}")