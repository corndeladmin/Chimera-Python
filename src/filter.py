## src/filter.py
def filter_data(logger, options, data):
    logger.info("Filtering data")
    if options.m:
        data = [item for item in data if item.get('magnitude') and float(item['magnitude']) >= options.m]
    if options.M:
        data = [item for item in data if item.get('magnitude') and float(item['magnitude']) <= options.M]
    return data
