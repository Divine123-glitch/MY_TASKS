import streamlit as st

st.title("BANK APP")

balance = 1000000

# Show options
st.write("### Options:")
options = st.selectbox("Please choose an option:",
    ["Select an option","1. Check Balance",  "2. Buy Data", "3. Transfer Money", "4. Buy Airtime", "5. Exit"])

if options == "1. Check Balance":
    st.write("Checking Balance...")
    st.success(f"Your current balance is: N{balance}")

elif options == "2. Buy Data":
    st.write("Buying Data...")
    data_number = st.text_input("Enter your phone number:", max_chars=15)
    data_amount = st.text_input("Enter the amount of data you want to buy (in MB/GB):", max_chars=5)
    data_network = st.text_input("Enter your network provider (e.g., MTN, GLO, Airtel, 9Mobile):")
    if st.button("Buy Data"):
        st.success(f"You have successfully purchased {data_amount} MB of data for {data_number} on {data_network}")
        st.info("Data purchase successful!")
elif options == "3. Transfer Money":
    st.write("Transfer Money...")
    transfer_number = st.text_input("Enter the recipient's account number:", max_chars=10)
    transfer_name = st.text_input("Enter the recipient's name:")
    if transfer_name and transfer_number:
        st.success(f"Transfer to {transfer_name} ({transfer_number}) initiated.")
        transfer_amount = st.text_input("Enter the amount to transfer:", max_chars=10)
        st.success(f"Transfer of N{transfer_amount} to {transfer_name}, ({transfer_number}) successful!")
        balance = int(balance)
        transfer_amount = int(transfer_amount)
        st.warning(balance - transfer_amount)
elif options == "4. Buy Airtime":
    st.write("Buying Airtime")
    airtime_number = st.text_input("Enter your phone number:", max_chars=15)
    airtime_amount = st.text_input("Enter the amount of airtime you want to buy:", max_chars=10)
    airtime_network = st.text_input("Enter your network provider (e.g., MTN, GLO, Airtel, 9Mobile):")
    if st.button("Buy Airtime"):
        st.success(f"You have successfully purchased N{airtime_amount} airtime for {airtime_number}")
        st.info("Airtime purchase successful!")
        balance = int(balance)
        airtime_amount= int(airtime_amount)
        st.warning({balance - airtime_amount})
elif options == "5. Exit":
    st.write("Exiting the app...")
    st.success("Thank you for using the BANK APP!")

