import dataclasses


@dataclasses.dataclass
class PhaseRequestSchema:
    customNames: list = dataclasses.field(default_factory=lambda: [])
    templateIds: list = dataclasses.field(default_factory=lambda: ["57871931437d35620b630b38"])


@dataclasses.dataclass
class PhaseResponseSchema:
    _original: str
    name: str
    created: str
    status_code: int


@dataclasses.dataclass
class DeletePhaseResponseSchema:
    _original: str
    name: str
    created: str
    status_code: int
