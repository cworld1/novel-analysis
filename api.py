from flask import Flask, request
from anal.anal_type import AnalType
from fetch.fetch_novel import FetchNovel
from fetch.fetch_cover import FetchCover

anal_type = AnalType()
fetch_novel = FetchNovel(sub_folder="rank_book_info")
fetch_cover = FetchCover()
app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    return response


# Test example：http://127.0.0.1:5000/fetch/novel?choose=random&count=3
@app.route("/fetch/novel")
def app_fetch_novel():
    choose = request.args.get("choose")
    count = int(request.args.get("count"))
    info = fetch_novel.fetch(choose=choose, count=count)
    return info


# Test example：http://127.0.0.1:5000/fetch/cover?&count=3
@app.route("/fetch/cover")
def app_fetch_cover():
    count = int(request.args.get("count"))
    covers = fetch_cover.fetch(count=count)
    return covers


# Test example：http://127.0.0.1:5000/anal/type?shape=bar
@app.route("/anal/type")
def app_anal_type():
    shape = request.args.get("shape")
    draw = anal_type.anal(shape=shape)
    return draw.dump_options_with_quotes()


app.run(debug=True)
