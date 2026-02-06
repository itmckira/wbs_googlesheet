# Google Apps Script Setup Instructions

1.  **Create a new Google Sheet**.
2.  Go to **Extensions** > **Apps Script**.
3.  Delete any code in the `Code.gs` file and paste the contents of `backend/Code.js` (from this project).
4.  **Save** the project.
5.  **Deploy as Web App**:
    *   Click **Deploy** > **New deployment**.
    *   Select type: **Web app**.
    *   Description: "WBS API".
    *   **Execute as**: Me (your email).
    *   **Who has access**: **Anyone** (This is important for the web app to access it without complex OAuth for now. If you need security, we can refine this later, but "Anyone" allows the simplest CORS access).
6.  Click **Deploy**.
7.  **Copy the Web App URL** (it ends with `/exec`).
8.  You will need this URL for the details step.
