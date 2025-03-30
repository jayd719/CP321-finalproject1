import pandas as pd

DATA = {
    "State": [
        "California",
        "Texas",
        "Florida",
        "New York",
        "Pennsylvania",
        "Illinois",
        "Ohio",
        "Georgia",
        "North Carolina",
        "Michigan",
        "New Jersey",
        "Virginia",
        "Washington",
        "Arizona",
        "Massachusetts",
        "Tennessee",
        "Indiana",
        "Maryland",
        "Colorado",
        "Wisconsin",
    ],
    "Population": [
        39538223,
        29145505,
        21538187,
        20201249,
        13002700,
        12812508,
        11799448,
        10711908,
        10439388,
        10077331,
        9288994,
        8631393,
        7705281,
        7151502,
        7029917,
        6910840,
        6785528,
        6177224,
        5773714,
        5893718,
    ],
    "Code": [
        "CA",
        "TX",
        "FL",
        "NY",
        "PA",
        "IL",
        "OH",
        "GA",
        "NC",
        "MI",
        "NJ",
        "VA",
        "WA",
        "AZ",
        "MA",
        "TN",
        "IN",
        "MD",
        "CO",
        "WI",
    ],
}


class FifaModel:
    def __init__(self):
        self.data = self._load_data()

    def _load_data(self):
        """Load and return the population data"""
        data = None
        return pd.DataFrame(data or DATA)

    def get_filtered_data(self, min_population):
        """Return data filtered by minimum population"""
        return self.data[self.data["Population"] >= min_population * 1000000]
