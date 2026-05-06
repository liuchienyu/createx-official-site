from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# 假資料（獨立檔案）
from artists_data import ARTISTS


# -------------------------
# Main Pages
# -------------------------
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/artists")
def artists():
    return render_template("artists.html", artists=ARTISTS)


@app.route("/artists/<slug>")
def artist_detail(slug):
    artist = next((a for a in ARTISTS if a["slug"] == slug), None)
    if not artist:
        abort(404)
    return render_template("artist_detail.html", artist=artist)

@app.route("/business")
def business():
    return render_template("business.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# -------------------------
# New Pages (Shop / Member)
# -------------------------
@app.route("/shop")
def shop():
    # 先用「準備中」頁面頂著
    return render_template("coming_soon.html", page_title="商城", page_desc="周邊、票券、合作企劃商品正在上架準備中。")


@app.route("/login")
def login():
    # 先用「準備中」頁面頂著
    return render_template("coming_soon.html", page_title="會員", page_desc="會員系統正在建置中，敬請期待。")


@app.route("/member")
def member():
    # 若你之後做會員中心，可以先導到同一頁
    return render_template("coming_soon.html", page_title="會員中心", page_desc="會員中心功能正在準備中。")


if __name__ == "__main__":
    app.run(debug=True)
