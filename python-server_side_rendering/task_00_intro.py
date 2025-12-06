#!/usr/bin/python3
"""
Template-based invitation generator.
"""

import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from template and attendee data.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries with attendee data
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Check if all items in attendees are dictionaries
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i} is not a dictionary")
            return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Start with the template
        invitation = template
        
        # Replace placeholders with data or "N/A" if missing
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A')
        event_date = attendee.get('event_date', 'N/A')
        event_location = attendee.get('event_location', 'N/A')
        
        # Replace all occurrences of each placeholder
        invitation = invitation.replace('{name}', str(name))
        invitation = invitation.replace('{event_title}', str(event_title))
        invitation = invitation.replace('{event_date}', str(event_date))
        invitation = invitation.replace('{event_location}', str(event_location))
        
        # Write to file
        filename = f'output_{i}.txt'
        try:
            with open(filename, 'w') as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
