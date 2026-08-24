from typing import TypeVar, Generic, List
from payment_gateway import PaymentMethod, CreditCardPayment, PayPalPayment

T = TypeVar("T")

class Stack(Generic[T]):
    def _init_(self) -> None:
        self.items: List[T] = []
    def push(self, item: T) -> None:
        self.items.append(item)
    def pop(self) -> T:
        return self.items.pop()

class Queue(Generic[T]):
    def _init_(self) -> None:
        self.items: List[T] = []
    def enqueue(self, item: T) -> None:
        self.items.append(item)
    def dequeue(self) -> T:
        return self.items.pop(0)

# Test for SCREENSHOT 8
if __name__ == "_main_":
    history = Stack[PaymentMethod]()
    history.push(CreditCardPayment())
    history.push(PayPalPayment())
    print("Popped from stack:", history.pop())

    queue = Queue[int]()
    queue.enqueue(10)
    queue.enqueue(20)
    print("Dequeued from queue:", queue.dequeue())