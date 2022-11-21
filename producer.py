from tweepy import Stream
from kafka import KafkaProducer
from config import settings

producer = KafkaProducer(bootstrap_servers=settings.SERVER_KAFKA)

class StdOutListener(Stream):
  def on_data(self, data):
    producer.send(settings.TOPIC_NAME, data)
    print(data)
    return True

  def on_error(self, status):
    print(status)
  
if __name__ == '__main__':
  stream  = StdOutListener(
    settings.TWITTER_API_KEY, 
    settings.TWITTER_API_SECRET_KEY, 
    settings.TWITTER_ACCESS_TOKEN, 
    settings.TWITTER_ACCESS_TOKEN_SECRET)

  # Setting para la busqueda
  tracks = settings.TRACKS        # Palabras, usuarios, hastags a buscar
  location = settings.LOCATION    # Ubicacion area de tuits
  languages = settings.LANGUAGES  # Idioma de los tuis

  stream.filter(track=tracks, locations=location, languages=languages)