#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct RegistroTelefono {
    string nombre;
    vector<string> telefonos;
};

vector<RegistroTelefono> directorio;

void ingresarRegistro() {
    RegistroTelefono nuevoRegistro;
    cout << "Ingrese el nombre del usuario: ";
    cin >> nuevoRegistro.nombre;
    cout << "Ingrese al menos un número de teléfono (hasta 3):" << endl;
    for (int i = 0; i < 3; i++) {
        string telefono;
        cout << "Teléfono " << i+1 << ": ";
        cin >> telefono;
        if (!telefono.empty()) {
            nuevoRegistro.telefonos.push_back(telefono);
        } else {
            break;
        }
    }
    directorio.push_back(nuevoRegistro);
}

void mostrarDirectorio() {
    cout << "Directorio Telefónico:" << endl;
    for (int i = 0; i < directorio.size(); i++) {
        cout << directorio[i].nombre << ": ";
        for (int j = 0; j < directorio[i].telefonos.size(); j++) {
            cout << directorio[i].telefonos[j] << " ";
        }
        cout << endl;
    }
}

void modificarRegistro() {
    string nombre;
    cout << "Ingrese el nombre del usuario que desea modificar: ";
    cin >> nombre;
    bool encontrado = false;
    for (int i = 0; i < directorio.size(); i++) {
        if (directorio[i].nombre == nombre) {
            cout << "Ingrese el nuevo número de teléfono o deje en blanco para no modificar:" << endl;
            for (int j = 0; j < 3; j++) {
                string telefono;
                cout << "Teléfono " << j+1 << ": ";
                cin >> telefono;
                if (!telefono.empty()) {
                    directorio[i].telefonos[j] = telefono;
                } else {
                    break;
                }
            }
            encontrado = true;
            break;
        }
    }
    if (!encontrado) {
        cout << "El nombre ingresado no se encuentra en el directorio." << endl;
    }
}

void buscarTelefono() {
    string nombre;
    cout << "Ingrese el nombre del usuario para buscar su teléfono: ";
    cin >> nombre;
    bool encontrado = false;
    for (int i = 0; i < directorio.size(); i++) {
        if (directorio[i].nombre == nombre) {
            cout << "El teléfono(s) de " << nombre << " es: ";
            for (int j = 0; j < directorio[i].telefonos.size(); j++) {
                cout << directorio[i].telefonos[j] << " ";
            }
            cout << endl;
            encontrado = true;
            break;
        }
    }
    if (!encontrado) {
        cout << "El nombre ingresado no se encuentra en el directorio." << endl;
    }
}

int main() {
    while (true) {
        cout << endl;
        cout << "Ingrese el número correspondiente a la acción que desea realizar:" << endl;
        cout << "1. Ingresar nuevo registro al directorio" << endl;
        cout << "2. Mostrar todo el directorio" << endl;
        cout << "3. Modificar registro existente" << endl;
        cout << " ";
    }
}
