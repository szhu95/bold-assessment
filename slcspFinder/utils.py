import csv
import sys
import collections
import logging

log = logging.getLogger(__name__)

def getRateAreasByZipcode(zips_input: str):
    """_summary_

    Args:
        zips_input (str): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
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
    """_summary_

    Args:
        plans_input (str): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
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
    """_summary_

    Args:
        zipcode (str): _description_
        rate_areas_by_zipcode (dict): _description_
        silver_rates_by_rate_area (dict): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
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
    """_summary_

    Args:
        slcsp_input (str): _description_
        rate_areas_by_zipcode (dict): _description_
        silver_rates_by_rate_area (dict): _description_

    Raises:
        e: _description_
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