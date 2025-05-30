# A Basic Flask App Linked to a Supabase Database

This is template for a simple [Flask](https://flask.palletsprojects.com) application with a [Turso](https://turso.tech/) SQLite database to store and provide data. The app uses [Jinja2](https://jinja.palletsprojects.com/templates/) templating for structuring pages and data, and [PicoCSS](https://picocss.com/) for styling.

## Project Structure

- **app** folder
    - **db** folder - Files relating to the database
        - **schema.sql** - The SQL to create your database
    - **static** folder - Files to be served as-is
        - **css** folder
            - **styles.css** - A user stylesheet
        - **js** folder
            - **utils.js** - Utility functions
        - **images** folder
            - **icon.svg** - Site favicon
            - *other example images*
    - **templates** folder
        - **components** folder
            - **messages.jinja** - Block to display flash messages
            - *other component templates*
        - **pages** folder
            - **base.jinja** - The base template for all pages
            - *other templates for specific pages*

    - **\_\_init__.py** - App launcher code
    - **db.py** - Functions for database setup and access

- **requirements.txt** - Defines the Python modules needed

- **.env** - Environment variable, e.g. Turso secrets
- **.env-example** - Demo .env file
- **.gitignore** - Prevents venv and .env from being pushed


## Project Setup and Deployment

See [SETUP.md](SETUP.md) for details of how to install and run the app locally for development, how to setup and configure the [Turso](https://turso.tech/) database, and how to deploy the app to [Render](https://render.com/) for hosting.

## Demo Site

A demo of this site is hosted [here](https://flask-turso-basic-app-setup.onrender.com)

*Note: This is a read-only version to avoid the DB being spammed!*
