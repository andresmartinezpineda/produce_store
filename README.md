# Produce Store

Web application for inventory and sales management in a fruit and vegetable store (fruver), developed with **Python** and **Django**. It allows you to manage products, categories, stock, and sales, all through a friendly and responsive web interface.

---

## 🚀 Main Features

- ✅ Create, edit, and delete products  
- 📦 Manage product stock levels  
- 🗂️ Organize by categories  
- 🧾 Register and view sales details  
- 🔍 Dynamic product search with JavaScript  
- 🎨 Custom styles using **Bootstrap** + `fruver_style.css`  
- 👥 System ready for multiple users (extensible)  

---

## 🧑‍💻 Technologies Used

- **Python 3**  
- **Django**  
- **SQLite** (can be adapted to PostgreSQL or MySQL)  
- **HTML5**, **CSS3**, **Bootstrap 5**  
- **Basic JavaScript** for dynamic search  
- **Git** and **GitHub** for version control  

---

## 📂 Project Structure

```
produce-store/
├── products/         # App for product and category management
├── sales/            # App for handling sales
├── templates/        # Custom HTML templates
├── static/           # CSS, JS, icons, and other static files
├── fruver_style.css  # Custom style sheet
├── db.sqlite3        # Local database
├── manage.py
```

---

## 📌 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/andresmartinezpineda/produce-store.git
cd produce-store
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate     # On Linux/Mac
env\Scripts\activate        # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open in your browser:  
   http://127.0.0.1:8000/

---

## 🔒 Admin Panel Access

To create a superuser:

```bash
python manage.py createsuperuser
```

---

## 📈 Project Status

This project is under active development. It is intended as a base for real-world applications and can be extended with user authentication, sales reports, advanced filters, Excel export, and more.

---

## 👨‍🔧 Author

**Andrés Martínez**  
[GitHub - andresmartinezpineda](https://github.com/andresmartinezpineda)

