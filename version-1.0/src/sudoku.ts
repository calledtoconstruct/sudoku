
export class Engine {
    static limit(options: Array<number>, board: Array<number>, x: number, y: number): Array<number> {
        if (board[y * 9 + x] !== 0) {
            return options.filter((option: number): boolean => {
                return board[y * 9 + x] !== option;
            });
        } else {
            return options;
        }
    }

    static options(board: Array<number>, x: number, y: number): Array<number> {
        let options = [1, 2, 3, 4, 5, 6, 7, 8, 9];
        
        for (let x1 = 0; x1 < 9; ++x1) {
            options = Engine.limit(options, board, x1, y);
        }
        
        for (let y1 = 0; y1 < 9; ++y1) {
            options = Engine.limit(options, board, x, y1);
        }
        
        const sector = {
            x: Math.floor(x / 3) * 3,
            y: Math.floor(y / 3) * 3
        };

        for (let y1 = sector.y; y1 < sector.y + 3; ++y1) {
            for (let x1 = sector.x; x1 < sector.x + 3; ++x1) {
                options = Engine.limit(options, board, x1, y1);
            }
        }

        return options;
    }
    
    static evaluate(board: Array<number>, x: number, y: number) {
        if (board[y * 9 + x] !== 0) {
            return board[y * 9 + x];
        }

        const options = Engine.options(board, x, y); 

        if (options.length === 1) {
            return options[0];
        }

        return 0;
    }
}
