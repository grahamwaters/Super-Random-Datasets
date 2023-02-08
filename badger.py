import random
import re
import numpy as np


def collect_badges(links):
    # Create dynamic badges for middle section
    badges = []
    badge_texts = []
    badge_count = len(links)
    for i in range(badge_count):
        badge_color = random.choice(["brightgreen", "green", "yellowgreen", "darkred","lightblue","darkgreen","purple","yellow", "orange", "red", "blue", "lightgrey","success", "important", "critical", "informational", "inactive","blueviolet", "ff69b4", "9cf"])
        # get the name of the file
        badge_link = links[i]
        badge_text = re.sub(r".*/", "", badge_link) # remove the file path and keep only the filename
        badge_text = re.sub(r"\.md", "", badge_text) # remove the .md extension
        badge_text = re.sub(r" ", "_", badge_text) # replace spaces with underscores
        if badge_text not in badge_texts:
            badge = f"[![{badge_text}](https://img.shields.io/badge/{badge_text}-{badge_color})]({badge_link})"
            badges.append(badge) # add the badge to the list
        badge_texts.append(badge_text.replace("_"," ")) # add the badge text to the list
    # concatenate the badges together then return the concatenated string
    return badges

def master_badge_function(links):
    badges = collect_badges(links)
    return badges


# Read in the top, middle, and bottom sections of the README
with open("docs/section_1.md", "r") as file:
    top = file.read()
    # Write the section to the top of the readme
    with open("README.md", "w") as file:
        file.write(top)

links = [
    "https://www.example.com/industries/specific_topics/file1.md",
    "https://www.example.com/industries/specific_topics/file2.md",
    "https://www.example.com/actors/file1.md"
]
with open("docs/section_2.md", "r") as file:
    # middle = file.read()
    updated_middle = master_badge_function(links) # collect the badges
    middle = "\n\n" + updated_middle
    # write the section to the bottom of the readme
    with open("README.md", "a") as file:
        file.write(middle)


with open("docs/section_3.md", "r") as file:
    bottom = file.read()
    # write the section to the bottom of the readme
    with open("README.md", "a") as file:
        file.write(bottom)
