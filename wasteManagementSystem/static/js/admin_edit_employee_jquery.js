// Document is ready
jq(document).ready(function () {
  // Validate phone number
  jq("#contactcheck").hide();
  let contactError = true;
  jq("#contact").keyup(function () {
    validateContact();
  });
  function validateContact() {
    let regex = /^\d{10}$/;
    let contactValue = jq("#contact").val();

    if (!regex.test(contactValue)) {
      jq("#contactcheck").show();
      contactError = false;
      return false;
    } else {
      jq("#contactcheck").hide();
      contactError = true;
    }
  }

  // Validate address
  jq("#addresscheck").hide();
  let addressError = true;
  jq("#address").keyup(function () {
    validateAddress();
  });
  function validateAddress() {
    let regex = /^[\w][ \w\.,]{3,98}[\w\.]$/i;
    let addressValue = jq("#address").val();
    if (!regex.test(addressValue)) {
      jq("#addresscheck").show();
      addressError = false;
      return false;
    } else {
      jq("#addresscheck").hide();
      addressError = true;
    }
  }

  // Validate fullname
  jq("#namecheck").hide();
  let nameError = true;
  jq("#name").keyup(function () {
    console.log("name");
    validateName();
  });
  function validateName() {
    let regex = /^[a-z][ a-z]{3,48}[a-z]$/i;
    let nameValue = jq("#name").val();
    if (!regex.test(nameValue)) {
      jq("#namecheck").show();
      nameError = false;
      return false;
    } else {
      jq("#namecheck").hide();
      nameError = true;
    }
  }

  // Validate Username
  jq("#usercheck").hide();
  let usernameError = true;
  jq("#usernames").keyup(function () {
    validateUsername();
  });

  function validateUsername() {
    let regex = /^[a-z\d]{5,12}$/i;
    let usernameValue = jq("#usernames").val();
    if (!regex.test(usernameValue)) {
      jq("#usercheck").show();
      usernameError = false;
      return false;
    } else {
      jq("#usercheck").hide();
      usernameError = true;
    }
  }

  // Validate Password
  jq("#passcheck").hide();
  let passwordError = true;
  jq("#password").keyup(function () {
    validatePassword();
  });
  function validatePassword() {
    let regex = /^[\w@-]{5,20}$/;
    let passwordValue = jq("#password").val();
    if (!regex.test(passwordValue)) {
      jq("#passcheck").show();
      passwordError = false;
      return false;
    } else {
      jq("#passcheck").hide();
      passwordError = true;
    }
  }

  // Validate Email
  const email = document.getElementById("email");
  email.addEventListener("blur", () => {
    let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
    let s = email.value;
    if (regex.test(s)) {
      email.classList.remove("is-invalid");
      emailError = true;
    } else {
      email.classList.add("is-invalid");
      emailError = false;
    }
  });

  // Submit button
  jq("#servererror").hide();
  jq("#submitbtn").click(function (event) {
    console.log("submit clkd");
    if (checkValidity()) {
      let dataf = jq("#myForm").serialize();
      jq("#servererror").hide();
      let link = jq("#myForm").attr("action");
      jq.ajax({
        url: link,
        data: dataf,
        type: "POST",
        dataType: "text",
        success: function (data) {
          console.log("ajax called");
          if (data == "1") {
            jq("#servererror").css("border", "2px solid #5df15d");
            jq("#servererror").text("Successfully Updated!");
            //jq("#servererror").slideUp();
            jq("#servererror").show();
            //jq("#servererror").slideDown();
          } else {
            jq("#servererror").css("border", "2px solid red");
            jq("#servererror").text(data);
            jq("#servererror").show();
          }
        },
      });
      event.preventDefault();
    } else {
      jq("#servererror").text("Your enterd data is invalide");
      event.preventDefault();
    }
  });

  function checkValidity() {
    validateContact();
    validateAddress();
    validateName();
    validateUsername();
    validatePassword();

    console.log("checking validity");
    console.log("contact " + contactError);
    console.log("address " + addressError);
    console.log("name " + nameError);
    console.log("username " + usernameError);
    console.log("pass " + passwordError);

    console.log(
      contactError == true &&
        addressError == true &&
        nameError == true &&
        usernameError == true &&
        passwordError == true
    );
    if (
      contactError == true &&
      addressError == true &&
      nameError == true &&
      usernameError == true &&
      passwordError == true
    ) {
      console.log("returning true");
      return true;
    } else {
      return false;
    }
  }
});