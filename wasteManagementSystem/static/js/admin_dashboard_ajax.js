var jq = $.noConflict();
function fetchdata() {
  jq.ajax({
    url: "/smart_bin_ajax/",
    type: "get",
    dataType: "json",
    success: function (data) {
      // console.log(data);

      data.forEach(function (value, index, array) {
        console.log(value.fields.dry_filled);
        jq("#" + value.pk + " .dry").text(
          "dry filled : " + value.fields.dry_filled + "%"
        );
        jq("#" + value.pk + " .wet").text(
          "wet filled : " + value.fields.wet_filled + "%"
        );
        if (value.fields.dry_filled > value.fields.wet_filled) {
          if (value.fields.dry_filled > 75) {
            jq("#" + value.pk + " .face2").css(
              "background",
              "linear-gradient(to top, red " +
                value.fields.dry_filled +
                "%, white 0%)"
            );
          } else {
            jq("#" + value.pk + " .face2").css(
              "background",
              "linear-gradient(to top, green " +
                value.fields.dry_filled +
                "%, white 0%)"
            );
          }
        } else {
          if (value.fields.wet_filled > 75) {
            jq("#" + value.pk + " .face2").css(
              "background",
              "linear-gradient(to top, red " +
                value.fields.wet_filled +
                "%, white 0%)"
            );
          } else {
            jq("#" + value.pk + " .face2").css(
              "background",
              "linear-gradient(to top, green " +
                value.fields.wet_filled +
                "%, white 0%)"
            );
          }
        }
      });
    },
    complete: function (data) {
      setTimeout(fetchdata, 5000);
    },
  });
}

jq(document).ready(function () {
  console.log("javascript runing");
  setTimeout(fetchdata, 5000);
  jq("#home").click(function () {
    console.log("clicked");
  });
});
