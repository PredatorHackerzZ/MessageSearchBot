# (c) @PredatorHackerzZ

from configs import Config
from database.db import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
