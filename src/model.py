"""-------------------------------------------------------
CP321: Assignment 7- Model.py
-------------------------------------------------------
Author:  JD
ID:      169018282
Uses:    pandas,numpy,plotly,dash
Version:  1.0.8
__updated__ = Sun Mar 30 2025
-------------------------------------------------------
"""

import pandas as pd
import numpy as np

REDUNDANT_COLS = [
    "DGUID",
    "Age (2)",
    "UOM",
    "UOM_ID",
    "SCALAR_FACTOR",
    "SCALAR_ID",
    "STATUS",
    "SYMBOL",
    "TERMINATED",
    "DECIMALS",
    "VECTOR",
    "REF_DATE",
    "COORDINATE",
]


class Model:
    def __init__(self, url):
        self.url = url
        self.data = self._load_data()
        self._preprocess_data()

    def _load_data(self):
        return pd.read_csv(self.url)

    def _preprocess_data(self):
        self.data = self.data.drop(columns=REDUNDANT_COLS)
        self.data.columns = [
            "geo",
            "education",
            "major",
            "occupation",
            "gender",
            "value",
        ]

        self.data["gender"] = self.data.gender.apply(self._clean_gender_col)
        self.data["noc"] = self.data.occupation.apply(self._clean_noc_codes)
        self.data["heir"] = self.data.noc.apply(self._clean_hierarchy_num)
        self.data["occupation_c"] = self.data.occupation.apply(self._clean_occupations)

    def _clean_gender_col(self, value):
        return value[:-1]

    def _clean_noc_codes(self, value):
        noc = value.split(" ")[0]
        if not noc.isdigit():
            return np.nan
        return noc

    def _clean_hierarchy_num(self, value):
        if type(value) is float:
            return 0
        return len(value)

    def _clean_occupations(self, value):
        value = value.split(" ")
        value.pop(0)
        return " ".join(value)

    def get_province_list(self):
        return sorted(self.data.geo.unique())

    def get_field_list(self):
        return sorted(self.data[self.data.heir == 1].occupation_c.unique())

    def get_gender_distribution_by_field(self, field, province_list):

        temp_df = (
            self.data[self.data.heir == 1]
            .groupby(["geo", "occupation_c", "gender"], as_index=False)
            .value.sum()
        )

        temp_df = temp_df[temp_df.occupation_c == field]
        return temp_df[temp_df.geo.isin(province_list)]
