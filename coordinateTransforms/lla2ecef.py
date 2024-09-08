import numpy as np

def LLA2ECEF(lla,model='WGS84'):
    """
    == Lat/Long/Alt to ECEF XYZ for both Spherical and WGS84 Earth ==

    Input:
        lla (tuple or list): A single array or tuple with (latitude, longitude, altitude).
                             - Latitude in degrees (range: -90 to 90).
                             - Longitude in degrees (range: -180 to 180).
                             - Altitude in meters.
                             
        model (str): Earth model to use ('WGS84' or 'SPHERICAL').

    Returns:
        tuple: A tuple (X, Y, Z) representing the ECEF coordinates in meters.
    
    Author: Allen
    Date: 08/09/2024

    """
    
    # Define Lat, Long and Alt
    lat,lon,alt = lla

    # Convert the Lat and Long to radians
    lat_rad = lat*(np.pi/180)
    lon_rad = lon*(np.pi/180)

    # If a WGS84 Earth is being used...
    if model == 'WGS84':

        # Define WGS84 Ellipsoid Constants
        semi_major_axis = 6378137.0
        eccentricity_sqrd = 6.69437999014e-3

        # Calculate the radius of curvature (m)
        radius = semi_major_axis/np.sqrt(1-eccentricity_sqrd*np.sin(lat_rad)**2)

        # Calculate the ECEF XYZ Coordinates
        X = (radius + alt) * np.cos(lat_rad)*np.cos(lon_rad)
        Y = (radius + alt) * np.cos(lat_rad)*np.sin(lon_rad)
        Z = ((1 - eccentricity_sqrd) * radius + alt) * np.sin(lat_rad)

    # If a Spherical Earth is being used...
    elif model == 'SPHERICAL':

        # Define Spherical Earth Radius (m)
        radius = 6371000
        
        # Calculate the ECEF XYZ Coordinates
        X = (radius + alt) * np.cos(lat_rad)*np.cos(lon_rad)
        Y = (radius + alt) * np.cos(lat_rad)*np.sin(lon_rad)
        Z = (radius + alt) * np.sin(lat_rad)

    else:
        raise ValueError("Invalid Model Specifier. Choose 'SPHERICAL' or 'WGS84'.")

    return X,Y,Z


# Test Wrapper
if __name__ == '__main__':

    object_lla = [45,45,0]
    object_ecef = LLA2ECEF(object_lla,'SPHERICAL')
    print(object_ecef)        
        
    
    
