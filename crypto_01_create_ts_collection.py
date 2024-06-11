import pymongo

import config

client = pymongo.MongoClient(config.CONNECTION_STRING)

client[config.DB_NAME].create_collection(
    "cryptoTS",
    timeseries = {
          "timeField": "timestamp",
          "metaField": "metadata",
          "granularity": "minutes"
    })

index_meta_and_timestamp = pymongo.IndexModel([('metadata.symbol', pymongo.DESCENDING), ('timestamp', pymongo.DESCENDING)], name="metaAndTimestamp")
client[config.DB_NAME].cryptoTS.create_indexes([index_meta_and_timestamp])
