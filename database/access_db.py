# (c) @PredatorHackerzZ

from configs import Config
from database.db import Database

db = Database(Config.DATABASE_URL, Config.BOT_SESSION_NAME)
