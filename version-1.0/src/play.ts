import { Engine, Result } from './sudoku';

const easy: Array<number> = [
    9, 0, 6, 3, 4, 0, 8, 1, 0,
    0, 5, 1, 7, 0, 0, 3, 0, 0,
    4, 7, 0, 0, 9, 1, 0, 0, 5,

    0, 0, 0, 9, 0, 3, 0, 0, 2,
    0, 0, 2, 0, 8, 7, 0, 0, 0,
    1, 0, 7, 2, 0, 0, 6, 0, 0,

    0, 8, 5, 0, 0, 9, 1, 0, 0,
    0, 3, 4, 0, 6, 0, 0, 0, 9,
    0, 1, 0, 5, 0, 8, 7, 0, 6,
];

const hard: Array<number> = [
    0, 0, 0, 2, 4, 7, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 7, 0,
    1, 9, 7, 0, 0, 3, 5, 0, 0,

    0, 0, 0, 0, 0, 1, 0, 0, 3,
    0, 5, 0, 0, 0, 0, 0, 6, 0,
    0, 0, 0, 0, 0, 0, 9, 0, 8,

    6, 0, 5, 0, 0, 0, 0, 0, 4,
    0, 3, 0, 9, 0, 8, 0, 0, 0,
    0, 0, 9, 0, 7, 0, 3, 0, 0,
];

const expert: Array<number> = [
    0, 0, 0, 0, 3, 0, 0, 0, 0,
    1, 2, 0, 7, 4, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 4,

    0, 0, 5, 0, 0, 0, 7, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 3, 0, 0, 6, 1, 0, 2, 8,

    0, 0, 0, 9, 0, 0, 0, 0, 2,
    4, 6, 0, 0, 0, 0, 8, 3, 0,
    0, 0, 7, 0, 0, 0, 0, 0, 9,
];

const silly: Array<number> = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0,

    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0,

    0, 0, 0, 9, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
];

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

    apply(board: Array<number>): void {
        // tslint:disable-next-line:max-line-length
        console.log(`guessing option ${this.option} of ${this.options.length} by applying ${this.options[this.option]} to ${this.x}, ${this.y}`);
        board[this.y * 9 + this.x] = this.options[this.option];
    }

    undo(board: Array<number>): void {
        console.log(`undoing ${this.x}, ${this.y}`);
        board[this.y * 9 + this.x] = 0;
    }
}

class Unknown {
    constructor(
        readonly x: number,
        readonly y: number,
        readonly options: Array<number>
    ) { }
}

const board: Array<number> = silly;
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
    board[y * 9 + x] = play.value;
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

type VerticalHandler = (y: number) => void;
type HorizontalHandler = (x: number, y: number) => void;

// tslint:disable-next-line:max-line-length
const scan: (vertical: VerticalHandler, horizontal: HorizontalHandler) => void = (vertical: VerticalHandler, horizontal: HorizontalHandler): void => {
    for (let y: number = 0; y < 9; ++y) {
        for (let x: number = 0; x < 9; ++x) {
            horizontal(x, y);
        }
        vertical(y);
    }
};

let line: string = '';

const verticalLog: VerticalHandler = (y: number): void => {
    if (y === 0) {
        console.log('+---------+---------+---------+');
    } else if (y % 3 === 0) {
        console.log('+---------+---------+---------+');
    }
    console.log(line);
    line = '';
    if (y === 8) {
        console.log('+---------+---------+---------+');
    }
};

const horizontalLog: HorizontalHandler = (x: number, y: number): void => {
    if (x === 0) {
        line += '|';
    } else if (x % 3 === 0) {
        line += '|';
    }
    line += ' ';
    line += board[y * 9 + x];
    line += ' ';
    if (x === 8) {
        line += '|';
    }
};

const evaluate: HorizontalHandler = (x: number, y: number): void => {
    const play: Result = Engine.evaluate(board, x, y);
    if (strategy[play.result]) {
        strategy[play.result](x, y, play);
    }
};

do {
    ++attempt;
    unknown.splice(0, unknown.length);
    invalid = false;
    scan(
        (y: number): void => verticalLog(y),
        (x: number, y: number): void => {
            evaluate(x, y);
            horizontalLog(x, y);
        }
    );

    remaining = board.reduce((count: number, current: number): number => count + ((current === 0) ? 1 : 0), 0);
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
            unknown.sort((red: Unknown, green: Unknown): number => green.options.length - red.options.length);
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
