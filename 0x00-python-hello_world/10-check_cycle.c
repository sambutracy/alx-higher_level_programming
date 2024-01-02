#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	while (slower != NULL && faster != NULL && faster->next != NULL)
	{
		slower = slower->next;
		faster = faster->next->next;

		if (slower == faster)
			return (1); /* Cycle detected */
	}

	return (0); /* No cycle */
}
