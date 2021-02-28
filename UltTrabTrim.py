class LivroQualquer():     
    def __init__(self, titulo= str, autor= str, editora= str, lancamento= str,  paginas= str, emprestimo= str, estado= str, assunto= str, arq= str, isbn= str):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.lancamento = lancamento
        self.paginas = paginas
        self.emprestimo = emprestimo
        self.estado = estado
        self.assunto = assunto
        self.arq = arq
        self.__isbn = isbn

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self):
        isbn =  str(isbn)
        b = list(isbn)
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
            raise ValueError('ISBN é válido!')
            return True
        else:
            print('ISBN é inválido!')
            return None 
        print("setter method called")
        self.__isbn = isbn

class LivroFisico(LivroQualquer):
    def __init__(self, titulo= str, autor= str, editora= str, lancamento= str,  paginas= str, emprestimo= str, estado= str, assunto= str, arq= str, isbn= str, capa= str, localizacao= str, aluno= str, professor= str):
        super().__init__(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, arq, isbn) 
        self.capa = capa
        self.localizacao = localizacao
        self.aluno =  aluno
        self.professor =  professor
        self.livros_cadastrados = []

    def verificar_sistema(self, titulo):
        for livro in self.livros_cadastrados:
            if livro["titulo"] == titulo: 
                return livro
        return True

    def cadastrar_livrofisico(self,titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, arq, isbn, capa, localizacao, aluno, professor):
        livro = {"titulo":titulo,    
                "autor": autor,
                "lançamento": lancamento,
                "editora": editora,
                "isbn": isbn,
                "paginas": paginas,
                "emprestimo": emprestimo,
                "estado": estado,
                "assunto": assunto,
                "capa": capa,
                "localizacao": localizacao,
                "aluno": aluno,
                "professor": professor}
        self.livros_cadastrados.append(livro)
        print('Livro cadastrado com sucesso!')
        return True

    def remover_livrofisico(self,nome_livro):
        for livro in self.livros_cadastrados:
            if nome_livro is None:
                print("Livro inexistente")
                return False
            else:
                self.livros_cadastrados.remove(livro)
                print("Livro Removido")
                return True

    def atualizar_livrofisico(self, titulo):
        self.remover_livrofisico(titulo)
        titulo = input("titulo: ")
        autor = input("autor: ")
        editora = input("editora: ")
        lancamento = input("lançamento: ")
        paginas = input("paginas: ")
        isbn = int(input("isbn(Ex.:9783161484100): "))
        capa = input("tipo de capa: ")
        localizacao = input("localização: ")
        emprestimo = input("emprestimo: ")
        estado = input("estado: ")
        assunto = input("assunto: ")
        if assunto.lower()== 'manuscrito':
            aluno = input("aluno:")
            professor =  input("professor:")
            self.cadastrar_livrofisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto,0, isbn, capa, localizacao, aluno, professor)                                  
        else:
            self.cadastrar_livrofisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto,0, isbn,capa,localizacao, 0, 0)

    def buscar_autor(self, autor= str):
        for indice, autor2 in enumerate(self.livros_cadastrados):
            if autor2.get('autor') == autor:
                print('Livros Fisicos: ', autor2)

    def imprimir_nome_livros(self):
        print("Livros Fisicos:")
        print(self.livros_cadastrados)

    def salvar_arquivo(self, arq= str):
        arquivo = open(arq, "a")
        letra = str(self.livros_cadastrados) + '\n'
        arquivo.write(letra)
        arquivo.close()
        print('Arquivo salvo com sucesso')
        return arquivo


