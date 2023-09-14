# Research Topics and Metrics for Health Analysis

## TODO

- Research how HRV and ECG are connected.
- Research the correlation between heart rate, blood pressure, and their relevance in HRV and ECG metrics.

---

## HRV Metrics

- HRV
- Heart Rate
- ECG

---

## HRV Algorithms

### Most Telling Metrics

1. **HRV Score**
    - Summarizes various measures.
    - Easily understood.
    - Tracks autonomic nervous system health.

2. **RMSSD**
    - Related to parasympathetic activity.
    - Quick to compute.

3. **SDNN**
    - Overall heart rate variability.
    - Needs more data.

### Moderate Impact Metrics

4. **LF & HF Independently**
    - Reflects sympathetic and parasympathetic activities.
    - Needs interpretation.

5. **LF/HF Ratio**
    - Simplifies LF & HF.
    - Context matters.

6. **RR Intervals**
    - Raw data for many metrics.
    - Hard to interpret alone.

### Least Telling Metrics

7. **Poincare Plot (SD1, SD2, SD1/SD2)**
    - Complex but informative.
    - Requires interpretation.

---

## Nervous System

- Sympathetic & Parasympathetic Coherence
    - More info from [Dr. Alan Watkins Part 1](https://youtu.be/q06YIWCR2Js?si=CEQqyBROOto1FCww) and [Part 2](https://youtu.be/Q_fFattg8N0?si=p20w-aUUBnXMgY6e)
- Nervous System Balance
- Vagal Tone
- "Balance" between SNS and PSNS

---

## Sleep Metrics

- Sleep stages (Wake, N1, N2, N3, REM)
- Total sleep time
- Respiratory rate

### Sleep Algorithms

- Sleep latency
- Sleep efficiency
- Sleep onset latency
- Wake after sleep onset
- Number of awakenings
- REM latency
- REM duration
- REM percentage

---

## Activity and Other Metrics

- Heart rate while exercising
- Resting heart rate
- Blood Pressure
- Mean arterial pressure
- Sunlight
- Meditation
- Screen Time
- Steps, general activity
- Body temperature?
- Emotional sentiment
- Medications

### Activity Algorithms

- Kerdo index
- FCI
- Pulse pressure
- Pulse wave velocity
- BCE Index
- Robinson Index
- Kvas Coefficient
- VO2/CO2 max

---

## Python Packages for Metrics and Algorithms

- HeartPy
- PyHRV
- PyEEG
- hrv
- biosppy
- hrv-analysis
- sleep-edf
- visbrain
- py-ecg-detectors

### Sentiment Analysis Packages

- textblob
- nltk
- spacy
- gensim
- polyglot
- flair
- fasttext
- transformers
- stanfordnlp
