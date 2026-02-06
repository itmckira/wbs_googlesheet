# WBS Google Sheet

A Python tool to create Work Breakdown Structure (WBS) items from Google Sheets.

## Features

- Read WBS data from Google Sheets
- Parse and create structured WBS items with hierarchy
- Support for task attributes: ID, Name, Description, Parent ID, Level, Duration, Dates, Resources
- Export WBS items to JSON format
- Display WBS items in a tree structure

## Prerequisites

- Python 3.7 or higher
- Google Cloud Project with Sheets API enabled
- OAuth 2.0 credentials from Google Cloud Console

## Installation

1. Clone this repository:
```bash
git clone https://github.com/itmckira/wbs_googlesheet.git
cd wbs_googlesheet
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up Google Sheets API access:

   a. Go to [Google Cloud Console](https://console.cloud.google.com/)
   
   b. Create a new project or select an existing one
   
   c. Enable the Google Sheets API:
      - Go to "APIs & Services" > "Library"
      - Search for "Google Sheets API"
      - Click "Enable"
   
   d. Create OAuth 2.0 credentials:
      - Go to "APIs & Services" > "Credentials"
      - Click "Create Credentials" > "OAuth client ID"
      - Choose "Desktop app" as the application type
      - Download the credentials and save as `credentials.json` in the project root
   
   e. The first time you run the application, it will open a browser window for authentication

## Google Sheet Format

Your Google Sheet should have the following columns (first row as headers):

| ID | Name | Description | Parent ID | Level | Duration | Start Date | End Date | Resources |
|----|------|-------------|-----------|-------|----------|------------|----------|-----------|
| 1.0 | Project Setup | Initial project setup | | 1 | 5 | 2024-01-01 | 2024-01-05 | John, Jane |
| 1.1 | Define Requirements | Gather and document requirements | 1.0 | 2 | 3 | 2024-01-01 | 2024-01-03 | John |
| 1.2 | Create Schedule | Develop project schedule | 1.0 | 2 | 2 | 2024-01-04 | 2024-01-05 | Jane |
| 2.0 | Development | Development phase | | 1 | 10 | 2024-01-06 | 2024-01-15 | Team |

### Column Descriptions:

- **ID**: Unique identifier for the WBS item (e.g., 1.0, 1.1, 2.0)
- **Name**: Task or deliverable name
- **Description**: Detailed description (optional)
- **Parent ID**: ID of the parent item for hierarchical structure (optional)
- **Level**: Hierarchical level (1 for top-level, 2 for sub-items, etc.)
- **Duration**: Estimated duration in days (optional)
- **Start Date**: Task start date (optional)
- **End Date**: Task end date (optional)
- **Resources**: Comma-separated list of assigned resources (optional)

## Usage

Run the script with your Google Sheet ID:

```bash
python main.py <spreadsheet_id> [range]
```

### Examples:

```bash
# Read from default range (Sheet1!A1:I100)
python main.py "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"

# Read from specific range
python main.py "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms" "WBS!A1:I50"
```

To find your spreadsheet ID:
- Open your Google Sheet in a browser
- The ID is in the URL: `https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit`

### Output

The script will:
1. Connect to Google Sheets and authenticate (if needed)
2. Read the WBS data from the specified sheet
3. Parse and validate the WBS items
4. Display the WBS tree structure in the console
5. Export the WBS items to `wbs_items.json`

Example output:
```
Connecting to Google Sheets...
Spreadsheet: Project WBS
Available sheets: Sheet1, WBS

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
    Description: Gather and document requirements
    Duration: 3.0 days
    Resources: John

  1.2 - Create Schedule
    Description: Develop project schedule
    Duration: 2.0 days
    Resources: Jane

✓ WBS items exported to wbs_items.json
✓ Total items created: 9
```

## Output File

The `wbs_items.json` file contains all WBS items in JSON format:

```json
[
  {
    "id": "1.0",
    "name": "Project Setup",
    "description": "Initial project setup",
    "parent_id": null,
    "level": 1,
    "duration": 5.0,
    "start_date": "2024-01-01",
    "end_date": "2024-01-05",
    "resources": ["John", "Jane"]
  }
]
```

## Project Structure

```
wbs_googlesheet/
├── main.py              # Main script to run the application
├── wbs_item.py          # WBS item data model
├── wbs_creator.py       # WBS parsing and creation logic
├── google_sheets.py     # Google Sheets API integration
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Troubleshooting

### "credentials.json not found" error
- Make sure you've downloaded the OAuth credentials from Google Cloud Console
- Save the file as `credentials.json` in the project root directory

### Authentication issues
- Delete `token.json` and re-authenticate
- Ensure the Google Sheets API is enabled in your Google Cloud Project

### "No data found" error
- Verify the spreadsheet ID is correct
- Check that the range name matches your sheet name
- Ensure the sheet is shared with your Google account

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.