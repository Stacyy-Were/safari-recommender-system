import streamlit as st
import requests
import pandas as pd

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Elite Safari Planner", page_icon="🦒", layout="centered")

# 2. CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Montserrat:wght@300;400;700&display=swap');

    /* Global Background */
    .stApp {
        background-color: #F9F4EE; 
    }

    /* --- ICON & TEXT FIX --- */
    /* This prevents the "_arrow_right" glitch by ensuring icons use system fonts */
    span[data-baseweb="icon"] {
        font-family: inherit !important;
    }
    
    /* Apply Montserrat only to text elements, avoiding icon containers */
    p, label, li, [data-testid="stMarkdownContainer"] p {
        font-family: 'Montserrat', sans-serif !important;
        color: #4A4A4A;
    }

    /* Elegant Hero Banner */
    .hero-container {
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), 
                          url('https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        padding: 90px 20px;
        text-align: center;
        border: 2px solid #C5A059;
        margin-bottom: 30px;
    }

    .logo-text {
        font-family: 'Playfair Display', serif;
        color: #FFFFFF !important;
        font-size: 55px;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 0px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.6);
    }

    .sub-logo {
        font-family: 'Montserrat', sans-serif;
        color: #D4AF37;
        font-size: 14px;
        letter-spacing: 8px;
        text-transform: uppercase;
    }

    /* Headers */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #3D3D3D !important;
    }

    /* Info Box (Fleet Assignment) */
    .stAlert {
        background-color: #EDEADE !important;
        border: 1px solid #4B5320 !important;
        color: #4B5320 !important;
        border-radius: 0px !important;
    }

    /* Expander Styling */
    .streamlit-expanderHeader {
        background-color: #FFFFFF !important;
        border-bottom: 1px solid #E0D7C6 !important;
        border-radius: 0px !important;
    }
    
    .streamlit-expanderHeader p {
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Luxury Form Styling */
    [data-testid="stForm"] {
        background-color: #FCF9F5 !important; 
        border: 2px solid #8B4513 !important; 
        padding: 40px !important;
        border-radius: 0px !important;
        box-shadow: 15px 15px 0px #4B5320; 
    }

    /* Form Inputs */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
    }

    /* Submit Button */
    .stButton>button {
        background: linear-gradient(145deg, #C5A059, #B8860B) !important;
        color: #FFFFFF !important;
        border: 1px solid #8B4513 !important;
        font-weight: 700 !important;
        height: 50px;
        width: 100%;
        letter-spacing: 2px;
    }

    .stButton>button:hover {
        background: #4B5320 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. TOP LOGO SECTION
st.markdown("""
    <div class="hero-container">
        <div class="logo-text">ELITE SAFARI</div>
        <div class="sub-logo">PLANNERS</div>
    </div>
    """, unsafe_allow_html=True)

# 4. KNOWLEDGE BASE
safari_data = [
    # KENYA
    {"name": "Masai Mara", "location": "Kenya", "mood": "Adventurous", "animals": "The Big Five, Wildebeest Migration", "best_time": "July - Oct", "vibe": "Classic Savannah"},
    {"name": "Amboseli", "location": "Kenya", "mood": "Relaxed", "animals": "Large Elephant Herds, Mt. Kilimanjaro", "best_time": "Jan - March", "vibe": "Scenic Photography"},
    {"name": "Samburu", "location": "Kenya", "mood": "Educational", "animals": "Reticulated Giraffe, Grevy's Zebra", "best_time": "June - Sept", "vibe": "Arid Culture"},
    {"name": "Ol Pejeta", "location": "Kenya", "mood": "Conservation", "animals": "Last Northern White Rhinos", "best_time": "Year-round", "vibe": "Wildlife Protection"},
    {"name": "Lake Nakuru", "location": "Kenya", "mood": "Relaxed", "animals": "Flamingos, White & Black Rhinos", "best_time": "Year-round", "vibe": "Lakeside Birding"},

    # TANZANIA
    {"name": "Serengeti", "location": "Tanzania", "mood": "Adventurous", "animals": "Lions, Leopards, Cheetahs", "best_time": "June - Sept", "vibe": "Endless Plains"},
    {"name": "Ngorongoro Crater", "location": "Tanzania", "mood": "Romantic", "animals": "High density of Predators", "best_time": "Year-round", "vibe": "Natural Wonder"},
    {"name": "Tarangire", "location": "Tanzania", "mood": "Relaxed", "animals": "Ancient Baobabs, Large Elephant Herds", "best_time": "June - Oct", "vibe": "Ancient Landscapes"},
    {"name": "Zanzibar Reefs", "location": "Tanzania", "mood": "Romantic", "animals": "Dolphins, Red Colobus Monkeys", "best_time": "Nov - Feb", "vibe": "Tropical Spice Island"},

    # UGANDA & RWANDA 
    {"name": "Bwindi Forest", "location": "Uganda", "mood": "Educational", "animals": "Mountain Gorillas", "best_time": "June - Aug", "vibe": "Jungle Trekking"},
    {"name": "Murchison Falls", "location": "Uganda", "mood": "Adventurous", "animals": "Nile Crocodiles, Rothschild Giraffes", "best_time": "Dec - Feb", "vibe": "River Expedition"},
    {"name": "Volcanoes Park", "location": "Rwanda", "mood": "Conservation", "animals": "Gorillas, Golden Monkeys", "best_time": "Dec - Feb", "vibe": "Misty Mountains"},
    {"name": "Akagera", "location": "Rwanda", "mood": "Relaxed", "animals": "Zebras, Antelopes, Hippos", "best_time": "June - Sept", "vibe": "Lakeside Safari"},

    #  BOTSWANA & NAMIBIA 
    {"name": "Okavango Delta", "location": "Botswana", "mood": "Romantic", "animals": "Water-adapted Lions, Hippos", "best_time": "May - Sept", "vibe": "Luxury Water Safari"},
    {"name": "Chobe River", "location": "Botswana", "mood": "Relaxed", "animals": "Massive Elephant crossings", "best_time": "May - Oct", "vibe": "Boat-based Safari"},
    {"name": "Sossusvlei", "location": "Namibia", "mood": "Romantic", "animals": "Oryx, Desert Fox", "best_time": "May - Oct", "vibe": "Towering Red Dunes"},
    {"name": "Etosha", "location": "Namibia", "mood": "Adventurous", "animals": "Rhinos around waterholes", "best_time": "July - Sept", "vibe": "Salt Pan Scenery"},
    {"name": "Skeleton Coast", "location": "Namibia", "mood": "Adventurous", "animals": "Desert Lions, Fur Seals", "best_time": "Oct - March", "vibe": "Rugged Isolation"},
    
    #  SOUTH AFRICA 
    {"name": "Kruger National Park", "location": "South Africa", "mood": "Educational", "animals": "The Big Five, Wild Dogs", "best_time": "May - Sept", "vibe": "World-Class Infrastructure"},
    {"name": "Phinda Reserve", "location": "South Africa", "mood": "Conservation", "animals": "Cheetahs, Black Rhinos", "best_time": "Year-round", "vibe": "Private Luxury"}
]


# 5. USER INPUTS
st.subheader("Tailor Your Expedition")
u_col1, u_col2 = st.columns([2, 1])

with u_col1:
    user_mood = st.select_slider("Select your desired vibe:", 
                               options=["Adventurous", "Relaxed", "Educational", "Romantic", "Conservation"])
with u_col2:
    user_pax = st.number_input("Guests (PAX):", min_value=1, max_value=25, value=2)

# Fleet Logic
vehicle = "1x Custom 4x4 Land Cruiser" if user_pax <= 6 else "2x Custom 4x4 Land Cruisers"

# 6. RESULTS
st.markdown("---")
matches = [t for t in safari_data if t["mood"] == user_mood]

if matches:
    st.info(f"🚙 **Fleet Assignment:** {vehicle}")
    for tour in matches:
        with st.expander(f"{tour['name'].upper()} — {tour['location']}"):
            st.markdown(f"*Experience Style: {tour['vibe']}*")
            c1, c2 = st.columns(2)
            c1.write(f"🐾 **Wildlife:** {tour['animals']}")
            c2.write(f"📅 **Best Time:** {tour['best_time']}")

    # 7. BOOKING FORM
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏹 Secure Your Private Itinerary")
    with st.form("safari_form"):
        f1, f2 = st.columns(2)
        with f1:
            name = st.text_input("Lead Traveler Name")
            email = st.text_input("Email")
        with f2:
            dest = st.selectbox("Preferred Destination", [t['name'] for t in matches])
            date = st.text_input("Desired Dates")
            
        notes = st.text_area("Special Requirements")
        
        MY_EMAIL = "stacywere1234@gmail.com" 
        if st.form_submit_button("DISPATCH INQUIRY"):
            if name and email:
                try:
                    payload = {"Name": name, "Email": email, "Dest": dest, "PAX": user_pax, "Notes": notes}
                    requests.post(f"https://formsubmit.co/ajax/{MY_EMAIL}", json=payload)
                    st.balloons()
                    st.success("Dispatch received. Our head ranger will contact you shortly.")
                except:
                    st.error("Connection error. Please try again.")
            else:
                st.warning("Please provide contact details.")

# 8. FOOTER
st.markdown("<p style='text-align:center; color:#C5A059; margin-top:50px; font-size:11px;'>© 2026 ELITE SAFARI PLANNERS | AFRICAN EXPEDITION SPECIALISTS</p>", unsafe_allow_html=True)