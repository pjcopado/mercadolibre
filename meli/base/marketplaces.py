import logging
from enum import Enum

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


class AuthorizationError(Exception):
    def __init__(self, code, message=".env problem set your file in the root project"):
        logging.warning(message)


class ENV(Enum):
    PRODUCTION = "PRODUCTION"
    SANDBOX = "SANDBOX"


class CurrencySymbols(Enum):
    USD = "$"
    MXN = "$"
    BRL = "R$"
    ARS = "$"
    VES = "$"
    GTQ = "$"
    BOB = "$"
    PEN = "$"
    PYG = "$"
    DOP = "$"
    COP = "$"
    HNL = "$"
    CUP = "$"
    CLP = "$"
    CRC = "$"
    PAB = "$"
    NIO = "$"
    UYU = "$"


class Currencies(Enum):
    VES = "VES"
    GTQ = "GTQ"
    BOB = "BOB"
    USD = "USD"
    PEN = "PEN"
    PYG = "PYG"
    DOP = "DOP"
    MXN = "MXN"
    COP = "COP"
    HNL = "HNL"
    CUP = "CUP"
    CLP = "CLP"
    BRL = "BRL"
    ARS = "ARS"
    CRC = "CRC"
    PAB = "PAB"
    NIO = "NIO"
    UYU = "UYU"


class MarketplacesIds(Enum):
    MLV = "MLV"
    MGT = "MGT"
    MBO = "MBO"
    MEC = "MEC"
    MPE = "MPE"
    MPY = "MPY"
    MRD = "MRD"
    MLM = "MLM"
    MCO = "MCO"
    MHN = "MHN"
    MCU = "MCU"
    MLC = "MLC"
    MSV = "MSV"
    MLB = "MLB"
    MLA = "MLA"
    MCR = "MCR"
    MPA = "MPA"
    MNI = "MNI"
    MLU = "MLU"


class Marketplaces(Enum):

    MLA = {
        "auth_url": "https://auth.mercadolibre.com.ar",  # Argentina
        "currency": Currencies.ARS,
    }

    MLB = {
        "auth_url": "https://auth.mercadolibre.com.br",  # Brasil
        "currency": Currencies.BRL,
    }

    MCO = {
        "auth_url": "https://auth.mercadolibre.com.co",  # Colombia
        "currency": Currencies.COP,
    }

    MCR = {
        "auth_url": "https://auth.mercadolibre.com.cr",  # Costa Rica
        "currency": Currencies.CRC,
    }

    MEC = {
        "auth_url": "https://auth.mercadolibre.com.ec",  # Ecuador
        "currency": Currencies.USD,
    }

    MLC = {
        "auth_url": "https://auth.mercadolibre.cl",  # Chile
        "currency": Currencies.CLP,
    }

    MLM = {
        "auth_url": "https://auth.mercadolibre.com.mx",  # Mexico
        "currency": Currencies.MXN,
    }

    MLU = {
        "auth_url": "https://auth.mercadolibre.com.uy",  # Uruguay
        "currency": Currencies.UYU,
    }

    MLV = {
        "auth_url": "https://auth.mercadolibre.com.ve",  # Venezuela
        "currency": Currencies.VES,
    }

    MPA = {
        "auth_url": "https://auth.mercadolibre.com.pa",  # Panama
        "currency": Currencies.PAB,
    }

    MPE = {
        "auth_url": "https://auth.mercadolibre.com.pe",  # Peru
        "currency": Currencies.PEN,
    }

    MRD = {
        "auth_url": "https://auth.mercadolibre.com.do",  # Dominicana
        "currency": Currencies.DOP,
    }

    # MNI = {"auth_url": "", "currency": Currencies.NIO}  # Nicaragua

    # MGT = {"auth_url": "", "currency": Currencies.GTQ}  # Guatemala

    # MBO = {"auth_url": "", "currency": Currencies.BOB}  # Bolivia

    # MPY = {"auth_url": "", "currency": Currencies.PYG}  # Paraguay

    # MSV = {"auth_url": "", "currency": Currencies.USD}  # El Salvador

    # MHN = {"auth_url": "", "currency": Currencies.HNL}  # Honduras

    # MCU = {"auth_url": "", "currency": Currencies.CUP}  # Cuba

    def __init__(self, info):
        self.token_url = "https://api.mercadolibre.com/oauth/token"
        self.endpoint = "https://api.mercadolibre.com"
        self.auth_url = info.get("auth_url")
        self.currency = info.get("currency")
