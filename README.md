<img width="1355" height="593" alt="image" src="https://github.com/user-attachments/assets/fd1d2622-9b30-49c9-a779-2f8ea75357ab" />
## 🏠 Bangalore House Price Prediction

A machine learning web application to predict real estate prices in Bangalore using scikit-learn and Flask.

### ✨ Features

- **Interactive Web Interface** - User-friendly form to input property details
- **Real-time Predictions** - Get instant price estimates for properties
- **Location-based Analysis** - Select from 100+ Bangalore localities
- **Property Details Input**:
  - Area in Square Feet
  - BHK (Bedrooms)
  - Bathrooms
  - Location

### 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Flask & Flask-CORS
- scikit-learn (ML Model)
- NumPy & Pandas

**Frontend:**
- HTML5 & CSS3
- JavaScript (jQuery)
- Responsive Design

**Deployment:**
- Nginx (Reverse Proxy)
- Gunicorn (WSGI Server)
- AWS EC2 (Ubuntu 24.04)
- Systemd Services

### 🚀 Live Demo

Visit: `http://YOUR_EC2_IP`

### 📸 Preview

![Bangalore House Price Prediction](https://your-screenshot-url.png)

### 🏗️ Architecture

```
Frontend (HTML/CSS/JS)
    ↓
Nginx (Port 80)
    ↓
Flask API (Port 5000)
    ↓
scikit-learn Model
```

### 📦 Installation

**Local Development:**
```bash
cd server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python server.py
```

**EC2 Deployment:**
```bash
git clone https://github.com/BandaruVijay/bangalore-house-price-prediction.git
cd bangalore-house-price-prediction/server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
gunicorn --bind 127.0.0.1:5000 server:app
```

### 📁 Project Structure

```
bangalore-house-price-prediction/
├── client/
│   ├── app.html
│   ├── app.css
│   └── app.js
├── server/
│   ├── server.py
│   ├── util.py
│   ├── requirements.txt
│   └── artifacts/
│       ├── bengalore_home_price_model.pickle
│       └── columns.json
└── README.md
```

### 🔧 Configuration

**Nginx Setup:**
- Serves frontend from `/var/www/bhp`
- Proxies API requests to Flask backend
- Handles SSL (optional with Let's Encrypt)

**Systemd Service:**
- Auto-restart on failure
- Runs as www-data user
- Logs available via `journalctl`

### 📊 Model Details

- **Algorithm**: Linear Regression / Ridge Regression
- **Training Data**: Bangalore housing dataset
- **Features**: Area, BHK, Bath, Location
- **Accuracy**: [Your model accuracy %]

### 🤝 Contributing

Feel free to fork and submit pull requests!

### 📝 License

MIT License - feel free to use this project!

### 👨‍💻 Author

[Your Name] - [Your GitHub](https://github.com/BandaruVijay)

---

**Made with ❤️ for Real Estate Predictions**

##### "git commands"
git add README.md
git commit -m "Add comprehensive README with project details"
git push origin main
