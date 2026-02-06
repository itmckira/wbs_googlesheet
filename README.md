# WBS Management Web App

A modern, glassmorphism-styled Work Breakdown Structure (WBS) management tool backed by Google Sheets.

## Features

- **Google Sheets Database**: Uses Google Sheets as a free, accessible backend.
- **Tree View Interface**: Visualize projects with hierarchical tasks.
- **Real-time Updates**: Add, Edit, and Delete tasks (requires backend setup).
- **Premium UI**: Built with React and Vanilla CSS, featuring glassmorphism and dark mode.

## Setup Instructions

### 1. Prerequisites
- Node.js installed.
- A Google Account (for Google Sheets).

### 2. Frontend Setup
```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

### 3. Backend Setup (Google Sheets)
1. Create a new Google Sheet.
2. Go to **Extensions** > **Apps Script**.
3. Copy the content of `backend/Code.js` into the script editor.
4. Deploy as a **Web App** (Execute as: "Me", Who has access: "Anyone").
5. Copy the **Web App URL**.

### 4. Connect Frontend to Backend
1. Open `src/api.js`.
2. Set `USE_MOCK = false`.
3. Paste your Web App URL into `GOOGLE_SCRIPT_URL`.

## Technologies
- Vite
- React
- Lucide React (Icons)
- Google Apps Script

## License
MIT
