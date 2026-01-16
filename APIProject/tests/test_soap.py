import logging
import pytest
from zeep import Client

wsdl = 'http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = Client(wsdl=wsdl)

@pytest.mark.parametrize("country,expected_code", [
    ("India", "IN"),
    ("United States", "US"),
])
def test_country_iso(country, expected_code):
    result = client.service.CountryISOCode(sCountryName=country)
    assert result == expected_code, "ISO code does not match expected value"
    logging.info(f"TEST PASSED: ISO code for {country} is {expected_code}")

def test_capital(iso_code="IN", expected_capital="New Delhi"):
    result = client.service.CapitalCity(sCountryISOCode=iso_code)
    assert result == expected_capital, "Capital city does not match expected value"
    logging.info(f"TEST PASSED: Capital city for {iso_code} is {expected_capital}")
