import { v4 as uuidv4 } from 'uuid';

// Replace this with your deployed Web App URL
const GOOGLE_SCRIPT_URL = 'YOUR_GOOGLE_SCRIPT_URL_HERE';

// Toggle this to false when you have deployed the script and updated the URL
const USE_MOCK = true;

// Mock Data for development
let mockData = [
    { id: '1', parentId: '', name: 'Project Start', duration: '1d', startDate: '2023-10-01', endDate: '2023-10-01', status: 'Done', assignedTo: 'Manager' },
    { id: '2', parentId: '', name: 'Planning Phase', duration: '5d', startDate: '2023-10-02', endDate: '2023-10-06', status: 'In Progress', assignedTo: 'Team' },
    { id: '3', parentId: '2', name: 'Gather Requirements', duration: '2d', startDate: '2023-10-02', endDate: '2023-10-03', status: 'Done', assignedTo: 'Alice' },
    { id: '4', parentId: '2', name: 'Design System', duration: '3d', startDate: '2023-10-04', endDate: '2023-10-06', status: 'In Progress', assignedTo: 'Bob' },
    { id: '5', parentId: '', name: 'Execution', duration: '10d', startDate: '2023-10-07', endDate: '2023-10-17', status: 'Pending', assignedTo: 'Team' }
];

export const fetchWBS = async () => {
    if (USE_MOCK) {
        console.log('Fetching mock data...');
        return new Promise(resolve => setTimeout(() => resolve(mockData), 500));
    }

    try {
        const response = await fetch(GOOGLE_SCRIPT_URL, {
            method: 'GET'
        });
        return await response.json();
    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
};

export const addWBSItem = async (item) => {
    if (USE_MOCK) {
        const newItem = { ...item, id: uuidv4() };
        mockData.push(newItem);
        return Promise.resolve({ status: 'success', data: newItem });
    }

    const payload = { action: 'add', item: { ...item, id: uuidv4() } };
    return sendPost(payload);
};

export const updateWBSItem = async (item) => {
    if (USE_MOCK) {
        const index = mockData.findIndex(d => d.id === item.id);
        if (index !== -1) {
            mockData[index] = { ...mockData[index], ...item };
            return Promise.resolve({ status: 'success', data: mockData[index] });
        }
        return Promise.reject('Item not found');
    }

    const payload = { action: 'update', item };
    return sendPost(payload);
};

export const deleteWBSItem = async (id) => {
    if (USE_MOCK) {
        mockData = mockData.filter(d => d.id !== id);
        return Promise.resolve({ status: 'success', id });
    }

    const payload = { action: 'delete', id };
    return sendPost(payload);
};

const sendPost = async (payload) => {
    // Google Apps Script requires CORS handling. 
    // 'no-cors' mode sends the request but we can't read the response directly if the script handles it a certain way,
    // but usually for JSON APIs we want standard CORS.
    // The 'echo' script provided uses ContentService which supports CORS redirects.

    // Note: fetch POST to Google Script often requires 'no-cors' OR proper setup.
    // With 'ContentService' and 'text/plain', it often works better across domains without preflight issues.
    // Actually, standard fetch works if the script is deployed as "Anyone".

    // However, simple POSTs are often blocked by CORS policies. Use 'no-cors' effectively means fire and forget or opaque response.
    // To get read response, we usually need the server to send Access-Control-Allow-Origin: *.
    // Apps Script does this automatically for "Anyone" access with GET, but POST is tricky.
    // A common workaround is using text/plain to avoid preflight options.

    try {
        const response = await fetch(GOOGLE_SCRIPT_URL, {
            method: 'POST',
            body: JSON.stringify(payload)
            // Headers mostly omitted to force simple request
        });
        return await response.json();
    } catch (error) {
        console.error("API POST Error:", error);
        throw error;
    }
};
