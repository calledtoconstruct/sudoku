/*
global describe, it, expect, beforeEach
*/
import { Board, Engine, Result } from '../src/sudoku';

const board: Board = new Board([
    9, 0, 6,  3, 4, 0,  8, 1, 0,
    0, 5, 1,  7, 0, 0,  3, 0, 0,
    4, 7, 0,  0, 9, 1,  0, 0, 5,

    0, 0, 0,  9, 0, 3,  0, 0, 2,
    0, 0, 2,  0, 8, 7,  0, 5, 0,
    1, 0, 7,  2, 0, 0,  6, 0, 0,

    0, 8, 5,  0, 0, 9,  1, 0, 0,
    0, 3, 4,  0, 6, 0,  0, 0, 9,
    0, 1, 0,  5, 0, 8,  7, 0, 6,
], 3, 3);

describe('given a non empty square', () => {
    const engine: Engine = new Engine(board);
    const x: number = 0;
    const y: number = 0;
    let result: Result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = engine.evaluate(x, y);
        });

        it('is known', () => {
            expect(result.result).toBe('known');
        });

        it('stays the same', () => {
            expect(result.value).toBe(9);
        });
    });
});

describe('given an empty square and all but one value exist', () => {
    const engine: Engine = new Engine(board);
    const x: number = 0;
    const y: number = 8;
    let result: Result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = engine.evaluate(x, y);
        });

        it('is valid', () => {
            expect(result.result).toBe('valid');
        });

        it('is the only option', () => {
            expect(result.value).toBe(2);
        });
    });
});

describe('given an empty square and only one option can not go elsewhere in sector', () => {
    const engine: Engine = new Engine(board);
    const x: number = 8;
    const y: number = 4;
    let result: Result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = engine.evaluate(x, y);
        });

        it('is valid', () => {
            expect(result.result).toBe('valid');
        });

        it('is the only option', () => {
            expect(result.value).toBe(1);
        });
    });
});

describe('given an empty square and only one option can not go elsewhere in row', () => {
    const engine: Engine = new Engine(board);
    const x: number = 0;
    const y: number = 3;
    let result: Result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = engine.evaluate(x, y);
        });

        it('is valid', () => {
            expect(result.result).toBe('valid');
        });

        it('is the only option', () => {
            expect(result.value).toBe(5);
        });
    });
});

const expert: Board = new Board([
    0, 0, 0,  0, 3, 0,  0, 0, 0,
    1, 2, 0,  7, 4, 0,  0, 0, 0,
    0, 0, 0,  1, 0, 0,  0, 0, 4,

    0, 0, 5,  0, 0, 0,  7, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 1, 0,
    0, 3, 0,  0, 6, 1,  0, 2, 8,

    7, 0, 0,  9, 0, 0,  0, 0, 2,
    4, 6, 0,  0, 0, 0,  8, 3, 0,
    9, 0, 7,  0, 0, 0,  0, 0, 9,
], 3, 3);

describe('given an empty square and there are four options', () => {
    const engine: Engine = new Engine(expert);
    const x: number = 6;
    const y: number = 1;
    let result: Result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = engine.evaluate(x, y);
        });

        it('is unknown', () => {
            expect(result.result).toBe('unknown');
        });

        it('has four options', () => {
            expect(result.options.length).toBe(4);
        });
    });
});

describe('given an empty square and no valid options exist', () => {
    const engine: Engine = new Engine(expert);
    const x: number = 0;
    const y: number = 5;
    let result: Result;
    describe('when evaluating', () => {
        beforeEach(() => {
            result = engine.evaluate(x, y);
        });

        it('is invalid', () => {
            expect(result.result).toBe('invalid');
        });
    });
});
