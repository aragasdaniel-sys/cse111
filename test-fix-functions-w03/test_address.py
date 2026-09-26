import pytest
from address import extract_city, extract_state, extract_zipcode

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("123 Maple Street Apt 4B, Springfield, IL 62704") == "Springfield"

def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("123 Maple Street Apt 4B, Springfield, IL 62704") == "IL"

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("123 Maple Street Apt 4B, Springfield, IL 62704") == "62704"

pytest.main(["-v", "--tb=line", "-rN", __file__])