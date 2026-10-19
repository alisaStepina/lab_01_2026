length = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
weight = {"g": 1, "kg": 1000}
temperature = ["c", "f", "k"]



def convert(v, f, t):
    f = f.lower()
    t = t.lower()
    if f in length and t in length:
        return float(v) * length[f] / length[t]
    if f in weight and t in weight:
        return float(v) * weight[f] / weight[t]
    if f in temperature and t in temperature:
        return conv_temp(float(v), f, t)
    k = list(length) + list(weight) + temperature
    if f not in k:
        raise ValueError(f"Неизвестная единица: {f}")
    if t not in k:
        raise ValueError(f"Неизвестная единица: {t}")
    raise ValueError(f"Несовместимые единицы: {f} и {t}")


def conv_temp(v, f, t):
    if f == "k" and v < 0:
        raise ValueError("Ниже абсолютного нуля")
    if f == "c" and v < -273.15:
        raise ValueError("Ниже абсолютного нуля")
    if f == "f" and v < -459.67:
        raise ValueError("Ниже абсолютного нуля")
    if f == "c":
        k = v + 273.15
    elif f == "f":
        k = (v - 32) * 5 / 9 + 273.15
    else:
        k = v
    if t == "c":
        return k - 273.15
    if t == "f":
        return (k - 273.15) * 9 / 5 + 32
    return k