"""

test for common.add_include_groups

"""

from sympyfy.common import INCLUDE_GROUPS, add_include_groups


def test_add_include_groups_full() -> None:
    test = add_include_groups(INCLUDE_GROUPS)

    assert test == "&include_groups=album%2Csingle%2Cappears_on%2Ccompilation"


def test_add_include_groups_one_missing() -> None:
    test = add_include_groups(["single", "appears_on", "compilation"])

    assert test == "&include_groups=single%2Cappears_on%2Ccompilation"


def test_add_include_groups_one_ko() -> None:
    test = add_include_groups(["xxx", "single", "appears_on", "compilation"])

    assert test == "&include_groups=single%2Cappears_on%2Ccompilation"


def test_add_include_groups_all_ko() -> None:
    test = add_include_groups(["xxx", "yyy", "zzz"])

    assert test == "&include_groups=album%2Csingle%2Cappears_on%2Ccompilation"
