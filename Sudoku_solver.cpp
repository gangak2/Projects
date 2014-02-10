#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define GridSize 9
#define UnfilledCell 0

void print_solution(int **);
bool Solvable(int **);
bool Findtraceable(int **, int *, int *);
bool RowSafety(int **, int, int);
bool ColSafety(int **, int, int);
bool MiniGridSafety(int **, int , int , int);
bool CheckSafety(int **, int , int , int);

void print_solution(int **array){
	for(int i=0;i < GridSize;i++){
		for(int j=0;j < GridSize;j++){
			printf("%d ",array[i][j]);
		}
		printf("\n");
	}
}

bool Findtraceable(int **array, int *row, int *col){
	for(*row=0;*row < GridSize;(*row)++){
		for(*col=0;*col < GridSize;(*col)++){
			if(array[*row][*col]==UnfilledCell)
				return true;
		}
	}
	return false;
}

bool RowSafety(int **array, int row, int attempt){
	for(int i=0;i < GridSize;i++){
		if(array[row][i]==attempt)
			return false;
	}
	return true;
}

bool ColSafety(int **array, int col, int attempt){
	for(int i=0;i < GridSize;i++){
		if(array[i][col]==attempt)
			return false;
	}
	return true;
}

bool MiniGridSafety(int **array, int row, int col, int attempt){
	for(int i=row;i<row+3;i++){
		for(int j=col;j<col+3;j++){
			if(array[i][j]==attempt)
				return false;
		}
	}
	return true;
}

bool CheckSafety(int **array, int row, int col, int attempt){
	if(RowSafety(array,row,attempt) && ColSafety(array,col,attempt) && MiniGridSafety(array,row-row%3,col-col%3,attempt))
		return true;
	else
		return false;
}

bool Solvable(int **array){
	int row,col;
	if(!Findtraceable(array,&row,&col)){
		return true;
	}
	else{
		//printf("%d\t%d\n",row,col);
		for(int attempt=1;attempt<=9;attempt++){
			if(CheckSafety(array,row,col,attempt)){
				array[row][col]=attempt;
				if(Solvable(array)){
					return true;
				}
				array[row][col]=UnfilledCell;
			}
		}
	}
	return false;
}

int main(){
	int **input_grid;
	input_grid = (int **)malloc(GridSize*sizeof(int*));
	for(int i=0;i < GridSize;i++){
		input_grid[i] = (int *)malloc(GridSize*sizeof(int));
	}
	for(int i=0;i<9;++i){
		for(int j=0;j<9;++j){
			scanf("%d",&input_grid[i][j]);
		}
	}
	printf("\n");
	if(Solvable(input_grid)){
		print_solution(input_grid);
	}
	else{
		printf("No Solution found\n");
	}
	return 0;
}