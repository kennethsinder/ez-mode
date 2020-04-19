import os
from os.path import join

class Form1040NrEz:

    FIELD_KEY_MAPPING = {
        '2019': {
            'first_name': 'FEFF00660031005F0031005B0030005D',
            'last_name': 'FEFF00660031005F0032005B0030005D',
            'ssn': 'FEFF00660031005F0033005B0030005D',
            'street_address': 'FEFF00660031005F0034005B0030005D',
            'city': 'FEFF00660031005F0035005B0030005D',
            'fc_name': 'FEFF00660031005F0036005B0030005D',
            'fc_province': 'FEFF00660031005F0037005B0030005D',
            'fc_postal_code': 'FEFF00660031005F0038005B0030005D',
            '1': None,  # TODO: support checkboxes
            '2': None,
            '3': 'FEFF00660031005F0039005B0030005D',
            '4': 'FEFF00660031005F00310030005B0030005D',
            '5': 'FEFF00660031005F00310031005B0030005D',
            '6': 'FEFF00660031005F00310032005B0030005D',
            '7': 'FEFF00660031005F00310033005B0030005D',
            '8': 'FEFF00660031005F00310034005B0030005D',
            '9': 'FEFF00660031005F00310035005B0030005D',
            '10': 'FEFF00660031005F00310036005B0030005D',
            '11': 'FEFF00660031005F00310037005B0030005D',
            '12': 'FEFF00660031005F00310038005B0030005D',
            '13': 'FEFF00660031005F00310039005B0030005D',
            '14': 'FEFF00660031005F00320030005B0030005D',
            '15': 'FEFF00660031005F00320031005B0030005D',
            '16': 'FEFF00660031005F00320032005B0030005D',
            '17': 'FEFF00660031005F00320033005B0030005D',
            '18a': 'FEFF00660031005F00320033005B0030005D',
            '18b': 'FEFF00660031005F00320035005B0030005D',
            '19': 'FEFF00660031005F00320036005B0030005D',
            '20': 'FEFF00660031005F00320037005B0030005D',
            '21': 'FEFF00660031005F00320038005B0030005D',
            '22': 'FEFF00660031005F00320039005B0030005D',
            '23a': 'FEFF00660031005F00330030005B0030005D',
            '23b': 'FEFF00660031005F00330031005B0030005D',
            '23c': None,
            '23d': 'FEFF00660031005F00330032005B0030005D',
            '23e': 'FEFF00660031005F00330033005B0030005D',
            '23e_line2': 'FEFF00660031005F00330034005B0030005D',
            '24': 'FEFF00660031005F00330035005B0030005D',
            '25': 'FEFF00660031005F00330036005B0030005D',
            '26': 'FEFF00660031005F00330037005B0030005D',
            'occupation': 'FEFF00660031005F00340031005B0030005D',
        }
    }

    def __init__(self, year=None):
        self.year = year
        if self.year is None:
            self.year = '2019'

        self.field_key_mapping = self.FIELD_KEY_MAPPING[self.year]
        self.data = {}
        for box_label in self.field_key_mapping:
            if self.field_key_mapping[box_label]:
                self.data[box_label] = ''

    def get_values(self):
        result = {}
        for key in self.data:
            result[self.field_key_mapping[key]] = self.data[key]
        return result

    def get_template_path(self):
        return join('templates', self.year, 'f1040nre.pdf')
