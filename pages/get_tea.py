import streamlit as st
from utils.db_handler import get_tea_from_db

def main():
    st.title("Get Some Tea ☕")
    st.write("Browse the latest drama-filled stories!")

    # Categorization of stories
    categories = ["work", "love", "friends", "family", "other"]
    selected_category = st.selectbox("Choose a category to browse:", categories)

    search_query = st.text_input("Search by tags", placeholder="e.g., work, love")
    stories = get_tea_from_db(search_query or selected_category)  # Default to category if no search

    if stories:
        for story in stories:
            st.markdown(f"**Story**: {story['text']}")
            st.markdown(f"*Tags*: {', '.join(story['tags'])}")
            st.markdown("---")
    else:
        st.write("No stories found for the specified tags.")

if __name__ == "__main__":
    main()
