from flask import *
from sqlite3 import *

app = Flask(__name__)


def get_films_info():
    conn = connect('./database/database.db')  # Remplacez "votre_base_de_donnees.db" par le nom de votre base de données SQLite contenant la table "films"
    cursor = conn.cursor()

    # Exécute la requête pour récupérer toutes les informations des films
    cursor.execute("SELECT name, description, annee, real, img, genre, note FROM films")
    rows = cursor.fetchall()

    # Crée un tableau pour stocker les informations des films
    films_info = []

    # Parcourt les résultats et les ajoute au tableau sous la forme d'un dictionnaire
    for row in rows:
        film = {
            "nom": row[0],
            "description": row[1],
            "annee": row[2],
            "real": row[3],
            "img": row[4],
            "genre": row[5],
            "note": row[6]
        }
        films_info.append(film)

    # Ferme la connexion à la base de données
    conn.close()

    return films_info


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', films=get_films_info())


@app.route('/film/<nom>')
def film(nom):
    conn = connect('./database/database.db')
    cursor = conn.cursor()

    # Exécute la requête pour récupérer les informations du film dont le nom est passé en paramètre
    cursor.execute("SELECT * FROM films WHERE name=?", (nom,))
    rows = cursor.fetchall()

    # Crée une variable pour stocker les informations du film
    film = {}

    # Parcourt les résultats et les ajoute au dictionnaire
    for row in rows:
        film = {
            "nom": row[0],
            "description": row[1],
            "annee": row[2],
            "real": row[3],
            "img": row[4],
            "genre": row[5],
            "note": row[6]
        }

    # Ferme la connexion à la base de données
    conn.close()

    return render_template('fiche_film.html', film=film)


if __name__ == '__main__':
    app.run()
