def get_filename():
    return "./templates/story.csv"


def get_story():
    file_name = get_filename()
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return
    all_story = [element.replace("\n", "").split(";") for element in lines]
    return all_story


def write_story(all_story):
    file_name = get_filename()
    try:
        with open(file_name, "w") as file:
            for record in all_story:
                row = ';'.join(record)
                file.write(row + "\n")
    except FileNotFoundError:
        return


def make_list_from_form_result(dictionary):
    table_heads = ["story_title", "story", "criteria", "bis_value", "estimation", "status"]
    story_list = []
    for key in table_heads:
        story_list.append(dictionary[key])
    return story_list


def save_new_story(new_story):
    new_story = make_list_from_form_result(new_story)
    all_story = get_story()
    all_story.append(new_story)
    new_id = str(len(all_story))
    all_story[-1].insert(0, new_id)
    write_story(all_story)


def find_line_index_by_id(id_, all_story):
    for i, line in enumerate(all_story):
        if line[0] == str(id_):
            return i
    raise ValueError("No line with such ID.")


def save_edited_story(id_, edited_story):
    edited_story = make_list_from_form_result(edited_story)
    edited_story.insert(0, str(id_))
    all_story = get_story()
    try:
        index = find_line_index_by_id(id_, all_story)
    except ValueError:
        return
    all_story[index] = edited_story
    write_story(all_story)


def delete_story(id_):
    all_story = get_story()
    try:
        index = find_line_index_by_id(id_, all_story)
    except ValueError:
        return
    all_story.pop(index)
    write_story(all_story)
