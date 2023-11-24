import pygame

""" from player import Player """
""" from enemigo import Enemy """
from constantes import *
from auxiliar import Auxiliar

import math


class Bullet:
    def __init__(
        self,
        owner,
        x_init,
        y_init,
        x_end,
        y_end,
        speed,
        path,
        frame_rate_ms,
        move_rate_ms,
        width=5,
        height=5,
    ) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        angle = math.atan2(
            y_end - y_init, x_end - x_init
        )  # Obtengo el angulo en radianes
        print("El angulo engrados es:", int(angle * 180 / math.pi))

        self.move_x = math.cos(angle) * speed
        self.move_y = math.sin(angle) * speed

        self.is_active = True

    def change_x(self, delta_x):
        self.x = self.x + delta_x
        self.rect.x = int(self.x)

    def change_y(self, delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)

    def do_movement(self, delta_ms, plataform_list, enemy_list, player_1):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.check_impact(enemy_list, player_1)

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            pass

    def check_impact(self, enemy_list, player_1):
        # Verifica la colisión con los enemigos
        if self.is_active:
            """for enemy_element in enemy_list:
            if (
                isinstance(enemy_element, Enemy)
                and self.owner != enemy_element
                and self.rect.colliderect(enemy_element.rect)
            ):
                print("IMPACTO ENEMY")
                self.is_active = False
                enemy_element.receive_shoot()
            """
        # Verifica la colisión con el jugador
        """ if (
            isinstance(player_1, Player)
            and self.owner != player_1
            and self.rect.colliderect(player_1.rect)
        ):
            print("IMPACTO PLAYER")
            self.is_active = False
            player_1.receive_shoot() """

    def update(self, delta_ms, plataform_list, enemy_list, player_1):
        self.do_movement(delta_ms, plataform_list, enemy_list, player_1)

        self.do_animation(delta_ms)

    def draw(self, screen):
        if self.is_active:
            if DEBUG:
                pygame.draw.rect(screen, color=(255, 0, 0), rect=self.rect)
            screen.blit(self.image, self.rect)
