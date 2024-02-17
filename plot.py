import streamlit as st

def main():
    st.title("Login Page")
    username = st.text_input("User")
    password = st.text_input("Pass", type="password")

    
    if st.button("Login"):
        if username == "your_username" and password == "your_password":
            st.success("Login successful!")
            # Add code for the page after successful login
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()

