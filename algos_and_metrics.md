# Research Topics and Metrics for Health Analysis

## TODO

- Add blood pressure metrics along with its overall insight impact.
- Read all the Python package documentation to determine which ones will be most useful to me.
- Outline the calculations that need to be done for each of the metrics.

---

## HRV Metrics

- HRV
- Heart Rate
- ECG

---

## Importance and Source of HRV and ECG Metrics
### !! Ordered by Importance !!

### Most Telling Metrics from ECG

1. **HRV Score (Weight: 9/10)**
   - Summarizes various measures.
   - Easily understood.
   - Tracks autonomic nervous system health.

2. **RMSSD (Weight: 8/10)**
   - Related to parasympathetic activity.
   - Quick to compute.

3. **SDNN (Weight: 7.5/10)**
   - Overall heart rate variability.
   - Needs more data.

4. **LF & HF Independently (Weight: 7/10)**
   - Reflects sympathetic and parasympathetic activities.
   - Needs interpretation.

5. **RR Intervals (Weight: 6.5/10)**
   - Raw data for many metrics.
   - Hard to interpret alone.

### Moderate Impact Metrics from ECG

1. **LF/HF Ratio (Weight: 6/10)**
   - Simplifies LF & HF.
   - Context matters.

### Least Telling Metrics from ECG

1. **Poincare Plot (SD1, SD2, SD1/SD2) (Weight: 4/10)**
   - Complex but informative.
   - Requires interpretation.

### Metrics that can be Adequately Derived from PPG HRV

- Note: All metrics are generally more accurate when derived from ECG. However, for convenience and continuous monitoring, PPG-derived HRV can be considered "good enough" for the following:

1. **LF & HF Independently (Weight: 5/10)**
   - For general trends and long-term monitoring.

2. **LF/HF Ratio (Weight: 4.5/10)**
   - For general context and lifestyle assessments.

3. **RR Intervals (Weight: 4/10)**
   - For a less accurate but more convenient option.

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
