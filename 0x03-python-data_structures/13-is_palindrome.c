#include "lists.h"
/**
 * is_palindrome - function to check a palindrome (symmetry)
 * @head: pointer to pointer to var head
 * Return: output
*/
int is_palindrome(lsitint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}
/**
 * aux_palind - auxiliary function
 * @head: pointer to pointer to var head
 * @end: end of linked list
 * Return: 0 on success
*/
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
