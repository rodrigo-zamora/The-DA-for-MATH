#Importar la librería Pygame
import pygame
import sys
import time
import os
import random
from pygame.locals import *

nombreJuego = "The DA for MATH"

#Tamaño de la ventana
screenWidth = 960
screenHeight = 700

#Posición inicial del avatar
posicionX = int(screenWidth/2)
posicionY = int(screenHeight/2)

#Definir colores en RGB
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0) 
lessred = (255, 75, 75)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 140, 0)

nivelesDesbloqueados = []

def ajustarVida():

    global vida1
    global vida1_rect
    global vida2
    global vida2_rect
    global vida3
    global vida3_rect
    global actualizarVida

    if puntos == 6:
        vida1 = pygame.image.load("imagenes/full.png")
        
        vida2 = pygame.image.load("imagenes/full.png")

        vida3 = pygame.image.load("imagenes/full.png")

    elif puntos == 5:
        vida1 = pygame.image.load("imagenes/half2.0.png")
        
        vida2 = pygame.image.load("imagenes/full.png")

        vida3 = pygame.image.load("imagenes/full.png")

    elif puntos == 4:
        vida1 = pygame.image.load("imagenes/empty.png")
        
        vida2 = pygame.image.load("imagenes/full.png")

        vida3 = pygame.image.load("imagenes/full.png")

    elif puntos == 3:
        vida1 = pygame.image.load("imagenes/empty.png")
        
        vida2 = pygame.image.load("imagenes/half2.0.png")

        vida3 = pygame.image.load("imagenes/full.png")

    elif puntos == 2:
        vida1 = pygame.image.load("imagenes/empty.png")
        
        vida2 = pygame.image.load("imagenes/empty.png")

        vida3 = pygame.image.load("imagenes/full.png")

    elif puntos == 1:
        vida1 = pygame.image.load("imagenes/empty.png")
        
        vida2 = pygame.image.load("imagenes/empty.png")

        vida3 = pygame.image.load("imagenes/half2.0.png")

    elif puntos == 0:
        vida1 = pygame.image.load("imagenes/empty.png")
        
        vida2 = pygame.image.load("imagenes/empty.png")

        vida3 = pygame.image.load("imagenes/empty.png")

    vida1 = pygame.transform.scale(vida1, (50,50))
    vida1_rect = vida1.get_rect()
    vida1_rect.center = (165, 45)
    vida2 = pygame.transform.scale(vida2, (50,50))
    vida2_rect = vida2.get_rect()
    vida2_rect.center = (105, 45)
    vida3 = pygame.transform.scale(vida3, (50,50))
    vida3_rect = vida3.get_rect()
    vida3_rect.center = (45, 45)

    actualizarVida = False

