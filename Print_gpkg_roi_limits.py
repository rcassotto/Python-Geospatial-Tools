## Script to read in geopackage and print boundary limits
## Author: Ryan Cassotto
## Date: November 7, 2024


import os
import sys
import glob
import geopandas as gpd


def parse_data_from_gpkg(data):
   ### Parse pertinent data
   geometry = data['geometry']
   minlon = geometry.total_bounds[0]
   minlat = geometry.total_bounds[1]
   maxlon = geometry.total_bounds[2]
   maxlat = geometry.total_bounds[3] 
   crs = geometry.crs
   return minlon, maxlon, minlat, maxlat, crs
    
if __name__ ==  "__main__":

    gpkg_fname = sys.argv[1]
    infile_path= os.getcwd();  
    infile_path_and_filename = os.path.join(infile_path, gpkg_fname)
        
    ## Read in individual .gpkg file
    print('Reading input file: ', infile_path_and_filename)
    data = gpd.read_file(infile_path_and_filename)   
    minlon, maxlon, minlat, maxlat, crs = parse_data_from_gpkg(data)
    
    print(""); print("Coordinate Reference System (CRS): ", crs); print("")
    
    print("Bounding Box:")
    print(minlon,"," ,minlat); print(maxlon,',' , minlat); print(maxlon,',' , maxlat), print(minlon,',' , maxlat)
       
    


    