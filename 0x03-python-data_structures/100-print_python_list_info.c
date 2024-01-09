#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic information about a Python list
 * @p: Python list object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloc, i;
	PyObject *item;

	/* Get size and allocated space of the list */
	size = Py_SIZE(p);
	alloc = list->allocated;

	/* Print size and allocated space information */
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	/* Loop through each element in the list and print its type */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
