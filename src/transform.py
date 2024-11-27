## src/transform.py
import time
import random
import string

def transform_data(logger, options, data):
    logger.info("Transforming data")
    dataset_name = options.dataset_name if options.dataset_name else ''.join(random.choices(string.ascii_lowercase, k=10))
    for item in data:
        item['dataset_name'] = dataset_name
        item['generation_time'] = time.time()
        item['origin'] = {'x': options.x or 0, 'y': options.y or 0}
        item['zoom'] = options.z or 0
    return data
