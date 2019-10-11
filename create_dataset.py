from pathlib import Path
import pandas as pd
import os
from typing import Union

def create_dataset(directory: Union[str, Path])->pd.DataFrame:
    if isinstance(directory, str): directory = Path(directory)
    files = os.listdir(directory)
    file = directory/Path(files[0])

    def get_entry(file):
        with open(file, "r") as f:
            text = f.read()
        return({"song":os.path.basename(file).split('.')[0],"lyrics":text})

    entries = []
    for file in files:
         file = directory/Path(file)
         entry = get_entry(file)
         entries.append(entry)

    return(pd.DataFrame(entries))


lyrics = create_dataset("./lyrics")
lyrics.to_csv("./lyrics-dataset.txt", index=False)
