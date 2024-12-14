import list_of_stories
def mulai_cerita():
    list_of_stories.display_list()
    theme = int(input("Silahkan Pilih tema ceritamu: "))

    match theme:  
        case 1: 
            print("kamu memilih cerita:" +  list_of_stories.list[0].title)
        case 2: 
            print("kamu memilih cerita:" + list_of_stories.list[1].title)
        case 3: 
            print("Kamu memilih cerita:" + list_of_stories.list[2].title)
        case default: 
            print("tolong pilih nomor yang benar")

