# ⚡ ChargeFuel — On-Demand Fuel & EV Charging Delivery Platform

A full-stack web application built with **Django** that connects customers with fuel and EV charging services. Customers can order fuel delivery or request EV charging at their location, while the company manages all orders through a dedicated admin dashboard.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About the Project

**ChargeFuel** is a service platform that allows customers to:
- Register and manage their account
- Order fuel delivery (petrol/diesel) right to their doorstep
- Request EV (Electric Vehicle) charging at their location
- Submit complaints and feedback
- Contact support

The company side provides a separate portal to:
- View and manage all incoming orders (fuel & EV charging)
- Handle customer complaints
- Read customer feedback and contact messages
- View all registered customers

---

## ✨ Features

### 👤 Customer Portal
| Feature | Description |
|---|---|
| **Sign Up / Login** | Register a new account with full profile details or log in with ID & password |
| **Customer Dashboard** | Central hub for accessing all customer services |
| **Order Fuel** | Order petrol or diesel delivery with quantity, fuel type, and drop location |
| **Order EV Charging** | Request mobile EV charging service at a specified location |
| **Submit Complaint** | Raise a complaint against an order with real-time status tracking |
| **Leave Feedback** | Submit feedback/reviews about the service |
| **Contact Us** | Send queries directly to the company |
| **Account Settings** | Change password securely |
| **Delete Account** | Permanently remove account after verification |

### 🏢 Company Portal
| Feature | Description |
|---|---|
| **Company Login** | Secure login for company staff |
| **Company Dashboard** | Overview of all company operations |
| **View Fuel Orders** | See all customer fuel delivery orders |
| **View EV Orders** | See all EV charging requests |
| **Manage Complaints** | View all customer complaints and their statuses |
| **View Feedback** | Browse all customer feedback |
| **View Customers** | Access full list of registered customers |
| **View Contact Queries** | Read messages sent through the contact form |
| **Company Settings** | Change company account password |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.x, Django 5.2 |
| **Database** | SQLite3 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Templating** | Django Template Language (DTL) |
| **Server** | Django Development Server (WSGI) |

---

## 📁 Project Structure

```
ChargeFuel/
│
├── ChargeFuel/               # Django project configuration
│   ├── settings.py           # Project settings
│   ├── urls.py               # Root URL configuration (all routes)
│   ├── wsgi.py               # WSGI entry point
│   └── asgi.py               # ASGI entry point
│
├── development/              # Main Django app
│   ├── views.py              # All view functions (customer + company logic)
│   ├── models.py             # Django models
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── migrations/           # Database migrations
│   └── static/
│       └── images/           # Static image assets
│
├── templates/                # HTML templates (23 pages)
│   ├── index.html            # Home page
│   ├── about.html            # About page
│   ├── services.html         # Services page
│   ├── contact.html          # Contact page
│   ├── signup.html           # Customer signup
│   ├── login.html            # Customer login
│   ├── customerdashboard.html # Customer dashboard
│   ├── order.html            # Order selection
│   ├── orderev.html          # Order EV charging
│   ├── orderfuel.html        # Order fuel delivery
│   ├── feedback.html         # Customer feedback
│   ├── complain.html         # Submit complaint
│   ├── settings.html         # Customer settings
│   ├── accounts.html         # Account management
│   ├── company.html          # Company login
│   ├── companydashboard.html # Company dashboard
│   ├── companysettings.html  # Company settings
│   ├── companyorderfuel.html # Company view fuel orders
│   ├── companyorderev.html   # Company view EV orders
│   ├── companycomplain.html  # Company manage complaints
│   ├── companyfeedback.html  # Company view feedback
│   ├── companycustomers.html # Company view customers
│   └── companycontact.html   # Company view contact queries
│
├── db.sqlite3                # SQLite database
└── manage.py                 # Django management script
```

---

## 🗄️ Database Schema

The project uses **SQLite3** with the following tables:

