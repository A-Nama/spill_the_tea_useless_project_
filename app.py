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
<<<<<<< HEAD
    st.set_page_config(page_title="Spill the Tea", page_icon="☕", layout="centered")

=======
    # Initialize session state for page navigation
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Set page configuration
    st.set_page_config(page_title="Spill the Tea", page_icon="☕", layout="centered")

    # Background image style
>>>>>>> 0d76a77bbe6c40bded660cbead1c0d3a027768c6
    st.markdown(
        """
        <style>
        .main {
            background-image: url('https://i.imgur.com/EaHsffn.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            height: 100vh;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            z-index: -1;
        }
        </style>
        """, unsafe_allow_html=True
    )
<<<<<<< HEAD

    st.title("☕ Spill the Tea ☕")
    st.markdown("Choose an option below:")
    
    if st.button("Spill the Tea"):
        st.session_state.page = "spill_tea"
        st.experimental_rerun()

    if st.button("Get Some Tea"):
        st.session_state.page = "get_tea"
        st.experimental_rerun()

    if 'page' in st.session_state:
        if st.session_state.page == "spill_tea":
            import spill_tea
            spill_tea.main()
        elif st.session_state.page == "get_tea":
            import get_tea
            get_tea.main()
    else:
        st.session_state.page = None
=======

    # Conditional rendering based on page state
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "spill_tea":
        from pages import spill_tea
        spill_tea.main()
    elif st.session_state.page == "get_tea":
        from pages import get_tea
        get_tea.main()
>>>>>>> 0d76a77bbe6c40bded660cbead1c0d3a027768c6

if __name__ == "__main__":
    main()
