$(document).ready(function () {
  $("#signup-form").submit(function (event) {
    event.preventDefault();

    // var formData = $(this).serialize();

    var formData = {
      name: $('input[name="name"]').val(),
      email: $('input[name="email"]').val(),
      password: $('input[name="password"]').val(),
    };

    $.ajax({
      url: "/api/users/signup",
      type: "POST",
      data: formData,
      success: function (response) {
        console.log(response);
        alert("회원가입 성공");
        window.location.href = "/";
      },
      error: function () {
        alert("오류 발생");
      },
    });
  });
});
