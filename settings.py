from dotenv import *
import os

load_dotenv()
api_key_valid = os.getenv("api_key_valid")
api_key_invalid = os.getenv("api_key_invalid")