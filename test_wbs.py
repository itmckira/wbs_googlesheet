#!/usr/bin/env python3
"""
Test script to validate WBS creation functionality without Google Sheets API
"""

import sys
from wbs_creator import parse_wbs_from_sheet, display_wbs_tree, export_wbs_to_dict_list
from example_data import get_sample_wbs_data


def test_wbs_parsing():
    """Test WBS parsing with sample data."""
    print("=== Testing WBS Creation ===\n")
    
    # Get sample data
    sample_data = get_sample_wbs_data()
    print(f"Sample data loaded: {len(sample_data)} rows")
    
    # Parse WBS items
    print("\nParsing WBS items...")
    wbs_items = parse_wbs_from_sheet(sample_data, has_header=True)
    
    if not wbs_items:
        print("❌ Failed: No WBS items parsed")
        return False
    
    print(f"✓ Successfully parsed {len(wbs_items)} WBS items")
    
    # Validate parsing
    expected_count = len(sample_data) - 1  # Minus header row
    if len(wbs_items) != expected_count:
        print(f"❌ Warning: Expected {expected_count} items, got {len(wbs_items)}")
    
    # Check first item
    first_item = wbs_items[0]
    print(f"\nFirst item validation:")
    print(f"  ID: {first_item.id}")
    print(f"  Name: {first_item.name}")
    print(f"  Level: {first_item.level}")
    print(f"  Resources: {first_item.resources}")
    
    if first_item.id != '1.0':
        print(f"❌ Failed: Expected ID '1.0', got '{first_item.id}'")
        return False
    
    if first_item.name != 'Project Setup':
        print(f"❌ Failed: Expected name 'Project Setup', got '{first_item.name}'")
        return False
    
    print("✓ First item validation passed")
    
    # Test hierarchy
    print(f"\nHierarchy validation:")
    level_2_items = [item for item in wbs_items if item.level == 2]
    print(f"  Found {len(level_2_items)} level-2 items")
    
    has_parent = any(item.parent_id for item in wbs_items)
    if has_parent:
        print(f"✓ Parent-child relationships found")
    else:
        print(f"❌ Warning: No parent-child relationships found")
    
    # Display tree
    display_wbs_tree(wbs_items)
    
    # Test export
    print("\nTesting export functionality...")
    wbs_dict_list = export_wbs_to_dict_list(wbs_items)
    
    if len(wbs_dict_list) != len(wbs_items):
        print(f"❌ Failed: Export count mismatch")
        return False
    
    print(f"✓ Export successful: {len(wbs_dict_list)} items")
    
    # Validate exported data structure
    first_dict = wbs_dict_list[0]
    required_keys = ['id', 'name', 'description', 'parent_id', 'level', 'duration', 'resources']
    
    for key in required_keys:
        if key not in first_dict:
            print(f"❌ Failed: Missing key '{key}' in exported data")
            return False
    
    print(f"✓ All required keys present in exported data")
    
    print("\n" + "="*50)
    print("✓ All tests passed!")
    print("="*50)
    return True


if __name__ == '__main__':
    try:
        success = test_wbs_parsing()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
