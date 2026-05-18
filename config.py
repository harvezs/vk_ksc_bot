import configparser
import os
import sys

def get_base_dir():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

BASE_DIR = get_base_dir()
CONFIG_PATH = os.path.join(BASE_DIR, "config.cfg")

if not os.path.isfile(CONFIG_PATH):
    raise FileNotFoundError(
        f"Файл конфигурации не найден: {CONFIG_PATH}\n"
        "Создайте config.cfg рядом с программой."
    )

config = configparser.ConfigParser()
config.read(CONFIG_PATH, encoding="utf-8")

VK_ACCESS_TOKEN = config.get("VK", "ACCESS_TOKEN")
VK_API_VERSION = config.get("VK", "API_VERSION", fallback="5.199")

HTTP_HOST = config.get("HTTP", "HOST", fallback="127.0.0.1")
HTTP_PORT = config.getint("HTTP", "PORT", fallback=12345)

DEFAULT_USERS = {
    int(uid.strip())
    for uid in config.get("USERS", "DEFAULT_USERS", fallback="").split(",")
    if uid.strip().isdigit()
}

MAX_MESSAGE_LENGTH = config.getint("MESSAGES", "MAX_MESSAGE_LENGTH", fallback=4000)