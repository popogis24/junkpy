import arcpy


#seta um workspace
arcpy.env.workspace = input('Insira o feature dataset: ')

dataset_23s = fr'C:/...'

#lista todos os features classes dentro do workspace
fcList = arcpy.ListFeatureClasses()

for fc in fcList:
    #reprojeta o feature class para o sistema de coordenadas desejado
    arcpy.management.Project(
    in_dataset=fc,
    out_dataset=dataset_23s+"/"+str(fc)+'_23s',
    out_coor_system='PROJCS["SIRGAS_2000_UTM_Zone_23S",GEOGCS["GCS_SIRGAS_2000",DATUM["D_SIRGAS_2000",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",-45.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    transform_method=None,
    in_coor_system='PROJCS["SIRGAS_2000_UTM_Zone_22S",GEOGCS["GCS_SIRGAS_2000",DATUM["D_SIRGAS_2000",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",-51.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    preserve_shape="NO_PRESERVE_SHAPE",
    max_deviation=None,
    vertical="NO_VERTICAL"
)