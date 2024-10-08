from models.address import Address
from models.company import Company

class User:
    def __init__(self, user_id: int, name: str, username: str, email: str, address: Address, phone: str, website: str, company: Company):
        self.id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'address': self.address.to_dict(),
            'phone': self.phone,
            'website': self.website,
            'company': self.company.to_dict()
        }