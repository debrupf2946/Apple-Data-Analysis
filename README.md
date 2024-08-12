# APPLE DATA ANALYSIS USING PYSPARK

## Overview

This repository contains a simple and modular data processing framework using Apache Spark. It includes components for loading data, transforming it, and saving the results to various destinations.

## Project Structure

```plaintext
├── data_sources.py      # Data source classes for CSV, Parquet, and Delta formats
├── extractors.py        # Extractor classes to load initial data
├── transformers.py      # Transformer classes for applying business logic
├── loaders.py           # Loader classes for saving transformed data
├── README.md            # Project documentation
```

## Components

- **Data Sources** (`data_sources.py`): Load data from CSV, Parquet, or Delta sources.
- **Extractors** (`extractors.py`): Extract and prepare initial data for processing.
- **Transformers** (`transformers.py`): Apply specific transformations to the data.
- **Loaders** (`loaders.py`): Save the transformed data to DBFS or Delta tables.

## Usage

1. **Load Data**:
    ```python
    data_source = get_data_source(data_type="csv", file_path="path/to/file.csv")
    df = data_source.get_data_frame()
    ```

2. **Transform Data**:
    ```python
    transformer = AirpodsAfterIphoneTransformer()
    transformed_df = transformer.transform(input_dfs)
    ```

3. **Save Data**:
    ```python
    loader = AirPodsAfterIphoneLoader(transformed_df)
    loader.sink()
    ```
## Results

### Transaction Data

| transaction_id | customer_id | product_name | transaction_date |
|----------------|-------------|--------------|------------------|
| 11             | 105         | iPhone       | 2022-02-01       |
| 14             | 105         | AirPods      | 2022-02-04       |
| 18             | 105         | MacBook      | 2022-02-08       |
| 12             | 106         | iPhone       | 2022-02-02       |
| 16             | 106         | MacBook      | 2022-02-06       |
| 20             | 106         | AirPods      | 2022-02-10       |
| 13             | 107         | AirPods      | 2022-02-03       |
| 17             | 107         | iPhone       | 2022-02-07       |
| 15             | 108         | iPhone       | 2022-02-05       |
| 19             | 108         | AirPods      | 2022-02-09       |

### Grouped Data (Products Purchased by Each Customer)

| customer_id | products            |
|-------------|---------------------|
| 107         | [AirPods, iPhone]   |
| 108         | [AirPods, iPhone]   |
| 106         | [AirPods, iPhone, MacBook] |
| 105         | [AirPods, iPhone, MacBook] |

### Filtered Data (Only AirPods and iPhone)

| customer_id | products          |
|-------------|-------------------|
| 107         | [AirPods, iPhone] |
| 108         | [AirPods, iPhone] |

### Customer Data

| customer_id | customer_name | join_date  | location |
|-------------|---------------|------------|----------|
| 105         | Eva           | 2022-01-01 | Ohio     |
| 106         | Frank         | 2022-02-01 | Nevada   |
| 107         | Grace         | 2022-03-01 | Colorado |
| 108         | Henry         | 2022-04-01 | Utah     |

### Joined Data (Customers Who Bought Only AirPods and iPhone)

| customer_id | customer_name | join_date  | location | products          |
|-------------|---------------|------------|----------|-------------------|
| 107         | Grace         | 2022-03-01 | Colorado | [AirPods, iPhone] |
| 108         | Henry         | 2022-04-01 | Utah     | [AirPods, iPhone] |
