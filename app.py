import os
import logging
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Enable CORS for all routes
CORS(app)

# Employee data from Potentiam Ltd Excel file
employees_data = [
    {
        "id": 1,
        "name": "Mahesh Reddy",
        "department": "Sales & Marketing",
        "role": "Lead Generation Specialist",
        "email": "mahesh.reddy@potentiam.com"
    },
    {
        "id": 2,
        "name": "Karishma Raj",
        "department": "Human Resources",
        "role": "Technical Recruiter",
        "email": "karishma.raj@potentiam.com"
    },
    {
        "id": 3,
        "name": "Riti Kumari",
        "department": "Finance",
        "role": "Accounts Assistant",
        "email": "riti.kumari@potentiam.com"
    },
    {
        "id": 4,
        "name": "Arpita Priyadarshini",
        "department": "Sales & Marketing",
        "role": "Lead Generation Team Lead",
        "email": "arpita.priyadarshini@potentiam.com"
    },
    {
        "id": 5,
        "name": "Jyestha Tripathy",
        "department": "Human Resources",
        "role": "Talent & HR",
        "email": "jyestha.tripathy@potentiam.com"
    },
    {
        "id": 6,
        "name": "Johnson Patrick",
        "department": "Engineering",
        "role": "Senior Software Developer",
        "email": "johnson.patrick@potentiam.com"
    },
    {
        "id": 7,
        "name": "Ushadeep Poshangari",
        "department": "Engineering",
        "role": "Senior Backend Developer",
        "email": "ushadeep.poshangari@potentiam.com"
    },
    {
        "id": 8,
        "name": "Dipanjan Das",
        "department": "Leadership",
        "role": "Building Potentiam",
        "email": "dipanjan.das@potentiam.com"
    },
    {
        "id": 9,
        "name": "Ankit Bhowmick",
        "department": "Engineering",
        "role": "Data Engineer",
        "email": "ankit.bhowmick@potentiam.com"
    },
    {
        "id": 10,
        "name": "Pooja Kumari",
        "department": "Human Resources",
        "role": "Technical Recruiter",
        "email": "pooja.kumari@potentiam.com"
    },
    {
        "id": 11,
        "name": "Gabriel Lichentanu",
        "department": "Human Resources",
        "role": "Head of Talent Acquisition",
        "email": "gabriel.lichentanu@potentiam.com"
    },
    {
        "id": 12,
        "name": "Imtieyaaz Thebus",
        "department": "Human Resources",
        "role": "Senior Talent Acquisition Specialist",
        "email": "imtieyaaz.thebus@potentiam.com"
    },
    {
        "id": 13,
        "name": "Shafeequr Rahman",
        "department": "Technology",
        "role": "Global Chief Digital Information Officer",
        "email": "shafeequr.rahman@potentiam.com"
    },
    {
        "id": 14,
        "name": "Monica Eckermann",
        "department": "Human Resources",
        "role": "Talent Acquisition Manager",
        "email": "monica.eckermann@potentiam.com"
    },
    {
        "id": 15,
        "name": "Charles Fenton",
        "department": "Leadership",
        "role": "Founder",
        "email": "charles.fenton@potentiam.com"
    }
]

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/employees', methods=['GET'])
def get_employees():
    """Get all employees"""
    try:
        app.logger.info("Fetching all employees")
        return jsonify({
            "success": True,
            "data": employees_data,
            "count": len(employees_data)
        })
    except Exception as e:
        app.logger.error(f"Error fetching employees: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Failed to fetch employees"
        }), 500

@app.route('/api/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """Get a specific employee by ID"""
    try:
        app.logger.info(f"Fetching employee with ID: {employee_id}")
        
        # Find employee by ID
        employee = next((emp for emp in employees_data if emp["id"] == employee_id), None)
        
        if employee:
            return jsonify({
                "success": True,
                "data": employee
            })
        else:
            return jsonify({
                "success": False,
                "error": "Employee not found"
            }), 404
            
    except Exception as e:
        app.logger.error(f"Error fetching employee {employee_id}: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Failed to fetch employee"
        }), 500

@app.route('/api/employees', methods=['POST'])
def add_employee():
    """Add a new employee"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'department', 'role', 'email']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}"
                }), 400
        
        # Generate new ID
        new_id = max(emp["id"] for emp in employees_data) + 1
        
        # Create new employee
        new_employee = {
            "id": new_id,
            "name": data["name"],
            "department": data["department"],
            "role": data["role"],
            "email": data["email"]
        }
        
        employees_data.append(new_employee)
        
        app.logger.info(f"Added new employee: {new_employee}")
        
        return jsonify({
            "success": True,
            "data": new_employee,
            "message": "Employee added successfully"
        }), 201
        
    except Exception as e:
        app.logger.error(f"Error adding employee: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Failed to add employee"
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
