import docx


def get_columns(document: docx.Document) -> list:
    tables = document.tables
    columns = list()
    for i in range(len(tables)):
        columns += tables[i].columns
    return columns


def get_column_data(columns: list, column_index: int) -> list:
    cells = list()
    for column in columns[column_index::9]:
        cells += column.cells[1:]
    cells.pop(0)
    cells_data = list()
    for cell in cells:
        cells_data.append(cell.text)
    return cells_data


def cut_list(data: list, start_index=-1) -> list:
    if start_index == -1:
        start_index = 0
        while data[start_index] == '':
            start_index += 1
    return data[start_index:]


class DocParser:
    def __init__(self, filename: str):
        self.document = docx.Document(filename)

    def get_column_data(self, column_index: int) -> list:
        columns = get_columns(self.document)
        return get_column_data(columns, column_index)
