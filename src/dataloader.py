#!/usr/bin/env python
# coding: utf-8

# In[2]:


#src/data_loader.py
import logging
from pathlib import Path
import pandas as pd
from io import BytesIO
import logging

def fetch_and_prepare_movielens_1m(data_folder = "/Users/gnaneshreddysaireddy/Documents/TasteDrift-MovieLens/data/raw/ml-1m", allow_download = False) -> pd.DataFrame:
    
    logging.info ("Starting load of MovieLeses 1M from local folder...")
    
    data_folder = Path(data_folder)
    ratings_path = data_folder / "ratings.dat"
    movies_path = data_folder / "movies.dat"
    
    #check files exist
    
    if not ratings_path.exists() or not movies_path.exists():
        raise FileNotFoundError(
                    f"Missing required files in {data_folder}. please manually download and extract MovieLnes 1M "
                    "from https://grouplense.org/datasets/movieslens/1m/"
        )
        
    ratings = pd.read_csv(ratings_path, sep = "::", engine = "python",
                              names = ["user_id", "movie_id","rating","timestamp"],encoding="latin-1")
    movies = pd.read_csv(movies_path, sep = "::", engine = "python",
                            names = ["movie_id","title", "genres"],encoding="latin-1")
    
    ratings["datetime"] = pd.to_datetime(ratings["timestamp"], unit = 's')
        
    df = ratings.merge(movies, on="movie_id")
    logging.info(f"Loaded dataset: {df.shape[0]:,} rows, {df['user_id'].nunique()} users.")
        
        
    return df
                     
   

