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

res = User(credentials=CREDENTIALS, marketplace=Marketplaces.MLA)

# response = res.get_by_id(user_id="829069618")
# response = res.get_logged_user_info()
# response = res.get_addresses(user_id="829069618")
# response = res.get_accepted_payment_methods(user_id="829069618")
response = res.get_brands(user_id="829069618")
print(response)
