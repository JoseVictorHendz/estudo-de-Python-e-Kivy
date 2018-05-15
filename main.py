
import kivy  # importa a biblioteca Kivy

kivy.require('1.10.0')  # esta é  a versão kivy atual (2017/09)

from kivy.app import App  # importação de classes necessárias ao programa
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.uix.filechooser import FileSystemLocal
from kivy.uix.boxlayout import BoxLayout


class MusicPlayer(BoxLayout):  # classe principal do programa

    def __init__(self, **kwargs):  # ao iniciar procura pelos arquivos MP3
        super(MusicPlayer, self).__init__(**kwargs)  # disponíveis no mesmo diretório do programa

        file_system = FileSystemLocal()

        self.listaMusicas = []  # cria uma lista para inserir os nomes dos arquivos

        for arquivoMusica in file_system.listdir('./'):  # preenche a lista com todos os nomes de arquivos que contenham
            if '.mp3' in arquivoMusica:  # mp3 no nome
                self.listaMusicas.append(arquivoMusica)

        self.indexMusicaAtual = 0  # inicia tocando o arquivo de index 0 na lista

    def pararMusica(self):  # para a musica através do método stop()
        self.musica.stop()

    def tocarProxima(self):
        self.musica = SoundLoader.load('bemVindo.mp3')  # cria um objeto tocador de musica
        # o nome do arquivo a ser tocado é dado pelo nome
        # disponível na lista de nomes, preenchida na inicialização do programa

        self.musica.play()  # toca a música
        self.indexMusicaAtual = self.indexMusicaAtual + 1  # atualiza o índice para a próxima música
        # ou retorna à primeira
        if self.indexMusicaAtual == len(self.listaMusicas):
            self.indexMusicaAtual = 0


class MusicApp(App):  # a aplicação mp3Music instancia um objeto MusicPlayer logo na inicialização
    def build(self):
        return MusicPlayer()


if __name__ == "__main__":  # cria e executa uma aplicação denominada mp3Music
    MusicApp().run()