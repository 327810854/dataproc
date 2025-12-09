# dataproc

## Tabular Data Processing

This project provides basic utilities for processing tabular data using
**pandas**, including loading CSV files, handling missing values, removing
duplicates, and selecting specific columns.

---

### Load CSV File

```python
from dataproc.tabular.proc import load_csv

df = load_csv("data/sample.csv")

from dataproc.tabular.proc import drop_empty, fill_empty

# Remove rows that contain missing values
df_clean = drop_empty(df)

# Fill missing values with a fixed value
df_filled = fill_empty(df, value=0)

from dataproc.tabular.proc import drop_duplicates

df_unique = drop_duplicates(df)

from dataproc.tabular.proc import keep_columns

df_selected = keep_columns(df, ["column1", "column2"])

dataproc/
├── dataproc/
│   └── tabular/
│       └── proc.py
├── dataproc/tests/
├── README.md
└── requirements.txt