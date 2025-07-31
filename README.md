# Taste Drift in Movie Preferences: A Behavioral Clustering Project

This project explores how user preferences for movie genres change over time using the [MovieLens 1M dataset](https://grouplens.org/datasets/movielens/1m/). We simulate a taste evolution model — inspired by how music apps like Spotify might track changes in musical mood — by building an ML pipeline that clusters users based on how their genre preferences shift over time.

---

## Objective

> Analyze behavioral drift in entertainment taste by:
>
> * Tracking how individual movie genre preferences change from early to late periods
> * Grouping users with similar behavioral changes using unsupervised learning

🔍 **Note:** This project began as a proxy for modeling music taste drift. While music taste depends on deeper audio features, lyrics, and emotion — this implementation uses movie genres as a stand-in to simulate the same core concept: **temporal evolution of user preference.**

---

## Project Structure

```bash
TasteDrift-MovieLens/
├── data/
│   ├── raw/              # Unzipped MovieLens 1M
│   └── processed/        # Cleaned + derived features
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_dashboard_reporting.ipynb
├── src/
│   └── data_loader.py    # Modular dataset loader
├── logs/
├── tests/
├── requirements.txt
└── README.md
```

---

## Pipeline Overview

### 1. Notebook 1: Data Exploration

* Loaded MovieLens ratings and movie metadata
* Parsed timestamps, merged genre info
* Explored trends in user activity, genres, and rating timelines

### 2. Notebook 2: Feature Engineering

* Split each user’s timeline into **early** and **late** buckets
* Built user × genre taste vectors (early vs. late preferences)
* Saved normalized vectors to CSV

### 3. Notebook 3: Modeling

* Applied **StandardScaler** + **UMAP** for dimensionality reduction
* Clustered users using **KMeans**
* Visualized clusters and taste transitions

### 4. Notebook 4: Dashboard & Reporting

* Visualized cluster distributions, taste shift timelines, and genre preferences
* Merged user clusters back to rating data for insight analysis

---

## Sample Visuals

> You can add screenshots here:

* UMAP cluster visual
* Bar plot of genre shift
* Ratings over time by cluster

---

## Limitations

* Movie genres are coarse-grained vs. music features like beats, lyrics, and energy
* No user demographics (age, location, etc.) to refine personalization
* Can’t directly map to Spotify-style emotional/tone tracking

Yet, this still demonstrates:

* ✅ Taste drift modeling
* ✅ Full ML pipeline from ingestion to dashboard
* ✅ Real-world job readiness in behavioral modeling

---

## How to Run

```bash
# Clone repo and enter folder
$ git clone https://github.com/yourusername/TasteDrift-MovieLens.git
$ cd TasteDrift-MovieLens

# Install dependencies
$ pip install -r requirements.txt

# Run notebooks in order:
notebooks/01_data_exploration.ipynb
notebooks/02_feature_engineering.ipynb
notebooks/03_modeling.ipynb
notebooks/04_dashboard_reporting.ipynb
```

---

## Inspired By

* Spotify’s evolving taste analysis
* Music mood detection
* Temporal collaborative filtering

---

## Contact

If you liked this project or want to collaborate on a real-world recommender system or behavior modeling application — [connect with me on LinkedIn](https://www.linkedin.com/in/gnanesh-reddy17/)!
