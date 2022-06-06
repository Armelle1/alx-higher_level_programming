#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int n; /* number of nodes */
	int values[10];
	int i, j;

	if (head == NULL || *head == NULL)
		return (0);
	current = *head;
	n = 0;
	while (current != NULL)
	{
		values[n] = current->n;
		current = current->next;
		n++;
	}
	for (i = 0, j = n - 1; i < n; i++, j--)
	{
		if (values[i] != values[j])
		{
			return (0);
		}
	}
	return (1);
}
