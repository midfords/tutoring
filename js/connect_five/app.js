$(document).ready(function() {
    let board = $( ".board" )

    for ( var i = 0; i < 15; i++ ) {
        var row = $( '<tr />' )

        for ( var j = 0; j < 15; j++ ) {
            var piece = $( '<td />', { 
              class: 'piece'
            });

            piece.hover( function() {
                $( this ).css({ 'opacity' : 0.7 });
            }, function() {
                $( this ).css({ 'opacity' : 0 });
            });

            piece.click(function(e) {
                console.log( "click" );
            });

            piece.appendTo(row);
        }

        row.appendTo(board);
    }
});

