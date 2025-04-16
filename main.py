from src.window import Window, Line, Point
from src.cell import Cell
def main():
    win = Window(800, 600)
    c = Cell(win)
    c.has_right_wall = False
    c.draw(50,50,100,100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom = False
    c2.draw(100,50,150,100)

    c.draw_move(c2)

    win.wait_for_close()


if __name__ == '__main__':
    main()