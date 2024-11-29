from flask import Flask, render_template, request
from database import get_pokemons, randomize_pokemons, show_pokemon, search_pokemon

app = Flask(__name__)


@app.route("/")
def index():
    pokemons = get_pokemons()
    return render_template("index.html", pokemons=pokemons)


@app.route("/random")
def random():
    pokemons = randomize_pokemons(5)
    return render_template("index.html", pokemons=pokemons)


# @app.route("/random-pick/<int:id>")
# def random_pick():
#     pokemon =


@app.route("/show/<int:id>")
def show(id):
    pokemon = show_pokemon(id)
    return render_template("show.html", pokemon=pokemon)


@app.route("/search")
def search():
    name = request.args.get("name")
    pokemon = search_pokemon(name)
    return render_template("show.html", pokemon=pokemon)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
