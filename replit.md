# Potentiam Ltd Employee Management System

## Overview

This is a web-based employee management system for Potentiam Ltd, built with Python Flask backend and vanilla JavaScript frontend. The application provides a simple interface to view and manage employee data with search and filtering capabilities.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Architecture Pattern**: RESTful API
- **Data Storage**: In-memory data structure (Python list/dictionary)
- **CORS**: Enabled for cross-origin requests
- **Session Management**: Flask sessions with configurable secret key

### Frontend Architecture
- **Technology**: Vanilla JavaScript with HTML5 and CSS3
- **UI Framework**: Bootstrap 5 with Replit dark theme for styling
- **Icons**: Font Awesome for iconography
- **Architecture Pattern**: Single Page Application (SPA)
- **API Communication**: Fetch API for backend communication

## Key Components

### Backend Components
1. **Flask Application** (`app.py`):
   - Main application entry point
   - Employee data management
   - API endpoint definitions
   - CORS configuration

2. **Application Runner** (`main.py`):
   - Development server configuration
   - Host and port settings
   - Debug mode enabled

3. **Employee Data Model**:
   - In-memory storage using Python lists
   - Sample data for 5+ employees
   - Fields: id, name, department, role, email

### Frontend Components
1. **HTML Template** (`templates/index.html`):
   - Responsive layout using Tailwind CSS
   - Employee listing interface
   - Search and filter controls
   - Modal dialogs for employee details

2. **JavaScript Application** (`static/js/app.js`):
   - EmployeeManager class for data management
   - Event handling for user interactions
   - API communication methods
   - DOM manipulation for dynamic content

3. **Custom Styling** (`static/css/style.css`):
   - Enhanced visual effects
   - Smooth transitions
   - Custom scrollbar styling
   - Accessibility improvements

## Data Flow

1. **Page Load**: Frontend fetches employee data from Flask API
2. **Search/Filter**: JavaScript filters data client-side for performance
3. **Employee Details**: Modal displays detailed employee information
4. **Add Employee**: Form submission sends data to backend API
5. **Real-time Updates**: Frontend updates without page refresh

## External Dependencies

### Backend Dependencies
- Flask (web framework)
- Flask-CORS (cross-origin resource sharing)
- Python standard library (os, logging)

### Frontend Dependencies
- Bootstrap 5 with Replit dark theme (via CDN)
- Font Awesome (via CDN)
- Modern browser with ES6 support

## Deployment Strategy

### Development Environment
- Flask development server
- Debug mode enabled
- Hot reload for code changes
- CORS enabled for frontend-backend communication

### Production Considerations
- Environment-based secret key configuration
- Database migration path planned (currently in-memory)
- WSGI server deployment ready
- Static file serving optimization

### Scalability Path
- Database integration (SQLite → PostgreSQL)
- API authentication and authorization
- Employee CRUD operations
- Role-based access control

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- July 06, 2025. Initial setup
- July 06, 2025. Updated with real employee data from Excel file and integrated Bootstrap 5 dark theme