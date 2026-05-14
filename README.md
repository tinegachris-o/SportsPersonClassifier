# 🏅 Sports Person Classifier

![celeb](./ui.jpg)

A machine learning web app that classifies sports celebrities from images using face and eye detection.

## 🚀 Live Demo

- **Frontend:** [sportspersonclassifier-i1gv.onrender.com](https://sportspersonclassifier-i1gv.onrender.com)
- **Backend API:** [tinegadev-sports-person-classifier.hf.space](https://tinegadev-sports-person-classifier.hf.space)

---

## 🧠 How It Works

1. User uploads an image via the browser
2. Frontend sends the image as base64 to the Flask API
3. OpenCV detects a face with **2 eyes** visible
4. A **Wavelet Transform** extracts features from the face
5. A trained **SVM / ML model** predicts the sports person
6. The result and probabilities are returned to the frontend

---

## 🏋️ Classified Athletes

| Athlete | Sport |
|---------|-------|
| Virat Kohli | Cricket |
| Roger Federer | Tennis |
| Serena Williams | Tennis |
| Maria Sharapova | Tennis |
| Lionel Messi | Football |

---

## 🗂️ Project Structure

```
SportsPersonClassifier/
├── server/
│   ├── artifacts/
│   │   ├── celeb_model.pkl         # Trained ML model
│   │   └── class_dictionary.json  # Label mappings
│   ├── server.py                  # Flask API
│   ├── util.py                    # Image processing & prediction
│   ├── wavelet.py                 # Wavelet transform helper
│   ├── Dockerfile                 # Docker config for HuggingFace
│   └── requirements.txt
├── model/
│   └── ...                        # Training notebooks
├── UI/
│   └── ...                        # Frontend (HTML/CSS/JS)
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript, Dropzone.js |
| Backend | Python, Flask, Flask-CORS |
| ML | Scikit-learn, OpenCV, PyWavelets |
| Deployment (API) | Hugging Face Spaces (Docker) |
| Deployment (UI) | Render (Static Site) |

---

## 🔧 Run Locally

**1. Clone the repo:**
```bash
git clone https://github.com/tinegachris-o/SportsPersonClassifier.git
cd SportsPersonClassifier
```

**2. Install dependencies:**
```bash
cd server
pip install -r requirements.txt
```

**3. Start the Flask server:**
```bash
python server.py
```

**4. Open `UI/app.html`** in your browser.

---

## 📦 API Usage

**Endpoint:** `POST /classify_image`

**Request:**
```
Content-Type: multipart/form-data
image_data: <base64 encoded image>
```

**Response:**
```json
[
  {
    "class": "virat_kohli",
    "class_probability": [12.0, 5.0, 75.0, 4.0, 4.0],
    "class_dictionary": {
      "lionel_messi": 0,
      "maria_sharapova": 1,
      "roger_federer": 2,
      "serena_williams": 3,
      "virat_kohli": 4
    }
  }
]
```

---

## 📄 License

MIT License