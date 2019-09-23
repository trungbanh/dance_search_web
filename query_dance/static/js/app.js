$(document).ready( function(){
    var query_data = {
        'body':'',
        'hand':'',
        'foot':''
    }
    $('#btn-check').click( function(){
        var bodys = document.getElementsByName('q-body');
        var lenght_b = bodys.length
        
        for (var i_b = 0; i_b<lenght_b; i_b++ ){
            if (bodys[i_b].checked) {
                query_data.body = bodys[i_b].value
            }
        }
        var hands = document.getElementsByName('q-hand');
        var lenght_h = hands.length
        
        for (var i_h = 0; i_h<lenght_h; i_h++ ){
            if (hands[i_h].checked) {

                query_data.hand = hands[i_h].value
            }
        }

        var foots = document.getElementsByName('q-foot');
        var lenght_f = foots.length
        
        for (var i_f = 0; i_f<lenght_f; i_f++ ){
            if (foots[i_f].checked) {
                query_data.foot = foots[i_f].value
            }
        }
        document.getElementById('q-text').innerHTML = query_data.body + " "+ query_data.hand +" "+ query_data.foot
    })

    $('#btn-search').click( function() {
    
        $.ajax({
            type: "post",
            url: '/Apsara',
            data: query_data,
            success: function(res,req) {
                console.log(req)
                console.log(res)

                $("#video").attr('src',"static/videos/cut"+res+".mp4" )
            }
        });
    })
})