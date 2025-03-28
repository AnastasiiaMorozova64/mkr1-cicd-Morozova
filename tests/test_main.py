import pytest
from main import Nation, DemographicStats

@pytest.fixture
def sample_nations():
    return [
        Nation("Україна", 603628, 40000000),
        Nation("Франція", 551695, 67000000),
        Nation("Німеччина", 357022, 83000000)
    ]

@pytest.fixture
def temp_data_file(tmp_path):
    data = """Україна, 603628, 40000000
Франція, 551695, 67000000
Німеччина, 357022, 83000000"""
    
    file_path = tmp_path / "test_data.txt"
    file_path.write_text(data, encoding="utf-8")
    return str(file_path)

@pytest.mark.parametrize(
    "title, territory_size, citizen_count, expected_repr",
    [
        ("Україна", 603628, 40000000, "Україна - 603628.0 км, 40000000 людей"),
        ("Франція", 551695, 67000000, "Франція - 551695.0 км, 67000000 людей"),
        ("Німеччина", 357022, 83000000, "Німеччина - 357022.0 км, 83000000 людей"),
    ]
)
def test_nation_init(title, territory_size, citizen_count, expected_repr):
    nation = Nation(title, territory_size, citizen_count)
    assert nation.title == title
    assert nation.territory_size == float(territory_size)
    assert nation.citizen_count == int(citizen_count)
    assert repr(nation) == expected_repr

def test_load_nation_data(temp_data_file):
    stats_handler = DemographicStats(temp_data_file)
    assert len(stats_handler.nation_list) == 3
    assert stats_handler.nation_list[0].title == "Україна"
    assert stats_handler.nation_list[1].title == "Франція"
    assert stats_handler.nation_list[2].title == "Німеччина"

def test_arrange_by_territory(sample_nations):
    sorted_nations = sorted(sample_nations, key=lambda n: n.territory_size, reverse=True)
    assert sorted_nations[0].title == "Україна"
    assert sorted_nations[1].title == "Франція"
    assert sorted_nations[2].title == "Німеччина"

def test_arrange_by_citizens(sample_nations):
    sorted_nations = sorted(sample_nations, key=lambda n: n.citizen_count, reverse=True)
    assert sorted_nations[0].title == "Німеччина"
    assert sorted_nations[1].title == "Франція"
    assert sorted_nations[2].title == "Україна"