| Table | Description | Key Columns |
|---|---|---|
| `customersignup` | Registered customers | `Id`, `Password`, `Fullname`, `Address`, `City`, `Contact`, `Gender`, `DOB`, `Email` |
| `companylogintable` | Company staff accounts | `ID`, `Password` |
| `customerorderfueltable` | Fuel delivery orders | `ID`, `Fuelcategory`, `fueltype`, `quantity`, `droplocation`, `contact` |
| `orderevchargingtable` | EV charging requests | `customerid`, `droplocation`, `contact` |
| `customercomplaintable` | Customer complaints | `customerid`, `orderid`, `dateofcomplain`, `complainstatus`, `complain` |
| `feedbacktable` | Customer feedback | `id`, `feedback` |
| `contacttable` | Contact form entries | `fnm`, `city`, `contact`, `query` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ChargeFuel.git
   cd ChargeFuel
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS / Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Navigate to the project directory**
   ```bash
   cd ChargeFuel
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Set up the SQLite database tables**

   Open Django shell or use DB Browser for SQLite to create the required tables:
   ```sql
   CREATE TABLE IF NOT EXISTS customersignup (
       Id TEXT PRIMARY KEY,
       Password TEXT,
       Fullname TEXT,
       Address TEXT,
       City TEXT,
       Contact TEXT,
       Gender TEXT,
       DOB TEXT,
       Email TEXT
   );

   CREATE TABLE IF NOT EXISTS companylogintable (
       ID TEXT PRIMARY KEY,
       Password TEXT
   );

   CREATE TABLE IF NOT EXISTS customerorderfueltable (
       ID TEXT,
       Fuelcategory TEXT,
       fueltype TEXT,
       quantity TEXT,
       droplocation TEXT,
       contact TEXT
   );

   CREATE TABLE IF NOT EXISTS orderevchargingtable (
       customerid TEXT,
       droplocation TEXT,
       contact TEXT
   );

   CREATE TABLE IF NOT EXISTS customercomplaintable (
       customerid TEXT,
       orderid TEXT,
       dateofcomplain TEXT,
       complainstatus TEXT,
       complain TEXT
   );

   CREATE TABLE IF NOT EXISTS feedbacktable (
       id TEXT,
       feedback TEXT
   );

   CREATE TABLE IF NOT EXISTS contacttable (
       fnm TEXT,
       city TEXT,
       contact TEXT,
       query TEXT
   );
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 🧭 Usage

### Customer Flow
1. Visit the home page and click **Sign Up** to register
2. **Log in** with your User ID and password
3. From the **Customer Dashboard**, choose:
   - **Order Fuel** → select fuel type and enter delivery location
   - **Order EV Charging** → enter your location for EV service
   - **Complaint** → raise an issue against a previous order
   - **Feedback** → share your experience
   - **Settings** → change your password
   - **Accounts** → delete your account

### Company Flow
1. Navigate to `/companylink` or click the Company Login link
2. Log in with company credentials
3. From the **Company Dashboard**, access:
   - Fuel Orders, EV Orders, Complaints, Feedback, Customers, and Contact queries

---

## 🌐 URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `homefun` | Home page |
| `/aboutlink` | `aboutfun` | About page |
| `/serviceslink` | `servicesfun` | Services page |
| `/contactlink` | `contactfun` | Contact page |
| `/signuplink` | `signupfun` | Customer signup form |
| `/loginlink` | `loginfun` | Customer login form |
| `/customerdashboardlink` | `customerdashboardfun` | Customer dashboard |
| `/orderlink` | `orderfun` | Order selection |
| `/orderevlink` | `orderevfun` | Order EV charging |
| `/orderfuellink` | `orderfuelfun` | Order fuel delivery |
| `/feedbacklink` | `feedbackfun` | Feedback form |
| `/complainlink` | `complainfun` | Complaint form |
| `/settingslink` | `settingsfun` | Customer settings |
| `/accountslink` | `accountsfun` | Account management |
| `/companylink` | `companyfun` | Company login |
| `/companydashboardlink` | `companydashboardfun` | Company dashboard |
| `/companysettingslink` | `companysettingsfun` | Company settings |
| `/loadcomplainlink` | `loadcomplainfun` | View complaints (company) |
| `/loadorderfuellink` | `loadorderfuelfun` | View fuel orders (company) |
| `/loadorderevlink` | `loadorderevfun` | View EV orders (company) |
| `/companyfeedbacklink` | `companyfeedbackfun` | View feedback (company) |
| `/companycustomerslink` | `companycustomersfun` | View customers (company) |
| `/companycontactlink` | `companycontactfun` | View contact queries (company) |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add: your feature description"`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open a Pull Request**

---

## ⚠️ Important Notes

> **Security**: This project uses `DEBUG = True` and a hardcoded `SECRET_KEY` which is suitable for **development only**. Before deploying to production:
> - Set `DEBUG = False`
> - Move `SECRET_KEY` to environment variables
> - Configure `ALLOWED_HOSTS`
> - Use a production-ready database (e.g., PostgreSQL)
> - Implement Django's built-in authentication system for more robust security

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Developed as a Django web application project demonstrating full-stack development with Python, Django, SQLite, and HTML/CSS.

---

> ⚡ *ChargeFuel — Bringing Energy to Your Doorstep*
