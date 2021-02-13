import os.path
import io
import pytest
import atop_raw
from atop_raw import utils


def read_data(filename):
    root = os.path.dirname(__file__)
    real_filename = os.path.join(root, "data", filename)
    with open(real_filename, "rb") as f:
        data = f.read()
    return data


def test_read_all_in_right_order():
    data = read_data("atop_1_26_debian8_x86_64.log")
    stream = io.BytesIO(data)
    reader = atop_raw.create_reader(stream)
    for record in reader.records:
        record.header
        record.sstat
        record.pstats


def test_read_all_in_wrong_order():
    data = read_data("atop_1_26_debian8_x86_64.log")
    stream = io.BytesIO(data)
    reader = atop_raw.create_reader(stream)
    for record in reader.records:
        record.pstats
        record.header
        record.sstat


def test_skip_all_records():
    data = read_data("atop_1_26_debian8_x86_64.log")
    stream = io.BytesIO(data)
    reader = atop_raw.create_reader(stream)
    for _record in reader.records:
        pass


def test_processutils():
    data = read_data("atop_1_26_debian8_x86_64.log")
    stream = io.BytesIO(data)
    reader = atop_raw.create_reader(stream)
    for record in reader.records:
        report = utils.ProcessReport(reader, record.sstat)
        for pstat in record.pstats:
            cpu = report.get_cpu_percent(pstat)
            mem = report.get_mem_percent(pstat)
            assert cpu == pytest.approx(0.00742272, abs=0.0001)
            assert mem == pytest.approx(0.03105252, abs=0.0001)
            break
        break
