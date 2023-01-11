from flask import *

def create_app():
	app = Flask(__name__,template_folder="templates", static_folder="static")
	app.secret_key = "djdksjsgevsjzjhxgsbdbjxzggshsjuxgzh"

	# views
	from .views import views
	app.register_blueprint(views, url_prefix="/")
	
	return app
	
