import config
import etl_utils

def main():
    # Ensure output directory exists
    etl_utils.ensure_dir_exists(config.PROCESSED_DATA_DIR)
    
    # 1. Filter title.basics and get tconst set
    basics_filtered, tconst_set = etl_utils.filter_title_basics()
    basics_filtered.to_csv(config.TITLE_BASICS_FILTERED_FILE, sep='\t', index=False)
    
    # 2. Filter title.ratings, title.crew, title.akas, title.episode by tconst
    etl_utils.filter_file_by_id(
        config.TITLE_RATINGS_FILE, config.TITLE_RATINGS_FILTERED_FILE, tconst_set, id_column='tconst', chunksize=config.CHUNKSIZE
    )
    etl_utils.filter_file_by_id(
        config.TITLE_CREW_FILE, config.TITLE_CREW_FILTERED_FILE, tconst_set, id_column='tconst', chunksize=config.CHUNKSIZE
    )
    etl_utils.filter_file_by_id(
        config.TITLE_AKAS_FILE, config.TITLE_AKAS_FILTERED_FILE, tconst_set, id_column='titleId', chunksize=config.CHUNKSIZE
    )
    etl_utils.filter_file_by_id(
        config.TITLE_EPISODE_FILE, config.TITLE_EPISODE_FILTERED_FILE, tconst_set, id_column='parentTconst', chunksize=config.CHUNKSIZE
    )
    
    # 3. Filter title.principals by tconst and category, get nconst set
    principals_filtered = etl_utils.filter_principals(
        config.TITLE_PRINCIPALS_FILE, config.TITLE_PRINCIPALS_FILTERED_FILE, tconst_set, config.PRINCIPALS_CATEGORIES, config.CHUNKSIZE
    )
    nconst_set = set(principals_filtered['nconst'])
    
    # 4. Filter name.basics by nconst
    etl_utils.filter_name_basics(
        config.NAME_BASICS_FILE, config.NAME_BASICS_FILTERED_FILE, nconst_set, config.CHUNKSIZE
    )
    print('\nETL process completed! Filtered data is in:', config.PROCESSED_DATA_DIR)

if __name__ == "__main__":
    main()