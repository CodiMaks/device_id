import streamlit as st
import platform


if 'label' not in st.session_state:
    st.session_state['label'] = ""

if 'label2' not in st.session_state:
    st.session_state['label2'] = ""

if 'label3' not in st.session_state:
    st.session_state['label3'] = ""

if 'label4' not in st.session_state:
    st.session_state['label4'] = ""

st.subheader(st.session_state['label'])
st.subheader(st.session_state['label2'])
st.subheader(st.session_state['label3'])
st.subheader(st.session_state['label4'])

show_id = st.button("SHOW", type="primary", use_container_width=True)

if show_id:
    st.session_state['label'] = f"{platform.node()}"
    st.session_state['label2'] = f"{platform.platform()}"
    st.session_state['label3'] = f"{platform.processor()}"
    st.session_state['label4'] = f"{platform.version()}"
    st.rerun()
