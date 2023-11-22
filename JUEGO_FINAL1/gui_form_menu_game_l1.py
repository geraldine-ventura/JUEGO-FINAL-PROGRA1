import pygame
from pygame.locals import *
from constantes import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet  # Asegúrate de que la ruta del módulo sea correcta


class FormGameLevel1:
    def __init__(
        self,
        w,
        h,
    ):
        # Inicializa el atributo surface
        self.surface = pygame.Surface((w, h))
        # --- GAME ELEMNTS ---
        self.static_background = Background(
            x=0,
            y=0,
            width=w,
            height=h,
            # path="Z_CLASE_23_inicio_NO_TOUCH copy/images/back/game-platform-cartoon-forest-landscape-2d-ui-design-computer-mobile-bright-wood-with-green-trees-grass-lianas-background-with-arcade-elements-jumping-bonus-items-nature-locations_107791-4657 (1).jpg",
            path="JUEGO_FINAL1/images/back/depositphotos_56565763-stock-illustration-seamless-background-fabulous-night-forest (1).jpg",
        )

        self.player = Player(
            x=0,
            y=400,
            speed_walk=6,
            speed_run=12,
            gravity=14,
            jump_power=30,
            frame_rate_ms=100,
            move_rate_ms=50,
            jump_height=140,
            p_scale=0.2,
            interval_time_jump=300,
        )

        self.enemy_list = []
        self.enemy_list.append(
            Enemy(
                x=450,
                y=400,
                speed_walk=6,
                speed_run=5,
                gravity=14,
                jump_power=30,
                frame_rate_ms=150,
                move_rate_ms=50,
                jump_height=140,
                p_scale=0.08,
                interval_time_jump=300,
            )
        )
        self.enemy_list.append(
            Enemy(
                x=900,
                y=400,
                speed_walk=6,
                speed_run=5,
                gravity=14,
                jump_power=30,
                frame_rate_ms=150,
                move_rate_ms=50,
                jump_height=140,
                p_scale=0.08,
                interval_time_jump=300,
            )
        )

        self.plataform_list = []
        self.plataform_list.append(Plataform(x=50, y=600, width=50, height=50, type=0))
        self.plataform_list.append(Plataform(x=400, y=500, width=50, height=50, type=1))
        self.plataform_list.append(Plataform(x=450, y=500, width=50, height=50, type=2))
        self.plataform_list.append(Plataform(x=500, y=500, width=50, height=50, type=3))
        self.plataform_list.append(
            Plataform(x=600, y=430, width=50, height=50, type=12)
        )
        self.plataform_list.append(
            Plataform(x=650, y=430, width=50, height=50, type=14)
        )
        self.plataform_list.append(
            Plataform(x=750, y=360, width=50, height=50, type=12)
        )
        self.plataform_list.append(
            Plataform(x=800, y=360, width=50, height=50, type=13)
        )
        self.plataform_list.append(
            Plataform(x=850, y=360, width=50, height=50, type=13)
        )
        self.plataform_list.append(
            Plataform(x=900, y=360, width=50, height=50, type=14)
        )

        # self.bullet_list = []
        self.player_bullet_list = []
        self.enemy_bullet_list = []

    def update(self, keys, delta_ms):
        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms, self.plataform_list)

            # Obtén las coordenadas a las que el enemigo apunta (esto puede variar según tu lógica)
            print("Player position:", self.player.rect.x, self.player.rect.y)

            target_x, target_y = self.player.rect.x, self.player.rect.y

            # Dispara una bala de enemigo
            enemy_bullet = Bullet(
                owner=enemy_element,
                x_init=enemy_element.rect.x,
                y_init=enemy_element.rect.y,
                x_end=target_x,
                y_end=target_y,
                speed=12,
                path="JUEGO_FINAL1/images/gui/hi_overlays/hi_overlay_variant_pigs2x_hi_png_1354840459.png",
                frame_rate_ms=5000,
                move_rate_ms=60,
            )

            # Agrega la bala a la lista de balas de enemigos
            enemy_element.bullet_list.append(enemy_bullet)

        # Resto de tu código de actualización...

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms, self.plataform_list)

        # Resto de tu código de actualización...

    def draw(self, screen):
        self.surface.fill(
            (0, 0, 0)
        )  # Llena la superficie con un color de fondo (puedes cambiarlo)
        self.static_background.draw(self.surface)

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)

        self.player.draw(self.surface)

        # Dibuja la superficie en la pantalla
        screen.blit(self.surface, (0, 0))

        ##########################

        # Dibujar balas del jugador
        for bullet in self.player.bullet_list:
            bullet.draw(screen)

        # Dibujar balas de los enemigos
        for enemy_element in self.enemy_list:
            for bullet in enemy_element.bullet_list:
                bullet.draw(screen)


##########################
