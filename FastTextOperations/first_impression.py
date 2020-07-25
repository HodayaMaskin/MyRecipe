import fasttext
import fasttext.util

def first_try():
    #fasttext.util.download_model('he', if_exists='ignore')
    ft = fasttext.load_model('cc.he.100.bin')
    #fasttext.util.reduce_model(ft, 100)
    #ft.save_model('cc.he.100.bin')
    nearest = ft.get_nearest_neighbors('אורז')
    nearest = ft.get_nearest_neighbors('קוקוס')
    nearest = ft.get_nearest_neighbors('קמח')
    nearest = ft.get_nearest_neighbors('ביצה')
    nearest = ft.get_nearest_neighbors('חמאה')
    nearest = ft.get_nearest_neighbors('פפריקה')
    print(nearest)