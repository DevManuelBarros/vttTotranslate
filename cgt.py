import bs4
import urllib.parse
import urllib.request
class cgt:


    def __init__(self, leng_ori="", leng_dest=""):
       #seteamos los valores de idioma de entrada y de salida,
       #por defecto sera de ingles a español

       #empezamos por idioma de origen
        if(leng_ori != "") :
            self.idioma_origen = leng_ori
        else:
            self.idioma_origen = 'en'

       #vamos a setear idioma resultado, por defecto español
        if(leng_dest != "") :
           self.idioma_destino = leng_dest
        else:
            self.idioma_destino = 'es'

        #comenzamos con los seteos por defecto


    def idioma_origen(self, leng_ori=""):
        if (leng_ori != ""): self.idioma_origen = leng_ori

    def idioma_destino(self, leng_dest=""):
        if (leng_dest != ""): self.idioma_destino = leng_dest

    def obtener_traduccion(self, texto=""):
        if(texto == "") : texto = "Hello World"

        URL = "https://translate.google.com/"
        http_headers = """\
                    Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/37.0.2049.0 Safari/537.36"""


        data = {'sl': self.idioma_origen, 'tl': self.idioma_destino, 'text': texto}

        querystring = urllib.parse.urlencode(data)

        request = urllib.request.Request(URL + '?' + querystring)

        opener = urllib.request.build_opener()

        request.add_header("User-Agent", http_headers)

        resultadoHtml = opener.open(request).read()
        html = bs4.BeautifulSoup(resultadoHtml, "html.parser")
        return html.find('span', id="result_box").getText()