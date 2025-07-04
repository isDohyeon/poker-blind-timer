$(document).ready(function () {
  $("#login-form").submit(function (event) {
    event.preventDefault();

    var loginData = {
      email: $('input[name="login-email"]').val(),
      password: $('input[name="login-password"]').val(),
    };

    $.ajax({
      url: "/api/users/login",
      type: "POST",
      data: loginData,
      success: function (response) {
        console.log(response);
        alert("로그인 성공");
        window.location.href = "/";
      },
      error: function () {
        alert("오류 발생");
      },
    });
  });
});
