from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB_PATH = os.environ.get("POSTGRES_DB_PATH")

SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

SMTP_USER = os.environ.get("SMTP_USER")