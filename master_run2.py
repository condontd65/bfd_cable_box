#-------------------------------------------------------------------------------
# Name:        master_run2
# Purpose:
#
# Author:      151268 - Timothy Condon
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
import glob

env.overwriteOutput = True

env.workspace = "c:/test/test.gdb"

# Create list of all circuit tables
filepaths = glob.glob("c:/Users/151268/Documents/BFD/tables/prepped_tables/*.csv")
print(filepaths)

# Fix backslash problem with filepaths by replacing backlash with forwardslash
filepaths = [f.replace('\\','/') for f in filepaths]
print(filepaths)

# Set constants for use in geospatial functions
x_coord = "long"
y_coord = "lat"
sp_ref = arcpy.SpatialReference(2249)
sort = "circuit_ord"

# List circuit numbers, will need to manually change
# Make sure these match up with filenames / csv files
# Perhaps there is a better way?
circuits = range(1,11)
print(circuits)

# Make xy event layer by looping over filepaths
for filepath,circuit in zip(filepaths, circuits):
    arcpy.MakeXYEventLayer_management(filepath, x_coord, y_coord, "event_layer", sp_ref)
    print("circuit " + filepath + " event created")
    # Now copy point features to workspace geodatabase
    arcpy.CopyFeatures_management("event_layer", "points_circuit_" + str(circuit))
    print("circuit " + str(circuit) + " points created")
    # Now run the points to line tool on all points in geodatabase
    arcpy.PointsToLine_management("points_circuit_" + str(circuit), "lines_circuit_" + str(circuit), Sort_Field = sort)
    print("circuit " + str(circuit) + " lines generated")






