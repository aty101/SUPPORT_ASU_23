#include <iostream>
using namespace std;

int main() {
	
	
	char choice;
	string plain_text;
	string cipher_text;
	long long key;
	int ascii=0;

	cout << "(Encyption=> E & e) or (decryption=> D & d) : ";
	cin >> choice;

	if (choice == 'E' || choice == 'e') {

		cout << "Enter the text : ";
		cin >> plain_text;
		cout << "Enter the key : ";
		cin >> key;


		for (int i = 0; i < plain_text.length(); i++) {
			ascii = plain_text[i];

			if (ascii >= 65 && ascii <= 90) {
				ascii -= 64;
				cipher_text += ((ascii + key) % 26) + 64;
			}
			else if (ascii >= 97 && ascii <= 122) {
				ascii -= 96;
				cipher_text += ((ascii + key) % 26) + 96;
			}

		}
		cout << cipher_text;
	}
	else if (choice == 'D' || choice == 'd') {
		cout << "Enter the text : ";
		cin >> cipher_text;
		cout << "Enter the key : ";
		cin >> key;


		for (int i = 0; i < cipher_text.length(); i++) {
			ascii = cipher_text[i];

			if (ascii >= 65 && ascii <= 90) {
				ascii -= 64;
				plain_text += (((ascii - key)+26) % 26) + 64;
			}
			else if (ascii >= 97 && ascii <= 122) {
				ascii -= 96;
				plain_text += (((ascii - key) + 26) % 26) + 96;
			}

		}
		cout << plain_text;
	}


	return 0;
}