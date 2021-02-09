class LivroQualquer():     
    def __init__(self, titulo = str, autor= str, editora= str, lancamento= str,  paginas= str, emprestimo= str, estado= str, assunto= str, arq = str, __isbn= str):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.lancamento = lancamento
        self.paginas = paginas
        self.emprestimo = emprestimo
        self.estado = estado
        self.assunto = assunto
        self.arq = arq
        self.__isbn = __isbn

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        __isbn =  str(__isbn)
        if len(__isbn) < 13  or len(__isbn) > 13:
            raise ValueError("Caracteres insuficiente para ISBN") 
        print("setter method called")
        self.__isbn =  isbn 

    @staticmethod
    def verificar_isbn(__isbn= str):
        b = list(__isbn.replace('-',''))
        k = []
        for val in b:
            k.append(int(val))
        c, d, item = k[:12:2], k[1::2], k[12]
        g, h = list(map(lambda x: x * 1, c)), list(map(lambda x: x * 3, d))
        lista = g + h
        soma = sum(lista)
        porc = soma % 10
        result = 10 - porc
        if result == item:
            return True
        else:
            return None 

class LivroFisico(LivroQualquer):
    def __init__(self, titulo = str, autor= str, editora= str, lancamento= str,  paginas= str, emprestimo= str, estado= str, assunto= str,arq= str, __isbn= str, capa= str, localizacao= str, aluno= str, professor=str):
        super().__init__(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, arq, __isbn) 
        self.capa = capa
        self.localizacao = localizacao


class LivroDigital(LivroQualquer):    
    def __init__(self, titulo = str, autor= str, editora= str, lancamento= str,  paginas= str, emprestimo= str, estado= str, assunto= str,arq= str, __isbn= str, url= str, tamanho= str):
        super().__init__(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto,arq, __isbn)
        self.url = url
        self.tamanho = tamanho


