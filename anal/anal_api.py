from io import BytesIO
from flask import Flask, send_file, request
from matplotlib import pyplot as plt
from anal_type import AnalType


anal_type = AnalType(interaction=False)
app = Flask(__name__)


def save_figure_to_buf(function, shape=None) -> BytesIO:
    buf = BytesIO()
    function(shape, callback=lambda: plt.savefig(buf, format="png"))
    buf.seek(0)
    return buf


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    return response


@app.route("/plot/type")
def plot_type():
    shape = request.args.get("shape")
    buf = save_figure_to_buf(anal_type.anal, shape)
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
