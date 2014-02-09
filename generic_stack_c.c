#include "generic_stack_c.h"

typedef struct _Students{
	char *Name;
	int Roll_number;
}_students;

int main(){
	// Demonstration for integer stack
 	_stackImproved* intStack = createStackImproved();
 	int squares[100],i;
 	for(i=0;i<100;i++){
 		squares[i] = i*i;
 	}
    int x = 500, y = 1000, z = 1500;
 
    if(isEmptyImproved(intStack)){
        printf("The stack is empty.\n");
    } 
    else{
        printf("The stack is not empty.\n");
    }

    for(i=0;i<100;i++){
    	pushImproved(&squares[i],intStack);
    }
    
    if(isEmptyImproved(intStack)){
        printf("The stack is empty.\n");
    } else {
        printf("The stack is not empty.\n");
    }

    printf("\nPopping %d\n", *(int*)popImproved(intStack));
    printf("\nThe element at top is %d\n", *(int*)topImproved(intStack));
 
 	// Demonstration for String stack
 	_stackImproved* stringStack = createStackImproved();

    char* book1 = "Harry potter and sorcesors stone";
    char* book2 = "Harry potter and chamber of secrets";
    char* book3 = "Harry potter and the prisoner of Azkaban";
    char* book4 = "Harry potter and the Goblet of fire";
    char* book5 = "Harry potter and Order of phoenix";
    char* book6 = "Harry potter and Half blood prince";
    char* book7 = "Harry potter and Deathly hallows";
    pushImproved(book1, stringStack);
    pushImproved(book2, stringStack);
    pushImproved(book3, stringStack);
    pushImproved(book4, stringStack);
    pushImproved(book5, stringStack);
    pushImproved(book6, stringStack);
    pushImproved(book7, stringStack);
    printf("We popped: %s\n", (char*)popImproved(stringStack));
    printf("The element at top is now: %s\n", (char*)topImproved(stringStack));

    // Demonstration for struct stack
    _stackImproved* structStack = createStackImproved();

    _students* Student1 = malloc(sizeof(_students));
    Student1->Name = "Gangaprasad Koturwar";
    Student1->Roll_number = 10259;
    _students* Student2 = malloc(sizeof(_students));
    Student2->Name = "Abhishek Dalmia";
    Student2->Roll_number = 10018;

    pushImproved(Student1,structStack);
    pushImproved(Student2,structStack);

    _students* popped = (_students*)popImproved(structStack);
    printf("We popped the student %s having roll number %d\n", popped->Name, popped->Roll_number);
    destroyStackImproved(intStack);
    destroyStackImproved(stringStack);
    return 0;
} 