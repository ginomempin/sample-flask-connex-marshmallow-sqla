from flask import render_template
import config

connex_app = config.connex_app

# Read the OpenAPI specification to configure the endpoints
connex_app.add_api("api.yml")


@connex_app.route("/")
def home():
    """
    This function just responds to the root URL (localhost:5000/).

    :return: The rendered template 'home.html'
    """
    return render_template("home.html")


if __name__ == "__main__":
    connex_app.run(host="0.0.0.0", port=5000, debug=True)
