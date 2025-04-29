'''
Jmoody
4.2025 Wk 12 Tool Development 8 - whereisit.py
Citation: Python for Networking & Security vol 3 - JOrtega
Usage: Command to run the script (if running from directory where script is located):
run in a different terminal: python whereisit.py whereisit.jpg
'''

import argparse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import sys

#Extracts the GPS tags from the EXIF metadata
def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    #Loops through all the EXIF tags to find GPS info
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            #Mapping GPS tags to human readable names by using GPSTAGS
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging
#Converts the coordinates from degrees, minutes and seconds to decimal degrees
def dms_to_dd(d, m, s, ref):
    decimal_degrees = d + float(m)/60 + float(s)/(60*60)
    #The south and west cords become negative in decimal degrees
    if ref in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

#Is extracting the Lat and Long Exif metadata
def extract_gps_coords(exif_data):
    geotags = get_geotagging(exif_data)
    if not geotags:
        return None, None
    #Converts the Lat and Long from DMS to DD
    latitude = dms_to_dd(geotags['GPSLatitude'][0], geotags['GPSLatitude'][1], geotags['GPSLatitude'][2], geotags['GPSLatitudeRef'])
    longitude = dms_to_dd(geotags['GPSLongitude'][0], geotags['GPSLongitude'][1], geotags['GPSLongitude'][2], geotags['GPSLongitudeRef'])

    return latitude, longitude

#Main function that will pars the arguments and display the GPS data
def main():
    #Sets up the srgument parser so it will accept the file as an input
    parser = argparse.ArgumentParser(description='Metadata from images')
    parser.add_argument('PICTURE_FILE', help='path to the file image')
    args = parser.parse_args()

    #Opens image and extracts EXIF data
    img_file = Image.open(args.PICTURE_FILE)
    exif_data = img_file._getexif()

    if exif_data is None:
        print("No EXIF data found")
        sys.exit()

    #Extracts and Prints the GPS Cords
    latitude, longitude = extract_gps_coords(exif_data)

    if latitude is not None and longitude is not None:
        print("GPS Coordinates: {}, {}".format(latitude, longitude))
        gmaps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print("Google Maps URL: {}".format(gmaps_url))

if __name__ == "__main__":
    main()
