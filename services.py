import click
import json
from models import Player
from terminaltables import AsciiTable

class TrackedEventParser():
    def __init__(self, protocol, archive, player_list):
        self.protocol = protocol
        self.archive = archive
        self.player_list = player_list

    def getPopulatedPlayerList(self):
        score_event = self.findScoreReultEvent()

        for stats in self.getTrackedStatsForPlayer(score_event):
            self.player_list.populatePlayerStats(stats)

        return self.player_list

    def getTrackedStatsForPlayer(self, score_event):
        tracked_stats = self.getTrackedStatSet()
        for instance in score_event["m_instanceList"]:
            if instance["m_name"] in tracked_stats:
               yield instance

    def findScoreReultEvent(self):
        for event in self.getEvents():
            if event["_event"] == "NNet.Replay.Tracker.SScoreResultEvent":
                return event

    def getEvents(self):
        if hasattr(self.protocol, 'decode_replay_tracker_events'):
            contents = self.archive.read_file('replay.tracker.events')
            return self.protocol.decode_replay_tracker_events(contents)
        else:
            return []

    def getTrackedStatSet(self):
        return ("Takedowns", "TimeSpentDead",
                 "SelfHealing", "MercCampCaptures",
                "TeamfightHeroDamage", "Healing Assists",
                "StructureDamage", "CreepDamage", "ProtectionGivenToAllies", "MinionDamage")


class PlayerList():
    def __init__(self):
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def setPlayerStat(self, player_index, stat_key, stat_value):
        self.players[player_index].setStat(stat_key, stat_value)

    def populatePlayerStats(self, stats):
        stat_name = stats["m_name"]
        index = 0
        for values in stats["m_values"]:
            if len(values) == 1 :
                self.setPlayerStat(index, stat_name, values[0]["m_value"])
            index = index + 1

    def getPlayerListStatTable(self):
        stat_headers = ["Takedowns", "StructureDamage", "MercCampCaptures", "TimeSpentDead"]
        columns = ["Player"] + stat_headers

        table_data = [columns]
        for p in self.players:
            player_data = [p.getPlayerName()]
            for stat in stat_headers:
                player_data.append(p.stats[stat])
            table_data.append(player_data)

        return AsciiTable(table_data)

    @staticmethod
    def createPlayerListFromReplayDetails(replay_details):
        player_list = PlayerList()
        for p in replay_details["m_playerList"]:
            player = Player()
            player.username = p["m_name"]
            player.color = 'blue' if p["m_color"]["m_b"] == 255 else 'red'
            player.hero = p["m_hero"]
            player_list.addPlayer(player)
        return player_list
