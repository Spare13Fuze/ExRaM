# Import Required Packages
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



def ECEF2LLA(ecef,model='WGS84'):
    """
    == ECEF XYZ to Lat/Long/Alt for both Spherical and WGS84 Earth ==

    Input:
        ecef (tuple or list): A single array or tuple with (X, Y, Z) coordinates in meters.
                             
        model (str): Earth model to use ('WGS84' or 'SPHERICAL').

    Returns:
        lla (tuple or list): A single array or tuple with (latitude, longitude, altitude).
                             - Latitude in degrees (range: -90 to 90).
                             - Longitude in degrees (range: -180 to 180).
                             - Altitude in meters.
    
    Author: Allen
    Date: 08/09/2024
    
    """
    
    # Define ECEF XYZ Coordinates
    X,Y,Z = ecef

    # Calculate the Longitude
    lon = np.arctan2(Y,X)

    # If the WGS84 Earth is being used...
    if model == 'WGS84':

        # Define Ellipsoidal Constants
        semi_major_axis = 6378137.0
        eccentricity_sqrd = 6.69437999014e-3
        semi_minor_axis = semi_major_axis * np.sqrt(1 - eccentricity_sqrd)

        # Calculate the distance from the Z-axis
        z_axis_dist = np.sqrt(X**2 + Y**2)

        # Make an initial guess for Lat and Alt
        theta = np.arctan2(Z * semi_major_axis,z_axis_dist * semi_minor_axis)
        lat = np.arctan2(Z + eccentricity_sqrd * semi_minor_axis * np.sin(theta)**3, z_axis_dist-eccentricity_sqrd * semi_major_axis * np.cos(theta)**3)
        radius = semi_major_axis / np.sqrt(1-eccentricity_sqrd * np.sin(lat)**2)
        alt = p/np.cos(lat) - radius

        # iteratively improve lat and alt
        lat_prev = lat
        while True:
            radius = semi_major_axis / np.sqrt(1-eccentricity_sqrd * np.sin(lat)**2)
            alt = z_axis_dist / np.cos(lat) - radius
            lat = np.arctan2(Z + eccentricity_sqrd * radius * np.sin(lat), z_axis_dist)
            if abs(lat-lat_prev) < 1e-12:
                break
            lat_prev = lat

    elif model == 'SPHERICAL':
        # Spherical Earth approximation
        radius = 6371000.0  # Average radius of the Earth in meters

        # Calculate latitude and altitude
        z_axis_dist = np.sqrt(X**2 + Y**2)
        lat = np.arctan2(Z, z_axis_dist)
        alt = np.sqrt(X**2 + Y**2 + Z**2) - radius

    else:
        raise ValueError("Invalid Model Specifier. Choose 'SPHERICAL' or 'WGS84'.")

    lat = lat * (180/np.pi)
    lon = lon * (180/np.pi)

    return lat,lon,alt

if __name__ == '__main__':
    
    object_lla = [45,45,0]
    object_ecef = LLA2ECEF(object_lla,'SPHERICAL')
    object_lla_return = ECEF2LLA(object_ecef,'SPHERICAL')
    print(object_ecef)
    print(object_lla_return)
    
