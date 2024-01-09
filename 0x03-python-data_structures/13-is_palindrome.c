#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	int is_palindrome = 1;

	if (*head == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}

		prev = prev->next;
		slow = slow->next;
	}
	prev = NULL;
	slow = *head;

	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	*head = prev; /* Update the head pointer */

	return is_palindrome;
}
