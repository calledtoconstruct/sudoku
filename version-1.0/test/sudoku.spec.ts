import { Engine } from '../src/sudoku';

const board = [
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

describe('given a non empty square', () => {
    const x = 0;
    const y = 0;
    let result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = Engine.evaluate(board, x, y);
        });

        it('stays the same', () => {
            expect(result).toBe(9);
        });
    });
});

describe('given an empty square and all but one value exist', () => {
    const x = 0;
    const y = 8;
    let result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = Engine.evaluate(board, x, y);
        });

        it('is the only option', () => {
            expect(result).toBe(2);
        });
    });
});

describe('given an empty square and only one option can not go elsewhere in sector', () => {
    const x = 8;
    const y = 4;
    let result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = Engine.evaluate(board, x, y);
        });

        it('is the only option', () => {
            expect(result).toBe(1);
        });
    });
});