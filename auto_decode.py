import chardet

def decode_text_safely(raw_data: bytes):
    """
    Safely decode text files using automatic encoding detection.
    """
    detected = chardet.detect(raw_data)
    encoding = detected.get("encoding") or "utf-8"

    try:
        return raw_data.decode(encoding)
    except:
        return raw_data.decode("latin-1", errors="ignore")
