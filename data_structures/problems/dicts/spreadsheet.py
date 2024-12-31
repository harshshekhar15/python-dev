"""
Today we are going to build a basic spreadsheet application like Google sheets or Excel but much simpler. Our spreadsheet, let’s call it OpenSheet, will only support cells which hold either integers or formulas that sum two cells.

You are tasked with writing a program that handles this functionality for OpenSheet. You can make any decisions you want regarding how this program is organized, but there must be some sort of setter/getter methods that can be called by the application for any given cell. All inputs will be strings.

For setting you can expect two inputs: the cell location and the cell value.

Example of how your setter could look
set_cell("C1", "45")
set_cell("B1", "10")
set_cell("A1", "=C1+B1")

For getting you will be provided one input that is the cell location.

Example of how your getter could look
set_cell("C1", "45")
set_cell("B1", "10")
set_cell("A1", "=C1+B1")
get_cell("A1") # should return 55 in this case

Assumptions
In memory storage
All cell location inputs will be well formed (no need to validate in code)
All cell value inputs will be well formed (no need to validate in code)
Cells value inputs are either a summation of two other cells or an int
Empty cells are treated as zero when accessed
"""
import re
class Spreadsheet:
    def __init__(self):
        self.cells = {}
        self.formula_cells = {}
    
    def set_cell(self, cell, value):
        self._clear_cell(cell)
        if value.startswith("="):
            self.formula_cells[cell] = value
        else:
            self.cells[cell] = value
    
    def _clear_cell(self, cell):
        if cell in self.formula_cells:
            self.formula_cells.pop(cell)
        if cell in self.cells:
            self.cells.pop(cell)
    
    def get_cell(self, cell):
        visited = set()
        if cell in self.cells:
            return self.cells[cell]
        elif cell in self.formula_cells:
            visited.add(cell)
            value = self.formula_cells[cell]
            return self._evaluate_formula(value, visited)
        else:
            return 0
    
    def _evaluate_formula(self, value, visited):
        formula = value
        print(f"Evaluating formula: {formula}")
        for cell in re.findall(r'[A-Z][0-9]+', value):
            if cell in self.cells:
                formula = formula.replace(cell, self.cells[cell])
            else:
                if cell in visited:
                    return -1
                visited.add(cell)
                new_cell = self.formula_cells[cell]
                new_value = self._evaluate_formula(new_cell, visited)
                if new_value == -1:
                    return -1
                formula = formula.replace(cell, new_value)
        return eval(formula[1:])

new_sheet = Spreadsheet()
new_sheet.set_cell("A3", "23")
new_sheet.set_cell("A4", "=A3+11")
print(f"A4 value: {new_sheet.get_cell('A4')}")
new_sheet.set_cell("A3", "=A4+12")
print(new_sheet.get_cell("A3"))