from flask import Flask, request
from anal.anal_type import AnalType


def api(debug=True):
    anal_type = AnalType()
    app = Flask(__name__)

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        return response

    @app.route("/plot/type")
    def plot_type():
        shape = request.args.get("shape")
        draw = anal_type.anal(shape=shape)
        return draw.dump_options_with_quotes()

    app.run(debug=debug)


if __name__ == "__main__":
    api()