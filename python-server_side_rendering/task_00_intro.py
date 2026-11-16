#!/usr/bin/python3

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):

        data = {
            "name": attendee.get("name") or "N/A",
            "event_title": attendee.get("event_title") or "N/A",
            "event_date": attendee.get("event_date") or "N/A",
            "event_location": attendee.get("event_location") or "N/A"
        }

        invitation = template.format(**data)

        filename = "output_{}.txt".format(index)

        try:
            with open(filename, "w") as file:
                file.write(invitation)

            print("Created {}".format(filename))

        except OSError as error:
            print("Error creating {}: {}".format(filename, error))

