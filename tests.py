# Test suite

from coorder import is_latlng

def test_epsg4326():
    assert is_latlng('epsg:4326') is True

def test_epsg4326_init():
    assert is_latlng({'init': 'epsg:4326'}) is True

def test_epsg3857():
    assert is_latlng('epsg:3857') is False

