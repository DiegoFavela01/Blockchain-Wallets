#Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Import the following functions from the `crypto_wallet.py` file:
from crypto_wallet import generate_account, get_balance, send_transaction




# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0x17e98d28D40881175167f8896a4AB3dA49b47b0C", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x64b1786Cf8989dc19EEE38a68ec855579FAD9Cc6", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x39b74e42aEc66f5Fdca6832eCaaF756A0e547068", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x5A5d693BF2cA6b6F92c21F92c9FfCd9A5E1f057C", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")
st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

balance = get_balance(w3, account.address)
st.sidebar.write(f"Current Balance -  {balance}")

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

wage = hourly_rate*hours


# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

if st.sidebar.button("Send Transaction"):
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people(w3)
