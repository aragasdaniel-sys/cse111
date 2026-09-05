from time_calculator import read_csv_file, calculate_percentage
from pytest import approx
import pytest

def test_calculate_percentage():
    assert calculate_percentage(0, 0) == 0
    assert calculate_percentage(5, 0) == 0
    assert calculate_percentage(1, 1) == approx(14.2857, abs=0.01)
    assert calculate_percentage(6, 20) == approx(4.2857, abs=0.01)
    assert calculate_percentage(10, 12) == approx(11.9047, abs=0.01)
    assert calculate_percentage(4, 8) == approx(7.1428, abs=0.01)
    assert calculate_percentage(1.5, 3) == approx(7.1428, abs=0.01)

# Used tmp_path to check instead of relying on a file that could not exist in everyones' computer
def test_read_csv_file(tmp_path):
    csv_file = tmp_path / "log.csv"
    csv_file.write_text("Sun August 09 2026,math,10\nMon August 10 2026,science,2\nTue August 11 2026,chemistry,0")

    result = read_csv_file(str(csv_file))

    assert result == [
    {"date": "Sun August 09 2026", "activity": "math", "hours": "10"},
    {"date": "Mon August 10 2026", "activity": "science", "hours": "2"},
    {"date": "Tue August 11 2026", "activity": "chemistry", "hours": "0"}
    ]

    csv_file2 = tmp_path / "empty_log.csv"
    csv_file2.write_text("")

    result2 = read_csv_file(str(csv_file2))

    assert result2 == []

pytest.main(["-v", "--tb=line", "-rN", __file__])