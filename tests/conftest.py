from copy import deepcopy

import pytest

from src import app


@pytest.fixture(autouse=True)
def restore_activities():
    initial_activities = deepcopy(app.activities)

    yield

    app.activities.clear()
    app.activities.update(deepcopy(initial_activities))
