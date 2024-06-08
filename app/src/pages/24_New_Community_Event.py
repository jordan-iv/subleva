import streamlit as st
import requests
import datetime
import requests
from streamlit_extras.app_logo import add_logo
import logging 
from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Event Manager", page_icon="🙏")

add_logo("assets/logo.png", height=400)

SideBarLinks()

st.header("New Community Event", divider='green')

# Creates an Event
st.write("**Create an Event**")
event_name = st.text_input("Event Name")
event_id = st.number_input("Event ID", value=0, step=1)
date = st.date_input("Event Date", value=datetime.date.today())
duration = st.number_input("Duration",value=0, step=1, placeholder="Type a value...")
venue_capacity = st.number_input("Venue Capcity",value=0, step=1, placeholder="Type a value...")

if st.button("Submit"):
    if event_name and date and duration and venue_capacity:
        post_data = {
            "eventName" : event_name,
            "eventID" : event_id,
            "date" : str(date),
            "duration" : duration,
            "venueCapacity" : venue_capacity
        }
        response = requests.post("http://api:4000/c/council_add_event", json=post_data)