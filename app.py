# app.py

import os
from dotenv import load_dotenv
load_dotenv()  # This loads the .env file


import streamlit as st
from email_utils import gmail_authenticate, get_latest_email, send_reply
from reply_generator import generate_reply

st.set_page_config(page_title="Email Reply Assistant", layout="centered")

st.title("📧 Email Reply Assistant")

if "service" not in st.session_state:
    st.session_state.service = gmail_authenticate()

if st.button("📥 Fetch Latest Email"):
    sender, text = get_latest_email(st.session_state.service)
    if sender:
        st.session_state.email_text = text
        st.session_state.sender = sender
        st.success(f"Fetched email from: {sender}")
    else:
        st.warning("No unread emails found.")

if "email_text" in st.session_state:
    st.subheader("📨 Incoming Email")
    st.text_area("Email Content", st.session_state.email_text, height=200)

    st.subheader("🎨 Choose Reply Tone")
    tone = st.selectbox("Select Tone", ["formal", "casual", "friendly", "apologetic"])

    if st.button("🤖 Generate Reply"):
        with st.spinner("Generating..."):
            reply = generate_reply(st.session_state.email_text, tone)
            st.session_state.generated_reply = reply
        st.success("Reply generated!")

if "generated_reply" in st.session_state:
    st.subheader("✍️ Generated Reply")
    reply_text = st.text_area("Edit Reply", st.session_state.generated_reply, height=200)

    if st.button("📤 Send Reply"):
        send_reply(st.session_state.service, st.session_state.sender, reply_text)
        st.success("Reply sent!")
