import random

def mad_libs():
    noun = input("Введите существительное: ")
    verb = input("Введите глагол в прошедшем времени: ")
    adjective = input("Введите прилагательное: ")
    place = input("Введите место: ")
    hei = input("Введите действие: ")
    oskorblenie = input("Введите оскорбление: ")
    story = f"В одном {place}, {adjective} {noun} {verb} жестко. И я такой кричу {hei}!, а он такой да ты {oskorblenie}"

    print(story)

if __name__ == "__main__":
    mad_libs()