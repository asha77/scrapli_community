"""scrapli_community.ubiquiti.edgeswitch.ubiquiti_edgeswitch"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.ubiquiti.edgeswitch.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.ubiquiti.edgeswitch.sync_driver import (
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^\([a-z0-9.\-_]{1,63}\)\s>$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^\([a-z0-9.\-_]{1,63}\)\s#$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="exit",
            escalate="enable",
            escalate_auth=True,
            escalate_prompt=r"^(?:[eE]nable\s){0,1}[pP]assword:\s?$",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^\([a-z0-9.\-_]{1,63}\)\s\([\w.\-@/:+ ]{1,32}\)#$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="end",
            escalate="configure",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Ambiguous command",
            "Command not found / Incomplete command. Use ? to list commands.",
            "Invalid input.",
            "Unrecognized command",
            "% Invalid input detected at '^' marker.",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
