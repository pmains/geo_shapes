from pyproj import Proj, transform
import shapefile
import simplekml

def esri_to_geo(*points):
    # ArcGIS format
    in_proj = Proj(init='epsg:3857')
    # Standard geodetic format
    out_proj = Proj(init='epsg:4326')
    # New array that will hold points in latitude/longitude
    new_points = []
    for point in points:
        x2, y2 = transform(in_proj, out_proj, point[0], point[1])
        # Append points as tuples
        new_points.append((x2, y2))
    return new_points

def main():
    # Read in all precincts
    sf = shapefile.Reader("VotingPrecincts.shp")
    shape_records = sf.shapeRecords()
    
    # Find Gilbert Gardens (Precinct 251)
    for i in xrange(len(shape_records)):
        sr = shape_records[i]
        if 'GILBERT GARDENS' in sr.record:
            break
    
    # Create KML file
    kml = simplekml.Kml()
    kml.newpolygon()
    poly = kml.features[0]
    # Convert points
    pts = esri_to_geo(*sr.shape.points)
    poly.outerboundaryis = pts
    kml.save("Arf.kml")

if __name__ == "__main__":
    main()
