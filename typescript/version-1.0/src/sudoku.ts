

export type VerticalHandler = (y: number) => void;
export type HorizontalHandler = (x: number, y: number) => void;

export class Sector {
    private readonly options: number = this.width * this.height;

    constructor(
        readonly width: number,
        readonly height: number
    ) {
    }

    scan(sector: { x: number, y: number }, action: (a: number, b: number) => void): void {
        for (let b: number = sector.y; b < sector.y + this.height; ++b) {
            for (let a: number = sector.x; a < sector.x + this.width; ++a) {
                action(a, b);
            }
        }
    }
}
export class Board {
    readonly sector: Sector = new Sector(this.width, this.height);
    readonly options: number = this.width * this.height;

    constructor(
        readonly board: Array<number>,
        readonly width: number,
        readonly height: number
    ) {
        if (this.board.length !== Math.pow(this.options, 2)) {
            throw new Error('Invalid board configuration.');
        }
    }

    empty(x: number, y: number): boolean {
        return this.board[y * this.options + x] === 0;
    }

    matches(x: number, y: number, option: number): boolean {
        return this.board[y * this.options + x] === option;
    }

    traverse(action: (a: number) => void): void {
        for (let a: number = 0; a < this.options; ++a) {
            action(a);
        }
    }

    get(x: number, y: number): number {
        return this.board[y * this.options + x];
    }

    set(x: number, y: number, option: number): void {
        this.board[y * this.options + x] = option;
    }

    scan(vertical: VerticalHandler, horizontal: HorizontalHandler): void {
        for (let y: number = 0; y < this.options; ++y) {
            for (let x: number = 0; x < this.options; ++x) {
                horizontal(x, y);
            }
            vertical(y);
        }
    }

    remaining(): number {
        return this.board.reduce((count: number, current: number): number => count + ((current === 0) ? 1 : 0), 0);
    }
}

export class Result {
    constructor(
        readonly result: 'invalid' | 'valid' | 'known' | 'unknown',
        readonly value: number,
        readonly options: Array<number> = new Array<number>()
    ) {}
}

export class Engine {
    constructor(
        readonly board: Board
    ) {

    }

    private limit(options: Array<number>, x: number, y: number): Array<number> {
        if (!this.board.empty(x, y)) {
            return options.filter((option: number): boolean => {
                return !this.board.matches(x, y, option);
            });
        } else {
            return options;
        }
    }

    private sector(x: number, y: number): { x: number, y: number } {
        const sector: Sector = this.board.sector;
        return {
            x: Math.floor(x / sector.width) * sector.width,
            y: Math.floor(y / sector.height) * sector.height
        };
    }

    private options(x: number, y: number): Array<number> {
        let options: Array<number> = new Array<number>();
        this.board.traverse((a: number) => options.push(a + 1));

        this.board.traverse((a: number) => options = this.limit(options, a, y));
        this.board.traverse((a: number) => options = this.limit(options, x, a));

        const sector: { x: number, y: number } = this.sector(x, y);

        this.board.sector.scan(sector, (a: number, b: number) => options = this.limit(options, a, b));

        return options;
    }

    evaluate(x: number, y: number): Result {
        if (!this.board.empty(x, y)) {
            return new Result('known', this.board.get(x, y));
        }

        const options: Array<number> = this.options(x, y);

        if (options.length === 1) {
            return new Result('valid', options[0]);
        }

        let community: Array<number> = [...options];

        const sector: { x: number, y: number } = this.sector(x, y);

        this.board.sector.scan(sector, (a: number, b: number) => {
            if (a !== x || b !== y) {
                if (this.board.empty(a, b)) {
                    const elsewhere: Array<number> = this.options(a, b);
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

        this.board.traverse((a: number): void => {
            if (a !== x) {
                if (this.board.empty(a, y)) {
                    const elsewhere: Array<number> = this.options(a, y);
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

        this.board.traverse((a: number): void => {
            if (a !== y) {
                if (this.board.empty(x, a)) {
                    const elsewhere: Array<number> = this.options(x, a);
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
