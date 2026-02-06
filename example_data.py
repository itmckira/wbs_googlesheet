"""
Example WBS data for testing and demonstration purposes
"""

# Sample WBS data that could come from a Google Sheet
SAMPLE_WBS_DATA = [
    ['ID', 'Name', 'Description', 'Parent ID', 'Level', 'Duration', 'Start Date', 'End Date', 'Resources'],
    ['1.0', 'Project Setup', 'Initial project setup', '', '1', '5', '2024-01-01', '2024-01-05', 'John, Jane'],
    ['1.1', 'Define Requirements', 'Gather and document requirements', '1.0', '2', '3', '2024-01-01', '2024-01-03', 'John'],
    ['1.2', 'Create Schedule', 'Develop project schedule', '1.0', '2', '2', '2024-01-04', '2024-01-05', 'Jane'],
    ['2.0', 'Development', 'Development phase', '', '1', '10', '2024-01-06', '2024-01-15', 'Team'],
    ['2.1', 'Backend Development', 'Develop backend APIs', '2.0', '2', '5', '2024-01-06', '2024-01-10', 'Alice, Bob'],
    ['2.2', 'Frontend Development', 'Develop user interface', '2.0', '2', '5', '2024-01-11', '2024-01-15', 'Carol, Dave'],
    ['3.0', 'Testing', 'Quality assurance and testing', '', '1', '5', '2024-01-16', '2024-01-20', 'QA Team'],
    ['3.1', 'Unit Testing', 'Test individual components', '3.0', '2', '2', '2024-01-16', '2024-01-17', 'Alice, Bob'],
    ['3.2', 'Integration Testing', 'Test system integration', '3.0', '2', '3', '2024-01-18', '2024-01-20', 'QA Team'],
]


def get_sample_wbs_data():
    """Return sample WBS data."""
    return SAMPLE_WBS_DATA
