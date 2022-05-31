#include "lists.h"

/**
 * check_cycle - checks for a loop in singly linked list
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *nextt;
	listint_t *prev;

	nextt = list;
	prev = list;
	while (list && nextt && p2->nextt)
	{
		list = list->next;
		nextt = nextt->next->next;

		if (list == nextt)
		{
			list = prev;
			prev =  nextt;
			while (1)
			{
				nextt = prev;
				while (nextt->next != list && nextt->next != prev)
				{
					nextt = nextt->next;
				}
				if (nextt->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
