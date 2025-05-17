from djangoapp.models import CarDealer, DealerReview
import json
import os

def populate_data():
    dealers = [
        {"id": 1, "full_name": "ABC Motors", "short_name": "ABC", "city": "New York", "state": "NY"},
        {"id": 2, "full_name": "XYZ Autos", "short_name": "XYZ", "city": "San Francisco", "state": "CA"},
        {"id": 3, "full_name": "Best Cars", "short_name": "BEST", "city": "Chicago", "state": "IL"},
        {"id": 4, "full_name": "Auto World", "short_name": "AUTO", "city": "Houston", "state": "TX"},
        {"id": 5, "full_name": "Motor Mall", "short_name": "MALL", "city": "Miami", "state": "FL"},
        {"id": 6, "full_name": "DriveTime", "short_name": "DRIVE", "city": "Seattle", "state": "WA"},
        {"id": 7, "full_name": "Premier Cars", "short_name": "PREMIER", "city": "Atlanta", "state": "GA"},
        {"id": 8, "full_name": "Value Autos", "short_name": "VALUE", "city": "Denver", "state": "CO"},
        {"id": 9, "full_name": "Top Gear Motors", "short_name": "TOPGEAR", "city": "Boston", "state": "MA"},
        {"id": 10, "full_name": "Speedy Motors", "short_name": "SPEEDY", "city": "Phoenix", "state": "AZ"},
        {"id": 11, "full_name": "Greenlight Auto", "short_name": "GREEN", "city": "Philadelphia", "state": "PA"},
        {"id": 12, "full_name": "Elite Rides", "short_name": "ELITE", "city": "Dallas", "state": "TX"},
        {"id": 13, "full_name": "Urban Motors", "short_name": "URBAN", "city": "Austin", "state": "TX"},
        {"id": 14, "full_name": "Metro Autos", "short_name": "METRO", "city": "San Diego", "state": "CA"},
        {"id": 15, "full_name": "Legendary Cars", "short_name": "LEGEND", "city": "Orlando", "state": "FL"},
        {"id": 16, "full_name": "Victory Motors", "short_name": "VICTORY", "city": "Charlotte", "state": "NC"},
        {"id": 17, "full_name": "Fusion Autos", "short_name": "FUSION", "city": "Nashville", "state": "TN"},
        {"id": 18, "full_name": "NextGen Motors", "short_name": "NEXTGEN", "city": "Portland", "state": "OR"},
        {"id": 19, "full_name": "Platinum Wheels", "short_name": "PLATINUM", "city": "Minneapolis", "state": "MN"},
        {"id": 20, "full_name": "Royal Auto Sales", "short_name": "ROYAL", "city": "Kansas City", "state": "MO"},
    ]

    for dealer in dealers:
        CarDealer.objects.update_or_create(
            id=dealer["id"],
            defaults={
                "full_name": dealer["full_name"],
                "short_name": dealer["short_name"],
                "city": dealer["city"],
                "state": dealer["state"]
            }
        )
