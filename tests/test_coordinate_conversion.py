import sys
import pytest
sys.path.append('..')

import conversions
import numpy as np


@pytest.mark.parametrize(("lat","lon", "expected"), [
                         [40.5954448,-105.1397824,13],
                        ])
def test_zone_number(lat, lon, expected):
    assert conversions.latlon_to_zone_number(lat, lon) == expected

@pytest.mark.parametrize(("lat","expected"), [[40.595445, "T"]])
def test_zone_letter(lat, expected):
    assert conversions.latitude_to_zone_letter(lat) == expected

@pytest.mark.parametrize(("lat","long","expected"), [
    [40.5954448,-105.1397824,(488172.53,4493858.59,13, "T")],
    [35.580491,-80.134277, (578437.67, 3937765.21, 17, "S")],
    ])
def test_utm_conversion(lat,long,expected):
    easting, northing, zone_number, zone_letter = expected

    conv_east, conv_north, conv_zone, conv_zone_letter = conversions.latlon_to_utm(lat, long)

    assert np.allclose([conv_east, conv_north], [easting, northing], atol=1e-5)
    assert conv_zone == zone_number
    assert conv_zone_letter == zone_letter