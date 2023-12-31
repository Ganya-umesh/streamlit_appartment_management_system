import streamlit as st
from auth import *
from features import *

def admin_page(username):
    admin_features=["complaints","dependent","employee","flat","flat_has_security","parking slot","resident","resident_avails_services","security","services","visitor"]
    choice = st.sidebar.selectbox("Select Feature", admin_features)
    admin_portion(choice,username)

def resident_page(username):
    resident_features = ["resident_avails_services","employee", "dependent", "visitor", "complaints","flat_has_security"]
    choice = st.sidebar.selectbox("Select Feature", resident_features)
    resident_portion(choice,username)

def security_page(username):
    security_features = ["visitor","staff_list", "resident_list","parking slot"]
    choice = st.sidebar.selectbox("Select Feature", security_features)
    security_portion(choice,username)

if 'user' not in st.session_state:
    st.session_state.login = False
    st.session_state.user = None
    st.session_state.username = ""

def main():
    custom_css = """
    <style>
        /* Change background color */
        .stApp {
            background-color: #00203FFF; /* Dark blue-gray background */
            color: #FFC300; /* Bright yellow text */
            padding: 20px; /* Add some padding for better readability */
            font-size: 18px; /* Larger font size */
        }

        /* Custom styling for headings */
        .stApp h1 {
            color: #ADEFD1FF; /* Coral heading color */
            text-align: center; /* Center align heading */
            margin-bottom: 30px; /* Add space below heading */
        }

        /* Style for Streamlit markdown elements */
        .stApp em {
            color: #2BAE66FF; /* Bright yellow for emphasized text */
            font-style: italic; /* Italic text */
        }

        .stApp strong {
            color: #FF5733; /* Coral for strong text */
            font-weight: bold; /* Bold text */
        }

        .stApp a {
            color: #58D68D; /* Green link color */
            text-decoration: none; /* Remove underline */
        }

        .stApp a:hover {
            text-decoration: underline; /* Add underline on hover */
        }
    </style>
    """


# Inject custom CSS with the `st.markdown()` function
    st.markdown(custom_css, unsafe_allow_html=True)
    username = ""
    password = ""
    login_placeholder = st.empty()

    st.title("User Profile")

    if st.session_state.user is None:
        # User Login
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        login_button = st.button("User Login")

        if login_button:
            user_id = login(username, password)
            if user_id is not None:
                st.session_state.login=True
                st.session_state.user = user_id 
                st.session_state.username = username
                st.success("Logged in successfully")
                print(st.session_state.user)
                # Initialize user_id here             

            else:
                st.error("User not found in the database. Please check your credentials")

    if st.session_state.login:
        if st.session_state.user[0][0]=='sec':
            security_page(st.session_state.username)
        elif st.session_state.user[0][0]=='res':
            resident_page(st.session_state.username)
        elif st.session_state.user[0][0]=='adm':
            admin_page(st.session_state.username)  
          
    
if __name__ == '__main__':
    main()