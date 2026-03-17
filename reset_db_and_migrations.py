import os
import pymongo
from pathlib import Path

# 1. Clear Migration Files
migration_dirs = [
    Path('users/migrations'),
    Path('issues/migrations'),
    Path('civic/db_migrations/auth'),
    Path('civic/db_migrations/contenttypes'),
]

print("Clearing migrations...")
for mdir in migration_dirs:
    if mdir.exists():
        for file in mdir.glob('*.py'):
            if file.name != '__init__.py':
                try:
                    os.remove(file)
                    print(f"Removed: {file}")
                except Exception as e:
                    print(f"Error removing {file}: {e}")

# 2. Drop MongoDB Database
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db_name = 'civic_db'
    client.drop_database(db_name)
    print(f"Dropped database: {db_name}")
except Exception as e:
    print(f"Error dropping database: {e}")

print("Reset complete.")
