from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

RAW_DATA = DATA_DIR / "raw" / "infcf16652007.json.gz"

WAREHOUSE_DIR = DATA_DIR / "warehouse"
WAREHOUSE_DIR.mkdir(exist_ok=True)

WAREHOUSE = WAREHOUSE_DIR / "warehouse.duckdb"
