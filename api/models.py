from django.db import models
import uuid


class Action(models.Model):
    ACTION_TYPE_EVENT = 'EVENT'
    ACTION_TYPE_PHONE = 'PHONE'

    ACTION_TYPE_CHOICES = (
        (ACTION_TYPE_EVENT, 'Event'),
        (ACTION_TYPE_PHONE, 'Phone')
    )

    event_uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    event_creator_uid = models.UUIDField(default=uuid.uuid4)
    action_title = models.CharField(max_length=256)
    action_description = models.CharField(max_length=2048)
    action_type = models.CharField(max_length=5, choices=ACTION_TYPE_CHOICES)
    has_cost = models.BooleanField(default=False)
    more_info = models.URLField()
    start_time_ms = models.IntegerField()  # TODO use date field
    end_time_ms = models.IntegerField()
    contact_name = models.CharField(max_length=256)
    contact_phone_email = models.CharField(
        max_length=256)  # TODO foreign key for contacts
    # TODO foreign key for event locations
    location = models.CharField(max_length=256)

    tags = models.CharField(max_length=1024, blank=True)
    instructions = models.CharField(max_length=2048, blank=True)

    def to_ical(self):
        return

    @staticmethod
    def valid_payload(payload):
        # check json to see if you can make action from it
        fields = ["action_title",
                  "action_description",
                  "action_type",
                  "has_cost",
                  "more_info",
                  "start_time_ms",
                  "end_time_ms",
                  "contact_name",
                  "contact_phone_email",
                  "location"]
        return all(field in fields for field in payload)
