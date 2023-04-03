# Bitcoin Exchange Matching Engine

This is an attempt to learn about financial markets and the technology powering them by building a matching engine for a hypothetical bitcoin exchange.

The matching engine is the core component of every financial exchange. It is responsible for matching buy and sell orders in real-time, determining the price and volume of each trade, and maintaining an orderly market.

Attempting to build a  matching engine for a Bitcoin exchange is a great way to learn about the technical aspects of exchange technology and gain experience with the software systems that power financial markets. You can start by studying the mechanics of order matching, understanding the data structures and algorithms used in matching engines, and then gradually building a prototype of a simple matching engine.

# Components

High-level architecture of the matching engine components:

1. Order book: A data structure that stores all the pending buy and sell orders for a particular trading pair. Each order will have a price, quantity, and order type.

2. Order matching algorithm: A function that compares incoming buy and sell orders and attempts to match them according to certain rules. The algorithm will follow different rules depending on the order type (limit, market, etc.).

3. Order execution engine: A function that executes matched orders, updating the account balances of the buyers and sellers and completing the trade.

4. API layer: A set of endpoints that allow users to submit, modify, and cancel orders through HTTP requests.

# The Basics of Order Matching

At a high level, order matching is the process of finding buyers and sellers who want to trade at the same price and quantity, and then executing their trades. This happens continuously in real-time, as new orders are submitted and existing orders are filled.

In a matching engine, orders are stored in a data structure called an order book. The order book contains two separate lists of orders: the bids, which are buy orders, and the asks, which are sell orders. Each order contains information such as the price, quantity, and type of order (limit, market, etc.).

When a new order is submitted, the matching engine first checks whether it can be immediately filled against an existing order in the opposite list. For example, if a buy order is submitted at a price higher than or equal to the lowest ask price in the order book, it can be immediately filled against that ask order. Similarly, if a sell order is submitted at a price lower than or equal to the highest bid price, it can be immediately filled against that bid order.

If the order cannot be immediately filled, it is added to the appropriate list (bid or ask) in the order book, and waits for a match to be found in the future.

The matching engine continuously searches for matches in the order book, and executes trades as soon as they are found. When a match is found, the matching engine updates the order book to reflect the new market conditions and notifies the relevant parties (buyers, sellers, and brokers) of the trade.

That's a brief overview of the mechanics of order matching. From here, you can start exploring the specific data structures, algorithms, and programming concepts involved in building a matching engine in Python.

# Order Book Data Structure

Once you have a good understanding of the mechanics of order matching, the next step is to design and implement a data structure to represent the order book. There are different data structures that can be used for this purpose, such as arrays, linked lists, or binary trees, and the choice depends on factors such as performance, scalability, and ease of implementation.

One commonly used data structure for order books is the Red-Black Tree, which provides fast lookup and insertion times and guarantees balanced tree height. You can use a Python library like sortedcontainers to implement a Red-Black Tree in Python.

Next, you can start implementing the logic for order submission, cancellation, and matching. This involves creating functions that can add new orders to the order book, cancel existing orders, and search for matches between the bids and asks. You will need to handle various types of orders, such as limit orders, market orders, and stop orders.
