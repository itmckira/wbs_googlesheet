/**
 * Serve the WBS data as JSON.
 */
function doGet(e) {
  const sheet = getSheet();
  const data = getData(sheet);
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Handle Add, Update, Delete actions.
 */
function doPost(e) {
  const sheet = getSheet();
  let result = {};
  
  try {
    const body = JSON.parse(e.postData.contents);
    const action = body.action;
    
    if (action === 'add') {
      result = addItem(sheet, body.item);
    } else if (action === 'update') {
      result = updateItem(sheet, body.item);
    } else if (action === 'delete') {
      result = deleteItem(sheet, body.id);
    } else {
      throw new Error('Unknown action: ' + action);
    }
    
    return ContentService.createTextOutput(JSON.stringify({ status: 'success', data: result }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// --- Helpers ---

const SHEET_NAME = 'WBS_Data';
const HEADERS = ['id', 'parentId', 'name', 'duration', 'startDate', 'endDate', 'status', 'assignedTo'];

function getSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(HEADERS);
  }
  return sheet;
}

function getData(sheet) {
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return []; // Only headers
  
  const headers = data[0];
  const rows = data.slice(1);
  
  return rows.map(row => {
    let obj = {};
    headers.forEach((h, i) => {
      obj[h] = row[i];
    });
    return obj;
  });
}

function addItem(sheet, item) {
  const row = HEADERS.map(h => item[h] || '');
  sheet.appendRow(row);
  return item;
}

function updateItem(sheet, item) {
  const data = sheet.getDataRange().getValues();
  // Find row by ID (Index 0 is ID)
  // Data array includes headers, so row index maps directly if we account for that.
  // Actually, getValues() is 0-indexed. Sheet rows are 1-indexed.
  
  const idIndex = HEADERS.indexOf('id');
  if (idIndex === -1) throw new Error('ID column not found');
  
  for (let i = 1; i < data.length; i++) {
    if (data[i][idIndex] == item.id) {
       const newRow = HEADERS.map(h => item[h] === undefined ? data[i][HEADERS.indexOf(h)] : item[h]);
       sheet.getRange(i + 1, 1, 1, HEADERS.length).setValues([newRow]);
       return item;
    }
  }
  throw new Error('Item not found: ' + item.id);
}

function deleteItem(sheet, id) {
  const data = sheet.getDataRange().getValues();
  const idIndex = HEADERS.indexOf('id');
  
  for (let i = 1; i < data.length; i++) {
    if (data[i][idIndex] == id) {
      sheet.deleteRow(i + 1);
      return { id: id, deleted: true };
    }
  }
  throw new Error('Item not found: ' + id);
}