#Avatar, posición inicial, movimiento
class Avatar(pygame.sprite.Sprite):

    #Función para el avatar
    def __init__(self, x):

        #Función de pygame
        pygame.sprite.Sprite.__init__(self)

        if "4" in nivelesDesbloqueados:
            #Seleccionar el archivo del avatar
            self.image = loadImage("imagenes/nivel4.png", True)

        elif "3" in nivelesDesbloqueados:
            #Seleccionar el archivo del avatar
            self.image = loadImage("imagenes/nivel3.png", True)

        elif "2" in nivelesDesbloqueados:
            #Seleccionar el archivo del avatar
            self.image = loadImage("imagenes/nivel2.png", True)

        else:
            #Seleccionar el archivo del avatar
            self.image = loadImage("imagenes/aa2.png", True)

        #Función de pygame para mostrar el avatar
        self.rect = self.image.get_rect()
        #Definir la posición en X del avatar
        self.rect.centerx = posicionX
        #Definir la posición en Y del avatar
        self.rect.centery = posicionY
        #Definir la velocidad del avatar
        self.speed = 0.25

    #Función para mover el avatar
    def mover(self, time, keys):

        #Hacer la variable global
        global esperandoRespuesta
        #Hacer la variable global para ser usada en otras funciones
        global nivel
        #Hacer la variable global para ser usada en otras funciones
        global puntos
        #Hacer la variable global para ser usada en otras funciones
        global multiplicadorPuntos
        #Hacer la variable global para ser usada en otras funciones
        global tiempoContestar
        #Hacer la variable global para ser usada en otras funciones
        global gameRunning
        #Crear una nueva variable con el valor del rectángulo
        avatarRecangulo = self.rect

        #Si el rectángulo del avatar colisiona con el rectángulo de la posible respuesta 1
        if avatarRecangulo.colliderect(posiblesRespuesta_1_rect):
            #Sacar de la lista de posibles respuestas el primer valor, y ver si es el mismo a la respuesta correcta
            if posiblesRespuestas[0] == respuestaCorrecta:
                self.rect.centerx = posicionX
                self.rect.centery = posicionY
                esperandoRespuesta = False
                nivel += 1
                pygame.mixer.Channel(0).set_volume(0.3)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sonidos/correct.wav'))
            
            else:
                if puntos == 0:
                    gameRunning = False
                    gameLost()

                else:
                    puntos = puntos - 1
                    self.rect.centerx = posicionX
                    self.rect.centery = posicionY   
                    pygame.mixer.Channel(1).set_volume(0.3)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('sonidos/wrong.wav')) 
                    ajustarVida()           

        if avatarRecangulo.colliderect(posiblesRespuesta_2_rect):
            if posiblesRespuestas[1] == respuestaCorrecta:
                self.rect.centerx = posicionX
                self.rect.centery = posicionY
                esperandoRespuesta = False
                nivel += 1
                pygame.mixer.Channel(0).set_volume(0.3)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sonidos/correct.wav'))
            
            else:
                if puntos == 0:
                    gameRunning = False
                    gameLost()

                else:         
                    puntos = puntos - 1
                    self.rect.centerx = posicionX
                    self.rect.centery = posicionY   
                    pygame.mixer.Channel(1).set_volume(0.3)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('sonidos/wrong.wav'))   
                    ajustarVida()    

        if avatarRecangulo.colliderect(posiblesRespuesta_3_rect):
            if posiblesRespuestas[2] == respuestaCorrecta:
                self.rect.centerx = posicionX
                self.rect.centery = posicionY
                esperandoRespuesta = False
                nivel += 1
                pygame.mixer.Channel(0).set_volume(0.3)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sonidos/correct.wav'))
            
            else:
                if puntos == 0:
                    gameRunning = False
                    gameLost()

                else:
                    puntos = puntos - 1
                    self.rect.centerx = posicionX
                    self.rect.centery = posicionY   
                    pygame.mixer.Channel(1).set_volume(0.3)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('sonidos/wrong.wav')) 
                    ajustarVida()    

        if avatarRecangulo.colliderect(posiblesRespuesta_4_rect):
            if posiblesRespuestas[3] == respuestaCorrecta:
                self.rect.centerx = posicionX
                self.rect.centery = posicionY
                esperandoRespuesta = False
                nivel += 1
                pygame.mixer.Channel(0).set_volume(0.3)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sonidos/correct.wav'))
            
            else:
                if puntos == 0:
                    gameRunning = False
                    gameLost()

                else:
                    puntos = puntos - 1
                    self.rect.centerx = posicionX
                    self.rect.centery = posicionY  
                    pygame.mixer.Channel(1).set_volume(0.3)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('sonidos/wrong.wav'))  
                    ajustarVida()    

        if avatarRecangulo.colliderect(posiblesRespuesta_5_rect):
            if posiblesRespuestas[4] == respuestaCorrecta:
                self.rect.centerx = posicionX
                self.rect.centery = posicionY
                esperandoRespuesta = False
                nivel += 1
                pygame.mixer.Channel(0).set_volume(0.3)   
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sonidos/correct.wav'))
            
            else:
                if puntos == 0:
                    gameRunning = False
                    gameLost()

                else:
                    puntos = puntos - 1
                    self.rect.centerx = posicionX
                    self.rect.centery = posicionY  
                    pygame.mixer.Channel(1).set_volume(0.3)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('sonidos/wrong.wav')) 
                    ajustarVida()       

        #Si la posición del avatar en la parte superior del mismo es mayor o igual a 0
        if self.rect.top >= 0:
            #Si la tecla presionada es [Arriba]
            if keys[K_UP]:
                #Mover el avatar, mediante el algoritmo = (posición actual en y - (velocidad del avatar * tiempo))
                self.rect.centery = int(self.rect.centery - (self.speed * time))

        #Si la posición del avatar en la parte izquierda del mismo es mayor o igual a 0
        if self.rect.left >= 0:
            #Si la tecla presionada es [Izquierda]
            if keys[K_LEFT]:
                #Mover el avatar, mediante el algoritmo = (posición actual en x - (velocidad del avatar * tiempo))
                self.rect.centerx = int(self.rect.centerx - (self.speed * time))

        #Si la posición del avatar en la parte inferior del mismo es menor o igual a la altura de la pantalla
        if self.rect.bottom <= screenHeight:
            #Si la tecla presionada es [Abajo]
            if keys[K_DOWN]:
                #Mover el avatar, mediante el algoritmo = (posición actual en y + (velocidad del avatar * tiempo))
                self.rect.centery = int(self.rect.centery + (self.speed * time))

        #Si la posición del avatar en la parte derecha del mismo es menor o igual a la anchura de la pantalla
        if self.rect.right <= screenWidth:    
            #Si la tecla presionada es [Derecha]
            if keys[K_RIGHT]:
                #Mover el avatar, mediante el algoritmo = (posición actual en x + (velocidad del avatar * tiempo))
                self.rect.centerx = int(self.rect.centerx + (self.speed * time))

