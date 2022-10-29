from flask import Flask, request, render_template
from getting_gif import formater, gif_links

app = Flask(__name__)


@app.route('/')
def home():
    return "hello home"

liste_gifs = []
@app.route('/handle', methods=("GET", "POST"))
def rechercher():
    global liste_gifs
    global contenu_requete
    if request.method == "POST":
        contenu_requete = request.form['recherche']
        liste_gifs = formater(gif_links(contenu_requete))
    return render_template("index.html", contenu = liste_gifs)


if __name__ == '__main__':
    app.run(debug=True)
