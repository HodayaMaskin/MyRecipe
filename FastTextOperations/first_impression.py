import fasttext
import fasttext.util

def first_try():
    fasttext.util.download_model('en', if_exists='ignore')
    ft = fasttext.load_model('cc.en.100.bin')
    nearest = ft.get_nearest_neighbors('rice')
    nearest = ft.get_nearest_neighbors('coconat')
    nearest = ft.get_nearest_neighbors('flour')
    nearest = ft.get_nearest_neighbors('egg')
    nearest = ft.get_nearest_neighbors('butter')
    nearest = ft.get_nearest_neighbors('paprika')
    print(nearest)