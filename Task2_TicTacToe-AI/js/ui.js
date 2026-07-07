function renderBoard(){

    cells.forEach((cell,index)=>{

        cell.innerHTML=board[index];

    });

}

function finishGame(result){

    gameOver=true;

    result.combo.forEach(index=>{

        cells[index].classList.add("win");

    });

    if(result.winner===PLAYER){

        status.innerHTML="🎉 You Win";

        playerScore++;

    }

    else{

        status.innerHTML="🤖 AI Wins";

        aiScore++;

    }

    updateScore();

}

function finishDraw(){

    gameOver=true;

    status.innerHTML="Draw Game";

    drawScore++;

    updateScore();

}

function updateScore(){

    document.getElementById("playerScore").innerHTML=playerScore;

    document.getElementById("aiScore").innerHTML=aiScore;

    document.getElementById("drawScore").innerHTML=drawScore;

}