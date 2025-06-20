from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# 初始化FastAPI应用
app = FastAPI(title="大模型工具调用后端")

# 配置CORS，允许前端跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议指定具体前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义请求数据模型
class ModelRequest(BaseModel):
    prompt: str
    model: Optional[str] = "default-model"
    temperature: Optional[float] = 0.7

# 大模型调用逻辑 - 预留接口
def call_large_model(prompt: str, model: str, temperature: float) -> str:
    """
    用户需在此处实现大模型调用逻辑
    参数:
        prompt: 用户输入的提示文本
        model: 模型名称
        temperature: 生成温度参数
    返回:
        模型生成的响应文本
    """
    # ===== 预留大模型调用位置 =====
    # 示例：返回模拟响应
    return f"[模拟响应] 已接收请求: {prompt}\n(模型: {model}, 温度: {temperature})"
    # ============================

# API端点：处理模型调用请求
@app.post("/api/call-model")
async def handle_model_call(request: ModelRequest):
    try:
        # 调用大模型逻辑
        response = call_large_model(
            prompt=request.prompt,
            model=request.model,
            temperature=request.temperature
        )
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"模型调用失败: {str(e)}")

# 健康检查端点
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "后端服务运行正常"}

# 主程序入口
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)