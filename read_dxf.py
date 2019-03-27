import sys
import os
from os.path import isfile, join, splitext
import progressbar
from svgpathtools import svg2paths2
import numpy as np
import argparse

FREECADPATH = '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD
import importDXF
import importSVG

# Parse the commands line arguments
parser = argparse.ArgumentParser(description="Extraction des formes svg depuis un fichier DXF")
parser.add_argument('--input', help="dossier d'entree contenant les dxf", default='in/')
parser.add_argument('--output', help="dossier de sortie pour les svg", default='out/')
parser.add_argument('--convert-to-png', help="convertit les svg en png", action='store_true')
parser.add_argument('--delete-svg', help="supprime tous les svg de sortie", action='store_true')
args = parser.parse_args()

input_path = args.input
output_path = args.output

# List all the DXF files to read
files = [f for f in os.listdir(input_path) if isfile(join(input_path, f))]

obj_with_content = []
obj_with_content_fat = []
coordinates = []

print "---------- Creation des fichiers svg ----------"
for f in files:
    current_filename = splitext(f)[0]

    # Import the DXF with the FreeCad library
    importDXF.open(join(input_path, f))
    doc = FreeCAD.ActiveDocument
    importSVG.export(doc.Objects, join(output_path, 'all_objects_' + current_filename + '.svg'))

    #Display a progress bar
    widgets = [f + ' :', progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]
    pbar = progressbar.ProgressBar(widgets=widgets, maxval=len(FreeCAD.ActiveDocument.Objects))
    pbar.start()

    for i, ob in enumerate(doc.Objects):
        pbar.update(i)

        svg_base_filename = join(output_path, current_filename + '_' + str(i))
        svg_filename = svg_base_filename + '.svg'
        svg_fat_filename = svg_base_filename + 'f.svg'
        importSVG.export([ob], svg_filename)
        paths, attributes, svg_attributes = svg2paths2(svg_filename)

        # Check if the svg consists of only one line
        if not (len(paths) == 1 and len(paths[0]) == 1):
            obj_with_content.append(svg_filename)
            # Create a svg version with bigger paths
            svg_width = float(svg_attributes['width'].replace('mm', ''))
            svg_height = float(svg_attributes['height'].replace('mm', ''))
            pixel_proportion = max(svg_width, svg_height) / 100.0
            obj_with_content_fat.append(svg_fat_filename)
            os.system("sed 's/stroke-width:[0-9]\+.\?[0-9]*/stroke-width:" + \
                      str(pixel_proportion) + "/g' " + svg_filename + " > " + svg_fat_filename)
        else:
            # If the svg consists of only one path remove it
            os.remove(svg_filename)
    pbar.finish()

if args.convert_to_png:
    print "---------- Conversion des fichiers svg en png ----------"
    os.system("mogrify -resize 200x200 -gravity center -extent 200x200^ -format png out/*f.svg")
if args.delete_svg:
    print "---------- Suppression des fichiers svg ----------"
    for o in obj_with_content:
        os.remove(o)
    for o in obj_with_content_fat:
        os.remove(o)
