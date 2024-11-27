## src/convert_from_chi.py
def convert_from_chi(logger, lines):
    logger.info("Converting from CHI format")
    data = []
    for line in lines:
        parts = line.strip().split('|')
        if len(parts) < 3:
            logger.warning(f"Line skipped due to insufficient data: {line}")
            continue
        data.append({
            'lat': parts[0],
            'long': parts[1],
            'comment': parts[2],
            'magnitude': parts[3] if len(parts) > 3 else None
        })
    return data
