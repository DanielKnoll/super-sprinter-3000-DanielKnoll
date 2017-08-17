def get_filename():
    return "./templates/story.csv"


def get_story():
    file_name = get_filename()
    try:
        story = get_story_from_file(file_name)
    except FileNotFoundError:
        return []
    for i in range(len(story)):
        story[i].insert(0, i+1)
    return story


def get_story_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    story = [element.replace("\n", "").split(";") for element in lines]
    return story


def write_story_to_file(file_name, story):
    with open(file_name, "w") as file:
        for record in story:
            row = ';'.join(record)
            file.write(row + "\n")
