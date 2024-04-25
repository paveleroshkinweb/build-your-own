def lrc_check(data: bytes):
    lrc = 0
    for word in data:
        data ^= word
    return lrc
