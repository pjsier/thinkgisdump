import pytest  # noqa

from thinkgisdump.geom import is_point, parse_coords, parse_geometry, point_coords


def test_parse_coords():
    test_geom_str = ",,34266493,51420302,0,3,0,4,-1,3,0,4,0,3,0,0"
    assert parse_coords(test_geom_str) == [
        (-88.09010356664658, 38.7387913583901),
        (-88.09010356664658, 38.73878508196507),
        (-88.09010356664658, 38.73877671339753),
        (-88.09010624885559, 38.73877043697122),
        (-88.09010624885559, 38.73876206840195),
        (-88.09010624885559, 38.73875579197434),
        (-88.09010624885559, 38.73875579197434),
    ]


def test_is_point():
    assert is_point(",,,,9,1,0,5,2,-5")
    assert not is_point(",,,,12,2,6,-5,2,-4")


def test_point_coords():
    assert point_coords([(-1, 1), (-0.5, 0), (1, -1)]) == [0.0, 0.0]


def test_parse_geometry():
    assert parse_geometry(["20,20,20,20,100,2,3,1"])["type"] == "Polygon"
    assert (
        parse_geometry(["20,20,20,20,100,2,4,1", "20,20,20,20,100,2,4,1"])["type"]
        == "MultiPolygon"
    )
