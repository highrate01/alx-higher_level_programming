#include "lists.h"
/**
 * check_cycle - This function checks if a singly
 * linked list has a cycle in it.
 * list: pointer to the linked list
 * Return: 1 if there is  cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *forward, *fast_forward;

	if (!list || !list->next)
		return (0);
	forward = list;
	fast_forward = list;

	while(fast_forward != NULL && forward != NULL && forward->next)
	{
		fast_forward = fast_forward->next;
		forward = forward->next->next;

		if (fast_forward == forward)
			return (1);
	}
	return (0);
}
