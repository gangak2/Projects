#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Idea is to receive data as a void data type and store them into a linked list

typedef struct Node{
	void *content;
	struct Node *next;
}_node;

typedef struct _StackImproved{
	int noElements;
	_node* head;
}_stackImproved;

_stackImproved* createStackImproved();
void emptyStackContentsImproved(_stackImproved* stack);
void destroyStackImproved(_stackImproved* stack);
int getNoElementsImproved(_stackImproved* stack);
int isEmptyImproved(_stackImproved* stack);
void* topImproved(_stackImproved* stack);
void pushImproved(void* item, _stackImproved* stack);
void* popImproved(_stackImproved* stack);

_stackImproved* createStackImproved(){
	_stackImproved* newStack = malloc(sizeof(_stackImproved));
	newStack->head = malloc(sizeof(_node));
	newStack->noElements = 0;
	return newStack;
}

void emptyStackContentsImproved(_stackImproved* stack){
	_node* thisNode = stack->head;
	_node* nextNode;
	while(1){
		nextNode = thisNode->next;
		free(thisNode);
		if(nextNode==NULL){
			break;
		}
		else thisNode=nextNode;
	}
}

void destroyStackImproved(_stackImproved* stack){
	emptyStackContentsImproved(stack);
	free(stack);
}

int getNoElementsImproved(_stackImproved* stack){
	return stack->noElements;
}

int isEmptyImproved(_stackImproved* stack){
	if(stack->noElements == 0)
    	return 1;
  	return 0;
}

void* topImproved(_stackImproved* stack){
	if(stack->noElements > 0){
		return stack->head->content;
	}
	fprintf(stderr, "No element in the stack, stack is empty");
  	return NULL;
}

void pushImproved(void* item, _stackImproved* stack){
	_node* newNode = malloc(sizeof(_node));
	newNode->content = item;
	newNode->next = NULL;
	if(stack->noElements == 0){
		stack->head = newNode;
	}
	else{
		newNode->next = stack->head;
		stack->head = newNode;
	}
	stack->noElements++;
}

void* popImproved(_stackImproved* stack){
	void* retVal;
	if(stack->noElements > 0){
		_node* p = stack->head;
		stack->noElements--;
		retVal = p->content;
		stack->head = p->next;
		free(p);
		return retVal;
	}
	fprintf(stderr, "No element in the stack, stack is empty");
  	return NULL;
}
