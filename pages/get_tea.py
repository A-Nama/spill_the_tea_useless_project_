import streamlit as st
from utils.db_handler import get_tea_from_db

def main():
    # Background image style
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.imgur.com/fxjOaib.png");
        background-size: cover;
        background-position: 70px 40px;
        background-repeat: no-repeat;
        background-attachment: fixed;
        margin-top: 50px; /* Adjusted padding */
    }
    .category-column {
        margin-bottom: 20px; /* Space between rows */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Define the tea categories and corresponding images
    tea_categories = {
        "Work": "https://i.imgur.com/0ozazoc.png",
        "University": "https://i.imgur.com/ZToGmJI.png",
        "Love": "https://i.imgur.com/gk2WyIk.png",
        "Friends": "https://i.imgur.com/WL3nsM4.png",
        "Exes": "https://i.imgur.com/9Cc0Qmq.png",
        "Family": "https://i.imgur.com/aMQeD57.png",
        "Others": "https://i.imgur.com/ftDq9hg.png",
    }

    # Display buttons for each tea category
    selected_category = st.session_state.get('selected_category', None)
    category_list = list(tea_categories.items())

    # Create rows of 3 columns each
    for i in range(0, len(category_list), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(category_list):  # Check to avoid index out of range
                category, img_url = category_list[i + j]
                with col:
                    st.image(img_url, width=100)  # Displaying the image
                    if st.button(category):
                        selected_category = category
                        st.session_state.selected_category = selected_category

    # Refresh if a category is selected
    if selected_category:
        st.session_state.page = "get_tea"
        st.rerun()  # Use rerun for Streamlit

    # Display stories
    if "selected_category" in st.session_state:
        selected_category = st.session_state.selected_category
        st.write(f"You selected: **{selected_category}**")
        
        stories = get_tea_from_db(selected_category.lower())

        if stories:
            for story in stories:
                st.markdown(f"**Story**: {story['text']}")
                st.markdown(f"*Tags*: {', '.join(story['tags'])}")
                st.markdown(f"*Drama Level*: {story.get('drama_level', 'N/A')}")
                st.markdown(f"*Posted on*: {story['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                st.markdown("---")
        else:
            st.write("No stories found for the selected category.")

    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()

if __name__ == "__main__":
    main()
