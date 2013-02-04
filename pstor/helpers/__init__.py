import os

def import_all(file, loc, glob):
    files = os.listdir(os.path.dirname(file))
    for module in list(set([os.path.splitext(f)[0] for f in files if "__init__" not in f])):
        __import__(module, loc, glob)