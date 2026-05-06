from flask import Flask, render_template, abort

from artists_data import ARTISTS
from news_data import NEWS

app = Flask(__name__)


@app.route("/")
def home():
    featured_artists = ARTISTS[:4]
    latest_news = NEWS[:3]

    return render_template(
        "home.html",
        featured_artists=featured_artists,
        latest_news=latest_news
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/artists")
def artists():
    return render_template("artists.html", artists=ARTISTS)


@app.route("/artists/<slug>")
def artist_detail(slug):
    artist = next((item for item in ARTISTS if item.get("slug") == slug), None)

    if artist is None:
        abort(404)

    return render_template("artist_detail.html", artist=artist)


@app.route("/business")
def business():
    return render_template("business.html")


@app.route("/news")
def news():
    return render_template("news.html", news_list=NEWS)


@app.route("/news/<slug>")
def news_detail(slug):
    news_item = next((item for item in NEWS if item.get("slug") == slug), None)

    if news_item is None:
        abort(404)

    return render_template("news_detail.html", news=news_item)


@app.route("/shop")
def shop():
    return render_template(
        "coming_soon.html",
        page_title="商城",
        page_desc="周邊、票券、合作企劃商品正在上架準備中。"
    )


@app.route("/login")
def login():
    return render_template(
        "coming_soon.html",
        page_title="會員",
        page_desc="會員系統正在建置中，敬請期待。"
    )


@app.route("/member")
def member():
    return render_template(
        "coming_soon.html",
        page_title="會員中心",
        page_desc="會員中心功能正在準備中。"
    )


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/healthz")
def healthz():
    return {"status": "ok"}


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("errors/500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)