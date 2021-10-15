import os
import threading
import datetime
import motor.motor_asyncio

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


def start() -> scoped_session:
    engine = create_engine(Config.DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()

class Thumbnail(BASE):
    __tablename__ = "thumbnail"
    id = Column(Integer, primary_key=True)
    msg_id = Column(Integer)
    
    def __init__(self, id, msg_id):
        self.id = id
        self.msg_id = msg_id

Thumbnail.__table__.create(checkfirst=True)

async def df_thumb(id, msg_id):
    with INSERTION_LOCK:
        msg = SESSION.query(Thumbnail).get(id)
        if not msg:
            msg = Thumbnail(id, msg_id)
            SESSION.add(msg)
            SESSION.flush()
        else:
            SESSION.delete(msg)
            file = Thumbnail(id, msg_id)
            SESSION.add(file)
        SESSION.commit()

async def del_thumb(id):
    with INSERTION_LOCK:
        msg = SESSION.query(Thumbnail).get(id)
        SESSION.delete(msg)
        SESSION.commit()

async def thumb(id):
    try:
        t = SESSION.query(Thumbnail).get(id)
        return t
    finally:
        SESSION.close()

class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            prefix=None,
            upload_as_doc=True,
            thumbnail=None,
            caption=None
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_prefix(self, id, prefix):
        await self.col.update_one({'id': id}, {'$set': {'prefix': prefix}})

    async def get_prefix(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('prefix', None)

    async def set_upload_as_doc(self, id, upload_as_doc):
        await self.col.update_one({'id': id}, {'$set': {'upload_as_doc': upload_as_doc}})

    async def get_upload_as_doc(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('upload_as_doc', False)

    async def set_thumbnail(self, id, thumbnail):
        await self.col.update_one({'id': id}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('thumbnail', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'id': id}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('caption', None)
