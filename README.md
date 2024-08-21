# my-portfolio

This project represents a portfolio website built using Django and other related technologies.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Docker](#docker-compose-setup)
- [Deployment](#deployment)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/Parsa-SadeghiAsl/my-portfolio.git
   ```

2. Create a virtual environment:
   ```
   python -m venv env
   ```

3. Activate the virtual environment:
   ```
   source env/bin/activate
   ```
   On Windows use:
    ```
   env\Scripts\activate
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up a `.env` file with your configuration variables:
   ```plaintext
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=your-database-url
   ```

6. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a superuser for administrative access (optional):
   ```
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```
   python manage.py runserver
   ```

## Docker Compose Setup

To use Docker Compose, you need to have [Docker](https://www.docker.com/get-started) and [docker-compose](https://docs.docker.com/compose/install/) installed.

1. Create a `docker-compose.yml` file in the root of your project:
   ```yaml
   version: '3.12'
   
   services:
     db:
       image: postgres:latest
       environment:
         POSTGRES_DB: postgres
         POSTGRES_USER: [your-database-user]
         POSTGRES_PASSWORD: [your-database-password]
       ports:
         - "5432:5432"
   
     web:
       build: .
       command: python manage.py runserver 0.0.0.0:8000
       volumes:
         - .:/code
       ports:
         - "8000:8000"
       depends_on:
         - db
   
   networks:
     default:
       driver: bridge
   ```

2. Update your `.env` file with database credentials for Docker Compose:
   ```plaintext
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://[your-database-user]:[your-database-password]@localhost/postgres
   ```

3. Run `docker compose up --build` to start and build the container.

4. Access your site at `http://localhost:8000`. 

## Deployment

For production deployment, consider deploying to a platform like Heroku, AWS, or DigitalOcean.

