# COFFEE SHOP

## Overview
This project simulates a simple coffee shop management system using Object-Oriented Programming (OOP) in Python. It includes three main classes:

- Customer
- Coffee
- Order

The relationships between these models are as follows:

- A Customer can have multiple Orders.
- A Coffee can be part of multiple Orders.
- An Order is associated with both a Customer and a Coffee.

## Features
- Customer Management: Create and manage customers, track their orders, and identify the customer who has spent the most on a specific coffee.
- Coffee Management: Create coffee types, track orders for each coffee, and calculate the number of orders and average price for each coffee.
- Order Management: Link customers and coffee with a price, ensuring data integrity and enabling various queries.

## Getting Started
### Requirements
- Python 3.x installed on your machine.
- An IDE or text editor of your choice (such as VS Code, PyCharm, or Sublime Text).

### Installation
1. Clone the Repository

bash
git clone https://github.com/Abdirahmanelyas/python-p3-code-challenge-coffee--shop


cd Phase3-code-challenge-coffee--shop


2. Create a Virtual Environment
bash
python -m venv venv

3. Activate the Virtual Environment
- On Windows:
bash
venv\Scripts\activate

- On macOS/Linux:
bash
source venv/bin/activate


4. Create Project Files and Folders
- Organize your project structure as follows:
css
coffee_shop/
├── models/
│   ├── coffee.py
│   ├── customer.py
│   └── order.py
├── venv/
├── requirements.txt
├── README.md

5. Install Dependencies

There are no external dependencies for this project. If you add any in the future, you can use a requirements.txt file to list them.

## Contributing
Feel free to contribute to this project by submitting issues, pull requests, or suggestions. Please follow standard Git workflow practices.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Abdirahman Elyas](https://github.com/Abdirahman Elyas)