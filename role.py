def remove_row(data, row):
    file = open(f"{data} , w")
    del file[row-1]
    file.close()