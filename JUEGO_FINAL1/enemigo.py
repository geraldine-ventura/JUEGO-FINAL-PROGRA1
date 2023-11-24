from player import *
from constantes import *
from auxiliar import Auxiliar
from bullet import Bullet


class Enemy:
    def __init__(
        self,
        x,
        y,
        speed_walk,
        speed_run,
        gravity,
        jump_power,
        frame_rate_ms,
        move_rate_ms,
        jump_height,
        p_scale=1,
        interval_time_jump=100,
    ) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",
            0,
            7,
            scale=p_scale,
        )
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",
            0,
            7,
            flip=True,
            scale=p_scale,
        )
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",
            0,
            7,
            scale=p_scale,
        )
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",
            0,
            7,
            flip=True,
            scale=p_scale,
        )

        ##-----------dead-enemy-path---------->
        self.enemy_dead_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",
            0,
            6,
            flip=False,
            scale=p_scale,
        )
        self.enemy_dead_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",
            0,
            6,
            flip=True,
            scale=p_scale,
        )

        ##---------enemy_shoot_path----------->

        self.enemy_shoot_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",
            1,
            3,
            flip=False,
            scale=p_scale,
            repeat_frame=2,
        )
        self.enemy_shoot_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",
            1,
            3,
            flip=True,
            scale=p_scale,
            repeat_frame=2,
        )

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(
            x + self.rect.width / 3, y, self.rect.width / 3, self.rect.height
        )
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0  # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    # receive_shoot(Enemy):------------------>
    def receive_shoot(self, direction, enemy_shoot_rect):
        print("Función receive_shoot llamada")
        print("enemy_shoot_rect:", enemy_shoot_rect)

        if self.ground_collition_rect.colliderect(enemy_shoot_rect):
            print("Coalision con enemigo detectada!cambia de animacion dead")
            if direction == DIRECTION_R:
                self.animation = self.enemy_dead_r
            else:
                self.animation = self.enemy_dead_l
            # self.reset_animation()  # Restablece la animación después de cambiarla

    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0

            if not self.is_on_plataform(plataform_list):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0

    def is_on_plataform(self, plataform_list):
        retorno = False

        if self.ground_collition_rect.bottom >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in plataform_list:
                if self.ground_collition_rect.colliderect(
                    plataforma.ground_collition_rect
                ):
                    retorno = True
                    break
        return retorno

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
                # print(self.frame)
            else:
                self.frame = 0

    def update(self, delta_ms, plataform_list):
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms)

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, color=(255, 0, 0), rect=self.collition_rect)
            pygame.draw.rect(
                screen, color=(255, 255, 0), rect=self.ground_collition_rect
            )

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

    def receive_shoot(self):
        self.lives -= 1
