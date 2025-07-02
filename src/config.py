import json
basic_data = {
    "puestos": {

    },
    "colores": {
        "tablero": ((100,200,100),(50,100,50)),
        "serpiente": (255,0,0),
        "manzana": (0,0,255),
        "fondo": (50,100,50),
        "contorno": (0,0,0),
        "titulo_lista": [(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(76,40,130)]
    },
    "juego": {
    }
}
class player_config():
    def __init__(self):
        self.configuracion = "serpiente/src/datos.json"
        try:
            with open(self.configuracion,"r") as data:
                self.datos = json.load(data)
                print(self.datos)
                self.creacion_variables()
        except:
            self.escritura(basic_data)
            player_config()
    def escritura(self,datos):
        with open(self.configuracion,"w") as data:
            json.dump(datos,data,indent=4)
    def creacion_variables(self):
        self.color_serpiente = self.datos["colores"]["serpiente"]
        self.color_manzana = self.datos["colores"]["manzana"]
        self.color_tablero = self.datos["colores"]["tablero"]
        self.color_fondo = self.datos["colores"]["fondo"]
        self.color_contorno = self.datos["colores"]["contorno"]
        self.color_lista_titulo = self.datos["colores"]["titulo_lista"]
