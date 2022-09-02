import random

topic_bank_directory = 'C:/'
topic_bank_filename = topic_bank_directory + "topic_bank.txt"


def topic_bank_from_file(filename):
    topic_bank_file_openage = open(topic_bank_filename, 'r')
    topic_bank = topic_bank_file_openage.read().splitlines()
    print(topic_bank)
    topic_bank_file_openage.close()

    return topic_bank


def get_topics_from_users_and_write_to_file():
    more_topics = 'y'
    topic_bank_file_openage = open(topic_bank_filename, 'a')
    while more_topics != "n":
        topic = input("add topic: ")
        topic_bank_file_openage.write(topic)
        topic_bank_file_openage.write('\n')
        more_topics = input("add more topics? (y or n)")
    topic_bank_file_openage.close()


def choose_random_topic(topic_list):
    randoms_list = topic_list.copy()
    print(len(randoms_list))
    choose_random = 'y'
    while choose_random != 'n':
        choose_random = input("choose a random topic? (y/n)")
        topic_index = random.randint(0, len(randoms_list)-1)
        print(topic_index)
        print(randoms_list[topic_index])
        randoms_list.remove(randoms_list[topic_index])
        if len(randoms_list) == 0:
            break


topic_list = topic_bank_from_file(topic_bank_filename)
choose_random_topic(topic_list)
get_topics_from_users_and_write_to_file()
