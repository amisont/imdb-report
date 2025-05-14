import pandas as pd
import os
import config

def ensure_dir_exists(path):
    """Ensure the output directory exists."""
    os.makedirs(path, exist_ok=True)

def filter_title_basics():
    """Filter the title.basics file with config-specified criteria and return filtered DataFrame and tconst set."""
    print("Filtering title.basics...")
    basics = pd.read_csv(config.TITLE_BASICS_FILE, sep='\t', dtype=str, na_values='\\N')
    ratings = pd.read_csv(config.TITLE_RATINGS_FILE, sep='\t', dtype=str, na_values='\\N')

    basics = basics.merge(ratings[['tconst', 'numVotes']], on='tconst', how='left')
    basics['startYear'] = pd.to_numeric(basics['startYear'], errors='coerce')
    basics['numVotes'] = pd.to_numeric(basics['numVotes'], errors='coerce').fillna(0).astype(int)

    mask = (
        basics['titleType'].isin(config.TITLE_TYPES) &
        (basics['startYear'] >= config.MIN_YEAR) &
        (basics['isAdult'] == config.NOT_ADULT) &
        (basics['numVotes'] >= config.MIN_NUM_VOTES)
    )
    filtered = basics[mask]
    tconst_set = set(filtered['tconst'])
    print(f"Filtered title.basics: {len(filtered)} records.")

    return filtered, tconst_set

def filter_file_by_id(input_file, output_file, id_set, id_column='tconst', chunksize=None):
    """
    Filter any TSV file by an ID column (defaults to tconst, but can handle titleId or others).
    
    Args:
        input_file: Path to input file
        output_file: Path to output file
        id_set: Set of IDs to include
        id_column: Name of the column to filter on (default: 'tconst')
        chunksize: Process file in chunks of this size
    """
    print(f"Filtering {os.path.basename(input_file)} by {id_column}...")
    filtered_chunks = []
    for chunk in pd.read_csv(input_file, sep='\t', dtype=str, na_values='\\N', chunksize=chunksize):
        filtered = chunk[chunk[id_column].isin(id_set)]
        filtered_chunks.append(filtered)
    result = pd.concat(filtered_chunks)
    print(f"Filtered {os.path.basename(input_file)}: {len(result)} records.")
    result.to_csv(output_file, sep='\t', index=False)
    return result

def filter_principals(input_file, output_file, tconst_set, categories, chunksize=None):
    """Filter title.principals by tconst and category."""
    print("Filtering title.principals by tconst and category...")
    filtered_chunks = []
    for chunk in pd.read_csv(input_file, sep='\t', dtype=str, na_values='\\N', chunksize=chunksize):
        filtered = chunk[
            chunk['tconst'].isin(tconst_set) &
            chunk['category'].isin(categories)
        ]
        filtered_chunks.append(filtered)
    result = pd.concat(filtered_chunks)
    print(f"Filtered title.principals: {len(result)} records.")
    result.to_csv(output_file, sep='\t', index=False)
    return result

def filter_name_basics(input_file, output_file, nconst_set, chunksize=None):
    """Filter name.basics by nconst."""
    print("Filtering name.basics by nconst...")
    filtered_chunks = []
    for chunk in pd.read_csv(input_file, sep='\t', dtype=str, na_values='\\N', chunksize=chunksize):
        filtered = chunk[chunk['nconst'].isin(nconst_set)]
        filtered_chunks.append(filtered)
    result = pd.concat(filtered_chunks)
    print(f"Filtered name.basics: {len(result)} records.")
    result.to_csv(output_file, sep='\t', index=False)
    return result