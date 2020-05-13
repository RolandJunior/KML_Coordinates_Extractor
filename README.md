# KML_Coordinates_Extractor
Python program to extract coordinates from a KML file.

* Extracts coordinates only from 'pins' (tag "Point").

* Input file must be:
  * named "input.kml".
  * placed in the same path as ".py".
  * in KML format (KMZ not supported).

* Output file will be:
  * named "output.txt".
  * created in the same path as ".py".
  * overwritten if it already exists.
  * in CSV format.
