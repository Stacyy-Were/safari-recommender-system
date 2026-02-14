import streamlit as st

st.set_page_config(page_title="Elite Safari Planner", page_icon="🦒", layout="wide")

# 1. Knowledge Base: Safari Tours
safari_data = [
    {"name": "Masai Mara", "location": "Kenya", "mood": "Adventurous", "weather": "Sunny & Dusty", "animals": ["Lions", "Wildebeest", "Cheetahs"], "best_time": "July - Oct"},
    {"name": "Serengeti", "location": "Tanzania", "mood": "Adventurous", "weather": "Hot & Vast", "animals": ["Lions", "Leopards", "Hyenas"], "best_time": "June - Sept"},
    {"name": "Amboseli", "location": "Kenya", "mood": "Relaxed", "weather": "Dry & Hot", "animals": ["Elephants", "Flamingos"], "best_time": "Jan - March"},
    {"name": "Bwindi Forest", "location": "Uganda", "mood": "Educational", "animals": ["Mountain Gorillas"], "best_time": "June - Aug"},
    {"name": "Ngorongoro Crater", "location": "Tanzania", "mood": "Romantic", "weather": "Mild & Misty", "animals": ["Black Rhinos", "Lions"], "best_time": "Year-round"},
    {"name": "Volcanoes Park", "location": "Rwanda", "mood": "Conservation", "weather": "Cool & Misty", "animals": ["Gorillas", "Golden Monkeys"], "best_time": "Dec - Feb"},
    {"name": "Samburu", "location": "Kenya", "mood": "Adventurous", "weather": "Arid & Hot", "animals": ["Gerenuk", "Grevy's Zebra"], "best_time": "June - Sept"},
    {"name": "Laikipia", "location": "Kenya", "mood": "Educational", "animals": ["Wild Dogs", "Rhinos"], "best_time": "Year-round"},
    {"name": "Tsavo East", "location": "Kenya", "mood": "Relaxed", "weather": "Hot", "animals": ["Red Elephants", "Lions"], "best_time": "Dec - March"},
    {"name": "Lake Manyara", "location": "Tanzania", "mood": "Relaxed", "weather": "Tropical", "animals": ["Tree-climbing Lions"], "best_time": "June - Oct"},
    {"name": "Queen Elizabeth", "location": "Uganda", "mood": "Adventurous", "weather": "Humid", "animals": ["Hippos", "Leopards"], "best_time": "Jan - Feb"},
    {"name": "Tarangire", "location": "Tanzania", "mood": "Relaxed", "weather": "Dry", "animals": ["Large Elephant Herds"], "best_time": "June - Oct"},
    {"name": "Ol Pejeta", "location": "Kenya", "mood": "Conservation", "animals": ["White Rhinos", "Chimpanzees"], "best_time": "Year-round"},
    {"name": "Murchison Falls", "location": "Uganda", "mood": "Adventurous", "weather": "Tropical", "animals": ["Crocodiles", "Giraffes"], "best_time": "Dec - Feb"},
    {"name": "Akagera", "location": "Rwanda", "mood": "Adventurous", "weather": "Warm", "animals": ["Zebras", "Antelopes"], "best_time": "June - Sept"},
    {"name": "Hell's Gate", "location": "Kenya", "mood": "Adventurous", "weather": "Sunny", "animals": ["Warthogs", "Buffalos"], "best_time": "Year-round"},
    {"name": "Zanzibar Reefs", "location": "Tanzania", "mood": "Romantic", "weather": "Tropical", "animals": ["Dolphins", "Sea Turtles"], "best_time": "Nov - Feb"},
    {"name": "Solio Reserve", "location": "Kenya", "mood": "Conservation", "animals": ["Rhinos"], "best_time": "Year-round"},
    {"name": "Lake Nakuru", "location": "Kenya", "mood": "Educational", "animals": ["Flamingos", "White Rhinos"], "best_time": "Year-round"},
    {"name": "Kidepo Valley", "location": "Uganda", "mood": "Adventurous", "weather": "Hot/Dry", "animals": ["Cheetahs", "Ostriches"], "best_time": "Sept - March"}
]

# 2. UI
st.title("🌍 Elite Safari Tour Recommender")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    user_mood = st.selectbox(
        "What is your trip vibe? (Mood)", 
        ["Adventurous", "Relaxed", "Educational", "Romantic", "Conservation"]
    )

with col2:
    user_pax = st.number_input("How many travelers (PAX)?", min_value=1, max_value=25, value=2)

st.markdown("---")

#3. Vehicle Logic
if user_pax <= 6:
    vehicle_type = "1x Custom 4x4 Land Cruiser"
    vehicle_note = "A single vehicle for an intimate, private experience."
elif user_pax <= 12:
    vehicle_type = "2x Custom 4x4 Land Cruisers"
    vehicle_note = "Your group will travel in two linked vehicles with radio communication."
else:
    vehicle_type = "Custom Overland Safari Truck"
    vehicle_note = "Equipped with an onboard kitchen and crew for large group comfort."



#4. Filtering & Displaying Results
matches = [tour for tour in safari_data if tour["mood"] == user_mood]

if matches:
    st.subheader(f"✨ Found {len(matches)} matches for a {user_mood} trip:")
    st.info(f"🚙 **Vehicle Assignment:** {vehicle_type}\n\n*{vehicle_note}*")
    
    for tour in matches:
        # Expanders to keep the list tidy
        with st.expander(f"📍 {tour['name']} ({tour['location']})"):
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"🐾 **Animals to see:** {', '.join(tour['animals'])}")
                if "weather" in tour: st.write(f"☀️ **Weather:** {tour['weather']}")
            with c2:
                st.write(f"📅 **Best Time to Visit:** {tour['best_time']}")
                if st.button(f"Request Quote for {tour['name']}", key=tour['name']):
                    st.success(f"Inquiry for {user_pax} PAX sent to the booking team!")
else:
    st.error("No tours match your criteria. Try a different mood!")