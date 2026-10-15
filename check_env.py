import sys, psutil, pyqtgraph, PySide6
from PySide6 import QtWidgets
import pynvml

print('Python  :', sys.version.split()[0])
print('PySide6 :', PySide6.__version__)
print('CPU     :', psutil.cpu_count(logical=True), 'logical cores,', psutil.cpu_percent(interval=0.5), '%')
print('RAM     :', round(psutil.virtual_memory().total / 2**30, 1), 'GiB total')
try:
    pynvml.nvmlInit()
    h = pynvml.nvmlDeviceGetHandleByIndex(0)
    name = pynvml.nvmlDeviceGetName(h)
    mem = pynvml.nvmlDeviceGetMemoryInfo(h)
    util = pynvml.nvmlDeviceGetUtilizationRates(h)
    temp = pynvml.nvmlDeviceGetTemperature(h, pynvml.NVML_TEMPERATURE_GPU)
    print('GPU     :', name, '|', round(mem.total / 2**30, 1), 'GiB VRAM |', util.gpu, '% |', temp, 'C')
    pynvml.nvmlShutdown()
except Exception as e:
    print('GPU     : NVML not available ->', e)
