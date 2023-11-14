import json
from datetime import datetime


def save_note(id, name, body):

    dt_now = datetime.now()
    dt_now_str = dt_now.strftime("%Y-%m-%d %H:%M:%S")
    notes = get_notes()
    notes.append({'id': id, 'name': name, 'body': body, 'date': dt_now_str})

    with open("notes.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(notes, ensure_ascii=False))
    return

def delete_note(id):
    notes = get_notes()
    i = 0
    for note in notes:
        if(note['id'] == int(id)):
            del notes[i]
            save_notes(notes)
            return True
        i += 1

    return False

def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(notes, ensure_ascii=False))
    return


def get_notes():
    with open("notes.json", "r", encoding="utf-8") as fh:
        notes = json.load(fh)

    sorted_notes = sorted(notes, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)

    return sorted_notes

def find_max_id(notes):
    max_id = 0
    for note in notes:
        if (note['id'] > max_id):
            max_id = note['id']
    return max_id

def get_note_by_id(id):
    notes = get_notes()
    for note in notes:
        if (note['id'] == int(id)):
            return note
    return False