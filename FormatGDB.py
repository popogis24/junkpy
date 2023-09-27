
import arcpy

workspace = arcpy.GetParameterAsText(0)
tool = arcpy.GetParameterAsText(1)

arcpy.env.workspace = workspace

def replace():
    featureclass = arcpy.ListFeatureClasses()
    for fc in featureclass:
        filename = fc
        replace_this = arcpy.GetParameterAsText(1)
        to_this = arcpy.GetParameterAsText(2)
        filename.replace(fr"{replace_this}",fr"{to_this}")

def add_depois():
    featureclass = arcpy.ListFeatureClasses()
    for fc in featureclass:
        filename = fc
        suffix = arcpy.GetParameterAsText(3)
        new_name = filename.replace(fr"{filename}",fr"{suffix}{fc}")
        arcpy.Rename_management(fc, new_name)

def add_antes():
    featureclass = arcpy.ListFeatureClasses()
    for fc in featureclass:
        filename = fc
        prefix = arcpy.GetParameterAsText(4)
        new_name = filename.replace(fr"{filename}",fr"{prefix}{fc}")
        arcpy.Rename_management(fc, new_name)

def title():
    for fc in feature_classes:
        step1_name = f"{fc}_step1"
        casefold_name = step1_name.casefold()
        arcpy.Rename_management(fc, casefold_name)
        remove = casefold_name.replace("_step1","")
        new_name = remove.title()
        arcpy.Rename_management(casefold_name, new_name)
