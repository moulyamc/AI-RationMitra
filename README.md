# AI Ration Mitra

AI Ration Mitra is a final year major project that modernizes the ration distribution system with AI-powered assistance. It combines a **Flask web application** with features like **chatbot, voice input/output, face recognition (separate module), and admin panel** to create a smarter ration management system.

## 🚀 Features
- 🧑‍💻 User & Admin Login System  
- 🤖 AI Chatbot for ration queries  
- 🎙️ Voice Input + Text-to-Speech Output  
- 🛒 Commodity Management (rice, wheat, dal, sugar, oil, etc.)  
- 📊 Flask-based Admin Dashboard  
- 👤 Face Recognition Module (separate, not integrated into main app)  

## 📂 Project Structure
```
AI-RationMitra/
│
├── RationApp/              # Main Flask Application
│   ├── main.py             # Entry point
│   ├── chatbot.py          # Chatbot logic (voice + text)
│   ├── models.py           # Database models
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, assets
│   └── requirements.txt    # Python dependencies
│
├── FaceRecognition/        # Standalone face recognition module
│   └── (independent code - not integrated)
│
└── README.md               # Project documentation
```

## ⚙️ Installation & Setup
1. Clone this repo:  
   ```bash
   git clone https://github.com/moulyamc/AI-RationMitra.git
   cd AI-RationMitra/RationApp
   ```  
2. Create a virtual environment:  
   ```bash
   python -m venv env
   env\Scripts\activate   # On Windows
   ```  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
4. Run the application:  
   ```bash
   python main.py
   ```  
   Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)   

## 👨‍💻 Authors
- Moulya M C  
- Team Members (if any)  

## ⭐ How to Contribute
If you find this useful, consider starring ⭐ the repo!
