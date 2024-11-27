## src/output.py
import json
import os
import redis

def output_data(logger, options, data):
    logger.info("Outputting data")
    has_produced_output = False

    if options.o:
        with open(options.o, 'w') as f:
            json.dump(data, f)
        logger.info(f"Data saved to {options.o}")
        has_produced_output = True

    if options.r:
        save_to_redis(logger, data)
        has_produced_output = True
    
    if not has_produced_output and not options.quiet:
        print(json.dumps(data, indent=2))


def save_to_redis(logger, data):
    logger.info("Saving data to Redis")
    client = redis.StrictRedis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379))
    for item in data:
        client.set(item['dataset_name'], json.dumps(item))
