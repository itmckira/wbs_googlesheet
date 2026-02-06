"""
WBS Item Data Model

This module defines the Work Breakdown Structure (WBS) item model.
"""

class WBSItem:
    """Represents a Work Breakdown Structure item."""
    
    def __init__(self, id, name, description="", parent_id=None, level=1, 
                 duration=0, start_date=None, end_date=None, resources=None):
        """
        Initialize a WBS item.
        
        Args:
            id: Unique identifier for the WBS item
            name: Name/title of the WBS item
            description: Detailed description of the item
            parent_id: ID of the parent item (None for root items)
            level: Hierarchical level in the WBS structure
            duration: Estimated duration (in days)
            start_date: Start date of the task
            end_date: End date of the task
            resources: List of assigned resources
        """
        self.id = id
        self.name = name
        self.description = description
        self.parent_id = parent_id
        self.level = level
        self.duration = duration
        self.start_date = start_date
        self.end_date = end_date
        self.resources = resources or []
    
    def __repr__(self):
        return f"WBSItem(id={self.id}, name='{self.name}', level={self.level})"
    
    def to_dict(self):
        """Convert WBS item to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'parent_id': self.parent_id,
            'level': self.level,
            'duration': self.duration,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'resources': self.resources
        }
    
    def display(self):
        """Display WBS item in a readable format."""
        indent = "  " * (self.level - 1)
        output = f"{indent}{self.id} - {self.name}"
        if self.description:
            output += f"\n{indent}  Description: {self.description}"
        if self.duration:
            output += f"\n{indent}  Duration: {self.duration} days"
        if self.resources:
            output += f"\n{indent}  Resources: {', '.join(self.resources)}"
        return output
