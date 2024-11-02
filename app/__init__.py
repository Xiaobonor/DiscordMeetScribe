# app/discord/__init__.py
import logging
import sys
import dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def create_app():
    dotenv.load_dotenv()

    return