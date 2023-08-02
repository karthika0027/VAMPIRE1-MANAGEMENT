class Config(object):
    LOGGER = True

    API_ID = 17713634
    API_HASH = "a8c943a69022fef3ac66accc7ba8ce6b"
    TOKEN = "5625036376:AAHJS3Tkf13qV8oz10vbYf-ePQY92NH5fj8"
    OWNER_ID = 5477924487
    OWNER_USERNAME = "hackerofrip"
    SUPPORT_CHAT = "Team_Vampir"
    JOIN_LOGGER = ("-1001770039008")
    EVENT_LOGS = ("-1001770039008")
    MUST_JOIN = "Team_Vampir"

    SQLALCHEMY_DATABASE_URI = "postgres://logi_ifgz_user:Llhuylk1TRi0vnqjOVT16icrhlRrBQBL@dpg-cdpo6n1gp3jr9p5e11i0-a.singapore-postgres.render.com/logi_ifgz"
    MONGO_DB_URI = "mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1955509952"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1955509952"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1955509952"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1955509952"
    WOLVES = "1955509952"

    DONATION_LINK = "https://t.me/hackerofrip"
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://te.legra.ph/file/087777b019b111a9f2bb7.jpg"
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
