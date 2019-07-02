.. _`Python Style Guidelines`:

Python Style Guidelines
=======================

Style should follow PEP8_ and PEP257_ in cases where this guideline
does not state a different preference.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _PEP257: https://www.python.org/dev/peps/pep-0257/

.. toctree::
   :numbered:

.. contents:: Table of Contents

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

They can also be done with parameter names, if they fit.

.. code-block:: python

    some_variable = some_function(param1=12, param2=32, param3=21)

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

Strings.
--------

Strings should use `'`, unless `'` needs to be a character in the
string.

.. code-block:: python

    some_string = 'abcdefg'

Multi-line strings.
-------------------

Opening and closing brackets should be on separate lines and
spaces should be at the end of the line, not the start.

.. code-block:: python

    some_multiline_string = (
        'this is a '
        'multiline '
        'string.'
    )

Docstrings.
-----------

Docstrings should open with three single quotes `'''`.
The first line of a docstring should always be on the line below
the opening `'''`. The closing `'''` always needs to be on its own
line and preceded by an empty line. The docstring must be followed by
an empty line.

.. code-block:: python

    def some_fn():
        '''
        This is a docstring.

        '''

        foo()
        return bar(12)


Docstring markup.
-----------------

Docstrings should use `numpy style formatting`_.
The examples below explains the markup to be used.

.. code-block:: python

    def some_fn(param1, param2, param3, param4, param5=12):
        '''
        The first line of the docstring.

        When literal, code values are specified they should be between
        two backticks, for example if I was to say that the default
        value of `param5` is ``12``. Argument names, such as
        `param5` or `param1` are surrounded by a single backtick.

        Simple code expressions, such as ``UserDefinedType(12) + 12``
        are also surrounded by two backticks. When multi-line or
        complicated code expressions are to be described, they
        should be performed in a code block.

        .. code-block:: python

            # This is a multi-line code example.
            variable_name = 'one two three'
            for i in range(10):
                print(i**2)

        Sometimes when talking about an attribute in a class we first
        want to make it clear to the reader what attribute we are
        referring to exactly so the :attr:`.SomeTypeName.attr_name`
        syntax is used. However as we continue to refer to
        :attr:`~.SomeTypeName.attr_name`, it is unnecessary to continue
        to state the class in front of the attribute, as it should be
        obvious to the reader by this point, so the ~ can be added to
        remove the class name from the compiled documentation. Use
        the ~ as appropriate to maximize the readability of the
        compiled documentation.

        Parameters
        ----------
        param1 : :class:`int`
            When the type being described is a builtin type, such as
            :class:`int` or :class:`str`, it should have the form
            the :class:`type_name`.

        param2 : :class:`.UserDefinedType`
            When the type being described refers to a user defined
            type within the same library, make sure the type name
            is preceded by a period.

        param3 : :class:`other.UserDefinedType`
            When the type being described refers to a user defined
            type in another library, state the name of the library
            and name the type. If the type is in a submodule of the
            library DO NOT name the submodules. For example, we may
            want to document the use of a :class:`numpy.ndarray`.

        param4 : :class:`~.mod.submod.subsubmod.UserDefinedType`
            Sometimes there may be two user defined types in the
            same library with the same name but defined in different
            submodules of the library. If we want to refer to form a
            hyperlink, we have to add the the necessary submodule
            names in front of the user defined type's name, so that
            it is unambiguous which type is being referred to. The
            ~ means that the submodule names will be removed from the
            compiled documentation. This means that the ~ can be
            removed or kept, depending on what is less confusing to
            the reader.

        param5 : :class:`int`, optional
            When the parameter is optional, it should be stated as
            optional after the type declaration.

        Returns
        -------
        :class:`int`
            Returns a number.

        '''

        return 12

    class SomeType:
        '''
        An example type.

        Note that class docstrings should not document the attributes
        defined in a parent class, unless there is something different
        about them.

        Attributes
        ----------
        alpha : :class:`int`
            Attributes defined within this class are referred to by
            the :attr:`alpha` or :attr:`beta` syntax.

        beta : :class:`str`
            Attributes of a different class are referred to by
            preceding with a period and the type name, for example
            :attr:`.SomeOtherType.attribute_name`.

        '''

        def __init__(self):
            self.alpha = 1
            self.beta = 'b'

.. _`numpy style formatting`: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
