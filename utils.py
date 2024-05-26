import os
import shutil

def mkdir_save_model(save_path):
    # Create a folder to save the weights and the loss
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        os.makedirs(save_path + "/weights")
        os.makedirs(save_path + "/loss")

    # Create a copy of the config.yaml file in the same folder
    shutil.copy("io/config.yaml ", save_path + "/")

def print_yellow(text):
    print("\033[93m {}\033[00m".format(text))

def underline(text):
    return "\033[4m {}\033[00m".format(text)

def print_red(text):
    print("\033[91m {}\033[00m".format(text))

def print_blue(text):
    print("\033[94m {}\033[00m".format(text))

def print_pink(text):
    print("\033[95m {}\033[00m".format(text))