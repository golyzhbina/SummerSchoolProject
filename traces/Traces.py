from dataclasses import dataclass


@dataclass
class Traces:
    sample_interval_in_s: int
    amount_samples: int
    length_of_trace: int
    traces: list