def ganarJuego():
    print("yei")

#Función para cargar imágenes al juego
def loadImage(filename, transparent=False):
    image = pygame.image.load(filename) 
    image = image.convert() 
    if transparent: 
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
        image = pygame.transform.scale(image, (60,95))
        return image

def gameLost():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('sonidos/death.wav'))
    global nivel
    global puntos
    gameLost = True
    textoLost = font.render("¡Has perdido!", True, white)
    textoLost_rect = textoLost.get_rect()
    textoLost_rect.center = (int(screenWidth/2), 400)
    screen.blit(textoLost, textoLost_rect)
    texto_puntajeTotal = font.render(f"Nivel alcanzado: {nivel}", True, white)
    texto_puntajeTotal_rect = texto_puntajeTotal.get_rect()
    texto_puntajeTotal_rect.center = (int(screenWidth/2), 350)
    screen.blit(texto_puntajeTotal, texto_puntajeTotal_rect)
    texto_puntajeTotala = font.render("¿Quieres volver a jugar?", True, white)
    texto_puntajeTotala_rect = texto_puntajeTotala.get_rect()
    texto_puntajeTotala_rect.center = (int(screenWidth/2), 450)
    screen.blit(texto_puntajeTotala, texto_puntajeTotala_rect)
    texto_si = font.render("  Si  ", True, white, green)
    texto_si_rect = texto_si.get_rect()
    texto_si_rect.center = (int(screenWidth/2)-50, 550)
    screen.blit(texto_si, texto_si_rect)
    texto_no = font.render("  No  ", True, white, red)
    texto_no_rect = texto_no.get_rect()
    texto_no_rect.center = (int(screenWidth/2)+50, 550)
    screen.blit(texto_no, texto_no_rect)
    displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
    lostImage = pygame.image.load("imagenes/Fondos/Planetas.png")
    screen.blit(lostImage, (0, 0))
    displaySurface.blit(textoLost, textoLost_rect)
    displaySurface.blit(texto_puntajeTotal, texto_puntajeTotal_rect)
    displaySurface.blit(texto_puntajeTotala, texto_puntajeTotala_rect)
    displaySurface.blit(texto_si, texto_si_rect)
    displaySurface.blit(texto_no, texto_no_rect)

    while gameLost == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if texto_no_rect.collidepoint(event.pos):
                    sys.exit()
                    pygame.quit()

                elif texto_si_rect.collidepoint(event.pos):
                    gameLost = False
                    pygame.display.update()
                    nivel = 1
                    puntos = 6
                    operadores = ["+"]
                    nivelesDesbloqueados = []
                    main()
                    
        pygame.display.update()    

