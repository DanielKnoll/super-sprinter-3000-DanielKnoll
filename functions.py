def get_filename():
    return "./templates/story.csv"


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


def get_story():
    file_name = get_filename()
    try:
        story = get_story_from_file(file_name)
    except FileNotFoundError:
        return []
    return story


def write_story(story):
    file_name = get_filename()
    try:
        write_story_to_file(file_name, story)
    except FileNotFoundError:
        return []


def save_new_story(new_story):
    table_heads = ["story_title", "story", "criteria", "b_value", "estimation", "status"]
    story = get_story()
    story.append([])
    for key in table_heads:
        story[-1].append(new_story[key])
    new_id = str(len(story))
    story[-1].insert(0, new_id)
    write_story(story)
