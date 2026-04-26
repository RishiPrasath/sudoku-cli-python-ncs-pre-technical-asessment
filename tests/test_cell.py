import pytest
from sudoku.cell import Cell


def test_cell_default_is_empty():
    # Arrange
    cell = Cell()

    # Assert
    assert cell.get_value() == None
    assert cell.is_empty() == True

def test_cell_prefilled_stores_value_and_flag():
    # Arrange
    cell = Cell(value=5, is_prefilled=True)

    # Assert
    assert cell.get_value() == 5
    assert cell.is_prefilled() == True
    assert cell.is_empty() == False

def test_cell_set_value_updates_empty_cell():
    # Arrange
    cell = Cell()
    assert cell.get_value() == None
    assert cell.is_empty() == True

    # Act
    cell.set_value(7)

    # Assert
    assert cell.get_value() == 7
    assert cell.is_empty() == False

def test_cell_set_value_raises_if_prefilled():
    # Arrange
    cell = Cell(value=5,is_prefilled=True)
    # Act + Assert
    with pytest.raises(ValueError):
        cell.set_value(3)


def test_cell_set_value_raises_if_zero():
    # Arrange
    cell = Cell()
    # Act + Assert
    with pytest.raises(ValueError):
        cell.set_value(0)



def test_cell_set_value_raises_if_out_of_range():
    # Arrange
    cell = Cell()
    # Act + Assert
    with pytest.raises(ValueError):
        cell.set_value(10)


def test_cell_clear_raises_if_prefilled():
    # Arrange
    cell = Cell(value=5,is_prefilled=True)
    # Act + Assert
    with pytest.raises(ValueError):
        cell.clear()

def test_cell_clear_does_nothing_if_already_empty():
    # Arrange
    cell = Cell()
    # Act
    cell.clear()
    # Assert
    assert cell.is_empty() == True

def test_cell_clear_removes_user_value():
    # Arrange
    cell = Cell(value=5,is_prefilled=False)
    # Act
    cell.clear()
    # Assert
    assert cell.get_value() == None
    assert cell.is_empty() == True 

def test_cell_set_value_raises_if_not_integer():
    # Arrange
    cell = Cell()
    # Act + Assert
    with pytest.raises(ValueError):
        cell.set_value("a")
