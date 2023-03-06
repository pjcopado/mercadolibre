import os
import dotenv

from meli.api.user import User
from meli.base.marketplaces import Marketplaces

dotenv.load_dotenv()

CLIENT_ID = os.environ.get("MELI_CLIENT_ID")
CLIENT_SECRET = os.environ.get("MELI_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("MELI_REFRESH_TOKEN")


CREDENTIALS = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "refresh_token": REFRESH_TOKEN,
}

print(CREDENTIALS)

res = User(credentials=CREDENTIALS, marketplace=Marketplaces.MLA)
print(res)

user = res.get_user_by_id(user_id="829069618")
print(user)
