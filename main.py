#!/usr/bin/env python3
"""
Main script to create WBS items from Google Sheet

Usage:
    python main.py <spreadsheet_id> [range]

Example:
    python main.py "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms" "Sheet1!A1:I100"
    python main.py "your-spreadsheet-id"
"""

import sys
import json
from google_sheets import read_sheet_data, get_spreadsheet_info
from wbs_creator import parse_wbs_from_sheet, display_wbs_tree, export_wbs_to_dict_list


def main():
    """Main function to orchestrate WBS creation from Google Sheet."""
    
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Error: Spreadsheet ID is required")
        print("\nUsage:")
        print("  python main.py <spreadsheet_id> [range]")
        print("\nExample:")
        print("  python main.py '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms' 'Sheet1!A1:I100'")
        print("  python main.py 'your-spreadsheet-id'")
        sys.exit(1)
    
    spreadsheet_id = sys.argv[1]
    range_name = sys.argv[2] if len(sys.argv) > 2 else 'Sheet1!A1:I100'
    
    try:
        print(f"Connecting to Google Sheets...")
        
        # Get spreadsheet info
        info = get_spreadsheet_info(spreadsheet_id)
        print(f"Spreadsheet: {info['title']}")
        print(f"Available sheets: {', '.join(info['sheets'])}")
        print()
        
        # Read data from the sheet
        print(f"Reading data from range: {range_name}")
        sheet_data = read_sheet_data(spreadsheet_id, range_name)
        
        if not sheet_data:
            print("No data found in the specified range.")
            sys.exit(1)
        
        print(f"Found {len(sheet_data)} rows")
        print()
        
        # Parse WBS items
        print("Parsing WBS items...")
        wbs_items = parse_wbs_from_sheet(sheet_data, has_header=True)
        
        if not wbs_items:
            print("No valid WBS items found.")
            sys.exit(1)
        
        print(f"Successfully parsed {len(wbs_items)} WBS items")
        
        # Display WBS tree
        display_wbs_tree(wbs_items)
        
        # Export to JSON file
        output_file = 'wbs_items.json'
        wbs_dict_list = export_wbs_to_dict_list(wbs_items)
        
        with open(output_file, 'w') as f:
            json.dump(wbs_dict_list, f, indent=2)
        
        print(f"\n✓ WBS items exported to {output_file}")
        print(f"✓ Total items created: {len(wbs_items)}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nPlease follow the setup instructions in README.md to configure Google Sheets API access.")
        sys.exit(1)
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
