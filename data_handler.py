def process_data(data):
    """Process the fetched data for manipulation."""
    processed_data = []
    for record in data:
        # Example manipulation: Update `Bemerkung` field
        if "data" in record and "JanuarMarian" in record["data"]:
            record["data"]["JanuarMarian"]["Bemerkung"] = "Updated Remark"
        processed_data.append(record)
    return processed_data
