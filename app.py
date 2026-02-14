import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Safari Mood Finder", page_icon="🦒", layout="wide")

# 2. KNOWLEDGE BASE
safari_data = [
    {"name": "Masai Mara", "location": "Kenya", "mood": "Adventurous", "weather": "Sunny & Dusty", "animals": "Lions, Wildebeest", "best_time": "July - Oct"},
    {"name": "Serengeti", "location": "Tanzania", "mood": "Adventurous", "weather": "Hot & Vast", "animals": "Lions, Leopards", "best_time": "June - Sept"},
    {"name": "Amboseli", "location": "Kenya", "mood": "Relaxed", "weather": "Dry & Hot", "animals": "Elephants, Flamingos", "best_time": "Jan - March"},
    {"name": "Bwindi Forest", "location": "Uganda", "mood": "Educational", "animals": "Mountain Gorillas", "best_time": "June - Aug"},
    {"name": "Ngorongoro Crater", "location": "Tanzania", "mood": "Romantic", "weather": "Mild & Misty", "animals": "Black Rhinos", "best_time": "Year-round"},
    {"name": "Volcanoes Park", "location": "Rwanda", "mood": "Conservation", "weather": "Cool & Misty", "animals": "Gorillas, Golden Monkeys", "best_time": "Dec - Feb"},
    {"name": "Samburu", "location": "Kenya", "mood": "Adventurous", "weather": "Arid & Hot", "animals": "Gerenuk, Grevy's Zebra", "best_time": "June - Sept"},
    {"name": "Laikipia", "location": "Kenya", "mood": "Educational", "animals": "Wild Dogs, Rhinos", "best_time": "Year-round"},
    {"name": "Tsavo East", "location": "Kenya", "mood": "Relaxed", "weather": "Hot", "animals": "Red Elephants", "best_time": "Dec - March"},
    {"name": "Lake Manyara", "location": "Tanzania", "mood": "Relaxed", "weather": "Tropical", "animals": "Tree-climbing Lions", "best_time": "June - Oct"},
    {"name": "Queen Elizabeth", "location": "Uganda", "mood": "Adventurous", "weather": "Humid", "animals": "Hippos, Leopards", "best_time": "Jan - Feb"},
    {"name": "Tarangire", "location": "Tanzania", "mood": "Relaxed", "weather": "Dry", "animals": "Elephant Herds", "best_time": "June - Oct"},
    {"name": "Ol Pejeta", "location": "Kenya", "mood": "Conservation", "animals": "White Rhinos, Chimpanzees", "best_time": "Year-round"},
    {"name": "Murchison Falls", "location": "Uganda", "mood": "Adventurous", "weather": "Tropical", "animals": "Crocodiles, Giraffes", "best_time": "Dec - Feb"},
    {"name": "Akagera", "location": "Rwanda", "mood": "Adventurous", "weather": "Warm", "animals": "Zebras, Antelopes", "best_time": "June - Sept"},
    {"name": "Hell's Gate", "location": "Kenya", "mood": "Adventurous", "weather": "Sunny", "animals": "Warthogs, Buffalos", "best_time": "Year-round"},
    {"name": "Zanzibar Reefs", "location": "Tanzania", "mood": "Romantic", "weather": "Tropical", "animals": "Dolphins, Turtles", "best_time": "Nov - Feb"},
    {"name": "Solio Reserve", "location": "Kenya", "mood": "Conservation", "animals": "Rhinos", "best_time": "Year-round"},
    {"name": "Lake Nakuru", "location": "Kenya", "mood": "Educational", "animals": "Flamingos, White Rhinos", "best_time": "Year-round"},
    {"name": "Kidepo Valley", "location": "Uganda", "mood": "Adventurous", "weather": "Hot/Dry", "animals": "Cheetahs, Ostriches", "best_time": "Sept - March"}
]

# 3. GOOGLE SHEETS CONNECTION
# Note: Google Sheets link > .streamlit/secrets.toml
conn = st.connection("gsheets", type=GSheetsConnection)

# 4. USER INTERFACE
st.title("🌍 Elite Safari Tour Recommender")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    user_mood = st.selectbox("What's your trip vibe?", ["Adventurous", "Relaxed", "Educational", "Romantic", "Conservation"])
with col2:
    user_pax = st.number_input("How many travelers (PAX)?", min_value=1, max_value=25, value=2)

# 5. DYNAMIC VEHICLE LOGIC
if user_pax <= 6:
    vehicle_type = "1x Custom 4x4 Land Cruiser"
elif user_pax <= 12:
    vehicle_type = "2x Custom 4x4 Land Cruisers"
else:
    vehicle_type = "Custom Overland Safari Truck"

# 6. FILTERING RESULTS
matches = [tour for tour in safari_data if tour["mood"] == user_mood]

# 7. DISPLAY RESULTS & ENQUIRY FORM
if matches:
    st.info(f"🚙 **Vehicle Assigned:** {vehicle_type}")
    
    for tour in matches:
        with st.expander(f"📍 {tour['name']} ({tour['location']})"):
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"🐾 **Animals:** {tour['animals']}")
                st.write(f"☀️ **Weather:** {tour['weather']}")
            with c2:
                st.write(f"📅 **Best Time:** {tour['best_time']}")

    st.markdown("---")
    # GOOGLE SHEETS FORM
    with st.form("booking_form"):
        st.subheader("📝 Request a Final Quote")
        full_name = st.text_input("Name")
        email = st.text_input("Email")
        selected_safari = st.selectbox("Which destination interests you most?", [t['name'] for t in matches])
        notes = st.text_area("Additional Notes")
        
        if st.form_submit_button("Send Inquiry"):
            if full_name and email:
                try:
                    # NEW ROW
                    new_lead = pd.DataFrame([{
                        "Name": full_name,
                        "Email": email,
                        "Mood": user_mood,
                        "PAX": user_pax,
                        "Destination": selected_safari,
                        "Vehicle": vehicle_type,
                        "Notes": notes
                    }])
                    
                    # READ-APPEND-WRITE
                    existing_data = conn.read()
                    updated_df = pd.concat([existing_data, new_lead], ignore_index=True)
                    conn.update(data=updated_df)
                    
                    st.balloons()
                    st.success("Sent! Your data has been recorded in the Safari Leads sheet.")
                except Exception as e:
                    st.error(f"Error connecting to Google Sheets: {e}")
            else:
                st.warning("Please enter your name and email!")
else:
    st.error("No matches found for this mood.")