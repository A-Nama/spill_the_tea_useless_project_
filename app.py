import streamlit as st
from pages import spill_tea
from pages import get_tea

def main():
    st.set_page_config(page_title="Spill the Tea", page_icon="☕", layout="centered")

    # Background image style
    st.markdown(
        """
        <style>
        .main { background-image: url('https://i.imgur.com/EaHsffn.jpeg');
                background-size: cover; }
        </style>
        """, unsafe_allow_html=True
    )

    st.title("☕ Spill the Tea ☕")
    st.markdown("Choose an option below:")
    
    if st.button("Spill the Tea"):
        st.session_state.page = "spill_tea"  # Save the page in session state
        st.rerun()  # Rerun to update the view

    if st.button("Get Some Tea"):
        st.session_state.page = "get_tea"  # Save the page in session state
        st.rerun()  # Rerun to update the view

    # Display the corresponding page
    if 'page' in st.session_state:
        if st.session_state.page == "spill_tea":
            import spill_tea  # Import the spill tea page
            spill_tea.main()
        elif st.session_state.page == "get_tea":
            import get_tea  # Import the get tea page
            get_tea.main()
    else:
        st.session_state.page = None  # Reset page if it doesn't exist

if __name__ == "__main__":
    main()
