jq(document).ready(function () {
  jq("#servererror").hide();
  jq("#submitbtn").click(function (event) {
    console.log("submit clkd");
    let dataf = jq("#addDustbin").serialize();
    jq("#servererror").hide();
    jq.ajax({
      url: "/add_smartbin/",
      data: dataf,
      type: "POST",
      dataType: "text",
      success: function (data) {
        console.log("ajax called");
        if (data == "1") {
          jq("#servererror").css("border", "2px solid #5df15d");
          jq("#servererror").text("Dustbin Added Successfully");
          jq("#servererror").show();
        } else {
          jq("#servererror").css("border", "2px solid red");
          jq("#servererror").text(data);
          jq("#servererror").show();
        }
      },
    });
    event.preventDefault();
  });
});
