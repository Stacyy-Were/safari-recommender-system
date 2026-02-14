import streamlit as st

st.title("🌍 Safari Tour Recommender")

# Set Page Config for a professional look
st.set_page_config(page_title="Safari Mood Finder", page_icon="🦒", layout="wide")

# --- 1. The Knowledge Base ---
# List of dictionaries to store the complex safari facts
safari_data = [
    {
        "name": "The Great Migration Thrill",
        "location": "Masai Mara, Kenya",
        "mood": "Adventurous",
        "weather": "Sunny & Dusty",
        "animals": ["Lions", "Wildebeest", "Cheetahs", "Crocodiles"],
        "max_pax": 6,
        "vehicle": "Open-top 4x4 Land Cruiser",
        "best_time": "July to October"
    },
    {
        "name": "Kilimanjaro Sunset Zen",
        "location": "Amboseli, Kenya",
        "mood": "Relaxed",
        "weather": "Dry & Hot",
        "animals": ["Elephants", "Flamingos", "Hippos"],
        "max_pax": 4,
        "vehicle": "Luxury Safari Van with Pop-up Roof",
        "best_time": "January to March"
    },
    {
        "name": "Northern Frontier Conservation",
        "location": "Samburu/Lewa, Kenya",
        "mood": "Educational",
        "weather": "Breezy & Arid",
        "animals": ["Black Rhino", "Grevy's Zebra", "Reticulated Giraffe"],
        "max_pax": 2,
        "vehicle": "Electric Silent Safari Jeep",
        "best_time": "Year-round"
    },
    {
        "name": "Coastal Bush & Beach Mix",
        "location": "Lamu/Tsavo, Kenya",
        "mood": "Romantic",
        "weather": "Humid & Tropical",
        "animals": ["Red Elephants", "Lions", "Dolphins"],
        "max_pax": 2,
        "vehicle": "Convertible Safari Jeep & Dhow Boat",
        "best_time": "November to February"
    }
]

# --- 2. USER INTERFACE (The Frontend) ---
st.title("🌍 Safari Tour Recommender")
st.markdown("---")

# Using columns to organize inputs
col1, col2 = st.columns(2)

with col1:
    user_mood = st.selectbox(
        "How are you feeling today? (Mood)", 
        ["Adventurous", "Relaxed", "Educational", "Romantic"]
    )

with col2:
    user_pax = st.number_input("How many travelers (PAX)?", min_value=1, max_value=10, value=2)

st.markdown("---")

# --- 3. FILTERING LOGIC (The Backend) ---
# We search the data for a mood match AND ensure the car can fit the group
matches = [
    tour for tour in safari_data 
    if tour["mood"] == user_mood and tour["max_pax"] >= user_pax
]

# --- 4. DISPLAYING RESULTS ---
if matches:
    st.subheader(f"✨ We found {len(matches)} matches for your {user_mood} trip:")
    
    for tour in matches:
        with st.container():
            # Create a nice "card" for each safari
            st.write(f"### {tour['name']}")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.info(f"📍 **Location:**\n{tour['location']}")
                st.info(f"🚙 **Vehicle:**\n{tour['vehicle']}")
            with c2:
                st.success(f"🐾 **Animals:**\n{', '.join(tour['animals'])}")
                st.success(f"☀️ **Weather:**\n{tour['weather']}")
            with c3:
                st.warning(f"👥 **Max Capacity:**\n{tour['max_pax']} PAX")
                st.warning(f"📅 **Best Time:**\n{tour['best_time']}")
            st.markdown("---")
else:
    st.error("No tours match your specific PAX and Mood combination. Try a smaller group or a different mood!")