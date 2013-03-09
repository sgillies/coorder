=======
Coörder
=======

The ordering of geospatial coordinates in data that conforms to current OGC
standards varies depending on the coordinate system used. Coörder is here to
help!

Let's say you parse the coordinates in a GeoRSS feed or GML document into
a sequence of tuples. Is the first item in the tuple the latitude or the
longitude? It depends on the coordinate reference system (CRS) chosen by the
producer. Geographic, unprojected, coordinate systems listed by number in the
EPSG table have latitude-longitude order. Some non-EPSG standard CRS have
longitude-latitude order. The ``coorder.is_latlng`` function aims to sort these
cases out and help determine whether, for example, coordinate order needs to be
flipped when converting GeoRSS or GML elements to GeoJSON.

Usage
=====

.. code-block:: python

  >>> from coorder import is_latlng
  >>> print is_latlng('urn:ogc:def:crs:EPSG::4326')
  True
  >>> print is_latlng('urn:ogc:def:crs:OGC:1.3:CRS84')
  False

Limitations
===========

Coörder doesn't deal with the WKT format.

Credits
=======

Coörder is written by Sean Gillies (https://github.com/sgillies). It is based
on code in feedparser (http://code.google.com/p/feedparser/) also written by
Sean Gillies.


