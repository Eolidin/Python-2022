def get_word_count(user_texts):

    for key in user_texts.keys():
        user_texts[key] = len(user_texts[key].split(" "))

    return user_texts


user_text_dict = {"user1": "Hier habe ich etwas geschrieben",
                  "user2": "Heute scheint die Sonne!",
                  "user3": "Programmieren macht mir wirklich Spaß",
                  "user4": "Wo ist der Seiteneffekte? Ich finde hier nichts."
                  }
#user_textlen_dict = get_word_count(user_text_dict)

#das problem ist, dass das Dictionary überschrieben wird
#mögliche lösung:
def get_word_count(user_texts):
    """
    gibt die anzahl der wörter des values zurück
    :param user_texts (dic): Ein dictionary mit string Values
    :return:dictionary mit anzahl der wörter pro key
    """
    results = {}
    for key in user_texts.keys():
        results[key] = len(user_texts[key].split(" "))

    return results

print(get_word_count(user_text_dict))
