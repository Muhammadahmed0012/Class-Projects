import streamlit as st
import pandas as pd

st.set_page_config(page_title="📚 Personal Library Manager", layout="centered")

st.title("📚 Personal Library Manager")
st.write("Add and manage your personal book collection!")

# Initialize session state
if 'library' not in st.session_state:
    st.session_state.library = []

# Form to add a new book
with st.form("add_book_form"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    genre = st.selectbox("Genre", ["Fiction", "Non-fiction", "Mystery", "Sci-fi", "Fantasy", "Biography", "Other"])
    status = st.selectbox("Status", ["Unread", "Read"])
    submitted = st.form_submit_button("Add Book")

    if submitted:
        if title and author:
            st.session_state.library.append({
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Status": status
            })
            st.success("Book added to your library!")
        else:
            st.error("Please enter both title and author.")

# Filter books
st.subheader("📖 Your Library")
filter_option = st.radio("Filter by status:", ["All", "Read", "Unread"], horizontal=True)

# Create DataFrame
df = pd.DataFrame(st.session_state.library)

# Apply filter
if not df.empty:
    if filter_option != "All":
        df = df[df["Status"] == filter_option]
    st.dataframe(df, use_container_width=True)
else:
    st.info("No books added yet. Add a book using the form above.")
