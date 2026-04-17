import pandas as pd
import pytest

# Load data (same logic as app)
df = pd.read_csv("processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])


def test_data_load():
    """Check data is loaded correctly"""
    assert not df.empty
    assert "sales" in df.columns
    assert "date" in df.columns
    assert "region" in df.columns


def test_region_filter():
    """Check region filtering works"""
    regions = df["region"].unique()
    expected = {"north", "south", "east", "west"}

    assert set(regions).issubset(expected)


def test_sales_are_numeric():
    """Ensure sales column is numeric"""
    assert pd.api.types.is_numeric_dtype(df["sales"])


def test_date_conversion():
    """Ensure date column is datetime"""
    assert pd.api.types.is_datetime64_any_dtype(df["date"])


def test_grouping_logic():
    """Check aggregation logic works"""
    grouped = df.groupby("date")["sales"].sum().reset_index()

    assert "sales" in grouped.columns
    assert "date" in grouped.columns
    assert len(grouped) <= len(df)