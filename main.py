"""news-image-20261126: deliver the pre-rendered front page as /output/entry.png."""
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "entry.png")
os.makedirs("/output", exist_ok=True)
shutil.copyfile(src, "/output/entry.png")
