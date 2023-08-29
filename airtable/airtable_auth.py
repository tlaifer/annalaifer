import configparser
import os

fp = os.path.join(os.path.dirname(__file__), '', 'auth_config.ini')
assert os.path.exists(fp)

class AirtableAuth:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(fp)
    
    def token(self):
        return self.config.get("airtable", "token")