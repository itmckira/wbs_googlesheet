"""
Google Sheet Template Example

This file demonstrates the expected structure of the Google Sheet
for creating WBS items.

To use this template:
1. Create a new Google Sheet
2. Set up the columns as shown below
3. Fill in your WBS items
4. Share the sheet with your Google account (if using service account)
5. Copy the spreadsheet ID from the URL
6. Run: python main.py <spreadsheet_id>
"""

TEMPLATE_STRUCTURE = """
Column A: ID          - Unique identifier (e.g., 1.0, 1.1, 2.0)
Column B: Name        - Task or deliverable name
Column C: Description - Detailed description (optional)
Column D: Parent ID   - ID of parent task for hierarchy (optional)
Column E: Level       - Hierarchical level (1, 2, 3, etc.)
Column F: Duration    - Duration in days (optional)
Column G: Start Date  - Start date in YYYY-MM-DD format (optional)
Column H: End Date    - End date in YYYY-MM-DD format (optional)
Column I: Resources   - Comma-separated list of resources (optional)
"""

SAMPLE_SHEET_URL = """
You can create a copy of this example spreadsheet:
https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/

Or create your own spreadsheet with the structure shown above.
"""

print(TEMPLATE_STRUCTURE)
print("\n" + "="*70 + "\n")
print(SAMPLE_SHEET_URL)
