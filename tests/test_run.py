import csv
import itertools
from slcspFinder.utils import getSilverRatesByRateArea, getRateAreasByZipcode, getSLCSPByZipcode

silver_rates_by_rate_area = getSilverRatesByRateArea("plans.csv")
rate_areas_by_zip_code = getRateAreasByZipcode("zips.csv")