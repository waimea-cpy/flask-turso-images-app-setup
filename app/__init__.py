#===========================================================
# App Creation and Launch
#===========================================================

from flask import Flask, render_template, request, flash, session, redirect, send_file
from app.db import init_db, connect_db, handle_db_errors
from app.errors import register_error_handlers
from app.errors import server_error
import html
import io


# Create the app
app = Flask(__name__)

# Create a session for messages, etc.
app.secret_key = "your-secret-key"

# Handle 404 and 500 errors
register_error_handlers(app)

# Setup the database
init_db(app)


#-----------------------------------------------------------
# Home page route
#-----------------------------------------------------------
@app.get("/")
def index():
    return render_template("pages/home.jinja")


#-----------------------------------------------------------
# About page route
#-----------------------------------------------------------
@app.get("/about/")
def about():
    return render_template("pages/about.jinja")


#-----------------------------------------------------------
# Things page route - Show all the things, and new thing form
#-----------------------------------------------------------
@app.get("/things/")
@handle_db_errors
def show_all_things():
    with connect_db() as client:
        # Get all the things from the DB
        sql = "SELECT * FROM things ORDER BY name ASC"
        result = client.execute(sql)
        things = result.rows

        # And show them on the page
        return render_template("pages/things.jinja", things=things)


#-----------------------------------------------------------
# Thing page route - Show details of a single thing
#-----------------------------------------------------------
@app.get("/thing/<int:id>")
@handle_db_errors
def show_one_thing(id):
    with connect_db() as client:
        # Get the things from the DB
        sql = "SELECT * FROM things WHERE id=?"
        values = [id]
        result = client.execute(sql, values)

        # Did we get a result?
        if result.rows:
            # yes, so show it on the page
            thing = result.rows[0]
            return render_template("pages/thing.jinja", thing=thing)

        else:
            # No, so show error
            return render_template("pages/404.jinja"), 404


#-----------------------------------------------------------
# Route for adding a thing, using data posted from a form
#-----------------------------------------------------------
@app.post("/add")
@handle_db_errors
def add_a_thing():
    # Get the data from the form
    name  = request.form.get("name")
    price = request.form.get("price")

    # Sanitise the inputs
    name = html.escape(name)
    price = html.escape(price)

    image_file = request.files['image']

    if not image_file:
        return server_error("Problem uploading image")

    image_data = image_file.read()
    mime_type = image_file.mimetype

    with connect_db() as client:
        # Add the thing to the DB
        sql = "INSERT INTO things (name, price, image, mime) VALUES (?, ?, ?, ?)"
        values = [name, price, image_data, mime_type]
        client.execute(sql, values)

        # Go back to the home page
        flash(f"Thing '{name}' added", "success")
        return redirect("/things")


#-----------------------------------------------------------
# Route for deleting a thing, Id given in the route
#-----------------------------------------------------------
@app.get("/delete/<int:id>")
@handle_db_errors
def delete_a_thing(id):
    with connect_db() as client:
        # Delete the thing from the DB
        sql = "DELETE FROM things WHERE id=?"
        values = [id]
        client.execute(sql, values)

        # Go back to the home page
        flash("Thing deleted", "warning")
        return redirect("/things")




@app.route('/image/<int:id>')
def get_image(id):
    with connect_db() as client:
        sql = "SELECT image, mime FROM things WHERE id = ?"
        values = [id]
        result = client.execute(sql, values)

        if result.rows:
            return send_file(
                io.BytesIO(result.rows[0]["image"]),
                mimetype=result.rows[0]["mime"]
            )

        return "Image not found", 404

