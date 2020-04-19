import os
import pdfrw

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

class FormPdf:

    def __init__(self, input_file_path, output_file_path):
        self.template_pdf = pdfrw.PdfReader(input_file_path)
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def write_output(self, data_dict):
        annotations = []
        for page in self.template_pdf.pages:
            annotations.extend(page[ANNOT_KEY])
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    # sides_positions = annotation.Rect
                    # left = min(sides_positions[0], sides_positions[2])
                    # bottom = min(sides_positions[1], sides_positions[3])
                    # print(left)
                    # print(bottom)
                    # print(key)
                    if key in data_dict.keys():
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )
        pdfrw.PdfWriter().write(self.output_file_path, self.template_pdf)
