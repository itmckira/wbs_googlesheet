"""
WBS Creator Module

This module provides functions to create WBS items from Google Sheets data.
"""

from wbs_item import WBSItem


def parse_wbs_from_sheet(sheet_data, has_header=True):
    """
    Parse WBS items from Google Sheets data.
    
    Expected columns in the sheet:
    - ID: Unique identifier
    - Name: Task name
    - Description: Task description (optional)
    - Parent ID: ID of parent task (optional)
    - Level: Hierarchical level
    - Duration: Duration in days (optional)
    - Start Date: Start date (optional)
    - End Date: End date (optional)
    - Resources: Comma-separated list of resources (optional)
    
    Args:
        sheet_data: List of rows from Google Sheet
        has_header: Whether the first row contains headers
    
    Returns:
        List of WBSItem objects
    """
    if not sheet_data:
        return []
    
    # Skip header row if present
    start_index = 1 if has_header else 0
    
    wbs_items = []
    
    for row_index, row in enumerate(sheet_data[start_index:], start=start_index):
        # Skip empty rows
        if not row or not any(row):
            continue
        
        # Pad row with empty strings if needed
        while len(row) < 9:
            row.append('')
        
        try:
            # Parse the row data
            item_id = row[0].strip() if row[0] else f"WBS-{row_index}"
            name = row[1].strip() if len(row) > 1 and row[1] else "Unnamed Task"
            description = row[2].strip() if len(row) > 2 and row[2] else ""
            parent_id = row[3].strip() if len(row) > 3 and row[3] else None
            
            # Parse level (default to 1 if not specified or invalid)
            try:
                level = int(row[4]) if len(row) > 4 and row[4] else 1
            except (ValueError, TypeError):
                level = 1
            
            # Parse duration (default to 0 if not specified or invalid)
            try:
                duration = float(row[5]) if len(row) > 5 and row[5] else 0
            except (ValueError, TypeError):
                duration = 0
            
            start_date = row[6].strip() if len(row) > 6 and row[6] else None
            end_date = row[7].strip() if len(row) > 7 and row[7] else None
            
            # Parse resources
            resources_str = row[8].strip() if len(row) > 8 and row[8] else ""
            resources = [r.strip() for r in resources_str.split(',') if r.strip()]
            
            # Create WBS item
            wbs_item = WBSItem(
                id=item_id,
                name=name,
                description=description,
                parent_id=parent_id,
                level=level,
                duration=duration,
                start_date=start_date,
                end_date=end_date,
                resources=resources
            )
            
            wbs_items.append(wbs_item)
        
        except Exception as e:
            print(f"Warning: Error parsing row {row_index}: {e}")
            continue
    
    return wbs_items


def display_wbs_tree(wbs_items):
    """
    Display WBS items in a tree structure.
    
    Args:
        wbs_items: List of WBSItem objects
    """
    if not wbs_items:
        print("No WBS items to display.")
        return
    
    print("\n=== Work Breakdown Structure ===\n")
    
    for item in wbs_items:
        print(item.display())
        print()


def export_wbs_to_dict_list(wbs_items):
    """
    Export WBS items to a list of dictionaries.
    
    Args:
        wbs_items: List of WBSItem objects
    
    Returns:
        List of dictionaries
    """
    return [item.to_dict() for item in wbs_items]
