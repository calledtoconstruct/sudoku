import { Engine } from './sudoku';

const easy = [
    9, 0, 6,  3, 4, 0,  8, 1, 0, 
    0, 5, 1,  7, 0, 0,  3, 0, 0, 
    4, 7, 0,  0, 9, 1,  0, 0, 5, 
    
    0, 0, 0,  9, 0, 3,  0, 0, 2, 
    0, 0, 2,  0, 8, 7,  0, 0, 0, 
    1, 0, 7,  2, 0, 0,  6, 0, 0, 
    
    0, 8, 5,  0, 0, 9,  1, 0, 0, 
    0, 3, 4,  0, 6, 0,  0, 0, 9, 
    0, 1, 0,  5, 0, 8,  7, 0, 6, 
];

const hard = [
    0, 0, 0,  2, 4, 7,  0, 0, 0,
    0, 0, 0,  1, 0, 0,  0, 7, 0,
    1, 9, 7,  0, 0, 3,  5, 0, 0,

    0, 0, 0,  0, 0, 1,  0, 0, 3,
    0, 5, 0,  0, 0, 0,  0, 6, 0,
    0, 0, 0,  0, 0, 0,  9, 0, 8,

    6, 0, 5,  0, 0, 0,  0, 0, 4,
    0, 3, 0,  9, 0, 8,  0, 0, 0,
    0, 0, 9,  0, 7, 0,  3, 0, 0,
];

const expert = [
    0, 0, 0,  0, 3, 0,  0, 0, 0,
    1, 2, 0,  7, 4, 0,  0, 0, 0,
    0, 0, 0,  1, 0, 0,  0, 0, 4,

    0, 0, 5,  0, 0, 0,  7, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 1, 0,
    0, 3, 0,  0, 6, 1,  0, 2, 8,

    0, 0, 0,  9, 0, 0,  0, 0, 2,
    4, 6, 0,  0, 0, 0,  8, 3, 0,
    0, 0, 7,  0, 0, 0,  0, 0, 9,
];

const board = expert;
let attempt: number = 0;
let remaining: number;
let last: number;
do {
    ++attempt;
    console.log('---------');
    for (let y = 0; y < 9; ++y) {
        let line = '';
        for (let x = 0; x < 9; ++x) {
            const play: number = Engine.evaluate(board, x, y);
            if (play !== 0) {
                board[y * 9 + x] = play;
            }
            line += board[y * 9 + x];
        }
        console.log(line);
    }
    remaining = board.reduce((count: number, current: number): number => count + ((current === 0) ? 1 : 0), 0);
    if (last && last == remaining) {
        console.log('giving up!');
        break;
    }
    last = remaining;
    console.log(`After ${attempt} attempts, ${remaining} remain.`);
}
while (remaining > 0)