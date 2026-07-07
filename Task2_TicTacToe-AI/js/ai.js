function aiMove() {

    if (gameOver) return;

    const difficulty = document.getElementById("difficulty").value;

    let move;

    if (difficulty === "easy") {

        let empty = [];

        board.forEach((cell, index) => {

            if (cell === "")
                empty.push(index);

        });

        move = empty[Math.floor(Math.random() * empty.length)];

    }

    else if (difficulty === "medium") {

        if (Math.random() < 0.5) {

            let empty = [];

            board.forEach((cell, index) => {

                if (cell === "")
                    empty.push(index);

            });

            move = empty[Math.floor(Math.random() * empty.length)];

        }

        else {

            move = getBestMove(board);

        }

    }

    else {

        move = getBestMove(board);

    }

    board[move] = AI;

    renderBoard();

    let result = checkWinner(board);

    if (result) {

        finishGame(result);

        return;

    }

    if (isDraw(board)) {

        finishDraw();

        return;

    }

    status.innerHTML = "Your Turn";

}