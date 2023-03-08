import os
import dotenv

from meli.api.sites import Sites
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

res = Sites(credentials=CREDENTIALS, marketplace=Marketplaces.MLA)

# response = res.get_all()
# response = res.get_site_domain_by_id(domain_id="mercadolibre.com.ar")
# response = res.get_site_listing_types(site_id="MLA")
response = res.get_site_listing_prices(site_id="MLA", price=1000)

print(response)
