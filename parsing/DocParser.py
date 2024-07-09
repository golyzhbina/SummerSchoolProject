import docx
import numpy as np


class DocParser:
    @staticmethod
    def get_depths_and_speeds(filename: str) -> tuple:
        document = docx.Document(filename)
        abs_depths = DocParser.get_column_data(document, 2)
        speeds = DocParser.get_column_data(document, 8)
        abs_depths, speeds = DocParser.cut(abs_depths, speeds)
        abs_depths = [float(elem) for elem in abs_depths]
        speeds = [float(elem) for elem in speeds]
        return abs_depths, speeds
    @staticmethod
    def get_column_data(document: docx.Document, column_index: int) -> list:
        columns = DocParser._get_columns(document)
        return DocParser._get_column_data(columns, column_index)

    @staticmethod
    def _get_columns(document: docx.Document) -> list:
        tables = document.tables
        columns = list()
        for i in range(len(tables)):
            columns += tables[i].columns
        return columns

    @staticmethod
    def _get_column_data(columns: list, column_index: int) -> list:
        cells = list()
        for column in columns[column_index::9]:
            cells += column.cells[1:]
        cells.pop(0)
        cells_data = list()
        for cell in cells:
            cells_data.append(cell.text)
        return cells_data

    @staticmethod
    def cut(abs_depth: list, speeds: list):
        for i in range(len(abs_depth)):
            if abs_depth[i] == '' or speeds[i] == '':
                abs_depth[i] = None
                speeds[i] = None

        none_filter = lambda x: x is not None

        return list(filter(none_filter, abs_depth)), list(filter(none_filter, speeds))
