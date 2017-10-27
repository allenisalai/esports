#!/bin/sh
set -e

for filename in Replays/*.StormReplay; do
  file=${filename:8}
  file=${file%".StormReplay"}
  mkdir -p "/hots_output/$file"
  python Protocol/heroprotocol.py --details "$filename" > "/hots_output/$file/player_details.json"
  python Protocol/heroprotocol.py --messageevents "$filename" > "/hots_output/$file/message_events.json"
done

for filename in /hots_output/*/*; do
  echo $filename
done
