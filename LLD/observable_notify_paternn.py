# Observable class
class StockObservable:
    def __init__(self):
        self._observers = []
        self._stock_count = 0

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._stock_count)

    def set_stock_count(self, count):
        self._stock_count = count
        self.notify_observers()

    def set_stock_count_zero(self):
        self._stock_count = 0

# Observer interface
class StockObserver:
    def update(self, stock_count):
        raise NotImplementedError("You must implement the update method.")

# Concrete observer that sends an email
class EmailAlertObserver(StockObserver):
    def __init__(self, email):
        self.email = email

    def update(self, stock_count):
        print(f"Email to {self.email}: Stock count updated to {stock_count}.")

# Concrete observer that sends a mobile notification
class MobileAlertObserver(StockObserver):
    def __init__(self, username):
        self.username = username

    def update(self, stock_count):
        print(f"Mobile notification to {self.username}: Stock count updated to {stock_count}.")

# Example usage
if __name__ == '__main__':
    # Create observable
    iphone_stock = StockObservable()

    # Create observers
    email_observer1 = EmailAlertObserver("xyz1@gmail.com")
    mobile_observer = MobileAlertObserver("user123")

    # Register observers
    iphone_stock.add_observer(email_observer1)
    iphone_stock.add_observer(mobile_observer)

    # Update stock and notify observers
    iphone_stock.set_stock_count(10)
    iphone_stock.set_stock_count_zero()
    iphone_stock.set_stock_count(5)