import streamlit as st
from pages import spill_tea, get_tea

def main():
    st.set_page_config(page_title="Spill the Tea", page_icon="☕", layout="centered")

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

if __name__ == "__main__":
    main()
