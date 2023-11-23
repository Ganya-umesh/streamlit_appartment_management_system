# streamlit_appartment_management_system
This repository hosts an Apartment Management System built using Streamlit and a relational database management system.

This Streamlit-based application is designed to streamline apartment management tasks using a MySQL backend. It offers distinct access levels—admin, security, and resident—providing tailored functionalities for each user type. This project incorporates database management system (DBMS) features, including triggers and procedures, to enhance functionality.

Getting Started

1)Clone the repository
```git clone https://github.com/Ganya-umesh/streamlit_apartment_management_system.git
```

2)Navigate to the Source Code Directory:
```cd streamlit_apartment_management_system/src
```
3)Install Dependencies:
```pip install -r requirements.txt
```
4)Update Database Configuration:
    --Open database.py.
    --Change the default password to 'user password' to match your MySQL configuration.

5)Run the Application:
```streamlit run main.py
```

6)Login:
  --Access the application using the login credentials found in the 'auth' table.
  --Choose between the roles: admin, security, or resident.
  

