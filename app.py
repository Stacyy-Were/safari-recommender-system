import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Elite Safari Planner", page_icon="🦒", layout="wide")

# 2. HEADER AND DESCRIPTION
st.title("🌍 Elite Safari Tour Recommender")
st.markdown("""
### Welcome to your next Great Adventure. 
We specialize in curated East African experiences. Our expert system matches your personal travel style 
with the most iconic landscapes in the world. Whether you seek the adrenaline of the **Great Migration** or the serenity of a **Private Conservancy**, we ensure the logistics—from PAX capacity to vehicle 
selection—are handled perfectly.
""")
st.info("💡 **How it works:** Select your preferred vibe and group size. Our engine will automatically assign the appropriate vehicle fleet and show you the best matching destinations.")
st.markdown("---")

# 3. THE KNOWLEDGE BASE (20 Destinations)
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

# 4. GOOGLE SHEETS CONNECTION
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception as e:
    st.error("Google Sheets connection not configured. Check your Streamlit Secrets.")

# 5. USER INPUTS
col1, col2 = st.columns([1, 1])

with col1:
    user_mood = st.radio(
        "What is your trip vibe?", 
        ["Adventurous", "Relaxed", "Educational", "Romantic", "Conservation"],
        horizontal=True
    )

with col2:
    user_pax = st.number_input("How many travelers (PAX)?", min_value=1, max_value=25, value=2)

# 6. DYNAMIC VEHICLE LOGIC
if user_pax <= 6:
    vehicle_type = "1x Custom 4x4 Land Cruiser"
    vehicle_desc = "Intimate and private."
elif user_pax <= 12:
    vehicle_type = "2x Custom 4x4 Land Cruisers"
    vehicle_desc = "Two vehicles linked by radio."
else:
    vehicle_type = "Custom Overland Safari Truck"
    vehicle_desc = "Spacious with onboard facilities."

# 7. FILTERING & RESULTS
matches = [tour for tour in safari_data if tour["mood"] == user_mood]

if matches:
    st.markdown(f"### Recommended for a {user_mood} Experience")
    st.success(f"🚙 **Vehicle Fleet Assigned:** {vehicle_type} ({vehicle_desc})")
    
    for tour in matches:
        with st.expander(f"📍 {tour['name']} — {tour['location']}"):
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"🐾 **Wildlife Highlights:** {tour.get('animals', 'Various Species')}")
                st.write(f"☀️ **Expected Weather:** {tour.get('weather', 'Variable')}")
            with c2:
                st.write(f"📅 **Best Time to Visit:** {tour.get('best_time', 'Year-round')}")

    st.markdown("---")
    
    # 8. BOOKING FORM
    with st.form("booking_form"):
        st.subheader("📝 Request a Customized Quote")
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        selected_safari = st.selectbox("Preferred Destination", [t['name'] for t in matches])
        notes = st.text_area("Any special requests or dietary requirements?")
        
        if st.form_submit_button("Send to Planning Team"):
            if full_name and email:
                try:
                    # Create the lead row
                    new_lead = pd.DataFrame([{
                        "Name": full_name,
                        "Email": email,
                        "Mood": user_mood,
                        "PAX": user_pax,
                        "Destination": selected_safari,
                        "Vehicle": vehicle_type,
                        "Notes": notes
                    }])
                    
                    # Read current sheet with ttl=0 to avoid cache issues
                    existing_data = conn.read(ttl=0)
                    
                    # Combine and Update
                    updated_df = pd.concat([existing_data, new_lead], ignore_index=True)
                    conn.update(data=updated_df)
                    
                    st.balloons()
                    st.success("Your request has been sent! Stacy and the team will be in touch.")
                except Exception as e:
                    st.error(f"Error submitting to Google Sheets: {e}")
            else:
                st.warning("Please provide your name and email address.")
else:
    st.error("No matches found for this specific mood. Please select a different vibe.")