from utils import getRateAreasByZipcode, getSilverRatesByRateArea, generateOutput

zips = "zips.csv"
plans = "plans.csv"
slcsp = "slcsp.csv"

if __name__ == "__main__":

    rate_areas_by_zipcode = getRateAreasByZipcode(zips)
    silver_rates_by_rate_area = getSilverRatesByRateArea(plans)
    generateOutput(slcsp, rate_areas_by_zipcode, silver_rates_by_rate_area)