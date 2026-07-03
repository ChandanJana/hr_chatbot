class ConfirmationRequired(Exception):
    def __init__(self, original, corrected, entity_type):
        super().__init__(f"Did you mean '{corrected}'?")
        self.original = original
        self.corrected = corrected
        self.entity_type = entity_type