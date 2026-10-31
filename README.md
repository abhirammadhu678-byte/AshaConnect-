# AshaConnect

AshaConnect is a Django-based healthcare management web platform connecting community health workers (ASHA workers), citizens, and administrators. The platform streamlines mother and child healthcare tracking, vaccination scheduling (prenatal and newborn vaccines), community health records, and administrative oversight.

## Features

- **Guest Portal**: Public homepage, awareness information, registration, and authentication.
- **User / Citizen Portal**: Personal profile management, newborn vaccine records, pregnant women vaccine tracking, and healthcare status.
- **ASHA Worker Portal**: Field updates, community tracking, and healthcare scheduling.
- **Admin Dashboard**: System administration, user/worker management, and reporting.

## Tech Stack

- **Backend**: Python 3, Django 5
- **Database**: SQLite (default / development)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap

## Getting Started

### Prerequisites

- Python 3.10+
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhirammadhu678-byte/AshaConnect-.git
   cd AshaConnect-
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
