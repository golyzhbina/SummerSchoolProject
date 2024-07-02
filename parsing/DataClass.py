import pars_doc_file
from scipy import interpolate


# only .docx files
class Data:
    def __init__(self, filename: str):
        self.speed_func = None
        parser = pars_doc_file.DocParser(filename)
        self.abs_depth = [int(elem) for elem in pars_doc_file.cut_list(parser.get_column_data(2))]
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
