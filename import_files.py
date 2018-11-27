#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      151268
#
# Created:     27/11/2018
# Copyright:   (c) 151268 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcinfo
import arcpy, sys, traceback
import os
import xlrd
from arcpy import env

#for file in os.listdir("c:/Users/151268/Documents/BFD/tables/prepped_tables"):
#    if filename.endswith(".csv"):
#        continue
#    else:
#        continue

env.overwriteOutput = True

env.workspace = "c:/Users/151268/Documents/BFD/tables/box_cable_test.gdb"

# create list of all circuit tables
for subdir, dirs, files in os.walk("c:/Users/151268/Documents/BFD/tables/prepped_tables"):
    for file in files:
        filepaths = subdir + os.sep + file

        if filepath.endswith(".csv"):
            print(filepaths)


# Set constants
x_coord = "long"
y_coord = "lat"
sp_ref = arcpy.SpatialReference(2249)

# List circuit numbers, will need to manually change
# Make sure these match up with filenames / csv files
# Perhaps there is a better way?
circuits = range(1,11)
print(circuits)

# Make xy event layer by looping over filepaths
for filepath,circuit in zip(filepaths, circuits):
    arcpy.MakeXYEventLayer_management(filepath, x_coord, y_coord, "event_layer", sp_ref)
    print("circuit " + circuit + " event created")
    arcpy.CopyFeatures_management(event_layer, "points_circuit_" + circuit)
    print("circuit " + circuit + " points created")
    arcpy.PointsToLine_management("points_circuit_" + circuit)

# Copy features to geodatabase



