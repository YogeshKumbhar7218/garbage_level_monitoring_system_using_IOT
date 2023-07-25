jq(document).ready(function () {
  jq("#new_employee").click(function (event) {
    let path = jq(this).attr("href");
    console.log(path);
    jq.ajax({
      url: path,
      type: "GET",
      dataType: "html",
      success: function (data) {
        jq(".Container").slideUp(function () {
          jq(".Container").html(data);
        });
        jq(".Container").slideDown();
      },
    });
    event.preventDefault();
  });

  jq(".emp_remove").click(function (event) {
    var path = jq(this).attr("href");
    console.log(path);
    jq.ajax({
      // The URL for the request
      url: path,
      // Whether this is a POST or GET request
      type: "GET",
      // The type of data we expect back
      dataType: "html",
      success: function (data) {
        console.log("success called");
      },
    });
    jq(this)
      .closest("tr")
      .fadeOut(function () {
        jq(this).closest("tr").remove();
      });

    event.preventDefault();
  });

  jq(".edit_employee").click(function (event) {
    let path = jq(this).attr("href");
    console.log(path);
    jq.ajax({
      url: path,
      type: "GET",
      dataType: "html",
      success: function (data) {
        jq(".Container").slideUp(function () {
          jq(".Container").html(data);
        });
        jq(".Container").slideDown();
      },
    });
    event.preventDefault();
  });
});
