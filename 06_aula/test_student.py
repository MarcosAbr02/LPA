import pytest
from student import Student


@pytest.fixture
def student_alice():
    return Student("Alice", [70, 85, 90])


@pytest.fixture
def student_bob():
    return Student("Bob", [50, 60, 70])


@pytest.fixture
def student_charlie():
    return Student("Charlie", [30, 40, 50])


def test_calculate_average(student_alice, student_bob, student_charlie):
    assert student_alice.calculate_average() == pytest.approx(81.67, abs=0.01)
    assert student_bob.calculate_average() == 60
    assert student_charlie.calculate_average() == 40


def test_is_passing(student_alice, student_bob, student_charlie):
    assert student_alice.is_passing() is True
    assert student_bob.is_passing() is True
    assert student_charlie.is_passing() is False
