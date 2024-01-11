#include <stdio.h>
#include <stddef.h>
#include "lists.h"

/**
 * print_dlistint - prints a doubly linked list,
 * @h:  pointer to the head
 * Return: Number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current;
	size_t nodeCount;

	current = h;
	nodeCount = 0;

	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		nodeCount++;
	}
	return (nodeCount);
}
