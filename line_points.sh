#!/usr/bin/env bash

source venv/bin/activate

mkdir -p line_points_coord
mkdir -p line_points_png

for i in {1..4} {6..8} 11 21 ; do
    python3 color-convert.py -i line_bg_png/line$i.png
    python3 detect_shapes.py -i result.png > line_points_coord/line$i.txt
    mv result.png line_points_png/line$i.png
done
    
