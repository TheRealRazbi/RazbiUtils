# Author: TheRealRazbi (https://github.com/TheRealRazbi)
# License: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


def test_smoketest():
    import razbi_utils

    from razbi_utils.core.modules import script_tools

    assert hasattr(razbi_utils.core, "script_tools")
    assert callable(script_tools.show_window)

    assert hasattr(script_tools, "hide_window")
    from razbi_utils.core import hide_window

    assert callable(hide_window)
