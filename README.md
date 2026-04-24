# Civic Catalyst (DMSS) 

**Civic Issue Reporting and Resolution System**

Civic Catalyst is a premium web application built to streamline the reporting, tracking, and resolution of civic issues. It offers a modern, responsive, and dynamic user interface with powerful role-based features.

🚀 **Live Demo:** https://civic-catalyst.onrender.com

## Features
- **Issue Reporting**: Users can report civic issues with image uploads and built-in voice-to-text form support.
- **Interactive Mapping**: View reported issues dynamically on an interactive map using Leaflet & OpenStreetMap.
- **Role-based Authentication**: Distinct dashboards and access levels for Users, Staff, and Admins.
- **Admin & Staff Dashboards**: Comprehensive issue tracking, member management, and the ability to update resolution statuses.
- **Modern UI**: Clean and premium aesthetic featuring glassmorphism, responsive design, and smooth animations.

## Tech Stack
- **Backend:** Python, Django
- **Database:** MongoDB
- **Frontend:** HTML, Tailwind CSS, Vanilla JavaScript (including Web Speech API)
- **Mapping:** Leaflet.js, OpenStreetMap
- **Cloud Storage:** Cloudinary (for media uploads)
- **Deployment:** Render

## Testing the Application

The application is fully deployed and can be tested directly without any local installation! 

1. **Visit the live site:** https://civic-catalyst.onrender.com
2. **Login to the Admin Dashboard** to view all issues, update statuses, or manage community members using the credentials below:

### Testing Credentials
- **Email:** `admin@civic.com`
- **Password:** `admin123`

---

## Local Setup & Installation (Optional)

If you wish to run or develop the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShivamJoshi7906/CIVIC_CATALYST.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup:**
   Create a `.env` file for your configuration containing your database URI and Cloudinary details.

4. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Default Admin:**
   ```bash
   python create_admin.py
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```
