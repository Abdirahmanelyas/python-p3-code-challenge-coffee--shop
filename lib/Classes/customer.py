class Customer:
    def _init_(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string of 1 to 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def coffees(self):
        from order import Order
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order