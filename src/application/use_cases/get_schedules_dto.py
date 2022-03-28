from dataclasses import dataclass, field


@dataclass
class GetSchedulesOutput:
    schedules: list = field(default_factory=list)
