from sortedcontainers import SortedDict

# Represents individual buy and sell orders
class Order:
    def __init__(self, order_id, price, quantity, order_type):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.order_type = order_type

# Represents the order book for the BTC/USD pair
class OrderBook:
    def __init__(self):
        self.bids = SortedDict()
        self.asks = SortedDict()
    
    def add_order(self, order):
        if order.order_type == "buy":
            if order.price in self.bids:
                self.bids[order.price] += order.quantity
            else:
                self.bids[order.price] = order.quantity
        elif order.order_type == "sell":
            if order.price in self.asks:
                self.asks[order.price] += order.quantity
            else:
                self.asks[order.price] = order.quantity
    
    def remove_order(self, order):
        if order.order_type == "buy":
            self.bids[order.price] -= order.quantity
            if self.bids[order.price] <= 0:
                del self.bids[order.price]
        elif order.order_type == "sell":
            self.asks[order.price] -= order.quantity
            if self.asks[order.price] <= 0:
                del self.asks[order.price]
    
    def get_bid_price(self):
        return self.bids.keys()[-1] if self.bids else None
    
    def get_ask_price(self):
        return self.asks.keys()[0] if self.asks else None
    
    def get_bid_quantity(self, price):
        return self.bids[price] if price in self.bids else 0
    
    def get_ask_quantity(self, price):
        return self.asks[price] if price in self.asks else 0

# Implement the order matching algorithm    
class OrderMatcher:
    def __init__(self, buy_book, sell_book):
        self.buy_book = buy_book
        self.sell_book = sell_book
    
    def match_orders(self):
        while True:
            best_bid_price = self.buy_book.get_bid_price()
            best_ask_price = self.sell_book.get_ask_price()
            
            if not best_bid_price or not best_ask_price or best_bid_price < best_ask_price:
                break
            
            best_bid_quantity = self.buy_book.get_bid_quantity(best_bid_price)
            best_ask_quantity = self.sell_book.get_ask_quantity(best_ask_price)
            matched_quantity = min(best_bid_quantity, best_ask_quantity)
            
            buy_order = Order(None, best_bid_price, matched_quantity, "buy")
            sell_order = Order(None, best_ask_price, matched_quantity, "sell")
            
            self.buy_book.remove_order(buy_order)
            self.sell_book.remove_order(sell_order)
            
            print(f"Matched order: {buy_order.quantity} @ {buy_order.price}")

# Initialize the order books, add some sample orders, and run the order matcher.
def main():
    buy_book = OrderBook()
    sell_book = OrderBook()
    
    buy_book.add_order(Order(1, 100, 10, "buy"))
    buy_book.add_order(Order(2, 95, 5, "buy"))
    buy_book.add_order(Order(3, 105, 20, "buy"))
    
    sell_book.add_order(Order(4, 110, 15, "sell"))
    sell_book.add_order(Order(5, 90, 10, "sell"))
    
    matcher = OrderMatcher(buy_book, sell_book)
    matcher.match_orders()
    
if __name__ == "__main__":
    main()