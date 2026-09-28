""" This is the main file for the blockchain project. 
It creates a blockchain, adds transactions to it, 
and displays the blockchain. """

from .blockchain import Blockchain
from .transaction import Transaction


def main():
    print("Hello from tp0!")
    
    # Création de la Blockchain
    blockchain = Blockchain()

    # Scénario demandé
    transaction1 = Transaction("Alice", "Bob", 50)
    transaction2 = Transaction("Bob", "Alice", 20)
    transaction3 = Transaction("Alice", "Bob", 10)

    # Ajout des transactions dans un bloc
    blockchain.add_block([
        transaction1,
        transaction2,
        transaction3
    ])

    # Affichage de la Blockchain
    print("Blockchain initiale :")
    blockchain.display_chain()

    print("\nLa Blockchain est-elle valide ?")
    print(blockchain.is_valid())

    # modification of a transaction to test the validity of the blockchain
    print("\nModification de la transaction...")

    ancien_hash = blockchain.chain[1].hash

    # Modification frauduleuse
    blockchain.chain[1].transactions[0].amount = 500

    nouveau_hash_calcule = blockchain.chain[1].calculate_hash()

    print("Ancien hash :", ancien_hash)
    print("Nouveau hash calculé :", nouveau_hash_calcule)

    print("\nLa Blockchain est-elle valide après modification ?")
    print(blockchain.is_valid())

if __name__ == "__main__":
    main()
