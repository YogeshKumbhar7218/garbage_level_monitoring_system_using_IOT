jq(document).ready(function () {
  jq(".btndelete").click(function (event) {
    let dataf = jq(this).closest("form").serialize();
    jq.ajax({
      // The URL for the request
      url: /remove_feedback/,
      // Whether this is a POST or GET request
      data: dataf,

      type: "POST",
      // The type of data we expect back
      dataType: "html",
      success: function (data) {
        console.log("success called");
      },
    });
    jq(this)
      .closest(".card_container")
      .fadeOut(function () {
        jq(this).closest(".card_container").remove();
      });

    event.preventDefault();
  });
});
