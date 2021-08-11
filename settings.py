from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# use 'sandbox' for development in the test environment
USERNAME = os.getenv("USER_NAME")

# use your sandbox app API key for development in the test environment
API_KEY = os.getenv("API_KEY")
