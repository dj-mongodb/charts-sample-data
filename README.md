# charts-sample-data
Download, create and push sample data to work with Atlas charts

## Install config
`pip3 install config`

## Change config file
- Rename config file from `config.sample.py` to `config.py`
- Change the MongoDB Atlas Connection String: See step 1 & step 2 from (here)[https://learn.mongodb.com/learn/course/connecting-to-mongodb-in-python/conclusion/learn?page=2]

## Dowload the data
```python3  crypto_00_download_data.py```

## Create a MongoDB Timeseries Collection on Atlas
```python3 crypto_01_create_ts_collection.py```

## Import the Data to the Collection
```python3 crypto_02_import_in_ts.py```
