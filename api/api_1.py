# Hands-on sessie
# Flask API's

# Normaal maak je de opdracht in een Jupyter Notebook,
# maar in dit geval is het handiger om een script te gebruiken
# aangezien we een server gaan opzetten. Ook leer je op deze manier
# hoe je de code uit een Jupyter Notebook gestructureerd omzet naar scripts.

# Opdracht 1: Maak een Flask API waaraan opgevraagd kan worden hoe laat het is.
# Om je op weg te helpen is het grootste deel van het script al ingevuld.

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class TimeResource(Resource):
    def get(self):
        ...

api.add_resource(TimeResource, '/api/time')

if __name__ == '__main__':
    app.run(debug=True)

# Opdracht 2: Test je API door het script te starten met "python api_1.py"
# en in je browser te navigeren naar de juiste pagina (wordt geprint in de console).
# Wordt de juiste datum en tijd geprint?

