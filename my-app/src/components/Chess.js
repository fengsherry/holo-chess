import { useState } from 'react';
import { Chessboard } from 'react-chessboard';
import Chess from 'chess.js';
function App() {
  const [game, setGame] = useState(new Chess());
  
  // perform modify function on game state
  function safeGameMutate(modify) {
    setGame((g) => {
      const update = { ...g };
      modify(update);
      return update;
    });
  }
  // make computer move
  function makeRandomMove() {
    const possibleMoves = game.moves();
    // exit if the game is over
    if (game.game_over() || game.in_draw() || possibleMoves.length === 0) return;
    // select random move
    const randomIndex = Math.floor(Math.random() * possibleMoves.length);
    // play random move
    safeGameMutate((game) => {
      game.move(possibleMoves[randomIndex]);
    });
  }
  // perform action when piece dropped by user
  function onDrop(sourceSquare, targetSquare) {
    // attempt move
    let move = null;
    safeGameMutate((game) => {
      move = game.move({
        from: sourceSquare,
        to: targetSquare,
        promotion: 'q'
      });
    });
    
    // illegal move made
    if (move === null) return false;
    // valid move made, make computer move
    setTimeout(makeRandomMove, 200);
    return true;
  }
  return <Chessboard position={game.fen()} onPieceDrop={onDrop} />;
}
export default App;