def map_value(value: int, from_low: int, from_hight: int, to_low: int, to_hight: int):
    value = min(max(value, from_low), from_hight)
    normalized_value = (value - from_low) / (from_hight - from_low)
    mapped_value = to_low + normalized_value * (to_hight - to_low)
    return int(mapped_value)
