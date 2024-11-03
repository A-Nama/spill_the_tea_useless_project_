import streamlit as st
from pages import spill_tea, get_tea

def show_home():
    st.title("☕ Spill the Tea ☕")
    st.markdown("Choose an option below:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Spill the Tea"):
            st.session_state.page = "spill_tea"
    with col2:
        if st.button("Get Some Tea"):
            st.session_state.page = "get_tea"

def main():
    # Initialize session state for page navigation
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Set page configuration
    st.set_page_config(page_title="Spill the Tea", page_icon="☕", layout="centered")

    # Background image style
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://i.imgur.com/EaHsffn.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            height: 100vh;
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Conditional rendering based on page state
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "spill_tea":
        spill_tea.main()
    elif st.session_state.page == "get_tea":
        get_tea.main()

if __name__ == "__main__":
    main()
