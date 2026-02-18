# 🦒 Elite Safari Tour Recommender

A professional Streamlit web application designed for East African safari agencies to provide curated travel recommendations and capture high-quality leads.

## 🚀 Features
* **Dynamic Matching:** Recommends 20+ specific destinations across Kenya, Tanzania, Uganda, and Rwanda based on user "vibes" (Adventurous, Romantic, etc.).
* **Smart Fleet Assignment:** Automatically calculates the required vehicle fleet (Land Cruisers vs. Overland Trucks) based on the number of travelers (PAX).
* **Lead Capture System:** Integrated inquiry form for users to request custom quotes directly.
* **Professional UI:** Built with a "Wide" layout, interactive expanders for wildlife details, and real-time feedback.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Framework:** [Streamlit](https://streamlit.io/)
* **Data Handling:** Pandas
* **Communication:** Requests API (Integrated with FormSubmit)

## 📦 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/safari-recommender-system.git](https://github.com/YOUR_USERNAME/safari-recommender-system.git)
   cd safari-recommender-system

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the application:**
   ```bash
   streamlit run app.py

## 📝 How the system works
The app uses a POST request to FormSubmit to send user inquiries directly to the agency's email.

Note: The first time a lead is sent, the receiver must check their email to activate the form endpoint (But for now, I get very complicated and confusing server responses, still trying to get around it)

