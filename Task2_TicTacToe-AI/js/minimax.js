// ============================================
// Minimax Algorithm with Alpha-Beta Pruning
// ============================================

function getBestMove(board) {

    let bestScore = -Infinity;
    let move = -1;

    for (let i = 0; i < 9; i++) {

        if (board[i] === "") {

            board[i] = AI;

            let score = minimax(board, 0, false, -Infinity, Infinity);

            board[i] = "";

            if (score > bestScore) {

                bestScore = score;
                move = i;

            }
        }
    }

    return move;
}

function minimax(board, depth, isMaximizing, alpha, beta) {

    let result = checkWinner(board);

    if (result !== null) {

        if (result.winner === AI)
            return 10 - depth;

        if (result.winner === PLAYER)
            return depth - 10;

    }

    if (isDraw(board))
        return 0;

    if (isMaximizing) {

        let bestScore = -Infinity;

        for (let i = 0; i < 9; i++) {

            if (board[i] === "") {

                board[i] = AI;

                let score = minimax(board, depth + 1, false, alpha, beta);

                board[i] = "";

                bestScore = Math.max(score, bestScore);

                alpha = Math.max(alpha, score);

                if (beta <= alpha)
                    break;

            }
        }

        return bestScore;

    } else {

        let bestScore = Infinity;

        for (let i = 0; i < 9; i++) {

            if (board[i] === "") {

                board[i] = PLAYER;

                let score = minimax(board, depth + 1, true, alpha, beta);

                board[i] = "";

                bestScore = Math.min(score, bestScore);

                beta = Math.min(beta, score);

                if (beta <= alpha)
                    break;

            }
        }

        return bestScore;

    }
}