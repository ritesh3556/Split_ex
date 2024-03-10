
# Expense Sharing Application

The Expense Sharing Application is a web-based platform designed to simplify the process of managing expenses and splitting costs among a group of users. It allows users to add expenses, split them equally or based on specific amounts or percentages, and keep track of balances between participants.

## Features

- **User Management**: Users can sign up, log in, and manage their profiles.
- **Expense Management**: Users can add expenses, specify the type of expense (equal, exact, or percentage), and select participants.
- **Balance Calculation**: The application automatically calculates and updates balances between users based on their expenses and payments.
- **Email Notifications**: Users receive email notifications when they are added to an expense, containing details of the expense and the amount they owe.
- **Scheduled Reminders**: Weekly email reminders are sent to users containing their total outstanding balances.
- **API Endpoints**: RESTful API endpoints are available for managing users, expenses, and balances.

## Technologies Used

- **Django**: Backend framework for building the application.
- **Django REST Framework**: Used for building RESTful APIs.
- **SQLite**: Lightweight relational database management system for storing application data.
- **JWT Authentication**: JSON Web Tokens for user authentication.
- **HTML/CSS/JavaScript**: Frontend technologies for building user interfaces.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/expense-sharing-app.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the development server:

```bash
python manage.py runserver
```

4. Access the application in your web browser at `http://localhost:8000`.

## API Documentation

The API documentation can be found at `/api/docs/` after starting the server. It provides detailed information about available endpoints, request parameters, and response formats.

## Usage

1. Sign up or log in to the application.
2. Add expenses by specifying the amount, type, and participants.
3. View balances to see how much each user owes or is owed by others.
4. Receive email notifications for new expenses and weekly reminders.
5. Use the provided API endpoints for programmatic access to application features.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Be sure to follow the contribution guidelines and maintain code quality and test coverage.

## License
