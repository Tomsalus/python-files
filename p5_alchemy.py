from typing import Set, Dict


# Program slouží k zjištění, jestli pomocí vlastněných substancí 
# dokážeme vyrobit požadovanou substanci. Vstupem je:
#
#  • množina substancí, které již máte k dispozici,
#  • slovník, který určuje, jak lze z existujících substancí vytvářet
#    nové: klíčem je substance kterou můžeme vytvořit a hodnotou je
#    seznam „vstupních“ substancí, které k výrobě potřebujeme,
#  • cílová substance, kterou se pokoušíme vyrobit.
#
# Program vypíše true pokud lze substanci vytvořit, v jiném případě vypíše false

def is_creatable(owned_substances: Set[str],
                 rules: Dict[str, Set[str]], wanted: str) -> bool:
    needed_substances = rules.get(wanted, "")

    if rules == {} and wanted not in owned_substances:
        return False

    for substance in rules:
        needed_substances = rules.get(substance, "")
        for material in needed_substances:
            if (material not in rules and material not in owned_substances):
                return False

    return True


def main() -> None:
    assert is_creatable({"a"}, {}, "a")
    assert is_creatable({"a", "b"}, {"c": {"a", "b"}}, "c")
    assert is_creatable({"a", "b"}, {"c": {"a"}, "d": {"c"}}, "d")
    assert is_creatable({"a", "b"}, {"c": {"a", "b"}, "d": {"a", "c"},
                                     "e": {"d", "b"}, "f": {"e", "a"}}, "f")
    assert is_creatable({"b", "c", "d"}, {"a": {"b", "c", "d"},
                                          "e": {"a", "b", "c", "d"},
                                          "f": {"a", "b", "c", "d", "e"}}, "f")

    assert not is_creatable({"a"}, {"c": {"a", "b"}}, "c")
    assert not is_creatable(set(), {"c": {"a", "b"}}, "c")
    assert not is_creatable({"a", "b"}, {}, "c")
    assert not is_creatable({"a", "b"}, {"c": {"a", "b"}, "d": {"a", "c"},
                                         "e": {"d", "b"},
                                         "f": {"e", "a", "h"}}, "f")


if __name__ == '__main__':
    main()