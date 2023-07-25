
jq(document).ready(function () {
    
    console.log("ready");



    jq("#home").addClass("active");        

    jq("#employee").click(function () {
        jq.ajax({
            url: '/admin_employee/',
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
        jq("#smartbin").removeClass("active");
        jq("#feedback").removeClass("active");
        jq(this).addClass("active");
        
    });
    jq("#smartbin").click(function () {
        jq.ajax({
            url: '/admin_smartbin/',
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
        jq("#employee").removeClass("active");
        jq("#home").removeClass("active");
        jq("#feedback").removeClass("active");
        jq(this).addClass("active");
        
        
    });
    jq("#feedback").click(function () {
        jq.ajax({
            url: '/admin_feedback/',
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
        jq("#employee").removeClass("active");
        jq("#home").removeClass("active");
        jq("#smartbin").removeClass("active");
        jq(this).addClass("active");
        
        
    });
});