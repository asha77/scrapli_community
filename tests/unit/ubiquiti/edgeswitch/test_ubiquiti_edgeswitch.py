import re

import pytest

from scrapli_community.ubiquiti.edgeswitch.ubiquiti_edgeswitch import (
    DEFAULT_PRIVILEGE_LEVELS,
    SCRAPLI_PLATFORM,
)


@pytest.mark.parametrize(
    "priv_pattern",
    [
        ("exec", "(sw-whatever) >"),
        ("privilege_exec", "(sw-whatever) #"),
        ("configuration", "(sw-whatever) (Config)#"),
        ("configuration", "(sw-whatever) (Interface 0/1)#"),
        ("exec", "(usw-24-lite) >"),
        ("privilege_exec", "(usw-24-lite) #"),
        ("configuration", "(usw-24-lite) (Config)#"),
        ("configuration", "(usw-24-lite) (Vlan 10)#"),
    ],
    ids=[
        "base_prompt_exec",
        "base_prompt_privilege_exec",
        "base_prompt_configuration",
        "base_prompt_configuration_interface",
        "hyphenated_prompt_exec",
        "hyphenated_prompt_privilege_exec",
        "hyphenated_prompt_configuration",
        "hyphenated_prompt_configuration_vlan",
    ],
)
def test_default_prompt_patterns(priv_pattern):
    priv_level_name = priv_pattern[0]
    prompt = priv_pattern[1]

    prompt_pattern = DEFAULT_PRIVILEGE_LEVELS.get(priv_level_name).pattern
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
