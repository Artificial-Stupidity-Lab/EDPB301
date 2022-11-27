import pandas as pd

char_name = ["Mando", "Grogu", "Eleven", "Jon", "Ross"]
series_name = ["Mandalorian", "Mandalorian",
               "Stranger Things", "Game of Thrones", "Friends"]
profession = ["Bounty Hunter", "Jedi Master", "Kid", "King", "Paleontologist"]
age = [35, 50, 14, 30, 35]

dict = {"Character Name": char_name, "Series Name": series_name,
        "Profession": profession, "Age": age}

df = pd.DataFrame(dict)

df.to_csv('shows.csv')