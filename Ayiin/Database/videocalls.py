from typing import Dict, List, Union

from Ayiin import db

videodb = db.Ayiinvideocalls


## limit


async def get_video_limit(chat_id: int) -> str:
    limit = await videodb.find_one({"chat_id": chat_id})
    return "" if not limit else limit["limit"]


async def set_video_limit(chat_id: int, limit: str):
    return await videodb.update_one(
        {"chat_id": chat_id}, {"$set": {"limit": limit}}, upsert=True
    )


## Queue Chats Video


async def get_active_video_chats() -> list:
    chats = videodb.find({"chat_id": {"$lt": 0}})
    return [] if not chats else list(await chats.to_list(length=1000000000))


async def is_active_video_chat(chat_id: int) -> bool:
    chat = await videodb.find_one({"chat_id": chat_id})
    return bool(chat)


async def add_active_video_chat(chat_id: int):
    is_served = await is_active_video_chat(chat_id)
    if is_served:
        return
    return await videodb.insert_one({"chat_id": chat_id})


async def remove_active_video_chat(chat_id: int):
    is_served = await is_active_video_chat(chat_id)
    if not is_served:
        return
    return await videodb.delete_one({"chat_id": chat_id})
