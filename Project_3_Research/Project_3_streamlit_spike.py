import streamlit as st


def main():
    st.set_page_config(page_title="Transcribed Meetings",
                       page_icon=None, layout='wide', initial_sidebar_state='auto')
    st.title("Transcribed Meetings")
    st.markdown("---")

    # List of names
    names = ["John", "Jane", "Alice", "Bob"]

    # Display list of names in a listbox
    selected_name = st.selectbox("Select a Name:", names)

    # Open button to open a new form
    if st.button("Open"):
        open_new_form(selected_name)

    # New button to open a new form
    if st.button("New"):
        open_new_form("")


def open_new_form(name):
    st.write(f"Opening new form for {name}")


if __name__ == "__main__":
    main()