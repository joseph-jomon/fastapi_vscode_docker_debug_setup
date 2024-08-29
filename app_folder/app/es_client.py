from elasticsearch import Elasticsearch
from app.vdb_config import vdb_settings

class VDBConnection:
    def __init__(self, host: str, timeout: int):
        self.client = Elasticsearch(host, timeout=timeout)

    def ping(self):
        return self.client.ping()