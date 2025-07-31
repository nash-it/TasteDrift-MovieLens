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

