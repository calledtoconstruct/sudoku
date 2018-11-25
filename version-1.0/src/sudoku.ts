

export class Result {
    constructor(
        readonly result: 'invalid' | 'valid' | 'known' | 'unknown',
        readonly value: number,
        readonly options: Array<number> = new Array<number>()
    ) {}
}

export class Engine {
    private static empty(board: Array<number>, x: number, y: number): boolean {
        return board[y * 9 + x] === 0;
    }

    private static limit(options: Array<number>, board: Array<number>, x: number, y: number): Array<number> {
        if (!Engine.empty(board, x, y)) {
            return options.filter((option: number): boolean => {
                return board[y * 9 + x] !== option;
            });
        } else {
            return options;
        }
    }

    private static sector(x: number, y: number): { x: number, y: number } {
        const sector: { x: number, y: number } = {
            x: Math.floor(x / 3) * 3,
            y: Math.floor(y / 3) * 3
        };

        return sector;
    }

    private static traverse(action: (a: number) => void): void {
        for (let a: number = 0; a < 9; ++a) {
            action(a);
        }
    }

    private static scan(sector: { x: number, y: number }, action: (a: number, b: number) => void): void {
        for (let b: number = sector.y; b < sector.y + 3; ++b) {
            for (let a: number = sector.x; a < sector.x + 3; ++a) {
                action(a, b);
            }
        }
    }

    private static options(board: Array<number>, x: number, y: number): Array<number> {
        let options: Array<number> = [1, 2, 3, 4, 5, 6, 7, 8, 9];

        Engine.traverse((a: number) => options = Engine.limit(options, board, a, y));
        Engine.traverse((a: number) => options = Engine.limit(options, board, x, a));

        const sector: { x: number, y: number } = Engine.sector(x, y);

        Engine.scan(sector, (a: number, b: number) => options = Engine.limit(options, board, a, b));

        return options;
    }

    static evaluate(board: Array<number>, x: number, y: number): Result {
        if (!Engine.empty(board, x, y)) {
            return new Result('known', board[y * 9 + x]);
        }

        const options: Array<number> = Engine.options(board, x, y);

        if (options.length === 1) {
            return new Result('valid', options[0]);
        }

        let community: Array<number> = [...options];

        const sector: { x: number, y: number } = Engine.sector(x, y);

        Engine.scan(sector, (a: number, b: number) => {
            if (a !== x || b !== y) {
                if (Engine.empty(board, a, b)) {
                    const elsewhere: Array<number> = Engine.options(board, a, b);
                    elsewhere.forEach((c: number): void => {
                        community = community.filter((d: number): boolean => c !== d);
                    });
                }
            }
        });

        if (community.length === 1) {
            return new Result('valid', community[0]);
        }

        let row: Array<number> = [...options];

        Engine.traverse((a: number): void => {
            if (a !== x) {
                if (Engine.empty(board, a, y)) {
                    const elsewhere: Array<number> = Engine.options(board, a, y);
                    elsewhere.forEach((b: number): void => {
                        row = row.filter((c: number): boolean => b !== c);
                    });
                }
            }
        });

        if (row.length === 1) {
            return new Result('valid', row[0]);
        }

        let column: Array<number> = [...options];

        Engine.traverse((a: number): void => {
            if (a !== y) {
                if (Engine.empty(board, x, a)) {
                    const elsewhere: Array<number> = Engine.options(board, x, a);
                    elsewhere.forEach((b: number): void => {
                        column = column.filter((c: number): boolean => b !== c);
                    });
                }
            }
        });

        if (column.length === 1) {
            return new Result('valid', column[0]);
        }

        const best: Array<Array<number>> = [ community, row, column, options ]
            .filter((value: Array<number>): boolean => value.length > 0)
            .sort((red: Array<number>, green: Array<number>): number => green.length - red.length);

        if (best.length > 0) {
            return new Result('unknown', 0, best[0]);
        }

        return new Result('invalid', 0);
    }
}
