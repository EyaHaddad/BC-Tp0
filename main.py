""" This is the main file for the blockchain project. 
It creates a blockchain, adds transactions to it, 
and displays the blockchain. """

import Transaction
import Blockchain
import Block

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


if __name__ == "__main__":
    main()
