#===========================================================
# Error Handling Functions
#===========================================================


from flask import render_template


#-----------------------------------------------------------
# 500 Server error page
#-----------------------------------------------------------
def server_error(message):
    return render_template("pages/500.jinja", error=message), 500


#-----------------------------------------------------------
# Provide error handlers to the Flask app
#-----------------------------------------------------------
def register_error_handlers(app):

    #------------------------------
    # 404 Page not found error page
    @app.errorhandler(404)
    def show_not_found(e):
        return render_template("pages/404.jinja"), 404


    #------------------------------
    # 500 Server error page
    @app.errorhandler(500)
    def show_server_error(e):
        return server_error(str(e))


