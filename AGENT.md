# AGENT.md

Entry for make.fun competition `u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9`
("The GPS Swears It Was a Shortcut").

## What it does

`main.py` (Python 3, standard library only) writes a single line of plain
text — the GPS's own excuse for sending the driver down the wrong road — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## The line

> The map said that lake was a road, and I stand by it; you got here early,
> you're just finishing the last hundred metres by swimming.

The GPS speaks in its own voice: smug, defensive, blaming the map, with a
fresh specific detail (the lake) and a twist in the final words instead of
the usual "recalculating" joke.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
