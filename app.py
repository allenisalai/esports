import click
import importlib
from os import listdir
from Protocol import protocol29406
from Protocol.mpyq import mpyq
from models import *
from services import *
import json


@click.command()
@click.option('--directory', help='Firectory of the replays.')

def process_directory(directory):
    replays_files = listdir(directory)
    for file in replays_files:
        replay_file = directory + '/' + file;
        archive = mpyq.MPQArchive(replay_file)

        contents = archive.header['user_data_header']['content']
        header = protocol29406.decode_replay_header(contents)

        # The header's baseBuild determines which protocol to use
        baseBuild = header['m_version']['m_baseBuild']

        try:
            protocol_module = __import__('Protocol', globals(), locals(), ['protocol%s' % (baseBuild,)])
            protocol = getattr(protocol_module,'protocol%s' % (baseBuild,))
        except:
            print >> sys.stderr, 'Unsupported base build: %d' % baseBuild

        contents = archive.read_file('replay.details')
        replay_details = protocol.decode_replay_details(contents)

        player_list = PlayerList.createPlayerListFromReplayDetails(replay_details)
        tracked_events = TrackedEventParser(protocol, archive, player_list)
        player_list = tracked_events.getPopulatedPlayerList()

        click.echo(player_list.getPlayerListStatTable().table)
        # for p in player_list.players:
        #     p.printPlayer()


if __name__ == '__main__':
    process_directory()