def planets():
    global planets
    clock = pygame.time.Clock()

    planets = True

    empezar = pygame.image.load("imagenes/Empezar.png")
    empezar_rect = empezar.get_rect()
    empezar_rect.center = (180, 400)

    creditos = pygame.image.load("imagenes/Creditos.png")
    creditos_rect = creditos.get_rect()
    creditos_rect.center = (179, 550)

    back = pygame.image.load("imagenes/Fondos/Planetas.png")
    surface = pygame.display.set_mode((screenWidth, screenHeight))

    screen.blit(back, (0, 0))
    surface.blit(empezar, empezar_rect)
    surface.blit(creditos, creditos_rect)

    who_we_are = False

    while planets == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if empezar_rect.collidepoint(event.pos):
                    planets = False
                    pygame.display.update()
                    gameMenu()
                if creditos_rect.collidepoint(event.pos):
                    who_we_are = True
                if salir_who_rect.collidepoint(event.pos):
                    who_we_are = False
        if who_we_are != False:
            who = pygame.image.load("imagenes/Fondos/Créditos.png")
            who = pygame.transform.scale(who, (960,700))
            salir_who_rect.center = (50, 40)
            screen.blit(who, (0, 0))
            screen.blit(salir_who, salir_who_rect)
        pygame.display.update()
'''
    while gameRunning == True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
            if eventos.type == pygame.MOUSEBUTTONUP:
                if pista_rect.collidepoint(eventos.pos):
                    gameHelp = True

                if salir_rect.collidepoint(eventos.pos):
                    gameHelp = False
        
        if gameHelp != False:
            helpImage = pygame.image.load("imagenes/Fondos/how2play.png")
            helpImage = pygame.transform.scale(helpImage, (960,700))
            salir_rect.center = (50, 50)
            screen.blit(helpImage, (0, 0))
            screen.blit(salir, salir_rect)
'''

