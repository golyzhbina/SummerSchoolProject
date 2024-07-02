from parsing import pars_doc_file
from scipy import interpolate


# only .docx files
class Data:
    def __init__(self, filename: str):
        self.speed_func = None
        parser = pars_doc_file.DocParser(filename)
        self.__get_abs_depth(parser)
        self.__get_speeds(parser)

    def __get_abs_depth(self, parser: pars_doc_file.DocParser):
        self.abs_depth = [int(elem) for elem in pars_doc_file.cut_list(parser.get_column_data(2))]
        max_depth = abs(min(self.abs_depth))
        self.abs_depth = [elem + max_depth for elem in self.abs_depth]

    def __get_speeds(self, parser: pars_doc_file.DocParser):
        self.speeds = [int(elem) for elem in parser.get_column_data(8)]
        self.speeds = pars_doc_file.cut_list(self.speeds, len(self.speeds) - len(self.abs_depth))

    def regularization_data(self):
        self.speed_func = interpolate.interp1d(self.abs_depth, self.speeds)

"""
import numpy as np
import matplotlib.pyplot as plt

data = Data('vel.docx')
data.regularization_data()

xnew = np.arange(-2227, -8, 10)
ynew = data.speed_func(xnew)   # use interpolation function returned by `interp1d`
plt.plot(data.abs_depth, data.speeds, 'o', xnew, ynew, '-')
plt.show()
"""
