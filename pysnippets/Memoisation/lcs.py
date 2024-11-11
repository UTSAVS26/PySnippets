import logging
from dataclasses import dataclass
from decorator import memoize

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class LCSSolver:
    @staticmethod
    @memoize
    def lcs(X: str, Y: str, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if X[m-1] == Y[n-1]:
            return 1 + LCSSolver.lcs(X, Y, m-1, n-1)
        else:
            return max(LCSSolver.lcs(X, Y, m, n-1), LCSSolver.lcs(X, Y, m-1, n)) 