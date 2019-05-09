#!/usr/bin/env python

import json


class BracketService:
    def __init__(self, year=None):
        if year is None:
            year = '2018'
        self.year = str(year)

        # TODO: Modular/customizable data source so we can swap it out
        # for a dummy data source in the tests.
        with open('nr-brackets.json') as bracket_file:
            self.data = json.loads(bracket_file.read())

    def get_tax(self, taxable_income):
        result = 0
        for tax_bracket in self.data[self.year]:
            pct = tax_bracket['percentage'] / 100.0
            if 'max' in tax_bracket and taxable_income > tax_bracket['max']:
                # TODO: handle the married filer tax bracket case.
                result += tax_bracket['max'] * pct
            elif 'min' in tax_bracket and taxable_income > tax_bracket['min']:
                result += (taxable_income - tax_bracket['min']) * pct
            elif 'min' not in tax_bracket:
                result += taxable_income * pct
        return result
