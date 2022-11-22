

def _encode_string(s: str) -> bytes:
    s_bytes = bytearray()
    s_bytes.extend(map(ord, s))

    data = bytearray()
    data.append(len(s_bytes))
    data.extend(s_bytes)

    return data


def send_wifi_settings(ssid: str, password: str) -> bytes:
    encoded_ssid = _encode_string(ssid)
    encoded_password = _encode_string(password)

    combined = bytearray()
    combined.append(len(encoded_ssid) + len(encoded_password))
    combined.extend(encoded_ssid)
    combined.extend(encoded_password)

    data = bytearray()
    data.append(0x01)
    data.extend(combined)

    checksum = sum(data) & 0xff
    data.append(checksum)
    return data