#Función para mostrar el botón de empezar
def gameMenu():

    #Poner la flag gameMenu en True
    gameMenu = True
    nivelSuma = font64.render("Nivel 1", True, white, green)
    nivelSuma_rect = nivelSuma.get_rect()
    nivelSuma_rect.center = (150, 400)
    avatarNivel1 = pygame.image.load("imagenes/aa2.png")
    avatarNivel1 = pygame.transform.scale(avatarNivel1, (70,125))
    avatarNivel1_rect = avatarNivel1.get_rect()
    avatarNivel1_rect.center = (140, 550)

    if "2" in nivelesDesbloqueados:
        nivelResta = font64.render("Nivel 2", True, white, green)

    else:
        nivelResta = font64.render("Nivel 2", True, white, red)

    nivelResta_rect = nivelResta.get_rect()
    nivelResta_rect.center = (365, 400)
    avatarNivel2 = pygame.image.load("imagenes/nivel2.png")
    avatarNivel2 = pygame.transform.scale(avatarNivel2, (86,100))
    avatarNivel2_rect = avatarNivel2.get_rect()
    avatarNivel2_rect.center = (362, 550)

    if "3" in nivelesDesbloqueados:
        nivelMultiplicacion = font64.render("Nivel 3", True, white, green)

    else:
        nivelMultiplicacion = font64.render("Nivel 3", True, white, red)

    nivelMultiplicacion_rect = nivelMultiplicacion.get_rect()
    nivelMultiplicacion_rect.center = (580, 400)
    avatarNivel3 = pygame.image.load("imagenes/nivel3.png")
    avatarNivel3 = pygame.transform.scale(avatarNivel3, (157,85))
    avatarNivel3_rect = avatarNivel3.get_rect()
    avatarNivel3_rect.center = (580, 550)

    if "4" in nivelesDesbloqueados:
        nivelDivision = font64.render("Nivel 4", True, white, green)

    else:
        nivelDivision = font64.render("Nivel 4", True, white, red)

    nivelDivision_rect = nivelDivision.get_rect()
    nivelDivision_rect.center = (795, 400)
    avatarNivel4 = pygame.image.load("imagenes/nivel4.png")
    avatarNivel4 = pygame.transform.scale(avatarNivel4, (121,90))
    avatarNivel4_rect = avatarNivel4.get_rect()
    avatarNivel4_rect.center = (795, 550)

    text = font.render("  Selecciona el nivel que deseas jugar  ", True, yellow)
    text_rect = text.get_rect()
    text_rect.center = (int(screenWidth/2), 650)
    mainImage = pygame.image.load("imagenes/Fondos/Planetas.png")
    displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
    screen.blit(mainImage, (0, 0))
    displaySurface.blit(text, text_rect)
    displaySurface.blit(nivelSuma, nivelSuma_rect)
    displaySurface.blit(nivelResta, nivelResta_rect)
    displaySurface.blit(nivelMultiplicacion, nivelMultiplicacion_rect)
    displaySurface.blit(nivelDivision, nivelDivision_rect)
    displaySurface.blit(avatarNivel1, avatarNivel1_rect)
    displaySurface.blit(avatarNivel2, avatarNivel2_rect)
    displaySurface.blit(avatarNivel3, avatarNivel3_rect)
    displaySurface.blit(avatarNivel4, avatarNivel4_rect)

    #Mientras la flag gameMenu sea verdadera
    while gameMenu == True:
        #Obtener el evento pygame
        for event in pygame.event.get():
            #Si el evento es presionar la tecla de escape
            if event.type == pygame.QUIT:
                #Salir del programa
                sys.exit()

            #Función para el evento de hacer click con el mouse
            if event.type == pygame.MOUSEBUTTONUP:
                if nivelSuma_rect.collidepoint(event.pos):
                    #Cierra el menú y muestra el juego main()
                    gameMenu = False
                    #Actualizar la pantalla con una función de pygame
                    pygame.display.update()
                    #Ir a la función principal del juego
                    main()

                elif nivelResta_rect.collidepoint(event.pos):
                    if "2" in nivelesDesbloqueados:
                        gameMenu = False
                        pygame.display.update()
                        operadores.append("-")
                        main()

                elif nivelMultiplicacion_rect.collidepoint(event.pos):
                    if "3" in nivelesDesbloqueados:
                        gameMenu = False
                        pygame.display.update()
                        operadores.append("*")
                        main()

                elif nivelDivision_rect.collidepoint(event.pos):
                    if "4" in nivelesDesbloqueados:
                        gameMenu = False
                        pygame.display.update()
                        operadores.append("/")
                        main()

        #Actualizar la pantalla
        pygame.display.update()

