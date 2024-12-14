class story_list:
    def __init__(self, id, title):
        self.id = id
        self.title = title

list = []
list.append(story_list(1, "Nyonya Meneer dan Aku Di tahun 1990-an"))
list.append(story_list(2, "Keruntuhan Masa Kerajaan Majapahin"))
list.append(story_list(3, "Bisnis di masa penjajahan Hindia Belanda"))




def display_list():

    print(str(list[0].id) +". "+ list[0].title)
    print(str(list[1].id) +". "+ list[1].title)   
    print(str(list[2].id) +". "+ list[2].title)  