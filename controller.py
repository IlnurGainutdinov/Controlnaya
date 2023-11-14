import json
from datetime import datetime

from model import (delete_note, find_max_id, get_note_by_id, get_notes,
                   save_note, save_notes)

notes = {}


def start():
    while True:
        command = input("*** Введите команду: ")

        if command == 'list':

            notes_list = get_notes()

            print("------ \nСписок заметок: ")
            for note in notes_list:
                print("- Заметка №" + str(note['id']) + ": " +
                  note['name'] + " (" + note['date'] + ")")
            print("------")
            continue

        if command == 'read':

            note_id = input("Введите номер заметки, которую хотите прочитать: ")

            note = get_note_by_id(note_id)

            if (note):
                print("------\nЗаметка №" + str(note['id']) + " от " + note['date'] +
                  "\nНазвание заметки: " + note['name'] + "\nТекст заметки: " + note['body'] + "\n------")
            else:
                print("Заметка с таким номером не найдена.\n------")

            continue

        if command == 'add':

            print("Введите название заметки: ")
            name = input()

            print("Введите текст заметки: ")
            body = input()

            notes_list = get_notes()

            if (len(notes_list) > 0):
                id = find_max_id(notes_list) + 1
            else:
                id = 1

            save_note(id, name, body)
            print("заметка сохранена.\n------")
            continue

        if command == 'edit':

            note_id = input("Введите номер заметки, которую хотите изменить: ")

            note = get_note_by_id(note_id)

            if (note):
                print("------\nЗаметка №" + str(note['id']) + " от " + note['date'] + "\nНазвание заметки: " +
                  note['name'] + "\nТекст заметки: " + note['body'] + "\n------\n *Режим редактирования*")
            else:
                print("Заметка с таким номером не найдена.\n------")
                continue

            print("Введите новое название заметки: ")
            name = input()

            print("Введите новый текст заметки: ")
            body = input()

            if (delete_note(note['id'])):
                save_note(note['id'], name, body)

            print("заметка успешно обновлена.\n------")
            continue

        if command == 'delete':

            delete_note_id = input(
            "Введите номер заметки, которую нужно удалить: ")

            if (delete_note(delete_note_id)):
                print("Заметка удалена успешно.\n------")
            else:
                print("Заметка с таким номером не найдена.\n------")

            continue

        if command == 'help':

            print("------ \nПриложение имеет следующие функции: \nlist - просмотр списка заметок \nadd - добавить заметку \nread - чтение заметки (указать № заметки) \nedit - изменить заметку (указать № заметки) \ndelete - удалить заметку (указать № заметки)\nexit - выход \nhelp - посмотреть туториал\n------")

        if command == 'exit':
            print("До свидания!")
            break
        else:

            print("Неопознанная команда. Изучите мануал - введите help.")
