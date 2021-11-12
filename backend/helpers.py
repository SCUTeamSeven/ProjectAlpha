def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def coords2A1String(row,col):
    col_string = colnum_string(col)
    return f"{col_string}{row}"

def cell2A1String(cell):
    col_string = colnum_string(cell.col)
    return f"{col_string}{cell.row}"


def col2Range(col_num,rows):
    col_string = colnum_string(col_num)
    start_cell = f"{col_string}{1}"
    end_cell = f"{col_string}{1 + rows}"
    return f"{start_cell}:{end_cell}"


def cell2Range(cell, rows):
    col_string = colnum_string(cell.col)

    start_cell = f"{col_string}{cell.row}"
    end_cell = f"{col_string}{cell.row + rows}"

    return f"{start_cell}:{end_cell}"

def coords2Range(row, col, rows):
    col_string = colnum_string(col)

    start_cell = f"{col_string}{row}"
    end_cell = f"{col_string}{row}"

    return f"{start_cell}:{end_cell}"
