from web3 import Web3
import os

# Define the file path
file_path = "sector_order.txt"

# Open the file in read-only mode
with open(file_path, "r") as file:
    # Read in the entire contents of the file
    file_contents = file.read()

# Compute the Keccak256 hash of the file's contents using the Web3 library
keccak_hash = Web3.keccak(text=file_contents)

# Print out the resulting hash
print("The Keccak256 hash of {} is: {}".format(
    os.path.basename(file_path), keccak_hash.hex()))