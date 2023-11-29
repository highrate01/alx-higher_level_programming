#include "lists.h"
#include <stdlib.h>
#include <unistd.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linked list
 * @number: input
 *
 * Return: pointer to the new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *recent = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (recent && recent->n < number)
		{
			temp = recent;
			recent = recent->next;
		}
		temp->next = new;
		new->next = recent;
	}
	return (new);
}
