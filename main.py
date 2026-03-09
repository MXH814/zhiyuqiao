from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义前端传过来的数据格式
class UserQuery(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "智语桥系统后端已启动"}

@app.post("/chat")
def chat_endpoint(query: UserQuery):

    print(f"收到学生问题: {query.text}")
    
  # 1. 检索环节 
    # 从 knowledge.csv 中寻找最相关的 HSK 教学知识点
    context_info = get_relevant_info(query.text)
    
    # 2. 生成环节
    # 将检索到的背景知识拼接到 Prompt 中，发给 DeepSeek 获取专业回答
    # 如果没搜到，generate_response 内部应能处理通用回答
    ai_reply = generate_response(query.text, context=context_info)
    
    # 3. 返回环节
    # 返回真正的 AI 答案给前端，前端再展示给学生
    return {"reply": ai_reply}