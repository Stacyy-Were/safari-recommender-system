import streamlit as st
import requests  # We need this to send the email data
import pandas as pd

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Elite Safari Planner", page_icon="🦒", layout="wide")

# 2. AGENCY DESCRIPTION & HEADER
st.title("🌍 Elite Safari Tour Recommender")
st.markdown("""
### Welcome to your next Great Adventure. 
We specialize in curated East African experiences. Our expert system matches your personal travel style 
with the most iconic landscapes in the world. Once you find your vibe, request a quote and our team will 
reach out to you directly via email.
""")
st.info("💡 **How it works:** Select your vibe and group size. We will assign the fleet and show you destinations. Request a quote to receive a custom itinerary.")
st.markdown("---")

# 3. THE KNOWLEDGE BASE
safari_data = [
    {"name": "Masai Mara", "location": "Kenya", "mood": "Adventurous", "weather": "Sunny & Dusty", "animals": "Lions, Wildebeest, Cheetahs", "best_time": "July - Oct"},
    {"name": "Serengeti", "location": "Tanzania", "mood": "Adventurous", "weather": "Hot & Vast", "animals": "Lions, Leopards, Hyenas", "best_time": "June - Sept"},
    {"name": "Amboseli", "location": "Kenya", "mood": "Relaxed", "weather": "Dry & Hot", "animals": "Elephants, Flamingos, Hippos", "best_time": "Jan - March"},
    {"name": "Bwindi Forest", "location": "Uganda", "mood": "Educational", "weather": "Rainy & Cool", "animals": "Mountain Gorillas", "best_time": "June - Aug"},
    {"name": "Ngorongoro Crater", "location": "Tanzania", "mood": "Romantic", "weather": "Mild & Misty", "animals": "Black Rhinos, Lions", "best_time": "Year-round"},
    {"name": "Volcanoes Park", "location": "Rwanda", "mood": "Conservation", "weather": "Cold & Misty", "animals": "Gorillas, Golden Monkeys", "best_time": "Dec - Feb"},
    {"name": "Samburu", "location": "Kenya", "mood": "Adventurous", "weather": "Arid & Hot", "animals": "Gerenuk, Grevy's Zebra", "best_time": "June - Sept"},
    {"name": "Laikipia", "location": "Kenya", "mood": "Educational", "weather": "Breezy & Arid", "animals": "Wild Dogs, Rhinos", "best_time": "Year-round"},
    {"name": "Tsavo East", "location": "Kenya", "mood": "Relaxed", "weather": "Hot", "animals": "Red Elephants, Lions", "best_time": "Dec - March"},
    {"name": "Lake Manyara", "location": "Tanzania", "mood": "Relaxed", "weather": "Tropical", "animals": "Tree-climbing Lions", "best_time": "June - Oct"},
    {"name": "Queen Elizabeth", "location": "Uganda", "mood": "Adventurous", "weather": "Humid", "animals": "Hippos, Leopards", "best_time": "Jan - Feb"},
    {"name": "Tarangire", "location": "Tanzania", "mood": "Relaxed", "weather": "Dry", "animals": "Massive Elephant Herds", "best_time": "June - Oct"},
    {"name": "Ol Pejeta", "location": "Kenya", "mood": "Conservation", "weather": "Mild", "animals": "White Rhinos, Chimpanzees", "best_time": "Year-round"},
    {"name": "Murchison Falls", "location": "Uganda", "mood": "Adventurous", "weather": "Tropical", "animals": "Crocodiles, Giraffes", "best_time": "Dec - Feb"},
    {"name": "Akagera", "location": "Rwanda", "mood": "Adventurous", "weather": "Warm", "animals": "Zebras, Antelopes", "best_time": "June - Sept"},
    {"name": "Hell's Gate", "location": "Kenya", "mood": "Adventurous", "weather": "Sunny", "animals": "Warthogs, Buffalos", "best_time": "Year-round"},
    {"name": "Zanzibar Reefs", "location": "Tanzania", "mood": "Romantic", "weather": "Tropical", "animals": "Dolphins, Sea Turtles", "best_time": "Nov - Feb"},
    {"name": "Solio Reserve", "location": "Kenya", "mood": "Conservation", "weather": "Cool", "animals": "Black & White Rhinos", "best_time": "Year-round"},
    {"name": "Lake Nakuru", "location": "Kenya", "mood": "Educational", "weather": "Mild", "animals": "Flamingos, White Rhinos", "best_time": "Year-round"},
    {"name": "Kidepo Valley", "location": "Uganda", "mood": "Adventurous", "weather": "Hot & Dry", "animals": "Cheetahs, Ostriches", "best_time": "Sept - March"}
]

# 4. USER INPUTS
col1, col2 = st.columns([1, 1])

with col1:
    user_mood = st.radio(
        "What is your trip vibe?", 
        ["Adventurous", "Relaxed", "Educational", "Romantic", "Conservation"],
        horizontal=True
    )

with col2:
    user_pax = st.number_input("How many travelers (PAX)?", min_value=1, max_value=25, value=2)

# 5. DYNAMIC VEHICLE LOGIC
if user_pax <= 6:
    vehicle_type = "1x Custom 4x4 Land Cruiser"
elif user_pax <= 12:
    vehicle_type = "2x Custom 4x4 Land Cruisers"
else:
    vehicle_type = "Custom Overland Safari Truck"

# 6. FILTERING & RESULTS
matches = [tour for tour in safari_data if tour["mood"] == user_mood]

if matches:
    st.markdown(f"### Recommended for a {user_mood} Experience")
    st.success(f"🚙 **Vehicle Assigned:** {vehicle_type}")
    
    for tour in matches:
        with st.expander(f"📍 {tour['name']} — {tour['location']}"):
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"🐾 **Wildlife:** {tour.get('animals', 'Various')}")
                st.write(f"☀️ **Weather:** {tour.get('weather', 'Variable')}")
            with c2:
                st.write(f"📅 **Best Time:** {tour.get('best_time', 'Year-round')}")

    st.markdown("---")
    
    # 7. EMAIL BOOKING FORM
    with st.form("email_form"):
        st.subheader("📬 Request a Custom Quote")
        full_name = st.text_input("Full Name")
        email_address = st.text_input("Your Email Address")
        selected_safari = st.selectbox("Destination of interest", [t['name'] for t in matches])
        notes = st.text_area("Any special requests (Dietary, Honeymoon, etc.)?")
        
        # Direct email
        MY_CONTACT_EMAIL = "stacywere1234@gmail.com" 
        
        submit_button = st.form_submit_button("Send Inquiry")
        
        if submit_button:
            if full_name and email_address:
                # Direct Email body
                email_body = f"""
                NEW SAFARI LEAD:
                -----------------
                Name: {full_name}
                Email: {email_address}
                Vibe: {user_mood}
                PAX: {user_pax}
                Destination: {selected_safari}
                Vehicle: {vehicle_type}
                Notes: {notes}
                """
                
                # Send to FormSubmit using POST request
                try:
                    response = requests.post(
                        f"https://formsubmit.co/ajax/{MY_CONTACT_EMAIL}",
                        data={
                            "_subject": f"🦁 New Inquiry from {full_name}",
                            "message": email_body,
                            "_replyto": email_address
                        }
                    )
                    if response.status_code == 200:
                        st.balloons()
                        st.success("Dankie! We've received your request and will email you back soon.")
                    else:
                        st.error("Submission failed. Please check your internet or try again.")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please fill in your name and email address.")
else:
    st.error("No matches found for this mood.")