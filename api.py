from flask import Flask, request
from anal.anal_type import AnalType
from fetch.fetch_novel import FetchNovel


anal_type = AnalType()
fetch_novel = FetchNovel(sub_folder="rank_book_info")
app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    return response


@app.route("/fetch/novel")
def app_fetch_novel():
    choose = request.args.get("choose")
    count = int(request.args.get("count"))
    info = fetch_novel.fetch(choose=choose, count=count)
    return info


@app.route("/anal/type")
def app_anal_type():
    shape = request.args.get("shape")
    draw = anal_type.anal(shape=shape)
    return draw.dump_options_with_quotes()


app.run(debug=True)
