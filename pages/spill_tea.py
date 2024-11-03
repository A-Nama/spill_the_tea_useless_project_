import streamlit as st
from utils.gpt_api_handler import dramatize_text
from utils.db_handler import save_tea_to_db

def main():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/jR03lTH.png");
            background-size: cover;
            background-position: bottom center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100vh;  /* Set height to viewport height */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.write("Share your story anonymously and let the drama begin!")

    story = st.text_area("Enter your story here:", placeholder="Type your tea...")
    tags = st.text_input("Tags (comma-separated)", placeholder="e.g., work, love, friends")
    drama_level = st.slider("Drama Level", min_value=1, max_value=10, value=5)

    if st.button("Teaify!"):
        if story.strip():
            dramatized_story = dramatize_text(story, drama_level)
            # Display the dramatized story before saving it
            st.write(f"**Dramatized Story Preview:**\n{dramatized_story}")
            save_confirmation = st.button("Save this Tea!")

            if save_confirmation:
                save_tea_to_db(dramatized_story, tags.split(",") if tags else [], drama_level)
                st.success("Your tea has been added with extra spice!")
            else:
                st.info("Feel free to make changes to your story or adjust the drama level.")
        else:
            st.error("Please write a story before Teaifying!")

    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()

if __name__ == "__main__":
    main()
