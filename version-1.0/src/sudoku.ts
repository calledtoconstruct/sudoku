
export class Engine {
    static empty(board: Array<number>, x: number, y: number): boolean {
        return board[y * 9 + x] === 0;
    }

    static limit(options: Array<number>, board: Array<number>, x: number, y: number): Array<number> {
        if (!Engine.empty(board, x, y)) {
            return options.filter((option: number): boolean => {
                return board[y * 9 + x] !== option;
            });
        } else {
            return options;
        }
    }

    static sector(x: number, y: number): { x: number, y: number } {
        const sector = {
            x: Math.floor(x / 3) * 3,
            y: Math.floor(y / 3) * 3
        };

        return sector;
    }

    static traverse(action: (a: number) => void): void {
        for (let a = 0; a < 9; ++a) {
            action(a);
        }
    }

    static scan(sector: { x: number, y: number }, action: (a: number, b: number) => void): void {
        for (let b = sector.y; b < sector.y + 3; ++b) {
            for (let a = sector.x; a < sector.x + 3; ++a) {
                action(a, b);
            }
        }
    }

    static options(board: Array<number>, x: number, y: number): Array<number> {
        let options = [1, 2, 3, 4, 5, 6, 7, 8, 9];

        Engine.traverse((a: number) => options = Engine.limit(options, board, a, y));
        Engine.traverse((a: number) => options = Engine.limit(options, board, x, a));

        const sector = Engine.sector(x, y);

        Engine.scan(sector, (a: number, b: number) => options = Engine.limit(options, board, a, b));

        return options;
    }

    static evaluate(board: Array<number>, x: number, y: number) {
        if (!Engine.empty(board, x, y)) {
            return board[y * 9 + x];
        }

        let options = Engine.options(board, x, y);

        if (options.length === 1) {
            return options[0];
        }

        const sector = Engine.sector(x, y);

        Engine.scan(sector, (a: number, b: number) => {
            if (a !== x || b !== y) {
                if (Engine.empty(board, a, b)) {
                    const elsewhere = Engine.options(board, a, b);
                    elsewhere.forEach((c: number): void => {
                        options = options.filter((d: number): boolean => c !== d);
                    });
                }
            }
        });

        if (options.length === 1) {
            return options[0];
        }

        return 0;
    }
}
