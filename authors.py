from tkinter import messagebox

authors = {
    "Binayam Gurung" : "binayam2.gurung@live.uwe.ac.uk",
    "Reece Turner" : "reece2.turner@live.uwe.ac.uk",
    "Zheng Yin": "Zheng2.Yin@live.uwe.ac.uk",
    "Anas Abueida" : "Anas2.Abueida@live.uwe.ac.uk",
    "Milo Patrick Carroll" : "Milo2.Carroll@live.uwe.ac.uk"
}


def show_creators():
    message = ""
    for k, v in authors.items():
        message += f"{k} : {v}\n"
        
    return messagebox.showinfo("Project Authors", f"Made by UWE Bristol Students: \n{message}")