import hmac
import hashlib
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class HMACGenerator:
    key: bytes
    message: str
    digestmod: str = 'sha256'

    def generate_hmac(self) -> str:
        try:
            digest = getattr(hashlib, self.digestmod)
            hmac_obj = hmac.new(self.key, self.message.encode(), digest)
            hmac_hex = hmac_obj.hexdigest()
            logging.info(f"Generated HMAC for message '{self.message}' using key '{self.key.decode()}': {hmac_hex}")
            return hmac_hex
        except AttributeError:
            logging.error(f"Unsupported digest mode: {self.digestmod}")
            raise
        except Exception as e:
            logging.error(f"Error generating HMAC: {e}")
            raise 