from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import config

def main():             
    consumer = KafkaConsumer(config.TOPIC_NAME)

    try:
        client = MongoClient(f'mongodb://{config.MONGODB_USER}:{config.MONGODB_USER_PASSWORD}@{config.MONGODB_SERVER}')
        print("Conectado a mongodb!!!")

        db = client[config.TOPIC_NAME]
        collection = db['tuits']
        for msg in consumer:
            output = []
            output.append(json.loads(msg.value))
            print(json.loads(msg.value))
            collection.insert_one(json.loads(msg.value))
            print ('\n')

    except Exception as e:        
        print("Error >>> ", e)

if __name__ == "__main__":
    main()