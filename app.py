import streamlit as st
from pages import spill_tea, get_tea

def show_home():

    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            margin: 40px 0;
            padding-top: 50px;  
        }
        </style>
    """, unsafe_allow_html=True)

    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, spacer, col2 = st.columns([1, 4, 1])

    with col1:
        if st.button("Spill the Tea"):
            st.session_state.page = "spill_tea"

    with col2:
        if st.button("Get Some Tea"):
            st.session_state.page = "get_tea"

    st.markdown('</div>', unsafe_allow_html=True)

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
            background-image: url("https://i.imgur.com/VWYfvtY.jpeg");
            background-size: contain;
            background-position: bottom center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
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
