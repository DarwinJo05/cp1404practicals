class ProgrammingLanguage:

    def __init__(self, name = "", typing = "", is_reflection = False, year = 0):
        self.name = name
        self.typing = typing
        self.is_Reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the typing is dynamic"""
        return self.typing.lower() == "dynamic"