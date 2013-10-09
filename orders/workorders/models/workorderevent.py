from events.mixins import ReferenceEvent, WorkflowCompareMixin
from events.models import Event


class WorkOrderEvent(Event, WorkflowCompareMixin):
    pass