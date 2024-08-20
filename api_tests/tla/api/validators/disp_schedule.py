def region_must_be_between_1_and_32(value: int):
    if not (1 <= value <= 32):
        raise ValueError('Значение region должно быть между 1 и 32')
    return value
