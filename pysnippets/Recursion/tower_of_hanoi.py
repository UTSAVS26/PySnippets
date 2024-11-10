import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class TowerOfHanoi:
    num_disks: int

    def solve(self, from_rod, to_rod, aux_rod):
        if self.num_disks <= 0:
            raise ValueError("Number of disks must be greater than zero")
        if self.num_disks == 1:
            logging.info(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
            return [(from_rod, to_rod)]
        moves = []
        moves += self.solve(from_rod, aux_rod, to_rod)
        moves.append((from_rod, to_rod))
        logging.info(f"Move disk {self.num_disks} from rod {from_rod} to rod {to_rod}")
        moves += self.solve(aux_rod, to_rod, from_rod)
        return moves

# Sample usage
if __name__ == "__main__":
    hanoi = TowerOfHanoi(3)
    print(hanoi.solve('A', 'C', 'B'))  # Output: Moves from rod A to C using B as auxiliary 