from fastapi import FastAPI
from .services.channels import all_channels
from .services.category import category_channels
from .services.categories import all_categories
from .services.now import now
from .services.info import channel
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="TVInfoAPI",
    description="API для работы с сайтом tvinfo.uz",
    version="1.0.0",
    contact={
        "name": "ulugbekov",
        "url": "https://dev.ulugbekov.uz",
        "email": "dev@ulugbekov.uz",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/ulugbekovv/TVInfoAPI/blob/main/LICENSE",
    },
)

class ChannelRequest(BaseModel):
    channel_url: str

class ChannelRequest2(BaseModel):
    channel_url: str
    date: str

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/channels", summary="Получить список всех каналов", description="Возвращает список всех доступных каналов")
async def channels_root():
    channels = all_channels()
    return {"channels": channels}

@app.get("/categories", summary="Получить список всех категорий", description="Возвращает список всех доступных категорий")
async def categories_root():
    categories = all_categories()
    return {"categories": categories}

@app.get("/category/{category}", summary="Получить список каналов в заданной категории", description="Возвращает список каналов в этой категории")
async def category_root(category: str):
    channels = category_channels(category)
    return {"channels": channels}

@app.post("/now", summary="Получить текущую программу в заданном канале", description="Возвращает программу в текущее время")
async def now_root(request: ChannelRequest):
    current_status = now(request.channel_url)
    return {"now": current_status}


@app.post('/channel', summary="Получить программу на весь день для заданной даты", description="Возвращает программу заданной даты")
async def channel_root(request: ChannelRequest2):
    info = channel(request.channel_url, request.date)
    return {"info": info}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
