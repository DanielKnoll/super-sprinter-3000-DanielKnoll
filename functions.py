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
        return
    return story


def write_story(story):
    file_name = get_filename()
    try:
        write_story_to_file(file_name, story)
    except FileNotFoundError:
        return


def make_list_from_form(dictionary):
    table_heads = ["story_title", "story", "criteria", "bis_value", "estimation", "status"]
    story_list = []
    for key in table_heads:
        story_list.append(dictionary[key])
    return story_list


def save_new_story(new_story):
    new_story = make_list_from_form(new_story)
    story = get_story()
    story.append(new_story)
    new_id = str(len(story))
    story[-1].insert(0, new_id)
    write_story(story)


def save_edited_story(id_, edited_story):
    edited_story = make_list_from_form(edited_story)
    edited_story.insert(0, str(id_+1))
    story = get_story()
    story[id_] = edited_story
    write_story(story)


def delete_story(id_):
    story = get_story()
    for i, line in enumerate(story):
        if line[0] == str(id_):
            story.pop(i)
            break
    write_story(story)
