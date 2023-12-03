#include "lists.h"

/**
 * add_nodeint_end - add new node at the end of a
 * listsint_t list
 *
 * @head: pointer to the pointer of first node
 * @n: number to be included in new node
 * Return: address of the new element on success,
 * NULL otherwise
 */
listsint_t *add_nodeint_end(listint_int **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = n;
	new->next = NULL;

	if (!*head)
		*head = new;
	else
	{
		while (current->next)
			current = current->next;
		current->next = new;
	}
	return (new);
}
/**
 * free_listint - free lists
 * @head: pointer to list to be freed
 * Return: nothing
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
