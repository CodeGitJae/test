from flask import Flask, Blueprint, render_template

bp = Blueprint("map", __name__, url_prefix="/map")

@bp.route("/search")
def map_search():
    return render_template("map/kakao_map.html")