import streamlit as st
import pandas as pd
import datetime as dt
from database import add_visitor,view_all_visitors,get_visitor,edit_visitor,drop_visitor,view_all_flats,view_all_visitors_resident

def flatids():
    result=view_all_flats()
    df=pd.DataFrame(result,columns=["FlatID","no_bhk"])
    list_flatids=[i for i in df['FlatID']]
    return list_flatids

def create_visitor():
    list_flatids=flatids()
    col1,col2=st.columns(2)

    with col1:
        vid=st.text_input("Visitor ID:")
        fid=st.selectbox("Flat ID:",list_flatids)
        fn=st.text_input("First name:")
        ln=st.text_input("Last name:")
        purpose=st.text_input("Purpose:")
    with col2:
        phone=st.text_input("Phone Number:")
        doen=st.date_input("Entry date:",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
        toen=st.time_input("Entry time:")
        doex=st.date_input("Exit date:",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
        toex=st.time_input("Exit time:")

    tsoen= str(doen)+" "+str(toen)
    tsoex= str(doex)+" "+str(toex)

    if st.button("Add visitor"):
        add_visitor(vid, fid, fn, ln, purpose, phone, tsoen, tsoex)
        st.success("Successfully added the visitor")

def show_visitors():
    result=view_all_visitors()
    df=pd.DataFrame(result,columns=["visitorID","flatID","Fname","Lname","purpose","phonenumber","time_of_entry","time_of_exit"],dtype=str)
    st.table(df)

def show_your_visitors(username):
    result=view_all_visitors_resident(username)
    df=pd.DataFrame(result,columns=["visitorID","flatID","Fname","Lname","purpose","phonenumber","time_of_entry","time_of_exit"],dtype=str)
    st.table(df)

def update_visitor():
    result = view_all_visitors()
    df = pd.DataFrame(result, columns=["visitorID", "flatID", "Fname", "Lname", "purpose", "phonenumber", "time_of_entry", "time_of_exit"], dtype=str)
    with st.expander("Current visitors:"):
        st.table(df)

    list_flatids = flatids()
    list_of_visitors = [i for i in df['visitorID']]
    select_visitor = st.selectbox("Select a visitor to edit:", list_of_visitors)
    selected_result = get_visitor(select_visitor)

    if selected_result:
        vid, fid, fn, ln, purpose, phone, stoen, stoex = selected_result[0][:8]

        # Convert datetime objects to strings
        stoen = str(stoen)
        stoex = str(stoex)


        # Splitting date and time components
        stoen_components = stoen.split(" ")
        stoex_components = stoex.split(" ")

        doen = toen = doex = toex = ""

        if len(stoen_components) == 2:
            doen, toen = stoen_components
        if len(stoex_components) == 2:
            doex, toex = stoex_components

        with st.expander("Visitor to edit:"):
            col1, col2 = st.columns(2)
            with col1:
                new_vid = st.text_input("Visitor ID:", vid)
                new_fid = st.selectbox("Flat ID:", list_flatids, index=list_flatids.index(fid))
                new_fn = st.text_input("First name:", fn)
                new_ln = st.text_input("Last name:", ln)
                new_purpose = st.text_input("Purpose:", purpose)
            with col2:
                new_phone = st.text_input("Phone Number:", phone)

                if len(doen.split('-')) == 3 and len(toen.split(':')) == 3:
                    new_doen = st.date_input("Entry date:", value=dt.date(int(doen.split('-')[0]), int(doen.split('-')[1]), int(doen.split('-')[2])), min_value=dt.date(1800, 1, 1), max_value=dt.datetime.today())
                    new_toen = st.time_input("Entry time:", dt.time(int(toen.split(':')[0]), int(toen.split(':')[1]), int(toen.split(':')[2])))

                if len(doex.split('-')) == 3 and len(toex.split(':')) == 3:
                    new_doex = st.date_input("Exit date:", value=dt.date(int(doex.split('-')[0]), int(doex.split('-')[1]), int(doex.split('-')[2])), min_value=dt.date(1800, 1, 1), max_value=dt.datetime.today())
                    new_toex = st.time_input("Exit time:", dt.time(int(toex.split(':')[0]), int(toex.split(':')[1]), int(toex.split(':')[2])))

                new_tsoen = str(new_doen) + " " + str(new_toen) if 'new_doen' in locals() else ""
                new_tsoex = str(new_doex) + " " + str(new_toex) if 'new_doex' in locals() else ""

                if st.button("Update visitor"):
                    edit_visitor(new_vid, new_fid, new_fn, new_ln, new_purpose, new_phone, new_tsoen, new_tsoex, vid)
                    st.success("Successfully updated the visitor")


def delete_visitor():
    result=view_all_visitors()
    df=pd.DataFrame(result,columns=["visitorID","flatID","Fname","Lname","purpose","phonenumber","time_of_entry","time_of_exit"],dtype=str)
    with st.expander("Current visitors:"):
        st.table(df)

    list_of_visitors=[i for i in df['visitorID']]
    selected_visitor=st.selectbox("Visitor to delete:",list_of_visitors)
    st.warning(f"Do you want to delete visitor {selected_visitor}?")
    if st.button("Delete visitor"):
        drop_visitor(selected_visitor)
        st.success("Visitor deleted successfully")