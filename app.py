import gradio as gr
from core.ai_agent import generate_response

def chat_interface(message, history):
    # 调用封装好的逻辑
    return generate_response(message)

demo = gr.ChatInterface(
    fn=chat_interface, 
    title="智语桥 - 国际中文教育 AI 助手",
    description="欢迎使用！我是你的中文教育小助手。"
)

if __name__ == "__main__":
    demo.launch(share=True)