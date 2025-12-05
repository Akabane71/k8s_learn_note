from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import user_api, order_api  # 你的路由文件

app = FastAPI(
    title="My Service",
    version="0.1.0"
)

# 1. 挂载路由
app.include_router(user_api.router, prefix="/api/v1", tags=["User"])
app.include_router(order_api.router, prefix="/api/v1", tags=["Order"])

# 2. 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 生产环境要收紧
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. 数据库/文件系统 连接
@app.lifespan("startup")
async def startup_event():
    # 初始化数据库/文件系统 连接
    pass

@app.lifespan("shutdown")
async def shutdown_event():
    # 关闭数据库/文件系统 连接
    pass