class Sistema():
    def __init__(self):
        self.livro_qualquer = LivroQualquer(0,0,0,0,0,0,0,0,0,0)
        self.livro_fisico = LivroFisico(0,0,0,0,0,0,0,0,0,0,0,0)
        self.livro_digital = LivroDigital(0,0,0,0,0,0,0,0,0,0,0,0)
        self.livros_cadastrados = []
        self.list_livro_digital = []
        self.list_livro_fisico = []
    
    def buscar_livro(self, livros_cadastrados= str, titulo= str):
        for livro in self.livros_cadastrados:
                if livro["titulo"] == titulo:
                    return livro
        return None
    
    def addLivroFisico(self, titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, arq, __isbn, capa, localizacao, aluno, professor ):
        if self.buscar_livro(self.livros_cadastrados, titulo) is None:
            livro = {"titulo":titulo,    
                    "autor": autor,
                    "lançamento": lancamento,
                    "editora": editora,
                    "isbn": __isbn,
                    "paginas": paginas,
                    "emprestimo": emprestimo,
                    "estado": estado,
                    "assunto": assunto,
                    "capa": capa,
                    "localizacao": localizacao,
                    "aluno": aluno,
                    "professor": professor}
            self.livros_cadastrados.append(livro)
            self.list_livro_fisico.append(livro)
            print('Livro cadastrado com sucesso!')
            return True
        else:
            print('Livro já cadastrado!')
            return False
        
    def addLivroDigital(self, titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, arq, __isbn, url, tamanho):
        if self.buscar_livro(self.livros_cadastrados, titulo) is None:
            livro = {"titulo":titulo,    
                    "autor": autor,
                    "lançamento": lancamento,
                    "editora": editora,
                    "isbn": __isbn,
                    "paginas": paginas,
                    "emprestimo": emprestimo,
                    "estado": estado,
                    "assunto": assunto,
                    "url": url,
                    "tamanho": tamanho,}
            self.livros_cadastrados.append(livro)
            self.list_livro_digital.append(livro)
            print('Livro cadastrado com sucesso!')
            return True
        else:
            print('Livro já cadastrado!')
            return False
        for livro in self.list_livro_digital:
            if novo_livro.nome == livro.nome:
                print("Livro já cadastrado!")
                return False
        self.list_livro_digital.append(novo_livro)
        self.livros_cadastrados.append(novo_livro)
        print("Livro cadastrado com sucesso!")

    def remvLivroFisico(self,nome_livro):
        for livro in self.list_livro_fisico:
            if nome_livro is None:
                print("Livro inexistente")
                return False
            else:
                self.list_livro_fisico.remove(livro)
                self.livros_cadastrados.remove(livro)
                print("Livro Removido")
                return True

    def remvLivroDigital(self,nome_livro):
        for livro in self.list_livro_digital:
            if nome_livro is None:
                print("Livro inexistente")
                return False
            else:
                self.list_livro_digital.remove(livro)
                self.livros_cadastrados.remove(livro)
                print("Livro Removido")
                return True

    def atlLivroDigital(self, titulo):
        self.remvLivroDigital(titulo)
        titulo = input("titulo: ")
        autor = input("autor: ")
        editora = input("editora: ")
        lancamento = input("lançamento: ")
        paginas = input("paginas: ")
        __isbn = input("isbn (Ex.:9783161484100): ")
        url = input("url: ")
        tamanho = input("tamanho: ")
        emprestimo = input("emprestimo: ")
        estado = input("estado: ")
        assunto = input("assunto: ")
        fisicoOUdigital = False
        if len(__isbn) < 13  or len(__isbn) > 13:
            self.livro_qualquer.verificar_isbn(__isbn)
            print('ISBN-13 inválido!')
            return None
        else:
            self.livro_digital.__init__( titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, url, tamanho )
            self.addLivroDigital(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, url, tamanho)
        

    def atlLivroFisico(self, titulo):
        self.remvLivroFisico(titulo)
        titulo = input("titulo: ")
        autor = input("autor: ")
        editora = input("editora: ")
        lancamento = input("lançamento: ")
        paginas = input("paginas: ")
        __isbn = input("isbn (Ex.:9783161484100): ")
        capa = input("tipo de capa: ")
        localizacao = input("localização: ")
        emprestimo = input("emprestimo: ")
        estado = input("estado: ")
        assunto = input("assunto: ")
        fisicoOUdigital = False
        if assunto.lower()== 'manuscrito':
            aluno = input("aluno:")
            professor =  input("professor:")
            if len(__isbn) < 13  or len(__isbn) > 13:
                self.livro_qualquer.verificar_isbn(__isbn)
                print('ISBN-13 inválido!')
                return False
            else:
                self.livro_fisico.__init__(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao, aluno, professor)
                self.addLivroFisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao, aluno, professor)   
        else:
            if len(__isbn) < 13  or len(__isbn) > 13:
                self.livro_qualquer.verificar_isbn(__isbn)
                print('ISBN-13 inválido!')
                return False
            else:
                self.livro_fisico.__init__(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao, 0, 0)
                self.addLivroFisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao,0, 0)


    def imprimir_nome_livros(self):
        print("Livros:")
        print(self.livros_cadastrados)
        
    def buscar_autor(self, autor= str):
        for indice, autor2 in enumerate(self.livros_cadastrados):
            if autor2.get('autor') == autor:
                print('Livros: ', autor2)

    def salvar_arquivo(self, arq= str):
        arquivo = open(arq, "a")
        letra = str(self.livros_cadastrados) + '\n'
        arquivo.write(letra)
        arquivo.close()
        print('Arquivo salvo com sucesso')
        return arquivo
                    

