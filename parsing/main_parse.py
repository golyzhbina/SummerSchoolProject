import pars_doc_file

# only .docx files
filename = 'vel.docx'
parser = pars_doc_file.DocParser(filename)
abs_depth = pars_doc_file.cut_list(parser.get_column_data(2))
speeds = parser.get_column_data(8)
speeds = pars_doc_file.cut_list(speeds, len(speeds) - len(abs_depth))