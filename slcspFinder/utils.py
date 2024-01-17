import csv
import sys
import collections
import logging

log = logging.getLogger(__name__)

def getRateAreasByZipcode(zips_input: str):
    """gets the rate areas associated by zipcode and saves the tuple in dictionary 

    Args:
        zips_input (str): zip file csv

    Raises:
        e: error

    Returns:
        _type_: dict
    """
    try:
        with open(zips_input, mode="r") as zips:
            rate_areas_by_zipcode = collections.defaultdict(set)
            for row in csv.DictReader(zips):
                rate_areas_by_zipcode[row["zipcode"]].add(row["state"] + " " + row["rate_area"])
    except Exception as e:
        log.error("getRateAreasByZipcode() raised an error %s", e)
        raise e
    return rate_areas_by_zipcode

def getSilverRatesByRateArea(plans_input: str):
    """gets the silver rates associated by rate area and saves the tuple in dictionary 

    Args:
        plans_input (str): plans file csv

    Raises:
        e: error

    Returns:
        _type_: dict
    """
    try:
        with open(plans_input, mode="r") as plans:
            silver_rates_by_rate_area = collections.defaultdict(set)
            for row in csv.DictReader(plans):
                if row["metal_level"] == "Silver":
                    state_rate_area = row["state"] + " " + row["rate_area"]
                    silver_rates_by_rate_area[state_rate_area].add(float(row["rate"]))
    except Exception as e:
        log.error("getSilverRatesByRateArea() raised an error %s", e)
        raise e
    return silver_rates_by_rate_area

def getSLCSPByZipcode(zipcode: str, rate_areas_by_zipcode: dict, silver_rates_by_rate_area: dict):
    """gets the SLCSP benchmark associated by zipcode and returns the value

    Args:
        zipcode (str): zipcode
        rate_areas_by_zipcode (dict): rate areas by zipcode dictionary
        silver_rates_by_rate_area (dict): silver rates by rate area dictionary

    Raises:
        e: error

    Returns:
        _type_: str
    """
    try:
        slcsp_output = ""
        rate_area = list(rate_areas_by_zipcode[zipcode])[0]
        if len(rate_areas_by_zipcode[zipcode]) == 1 and rate_area in silver_rates_by_rate_area:
            if len(silver_rates_by_rate_area[rate_area]) >= 2:
                silver_rates_sorted = sorted(silver_rates_by_rate_area[rate_area])
                slcsp_output = "{:.2f}".format(silver_rates_sorted[1])
    except Exception as e:
        log.error("getSLCSPByZipcode raised an error %s", e)
        raise e
    return slcsp_output

def generateOutput(slcsp_input: str, rate_areas_by_zipcode: dict, silver_rates_by_rate_area: dict):
    """Generates the output of zip codes and their associated SLCSP benchmark

    Args:
        slcsp_input (str): slcsp file csv
        rate_areas_by_zipcode (dict): rate areas by zipcode dictionary
        silver_rates_by_rate_area (dict): silver rates by rate area dictionary

    Raises:
        e: error
    """
    try:
        with open(slcsp_input, mode="r") as slcsp:
            sys.stdout.write('zipcode,rate\n')
            for row in csv.DictReader(slcsp):
                benchmark_rate = getSLCSPByZipcode(row["zipcode"], rate_areas_by_zipcode, silver_rates_by_rate_area)
                sys.stdout.write(f'{row["zipcode"]},{benchmark_rate}\n')
    except Exception as e:
        log.error("generateOutput raised an error %s", e)
        raise e
    return