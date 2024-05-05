Remove Duplicates from nested array

```python
`# Python3 code to demonstrate`

`# removing duplicate sublist`

`# using set() + sorted()`

`# Initializing list`

`test_list` `=` `[[``1``,` `0``,` `-``1``], [``-``1``,` `0``,` `1``], [``-``1``,` `0``,` `1``],`

             `[``1``,` `2``,` `3``], [``3``,` `4``,` `1``]]`

`# Printing original list`

`print``(``"The original list : "` `+` `str``(test_list))`

`# Removing duplicate sublist`

`# using set() + sorted()`

`res` `=` `list``(``set``(``tuple``(``sorted``(sub))` `for` `sub` `in` `test_list))`

`# Printing result`

`print``(``"The list after duplicate removal : "` `+` `str``(res))`
```
