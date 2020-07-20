import fasttext
import fasttext.util

def first_try():
    #fasttext.util.download_model('he', if_exists='ignore')
    ft = fasttext.load_model('cc.he.300.bin')
    #print(ft.get_dimension())
    #fasttext.util.reduce_model(ft, 100)
    #print(ft.get_dimension())
    nearest = ft.get_nearest_neighbors('שוקולד')
    print(nearest)

first_try()