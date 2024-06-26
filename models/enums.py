from enum import Enum


class OrderStatus(str, Enum):
    ORDER_INIT = "ORDER_INIT"
    ORDER_PAID = "Order Paid"
    ORDER_ARTICLES_CONFIRMED = "Order articles confirmed"
    ORDER_ARTICLES_DENIED = "Order articles denied"
    ORDER_BEING_PACKED = "Order being packed"
    ORDER_SENT = "Order sent"
    ORDER_DELIVERED = "Order delivered"
    ORDER_CANCELED = "Order canceled"