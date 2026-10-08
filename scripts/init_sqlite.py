"""Initialize empty SQLite databases; never overwrite existing data."""
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DATABASES = {'code/output/area/51area.db': 'database/sqlite/code/output/area/51area.schema.sql', 'code/output/clean/51job.db': 'database/sqlite/code/output/clean/51job.schema.sql', 'code/output/job/51job.db': 'database/sqlite/code/output/job/51job.schema.sql', 'code/web/identifier.sqlite': 'database/sqlite/code/web/identifier.schema.sql'}

if __name__ == "__main__":
    for db_path, schema_path in DATABASES.items():
        target = ROOT / db_path
        if target.exists():
            print("SKIP existing:", db_path)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(target) as connection:
            connection.executescript((ROOT / schema_path).read_text(encoding="utf-8"))
        print("Created:", db_path)
