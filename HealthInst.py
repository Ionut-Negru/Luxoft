# HealthInst.py
"""This class holds the information for a healthInst MO"""


class HealthInst:

    def __init__(self, current_health=0, max_sev=0):
        """Initialization for the object"""
        self.current_health = int(current_health)
        self.max_sev = max_sev

    def displayed_health(self):
        if self.current_health >= 100:
            return "Healthy"
        else:
            return "Unhealthy"
