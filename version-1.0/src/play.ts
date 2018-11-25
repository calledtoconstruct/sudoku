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

class Guess {
    private option: number = 0;
    constructor(
        private readonly x: number,
        private readonly y: number,
        private readonly options: Array<number>
    ) { }

    next(): boolean {
        if (this.option < this.options.length) {
            ++this.option;
            return true;
        } else {
            return false;
        }
    }

    apply(board: Array<number>): void {
        console.log(`applying ${this.options[this.option]} to ${this.x}, ${this.y}`);
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

const board: Array<number> = expert;
let attempt: number = 0;
let remaining: number;
let last: number;
let guessing: boolean = false;
let guess: Array<Guess> = new Array<Guess>();
do {
    ++attempt;
    const unknown: Array<Unknown> = new Array<Unknown>();
    let invalid: boolean = false;
    console.log('---------');
    for (let y: number = 0; y < 9; ++y) {
        let line: string = '';
        for (let x: number = 0; x < 9; ++x) {
            const play: Result = Engine.evaluate(board, x, y);
            if (play.result === 'valid') {
                board[y * 9 + x] = play.value;
                if (guessing) {
                    guess.push(new Guess(x, y, new Array<number>()));
                }
            } else if (play.result === 'unknown') {
                unknown.push(new Unknown(x, y, play.options));
            } else if (play.result === 'invalid') {
                invalid = true;
            }
            line += board[y * 9 + x];
        }
        console.log(line);
    }

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
        unknown.sort((red: Unknown, green: Unknown): number => green.options.length - red.options.length);
        if (canGuess) {
            console.log('guessing...');
            guessing = true;
            const current: Guess = new Guess(unknown[0].x, unknown[0].y, unknown[0].options);
            if (current.next()) {
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
