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

pd.options.mode.chained_assignment = None
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

    def get_gender_distribution_arsc(self, field):
        temp_df = (
            self.data[self.data.heir == 1]
            .groupby(["occupation_c", "gender"], as_index=False)
            .value.sum()
        )
        return temp_df[temp_df.occupation_c == field]

    def _get_list_of_all_level_occupation(self, level=5):
        return self.data[self.data.heir == level].occupation_c.unique()

    def _get_list_of_engineering(self):
        ENGINEERING_OCCUPATIONS = {
            "electrical and electronics engineers",
            "mechanical engineers",
            "computer engineers",
        }
        occupations = self._get_list_of_all_level_occupation(5)
        essentail_cols = []
        for occupation in occupations:
            lower_occupation = occupation.lower()
            if any(eng in lower_occupation for eng in ENGINEERING_OCCUPATIONS):
                essentail_cols.append(occupation)
        return essentail_cols

    def _update_education(self, value):
        if value == "Postsecondary certificate, diploma or degree":
            return "With Postsecondary Education"
        return "Without Postsecondary Education"

    def get_engineering_df(self):
        eng_df = self.data[self.data.occupation_c.isin(self._get_list_of_engineering())]
        eng_df["education_filtered"] = eng_df["education"].apply(self._update_education)
        return eng_df

    def get_list_of_essential_occ(self):
        ESSENTIAL_OCCUPATIONS = {"nurse", "police", "fire"}
        essentail_cols = []
        occupations = self._get_list_of_all_level_occupation(5)
        for occupation in occupations:
            lower_occupation = occupation.lower()
            if (
                any(
                    essential in lower_occupation for essential in ESSENTIAL_OCCUPATIONS
                )
                and "nursery" not in lower_occupation
            ):
                essentail_cols.append(occupation)
        return essentail_cols

    def get_essentails_df(self):
        essential_df = self.data[
            self.data.occupation_c.isin(self.get_list_of_essential_occ())
        ]
        return essential_df

    def get_essentails_df_whole(self):
        df = self.get_essentails_df()
        df = df.groupby(["geo", "occupation_c"], as_index=False).value.sum()
        return df
