import duckdb
import pathlib as pl

duck_db_path = pl.Path(__file__).parents[2] / 'data/prices_2.db'

db = duckdb.connect(database=duck_db_path.as_posix(), read_only=True)
