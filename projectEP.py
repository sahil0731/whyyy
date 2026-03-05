import streamlit as st

# Page configuration
st.set_page_config(page_title="QuickTicket", page_icon="🎫")


def main():
    st.title("🎫 QuickTicket Booking")
    st.markdown("Reserve your spot for the **Grand Tech Summit 2026**.")

    # --- Booking Form ---
    with st.form("booking_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")

        with col2:
            ticket_type = st.selectbox("Ticket Category", ["General", "VIP", "Backstage Pass"])
            quantity = st.number_input("Number of Tickets", min_value=1, max_value=10, value=1)

        date = st.date_input("Select Date")
        special_requests = st.text_area("Additional Requests (Optional)")

        submit_button = st.form_submit_button("Book Now")

    # --- Handling Logic ---
    if submit_button:
        if name and email:
            # Pricing logic
            prices = {"General": 50, "VIP": 150, "Backstage Pass": 300}
            total_cost = prices[ticket_type] * quantity

            st.success(f"Success! Thank you, {name}.")

            # Summary Table
            st.subheader("Booking Summary")
            st.write(f"**Confirmation for:** {ticket_type} Ticket(s)")
            st.write(f"**Total Amount:** ${total_cost}")
            st.info("A confirmation email has been sent to your inbox.")

            # Balloon effect for a little flair
            st.balloons()
        else:
            st.warning("Please fill in your name and email to proceed.")


if __name__ == "__main__":
    main()