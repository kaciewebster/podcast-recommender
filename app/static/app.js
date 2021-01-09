let get_user_input = function() {
    let title = $("input#title").val()
    let num_recs = $("input#num_recs").val()
    return {'title': parseInt(title),
            'num_recs': parseInt(num_recs)}
};

let send_input_json = function(user_input) {
    $.ajax({
        url: '/recommend',
        contentType: "application/json; charset=utf-8",
        type: 'POST',
        success: function (data) {
            display_recommendations(data);
        },
        data: JSON.stringify(user_input)
    });
};

let display_recommendations = function(recommendation) {
    $("span#recommend").html(recommendation.a + ", " + recommendation.b + ", and " + recommendation.c)
};


$(document).ready(function() {

    $("button#solve").click(function() {
        let user_input = get_user_input();
        send_input_json(user_input);
    })

})