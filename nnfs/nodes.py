import random as _random
from typing import Optional
import activation as _activation

class Node:
    def __init__(self, activation: Optional[_activation.ActivationFunction] = None) -> None:
        self.weights: list[float] = []
        self.w = _random.random()
        self.activation: _activation.ActivationFunction
        
        if activation and isinstance(activation, _activation.ActivationFunction):
            self.activation = activation
        else: 
            self.activation = _activation.Basic()

    def __str__(self) -> str:
        return f"Node(activation='{self.activation.name}', weigths={self.weights})"

    def activate(self, res: float) -> float:
        return self.activation.apply_formula(res)

    def calc(self, x: float, conn_n: Optional[int] = None):
        """
        Calculate the value of the data after it passed trough this node
        based on the destination node
        """
        if not conn_n:
            return self.activate(x * self.w)
        
        if conn_n < 0 or conn_n > len(self.weights):
            raise ValueError(f"Invalid connection_number (must be 0 < x < len(self.weights)): conn_n={conn_n}")
        return self.activate(x * self.weights[conn_n])
    