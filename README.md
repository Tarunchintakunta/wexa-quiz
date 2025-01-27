Wexa Quiz

Wexa Quiz is a full-stack application that combines a React-based frontend and a Python-based backend with PostgreSQL as the database. The application provides a seamless quiz platform where users can participate in quizzes, track their scores, and enhance their knowledge.

Project Overview

Frontend

The frontend is built using React and Vite, offering a fast and interactive user interface.

Backend

The backend is powered by Python with FastAPI, handling API requests and managing database interactions.

Database

PostgreSQL is used as the database to store user data, quiz details, questions, and results.

Features

Frontend Features

Interactive quizzes on various topics.

Score tracking and display.

Responsive and user-friendly design for seamless navigation.

Backend Features

User Management: Register and authenticate users.

Quiz Management: Create, update, and delete quizzes.

Question Management: Add, edit, and remove quiz questions.

Result Tracking: Store and retrieve quiz results for users.

Installation

Prerequisites

Ensure you have the following installed:

Node.js (for frontend)

Python 3.x (for backend)

PostgreSQL (for database)

Setup Instructions

Backend Setup

Clone the repository:

git clone https://github.com/Tarunchintakunta/wexa-quiz.git
cd wexa-quiz/Backend

Install dependencies:

pip install -r requirements.txt

Configure PostgreSQL:

Update the database configuration in database.py with your PostgreSQL credentials.

Run the script to initialize the database:

python database.py

Start the backend server:

python main.py

The server will run at http://localhost:8000.

Frontend Setup

Navigate to the frontend directory:

cd wexa-quiz/Frontend

Install dependencies:

npm install

Start the frontend server:

npm run dev

The application will be available at http://localhost:3000.

API Endpoints

User Management

POST /users/register: Register a new user.

POST /users/login: Authenticate a user.

Quiz Management

GET /quizzes: Retrieve all quizzes.

POST /quizzes: Create a new quiz.

PUT /quizzes/{id}: Update an existing quiz.

DELETE /quizzes/{id}: Delete a quiz.

Question Management

GET /questions: Retrieve questions for a specific quiz.

POST /questions: Add a question to a quiz.

PUT /questions/{id}: Update a question.

DELETE /questions/{id}: Remove a question.

Result Tracking

POST /results: Submit quiz results.

GET /results/{user_id}: Get results for a specific user.

Contributing

Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch for your changes.

Commit and push your changes.

Open a pull request to the main branch.

