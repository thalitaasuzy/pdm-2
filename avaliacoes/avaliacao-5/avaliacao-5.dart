import 'dart:io';
import 'package:sqlite3/sqlite3.dart';

void main() {
  final db = sqlite3.open('database.db');

  // Criação da tabela TB_ALUNO
  db.execute('''
    CREATE TABLE IF NOT EXISTS TB_ALUNO (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL
    )
  ''');

  // Função para adicionar um aluno
  void adicionarAluno(String nome) {
    db.execute('INSERT INTO TB_ALUNO (nome) VALUES (?)', [nome]);
    print('Aluno adicionado: $nome');
  }

  // Função para listar todos os alunos
  void listarAlunos() {
    final result = db.select('SELECT * FROM TB_ALUNO');
    if (result.isEmpty) {
      print('Nenhum aluno encontrado.');
    } else {
      for (final row in result) {
        print('ID: ${row['id']}, Nome: ${row['nome']}');
      }
    }
  }

  // Função para inicializar o banco de dados com um aluno e listar os alunos
  void inicializarEListar() {
    // Adiciona o aluno "José"
    adicionarAluno('José');

    // Lista todos os alunos
    print('\nLista de alunos após adicionar José:');
    listarAlunos();
  }

  // Chama a função para inicializar e listar alunos
  inicializarEListar();

  // Recebendo input do usuário
  while (true) {
    print('\nEscolha uma opção:');
    print('1. Adicionar aluno');
    print('2. Listar alunos');
    print('3. Sair');
    final escolha = stdin.readLineSync();

    switch (escolha) {
      case '1':
        print('Digite o nome do aluno:');
        final nome = stdin.readLineSync();
        if (nome != null && nome.isNotEmpty) {
          adicionarAluno(nome);
        } else {
          print('Nome inválido.');
        }
        break;
      case '2':
        listarAlunos();
        break;
      case '3':
        db.dispose();
        print('Saindo...');
        return;
      default:
        print('Opção inválida.');
    }
  }
}
