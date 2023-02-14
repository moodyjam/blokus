let piece = [[1,0],[1,1]];
let rotation = 0; // keep track of current rotation

document.addEventListener('keydown', function(event) {
  if (event.code === 'Space') {
    // rotate piece 90 degrees clockwise
    rotation = (rotation + 90) % 360;
    fetch('/rotate-piece', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        piece: piece,
        angle: rotation
      })
    })
    .then(response => response.json())
    .then(data => {
      piece = data;
      renderPiece(piece, rotation);
    });
  } else if (event.code === 'ArrowLeft') {
    // flip piece horizontally
    fetch('/flip-piece', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        piece: piece,
        direction: 'horizontal'
      })
    })
    .then(response => response.json())
    .then(data => {
      piece = data;
      renderPiece(piece, rotation);
    });
  } else if (event.code === 'ArrowRight') {
    // flip piece vertically
    fetch('/flip-piece', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        piece: piece,
        direction: 'vertical'
      })
    })
    .then(response => response.json())
    .then(data => {
      piece = data;
      renderPiece(piece, rotation);
    });
  }
});

function renderPiece(piece, rotation) {
  // render the piece on the grid with the given rotation
  // ...
}
