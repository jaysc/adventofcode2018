class Cart(object):
    # up, right, down, left = 0,1,2,3
    def __init__(self, x:int, y:int, direction:int):
        self.x = x;
        self.y = y;
        self.d = direction;
        self.nextIntersect = 1;
        self.explode = False;

    def move(self, grid:dict):
        if self.d == 0:
            self.y -= 1;
        elif self.d == 1:
            self.x += 1;
        elif self.d == 2:
            self.y += 1;
        elif self.d == 3:
            self.x -= 1;

        if (self.x,self.y) in grid:
            action = grid[(self.x,self.y)];
            if action is not None:
                if action == '\\':
                    if self.d == 0 or self.d == 2:
                        self.d -= 1;
                    else:
                        self.d += 1;
                elif action == '/':
                    if self.d == 0 or self.d == 2:
                        self.d += 1;
                    else:
                        self.d -= 1;
                elif action == '+':
                    if self.nextIntersect == 1:
                        self.d -= 1;
                    elif self.nextIntersect == 3:
                        self.d += 1;
                    self.nextIntersect = ((self.nextIntersect) % 3) + 1;
                self.d = self.d % 4;
grid = dict();
r = 0;
carts = set();
with open("input.txt", "r") as file:
    y = 0;
    for line in file.readlines():
        line = line.rstrip();
        row = list(line);

        if set(['v','<','>','^', '/','\\','\+']).intersection(set(row)):
            for x, c in enumerate(row):
                if c in ['-', ' ']:
                    continue;

                if c == '^':
                    carts.add(Cart(x,y,0));
                elif c == '>':
                    carts.add(Cart(x,y,1));
                elif c == 'v':
                    carts.add(Cart(x,y,2));
                elif c == '<':
                    carts.add(Cart(x,y,3));
                elif c in ['\\','/','+']:
                    grid[(x,y)] = c

        y += 1;

cartPositions = dict();
for tick in range(15000):
    cartExploded = False;
    for cart in sorted(carts, key = lambda cart: (cart.x,cart.y)):
        if not cart.explode:
            if (cart.x,cart.y) in cartPositions:
                del cartPositions[(cart.x,cart.y)];
            cart.move(grid);
            #print(cart.x,cart.y)

            if (cart.x,cart.y) not in cartPositions:
                cartPositions[(cart.x,cart.y)] = cart;
            else:
                # print(tick)
                # print("Crash at {}!!".format(list(cartPositions)[0]))
                cart.explode = True;
                cartPositions[(cart.x,cart.y)].explode = True;
                del cartPositions[(cart.x,cart.y)]
    
    if len([cart for cart in carts if not cart.explode]) == 1:
        print("last")
        break

for cart in carts:
    if not cart.explode:
        print(cart.x,cart.y)
    #print(sorted(list(cartPositions)[:]))
