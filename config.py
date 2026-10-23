from dotenv import load_dotenv
import os

load_dotenv()

ORIGEM = os.getenv("ORIGEM")
DESTINO = os.getenv("DESTINO")