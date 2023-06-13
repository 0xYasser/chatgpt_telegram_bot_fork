import yaml
import dotenv
from pathlib import Path
import ast
import os
from dotenv import load_dotenv


config_dir = Path(__file__).parent.parent.resolve() / "config"
load_dotenv(dotenv_path=config_dir / "config.env")

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# config parameters

openai_api_key = os.environ["OPENAI_API_KEY"]
telegram_token = os.environ["TELEGRAM_TOKEN"]
cosmosdb_connection_string = os.environ["COSMOSDB_CONNECTION_STRING"]
cosmosdb_database_id = os.environ["COSMOSDB_DATABASE_ID"]


use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
env_allowed_users = os.environ.get('ALLOWED_TELEGRAM_USERNAMES', '')
allowed_telegram_usernames = (lambda s: s.split(',') if s else [])(os.environ.get('ALLOWED_TELEGRAM_USERNAMES', ''))
new_dialog_timeout = config_yaml.get("new_dialog_timeout", 600)
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)

# chat_modes
with open(config_dir / "chat_modes_en.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
