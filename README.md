# streamlit_appartment_management_system

This repository hosts an Apartment Management System built using Streamlit and a relational database management system.

This Streamlit-based application is designed to streamline apartment management tasks using a MySQL backend. It offers distinct access levels: admin, security, and resident—providing tailored functionalities for each user type. This project incorporates database management system (DBMS) features, including triggers and procedures, to enhance functionality.

## Getting Started

1. **Clone the repository**
    ```bash
    git clone https://github.com/Ganya-umesh/streamlit_apartment_management_system.git
    ```

2. **Navigate to the Source Code Directory:**
    ```bash
    cd streamlit_apartment_management_system/src
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Update Database Configuration:**
    - Open `database.py`.
    - Change the default password to 'user password' to match your MySQL configuration.

5. **Run the Application:**
    ```bash
    streamlit run main.py
    ```

6. **Login:**
    - Access the application using the login credentials found in the 'auth' table.
    - Choose between the roles: admin, security, or resident.


<img width="956" alt="Screenshot 2023-11-23 180129" src="https://github.com/Ganya-umesh/streamlit_appartment_management_system/assets/118112049/27e2195b-bdae-4b6f-85c0-774d1f6423bf">

<img width="960" alt="Screenshot 2023-11-23 182001" src="https://github.com/Ganya-umesh/streamlit_appartment_management_system/assets/118112049/9c783d57-b6e5-461e-a532-c021400b6593">

<img width="959" alt="Screenshot 2023-11-23 182051" src="https://github.com/Ganya-umesh/streamlit_appartment_management_system/assets/118112049/d9b1fbe5-e1d3-4c86-b051-3051ac89a6ad">
