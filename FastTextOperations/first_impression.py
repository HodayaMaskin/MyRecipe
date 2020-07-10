import fasttext
import fasttext.util

def first_try():
    fasttext.util.download_model('en', if_exists='ignore')
    ft = fasttext.load_model('cc.en.100.bin')
    nearest = ft.get_nearest_neighbors('chocolate')
    print(nearest)