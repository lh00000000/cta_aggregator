

#####WIP

/action
    - add a new action event
    - POST or PUT
    - body:
        ```
        {
            "API_KEY": "...",
            "ACTION": {
              "action_title": title of action/event
              "action_type": "EVENT" or "PHONE"
              "action_description": description of event
              "start_time_ms": event start time as utc ms since epoch
              "end_time_ms": event start time as utc ms since epoch
              "has_cost": boolean, if event is not free
              "contact_name": name of point-of-contact-person
              "contact_phone_email": point of contact person's phone number or email
              "instructions": string, can be something like call script
              "more_info": url for event details
              "location": location of event, can be address or area etc (yes it should probably be another table)
              "tags":  optional comma delimited string of tags
            }
        }
        ```
/action/{UUID}
    - POST
    - upsert using UUID
    - body is same as above

/action/{UUID}
    - GET
    - get event details as json

/action/{UUID}/ical
    - GET
    - get event as ical (NOT IMPLEMENTED)

/actions/{EVENT_TYPE}/{TIME_FILTER}
    - get back a bunch of events
    - PAGING NOT IMPLEMENTED YET
    - EVENT_TYPE : "ANY", "EVENT", or "PHONE"
    - TIME_FILTER : "ALL", "FUTURE"
        - "FUTURE" will not return events that have already ended at the time of call