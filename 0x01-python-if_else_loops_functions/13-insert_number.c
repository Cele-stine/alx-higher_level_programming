#include "lists.h"

/**
 * insert_node - This is a function tat inserts a new node to a
 * sorted singly linked list
 * @head: the head node
 * @number: the number to insert
 * Return: the address of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new -> n = number;
	new -> next = NULL;
	if (*head == NULL || (*head) -> n >= new -> n)
	{
		new -> next = *head;
		*head = new;
		return (new);
	}
	else
	{
		current = *head;
		while (current -> next != NULL && current -> next -> n < new -> n)
		{
			current = current -> next;
		}
		new -> next = current -> next;
		current -> next = new;
		return (new);
	}
}
