import { Board, Engine, Result, VerticalHandler, HorizontalHandler } from './sudoku';

const easy: Board = new Board([
    9, 0, 6, 3, 4, 0, 8, 1, 0,
    0, 5, 1, 7, 0, 0, 3, 0, 0,
    4, 7, 0, 0, 9, 1, 0, 0, 5,

    0, 0, 0, 9, 0, 3, 0, 0, 2,
    0, 0, 2, 0, 8, 7, 0, 0, 0,
    1, 0, 7, 2, 0, 0, 6, 0, 0,

    0, 8, 5, 0, 0, 9, 1, 0, 0,
    0, 3, 4, 0, 6, 0, 0, 0, 9,
    0, 1, 0, 5, 0, 8, 7, 0, 6,
], 3, 3);

const hard: Board = new Board([
    0, 0, 0, 2, 4, 7, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 7, 0,
    1, 9, 7, 0, 0, 3, 5, 0, 0,

    0, 0, 0, 0, 0, 1, 0, 0, 3,
    0, 5, 0, 0, 0, 0, 0, 6, 0,
    0, 0, 0, 0, 0, 0, 9, 0, 8,

    6, 0, 5, 0, 0, 0, 0, 0, 4,
    0, 3, 0, 9, 0, 8, 0, 0, 0,
    0, 0, 9, 0, 7, 0, 3, 0, 0,
], 3, 3);

const expert: Board = new Board([
    0, 0, 0, 0, 3, 0, 0, 0, 0,
    1, 2, 0, 7, 4, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 4,

    0, 0, 5, 0, 0, 0, 7, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 3, 0, 0, 6, 1, 0, 2, 8,

    0, 0, 0, 9, 0, 0, 0, 0, 2,
    4, 6, 0, 0, 0, 0, 8, 3, 0,
    0, 0, 7, 0, 0, 0, 0, 0, 9,
], 3, 3);

const silly: Board = new Board([
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0,

    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0,

    0, 0, 0, 9, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
], 3, 3);

const large: Board = new Board([
     1,  2,  0,  0,   0,  0,  0,  3,   0,  0,  6,  0,
     0,  5,  0,  8,   0,  7,  6,  0,  11,  0,  0,  0,
     0,  0, 12,  4,   0,  0, 10,  0,   0,  9,  0,  0,

     0,  0,  0,  0,   0,  0,  2,  0,   0,  0,  0,  0,
     0, 11,  0,  0,   0,  0,  0,  0,  10,  0,  0,  5,
     0,  7,  4,  0,   0,  0,  0,  0,   0,  0,  8,  0,

    10,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     2,  0,  0,  0,   0,  0,  0,  0,   0,  0,  7,  0,
     0,  3,  9,  8,   0,  0, 12,  0,   4,  0,  5,  6,

     9,  0,  5,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     0,  0,  0,  0,  11,  0,  0,  0,   0, 12,  0,  0,
     6,  0,  0,  0,   0,  0,  8,  0,   2,  0,  0,  7,
], 4, 3);

const huge: Board = new Board([
     1,  0,  0,  0,   0,  0,  0,  3,   0,  0,  0,  0,   0,  0,  0, 14,
     0,  0,  0,  8,   0,  7,  0,  0,  14,  0,  0,  0,   0,  0,  5,  0,
     0,  0, 12,  0,   0,  0,  0,  0,   0,  9,  0,  0,  13,  0,  0,  0,
    16,  0,  0,  0,   0,  0, 12,  0,   0,  0,  0,  6,   0,  0,  0,  0,

     0,  0,  0,  0,   0,  0,  2,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     0, 11,  0,  0,   0,  0,  0,  0,  15,  0,  0,  0,   0,  0,  0,  0,
     0,  0,  0,  0,   0,  0,  0,  0,   0,  0,  8,  0,   5,  0, 11,  0,
     0,  0,  7,  4,  15,  0,  0,  9,   0,  0,  0,  0,   0,  0,  0,  0,

    10,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     0,  0,  0,  0,   0,  0,  0,  0,   0,  0,  7,  0,   6,  0,  0,  0,
     0,  3, 13,  0,   0,  0, 15,  0,   4,  0,  0,  0,   0,  0,  0, 10,
     0,  0,  0,  0,   5,  0,  0,  0,   0,  6,  0, 11,   0,  0,  0,  0,

     9,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,   0, 10,  0,  0,
     0,  0,  0,  0,  11,  0,  0,  0,   0, 12,  0,  0,   2,  0,  0,  0,
     6,  0,  0,  0,   0,  0,  8,  0,   2,  0,  0,  7,   0,  0, 14,  0,
     4,  0,  0, 16,   0,  0,  0,  0,   0,  0,  0,  0,   3,  0,  0,  0,
], 4, 4);

class Guess {
    private option: number = 0;
    constructor(
        private readonly x: number,
        private readonly y: number,
        private readonly options: Array<number>
    ) { }

    next(): boolean {
        if (this.option < this.options.length - 1) {
            ++this.option;
            return true;
        } else {
            return false;
        }
    }

