# 💰 Django Expense Tracker

A simple and beginner‑friendly **Expense Tracker web application** built using **Django**.
This project allows users to **add, view, and delete daily expenses** with a clean UI and basic styling.

---

## 📌 Features

* ➕ Add daily expenses (amount, description, date)
* 📋 View all expenses in a table
* ❌ Delete an expense
* 🎨 Clean UI with basic CSS styling
* 🧩 Beginner‑friendly Django structure

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite (default Django DB)
* **Frontend:** HTML, CSS

---

## 📂 Project Structure

```
ExpenseProject/
│
├── expense_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tracker/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── add_expense.html
│   └── view.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
```

**Activate:**

* Windows:

```bash
.venv\Scripts\activate
```

* macOS / Linux:

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🖥️ Screens

* **Add Expense Page** – Add daily expense details
* **View Expense Page** – View and delete expenses

*(Screenshots can be added here later)*

---

## 📄 requirements.txt

```
Django>=6.0
```

---

## 🧠 Learning Outcomes

* Django project & app structure
* URL routing and views
* Models and database migrations
* Template rendering with context data
* Basic CRUD operations
* GitHub project setup

---

## 📌 Future Enhancements

* Edit expense feature
* Category‑wise expenses
* Monthly / yearly summary
* Authentication (login/signup)
* Deployment (Render / Railway / PythonAnywhere)

---

## 👩‍💻 Author

**Julienne Brijit Jacob**

B.Tech – CSE-AI

---