class Menu():
    def __init__(self):
        self.livro_qualquer = LivroQualquer(0,0,0,0,0,0,0,0,0,0)
        self.livro_fisico = LivroFisico(0,0,0,0,0,0,0,0,0,0,0,0)
        self.livro_digital = LivroDigital(0,0,0,0,0,0,0,0,0,0,0,0)
        self.sistema = Sistema()

    def imprimir_opcao(self):
        print("")
        print("1 - Livro Físico")
        print("2 - Livro Digital")
        print("")

    def imprimir_comandos(self):
        print("")
        print("MENU:")
        print("1 - Cadastrar Livro")
        print("2 - Remover Livro")
        print("3 - Atualizar informação de livro")
        print("4 - Buscar livros por autor")
        print("5 - Imprimir Livros Cadastrados")
        print("6 - Salvar e Sair")
        print("")

    def main(self):
        self.imprimir_comandos()
        opcao = int(input("Digite uma opção acima: "))
        while opcao in [1, 2, 3, 4, 5, 6]:
            if opcao == 1:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                print("")
                while opcao in [1, 2]:
                    if opcao == 1: 
                        fisicoOUdigital = True
                        titulo = input("titulo: ")
                        autor = input("autor: ")
                        editora = input("editora: ")
                        lancamento = input("lançamento: ")
                        paginas = input("paginas: ")
                        __isbn = str(input("isbn (Ex.:9783161484100): "))
                        capa = input("tipo de capa: ")
                        localizacao = input("localização: ")
                        emprestimo = input("emprestimo: ")
                        estado = input("estado: ")
                        assunto = input("assunto: ")
                        if assunto.lower()== 'manuscrito':
                            aluno = input("aluno:")
                            professor =  input("professor:")
                            if len(__isbn) < 13  or len(__isbn) > 13:
                                self.livro_qualquer.verificar_isbn(__isbn)
                                print('ISBN-13 inválido!')
                                return False
                            else:
                                self.livro_fisico.__init__(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao, aluno, professor)
                                self.sistema.addLivroFisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao, aluno, professor)   
                        else:
                            if len(__isbn) < 13  or len(__isbn) > 13:
                                self.livro_qualquer.verificar_isbn(__isbn)
                                print('ISBN-13 inválido!')
                                return False
                            else:
                                self.livro_fisico.__init__(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao, 0, 0)
                                self.sistema.addLivroFisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, capa, localizacao,0, 0)
                        break

                    elif opcao == 2:
                        titulo = input("titulo: ")
                        autor = input("autor: ")
                        editora = input("editora: ")
                        lancamento = input("lançamento: ")
                        paginas = input("paginas: ")
                        __isbn = input("isbn (Ex.:9783161484100): ")
                        url = input("url: ")
                        tamanho = input("tamanho: ")
                        emprestimo = input("emprestimo: ")
                        estado = input("estado: ")
                        assunto = input("assunto: ")
                        fisicoOUdigital = False
                        if len(__isbn) < 13  or len(__isbn) > 13:
                            self.livro_qualquer.verificar_isbn(__isbn)
                            print('ISBN-13 inválido!')
                            return None
                        else:
                            self.livro_digital.__init__( titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, url, tamanho )
                            self.sistema.addLivroDigital(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, 0, __isbn, url, tamanho)
                    break

            elif opcao == 2:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                print("")
                while opcao in [1, 2]:
                    if opcao == 1: 
                        titulo = input('Titulo que deseja remover: ')
                        self.sistema.remvLivroFisico(titulo)
                        break
                    elif opcao == 2:
                        titulo = input('Titulo que deseja remover: ')
                        self.sistema.remvLivroDigital(titulo)
                        break        

            elif opcao == 3:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                while opcao in [1, 2]:
                    if opcao == 1:
                        titulo = input("Titulo que deseja atualizar:")
                        self.sistema.atlLivroFisico(titulo)
                        break
                    elif opcao == 2:    
                        titulo = input("Titulo que deseja atualizar:")
                        self.sistema.atlLivroDigital(titulo)
                        break

            elif opcao == 4:
                autor = input('Autor que desejas buscar: ')
                self.sistema.buscar_autor(autor)
                    
            elif opcao == 5:
                self.sistema.imprimir_nome_livros()

            elif opcao == 6:
                arq = input('Digite o nome do arquivo: ')
                self.sistema.salvar_arquivo(arq)
                exit()

            self.imprimir_comandos()
            opcao = int(input("Digite uma opção acima: "))


if __name__ == "__main__":
    g = Menu()
    g.main()
