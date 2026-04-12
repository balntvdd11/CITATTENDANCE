# ECC Attendance System Documentation

## System Overview

ECC Attendance System is a Django-based web application for laboratory attendance management. It uses Django, Django REST Framework, and elliptic curve cryptography concepts to support secure student registration, QR-based attendance verification, and device-aware login flows.

## Project Description

The application is built for laboratory use in the University of the Assumption and similar educational institutions. It allows administrators to create attendance sessions, generate attendance QR codes, and view attendance reports. Students can register, log in, and verify attendance through browser-based workflows.

## Purpose

The system is designed to automate attendance tracking, reduce manual errors, and improve record accuracy. It supports secure session control, device-aware registration, and signature-based validation to help maintain attendance data integrity.

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Django, Django REST Framework
- Database: SQLite by default; supports `DATABASE_URL` for PostgreSQL or other production databases
- Algorithm: ECC / ECDSA utilities for key generation, signing, and verification

## Deployment

- `Procfile` – process definition for production hosting
- `requirements.txt` – project dependencies
- `build.sh` – deployment automation and build script

## Use Cases

- Laboratory attendance management for universities or training centers
- Teacher-managed session creation and attendance monitoring
- Student attendance registration and verification using browser interaction
- Administrative reporting and attendance export

## Role-Based Access

- Administrators: manage attendance sessions, start/close sessions, generate reports, and view dashboards
- Students: register with device binding, log in, and mark attendance through QR validation

## System Architecture and Components

### Backend

The backend is built using Django and Django REST Framework.

Core backend files:
- `manage.py` – project command utilities
- `db.sqlite3` – default data store for local development

API module:
- `api/models.py` – defines `Student`, `Session`, and `Attendance`
- `api/serializers.py` – converts model instances to JSON payloads
- `api/views.py` – contains authentication, session, attendance, and report logic
- `api/urls.py` – API endpoint routing
- `api/tests.py` – test coverage for business flows
- `api/utils.py` – ECC/ECDSA helper functions for key generation, message signing, and signature verification
- `api/migrations/` – tracks model schema changes

Project configuration:
- `attendance_system/settings.py` – global application settings, CORS, static files, and cookie security
- `attendance_system/urls.py` – top-level URL routing for web and API views
- `attendance_system/middleware.py` – custom middleware for admin cache control and redirects
- `attendance_system/asgi.py` / `attendance_system/wsgi.py` – deployment entry points

### Frontend

The frontend provides user-facing pages and browser interactions.

Templates:
- `attendance_system/templates/index.html` – homepage
- `attendance_system/templates/portal_login.html` – portal login page
- `attendance_system/templates/portal_dashboard.html` – student/admin portal dashboard
- `attendance_system/templates/student_dashboard.html` – student attendance interface
- `attendance_system/templates/student.html` – student portal profile view

Static files:
- `attendance_system/static/css/style.css` – main styling
- `attendance_system/static/js/admin.js` – administrator UI behavior
- `attendance_system/static/js/student-dashboard.js` – student dashboard interactions
- `attendance_system/static/js/student-portal.js` – login and portal functionality

Production-ready static assets are built into `attendance_system/staticfiles/`.

## System Features

- Role-based access control for staff and student portals
- Student registration with ECC public key storage and device fingerprint support
- Session creation with time windows for present, late, and timed-out attendance
- Attendance tracking with time-in/time-out records and status classification
- QR generation and validation endpoints for secure attendance verification
- REST API support for login, registration, session listing, attendance verification, and reporting
- Report export functionality for attendance summaries
- Database migrations to preserve schema and support updates
- Custom middleware for admin security and request handling
- CORS and secure cookie configuration for safe frontend communication

## Web and Device Interaction

The system integrates web and browser/device workflows:

- Web pages provide portal login, student dashboard, and attendance views.
- API endpoints support authentication, QR code generation, QR validation, session management, and report export.
- Students can register with a device fingerprint and public key, enabling device-bound attendance flows.
- ECC utilities in `api/utils.py` enable generation of private/public key pairs, signing messages, and verifying signatures.
- Secure cookie settings and CORS configuration in `attendance_system/settings.py` allow safe browser-based access from local or remote frontends.

## ECC Security and Algorithm Integration

The project includes ECC/ECDSA helper functions for security-related operations. Its current implementation focuses on digital signature generation and verification for attendance and authentication-related workflows.

### Key ECC Concepts

- ECC provides stronger authentication with smaller key sizes.
- ECDSA is used to sign and verify messages, supporting tamper-resistant attendance validation.

### Algorithm Functionality

Implemented in `api/utils.py`, the system supports:
- ECC key pair generation using the NIST P-256 curve
- signature creation for message validation
- signature verification using stored public keys

These utilities help make attendance operations more secure, especially for QR-based verification and device-aware registration.

## Installation and Running

1. Activate your Python environment.
2. Install dependencies from `requirements.txt`.
3. Run database migrations with `python manage.py migrate`.
4. Start the application with `python manage.py runserver`.
5. Open `http://127.0.0.1:8000/` in a browser.

## Conclusion

ECC Attendance System is a Django-based laboratory attendance solution aligned to your project. It combines portal-based attendance workflows, ECC signature utilities, device-aware registration, and report generation to support secure attendance management in laboratory environments.
