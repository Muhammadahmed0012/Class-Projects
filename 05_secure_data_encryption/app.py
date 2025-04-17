import streamlit as st
from cryptography.fernet import Fernet

# Function to generate key from password
def generate_key(password: str) -> bytes:
    return Fernet(Fernet.generate_key())  # This creates a new key each time

# Function to encrypt the message
def encrypt_data(data: str, key: bytes) -> str:
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data.decode()

# Function to decrypt the message
def decrypt_data(encrypted_data: str, key: bytes) -> str:
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

# Streamlit UI setup
st.title("🔒 Secure Data Encryption")
st.write("Encrypt and decrypt your sensitive data securely.")

# Get password from user to generate key
password = st.text_input("Enter a password to generate a key", type="password")

# Generate key based on password
if password:
    key = generate_key(password)
    st.write("Key generated based on your password.")

    # Select between Encrypt or Decrypt
    option = st.radio("Select an option:", ["Encrypt Data", "Decrypt Data"])

    if option == "Encrypt Data":
        data_to_encrypt = st.text_area("Enter data to encrypt")
        if data_to_encrypt:
            encrypted = encrypt_data(data_to_encrypt, key)
            st.success(f"Encrypted Data: {encrypted}")

    elif option == "Decrypt Data":
        data_to_decrypt = st.text_area("Enter data to decrypt")
        if data_to_decrypt:
            try:
                decrypted = decrypt_data(data_to_decrypt, key)
                st.success(f"Decrypted Data: {decrypted}")
            except Exception as e:
                st.error("Invalid data or key for decryption.")

