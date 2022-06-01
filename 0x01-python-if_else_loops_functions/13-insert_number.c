#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a new node at a given position.
 * @head: head of list
 * @number: value of new node
 * Return: the address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *after, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if ((*head) == NULL)
	{
		new->next = NULL;
		*head = new;
		return (*head);
	}
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}	
	prev = after = *head;
	while (after->next)
	{
		after = after->next;
		if (after->n >= number)
			break;
		prev = after;
	}
	if (after->next == NULL)
	{
		new->next = NULL;
		after->next = new;
	}
	else
	{
		prev->next = new;
		new->next = after;
	}
	return (new);
}
