from __future__ import absolute_import
from flytekit.clis.sdk_in_container import launch_plan
import pytest


def test_list_commands(mock_ctx):
    g = launch_plan.LaunchPlanExecuteGroup('test_group')
    v = g.list_commands(mock_ctx)
    assert v == ['common.workflows.simple.SimpleWorkflow']


def test_get_commands(mock_ctx):
    g = launch_plan.LaunchPlanExecuteGroup('test_group')
    v = g.get_command(mock_ctx, 'common.workflows.simple.SimpleWorkflow')
    assert v.params[0].human_readable_name == 'input_1'
    assert 'INTEGER' in v.params[0].help
    assert v.params[1].human_readable_name == 'input_2'
    assert 'INTEGER' in v.params[1].help
    assert 'Not required.' in v.params[1].help

    with pytest.raises(Exception):
        g.get_command(mock_ctx, 'common.workflows.simple.DoesNotExist')
    with pytest.raises(Exception):
        g.get_command(mock_ctx, 'does.not.exist')
