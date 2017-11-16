from flask import Flask
import json
import io

app = Flask(__name__)

@app.route("/")
def hello():
    #thawed = jsonpickle.decode(read('/hots_output/Tomb_of_the_Spider_Queen/details.json'))
    file = open('/hots_output/Tomb_of_the_Spider_Queen/details.json')

    details = json.loads(file.read())
    player_names = [];
    #for player in details['m_playerList']
    #    player_names.append(player['m_name'])

    return json.dumps(player_names)

if __name__ == "__main__":
    app.run(debug=true, host='0.0.0.0', port=9090)
