def GetRes():
    res_file = open("ResSettings/ResSettings.txt", "r")
    res_list = res_file.read().splitlines()
    res_file.close()
    return res_list

def GetValues():
    parameter_file = open("Menu/parameter_menu.txt", "r")
    par_list = parameter_file.read().splitlines()
    parameter_file.close()
    return par_list