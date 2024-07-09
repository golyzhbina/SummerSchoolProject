from obspy.io.segy.core import _read_segy
from obspy.core.util import get_example_file
from traces.Traces import Traces
from traces.TracesFilter import TracesFilter


class TracesReader:

    @staticmethod
    def read_traces(filename: str) -> Traces:
        file = _read_segy(get_example_file(filename), unpack_trace_headers=True)
        interval = file[0].stats.segy.trace_header["sample_interval_in_ms_for_this_trace"] / 1000 # in milliseconds
        amount_samples = file[0].stats.segy.trace_header["number_of_samples_in_this_trace"]
        traces = []

        for i in range(len(file)):
            traces.append(file[i].data)

        traces = TracesFilter.filter_traces(traces)

        return Traces(interval, amount_samples, amount_samples * interval, traces)

