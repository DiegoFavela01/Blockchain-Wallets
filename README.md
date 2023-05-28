# Blockchain-Wallets
Challenge 19 - University of Berkeley Financial Technology Boot Camp
## Overview
This project focuses on the implementation of a code that enables individuals to send cryptocurrency payments to fintech professionals. It is designed to work with Ganache, a personal Ethereum blockchain, for testing and development purposes.

## Technology
The code was developed using the following technology stack:
- Python 
- Streamlit
- web3
- bip44
- python-dotenv
## File Changes
Once the application launches, make sure to update the account addresses found in the candidate_database dictionary in the fintech_finder.py file. 
  * Match the addresses with the ones shown in Ganache, excluding the first one.

## Usage
To use the Cryptocurrency Payment System, follow the steps below:

- Launch Ganache, ensuring that it is running properly.
- Copy the MNEMONIC shown at the top of the address list in Ganache.
- In the same folder as the fintech_finder.py and crypto_wallet.py files, create a new .env file.
- Inside the .env file, add the following line:
  - MNEMONIC = <'PASTE COPIED MNEMONIC FROM GANACHE'>
- Launch the Fintech Finder application by running the following command from the command line:
```
streamlit run fintech_finder.py
```
- Select a candidate from the drop-down list in the sidebar.
- Enter the number of hours you want to hire the selected individual for. Please note that there is a limited amount of ether in each account, so keep the value relatively low to ensure you have enough ETH to cover the cost.
- Click the 'Send Transaction' button.
- After submitting the transaction, the sidebar will update with a copy of the transaction hash.
- Ganache, you can verify the following:
  - A new transaction should appear under the 'Transactions' tab, matching your submission.
  - Your account balance (the first listed) should reflect the reduction in funds.
  - The account balance for the selected fintech professional should reflect an increase.
#### *Please ensure that you have a basic understanding of Ethereum, Ganache, and the related technologies before proceeding with the usage of this code.*

