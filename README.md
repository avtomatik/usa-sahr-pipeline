# USA Sahr Pipeline

A lightweight analytics pipeline built around:

* DuckDB for storage and querying
* dbt for transformations
* Python for ingestion and visualization
* [Historical inflation conversion factors compiled by Robert C. Sahr](https://liberalarts.oregonstate.edu/sites/liberalarts.oregonstate.edu/files/polisci/faculty-research/sahr/inflation-conversion/excel/infcf17742018.xlsx)

## Project Structure

```text
data/
├── raw/
│   └── infcf16652007.json.gz
│
└── warehouse/
    └── warehouse.duckdb

ingestion/
└── ingest.py

transform/

main.py
```

## Dataset

The project uses a normalized JSON representation of the historical inflation conversion factors dataset originally published by Robert C. Sahr.

The raw dataset is stored as:

```text
data/raw/infcf16652007.json.gz
```

with records of the form:

```json
{
  "series_name": "CPI [1982-84] CF",
  "year": 1665,
  "conversion_factor": 0.092
}
```

## Option 1: Spyder IDE (Anaconda)

This project works well with Spyder, which is included with the Anaconda distribution.

Install DuckDB into your active conda environment:

```bash
conda install duckdb
```

Additional packages may be installed as needed:

```bash
conda install pandas matplotlib
```

Open the project in Spyder and execute:

```python
%run ingestion.ingest
%run -m main
```

## Option 2: uv

Create and synchronize the project environment:

```bash
uv sync
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the pipeline:

```bash
uv run python -m ingestion.ingest
```

Alternatively:

```bash
uv run python ingestion/ingest.py
```

## DuckDB

The warehouse is stored locally:

```text
data/warehouse/warehouse.duckdb
```

Raw data is loaded into:

```sql
raw.sahr
```

Example:

```sql
select *
from raw.sahr
limit 10;
```

## dbt

Transformations are delegated to dbt.

Typical schema layout:

```text
raw
├── sahr

staging
├── stg_sahr

marts
├── inflation_rates
```

Run dbt models from the project root:

```bash
dbt run
```

Run tests:

```bash
dbt test
```

## Development Philosophy

This project intentionally favors simplicity:

* One raw dataset
* One DuckDB warehouse
* SQL transformations via dbt
* Minimal Python ingestion code
* No configuration registries
* No dataset abstractions
* No unnecessary framework code

Data flow:

```text
raw JSON.GZ
    ↓
DuckDB ingestion
    ↓
raw.sahr
    ↓
dbt models
    ↓
analytics / visualization
```

## License

See LICENSE.md.
