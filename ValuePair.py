try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.api.deco import keyword
    ROBOT = False
    
except Exception:
    ROBOT = False

class ValuePair:
    
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    def __init__(self, x, y):
        BuiltIn().log_to_console(f"values assigned: {x} and {y}")
        self.x = x
        self.y = y

    @keyword("SUM")
    def sum_of_value(self):
        return(self.x + self.y)
    
    @keyword("DIFF")
    def diff_of_value(self):
        return(self.x - self.y)
