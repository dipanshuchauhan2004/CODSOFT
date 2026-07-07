let board=[];

let currentPlayer=PLAYER;

let gameOver=false;

let playerScore=0;

let aiScore=0;

let drawScore=0;

const cells=document.querySelectorAll(".cell");

const status=document.getElementById("status");

const restartBtn=document.getElementById("restartBtn");

const newGameBtn=document.getElementById("newGameBtn");

function initializeGame(){

    board=["","","","","","","","",""];

    currentPlayer=PLAYER;

    gameOver=false;

    status.innerHTML="Your Turn";

    cells.forEach(cell=>{

        cell.innerHTML="";

        cell.classList.remove("win");

        cell.addEventListener("click",handleMove);

    });

}

function handleMove(e){

    if(gameOver)return;

    let index=e.target.dataset.index;

    if(board[index]!="")return;

    board[index]=PLAYER;

    renderBoard();

    let result=checkWinner(board);

    if(result){

        finishGame(result);

        return;

    }

    if(isDraw(board)){

        finishDraw();

        return;

    }

    status.innerHTML="AI Thinking...";

    setTimeout(aiMove,500);

}

restartBtn.onclick=initializeGame;

newGameBtn.onclick=()=>{

    playerScore=0;

    aiScore=0;

    drawScore=0;

    updateScore();

    initializeGame();

};