# 📧 Email Tracking System

A Django-based email tracking system that detects when recipients open emails using tracking pixels.

Built to provide insights into email engagement and open activity.

---

## 🚀 Features

- Send emails with tracking pixel
- Detect email opens
- Store timestamp of email activity
- Unique tracking for each email
- Dashboard to monitor email status
- Real-time tracking mechanism

---

## 🧠 How It Works

The system embeds a tiny invisible tracking image inside emails.

When the recipient opens the email:
1. The tracking pixel loads
2. A request is sent to the server
3. The server records:
   - Open status
   - Timestamp
   - Tracking ID

This allows the sender to know whether the email was viewed.

---

## 🛠️ Tech Stack

- Python
- Django
- SQLite
- HTML/CSS
- Gmail SMTP
- Tracking Pixel Logic



## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/email-tracking-system.git
```

### 2. Move into project folder

```bash
cd email-tracking-system
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```
Live link-https://lnkd.in/gTyUCYx8

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run server

```bash
python manage.py runserver
```

---

## 📌 Future Improvements

- Email analytics dashboard
- Click tracking
- Attachment tracking
- Real-time notifications
- Multiple email provider support

---


