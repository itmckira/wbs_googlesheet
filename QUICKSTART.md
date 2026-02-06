# Quick Start Guide

This guide helps you get started with the WBS Google Sheet tool quickly.

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Up Google Sheets API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Enable the Google Sheets API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download credentials as `credentials.json` and place in project root

## Step 3: Prepare Your Google Sheet

Create a Google Sheet with these columns:

```
ID | Name | Description | Parent ID | Level | Duration | Start Date | End Date | Resources
```

Example data:
```
1.0 | Project Setup | Initial setup | | 1 | 5 | 2024-01-01 | 2024-01-05 | John, Jane
1.1 | Requirements  | Define req   | 1.0 | 2 | 3 | 2024-01-01 | 2024-01-03 | John
```

## Step 4: Run the Tool

### Test with Sample Data (No API Required)
```bash
python test_wbs.py
```

### Run with Your Google Sheet
```bash
python main.py "YOUR_SPREADSHEET_ID"
```

To find your spreadsheet ID:
- Open your Google Sheet
- Look at the URL: `https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit`
- Copy the SPREADSHEET_ID part

### Specify Custom Range (Optional)
```bash
python main.py "YOUR_SPREADSHEET_ID" "Sheet1!A1:I50"
```

## Step 5: View Results

The tool will:
- Display WBS items in a tree structure in the console
- Export data to `wbs_items.json`

## Common Issues

### "credentials.json not found"
- Download OAuth credentials from Google Cloud Console
- Save as `credentials.json` in project directory

### "No data found"
- Check spreadsheet ID is correct
- Verify sheet name in range (default: Sheet1)
- Ensure sheet has data starting from row 1

### First-time authentication
- Browser window will open for authentication
- Sign in with your Google account
- Grant permissions to access Google Sheets
- Token will be saved for future runs

## Example Output

```
Connecting to Google Sheets...
Spreadsheet: Project WBS
Available sheets: Sheet1

Reading data from range: Sheet1!A1:I100
Found 10 rows

Parsing WBS items...
Successfully parsed 9 WBS items

=== Work Breakdown Structure ===

1.0 - Project Setup
  Description: Initial project setup
  Duration: 5.0 days
  Resources: John, Jane

  1.1 - Define Requirements
    Description: Gather requirements
    Duration: 3.0 days
    Resources: John

✓ WBS items exported to wbs_items.json
✓ Total items created: 9
```

## Next Steps

- Modify your Google Sheet to add your own WBS items
- Use the exported JSON for integration with other tools
- Customize the parsing logic in `wbs_creator.py` if needed
- Add additional fields to `wbs_item.py` as required

For more details, see the full [README.md](README.md)
