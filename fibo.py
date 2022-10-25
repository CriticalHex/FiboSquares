import pygame

pygame.init()


def color(iter: int):
    return iter * 6, iter * 8, iter * 12


def main() -> None:
    screen = pygame.display.set_mode((800, 800))
    running = True
    clock = pygame.time.Clock()

    n = 2
    fib_1 = 0
    fib_2 = 1
    fibo = 0

    rects: list[tuple[int, int, int], pygame.Rect] = []
    rects.append([color(n), pygame.Rect(400, 400, fibo, fibo)])

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False
            if keys[pygame.K_LSHIFT]:
                if n <= 2:
                    fibo = n - 1
                else:
                    fibo = fib_1 + fib_2
                    fib_1 = fib_2
                    fib_2 = fibo
                match n % 4:
                    case 0:
                        gen = pygame.Rect(0, 0, fibo, fibo)
                        gen.bottomleft = rects[-1][1].bottomright
                        rects.append([color(n), gen])
                    case 1:
                        gen = pygame.Rect(0, 0, fibo, fibo)
                        gen.bottomright = rects[-1][1].topright
                        rects.append([color(n), gen])
                    case 2:
                        gen = pygame.Rect(0, 0, fibo, fibo)
                        gen.topright = rects[-1][1].topleft
                        rects.append([color(n), gen])
                    case 3:
                        gen = pygame.Rect(0, 0, fibo, fibo)
                        gen.topleft = rects[-1][1].bottomleft
                        rects.append([color(n), gen])

                n += 1
                print(fibo)

        screen.fill((0, 0, 0))

        for r in rects:
            pygame.draw.rect(screen, *r)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
