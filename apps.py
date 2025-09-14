class AppService:
    def __init__(self):
        self.app_mappings = {
            'chrome': self.open_chrome,
            'browser': self.open_chrome,
            'notepad': self.open_notepad,
            'calculator': self.open_calculator,
        }
    
    def open_application(self, app_name):
        """Open applications - mock version"""
        app_name = app_name.lower()
        
        for key, method in self.app_mappings.items():
            if key in app_name:
                return method()
        
        return "Application not supported yet."
    
    def open_chrome(self):
        """Open Google Chrome - mock version"""
        return "Would open Google Chrome"
    
    def open_notepad(self):
        """Open Notepad - mock version"""
        return "Would open Notepad"
    
    def open_calculator(self):
        """Open Calculator - mock version"""
        return "Would open Calculator"