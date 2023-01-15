#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if palindrome
 * @head: head of node
 *
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{

	if (head == NULL || *head == NULL)
		return (1);

	if (p_check(head, *head))
	{
		return (1);
	}
	return (0);
}

/**
 * p_check - check for palindrome
 * @left: Go left
 * @right: Go right
 *
 * Return: integer
 */

int p_check(listint_t **left, listint_t *right)
{
	int is_p = 0;

	if (right)
	{
		is_p = p_check(left, right->next);
	}
	else
	{
		return (1);
	}

	if (is_p == 1)
	{
		if ((*left)->n == right->n)
		{
			(*left) = (*left)->next;
			return (1);
		}
	}
	return (0);
}
