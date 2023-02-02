#In this program replaace if else ladder with dictionary

def key_map(key):
    if key == 33:
        return '{UP}'
    elif key == 45:
        return '{ESC}'
    elif key == 67:
        return '{PGDN}'
    elif key == 88:
        return '{PGUP}'
    else:
        return None


key_dict = {
    33: '{UP}',
    45: '{ESC}',
    67: '{PGDN}',
    88: '{PGUP}',

}

print(key_map(88))

#In below function , eliminate switch case using python dictionaries

def key_map(key):
    return key_dict.get(key)


print(key_map(88))

key_dic1 = {
    0: "Sub Zero",
    10: "Very Cold",
    20: "cold",
    30: "moderate",
    40: "hot",
    50: "very hot",
    float('inf'): "Extreme hot"
}

def weather_label(temp):
    for key, value in key_dic1.items():
        if (temp<key):
            return value

print(weather_label(15))

    