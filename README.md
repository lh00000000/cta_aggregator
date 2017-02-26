

#####WIP

- /action
    - add a new action event
    - POST or PUT
    - body:  
```javascript
{
    "API_KEY": "...",
    "ACTION": {  
      "action_title": "The Last Battle", //title of action/event  
      "action_type": "EVENT", // enum "EVENT" or "PHONE"  
      "action_description": "The most important event ever.", // description of event  
      "start_time_ms": 0, // int, event start time in epoch // I should probably change this to seconds...
      "end_time_ms": 9999999999, //int, event start time as in epoch
      "has_cost": true, //boolean, if event is not free
      "contact_name": "Carly Rae Jepsen", // name of point-of-contact-person
      "contact_phone_email": "email@me.maybe", //point of contact person's phone number or email
      "instructions": "Do your best!", //string, can be something like call script
      "more_info": "zombo.com", //url for event details
      "location": "USA", //location of event, can be address or area etc (yes it should probably be another table)
      "tags":  "cool,rad,best" //optional comma delimited string of tags
    }
}
```
- /action/{UUID}
    - POST
    - upsert using UUID
    - body is same as above

- /action/{UUID}
    - GET
    - get event details as json

- /action/{UUID}/ical
    - GET
    - get event as ical (NOT IMPLEMENTED)

- /actions/{EVENT_TYPE}/{TIME_FILTER}
    - get back a bunch of events
    - PAGING NOT IMPLEMENTED YET
    - EVENT_TYPE : "ANY", "EVENT", or "PHONE"
    - TIME_FILTER : "ALL", "FUTURE"
        - "FUTURE" will not return events that have already ended at the time of call
