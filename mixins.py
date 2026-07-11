class TimestampMixin:
    """Provides a timestamp when a record is created."""
    def get_info(self):
        return "TimestampMixin called"

class SerializerMixin:
    """Provides a helper method to convert database objects to dictionaries/JSON."""
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.columns}
    
    def get_info(self):
        return "SerializerMixin called"