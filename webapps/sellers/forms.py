from typing import List
from typing import Optional

from fastapi import Request


class SellerCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.name: str
        self.email: str
        self.paypal: Optional[str] = None
        self.collection: Optional[str] = None
        self.total_number_of_books: Optional[int] = 0
        self.dropoff_location: Optional[int] = 0
        self.pricing_option: Optional[int] = 0
        self.proceed_option: Optional[int] = 0
        self.extrabook_option: Optional[int] = 0
        self.comments: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.email = form.get("email")
        self.paypal = form.get("paypal")
        self.collection = form.get("collection")
        self.total_number_of_books = form.get("total_number_of_books")
        self.dropoff_location = form.get("dropoff_location")
        self.pricing_option = form.get("pricing_option ")
        self.proceed_option = form.get("proceed_option")
        self.extrabook_option = form.get("extrabook_option")
        self.comments = form.get("comments")

    def is_valid(self):
        if not self.name or not len(self.name) >= 4:
            self.errors.append("A valid name is required")
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Valid Email is required e.g. test@example.com")
        if not self.errors:
            return True
        return False
