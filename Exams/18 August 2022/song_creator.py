def add_songs(*args):
    res = ""
    songs = {}

    for music in args:
        title, text = music

        if title not in songs:
            songs[title] = []
        for i in text:
            songs[title].append(i)

    for key, value in songs.items():
        res += f"- {key}" + "\n"
        for txt in value:
            res += f"{txt}" + "\n"

    return res


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))

