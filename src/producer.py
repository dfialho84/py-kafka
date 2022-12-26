from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from random import choice

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'), help="Arquivo de Configuração")
    args = parser.parse_args()
    return args

def read_config():
    args = parse_args()

    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])
    return config

def log_msg(msg):
    template = "Produced event to topic {topic}: key = {key:12} value = {value:12}"
    return template.format(topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8'))

def delivery_callback(err, msg):
    if err:
        print("ERROR: Message failed delivery: {}.".format(err))
    else:
        print(log_msg(msg))

def main():
    """
    Produz itens aleatórios

    :return: Nada
    :rtype: None
    """
    config = read_config()
    producer = Producer(config)
    topic = "purchases"
    user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']
    
    count = 0
    for _ in range(10):
        user_id = choice(user_ids)
        product = choice(products)
        producer.produce(topic, product, user_id, callback=delivery_callback)
        count += 1
    
    producer.poll(10000)
    producer.flush()

if __name__ == '__main__':
    main()
