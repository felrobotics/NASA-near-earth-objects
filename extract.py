"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    neos = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip the header line.
        for row in reader:
            designation = row[3]
            name = row[4]
            diameter = row[15]
            hazardous = row[7]
            neo = NearEarthObject(
                designation=designation,
                name=name,
                diameter=diameter,
                hazardous=hazardous)
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Load close approach data from the given JSON file.
    approaches_list = []
    with open(cad_json_path, 'r') as infile:
        cad_data = json.load(infile)['data']
        for cad in cad_data:
            designation = cad[0]
            time = cad[3]
            distance = cad[4]
            velocity = cad[7]
            approach = CloseApproach(
                designation=designation,
                time=time,
                distance=distance,
                velocity=velocity)
            approaches_list.append(approach)
    return approaches_list
