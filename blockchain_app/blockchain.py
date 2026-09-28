"""
A class to represent a blockchain."""

import hashlib
import json
import uuid
from datetime import datetime
from .transaction import Transaction
from .block import Block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        genesis_transaction = Transaction(
            "SYSTEM",
            "SYSTEM",
            0
        )

        genesis_block = Block(
            index=0,
            transactions=[genesis_transaction],
            previous_hash="0"
        )

        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        for transaction in transactions:
            if not transaction.is_valid():
                raise ValueError("Transaction invalide")

        latest_block = self.get_latest_block()

        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            previous_hash=latest_block.hash
        )

        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Vérification du hash du bloc actuel
            if current_block.hash != current_block.calculate_hash():
                return False

            # Vérification du lien avec le bloc précédent
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        for block in self.chain:
            print("=" * 60)
            print(f"Bloc numéro : {block.index}")
            print(f"Date : {block.timestamp}")
            print(f"Previous Hash : {block.previous_hash}")
            print(f"Hash : {block.hash}")

            print("Transactions :")
            for transaction in block.transactions:
                print(f"  - {transaction}")
