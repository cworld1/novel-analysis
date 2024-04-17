from flask import Flask, request, send_file
from flask import jsonify
from fetch.fetch_novel import FetchNovel
from fetch.fetch_cover import FetchCover
from fetch.fetch_banner import FetchBanner
from fetch.fetch_character import FetchCharacter
from anal.anal_type import AnalType
from anal.anal_author import AnalAuthor
from anal.anal_comment import AnalComment

fetch_novel = FetchNovel(sub_folder="rank_book_info")
fetch_cover = FetchCover()
fetch_banner = FetchBanner()
fetch_character = FetchCharacter()
anal_type = AnalType()
anal_author = AnalAuthor()
anal_comment = AnalComment()

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    return response


### Fetch basic infos ###


# Fetch novel basic infos
@app.route("/fetch/novel")
# Test example：http://127.0.0.1:5000/fetch/novel?choose=random&count=3
def app_fetch_novel():
    choose = request.args.get("choose")
    count = int(request.args.get("count"))
    return fetch_novel.fetch(choose=choose, count=count)


# Fetch novel cover randomly
@app.route("/fetch/cover")
# Test example：http://127.0.0.1:5000/fetch/cover?&count=3
def app_fetch_cover():
    count = int(request.args.get("count"))
    return fetch_cover.fetch(count=count)


# Fetch banner info
@app.route("/fetch/banners")
# Test example：http://127.0.0.1:5000/fetch/banners
def app_fetch_banner_info():
    return fetch_banner.fetch_banner_info()


# Fetch banner image
@app.route("/fetch/banner")
# Test example：http://127.0.0.1:5000/fetch/banner?id=3
def app_fetch_banner():
    image_id = request.args.get("id")
    file_path = fetch_banner.fetch_banner(image_id)
    return send_file(file_path, mimetype="image/jpeg")


@app.route("/fetch/character")
# Test example：http://127.0.0.1:5000/fetch/character?name=longzu
def app_fetch_character():
    name = request.args.get("name")
    detail_data = fetch_character.fetch(name)
    return jsonify(detail_data)


### Get anal infos ###


# Get anal type echart infos
@app.route("/anal/type")
# Test example：http://127.0.0.1:5000/anal/type?shape=bar
def app_anal_type():
    shape = request.args.get("shape")
    draw = anal_type.anal(shape=shape)
    return draw.dump_options_with_quotes()


# Get anal author echart infos
@app.route("/anal/author")
# Test example：http://127.0.0.1:5000/anal/author?shape=bar
def app_anal_author():
    shape = request.args.get("shape")
    draw = anal_author.anal(shape=shape)
    return draw.dump_options_with_quotes()


# Get anal comment echart infos
@app.route("/anal/comment")
# Test example：http://127.0.0.1:5000/anal/comment?shape=wordcloud
def app_anal_commment():
    shape = request.args.get("shape")
    draw = anal_comment.anal(shape=shape)
    return draw.dump_options_with_quotes()


app.run(debug=True)
