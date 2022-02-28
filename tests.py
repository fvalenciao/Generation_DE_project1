from db import execute_query
from funcs import get_courier, select_key
from unittest.mock import patch

@patch("db.pymysql.connect")
def test_execute_query(mock_connect):
    mock_cursor = mock_connect.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = []
    rows = execute_query("select * from products")
    mock_cursor.execute.assert_called_once_with("select * from products")
    assert rows == []
    
@patch("builtins.input")
def test_get_courier(mock_input):
    mock_input.return_value = '1'
    courier = get_courier(['John'])
    assert courier == 'John'

@patch("builtins.input")
def test_select_key(mock_input):
    mock_input.return_value = '1'
    result = select_key(['name'])
    assert result == 'name'