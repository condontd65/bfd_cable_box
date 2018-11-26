#-------------------------------------------------------------------------------
# Name:        excel_to_table
# Purpose:
#
# Author:      151268 - Timothy Condon
#
# Created:     26/11/2018
# Copyright:   (c) 151268 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcinfo
import arcpy, sys, traceback
import os
import xlrd
from arcpy import env

env.overwriteOutput = True

env.workspace = "c:/Users/151268/Documents/BFD/tables/box_cable_test.gdb"

#set variables
input_table = "c:/Users/151268/Documents/BFD/tables/cable_test_only2.csv"
x_coord = "long"
y_coord = "lat"
out_layer = "c2_feature_test"
#save_layer = "c2_feature_test.lyr"
save_points = "test_code_points"
out_lines = "test_code_lines"
sp_ref = arcpy.SpatialReference(2249)


#arcpy.ExcelToTable_conversion(input_table,
#    "c:/Users/151268/Documents/BFD/tables/box_cable_test.gdb", "Sheet1")
#print("Table conversion complete")


arcpy.MakeXYEventLayer_management(input_table, x_coord, y_coord, out_layer, sp_ref)
print("Point event generated")

arcpy.CopyFeatures_management(out_layer, save_points)


#arcpy.SaveToLayerFile_management(out_layer, save_layer)

#arcpy.FeatureToPoint_management(out_layer, save_points)
#print("Points generated")

arcpy.PointsToLine_management(save_points, out_lines, Sort_Field = "circuit_ord")
print("Line generated")