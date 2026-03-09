import pandas as pd

def get_relevant_info(query_text):
    try:
        # 读取表格数据
        df = pd.read_csv("knowledge.csv")
        
        # 搜索逻辑：查看问题列是否包含用户输入的关键词
        # 后续把这里升级为向量检索
        results = df[df['Question'].str.contains(query_text, na=False, case=False)]
        
        if not results.empty:
            # 返回最匹配的一条答案
            return results.iloc[0]['Answer']
        return "未在手册中找到直接对应规定。"
    except Exception as e:
        return f"知识库读取失败: {str(e)}"