import datetime
import calendar

class Helpers:
    @staticmethod
    def get_current_time():
        """Get current time"""
        return datetime.datetime.now().strftime("%I:%M %p")
    
    @staticmethod
    def get_current_date():
        """Get current date"""
        today = datetime.datetime.now()
        date = today.strftime("%B %d, %Y")
        day = calendar.day_name[today.weekday()]
        return f"Today is {day}, {date}"
    
    @staticmethod
    def extract_city_from_command(command):
        """Extract city name from weather command"""
        if 'in' in command:
            return command.split('in ')[-1].strip()
        return None
    
    @staticmethod
    def extract_search_query(command):
        """Extract search query from command"""
        if 'search' in command:
            return command.replace('search', '').strip()
        return None
    
    @staticmethod
    def extract_app_name(command):
        """Extract application name from command"""
        if 'open' in command:
            return command.replace('open', '').strip()
        return None