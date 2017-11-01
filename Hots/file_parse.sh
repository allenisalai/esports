#!/bin/sh
set -e

for filename in Replays/*.StormReplay; do
  file=${filename:8}
  file=${file%".StormReplay"}
  mkdir -p "/hots_output/$file"


  for report in "details" "messageevents"; do
    echo $report
    output="/hots_output/$file/$report.json"
    python Protocol/heroprotocol.py "--$report" "$filename" > $output
    echo $output
  done
done

for filename in /hots_output/*/*; do
  echo $filename
done
