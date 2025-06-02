#===========================================================
# Session Related Functions
#===========================================================

from dotenv import load_dotenv
import os


#-----------------------------------------------------------
# Load the session key from .env and set it for the app
#-----------------------------------------------------------
def init_session(app):
    load_dotenv()
    SESSION_KEY = os.getenv("SESSION_KEY")
    app.secret_key = SESSION_KEY
