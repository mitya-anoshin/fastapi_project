from fastapi import APIRouter

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache


from redis import asyncio as aioredis

import time

router = APIRouter()


@cache()
async def get_cache():
    return 1


@router.get("/")
@cache(expire=60)
async def index():
    return dict(hello="world")


@router.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

@router.get('/operationsWithData')
@cache(expire=30)
async def getbigdata():
    time.sleep(3)
    return "SUUUUUUUUUUUUUUUUUUUUUUUUUUU"
