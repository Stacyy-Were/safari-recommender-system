🦒 Elite Safari Tour Recommender
A professional Streamlit web application designed for East African safari agencies to provide curated travel recommendations and capture high-quality leads.

🚀 Features
Dynamic Matching: Recommends 20+ specific destinations across Kenya, Tanzania, Uganda, and Rwanda based on user "vibes" (Adventurous, Romantic, etc.).

Smart Fleet Assignment: Automatically calculates the required vehicle fleet (Land Cruisers vs. Overland Trucks) based on the number of travelers (PAX).

Lead Capture System: Integrated inquiry form for users to request custom quotes directly.

Professional UI: Built with a "Wide" layout, interactive expanders for wildlife details, and real-time feedback.

🛠️ Tech Stack
Language: Python 3.x

Framework: Streamlit

Data Handling: Pandas

Communication: Requests API (Integrated with FormSubmit/EmailJS)

📦 Installation & Local Setup
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/safari-recommender-system.git
cd safari-recommender-system
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
📂 Project Structure
Plaintext
├── app.py              # Main application logic and UI
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation
📝 Configuration
To enable the email inquiry feature, ensure the MY_EMAIL variable in app.py is updated to your professional contact address. For production deployment on Streamlit Cloud, remember to verify your sender address via the chosen email API service.

🦒 Destinations Covered
Includes iconic locations such as:

Kenya: Masai Mara, Amboseli, Samburu, Ol Pejeta.

Tanzania: Serengeti, Ngorongoro Crater, Tarangire.

Uganda: Bwindi Impenetrable Forest, Murchison Falls.

Rwanda: Volcanoes National Park, Akagera.