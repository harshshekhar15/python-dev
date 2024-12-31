
import re

class Spreadsheet:
    def __init__(self):
        self.cells = {}
        self.formula_cells = {}
    
    def get_cell(self, cell):
        visited = set()
        if cell in self.cells:
            return self.cells[cell]
        elif cell in self.formula_cells:
            visited.add(cell)
            formula = self.formula_cells[cell]
            return self._evaluate_formula(formula, visited)
        return 0
    
    def _evaluate_formula(self, value, visited):
        formula = value
        for cell in re.findall(r'[A-Z][0-9]+', value):
            if cell in self.cells:
                formula = formula.replace(cell, self.cells[cell])
            elif cell in self.formula_cells:
                if cell in visited:
                    return -1
                visited.add(cell)
                new_formula = self.formula_cells[cell]
                new_value = self._evaluate_formula(new_formula, visited)
                if new_value == -1:
                    return -1
                formula = formula.replace(cell, new_value)
        return eval(formula[1:])   
    
    def set_cell(self, cell, value):
        self._clear_cell(cell)
        if value.startswith("="):
            self.formula_cells[cell] = value
        else:
            self.cells[cell] = value
            
    def _clear_cell(self, cell):
        if cell in self.cells:
            self.cells.pop(cell)
        if cell in self.formula_cells:
            self.formula_cells.pop(cell)

new_sheet = Spreadsheet()
new_sheet.set_cell("A3", "23")
new_sheet.set_cell("A4", "=A3+11")
print(f"A4 value: {new_sheet.get_cell('A4')}")
new_sheet.set_cell("A3", "=A4+12")
print(new_sheet.get_cell("A3"))