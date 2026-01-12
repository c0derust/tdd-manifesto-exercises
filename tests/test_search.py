import pytest

from src.search import search


@pytest.fixture
def test_cities():
    return [
        "Paris",
        "Budapest",
        "Skopje",
        "Rotterdam",
        "Valencia",
        "Vancouver",
        "Amsterdam",
        "Vienna",
        "Sydney",
        "NewYorkCity",
        "London",
        "Bangkok",
        "Hong Kong",
        "Dubai",
        "Rome",
        "Istanbul",
    ]


def test_search_returns_matching_cities(test_cities):
    result = search("London", test_cities)

    assert result == ["London"]


def test_seach_returns_empty_result_for_short_query(test_cities):
    result = search("L", test_cities)

    assert result == []


def test_search_returns_exact_prefix_matches(test_cities):
    result = search("Va", test_cities)

    assert result == ["Valencia", "Vancouver"]


def test_search_is_case_sensitive(test_cities):
    result = search("london", test_cities)

    assert result == []


def test_search_works_on_partial_matches(test_cities):
    result = search("ape", test_cities)

    assert result == ["Budapest"]


def test_search_returns_all_on_asterisk(test_cities):
    result = search("*", test_cities)

    assert result == test_cities