#Función para mostrar ventana del juego
def main():

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption(nombreJuego)
    background_image = pygame.image.load("imagenes/Fondos/mapa2.png")
    background_image = pygame.transform.scale(background_image, (960,700))
    avatar = Avatar(30)
    clock = pygame.time.Clock()
    global esperandoRespuesta
    global posiblesRespuestas
    global respuestaCorrecta
    global operador
    global puntos
    global gameRunning
    global nivel
    global actualizarVida

    esperandoRespuesta = False
    gameRunning = True
    gameHelp = False
    actualizarVida = True

    while gameRunning == True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

            if eventos.type == pygame.MOUSEBUTTONUP:
                if pista_rect.collidepoint(eventos.pos):
                    gameHelp = True

                if salir_rect.collidepoint(eventos.pos):
                    gameHelp = False
        
        if gameHelp != False:
            helpImage = pygame.image.load("imagenes/Fondos/how2play.png")
            helpImage = pygame.transform.scale(helpImage, (960,700))
            salir_rect.center = (50, 40)
            screen.blit(helpImage, (0, 0))
            screen.blit(salir, salir_rect)

        else:
            if nivel == 25:
                nivel = 1

                if ("+" and "-" and "*" and "/") in operadores:
                    ganarJuego()
                    gameRunning = False
                
                elif ("+" and "-" and "*") in operadores:
                    gameRunning = False
                    operadores.append("/")
                    nivelesDesbloqueados.append("4")
                    gameMenu()
                
                elif ("+" and "-") in operadores:
                    gameRunning = False
                    operadores.append("*")
                    nivelesDesbloqueados.append("3")
                    gameMenu()
                
                elif "+" in operadores:
                    gameRunning = False
                    operadores.append("-")
                    nivelesDesbloqueados.append("2")
                    gameMenu()

            #Mostrar en la pantalla en la posición 0,0 la imagen
            screen.blit(background_image, (0, 0))
            #Mostrar en la pantalla en la posición del avatar definida la imagen
            screen.blit(avatar.image, avatar.rect)
            avatar.mover(time, keys)

            #               #
            #   PROBLEMAS   #
            #               #
            if actualizarVida == True:
                ajustarVida()
                actualizarVida = False
            #Saber si hay un problema definido o no
            if esperandoRespuesta == False:
                #Cambiar la flag a verdadero
                esperandoRespuesta = True
                #Escoger un operador aleatorio de la lista operadores
                operador = random.choice(operadores)
                #Obtener un valor aleatorio entre 0 y 100
                valor1 = random.randint(0, (nivel*4))
                #Obtener un valor aleatorio entre 0 y 100
                valor2 = random.randint(1, (nivel*4))
                #Valor aleatorio 1 y 2, usado para la respuesta incorrecta 1
                aleatorio_1, aleatorio_2 = random.randint(0, 5), random.randint(1, 5)
                #Valor aleatorio 3 y 4, usado para las respuesta incorrecta 2
                aleatorio_3, aleatorio_4 = random.randint(0, 5), random.randint(1, 5)
                #Valor aleatorio 5 y 6, usado para las respuesta incorrecta 3
                aleatorio_5, aleatorio_6= random.randint(0, 5), random.randint(1, 5)
                #Valor aleatorio 7 y 8, usado para las respuesta incorrecta 4
                aleatorio_7, aleatorio_8 = random.randint(0, 5), random.randint(1, 5)
                #Concatenar los valores para obtener el problema
                problema = str(valor1) + operador + str(valor2)
                #Evaluar el problema que está en string y redondearlo
                respuestaCorrecta = round(eval(problema), 3)
                #Crear la respuesta incorrecta 1
                respuestaIncorrecta_1 = round(eval(str(valor1+aleatorio_1) + operador + str(valor2-aleatorio_2)), 3)
                #Crear la respuesta incorrecta 2
                respuestaIncorrecta_2 = round(eval(str(valor1+aleatorio_3) + operador + str(valor2-aleatorio_4)), 3) 
                #Crear la respuesta incorrecta 3
                respuestaIncorrecta_3 = round(eval(str(valor1+aleatorio_5) + operador + str(valor2-aleatorio_6)), 3) 
                #Crear la respuesta incorrecta 4
                respuestaIncorrecta_4 = round(eval(str(valor1+aleatorio_7) + operador + str(valor2-aleatorio_8)), 3) 

                #While para evitar que la respuesta incorrecta sea igual a la correcta, empezando el sistema de nuevo
                while respuestaIncorrecta_1 == respuestaCorrecta or respuestaIncorrecta_1 == respuestaIncorrecta_2 or respuestaIncorrecta_1 == respuestaIncorrecta_3 or respuestaIncorrecta_1 == respuestaIncorrecta_4:
                    #Valor aleatorio 1, usado para las respuestas incorrectas
                    aleatorio_1 = random.randint(0, 5)
                    #Valor aleatorio 2, usado para las respuestas incorrectas
                    aleatorio_2 = random.randint(1, 5)
                    #Crear la respuesta incorrecta 1
                    respuestaIncorrecta_1 = round(eval(str(valor1+aleatorio_1) + operador + str(valor2-aleatorio_2)), 3)
                
                #While para evitar que la respuesta incorrecta sea igual a la correcta, empezando el sistema de nuevo
                while respuestaIncorrecta_2 == respuestaCorrecta or respuestaIncorrecta_2 == respuestaIncorrecta_1 or respuestaIncorrecta_2 == respuestaIncorrecta_3 or respuestaIncorrecta_2 == respuestaIncorrecta_4:
                    #Valor aleatorio 3, usado para las respuestas incorrectas
                    aleatorio_3 = random.randint(0, 5)
                    #Valor aleatorio 4, usado para las respuestas incorrectas
                    aleatorio_4 = random.randint(1, 5)
                    #Crear la respuesta incorrecta 2
                    respuestaIncorrecta_2 = round(eval(str(valor1+aleatorio_3) + operador + str(valor2-aleatorio_4)), 3)
                
                #While para evitar que la respuesta incorrecta sea igual a la correcta, empezando el sistema de nuevo
                while respuestaIncorrecta_3 == respuestaCorrecta or respuestaIncorrecta_3 == respuestaIncorrecta_1 or respuestaIncorrecta_3 == respuestaIncorrecta_2 or respuestaIncorrecta_3 == respuestaIncorrecta_4:
                    #Valor aleatorio 3, usado para las respuestas incorrectas
                    aleatorio_5 = random.randint(0, 5)
                    #Valor aleatorio 4, usado para las respuestas incorrectas
                    aleatorio_6 = random.randint(1, 5)
                    #Crear la respuesta incorrecta 2
                    respuestaIncorrecta_3 = round(eval(str(valor1+aleatorio_5) + operador + str(valor2-aleatorio_6)), 3)
                
                #While para evitar que la respuesta incorrecta sea igual a la correcta, empezando el sistema de nuevo
                while respuestaIncorrecta_4 == respuestaCorrecta or respuestaIncorrecta_4 == respuestaIncorrecta_1 or respuestaIncorrecta_4 == respuestaIncorrecta_2 or respuestaIncorrecta_4 == respuestaIncorrecta_3:
                    #Valor aleatorio 3, usado para las respuestas incorrectas
                    aleatorio_7 = random.randint(0, 5)
                    #Valor aleatorio 4, usado para las respuestas incorrectas
                    aleatorio_8 = random.randint(1, 5)
                    #Crear la respuesta incorrecta 2
                    respuestaIncorrecta_4 = round(eval(str(valor1+aleatorio_7) + operador + str(valor2-aleatorio_8)), 3)

                #Crear una lista con las posibles respuestas, para ser acomodadas aleatoriamente
                posiblesRespuestas = [respuestaCorrecta, respuestaIncorrecta_1, respuestaIncorrecta_2, respuestaIncorrecta_3, respuestaIncorrecta_4]
                #Poner en orden aleatorio la lista 5 veces, para evitar que la respuesta esté en la misma posición
                for i in range(5):
                    random.shuffle(posiblesRespuestas)

            #Crear el texto para el nivel, escogiendo los colores
            textoNivel = font.render(f"Problema {nivel} de 25", True, black)
            #Crear el regtángulo que contendrá el texto
            textoNivel_rect = textoNivel.get_rect()
            #Darle una posición al rectángulo
            textoNivel_rect.center = (int(screenWidth/2), 115)
            #Mostrar el texto y su rectángulo
            screen.blit(textoNivel, textoNivel_rect)
            #Crear el texto para el problema, escogiendo los colores
            textoProblema = font.render(f"{problema}", True, black)
            #Crear el rectángulo que contendrá el texto
            textoProblema_rect = textoProblema.get_rect()
            #Darle una posición al rectángulo
            textoProblema_rect.center = (int(screenWidth/2), 165)
            #Mostrar el texto y su rectángulo
            screen.blit(textoProblema, textoProblema_rect)

            #                                           #
            #   GENERAR IMÁGENES CON LAS RESPUESTAS     #
            #                                           #

            #Crear variables de cada respuesta
            posiblesRespuesta_1 = posiblesRespuestas[0]
            posiblesRespuesta_2 = posiblesRespuestas[1]
            posiblesRespuesta_3 = posiblesRespuestas[2]
            posiblesRespuesta_4 = posiblesRespuestas[3]
            posiblesRespuesta_5 = posiblesRespuestas[4]
            #Asignar el texto a cada variable, con letra blanco y sin fondo
            posiblesRespuesta_1 = font.render(f"{posiblesRespuesta_1}", True, white)
            posiblesRespuesta_2 = font.render(f"{posiblesRespuesta_2}", True, white)
            posiblesRespuesta_3 = font.render(f"{posiblesRespuesta_3}", True, white)
            posiblesRespuesta_4 = font.render(f"{posiblesRespuesta_4}", True, white)
            posiblesRespuesta_5 = font.render(f"{posiblesRespuesta_5}", True, white)
            #Generar un rectángulo de acuerdo a la letra
            posiblesRespuesta_1_rect = posiblesRespuesta_1.get_rect()
            posiblesRespuesta_2_rect = posiblesRespuesta_2.get_rect()
            posiblesRespuesta_3_rect = posiblesRespuesta_3.get_rect()
            posiblesRespuesta_4_rect = posiblesRespuesta_4.get_rect()
            posiblesRespuesta_5_rect = posiblesRespuesta_5.get_rect()
            #Posición de la primera respuesta
            contadorPosicion = 160
            #Posición de la primera respuesta y distancia con la siguiente respuesta
            posiblesRespuesta_1_rect.center = (contadorPosicion, 605)
            contadorPosicion += 170
            #Posición de la segunda respuesta y distancia con la siguiente respuesta
            posiblesRespuesta_2_rect.center = (contadorPosicion, 605)
            contadorPosicion += 142
            #Posición de la tercera respuesta y distancia con la siguiente respuesta
            posiblesRespuesta_3_rect.center = (contadorPosicion+40, 605)
            contadorPosicion += 142
            #Posición de la cuarta respuesta y distancia con la siguiente respuesta
            posiblesRespuesta_4_rect.center = (contadorPosicion+60, 605)
            contadorPosicion += 142
            #Posición de la quinta respuesta y distancia con la siguiente respuesta
            posiblesRespuesta_5_rect.center = (contadorPosicion+90, 605)
            pista_rect.center = (900, 50)

            


            #Mostrar todas las respuestas
            screen.blit(posiblesRespuesta_1, posiblesRespuesta_1_rect)
            screen.blit(posiblesRespuesta_2, posiblesRespuesta_2_rect)
            screen.blit(posiblesRespuesta_3, posiblesRespuesta_3_rect)
            screen.blit(posiblesRespuesta_4, posiblesRespuesta_4_rect)
            screen.blit(posiblesRespuesta_5, posiblesRespuesta_5_rect)
            screen.blit(pista, pista_rect)

            screen.blit(vida1, vida1_rect)
            screen.blit(vida2, vida2_rect)
            screen.blit(vida3, vida3_rect)

        #Actualizar la pantalla
        pygame.display.update()

    return 0

