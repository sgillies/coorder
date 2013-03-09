# Test suite

from coorder import is_latlng

def test_epsg4326():
    assert is_latlng('EPSG:4326') is True

def test_epsg4326_init():
    assert is_latlng({'init': 'epsg:4326'}) is True

def test_4326():
    assert is_latlng(4326) is True

def test_None():
    assert is_latlng(None) is False

def test_epsg3857():
    assert is_latlng('epsg:3857') is False

def test_CRS84():
    assert is_latlng('urn:ogc:def:crs:OGC:1.3:CRS84') is False

