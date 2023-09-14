TODO: Research how HRV and ECG are connected. Also research how heart rate and blood pressure can be looped (or not 
looped) into the functions of those metrics and their relevance towards getting meaningful deductions from our analysis.

- **HRV Metrics:**
    - HRV
    - Heart Rate
    - ECG


- **HRV Algorithms:**
    - HRV Score
    - InRMSSD
      - Logarithmic transformation of RMSSD.
    - RMSSD
      - A measure to quantify the variability in RR intervals.
      - Focuses on short-term fluctuations, often related to respiratory influences.
    - SDNN
      - A measure of the variability in the time between all pairs of consecutive heartbeats (NN intervals).
      - Gives a broader view, capturing long-term fluctuations.
    - NN50
      - Counts how many NN intervals differ by more than 50 ms.
    - pNN50
      - Proportional version of NN50, more interpretable. `(NN50/Total NN Intervals) x 100`
    - Poincare plot (SD1, SD2, SD1/SD2)
      - Visual insight into heart rate dynamics. Patterns can indicate different physiological or pathological states.
    - Simple Entropy and Approximate Entropy
    - LF & HF
    - LF/HF ratio
    - RR Intervals
      - The time intervals between consecutive R-peaks in an ECG. Usually measured in milliseconds.
    - MxDMn
      - The maximum minus the minimum NN interval. Reflects extreme variability.
    - Moda
    - AMo50
      - The average of NN intervals differing by more than 50ms. A sort of blend between RMSSD and NN50.
    - CV
    - TINN
    - FFT (Fast Fourier Transform)
      - Potentially for ECGs, check for HRV too

---

- **Nervous System:**
  - Sympathetic & Parasympathetic Coherence
    - More info from Dr. Alan Watkins [Part 1](https://youtu.be/q06YIWCR2Js?si=CEQqyBROOto1FCww) and [Part 2](https://youtu.be/Q_fFattg8N0?si=p20w-aUUBnXMgY6e)
  - Nervous System Balance (separate from coherence)
  - Vagal Tone (from HRV)
  - "Balance" between SNS and PSNS

---

- **Sleep Metrics:**
    - Sleep stages (Wake, N1, N2, N3, REM)
    - Total sleep time
    - Respiratory rate


- **Sleep Algorithms:**
    - Sleep latency
    - Sleep efficiency
    - Sleep onset latency
    - Wake after sleep onset
    - Number of awakenings
    - REM latency
    - REM duration
    - REM percentage

---

- **Activity and Other Metrics:**
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


- **Activity Algorithms:**
    - Kerdo index
    - FCI
    - Pulse pressure
    - Pulse wave velocity
    - BCE Index
    - Robinson Index
    - Kvas Coefficient
    - VO2/CO2 max

---

- **Python Packages:**
    - Metrics and Algos:
      - HeartPy
      - PyHRV
      - PyEEG
      - hrv
      - biosppy
      - hrv-analysis
      - sleep-edf
      - visbrain
      - py-ecg-detectors
    - Sentiment Analysis
      - textblob
      - nltk
      - spacy
      - gensim
      - polyglot
      - flair
      - fasttext
      - transformers
      - stanfordnlp