#Iniciar el módulo de pygame
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

#SONIDO DE FONDO
pygame.mixer.music.load(os.path.join(os.getcwd(), 'sonidos', 'Songs' , 'fondo_todo.mp3'))
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

#Mostrar el nivel donde está el jugador
nivel = 1
puntos = 6
#Lista con las posibles operaciones
operadores = ["+"]
#Tipo de letra a usar y tamaño de la misma
font = pygame.font.Font('freesansbold.ttf', 32)
font16 = pygame.font.Font('freesansbold.ttf', 16)
font64 = pygame.font.Font('freesansbold.ttf', 50)
textoPrueba = font.render("123", True, white)
posiblesRespuesta_1_rect = textoPrueba.get_rect()
posiblesRespuesta_1_rect.center = (160, 605) 
posiblesRespuesta_2_rect = textoPrueba.get_rect()
posiblesRespuesta_2_rect.center = (330, 605) 
posiblesRespuesta_3_rect = textoPrueba.get_rect()
posiblesRespuesta_3_rect.center = (500, 605) 
posiblesRespuesta_4_rect = textoPrueba.get_rect()
posiblesRespuesta_4_rect.center = (670, 605) 
posiblesRespuesta_5_rect = textoPrueba.get_rect()
posiblesRespuesta_5_rect.center = (840, 605)

salir = font64.render("[x]", True, lessred)
salir_rect = salir.get_rect()

salir_who = font64.render("[x]", True, lessred)
salir_who_rect = salir_who.get_rect()

pista = font64.render("?", True, yellow)
pista_rect = pista.get_rect()

gameRunning = False
actualizarVida = True
#Crear una pantalla
screen = pygame.display.set_mode((screenWidth, screenHeight), 0 , 32)
#Nombre de la pantalla
pygame.display.set_caption(nombreJuego)
#Iniciar el menú del juego
planets()