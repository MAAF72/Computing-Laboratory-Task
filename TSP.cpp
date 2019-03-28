#include <iostream>
#include <vector>
#include <algorithm>
#define ROW 19
#define COLUMN 19

typedef long long ll;

using namespace std;

int Edge[ROW][COLUMN];
vector<int> Vertex;

void AddVertex(char V) {
	Vertex.push_back(V - 'A');
}

void AddEdge(char A, char B, int W) {
	int i = A - 'A';
	int j = B - 'A';
	Edge[i][j] = Edge[j][i] = W;
}

void InitializeEdge() {
	for(int i = 0; i < ROW; i++) {
		for(int j = 0; j < COLUMN; j++) {
			Edge[i][j] = -1;
		}
	}
}

ll TSP(char Start) {
	int MinWeight = INT_MAX;
	vector<char> Path;
	do {
		vector<char> CurrPath;
		int CurrWeight = 0;
		
		bool Valid = true;
		int CurrVertex = Start - 'A';
		for(int i = 0; ((i < (int)Vertex.size()) && Valid); i++) {
			if(Edge[CurrVertex][Vertex[i]] != -1) {
				CurrWeight += Edge[CurrVertex][Vertex[i]]; //Vertex[i] = Next Vertex
				CurrVertex = Vertex[i];
				CurrPath.push_back((char)(Vertex[i] + 'A')); //Pushing CurrVertex to the path
			} else {
				Valid = false;
			}
		}
		
		if(Valid) {
			if(Edge[CurrVertex][Start - 'A'] != -1) {
				CurrWeight += Edge[CurrVertex][Start - 'A']; //Adding Edge CurrVertex - Start Vertex
				CurrPath.push_back(Start);
				if(CurrWeight < MinWeight) {
					MinWeight = CurrWeight;
					Path = CurrPath;
				}
			}
		}
	} while(next_permutation(Vertex.begin(), Vertex.end())); //Generate Permutation between Vertex begin - Vertex end, lexicographicaly
	
	cout << Start;
	for(auto P : Path) {
		cout << " " << P;
	}
	cout << endl;
	return MinWeight;
}

int main() {
	InitializeEdge();
	
	AddVertex('A');
	AddVertex('B');
	AddVertex('C');
	AddVertex('D');
	AddVertex('E');
	AddVertex('F');
	AddVertex('G');
	//AddVertex('S'); Start Point
	
	AddEdge('S', 'A', 6);
	AddEdge('S', 'B', 14);
	AddEdge('S', 'C', 10);
	
	AddEdge('A', 'B', 6);
	AddEdge('B', 'C', 4);
	
	AddEdge('A', 'D', 24);
	AddEdge('B', 'E', 15);
	AddEdge('C', 'F', 18);
	
	AddEdge('D', 'E', 4);
	AddEdge('E', 'F', 4);
	
	AddEdge('D', 'G', 9);
	AddEdge('E', 'G', 9);
	AddEdge('F', 'G', 9);
	
	cout << TSP('S') << endl;
	return 0;
}