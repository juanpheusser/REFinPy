class Land:
    pass

class DevelopmentLand(Land):
    def __init__(self, zoning: str, infrastructure: bool = False):
        pass

class RawLand(DevelopmentLand): 
    pass

class InfillLand(DevelopmentLand):
    pass

class SubdivisionLand(DevelopmentLand): 
    pass

class AgriculturalLand(Land):
    def __init__(self, soil_type: str, water_access: str): 
        pass
