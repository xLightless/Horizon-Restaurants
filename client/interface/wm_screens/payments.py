



class Offers(object):
    def get_discounts():
        return
    
    def validate_discount(self, discount_code:str):
        return
    
    def _create_discount(self, discount_code:str):
        return
    
    def _update_discount(self, discount_code:str, percentage:float):
        return
    
    def _delete_discount(self, discount_code:str):
        return


class Payment(object):
    def check_for_discounted_offers(self) -> Offers:
        return Offers.get_discounts()
    
    def validate_payment(self) -> bool:
        return
    
    def cancel_payment(self):
        return
    
    def refund_payment(self):
        return