jq(document).ready(function () {
  // Submit button
  jq("#servererror").hide();
  jq("#submitbtn").click(function (event) {
    console.log("submit clkd");
    let link = jq("#addDustbin").attr("action");
    let dataf = jq("#addDustbin").serialize();
    jq("#servererror").hide();
    jq.ajax({
      url: link,
      data: dataf,
      type: "POST",
      dataType: "text",
      success: function (data) {
        console.log("ajax called");
        if (data == "1") {
          jq("#servererror").css("border", "2px solid #5df15d");
          jq("#servererror").text("smartbin Updated successfully!");
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