class LivroDigital(LivroQualquer):    
    def __init__(self,titulo= str, autor= str, editora= str, lancamento= str,  paginas= str, emprestimo= str, estado= str, assunto= str, arq= str, isbn= str, url= str, tamanho= str):
        super().__init__(titulo , autor, editora, lancamento,  paginas, emprestimo, estado, assunto, arq, isbn)
        self.url = url
        self.tamanho = tamanho
        self.livros_cadastrados = []

    def verificar_sistema(self, titulo):
        for livro in self.livros_cadastrados:
            if livro["titulo"] == titulo: 
                return livro
        return True

    def cadastrar_livrodigital(self, titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, arq, isbn, url, tamanho):
        livro = {"titulo":titulo,    
                "autor": autor,
                "lançamento": lancamento,
                "editora": editora,
                "isbn": isbn,
                "paginas": paginas,
                "emprestimo": emprestimo,
                "estado": estado,
                "assunto": assunto,
                "url": url,
                "tamanho": tamanho}
        self.livros_cadastrados.append(livro)
        print('Livro cadastrado com sucesso!')
        return True 

    def remover_livrodigital(self,nome_livro):
        for livro in self.livros_cadastrados:
            if nome_livro is None:
                print("Livro inexistente")
                return False
            else:
                self.livros_cadastrados.remove(livro)
                print("Livro Removido")
                return True

    def atualizar_livrodigital(self, titulo):
        self.remover_livrodigital(titulo)
        titulo = input("titulo: ")
        autor = input("autor: ")
        editora = input("editora: ")
        lancamento = input("lançamento: ")
        paginas = input("paginas: ")
        isbn = input("isbn (Ex.:9783161484100): ")
        url = input("url: ")
        tamanho = input("tamanho: ")
        emprestimo = input("emprestimo: ")
        estado = input("estado: ")
        assunto = input("assunto: ")                     
        self.cadastrar_livrofisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto, isbn, url, tamanho)


    def buscar_autor(self, autor= str):
        for indice, autor2 in enumerate(self.livros_cadastrados):
            if autor2.get('autor') == autor:
                print('Livros Digitais: ', autor2)

    def imprimir_nome_livros(self):
        print("Livros Digital:")
        print(self.livros_cadastrados)

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
        self.livro_fisico = LivroFisico(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        self.livro_digital = LivroDigital(0,0,0,0,0,0,0,0,0,0,0,0)

    def imprimir_opcao(self):
        print("")
        print("1 - Livro físico")
        print("2 - livro digital")
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
                        titulo = input("titulo: ")
                        autor = input("autor: ")
                        editora = input("editora: ")
                        lancamento = input("lançamento: ")
                        paginas = input("paginas: ")
                        isbn = int(input("isbn(Ex.:9783161484100): "))
                        capa = input("tipo de capa: ")
                        localizacao = input("localização: ")
                        emprestimo = input("emprestimo: ")
                        estado = input("estado: ")
                        assunto = input("assunto: ")
                        if self.livro_fisico.verificar_sistema(titulo) == True:
                            if assunto.lower()== 'manuscrito':
                                aluno = input("aluno:")
                                professor =  input("professor:")
                                self.livro_fisico.cadastrar_livrofisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto,0, isbn, capa, localizacao, aluno, professor)                                  
                            else:
                                self.livro_fisico.cadastrar_livrofisico(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto,0, isbn,capa,localizacao, 0, 0) 
                        else:
                            print('Livro já cadastrado!')
                        break   

                    elif opcao == 2:
                        titulo = input("titulo: ")
                        autor = input("autor: ")
                        editora = input("editora: ")
                        lancamento = input("lançamento: ")
                        paginas = input("paginas: ")
                        isbn = int(input("isbn(Ex.:9783161484100): "))
                        url = input("url: ")
                        tamanho = input("tamanho:r")
                        localizacao = input("localização: ")
                        emprestimo = input("emprestimo: ")
                        estado = input("estado: ")
                        assunto = input("assunto: ")
                        if self.livro_fisico.verificar_sistema(titulo) == True:                      
                            self.livro_digital.cadastrar_livrodigital(titulo, autor, editora, lancamento,  paginas, emprestimo, estado, assunto,0, isbn, url, tamanho)
                        else:
                            print('Livro já cadastrado!')
                        break

            elif opcao == 2:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                print("")
                while opcao in [1, 2]:
                    if opcao == 1: 
                        titulo = input('Titulo que deseja remover: ')
                        self.livro_fisico.remover_livrofisico(titulo)
                        break
                    elif opcao == 2:
                        titulo = input('Titulo que deseja remover: ')
                        self.livro_digital.remover_livrodigital(titulo)
                        break
                
            elif opcao == 3:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                while opcao in [1, 2]:
                    if opcao == 1:
                        titulo = input("Titulo que deseja atualizar:")
                        self.livro_fisico.atualizar_livrofisico(titulo)
                        break
                    elif opcao == 2:    
                        titulo = input("Titulo que deseja atualizar:")
                        self.livro_digital.atualizar_livrodigital(titulo)
                        break

            elif opcao == 4:
                autor = input('Autor que deseja buscar: ')
                self.livro_fisico.buscar_autor(autor)
                self.livro_digital.buscar_autor(autor)
                    
            elif opcao == 5:
                self.livro_fisico.imprimir_nome_livros()
                self.livro_digital.imprimir_nome_livros()

            elif opcao == 6:
                arq1 = input('Digite o nome do arquivo para os livros fisicos: ')
                arq2 = input('Digite o nome do arquivo para os livros digitais: ')
                self.livro_digital.salvar_arquivo(arq2)
                self.livro_fisico.salvar_arquivo(arq1)
                exit()

            self.imprimir_comandos()
            opcao = int(input("Digite uma opção acima: "))


if __name__ == "__main__":
    g = Menu()
    g.main()
