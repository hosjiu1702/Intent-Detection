""" Load PhoATIS
"""
import os


def load_file(path):
    lines = []
    with open(path, "r") as f:
        lines = f.readlines()

    return lines


def load_data(path):
    X, y = [], []
    X_path = os.path.join(path, "seq.in")
    y_path = os.path.join(path, "label")
    X = load_file(X_path)
    y = load_file(y_path)

    return X, y


def load_phoatis(data_root_path, split="all"):
    if split == "all":
        train_X, val_X, test_X = [], [], []
        train_y, val_y, test_y = [], [], []

        train_path = os.path.join(data_root_path, "train")
        val_path = os.path.join(data_root_path, "dev")
        test_path = os.path.join(data_root_path, "test")

        train_X, train_y = load_data(train_path)
        val_X, val_y = load_data(val_path)
        test_X, test_y = load_data(test_path)
        
        return (train_X, train_y), (val_X, val_y), (test_X, test_y)
    

if __name__ == "main":
    data_path = "../../data/phoatis/"
    train_path = os.path.join(data_path, "train")
    val_path = os.path.join(data_path, "dev")
    test_path = os.path.join(data_path, "test")

    train, val, test = load_phoatis(data_path, split="all")
    train_X, train_y = train[0], train[1]
    val_X, val_y = val[0], val[1]
    test_X, test_y = test[0], test[1]