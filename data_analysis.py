# TODO: Add the following algorithms and metrics:
# - HRV Algorithms and Metrics:
    # - InRMSSD
    # - RMSSD
    # - SDNN
    # - NN50
    # - pNN50
    # - Poincare plot (SD1, SD2, SD1/SD2)
    # - Simple Entropy and Approximate Entropy
    # - TINN
    # - LF/HF ratio
    # - Mean RR
    # - MxDMn
    # - Moda
    # - AMo50
    # - CV

# - Sleep Algorithms and Metrics:
    # - Sleep stages (Wake, N1, N2, N3, REM)
    # - Sleep latency
    # - Sleep efficiency
    # - Sleep onset latency
    # - Wake after sleep onset
    # - Number of awakenings
    # - Total sleep time
    # - REM latency
    # - REM duration
    # - REM percentage
    # - Respiratory rate
    # - Add more later

# - Activity Algorithms and Metrics:
    # - HRV
    # - Heart rate while exercising
    # - Resting heart rate
    # - Blood Pressure
    # - ECGs?
    # - Mean arterial pressure
    # - Kerdo index
    # - FCI
    # - Pulse pressure
    # - Pulse wave velocity
    # - BCE Index
    # - Robinson Index
    # - Kvas Coefficient
    # - Sunlight
    # - Screen Time
    # - Steps, general activity
    # - Body temperature?
    # - Emotional sentiment
    # - Medications
    # - VO2/CO2 max

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.stats as stats
import math

