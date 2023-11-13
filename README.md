# Flask Tic Tac Toe Server

This Flask application serves as the backend for a Tic Tac Toe game. It uses Flask-SocketIO for real-time communication and is designed to work with a separate frontend.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10
- Pipenv

## Setup

1. Clone the Repository
   
   `git clone https://github.com/benbenbuhben/CS506-IP-backend.git`
   
   `cd CS506-IP-backend`

2. Install Dependencies
   Use pipenv to install the required packages:

   `pipenv install`

3. Activate the Virtual Environment

   `pipenv shell`

4. Set Environment Variables

   Create a .env file in the root directory of the project and add the necessary environment variables:

   ```
   SECRET_KEY=[Your Secret Key]
   PORT=5001 // Must be synced with frontend
   ```

   Replace [Your Secret Key] with a secret key of your choosing. The `SECRET_KEY` is used by Flask to securely sign the session cookies, protecting the session data from being tampered with. It's also used for security features such as CSRF protection in forms.

## Running the Application

1. Start the Flask Server

   `pipenv run python app.py`

   The server will start on http://localhost:5001 (or on another port if you specified a different one in .env).
