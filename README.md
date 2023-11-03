# invoice-gen
Chatbubble invoice generator
Invoice Gen
Invoice Gen is an open-source invoicing web application designed to allow users to easily create, manage, and send invoices. Built with Flask, React, Bootstrap, and PostgreSQL, this project is ideal for developers seeking to dive into full-stack web development and contribute to a growing open-source community.



Features
User Authentication: Register, login, and manage user profiles.
CRUD Operations for Invoices: Create, read, update, and delete invoices with ease.
Template Customization: Customize the layout, branding, and details of your invoices.
PDF Generation: Easily generate a PDF of your invoice for printing or email.
Data Validation: Ensuring the data entered for invoices is valid and correct.
Getting Started
Prerequisites
Python 3.x
PostgreSQL
Node.js and npm (for React and frontend dependencies)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-github-username/invoice-gen.git
cd invoice-gen
Set up a Virtual Environment and Install Backend Dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Install Frontend Dependencies:

bash
Copy code
cd frontend
npm install
Set Up the Database:

bash
Copy code
# Make sure PostgreSQL is running and then:
flask db init
flask db migrate
flask db upgrade
Run the Application:

bash
Copy code
flask run
Contributing
Contributions are welcome! Please read the CONTRIBUTING.md for details on how to contribute.

License
This project is licensed under the MIT

Acknowledgments
Special thanks to all contributors and supporters!
Any third-party libraries or resources you've used.
