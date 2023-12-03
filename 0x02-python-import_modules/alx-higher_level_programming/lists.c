#include "lists.h"

/**
 * print_listint - prints all elements of listint list
 * @h: pointer to the head
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;

	while (current)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}
