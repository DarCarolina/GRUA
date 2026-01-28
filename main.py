import pygame
import sys

# Inicializar pygame
pygame.init()

# Ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de Grúa")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
AZUL = (0, 0, 200)

# Reloj
clock = pygame.time.Clock()

# Posición de la grúa
grua_x = 400
gancho_y = 150

# Carga
carga_x = grua_x
carga_y = gancho_y + 40
carga_sujeta = False

# Velocidades
velocidad = 5

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                carga_sujeta = not carga_sujeta

    teclas = pygame.key.get_pressed()

    # Movimiento horizontal
    if teclas[pygame.K_LEFT]:
        grua_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        grua_x += velocidad

    # Movimiento vertical del gancho
    if teclas[pygame.K_UP]:
        gancho_y -= velocidad
    if teclas[pygame.K_DOWN]:
        gancho_y += velocidad

    # Limitar movimientos
    grua_x = max(50, min(750, grua_x))
    gancho_y = max(100, min(400, gancho_y))

    # Si la carga está sujeta, sigue al gancho
    if carga_sujeta:
        carga_x = grua_x
        carga_y = gancho_y + 40

    # Dibujar
    pantalla.fill(BLANCO)

    # Estructura de la grúa
    pygame.draw.rect(pantalla, NEGRO, (grua_x - 50, 50, 100, 20))
    pygame.draw.line(pantalla, NEGRO, (grua_x, 70), (grua_x, gancho_y), 3)

    # Gancho
    pygame.draw.circle(pantalla, AZUL, (grua_x, gancho_y), 8)

    # Carga
    pygame.draw.rect(pantalla, ROJO, (carga_x - 15, carga_y, 30, 30))

    pygame.display.flip()
    clock.tick(60)