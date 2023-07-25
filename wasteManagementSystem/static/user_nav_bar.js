
jq(document).ready(function () {
    
    console.log("ready");



    jq("#home").addClass("active");        

    jq("#feedback").click(function () {
        jq.ajax({
            url: '/user_feedback/',
            type: 'get',
            dataType: "html",
            success: function (data) {
                jq(".Container").slideUp(function () {
                    jq(".Container").html(data);
                });
                jq(".Container").slideDown();
                
            },
            complete: function (data) {
                console.log('complete');
            }
        });

        jq("#home").removeClass("active");
        jq(this).addClass("active"); 
    });
});