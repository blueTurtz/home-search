from dataclasses import dataclass

@dataclass
class BasicInformation:
    street_address: str
    neighborhood: str
    price: float
    id: int


@dataclass
class AvailableSpace:
    id: int
    bedrooms: int
    bathrooms: float
    square_footage: int
