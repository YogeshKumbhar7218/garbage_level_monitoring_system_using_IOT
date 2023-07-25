// Document is ready
var jq = $.noConflict();
jq(document).ready(function () {
  // Submit button
  jq("#servererror2").hide();
  jq("#signinSubmitbtn").click(function (event) {
    console.log("submit clkd");

    let dataf = jq("#signinForm").serialize();
    jq("#servererror2").hide();
    jq.ajax({
      url: "/admin_login/",
      data: dataf,
      type: "POST",
      dataType: "text",
      success: function (data) {
        console.log("ajax called");
        if (data == "1") {
          jq(location).attr("href", "/admin_home_page/");
          // Go to user home page
        } else if (data == "2") {
          jq(location).attr("href", "/Employee_home_page/");
        } else {
          jq("#servererror2").css({
            border: "2px solid #ed6767b0",
            "background-color": "#ed6767b0",
          });
          jq("#servererror2").text(data);
          jq("#servererror2").show();
        }
      },
    });
    event.preventDefault();
  });
});
