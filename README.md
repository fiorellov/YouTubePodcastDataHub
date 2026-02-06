# YouTube Podcast Analysis  
### A Multimodal Study of Audio, Visual, and Engagement Dynamics

This project analyzes the evolution and performance of podcast content on **YouTube**, combining **audio signal processing**, **natural language processing**, **computer vision**, and **statistical modeling**.

The goal is to understand which factors influence **views, likes, comments, and audience sentiment** in long-form podcast content, with a specific focus on how podcasts have adapted to YouTube as a primary distribution platform.

---

## Project Overview

The analysis focuses on **24 of the most popular U.S.-based podcast channels on YouTube** (May 2024), selected from public rankings.  
Across these channels, the project examines:

- Publishing behavior and frequency  
- Topic evolution over time  
- Audience sentiment in comments  
- Audio feature evolution  
- Visual design choices (frames and thumbnails)  
- Statistical drivers of engagement  

The project adopts a **data-driven, multimodal approach**, integrating structured metadata with unstructured text, audio, and visual data.

---

## Dataset Summary

| Component | Size |
|---------|------|
| Podcast channels | 24 |
| Episodes analyzed | 13,756 |
| Transcripts | 13,218 |
| Audio files | ~7,500 |
| Audio duration | ~2,765 hours |
| Comments | 18M+ |
| Filtered comments (sentiment) | ~6M |

---

## Data Collection

### Metadata
- Episode title, description, views, likes, duration, publication date
- Channel-level metadata (subscribers, channel age, total views)

### Transcripts
- Retrieved through YouTube APIs
- Stored as CSV files for NLP processing

### Comments
- Collected using YouTube Data API (Google Console tokens)
- Stored as JSON
- Over 18 million comments processed

### Audio
- Extracted using:
  - `Pytube`
  - `FFmpeg`
  - `Pydub`
  - `Librosa`
- Normalized and resampled to 44.1 kHz
- Parallel processing with **Dask (32 cores)**

### Visual Assets
- Thumbnails downloaded via `requests`
- Video frames extracted using `OpenCV`
- Scene changes detected via grayscale histogram correlation
- Duplicate frames removed using perceptual hashing (`imagehash.phash`)

---

## Topic Extraction

Topics are inferred from podcast transcripts using **embedding-based classification**.

### Topic Set
- Politics  
- Sports  
- Economy  
- Health  
- Technology  
- Culture  
- Education  
- Environment  
- Crime  
- Entertainment  
- Music  

### Methodology
- Text preprocessing (regex cleanup, tokenization, normalization)
- Word embeddings via **Word2Vec (Google News, 300d)**
- Transcript vectors computed as mean word embeddings
- Topic vectors built from curated keyword sets
- Assignment via **cosine similarity**

A qualitative evaluation on a subset of episodes shows acceptable directional accuracy, with known classification noise.

---

## Sentiment Analysis

Audience perception is analyzed through **YouTube comments**.

### Model
- **VADER (Valence Aware Dictionary and sEntiment Reasoner)**

### Processing Steps
- Removal of URLs, mentions, hashtags
- Normalization of social-text artifacts
- Sentiment polarity scoring (neg / neu / pos / compound)

### Filtering
- Only comments with `compound > 0.6` retained
- Final sentiment dataset: ~6 million comments

### Key Insight
Positive sentiment dominates overall, but **negative sentiment increases over time**, likely reflecting higher polarization, topic sensitivity, or stronger audience engagement.

---

## Audio Feature Analysis

Audio analysis investigates how podcast sound design has evolved and how it correlates with engagement.

### Extracted Features
- RMS energy
- Pitch (mean, std)
- Speech tempo
- Zero-crossing rate
- Spectral centroid & roll-off
- MFCCs (1–7)
- Higher-order statistics (kurtosis, skewness)

### Findings
- A noticeable shift occurs around late 2019
- Early phase: higher energy and aggressive delivery
- Post-2020: lower intensity, clearer and brighter sound
- Likely optimization for mobile listening and long-duration comfort

---

## Visual Analysis: Frames & Thumbnails

### Frame Color Analysis
- Representative frames extracted per scene
- Dominant colors identified via K-means clustering
- Converted to HSL and stripped of saturation/lightness
- Analysis conducted on **Hue only**

**Result:**  
A clear long-term shift from cooler palettes to **warmer tones**, associated with comfort, familiarity, and viewer retention.

### Thumbnail Analysis
- Same pipeline applied to thumbnails
- Even stronger dominance of warm, saturated colors
- Reflects attention capture and click-optimization strategies

---

## Engagement Modeling

### Dependent Variables
- Views  
- Likes  
- Comments  

### Model
- **Negative Binomial Regression**
- Chosen due to overdispersion in count data
- Robust covariance estimation
- Audio features standardized (z-score)

### Key Drivers

**Views**
- Lower pitch (deeper voices)
- Specific MFCC coefficients
- Longer videos
- Larger subscriber base
- Both vivid and darker visual tones

**Likes**
- Clearer, high-frequency audio
- Brighter and more saturated thumbnails
- Higher frame hue values
- Presence of people in thumbnails
- Shorter duration videos perform better

**Comments**
- Faster tempo
- Visually vivid thumbnails
- Higher color intensity
- More faces in thumbnails
- Decline with video age and duration

---

## Limitations

- Audio features available for ~40% of episodes
- Topic classification is dictionary-driven, not generative
- Results are observational and correlational
- Platform-specific dynamics (YouTube) may not generalize fully

---

## Technologies Used

- Python
- Google API
- Librosa, Pydub, FFmpeg
- OpenCV
- Scikit-learn
- Word2Vec
- VADER
- Dask
- Altair
- Vega / Vega-Lite
- Flourish

---

## Purpose of the Project

This project is intended as:

- A **data journalism case study**
- A **multimodal analytics pipeline**
- A **research-oriented exploration of digital media design**
- A foundation for future work on recommender systems, creator optimization, and platform studies

---

## License

This project is provided for **research and educational purposes**.
---