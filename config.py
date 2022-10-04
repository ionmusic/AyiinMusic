from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5425879491:AAH6aNFn326MjsZnyjN_ilQOhMJilhdHcqs")
API_ID = int(getenv("API_ID", "16510278"))
API_HASH = getenv("API_HASH", "15e66907e1d030b9f203859fc4c54845")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "300"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ion:ion@cluster0.m5ylj7l.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5063062493").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1008552110").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001667736274"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "KAZU MUSUC")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/AyiinXd/MultiAssistant"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1", "BQAkQkYgZ-9NDGikteLrMShCnet53fqUP1SOkCAgV1qjCr8slr3vfL7_MGSZq92le7-aXTSHiMnupk3XSdS1k--K5pL10gX0MT5FdhHgUYQysZh-ZEsv-_lzSoeoSwSJRQeWnngFinqF00v6BgqZIOS7JaRq1eQrefz9S4w1BU15xl68PaW5ZddIIDzU6EgR8J_Ca0ZfqQiwbZmrolb-V9i89vY4jLuXKjdoh7VeMg4EXmCqnUjc0CrCfiRxhKRevsLiptMwqAIgWw_XrWshZkXGxNiiN6vXtpGxmGM_hxz9iE6j2wnM6o72ZDh6t2c_2VH7XjtaQs0NpgoI0a-C-wQ3PB1IrgA"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION", "BQAkQkYgZ-9NDGikteLrMShCnet53fqUP1SOkCAgV1qjCr8slr3vfL7_MGSZq92le7-aXTSHiMnupk3XSdS1k--K5pL10gX0MT5FdhHgUYQysZh-ZEsv-_lzSoeoSwSJRQeWnngFinqF00v6BgqZIOS7JaRq1eQrefz9S4w1BU15xl68PaW5ZddIIDzU6EgR8J_Ca0ZfqQiwbZmrolb-V9i89vY4jLuXKjdoh7VeMg4EXmCqnUjc0CrCfiRxhKRevsLiptMwqAIgWw_XrWshZkXGxNiiN6vXtpGxmGM_hxz9iE6j2wnM6o72ZDh6t2c_2VH7XjtaQs0NpgoI0a-C-wQ3PB1IrgA"))
