"""
A class to represent a transaction in the blockchain.
"""

import hashlib
import json
import uuid
from datetime import datetime
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.now().isoformat()
    
    def is_valid(self):
        return (isinstance(self.sender, str)
            and isinstance(self.receiver, str)
            and self.sender != ""
            and self.receiver != ""
            and isinstance(self.amount, (int, float))
            and self.amount > 0
            )
    def to_dict(self):
        return {
        "id": self.id,
        "sender": self.sender,
        "receiver": self.receiver,
        "amount": self.amount,
        "timestamp": self.timestamp
        }
    def __str__(self):
        return f"{self.sender} -> {self.receiver} : {self.amount}"
