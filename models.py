import click
import json

class Player():
    def __init__(self):
        self.username = ''
        self.hero = ''
        self.stats = {}
        self.color = ''

    def setStat(self, stat_key, stat_value):
        self.stats[stat_key] = stat_value

    def getPlayerName(self):
        return self.username + " (" + self.hero + ")"

    def printPlayer(self):
        click.echo(self.getPlayerName())
        click.echo(json.dumps(self.stats))
