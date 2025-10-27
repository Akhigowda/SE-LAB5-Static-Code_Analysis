"""Inventory Management System

Provides functions to manage adding, removing, saving, and loading
inventory data with logging, validation, and static analysis compliance.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global inventory data
STOCK_DATA = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item with a specified quantity to the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(
            "Invalid item or quantity type: item=%s, qty=%s",
            item,
            qty
        )
        return

    STOCK_DATA[item] = STOCK_DATA.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    """Remove a specific quantity of an item from inventory."""
    try:
        STOCK_DATA[item] -= qty
        if STOCK_DATA[item] <= 0:
            del STOCK_DATA[item]
            logging.info(
                "Item '%s' removed from inventory.", item
            )
    except KeyError:
        logging.warning(
            "Attempted to remove non-existent item: %s",
            item
        )


def get_qty(item):
    """Return the quantity of a specific item."""
    return STOCK_DATA.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        logging.info(
            "Data loaded successfully from %s",
            file_path
        )
        return data
    except FileNotFoundError:
        logging.error(
            "File %s not found. Starting with empty inventory.",
            file_path
        )
        return {}


def save_data(file_path="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(STOCK_DATA, file, indent=4)
    logging.info(
        "Data saved successfully to %s",
        file_path
    )


def print_data():
    """Display all items and their quantities."""
    print("Items Report")
    for item, qty in STOCK_DATA.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below a given threshold."""
    return [
        item for item, qty in STOCK_DATA.items()
        if qty < threshold
    ]


def main():
    """Main function to demonstrate inventory operations."""
    stock_data_loaded = load_data()
    if stock_data_loaded:
        STOCK_DATA.update(stock_data_loaded)

    add_item("apple", 10)
    add_item("banana", -2)
    add_item("orange", 6)
    remove_item("apple", 3)
    remove_item("grapes", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    print_data()


if __name__ == "__main__":
    main()
