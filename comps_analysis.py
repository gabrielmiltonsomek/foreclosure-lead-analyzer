"""
Comparable Sales Analysis

This module simulates comparable property analysis for foreclosure leads.

It is designed to show how property records could be evaluated against
estimated market value, purchase price, and potential investment spread.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class PropertyComp:
    """Represents a comparable property sale."""

    address: str
    sale_price: float
    square_feet: int


@dataclass
class LeadValuation:
    """Stores estimated valuation data for a foreclosure lead."""

    property_address: str
    estimated_value: float
    target_purchase_price: float
    estimated_spread: float


def calculate_average_price_per_sqft(comps: List[PropertyComp]) -> float:
    """Calculates the average price per square foot from comparable sales."""

    if not comps:
        return 0.0

    total_price_per_sqft = sum(comp.sale_price / comp.square_feet for comp in comps)
    return round(total_price_per_sqft / len(comps), 2)


def estimate_property_value(square_feet: int, comps: List[PropertyComp]) -> float:
    """Estimates property value using average comparable sale price per square foot."""

    average_price_per_sqft = calculate_average_price_per_sqft(comps)
    return round(square_feet * average_price_per_sqft, 2)


def analyze_lead(
    property_address: str,
    square_feet: int,
    target_purchase_price: float,
    comps: List[PropertyComp],
) -> LeadValuation:
    """Analyzes a foreclosure lead using comparable sale data."""

    estimated_value = estimate_property_value(square_feet, comps)
    estimated_spread = round(estimated_value - target_purchase_price, 2)

    return LeadValuation(
        property_address=property_address,
        estimated_value=estimated_value,
        target_purchase_price=target_purchase_price,
        estimated_spread=estimated_spread,
    )


def main() -> None:
    """Runs a sample comparable sales analysis."""

    comps = [
        PropertyComp("123 Sample Street", 325000, 1500),
        PropertyComp("456 Example Avenue", 350000, 1600),
        PropertyComp("789 Demo Drive", 315000, 1450),
    ]

    result = analyze_lead(
        property_address="100 Foreclosure Lane",
        square_feet=1525,
        target_purchase_price=240000,
        comps=comps,
    )

    print("Comparable Sales Analysis")
    print("-" * 30)
    print(f"Property: {result.property_address}")
    print(f"Estimated Value: ${result.estimated_value:,.2f}")
    print(f"Target Purchase Price: ${result.target_purchase_price:,.2f}")
    print(f"Estimated Spread: ${result.estimated_spread:,.2f}")


if __name__ == "__main__":
    main()