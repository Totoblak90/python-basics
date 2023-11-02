import pandas as pd

phonetic_alfabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for index,
                 row in phonetic_alfabet_df.iterrows()}

result = [phonetic_dict[code.upper()] for code in input("Enter a word: ")]
