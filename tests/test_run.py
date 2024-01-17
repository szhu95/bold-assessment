from slcspFinder.utils import getSilverRatesByRateArea, getRateAreasByZipcode, getSLCSPByZipcode

rate_areas_by_zipcode = getRateAreasByZipcode("zips.csv")
silver_rates_by_rate_area = getSilverRatesByRateArea("plans.csv")

def test_get_rate_areas():
    """testing rates areas for specific zipcode"""
    assert rate_areas_by_zipcode["32431"] == {"FL 31", "FL 67"}

def test_get_silver_rates():
    """testing silver rates for specific rate area"""
    assert silver_rates_by_rate_area['IL 1'] == {231.84, 272.26, 279.89, 
                                                 280.31, 282.61, 283.7, 
                                                 282.88, 297.95, 238.35, 
                                                 305.96, 366.56, 309.4, 
                                                 249.77, 318.19, 446.14, 
                                                 321.4, 322.45, 454.75, 
                                                 207.04, 209.95, 211.06, 
                                                 343.9, 215.16, 218.16, 
                                                 347.12, 220.37, 223.45, 
                                                 248.77, 224.63, 223.16, 
                                                 227.63, 228.65, 229.47, 
                                                 230.07, 229.38, 230.49, 
                                                 233.14, 234.09, 235.03, 
                                                 232.71, 237.32, 238.71, 
                                                 239.76, 240.25, 241.9, 
                                                 241.19, 243.07, 243.67, 
                                                 373.66, 243.87, 247.3, 
                                                 248.28, 249.85, 252.21}
    
def test_get_slcsp_by_zipcode():
    """testing benchmark for specific zipcode"""
    benchmark = getSLCSPByZipcode("86313", rate_areas_by_zipcode, silver_rates_by_rate_area)
    assert benchmark == "292.90"
    
def test_one_silver_plan():
    """testing area with one silver plan should return empty string for benchmark"""
    benchmark = getSLCSPByZipcode("08037", rate_areas_by_zipcode, silver_rates_by_rate_area)
    assert benchmark == ""
    
def test_duplicate_silver_plans():
    """testing zipcode with duplicate silver rate prices should return correct benchmark"""
    benchmark = getSLCSPByZipcode("52654", rate_areas_by_zipcode, silver_rates_by_rate_area)
    assert benchmark == "242.39"
    
def test_multiple_rate_areas():
    """testing zipcode with multiple rate areas should return empty string for benchmark
    46706 is mapped to {'IN 3', 'IN 4'}
    """
    benchmark = getSLCSPByZipcode("46706", rate_areas_by_zipcode, silver_rates_by_rate_area)
    assert benchmark == ""