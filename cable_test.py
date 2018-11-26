#-------------------------------------------------------------------------------
# Name:        cable_test
# Purpose:
#
# Author:      151268 - Timothy Condon
#
# Created:     26/11/2018
# Copyright:   (c) 151268 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os
import xlrd

arcpy.env.overwriteOutput = True

arcpy.env.workspace = "c:/Users/151268/Desktop/TC_FAO/firebox/box_cable_test.gdb"

#in_feature_class = 'cable_features'
target_workspace = 'c:/Users/151268/Desktop/TC_FAO/firebox/box_cable_work.gdb'

def importallsheets(in_excel, out_gdb):
    workbook = xlrd.open_workbook(in_excel)
    sheets = [sheet.name for sheet in workbook.sheets()]
    print('{} sheets found: {}'.format(len(sheets), ','.join(sheets)))
    for sheet in sheets:
        # The out_table s based on the input excel filename
        #an underscore seperator followed by the sheet name
        out_table = os.path.join(
            out_gdb,
            arcpy.ValidateTableName(
                "{0}_{1}".format(os.path.basename(in_excel), sheet),
                out_gdb))
        print('Converting {} to {}'.format(sheet, out_table))

        # Perform the conversion
        arcpy.ExcelToTable_conversion(in_excel, out_table, sheet)

if __name__ == '__main__':
    importallsheets('in_file','gdb')