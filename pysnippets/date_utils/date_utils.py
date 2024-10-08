from datetime import datetime

def convert_to_iso8601(date_string):
    """
    Convert a date string to ISO-8601 format.

    Args:
        date_string (str): A date string in the format 'YYYY-MM-DD' or 'MM/DD/YYYY'.

    Returns:
        str: Date in ISO-8601 format (YYYY-MM-DD).
    """
    try:
        # Try parsing the date in different formats
        if '-' in date_string:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        else:
            date_obj = datetime.strptime(date_string, '%m/%d/%Y')

        return date_obj.isoformat()
    except ValueError as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    print(convert_to_iso8601("2024-10-06"))  # Outputs: 2024-10-06T00:00:00
    print(convert_to_iso8601("10/06/2024"))  # Outputs: 2024-10-06T00:00:00
