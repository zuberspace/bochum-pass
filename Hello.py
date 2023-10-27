import random
import time
from datetime import date
import pandas as pd
import streamlit as st
from utils import generate_sha256_hash, check_hash_in_sample

csv_file = "hashes.csv"
df = pd.read_csv(csv_file, header=None, names=['Hash'])
hash_list = df['Hash'].tolist()


def run():
    st.set_page_config(
        page_title="Bochum Pass Proof of Concept",
        page_icon="",
    )

    def update_input(input):
        st.session_state.input = input

    def update_user(name, birthday, case_number):
        st.session_state.name = name
        st.session_state.birthday = birthday
        st.session_state.case_number = case_number

    st.title("Bochum Pass")
    st.caption("Proof of Concept")

    col1_user, col2_user, col3_user = st.columns(3)
    if col1_user.button(":red[Max]"):
        update_user("Max Mustermann", date(1988, 2, 13), "ABC123456")

    if col2_user.button(":green[Maike]"):
        update_user("Maike Musterfrau", date(1964, 5, 26), "123456ABC")


    # Input fields
    name = st.text_input("Name", key='name')
    birthday = st.date_input("Birthday", min_value=date(1900, 1, 1), max_value=date.today(), format="DD/MM/YYYY", key='birthday')
    case_number = st.text_input("Case number", key='case_number')

    col1, col2, col3 = st.columns(3)
    if col1.button("Submit User Input"):
        sha256_hash = generate_sha256_hash(name, birthday, case_number)
        update_input(sha256_hash)

    if col2.button("Select Random Hash"):
        random_hash = random.choice(hash_list)
        update_input(random_hash)

    user_input = st.text_input("Enter a SHA-256 hash:", key='input',)

    if st.button("Check Hash"):
        start_time = time.time()
        if check_hash_in_sample(user_input, hash_list):
            st.success("The hash exists in the list.")
        else:
            st.error("The hash does not exist in the list.")
        end_time = time.time()
        elapsed_time = end_time - start_time
        st.write(f"Elapsed time for the lookup: {elapsed_time:.4f} seconds")

    with st.expander("Hash list"):
        st.write(df['Hash'])


if __name__ == "__main__":
    run()