    apply(board: Board): void {
        // tslint:disable-next-line:max-line-length
        console.log(`guessing option ${this.option} of ${this.options.length} by applying ${this.options[this.option]} to ${this.x}, ${this.y}`);
        board.set(this.x, this.y, this.options[this.option]);
    }

    undo(board: Board): void {
        console.log(`undoing ${this.x}, ${this.y}`);
        board.set(this.x, this.y, 0);
    }
}

class Unknown {
    constructor(
        readonly x: number,
        readonly y: number,
        readonly options: Array<number>
    ) { }
}

const board: Board = silly;
const engine: Engine = new Engine(board);
let attempt: number = 0;
let remaining: number;
let last: number;
let guessing: boolean = false;
let guess: Array<Guess> = new Array<Guess>();
const unknown: Array<Unknown> = new Array<Unknown>();
let invalid: boolean = false;

type PlayHandler = (x: number, y: number, play: Result) => void;
type StrategyMap = { [K: string]: PlayHandler };

const handleValidPlay: PlayHandler = (x: number, y: number, play: Result): void => {
    board.set(x, y, play.value);
    if (guessing) {
        guess.push(new Guess(x, y, new Array<number>()));
    }
};

const handleUnknownPlay: PlayHandler = (x: number, y: number, play: Result): void => {
    unknown.push(new Unknown(x, y, play.options));
};

const handleInvalidPlay: PlayHandler = (x: number, y: number, play: Result): void => {
    invalid = true;
};

const strategy: StrategyMap = {
    "valid": handleValidPlay,
    "unknown": handleUnknownPlay,
    "invalid": handleInvalidPlay
};

let line: string = '';

// ┌───┬┐│├┤┼└┴┘┘

const maximum: number = board.options.toString().length;

// tslint:disable-next-line:max-line-length
const draw: (left: string, separator: string, junction: string, right: string) => string = (left: string, separator: string, junction: string, right: string): string => {
    let line: string = '';
    for (let index: number = 0; index < board.options; ++index) {
        if (index === 0) {
            line += left;
        } else if (index % board.sector.width === 0) {
            line += junction;
        }
        for (let place: number = 0; place < maximum + 2; ++place) {
            line += separator;
        }
        if (index === board.options - 1) {
            line += right;
        }
    }
    return line;
};

let top: string = draw('┌', '─', '┬', '┐');
let middle: string = draw('├', '─', '┼', '┤');
let bottom: string = draw('└', '─', '┴', '┘');

const verticalLog: VerticalHandler = (y: number): void => {
    if (y === 0) {
        console.log(top);
    } else if (y % board.sector.height === 0) {
        console.log(middle);
    }
    console.log(line);
    line = '';
    if (y === board.options - 1) {
        console.log(bottom);
    }
};

const horizontalLog: HorizontalHandler = (x: number, y: number): void => {
    const current: number = board.get(x, y).toString().length;
    if (x === 0) {
        line += '│';
    } else if (x % board.sector.width === 0) {
        line += '│';
    }
    if (board.get(x, y) === 0) {
        for (let place: number = 0; place < maximum + 2; ++place) {
            line += ' ';//'∙';
        }
    } else {
        for (let place: number = 0; place < maximum + 1 - current; ++place) {
            line += ' ';
        }
        line += board.get(x, y);
        line += ' ';
    }
    if (x === board.options - 1) {
        line += '│';
    }
};

const evaluate: HorizontalHandler = (x: number, y: number): void => {
    const play: Result = engine.evaluate(x, y);
    if (strategy[play.result]) {
        strategy[play.result](x, y, play);
    }
};

do {
    console.log('\x1B[2J');

    ++attempt;
    unknown.splice(0, unknown.length);
    invalid = false;
    board.scan(
        (y: number): void => verticalLog(y),
        (x: number, y: number): void => {
            evaluate(x, y);
            horizontalLog(x, y);
        }
    );

    remaining = board.remaining();
    console.log(`After ${attempt} attempts, ${remaining} remain.`);

    if (guessing && invalid) {
        console.log('reached a dead end!');
        while (guess.length > 0) {
            const current: Guess = guess.pop();
            current.undo(board);
            if (current.next()) {
                current.apply(board);
                guess.push(current);
                break;
            }
        }
        if (guess.length === 0) {
            console.log('guessing failed!');
            break;
        }
    } else if (last && last === remaining) {
        const canGuess: boolean = unknown.length > 0;
        if (canGuess) {
            unknown.sort((red: Unknown, green: Unknown): number => {
                const primary: number = green.options.length - red.options.length;
                if (primary !== 0) {
                    return primary;
                }
                const secondary: number = green.x - red.x;
                if (secondary !== 0) {
                    return secondary;
                }
                return green.y - red.y;
            });
            const best: Unknown = unknown[0];
            const current: Guess = new Guess(best.x, best.y, best.options);
            if (current.next()) {
                guessing = true;
                current.apply(board);
                guess.push(current);
            }
        } else {
            console.log('giving up!');
            break;
        }
    }
    last = remaining;
}
while (remaining > 0);
