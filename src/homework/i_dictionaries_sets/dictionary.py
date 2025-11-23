def add_inventory(inventory_dictionary: dict, widget_name: str, quantity: int) -> None:
    """
    Add or update an inventory item in-place.
    - If widget_name does not exist, insert with given quantity.
    - If it exists, increase its quantity by the given amount (can be negative).
    Non-value-returning function (returns None).
    """
    if widget_name in inventory_dictionary:
        inventory_dictionary[widget_name] += quantity
    else:
        inventory_dictionary[widget_name] = quantity


def remove_inventory_widget(inventory_dictionary: dict, widget_name: str) -> str:
    """
    Remove widget_name from inventory_dictionary if present.
    Return:
      - 'Record deleted' if removed
      - 'Item not found' if not present
    """
    if widget_name in inventory_dictionary:
        del inventory_dictionary[widget_name]
        return 'Record deleted'
    return 'Item not found'

