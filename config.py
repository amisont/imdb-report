import os

# === PATHS ===
RAW_DATA_DIR = os.path.join('data', 'raw')
PROCESSED_DATA_DIR = os.path.join('data', 'processed')

TITLE_BASICS_FILE = os.path.join(RAW_DATA_DIR, "title.basics.tsv")
TITLE_RATINGS_FILE = os.path.join(RAW_DATA_DIR, "title.ratings.tsv")
TITLE_PRINCIPALS_FILE = os.path.join(RAW_DATA_DIR, "title.principals.tsv")
TITLE_CREW_FILE = os.path.join(RAW_DATA_DIR, "title.crew.tsv")
TITLE_AKAS_FILE = os.path.join(RAW_DATA_DIR, "title.akas.tsv")
TITLE_EPISODE_FILE = os.path.join(RAW_DATA_DIR, "title.episode.tsv")
NAME_BASICS_FILE = os.path.join(RAW_DATA_DIR, "name.basics.tsv")

# Output file names
TITLE_BASICS_FILTERED_FILE = os.path.join(PROCESSED_DATA_DIR, "title.basics.filtered.tsv")
TITLE_RATINGS_FILTERED_FILE = os.path.join(PROCESSED_DATA_DIR, "title.ratings.filtered.tsv")
TITLE_PRINCIPALS_FILTERED_FILE = os.path.join(PROCESSED_DATA_DIR, "title.principals.filtered.tsv")
TITLE_CREW_FILTERED_FILE = os.path.join(PROCESSED_DATA_DIR, "title.crew.filtered.tsv")
TITLE_AKAS_FILTERED_FILE = os.path.join(PROCESSED_DATA_DIR, "title.akas.filtered.tsv")
TITLE_EPISODE_FILTERED_FILE = os.path.join(PROCESSED_DATA_DIR, "title.episode.filtered.tsv")
NAME_BASICS_FILTERED_FILE = os.path.join(PROCESSED_DATA_DIR, "name.basics.filtered.tsv")

# === FILTER CHOICES ===
TITLE_TYPES = ['movie', 'tvSeries']    # Types to keep
MIN_YEAR = 1995                       # Minimum startYear
NOT_ADULT = '0'                        # Only non-adult
MIN_NUM_VOTES = 1000                  # Minimum number of votes

# Principals (cast/crew) roles to keep
PRINCIPALS_CATEGORIES = ['actor', 'actress', 'director', 'writer']

# Chunksize for large file processing
CHUNKSIZE = 1_000_000