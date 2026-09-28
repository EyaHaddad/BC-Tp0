"""
A class to represent a block in the blockchain."""

import hashlib
import json
import uuid
from datetime import datetime


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = datetime.now().isoformat()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "transactions": [
                transaction.to_dict()
                for transaction in self.transactions
            ],
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash
        }

        data_string = json.dumps(
            block_data,
            sort_keys=True
        ).encode()

        return hashlib.sha256(data_string).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "transactions": [
                transaction.to_dict()
                for transaction in self.transactions
            ],
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)
