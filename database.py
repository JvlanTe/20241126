import sqlite3


def get_connection_db():
    conn = sqlite3.connect("pokemon.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    conn = get_connection_db()
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon(
        id INTEGER PRIMARY KEY,

        name TEXT,

        type1 TEXT,

        type2 TEXT,

        height REAL,

        weight REAL,

        generation INTEGER,

        total_stats INTEGER,

        hp INTEGER,

        attack INTEGER,

        defense INTEGER,

        special_attack INTEGER,

        special_defense INTEGER,

        speed INTEGER,

        catch_rate INTEGER,

        is_baby BOOLEAN,

        is_legendary BOOLEAN,

        evolves_from INTEGER,

        image_url TEXT
        )
"""
    )
    conn.commit()
    c.close()


# ポケモン全データを取得する関数
def get_pokemons():
    conn = get_connection_db()
    c = conn.cursor()
    pokemons = c.execute("SELECT * FROM pokemon").fetchall()
    return pokemons


# ポケモンデータをランダムに取得する関数
def randomize_pokemons(number):
    conn = get_connection_db()
    c = conn.cursor()
    pokemons = c.execute("SELECT * FROM pokemon ORDER BY RANDOM() limit ?;", (number,)).fetchall()
    return pokemons


def show_pokemon(id):
    conn = get_connection_db()
    c = conn.cursor()
    pokemon = c.execute("SELECT * FROM pokemon WHERE id = ?;", (id,)).fetchone()
    c.close()
    return pokemon


# ポケモンの名前で検索してデータを取得する関数
def search_pokemon(name):
    conn = get_connection_db()
    c = conn.cursor()
    pokemon = c.execute("SELECT * FROM pokemon WHERE name = ?;", (name,)).fetchone()
    c.close()
    return pokemon


# 指定されたポケモンの検索回数を増加させる関数
def increment_count(id):
    conn = get_connection_db()
    c = conn.cursor()
    c.execute("UPDATE pokemon SET count = count + 1 WHERE id = ?", (id,))
    conn.commit()
    c.close()


# ポケモンの検索ランキングを取得する関数
def get_count():
    conn = get_connection_db()
    c = conn.cursor()
    rankings = c.execute("SELECT name , count FROM pokemon ORDER BY count DESC LIMIT 10").fetchall()
    c.close()
    return rankings


# def random_pick(rp):
#     conn = get_connection_db()
#     c = conn.cursor()
#     pokemon = c.execute("SELCET * FROM pokemon ORDER BY RANDOM() limit 1;").fetchone()
#     retrun pokemon
