from kafka import KafkaConsumer
from pymongo import MongoClient
import json
from config import settings

def main():             
    consumer = KafkaConsumer(settings.TOPIC_NAME)

    try:
        client = MongoClient(f'mongodb://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGODB_SERVER}')
        print("Conectado a mongodb!!!")

        db = client[settings.TOPIC_NAME]
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