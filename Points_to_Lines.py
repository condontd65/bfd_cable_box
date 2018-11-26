#-------------------------------------------------------------------------------
# Name:        Circuit Points to Lines over Large Circuit Counts
# Purpose:     Automate Creating of Circuit Lines
#
# Author:      151268 - Timothy Condon
#
# Created:     31/08/2018
# Copyright:   (c) 151268 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
arcpy.env.overwriteOutput = True

arcpy.env.workspace = "c:/Users/151268/Desktop/TC_FAO/firebox/box_cable_work.gdb"

in_feature_class = 'cable_features'
target_workspace = 'c:/Users/151268/Desktop/TC_FAO/firebox/box_cable_work.gdb'



#Loop through circuit_bin# to get create binary yes/no circuit outputs

#create loop of input fields for splitting attributes of all
fields = [["circuit_bin_1", "circuit_bin_2", "circuit_bin_3", "etc... "]]  #add more info when known (circuit numbers)

#create list of circuit numbers for looping through
circuits = [["1", "2", "3", "ect..."]] #add more info when known (circuit numbers)


#loop through all circuit_binary field numbers to create 1/0 (yes/no) binary feature classes for each circuit
#target_workspace field will need to be a unique geodatabase that will contain a large number of feature classes generated using this step
for field in fields:
     arcpy.SplitByAttributes_analysis(in_feature_class, target_workspace, field)
     print(field + "complete")



#Now looking to Split by Attribute using parallel loop over feature classes and circuit numbers
#target_workspace field will need to be a unique geodatabase that will contain a large number of feature classes generated using this step
#import all split by attribute results in a list
fcs = arcpy.ListFeatureClasses('*_1') #may need to add more info when known or need exact circuit numbers

#create list of fields for ordering, it should match total fcs
orders = [["circuit_ord_1", "circuit_ord_2", "circuit_ord_3", "etc..."]]

#loop through all feature classes and split by attributes through looped ord fields
for fc,order in zip(fcs, ords):
    arcpy.Sort_management(fc, "path/"+fc+"_sort", order)
    print(fc+"complete")



#Run Points to Line on all the sorted feature classes

#create list of feature classes in a list
fcs = arcpy.ListFeatureClasses("*_1_sort") #may need to add more info when known or need exact circuit numbers

for fc,circuit in zip(fcs,circuits):
     arcpy.PointsToLine_management(fc, "path/"+circuit+"_run")
     print(fc+"complete")



#Create identifier field (circuit #) and merge all together

#create list of line feature classes
fcs = arcpy.ListFeatureClasses("*_run") #may need to add more info when known or need exact circuit numbers

#add circuit field before merge by looping over all features
for fc,circuit in zip(fc,circuits):
    arcpy.AddField_management(fc, "Circuit_Val", "SHORT", field_length = 10)
    with arcpy.da.UpdateCursor(fc, "Circuit_Val") as cursor:
        for row in cursor:
            row[0] = circuit
            cursor.updateRow(row)

#create merge and sort outputs, name the output circuits
mergeOutput = r"c:/Users/151268/Desktop/TC_FAO/firebox/box_cable_work.gdb/circuit_raw"
sortOutput = r"c:/Users/151268/Desktop/TC_FAO/firebox/box_cable_work.gdb/circuits"
sort_field = [["Circuit_Val", "ASCENDING"]]

#create merge from all line classes and sort it by circuit number
arcpy.Merge_management(fcs,mergeOutput)
arcpy.Sort_management(mergeOutput, sortOutput, sort_field)

#the output may need to be sorted one more time by order, doublecheck this



























