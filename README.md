# thinkgisdump

[![Build status](https://github.com/pjsier/thinkgisdump/workflows/CI/badge.svg)](https://github.com/pjsier/thinkgisdump/actions)
![pypi](https://img.shields.io/pypi/v/thinkgisdump)

Command line tool for scraping GeoJSON from [ThinkGIS](https://www.wthgis.com/) sites. Based on [pyesridump](https://github.com/openaddresses/pyesridump).

## Install

You can install `thinkgisdump` using pip with the following command:

```shell
pip install thinkgisdump
```

This will add the script `thinkgis2geojson` to your path.

## Usage

```shell
usage: thinkgis2geojson [-h] [-l LAYER_ID] [-o OUTPUT] url

Scrape GeoJSON from ThinkGIS sites

positional arguments:
  url                   ThinkGIS server URL, layer ID will be parsed from the dsid query param if present

optional arguments:
  -h, --help            show this help message and exit
  -l LAYER_ID, --layer-id LAYER_ID
                        Layer ID (in the dsid query param) to be scraped
  -o OUTPUT, --output OUTPUT
                        Output file name, defaults to stdout
```

Because of the defaults and setting the layer ID based on query params, the following two command are equivalent.

```shell
thinkgis2geojson https://richlandil.wthgis.com --layer-id 1283 -o richland-precincts.geojson
thinkgis2geojson 'https://richlandil.wthgis.com?dsid=1283' > richland-precincts.geojson
```

## Notes

To get the parameters you'll need to scrape a given ThinkGIS layer, you can open the "Index" section on a map page. On the map index panel that opens up, you can open developer tools to see the full URL of the link for the layer you're interested in. The layer ID will be in the `dsid` parameter. You can also use this full URL including the query parameter in the `url` argument and it will be used without supplying `--layer-id` separately.

ThinkGIS returns point and multipoint geometries as polygon circles. When these are encountered, the mean point of the circle is used to create a point or multipoint GeoJSON geometry. Line shapes are also returned as polygons, and currently these are returned as polygons without further transformation.
