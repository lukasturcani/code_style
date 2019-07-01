.. contents:: Table of Contents


.. _`Python Style Guidelines`:

Python Style Guidelines
=======================

Style should follow PEP8_ and PEP257_ in cases where this guideline
does not state a different preference.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _PEP257: https://www.python.org/dev/peps/pep-0257/

.. toctree::
   :numbered:

Line length.
------------

Line length should be at most 71 visible characters, so that it is
72 with newlines. This ensures that all lines obey PEP8_ and that
all lines are the same length.

Comprehensions.
---------------

Comprehensions should be done on a single line, if they fit.

.. code-block:: python

    list1 = [2*x for x in range(20)]
    list2 = [2*x for x in range(20) if 2*x % 4 == 0]
    set1 = {2*x for x in range(20)}
    dict1 = {key: value for key, value in zip(range(10), (10, 20))}

If the the comprehension does not fit on a single line, try placing
the opening and closing brackets on separate lines.

.. code-block:: python

    some_very_long_variable_name = [
        some_element for some_element in some_long_container_name
    ]

    some_other_very_long_variable_name = {
        key: value for key, value in zip(range(10), range(10, 20))
    }

If the comprehension still does not fit, split it so that each
Python keyword begins on a new line, with the exception of
``for`` and ``in`` which should be placed on the same line, if they
fit.

.. code-block:: python

    some_very_long_variable_name = [
        some_very_long_function_name(some_very_long_element_name)
        for some_very_long_element_name in some_long_container_name
        if some_very_long_element_name == 20
        and some_very_long_element_name % 2 == 1
    ]

    some_other_very_long_variable_name = {
        key_name: value_name
        for key_name, value_name in zip(range(10), range(10, 20))
    }

Function calls.
---------------

Function calls, with 3 or fewer parameters, may be done on a single
line without any parameter names.

.. code-block:: python

    some_variable = some_function(1, 2, 3)

Functions with more than 3 parameters must be called with each
parameter specified by name and on a separate line.

.. code-block:: python

    some_variable = some_function(
        param_name1=1,
        param_name2=2,
        param_name3=3,
        param_name4='4th'
    )

This keeps everything readable and ensures that parameters are not
sensitive to order.

Function and method definitions.
--------------------------------

Functions and methods should be defined so that they are on a single
line, if they fit.

.. code-block:: python

    def some_function(param1, param2, param3, keyword_param=10):
        return 12

If the function or method does not fit on a single line it should be
split so that each parameter is on a separate line. The closing
``):`` is at the same indentation as the ``def`` keyword.

.. code-block:: python

    def some_function(
        some_very_long_parameter_name1,
        some_very_long_parameter_name2,
        some_keyword_parameter=12
    ):
        return 12
