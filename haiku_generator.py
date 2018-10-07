def generate_haiku(phrases, colors, emotion_data, weather_data):
    # generate haiku here
    # data = (phrases, colors, emotions, weather_data)
    res = str(phrases) + "<br>" + str(colors) + "<br>" + \
        str(emotion_data) + "<br>" + str(weather_data)
    return res
