import logging
from dataclasses import dataclass
from decorator import memoize
from typing import Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class Item:
    value: int
    weight: int

@dataclass
class KnapsackSolver:
    @staticmethod
    @memoize
    def knapsack(max_weight: int, items: Tuple[Item, ...], n: int) -> int:
        if n == 0 or max_weight == 0:
            return 0
        current_item = items[n-1]
        if current_item.weight > max_weight:
            return KnapsackSolver.knapsack(max_weight, items, n-1)
        else:
            return max(
                current_item.value + KnapsackSolver.knapsack(max_weight - current_item.weight, items, n-1),
                KnapsackSolver.knapsack(max_weight, items, n-1)
            ) 