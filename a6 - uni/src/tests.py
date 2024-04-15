import functions


def test_add():
    scores = []
    stack = []
    scores = functions.add_result(stack, scores, 5, 6, 7)
    assert scores == [(5, 6, 7)]


def test_insert():
    scores = [(1, 2, 3)]
    stack = []
    scores = functions.insert_result(stack, scores, 5, 6, 7, 0)
    assert scores == [(5, 6, 7)]


def test_remove():
    scores = [(1, 1, 1)]
    stack = []
    scores = functions.remove_score(stack, scores, 0)
    assert scores == [(0, 0, 0)]

    scores = [(1, 1, 1), (1, 1, 1)]
    stack = []
    scores = functions.remove_scores(stack, scores, 0, 1)
    assert scores == [(0, 0, 0), (0, 0, 0)]


def test_replace():
    scores = [(1, 1, 1)]
    stack = []
    scores = functions.replace_score(stack, scores, 0, "P1", 7)
    assert scores == [(7, 1, 1)]


def test_all():
    test_add()
    test_insert()
    test_remove()
    test_replace()