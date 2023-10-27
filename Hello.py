import random
import time
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

    st.title("Bochum Pass")
    st.caption("Proof of Concept")

    # Input fields
    name = st.text_input("Name", "Max Mustermann")
    birthday = st.date_input("Birthday")
    id_number = st.text_input("Case number"), "ABC123456"

    col1, col2, col3 = st.columns(3)
    if col1.button("Submit User Input"):
        sha256_hash = generate_sha256_hash(name, birthday, id_number)
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
