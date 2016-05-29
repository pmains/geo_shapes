from pyproj import Proj, transform
import shapefile
import simplekml

def esri_to_geo(*points):
    in_proj = Proj(init='epsg:3857')
    out_proj = Proj(init='epsg:4326')
    new_points = []
    for point in points:
        x2, y2 = transform(in_proj, out_proj, point[0], point[1])
        new_points.append((x2, y2))
    return new_points

def main():
    sf = shapefile.Reader("VotingPrecincts.shp")
    shape_records = sf.shapeRecords()

    for i in xrange(len(shape_records)):
        sr = shape_records[i]
        if 'GILBERT GARDENS' in sr.record:
            break
    
    kml = simplekml.Kml()
    kml.newpolygon()
    poly = kml.features[0]
    pts = coords.esri_to_geo(*sr.shape.points)
    poly.outerboundaryis = pts
    kml.save("Arf.kml")

if __name__ == "__main__":
    main()
