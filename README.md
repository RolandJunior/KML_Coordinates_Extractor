# KML_Coordinates_Extractor
Python program to extract coordinates from a KML file.

* Input file must be:
  * named "input.kml";
  * placed in the same path as ".py";
  * in KML format (KMZ not supported).

* Output files will be:
  * named "output_###.txt", according with the element type;
  * created in the same path as ".py";
  * overwritten if they already exists;
  * in CSV format.

* Known issues:
  * Only extract coordinates from "Point", "LineString" and "Polygon" elements;
  * Doesn't extract 3D information.
