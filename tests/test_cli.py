import pytest  # noqa

from thinkgisdump.cli import parse_feature


def test_parse_feature():
    feature_content = """
    <overlay>
    <info>
    <![CDATA[<tr><td class=ftrfld>Feature Name</td><td class=ftrval>Test</td></tr>]]>
    </info>
    <poly>,,34316907,51487011,0,3,0,4,0,3,0,4,0,3,-1,0,0</poly>
    <zoomto>34316516,51486814,34316907,51487207,17</zoomto>
    </overlay>
    """
    assert parse_feature(feature_content, "1") == {
        "type": "Feature",
        "properties": {"id": "1", "Feature Name": "Test"},
        "geometry": {
            "type": "Point",
            "coordinates": [-87.95488402247429, 38.59907254824296],
        },
    }
