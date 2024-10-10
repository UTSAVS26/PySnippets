# test_case_conversions.py

import pytest
from pysnippets import *


def camel_to_snake_case():
    assert camel_to_snake_case("fightForChange") == "fight_for_change"
    assert camel_to_snake_case("openSourceContribution") == "open_source_contribution"


def snake_to_camel_case():
    assert snake_to_camel_case("an_apple_a_day") == "anAppleADay"
    assert snake_to_camel_case("john_smith") == "johnSmith"
