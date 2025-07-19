from tw_textforge.agent.general.single_agent_graph import GeneralSingleAgentGraph
from tw_textforge.prompt.GSAT.chinese import gast_chinese_question_analysis_generator_prompt

class GSATChineseGraph_QuestionAnalysis(GeneralSingleAgentGraph):
    """
    為學測中文綜合設計的單代理流程圖
    """
    PROMPT = gast_chinese_question_analysis_generator_prompt